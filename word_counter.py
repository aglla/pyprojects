#GUI Word Counter

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        menubar.add_command(label = 'quit', command = root.quit)
        root.config(menu = menubar)
        self.label1 = Label(self, text = 'Paste your text below')
        self.label1.grid(row = 0, column = 2)

        self.text1 = Text(self, width = 60, height = 30)
        self.text1.grid(row=2, column = 2)

        self.button1 = Button(self, text = 'Submit', command = self.convert)
        self.button1.grid(row=3,column = 0)
        self.button2 = Button(self, text = 'Clear', command = self.clear)
        self.button2.grid(row=3, column = 6)

        self.label2 = Label(self, text = 'Words:')
        self.label2.grid(row = 5, column = 0)
        self.entry1 = Entry(self)
        self.entry1.grid(row = 6, column = 0)

    def convert(self):
        userText = self.text1.get("1.0", END)
        wordList = userText.split()
        number_of_words = len(wordList)
        self.entry1.delete(0, END)
        self.entry1.insert(END, number_of_words) 

    def clear(self):
        self.text1.delete("1.0", END)
        self.entry1.delete(0, END)
        
                           
root = Tk()
root.title('Testing and Entry widget')
root.geometry('900x700')
app = Application(root)
app.mainloop()
        
        
        
