from tkinter import Label, Entry, Button, StringVar
import yt_dlp

BG_COLOR = "#171717"
FONT_TITLE = ("Arial", 30)


class YT:
    def __init__(self, root) -> None:
        self.root = root
        self.url_variable = StringVar()

        # Styling YT
        Label(text="YT ", bg=BG_COLOR, foreground="red", font=FONT_TITLE).place(
            relx=0.38, rely=0.1, anchor="center"
        )
        Label(
            text=" Download ⬇",
            background=BG_COLOR,
            foreground="#fff",
            font=FONT_TITLE,
        ).place(relx=0.5, rely=0.1, anchor="center")

        # URL Input Label
        Label(
            text="Enter URL: ", foreground="#fff", bg=BG_COLOR, font=("Arial", 25)
        ).place(relx=0.3, rely=0.3)

        # URL Input
        Entry(
            textvariable=self.url_variable,
            font=("Arial", 20, "normal"),
            background="#fff",
            foreground="#000",
        ).place(relx=0.45, rely=0.3)

        def submit() -> None:
            if self.url_variable.get() == "":
                Label(
                    text="Please enter URL",
                    background="red",
                    font=("Arial", 14),
                ).place(relx=0.4, rely=0.4)
            else:
                # use yt_dlp to download the video
                with yt_dlp.YoutubeDL() as ydl:
                    ydl.download([self.url_variable.get()])

                Label(
                    text="Video has been downloaded successfully!",
                    background="green",
                    font=("Arial", 14),
                ).place(relx=0.4, rely=0.4)

        Button(text="Submit", command=submit).place(relx=0.5, rely=0.5)




