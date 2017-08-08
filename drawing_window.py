import tkinter
import matplotlib.pyplot as plt
from ctypes import windll
from PIL import ImageGrab
# from display_image import display_image_from_vector
from predict import make_prediction
from process_image import process_image


class DrawingWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Character Recognition')
        self.bottom = tkinter.Frame(self.main_window)
        self.bottom.pack(side=tkinter.BOTTOM)
        self.create_canvas()
        self.create_submit_button()
        self.create_clear_button()
        self.create_text_widget()

    def get_coords(self):
        print(self.main_window.winfo_rootx())
        print(self.main_window.winfo_rooty())

    def create_canvas(self):
        canvas_width = 400
        canvas_height = 400
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=canvas_width,
                                     height=canvas_height)
        self.canvas.configure(background='white')
        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH,
                         padx=10,
                         pady=10)
        self.canvas.bind("<B1-Motion>", self.paint)

    def create_submit_button(self):
        self.button = tkinter.Button(master=self.main_window,
                                     text='Submit',
                                     font=('Helvetica', 12))
        self.button.pack(in_=self.bottom,
                         side=tkinter.LEFT,
                         padx=5,
                         pady=8)
        self.button.bind("<Button-1>", self.get_screenshot)
        self.button.bind("<ButtonRelease-1>", self.show_letter)

    def create_clear_button(self):
        self.button = tkinter.Button(master=self.main_window,
                                     text='Clear',
                                     font=('Helvetica', 12))
        self.button.pack(in_=self.bottom,
                         side=tkinter.RIGHT,
                         padx=5,
                         pady=8)
        self.button.bind("<ButtonRelease-1>", self.clear_drawing)

    def create_text_widget(self):
        self.text = tkinter.Text(master=self.main_window,
                                 width=40,
                                 height=2,
                                 font=('Helvetica', 14))
        self.text.pack(side=tkinter.BOTTOM, padx=10, pady=5)
        self.text.tag_configure('tag-center', justify='center')

    def paint(self, event):
        black = "#000000"
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_oval(x1, y1, x2, y2, fill=black)

    def get_screenshot(self, event):
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width() - 1
        y1 = y + self.canvas.winfo_height() - 1
        ImageGrab.grab(bbox=(x, y, x1, y1)).save('letter.png')

    def show_letter(self, event):
        # try:
        #     plt.close()
        # except:
        #     pass
        image = process_image('letter.png')
        # display_image_from_vector(image.flatten())
        pred, conf = make_prediction(image)
        self.text.configure(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        self.text.insert("end",
                         "Prediction: " + pred + \
                         '\nConfidence: ' + conf + '%',
                         'tag-center')
        self.text.configure(state=tkinter.DISABLED)
        plt.show(block=False)

    def clear_drawing(self, event):
        # try:
        #     plt.close()
        # except:
        #     pass
        self.canvas.delete('all')
        self.text.configure(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        self.text.configure(state=tkinter.DISABLED)

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    user32 = windll.user32
    user32.SetProcessDPIAware()
    window = DrawingWindow()
    window.run()
