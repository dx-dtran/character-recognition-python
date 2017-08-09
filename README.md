# Character Recognition

## Introduction

This is an optical character recognition project written in Python using the NumPy, Matplotlib, and PIL libraries. Users draw a lowercase character into a GUI and an artificial neural network predicts what letter it is.

<p align="center">
<img src="https://github.com/dx-dtran/character-recognition-python/blob/master/images/example1.PNG" height="300"/>
<img src="https://github.com/dx-dtran/character-recognition-python/blob/master/images/example2.PNG" height="300"/>
<br>Correct predictions of two variations of 'k'
</p>

## Table of Contents
1. [Dependencies and Installation](#dependencies-and-installation)
2. [Limitations](#limitations)
3. [How It Works](#how-it-works)
    * [Making the dataset](#making-the-dataset)
    * [Creating the GUI](#creating-the-gui)
    * [Neural Networks](#the-neural-network)
4. [Known Issues](#known-issues)

## Dependencies and Installation

This project imports the NumPy, Matplotlib, PIL, ctypes, and tkinter libraries. Only ctypes and tkinter are pre-installed libraries from the Python Standard Library.

The easiest way to obtain NumPy, Matplotlib, and PIL is by [downloading and installing Anaconda 4.4.0](https://www.continuum.io/downloads) for **Python 3.6.** Anaconda comes with all these libraries (and many more) pre-installed.

Once Anaconda is installed, clone this repository to obtain the Python scripts:
```
$ git clone https://github.com/dx-dtran/character-recognition-python.git
```

Before running the scripts, make sure the custom Anaconda Python 3.6.1 interpreter is being used in your environment. For example, if you are opening the .py files in the PyCharm IDE, select Anaconda Python 3.6.1 from the list of interpreters. All import statements made in the scripts will now be recognized by the interpreter.

## Limitations

A tkinter.Canvas widget is used for letter drawing. Drawings from the Canvas need to be outputted to a .png file for the neural network to process the image data and predict a letter. Right now, the tkinter.Canvas widget's image file is obtained using a screenshot of the widget. Screenshots are done using the PIL library's ImageGrab function, which is currently only available for Windows. 

Furthermore, ImageGrab requires display settings to be at 100% resolution scaling; otherwise, it might grab a zoomed-in/zoomed-out image that may include a portion of the screen outside the widget's boundaries. To prevent the user from having to adjust display settings just to run ImageGrab, the windll function from the ctypes library is used to ignore resolution scaling. ctypes.windll is also only available for Windows.

ImageGrab also cannot take screenshots from any secondary monitors. Any screenshots taken on a second monitor will result in a black image.

## How It Works

Creating this project required four main steps:
1. Making a dataset of lowercase letters
2. Creating a GUI for users to draw characters
3. Training a neural network to the learn the dataset
4. Having that neural network predict unseen characters

### Making the dataset

The training dataset currently contains 3600 examples of lowercase letters. It is called [characterDataset.txt](https://github.com/dx-dtran/character-recognition-python/blob/master/data/characterDataset.txt) and can be found in the data directory of this repository.

2600 examples come from screenshots of 100 different Microsoft Word fonts (100 fonts per letter). The remaining 1000 examples are handwritten submissions from four people.

Each row in the dataset represents an example of a letter. The first 900 elements of each row are the pixel color values (1 for black, 0 for white) of a 30x30 image of a letter. The last 26 elements of each row represent a letter-classification vector, where the index of the number 1 is the index of the image's associated letter.

Each of the rows in the dataset has been obtained by processing pictures of letters through the [process_image.py](https://github.com/dx-dtran/character-recognition-python/blob/master/process_image.py) script. The script performs the following computations:
1. Removes any whitespace surrounding the letter
2. Resizes image down to a square, 30 by 30 pixel image
3. Performs binary-thresholding so the image’s pixel intensity/color data is reduced to 1’s and 0’s: 1 for black, 0 for white
4. Flattens the image into a 1 by 900 vector. The first 30 elements represent the first row of the image’s pixels, the next 30 represent the second row, etc.

### Creating the GUI

The letter drawing window contains four main main elements: a tkinter.Canvas object for drawing, and three tkinter.Button objects for predicting a letter, showing prediction data, and clearing the Canvas. 

The Canvas object tracks the user's cursor movements. When the user clicks and drags the cursor, a series of circles are drawn in the cursor's path. When the user submits the drawing for character recognition, the script takes a screenshot of the Canvas and saves it to a file.

### The Neural Network

This project uses a 3-layer neural network to learn and predict characters. 

To predict a character from an image, the neural network essentially takes a 1 by 900 vector of pixels and does two matrix multiplications to transform the image into a 1 by 26 letter-classification vector. Each element in the letter-classification vector is the probability of the image representing the corresponding letter.

To learn characters from a dataset, the neural network must determine the values of the two transformation matrices described above. This is done using the backpropagation and gradient descent algorithms. What this essentially boils down to is finding matrix values that minimize the difference between each image's pixel vector and its corresponding letter vector.

These backpropagation and gradient descent computations have been done in a separate MATLAB script not included in this repository. Instead, only the final matrix data is included and is stored in [weights1.txt](https://github.com/dx-dtran/character-recognition-python/blob/master/weights1.txt) and [weights2.txt](https://github.com/dx-dtran/character-recognition-python/blob/master/weights2.txt).

## Known Issues
