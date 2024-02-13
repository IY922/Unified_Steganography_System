from pydub import AudioSegment
import array
import tkinter as tk
from tkinter import filedialog, messagebox

def show_message_in_audio(audio_path):
    try:
        # Open the audio file
        audio = AudioSegment.from_wav(audio_path)

        # Convert the audio data to a mutable array
        audio_array = array.array("h", audio.raw_data)

        # Extract the message from the least significant bit of each audio sample
        binary_message = ""
        for i in range(len(audio_array)):
            binary_message += str(audio_array[i] & 1)

        # Convert the binary message to ASCII
        message = binary_to_ascii(binary_message)

        return message

    except Exception as e:
        # Handle any errors that may occur during the process
        messagebox.showerror("Error", str(e))
        return None

def binary_to_ascii(binary_str):
    # Convert binary string to ASCII using fixed-width (8 bits) for each character
    ascii_message = ""
    for i in range(0, len(binary_str), 8):
        ascii_message += chr(int(binary_str[i:i+8], 2))
    return ascii_message

# Example usage:
# message = show_message_in_audio("output_audio_with_message.wav")
# print(message)
