#Christopher Carter -- Python Final Practical
from tkinter import *
from tkinter import ttk
import math


class GUI:
    def __init__(self, master):
        master.title("Draw Circle")
        master.geometry("800x800+100+100")

        def onQuit():
            master.destroy()

        def setCenter(event):
            self.cenX = event.x
            self.cenY = event.y

            self.cir = canvas.create_oval((event.x-1), (event.y-1), (event.x+1), (event.y+1))


        def setRadius(event):
            radius = math.sqrt(((event.x-self.cenX)**2)+((event.y-self.cenY)**2))

            canvas.delete(self.cir)
            self.cir = canvas.create_oval((self.cenX-radius), (self.cenY-radius), (self.cenX+radius), (self.cenY+radius))

        # SET UP MENU
        master.option_add("*tearOff", False)
        menuBar = Menu(master)
        master.config(menu = menuBar)

        exitMenu = Menu(menuBar)
        menuBar.add_cascade(menu = exitMenu, label = "Exit")
        exitMenu.add_command(label = "Quit", command = onQuit)

        # SET UP CANVAS
        canvas = Canvas(master)
        canvas.config(width=800, height=800, background="white")
        canvas.pack()
        canvas.bind("<ButtonPress-1>",setCenter)
        canvas.bind("<B1-Motion>",setRadius)



def main():
    root=Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__": main()
