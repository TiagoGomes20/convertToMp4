import os
import pytube
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video(url, output_path):
    youtube = pytube.YouTube(url)
    stream = youtube.streams.get_highest_resolution()
    stream.download(output_path=output_path)
    return stream.default_filename

def convert_to_mp3(video_file, output_file):
    os.system(f"ffmpeg -i {video_file} {output_file}")

def convert_to_wav(video_file, output_file):
    os.system(f"ffmpeg -i {video_file} {output_file}")

def convert_to_mp4(video_file, output_file):
    os.system(f"ffmpeg -i {video_file} {output_file}")

def convert():
    url = entry_url.get()
    output_format = var.get()

    # Download the video
    output_path = filedialog.askdirectory()
    if output_path:
        video_file = download_video(url, output_path)

        # Convert to the specified format
        output_file = os.path.join(output_path, f"{video_file.replace('.mp4', '')}.{output_format}")

        if output_format == 'mp3':
            convert_to_mp3(os.path.join(output_path, video_file), output_file)
        elif output_format == 'wav':
            convert_to_wav(os.path.join(output_path, video_file), output_file)
        elif output_format == 'mp4':
            convert_to_mp4(os.path.join(output_path, video_file), output_file)

        # Display a pop-up message indicating conversion completion
        messagebox.showinfo("Conversion Complete", f"Conversion completed: {output_file}")
    else:
        print("Please select an output directory.")

# Create GUI
root = tk.Tk()
root.title("YouTube Converter")

# YouTube URL input
label_url = tk.Label(root, text="Enter YouTube URL:")
label_url.pack()

entry_url = tk.Entry(root)
entry_url.pack()

# Output format selection
label_format = tk.Label(root, text="Choose output format:")
label_format.pack()

var = tk.StringVar(value="mp3")



mp4_radio = tk.Radiobutton(root, text="MP4", variable=var, value="mp4")
mp4_radio.pack()

# Conversion button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

root.mainloop()
