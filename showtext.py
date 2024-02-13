from tkinter import filedialog
from tkinter import messagebox

def show_message_in_text(file_path):
    try:
        # Read the content of the text file
        with open(file_path, 'r') as file:
            content = file.read()

        # Split the content into lines
        lines = content.split('\n')

        # Extract the message from the last line
        binary_message = lines[-1]

        # Convert the binary message to ASCII
        message = binary_to_ascii(binary_message)

        return message
    except Exception as e:
        print(f"Error showing message: {e}")
        messagebox.showerror("Error", f"Error showing message: {e}")

def binary_to_ascii(binary_str):
    # Convert binary string to ASCII using fixed-width (8 bits) for each character
    ascii_message = ""
    for i in range(0, len(binary_str), 8):
        ascii_message += chr(int(binary_str[i:i+8], 2))
    return ascii_message

# Example usage:
# message = show_message_in_text("example.txt")
# print(message)
