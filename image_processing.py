from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image, ImageTk
import os


class ImageProcessing:
    def __init__(self, canvas, watermarker):
        """Initializes the parameters for the image."""
        self.path = ''
        self.pillow_image = Image.Image()
        self.tk_image = PhotoImage()
        self.canvas = canvas
        self.image = ''
        self.watermark = Image.Image()
        self.watermarker = watermarker

    def upload_file(self):
        """Prompts the user to select an image with one of the file types allowed.
        Calls the update_image method that will present the image in the GUI."""
        if not self.watermarker.watermark:
            messagebox.showinfo(message='Please select a watermark first, before selecting images.',
                                title='Select Images')
        else:
            f_types = [('jpeg', '.jpg .jpeg'), ('png', '.png'), ('bitmap', 'bmp'), ('gif', '.gif')]
            self.path = askopenfilename(filetypes=f_types)
            self.pillow_image = Image.open(self.path).convert('RGBA')
            self.update_image()

    def add_watermark(self):
        """Adds the watermark to the picture."""
        # Changes the size of the watermark
        new_watermark = self.watermarker.pillow_image.resize((self.watermarker.width, self.watermarker.height))

        # Repositions the watermark
        position = self.watermarker.x, self.watermarker.y

        # Changes the watermark's opacity
        self.watermarker.set_opacity()

        # Rotates the watermark
        new_watermark = new_watermark.rotate(self.watermarker.rotation, expand=True)

        # Pastes the watermark onto the image
        new_image = self.pillow_image.copy()
        new_image.paste(new_watermark, position, new_watermark)
        return new_image

    def update_image(self):
        """Updates the image on the canvas, including the watermark."""
        self.watermark = self.add_watermark()
        copy = self.watermark.copy()

        # Resizes the image to fit within the GUI
        width, height = copy.size
        if width > 500:
            multiplier = 500 / width
            new_width = int(width * multiplier)
            new_height = int(height * multiplier)
        if new_height > 500:
            multiplier = 500 / new_height
            new_width = int(new_width * multiplier)
            new_height = int(new_height * multiplier)
        image_resized = copy.resize((new_width, new_height))

        self.tk_image = ImageTk.PhotoImage(image_resized)
        self.canvas.delete('all')
        self.canvas.config(width=new_width, height=new_height)
        self.image = self.canvas.create_image(
            int(new_width / 2), int(new_height / 2),
            image=self.tk_image
        )

    def save_file(self):
        """Prompts the user to select a destination folder to save the final image."""
        if self.path and self.watermarker.path:
            directory = askdirectory(title='Please, select the save folder.')
            self.pillow_image = Image.open(self.path)
            final_image = self.add_watermark()
            save_path = f'{directory}/{os.path.basename(self.path)}'
            final_image.save(save_path)
            messagebox.showinfo(message='Your image has been saved!',
                                title='Save Successful')
        else:
            messagebox.showinfo(message='You haven\'t uploaded a watermark or an image.',
                                title="Error")
