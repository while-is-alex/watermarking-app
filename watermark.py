from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


class Watermarker:
    def __init__(self, canvas):
        """Initializes the parameters for the watermark."""
        self.path = ''
        self.pillow_image = Image.Image()
        self.tk_image = PhotoImage()
        self.canvas = canvas
        self.watermark = False
        self.width = 100
        self.height = 100
        self.x, self.y = (0, 0)
        self.opacity = 150
        self.rotation = 0

    def upload_watermark(self):
        """Prompts the user to select a file to be used as watermark (.png only)."""
        f_types = [('png', '.png')]
        self.path = askopenfilename(filetypes=f_types)
        self.pillow_image = Image.open(self.path).convert('RGBA')
        copy = self.pillow_image.copy()
        copy.thumbnail((200, 200))
        self.width, self.height = copy.size
        self.tk_image = ImageTk.PhotoImage(copy)
        self.canvas.delete('all')
        self.canvas.config(width=self.width, height=self.height)
        self.watermark = self.canvas.create_image(
            int(self.width / 2), int(self.height / 2),
            image=self.tk_image
        )

    def change_y(self, move):
        """Receives a positional argument of type integer in order to
        move the watermark on the Y axis."""
        if self.watermark:
            self.y = self.y + move

    def change_x(self, move):
        """Receives a positional argument of type integer in order to
        move the watermark on the X axis."""
        if self.watermark:
            self.x = self.x + move

    def change_size(self, change):
        """Receives a positional argument of type integer in order to
        alter the size of the watermark."""
        self.width = self.width + change
        self.height = self.height + change

    def set_opacity(self):
        """Sets the default opacity of the watermark."""
        alpha = self.pillow_image.getchannel('A')
        new_alpha = alpha.point(lambda i: self.opacity if i > 0 else 0)
        self.pillow_image.putalpha(new_alpha)

    def change_opacity(self, change):
        """Receives a positional argument of type integer in order to
        alter the opacity of the watermark."""
        self.opacity = self.opacity + change

    def rotate_right(self):
        """Rotates the watermark clockwise."""
        self.rotation = self.rotation - 10

    def rotate_left(self):
        """Rotates the watermark counterclockwise."""
        self.rotation = self.rotation + 10
