import tkinter as tk
from tkinter import filedialog
from converter import convert_pdf_to_audio

pdf_path = ""

def select_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        file_label.config(text=f"Selected file: {pdf_path.split('/')[-1]}")

def convert_to_audio():
    if not pdf_path:
        status_label.config(text="Please select a PDF file first.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not output_path:
        status_label.config(text="Save cancelled.")
        return

    status_label.config(text="Converting... Please wait.")
    root.update()

    result = convert_pdf_to_audio(pdf_path, output_path)
    status_label.config(text=result)

def main():
    global root
    root = tk.Tk()
    root.title("Audiobook Maker")
    root.geometry("400x250")

    global file_label
    file_label = tk.Label(root, text="No file selected")
    file_label.pack(pady=10)

    select_button = tk.Button(root, text="Select PDF", command=select_pdf)
    select_button.pack(pady=10)

    convert_button = tk.Button(root, text="Convert to Audiobook", command=convert_to_audio)
    convert_button.pack(pady=10)

    global status_label
    status_label = tk.Label(root, text="")
    status_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()