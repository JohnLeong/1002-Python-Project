from Tkinter import *
import tkFileDialog

class Application(Frame):
    CONST_APP_NAME = "1002 Python Project"
    CONST_WINDOW_MIN_WIDTH = 400
    CONST_WINDOW_MIN_HEIGHT = 300

    def __init__(self, master=None):
        self.selectedFileName = "No file selected"

        Frame.__init__(self, master)
        master.title(Application.CONST_APP_NAME)
        master.minsize(Application.CONST_WINDOW_MIN_WIDTH, Application.CONST_WINDOW_MIN_HEIGHT)
        #master.resizable(False, False)
        self.pack(anchor = "w", padx = (10, 10), pady = (10, 10))
        self.createWidgets()

    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.file_label = Label(self, text = "Selected file: ")
        self.file_label.grid(row = 0, column = 1)
        self.selected_file_label = Label(self, text = self.selectedFileName, anchor = "w")
        self.selected_file_label.grid(row = 0, column = 3, columnspan = "3")
        self.file_button = Button(self, text = "Select a file", command = self.selectFile)
        self.file_button.grid(row = 0, column = 0)

    def selectFile(self):
        self.selectedFileName = tkFileDialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.selected_file_label["text"] = self.selectedFileName
        print "Currently selected file: " + self.selectedFileName
        return self.selectedFileName
