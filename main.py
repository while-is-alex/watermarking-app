from tkinter import *
from image_processing import ImageProcessing
from watermark import Watermarker

# Initializes the window
window = Tk()
window.title('Watermark Generator')
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(window, width=0, height=0)
canvas.grid(column=1, row=2, rowspan=15, columnspan=4)

# Classes
watermarker = Watermarker(canvas)
image = ImageProcessing(canvas, watermarker)

# Section: Main
main_text = Label(text='Add a watermark to your image:', font=('Courier', 20))
main_text.grid(column=1, row=0, columnspan=3, sticky=W)
instructions = Label(
    text='Upload your watermark as a PNG picture with a transparent background\nfirst and then load your image.',
    font=('Courier', 13)
)
instructions.config(justify=LEFT, height=5)
instructions.grid(column=1, row=1, columnspan=3)
upload = Button(window, text='Upload watermark', width=14, command=lambda: watermarker.upload_watermark())
upload.grid(column=3, row=18, sticky=E, pady=5)

# Section: Open and Save
open_file = Button(window, text='📂', width=3, command=lambda: image.upload_file())
open_file.grid(column=5, row=0, columnspan=2)
save_file = Button(window, text='💾', width=3, command=lambda: image.save_file())
save_file.grid(column=6, row=0, columnspan=2)

# Section: Move
move_text = Label(text='Watermark Position', font=('Courier', 15))
move_text.grid(column=5, row=1, columnspan=3)
up = Button(window, text='▲', width=3, command=lambda: [watermarker.change_y(-10), image.update_image()])
up.grid(column=6, row=2)
left = Button(window, text='◀︎', width=3, command=lambda: [watermarker.change_x(-10), image.update_image()])
left.grid(column=5, row=3)
right = Button(window, text='▶︎', width=3, command=lambda: [watermarker.change_x(10), image.update_image()])
right.grid(column=7, row=3)
down = Button(window, text='▼', width=3, command=lambda: [watermarker.change_y(10), image.update_image()])
down.grid(column=6, row=4)

# Section: Size
size = Label(text='Size', font=('Courier', 15))
size.grid(column=5, row=6, columnspan=3, pady=15)
size_up = Button(window, text='▲', width=3, command=lambda: [watermarker.change_size(10), image.update_image()])
size_up.grid(column=5, row=7, columnspan=2)
size_down = Button(window, text='▼', width=3, command=lambda: [watermarker.change_size(-10), image.update_image()])
size_down.grid(column=6, row=7, columnspan=2)

# Section: Opacity
opacity = Label(text='Opacity', font=('Courier', 15))
opacity.grid(column=5, row=9, columnspan=3, pady=15)
opacity_up = Button(window, text='▲', width=3, command=lambda: [watermarker.change_opacity(10), image.update_image()])
opacity_up.grid(column=5, row=10, columnspan=2)
opacity_down = Button(window, text='▼', width=3, command=lambda: [watermarker.change_opacity(-10), image.update_image()])
opacity_down.grid(column=6, row=10, columnspan=2)

# Section: Rotate
rotate = Label(text='Rotate', font=('Courier', 15))
rotate.grid(column=5, row=12, columnspan=3, pady=15)
rotate_right = Button(window, text='↻', width=3, command=lambda: [watermarker.rotate_right(), image.update_image()])
rotate_right.grid(column=5, row=13, columnspan=2)
rotate_left = Button(window, text='↺', width=3, command=lambda: [watermarker.rotate_left(), image.update_image()])
rotate_left.grid(column=6, row=13, columnspan=2)

# Keeps the window open
window.mainloop()
