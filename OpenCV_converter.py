from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from shutil import copyfile

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Image converter for Computer Vision")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button()

    def button(self):
        """ Creating the buttons:"""

        # button to open file explorer
        self.button = ttk.Button(self.labelFrame, text="Browse Files", command=self.fileDialog)
        self.button.grid(column=1, row=1)

        # button to convert file using GaussianBlur()
        self.button_convert = Button(self, text="Convert File! (Gaus)", command=self.convertPhotoGaus)
        self.button_convert.grid(row=3, column=1)

        # button to convert file using threshold()
        self.button_thres = Button(self, text="Convert File! (Threshold)", command=self.convertPhotoThres)
        self.button_thres.grid(row=4, column=1)

        # button to rotate the chosen image, if not displayed in portrait
        self.button_rotate = Button(self, text="Rotate image", command=self.rot_img)
        self.button_rotate.grid(row=5, column=0)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(title="Select A File",
                                                   filetype=(("jpg files", "*.jpg"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)

        img = Image.open(self.filename)
        img_final = img.resize((250, 250))  # shrinking the image to a set number of pixels
        photo = ImageTk.PhotoImage(img_final)

        self.label2 = Label(image=photo)
        self.label2.image = photo
        self.label2.grid(column=0, row=4)

    def rot_img(self):
        img = Image.open(self.filename)
        img_rotated = img.transpose(Image.ROTATE_270)  # rotating the image if not correctly shown
        img_final = img_rotated.resize((250, 250))
        photo = ImageTk.PhotoImage(img_final)

        self.label2 = Label(image=photo)
        self.label2.image = photo
        self.label2.grid(column=0, row=4)

    def convertPhotoGaus(self):

        copyfile(self.filename, "ph_copy.jpg")
        copied_ph = cv2.imread("ph_copy.jpg")

        gray_ph = cv2.cvtColor(copied_ph, cv2.COLOR_BGR2GRAY)  # graying out the original photo

        # applying the GaussianBlur() function
        gaussianBlur_ph = cv2.GaussianBlur(gray_ph, (31, 31), 0)
        cv2.imwrite("Gray_me_final.jpg", gaussianBlur_ph)

        img2 = Image.open("Gray_me_final.jpg")
        img2 = img2.resize((250, 250))
        photo2 = ImageTk.PhotoImage(img2)

        self.label_converted = Label(image=photo2)
        self.label_converted.image = photo2
        self.label_converted.grid(column=2, row=4)

        self.label_info = Label(text="This photo was converted to gray and \n"
                                     "the GaussianBlur() function was applied to the image\n"
                                     "ready for CV experiments :)")
        self.label_info.grid(row=5, column=2)

        cv2.destroyAllWindows()

    def convertPhotoThres(self):

        copyfile(self.filename, "ph_copy.jpg")
        copied_ph = cv2.imread("ph_copy.jpg")

        gray_ph = cv2.cvtColor(copied_ph, cv2.COLOR_BGR2GRAY)  # graying out the original photo

        # applying the threshold() function for pixel intensity
        thres_ph = cv2.threshold(gray_ph, 120, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite("thres_me_final.jpg", thres_ph)

        img2 = Image.open("thres_me_final.jpg")
        img2 = img2.resize((250, 250))
        photo2 = ImageTk.PhotoImage(img2)

        self.label_converted = Label(image=photo2)
        self.label_converted.image = photo2
        self.label_converted.grid(column=2, row=6)



        self.label_info = Label(text="This photo was converted to gray and \n"
                                     "the threshold function was applied to the image\n"
                                     "ready for CV experiments :)")
        self.label_info.grid(row=7, column=2)

        cv2.destroyAllWindows()

root = Root()
root.mainloop()
