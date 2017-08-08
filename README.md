# Character Recognition in Python

## Introduction

This is an optical character recognition project written in Python using the NumPy, Matplotlib, and PIL libraries. Users draw a lowercase character into a GUI and an artificial neural network predicts what letter it is.

## Table of Contents
1. [Dependencies and Installation](#dependencies-and-installation)
2. [Notes to the User](#warnings)
3. [How It Works](#how-it-works)
4. [Known Issues](#known-issues)

## Dependencies and Installation

This project imports the NumPy, Matplotlib, PIL, ctypes, and tkinter libraries. Only ctypes and tkinter are installed natively in Python 3.6.2 from the Python.org website.

The easiest way to obtain all five libraries is by downloading Anaconda 4.4.0. Anaconda comes with all five of these libraries (and many more) pre-installed.

Once Anaconda is installed, clone this repository to obtain the Python scripts:
```
$ git clone https://github.com/dx-dtran/character-recognition-python.git
```

Before running the scripts, make sure the custom Anaconda Python 3.6.1 interpreter is being used. For example, if you are opening the .py files in the PyCharm IDE, select Anaconda Python 3.6.1 from the list of interpreters. All import statements made in the scripts will now be recognized by the interpreter.

## Notes to the User

A tkinter.Canvas widget is used for letter drawing. Drawings from the Canvas need to be outputted to a .png file for the neural network to process the image data and predict a letter. Right now, the tkinter.Canvas widget's image file is obtained using a screenshot of the widget. Screenshots are done using the PIL library's ImageGrab function, which is currently only available for Windows. 

Furthermore, ImageGrab requires display settings to be at 100% resolution scaling; otherwise, it might grab a portion of the screen behind the widget. To prevent the user from having to adjust display settings just to run ImageGrab, the windll function from the ctypes library is used to ignore resolution scaling. ctypes.windll is also only available for Windows.

ImageGrab also cannot take screenshots from any secondary monitors. Any screenshots taken on a second monitor will result in a black image.

## How It Works

## Known Issues
