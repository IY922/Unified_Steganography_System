import tkinter as tk
from HideMessage import HideMessage
from ShowMessage import ShowMessage


class SteganographyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Steganography")
        self.master.geometry("400x200")

        self.title_label = tk.Label(self.master, text="Steganography", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        self.hide_button = tk.Button(self.master, text="Hide Message", command=self.hide_message,
                                     font=("Helvetica", 14))
        self.hide_button.pack(pady=10)

        self.show_button = tk.Button(self.master, text="Show Message", command=self.show_message,
                                     font=("Helvetica", 14))
        self.show_button.pack(pady=10)

        # Add some padding and configure background color
        self.master.configure(bg="#F0F0F0")

    def hide_message(self):
        # Hide the main window and open the HideMessage window
        self.master.iconify()  # Minimize the main window
        HideMessage(self.master)

    def show_message(self):
        # Hide the main window and open the ShowMessage window
        self.master.iconify()  # Minimize the main window
        ShowMessage(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
