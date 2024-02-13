import tkinter as tk
from tkinter import ttk, filedialog
from hideimage import hide_message_in_image
from hidetext import hide_message_in_text
from hideaudio import hide_message_in_audio

class HideMessage:
    def __init__(self, root):
        # Save a reference to the main window
        self.root = root

        # Create a new Toplevel window with the specified background color
        self.hide_message_window = tk.Toplevel(root)
        self.hide_message_window.title("Hide Message Window")
        self.hide_message_window.configure(bg="#F08080")  # Background color

        # Label and Combobox for selecting file type with larger font
        file_type_label = tk.Label(self.hide_message_window, text="Select File Type:", font=("Helvetica", 14))  # Larger font size, Background color
        file_type_label.pack(pady=5)

        self.file_type_var = tk.StringVar()
        file_type_options = ["Image", "Text", "Audio"]
        file_type_dropdown = ttk.Combobox(self.hide_message_window, textvariable=self.file_type_var, values=file_type_options)
        file_type_dropdown.set("Image")  # Default value
        file_type_dropdown.pack(pady=5)

        # Browse button to select a file
        browse_button = tk.Button(self.hide_message_window, text="Browse", command=self.browse_file)  # Background color
        browse_button.pack(pady=10)

        # Label to display the selected file path with larger font
        self.file_path_label = tk.Label(self.hide_message_window, text="Selected File: None", font=("Helvetica", 12))  # Larger font size, Background color
        self.file_path_label.pack(pady=5)

        # Label for guiding the user
        message_label = tk.Label(self.hide_message_window, text="Enter the hidden message below:",font=("Helvetica", 12))  # Larger font size, Background color
        message_label.pack(pady=5)

        # Text entry for entering the message with larger font
        self.message_entry = tk.Entry(self.hide_message_window, width=50, font=("Helvetica", 12))  # Larger font size, Background color
        self.message_entry.pack(pady=10)

        # Button to hide the message
        hide_button = tk.Button(self.hide_message_window, text="Hide Message", command=self.hide_message)  # Background color
        hide_button.pack(pady=10)

        # Button to close the HideMessage window and show the main window with larger font
        close_button = tk.Button(self.hide_message_window, text="Close", command=self.close_windows, font=("Helvetica", 12))  # Larger font size, Background color
        close_button.pack()

    def browse_file(self):
        # Open a file dialog based on the selected file type
        file_type = self.file_type_var.get().lower()
        file_types = {
            "image": [("Image files", "*.png")],
            "text": [("Text files", "*.txt")],
            "audio": [("Audio files", "*.wav")]
        }

        file_path = filedialog.askopenfilename(
            parent=self.hide_message_window,
            initialdir=".",
            title=f"Select {file_type.capitalize()} File to Hide Message",
            filetypes=file_types[file_type]
        )

        # Update the file path label
        self.file_path_label.config(text=f"Selected File: {file_path}")
        self.hide_message_window.configure(bg="#87CEEB")

    def hide_message(self):
        file_type = self.file_type_var.get().lower()
        file_path = self.file_path_label.cget("text").replace("Selected File: ", "")
        message = self.message_entry.get()

        # Call the appropriate function based on the selected file type
        if file_type == "image":
            hide_message_in_image(file_path, message)
        elif file_type == "text":
            hide_message_in_text(file_path, message)
        elif file_type == "audio":
            hide_message_in_audio(file_path, message)

        self.hide_message_window.configure(bg="#98FB98")

    def close_windows(self):
        # Close the HideMessage window and show the main window
        self.hide_message_window.destroy()
        self.root.deiconify()
