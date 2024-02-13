from PIL import Image

def show_message_in_image(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract the hidden message using the appropriate method (use your method here)
        message = extract_message_from_image(img)

        return message
    except Exception as e:
        # Handle exceptions (e.g., file not found, invalid image format)
        return f"Error: {str(e)}"

def extract_message_from_image(image):
    # Implement the message extraction logic specific to your steganography technique
    # Use the methods and techniques from the project code you provided in the start
    # ...

    # For example, if you stored the message in the least significant bits of pixel values:
    message = extract_message_from_lsbs(image)

    return message

def extract_message_from_lsbs(image):
    # Example: Extracting the message from the least significant bits of pixel values
    width, height = image.size
    message = ""
    byte_buffer = 0
    bits_in_buffer = 0

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Assuming the message is stored in the red, green, and blue channels' LSBs
            message_bit_r = pixel[0] & 1
            message_bit_g = pixel[1] & 1
            message_bit_b = pixel[2] & 1

            # Combine the bits into a single byte
            byte_value = (message_bit_r << 2) | (message_bit_g << 1) | message_bit_b

            # Add the byte value to the buffer
            byte_buffer = (byte_buffer << 3) | byte_value
            bits_in_buffer += 3

            # Check if there are enough bits to form a character
            while bits_in_buffer >= 8:
                bits_in_buffer -= 8
                # Extract the top 8 bits from the buffer as a character
                char_value = (byte_buffer >> bits_in_buffer) & 0xFF

                # Append the character to the message
                message += chr(char_value)

                # Break the loop if the null terminator is encountered
                if char_value == 0:
                    return message

    return message

def binary_to_ascii(binary_str):
    # Convert binary string to ASCII using fixed-width (8 bits) for each character
    ascii_message = ""
    for i in range(0, len(binary_str), 8):
        ascii_message += chr(int(binary_str[i:i+8], 2))
    return ascii_message