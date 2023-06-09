# Watermarking app
This application allows you to add your watermark to an image through the use of a GUI, where your able to precisely position your watermark over the image, as well as configure its size, opacity and rotation. Lastly, once you're satisfied with the result, you're able to export the final, watermarked image.

## Getting started
1. Clone the repository:
```
git clone https://github.com/while-is-alex/watermark-generator.git
```

2. Change the directory to the project folder.

3. Create a virtual environment and activate it:
```
py -m venv venv
source venv/bin/activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Finally, to initialize the interface, run the `main.py` file. The app will launch and display the home screen.

![home-screen.png](https://i.ibb.co/QpXjvp5/home-screen.png)

## Features
### Watermark file selection
According to the instructions presented on screen, the user, first, should upload their watermark, which can be done by pressing the "upload watermark" button. The user will be prompted to select the path to their watermark (a .png file).

![selecting-watermark.png](https://i.ibb.co/jfQ17jZ/watermark-selection.png)

### Image file selection
Next, the user is prompted to select the path to the image to be watermarked. In order to properly fit the application window, the image preview is resized to a default value.

![selecting-image.png](https://i.ibb.co/KXsHYts/selecting-image.png)

### Watermark customization

Once both the watermark and the image have been selected, the user can fine-tune their watermark's parameters to reach their desired outcome.

![adjusting-watermark.png](https://i.ibb.co/nPMLhSb/adjusting-watermark.png)

### Saving

When the user is satisfied with the final product, they're able to export the watermarked image by click the "save" button. The user is then prompted to choose the destination path. The image is automatically converted to RGB before being exported.

![saving.png](https://i.ibb.co/rQKfNTK/saving.png)

## Requirements

This app requires the following:

+ Python 3
+ Tkinter
+ Pillow
