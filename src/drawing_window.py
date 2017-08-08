import tkinter
from ctypes import windll

import matplotlib.pyplot as plt
from PIL import ImageGrab
from predict import make_prediction
from process_image import process_image

from src.display_image import display_image_from_vector


class DrawingWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.create_canvas()
        self.create_submit_button()
        self.create_clear_button()

    def get_coords(self):
        print(self.main_window.winfo_rootx())
        print(self.main_window.winfo_rooty())

    def create_canvas(self):
        canvas_width = 400
        canvas_height = 400
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=canvas_width,
                                     height=canvas_height)
        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)

    def create_submit_button(self):
        self.button = tkinter.Button(master=self.main_window,
                                     text='Submit')
        self.button.pack(side=tkinter.BOTTOM)
        self.button.bind("<Button-1>", self.get_screenshot)
        self.button.bind("<ButtonRelease-1>", self.show_letter)

    def create_clear_button(self):
        self.button = tkinter.Button(master=self.main_window,
                                     text='Clear')
        self.button.pack(side=tkinter.BOTTOM)
        self.button.bind("<ButtonRelease-1>", self.clear_drawing)

    def paint(self, event):
        black = "#000000"
        x1, y1 = (event.x - 7), (event.y - 7)
        x2, y2 = (event.x + 7), (event.y + 7)
        self.canvas.create_oval(x1, y1, x2, y2, fill=black)

    def get_screenshot(self, event):
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width() - 1
        y1 = y + self.canvas.winfo_height() - 1
        print(x, y, x1, y1)
        ImageGrab.grab(bbox=(x, y, x1, y1)).save('letter.png')

    def show_letter(self, event):
        try:
            plt.close()
        except:
            pass
        image = process_image('letter.png')
        display_image_from_vector(image.flatten())
        make_prediction(image)
        plt.show(block=False)

    def clear_drawing(self, event):
        try:
            plt.close()
        except:
            pass
        self.canvas.delete('all')

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    user32 = windll.user32
    user32.SetProcessDPIAware()
    x = DrawingWindow()
    x.run()
