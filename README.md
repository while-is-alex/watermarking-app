# Watermarking app
This application allows you to add your watermark to an image through the use of a GUI, where your able to precisely position your watermark over the image, as well as configure its size, opacity and rotation. Lastly, once you're satisfied with the result, you're able to export the final, watermarked image.

## Getting started
1. Clone the repository:
```
git clone https://github.com/while-is-alex/watermark-generator.git
```

2. Change the directory to the project folder.

3. Create a virtual environment:
```
py -m venv venv
venv/Scripts/activate
```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Finally, to initialize the interface, run the `main.py` file. The app will launch and display the home screen.

![home-screen.png](https://i.ibb.co/QpXjvp5/home-screen.png)

## Features
### Watermark selection
According to the instructions presented on screen, the user, first, should upload their watermark, which can be done by pressing the "upload watermark" button. The user will be prompted to select the path to their watermark (a .png file).

![selecting-watermark.png](https://i.ibb.co/34Wdb6D/selecting-watermark.png)
