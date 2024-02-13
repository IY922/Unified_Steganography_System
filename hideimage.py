from PIL import Image
from tkinter import filedialog
from tkinter import messagebox

def hide_message_in_image(input_image_path, message):
    try:
        # Open the image
        image = Image.open(input_image_path)

        # Convert the message to binary and append a null character
        binary_message = ''.join(format(ord(char), '08b') for char in message) + '00000000'

        # Ensure the image has enough space to hide the message
        if len(binary_message) > image.width * image.height * 3:  # Multiply by 3 for RGB channels
            raise ValueError("Message is too long to hide in the image")

        # Iterate over each pixel in the image
        index = 0
        for y in range(image.height):
            for x in range(image.width):
                pixel = list(image.getpixel((x, y)))

                # Modify the least significant bit of each color component to store one bit of the message
                for color_channel in range(3):  # RGB channels
                    if index < len(binary_message):
                        pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[index])
                        index += 1

                # Update the pixel in the image
                image.putpixel((x, y), tuple(pixel))

        # Allow the user to choose the output file path
        output_image_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save Hidden Message Image As"
        )

        if output_image_path:
            # Save the modified image
            image.save(output_image_path)
            messagebox.showinfo("Success", "Saved Successfully")

    except Exception as e:
        # Handle any errors that may occur during the process
        print(f"Error: {e}")

# Example usage:
# hide_message_in_image("input_image.png", "This is a hidden message")
