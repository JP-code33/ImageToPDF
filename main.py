import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.colors import white
from PIL import Image
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):

        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Comic Sans MS",20,"bold"),fg="white",bg="black")
        title_label.pack(pady=(20,10))

        selectImageButton = tk.Button(self.root,text="Select Images",font=("Comic Sans MS",11,"bold"),fg="white",bg="#003b63",activebackground="#003b63",padx=10,pady=5,command=self.select_images)
        selectImageButton.pack(pady=(0,15))

        self.selected_images_listbox.configure(bg="#1e1e1e",fg="white",font=("Comic Sans MS",10),selectbackground="#003b63",selectforeground="white",height=12,bd=1,relief="solid")
        self.selected_images_listbox.pack(pady=(0,20), padx=30, fill=tk.BOTH,expand=True)

        label = tk.Label(self.root, text="Enter the PDF name:",font=("Comic Sans MS",11),fg="#cccccc",bg="black")
        label.pack(pady=(0,5))

        pdf_name_entry = tk.Entry(self.root,textvariable=self.output_pdf_name,width=35,justify='center',font=("Comic Sans MS", 11),bg="#252526",fg="white",insertbackground="white",bd=1,relief="solid")
        pdf_name_entry.pack(pady=(0,25))

        self.convertButton = tk.Button(self.root,text="Convert to PDF",font=("Comic Sans MS",12,"bold"),fg="white",bg="#003b63",activebackground="#005999",activeforeground="white",padx=20,pady=8,command=self.convert_images_to_pdf,state="disabled")
        self.convertButton.pack(pady=(0,25))

        footer = tk.Label(self.root,text="Supports PNG, JPG, JPEG", font=("Comic Sans MS",9,"bold"),fg="#FFFFFF",bg="black")
        footer.pack(side="bottom",pady=15)
        
    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Images files", "*.png;*.jpg;*.jpeg")])
        self.updateSelectedImageListbox()
        if self.image_paths:
            self.convertButton.config(state="normal")
        else:
            self.convertButton.config(state="disabled")

    def updateSelectedImageListbox(self):
        self.selected_images_listbox.delete(0,tk.END)
        for image_path in self.image_paths:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)    

    def convert_images_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("No Images Selected", "Please Select One or More Image(s)")
            return

        defaultName = self.output_pdf_name.get() if self.output_pdf_name.get() else "output"
        output_pdf_path = filedialog.asksaveasfilename(title="Save PDF As",initialfile=defaultName + ".pdf",defaultextension=".pdf",filetypes=[("PDF files", "*.pdf")])
        if not output_pdf_path:
            messagebox.showinfo("Cancelled","PDF conversion was cancelled")
            return
        
        try:
            pdf = canvas.Canvas(output_pdf_path, pagesize=(612,792))
            for image_path in self.image_paths:
                img = Image.open(image_path)
                availableWidth = 540
                availableHeight = 720
                scaleFactor = min(availableWidth / img.width, availableHeight / img.height)
                newWidth = img.width * scaleFactor
                newHeight = img.height * scaleFactor
                x_centered = (612 - newWidth) / 2
                y_centered = (792 - newHeight) / 2

                pdf.setFillColor(white)
                pdf.rect(0,0,612,792,fill=True)
                pdf.drawInlineImage(img, x_centered, y_centered, width=newWidth, height=newHeight)
                pdf.showPage()

            pdf.save()
            messagebox.showinfo("Success",f"The PDF has been created and is saved to:\n{output_pdf_path}")

        except Exception as e:
            messagebox.showerror("Conversion Failed",f"An error has occured while converting.\n{e}")




def main():
    root = tk.Tk()
    converter = ImageToPDFConverter(root)
    root.title("Image to PDF Converter")
    root.geometry("500x700")
    root.configure(bg="black")
    root.mainloop()

if __name__ == "__main__":
    main()