import tkinter as tk
from tkinter import filedialog
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Comic Sans MS",18,"bold"), fg="white", bg="black")
        title_label.pack(pady=10,)

def main():
    root = tk.Tk()
    converter = ImageToPDFConverter(root)
    root.title("Image to PDF Converter")
    root.geometry("500x700")
    root.configure(bg="black")
    root.mainloop()

if __name__ == "__main__":
    main()