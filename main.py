from tkinter import Tk
from helper import YT

BG_COLOR = "#171717"
WIDTH = 900
HEIGHT = 600

if __name__ == "__main__":
    # Instantiating top level
    root = Tk()
    root.grid_columnconfigure(2, weight=1)
    # Giving title name to the app
    root.title("Download YouTube Videos")
    # Setting height and width for the app window
    root.geometry("{}x{}".format(WIDTH, HEIGHT))
    # Changing the background color
    root.config(bg=BG_COLOR)
    # Calling the app
    app = YT(root)
    # Mainloop which will cause this toplevel to run infinitely
    root.mainloop()



