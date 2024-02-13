from tkinter import filedialog
from tkinter import messagebox

def hide_message_in_text(file_path, message):
    try:
        # Read the existing content of the text file
        with open(file_path, 'r') as file:
            original_content = file.read()

        # Convert the message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in message)

        # Prompt the user to choose the output file path
        output_file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Hidden Message Text As"
        )

        if output_file_path:
            # Combine the original content with the binary message
            hidden_content = f"{original_content}\n{binary_message}"

            # Write the combined content to the new text file
            with open(output_file_path, 'w') as file:
                file.write(hidden_content)

            print("Message hidden successfully in the new text file.")
            messagebox.showinfo("Success", "Message hidden successfully.")
    except Exception as e:
        print(f"Error hiding message: {e}")
        messagebox.showerror("Error", f"Error hiding message: {e}")

# Example usage:
# hide_message_in_text("example.txt", "This is a hidden message")
