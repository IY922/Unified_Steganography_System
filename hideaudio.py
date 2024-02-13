from pydub import AudioSegment
import array
from tkinter import filedialog
from tkinter import messagebox
import wave

def hide_message_in_audio(input_audio_path, message):
    try:
        # Open the audio file
        audio = AudioSegment.from_wav(input_audio_path)

        # Convert the message to binary
        binary_message = ''.join(format(ord(char), '08b') for char in message)

        # Ensure the audio has enough space to hide the message
        if len(binary_message) > len(audio.raw_data) // 8:
            raise ValueError("Message is too long to hide in the audio")

        # Convert the audio data to a mutable array
        audio_array = array.array("h", audio.raw_data)

        # Hide the message in the audio data
        for i in range(len(binary_message)):
            # Assuming 16-bit PCM, modify the least significant bit of each audio sample
            audio_array[i] = (audio_array[i] & ~1) | int(binary_message[i])

        # Create a new AudioSegment with the modified audio data
        modified_audio = AudioSegment(
            audio_array.tobytes(),
            frame_rate=audio.frame_rate,
            sample_width=audio.sample_width,
            channels=audio.channels
        )

        # Allow the user to choose the output file path
        output_audio_path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            title="Save Hidden Message Audio As"
        )

        if output_audio_path:
            # Save the modified audio
            modified_audio.export(output_audio_path, format="wav")
            messagebox.showinfo("Success", "Saved Successfully")

    except Exception as e:
        # Handle any errors that may occur during the process
        print(f"Error: {e}")

# Example usage:
# hide_message_in_audio("input_audio.wav", "This is a hidden message")
