
import tkinter as tk
from PIL import Image, ImageTk


class FloatingAvatar:

    def __init__(self):

        self.root = tk.Tk()

        # Remove normal window appearance
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # Transparent background on Windows
        self.transparent_color = "#ff00ff"
        self.root.configure(bg=self.transparent_color)

        self.root.wm_attributes(
            "-transparentcolor",
            self.transparent_color
        )

        # Load avatar
        image = Image.open("assets/Avatar image.png").convert("RGBA")

        image = image.resize(
            (120, 150),
            Image.Resampling.LANCZOS
        )

        self.photo = ImageTk.PhotoImage(image)

        # Display only the avatar
        self.label = tk.Label(
            self.root,
            image=self.photo,
            bg=self.transparent_color,
            borderwidth=0
        )

        self.label.pack()

        # Position on right side
        width = 120
        height = 150

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width - width - 20
        y = screen_height - height - 100

        self.root.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        # Initially hidden
        self.root.withdraw()

    def show_alert(self):

        self.root.deiconify()
        self.root.lift()

        # Hide after 8 seconds
        self.root.after(8000, self.hide_avatar)

    def hide_avatar(self):

        self.root.withdraw()

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    avatar = FloatingAvatar()

    # Test avatar after 2 seconds
    avatar.root.after(2000, avatar.show_alert)

    avatar.run()
