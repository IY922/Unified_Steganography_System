import tkinter as tk
from tkinter import ttk, filedialog
from showimage import show_message_in_image
from showtext import show_message_in_text
from showaudio import show_message_in_audio

class ShowMessage:
    def __init__(self, root):
        # Save a reference to the main window
        self.root = root

        # Create a new Toplevel window with the specified background color
        self.show_message_window = tk.Toplevel(root)
        self.show_message_window.title("Show Message Window")
        self.show_message_window.configure(bg="#F08080")  # Background color

        # Label and Combobox for selecting file type with larger font
        file_type_label = tk.Label(self.show_message_window, text="Select File Type:", font=("Helvetica", 14))  # Larger font size, Background color
        file_type_label.pack(pady=5)

        self.file_type_var = tk.StringVar()
        file_type_options = ["Image", "Text", "Audio"]
        file_type_dropdown = ttk.Combobox(self.show_message_window, textvariable=self.file_type_var, values=file_type_options)
        file_type_dropdown.set("Image")  # Default value
        file_type_dropdown.pack(pady=5)

        # Browse button to select a file
        browse_button = tk.Button(self.show_message_window, text="Browse", command=self.browse_file)  # Background color
        browse_button.pack(pady=10)

        # Label to display the selected file path with larger font
        self.file_path_label = tk.Label(self.show_message_window, text="Selected File: None", font=("Helvetica", 12))  # Larger font size, Background color
        self.file_path_label.pack(pady=5)

        # Button to show the message
        show_button = tk.Button(self.show_message_window, text="Show Message", command=self.show_message)  # Background color
        show_button.pack(pady=10)

        # Text box for displaying the message with larger font
        self.message_display = tk.Text(self.show_message_window, wrap="word", width=50, height=10, font=("Helvetica", 12))  # Larger font size, Background color
        self.message_display.pack(pady=10)

        # Button to close the ShowMessage window and show the main window with larger font
        close_button = tk.Button(self.show_message_window, text="Close", command=self.close_windows, font=("Helvetica", 12))  # Larger font size, Background color
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
            parent=self.show_message_window,
            initialdir=".",
            title=f"Select {file_type.capitalize()} File to Show Message",
            filetypes=file_types[file_type]
        )

        # Update the file path label
        self.file_path_label.config(text=f"Selected File: {file_path}")
        self.show_message_window.configure(bg="#87CEEB")  # Background color

    def show_message(self):
        file_type = self.file_type_var.get().lower()
        file_path = self.file_path_label.cget("text").replace("Selected File: ", "")

        # Call the appropriate function based on the selected file type
        if file_type == "image":
            message = show_message_in_image(file_path)
            # Display the message in the Text widget
            self.message_display.delete("1.0", tk.END)  # Clear previous content
            self.show_message_window.configure(bg="#98FB98")  # Background color
            self.message_display.insert(tk.END, message)
        elif file_type == "text":
            message = show_message_in_text(file_path)
            if message is not None:
                # Display the message in the Text widget
                self.message_display.delete("1.0", tk.END)  # Clear previous content
                self.show_message_window.configure(bg="#98FB98")  # Background color
                self.message_display.insert(tk.END, message)
        elif file_type == "audio":
            message = show_message_in_audio(file_path)
            # Display the message in the Text widget
            self.message_display.delete("1.0", tk.END)  # Clear previous content
            self.show_message_window.configure(bg="#98FB98")  # Background color
            self.message_display.insert(tk.END, message)

    def close_windows(self):
        # Close the ShowMessage window and show the main window
        self.show_message_window.destroy()
        self.root.deiconify()
