from tkinterdnd2 import TkinterDnD, DND_FILES # Drag-and-drop event for files
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
import os


class App(TkinterDnD.Tk):   # Inherit from TkinterDnD.Tk for drag-and-drop support
    
    def __init__(self):
        super().__init__()  # Call constructor of parent class
        self.init_dnd()     # Initialize drag-and-drop support
        self.init_ui()      # Initialize UI


    def init_dnd(self):
        '''
        Initializes drag-and-drop support for the object
        on_file_drop function called when a drop event occurs
        '''
        
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_file_drop_callback)


    def init_ui(self):
        '''Initializes UI elements'''
        
        # Colors
        main_bg = "#323232"
        box_bg = "#1d1d1d"
        button_bg = '#1f5ba4'

        # Appearance
        self.title("PDF Encryption")
        self.configure(background=main_bg)
        self.geometry("500x600")

        # Enter Password
        self.password_instructions = tk.Label(self, text="Please Enter a Password Below", fg="white", background=main_bg)  
        self.password_instructions.pack(pady=(8, 3))

        self.password = tk.Entry(self, show="*", fg="black", bg="white", width=25) 
        self.password.pack(pady=5)

        # Instructions
        self.info = tk.Label(self, text="Please Drag and Drop Files for Encryption Below", fg="white", background=main_bg)  
        self.info.pack(pady=3)

        # Encryption button
        self.encrypt_button = tk.Button(self, text="Encrypt Files", command=self.encrypt_callback)
        self.encrypt_button.pack(pady=4)  

        # No files were found message
        self.empty_msg = tk.Label(self, text="", fg="red", background=main_bg)  
        self.empty_msg.pack()

        # Display box for files dropped 
        self.pdf_input_box = tk.Listbox(self, width=50, height=10, bg=box_bg, fg='white')
        self.pdf_input_box.pack(pady=10)

        # Message for the output listbox
        self.success_msg = tk.Label(self, text="Files That Were Successfully Encrypted", fg="white", background=main_bg)  
        self.success_msg.pack(pady=2)

        # Display box for successfully encrypted files
        self.pdf_output_box = tk.Listbox(self, width=50, height=10, bg=box_bg, fg='white')  
        self.pdf_output_box.pack(pady=10)



    def on_file_drop_callback(self, event):
        '''
        Callback for handling the file drop event. Function splits the event data into files
        and inserts the files into the pdf_file_box if it is a pdf.
        '''

        files = self.tk.splitlist(event.data)
        for file in files:
            if file.lower().endswith(".pdf"):
                self.pdf_input_box.insert(tk.END, file)


    def encrypt_callback(self):
        '''
        Callback for handling the encrypt button. Function gets a list of file
        paths from the pdf_input_box and encrypts each file path.
        '''
        entered_password = self.password.get()

        if entered_password == "":                     # If no password, display a error
            self.empty_msg.config(text="Please Enter a Password") 
        elif self.pdf_input_box.size() == 0:            # If listbox is empty, display a error
            self.empty_msg.config(text="Please Drop Files Here to Encrypt") 
        else:
            self.empty_msg.config(text="")              # Reset error to an empty string when files are detected
            self.pdf_output_box.delete(0, tk.END)       # Delete all file paths in the ouput box if they exist
            for _ in range(self.pdf_input_box.size()):  
                file_path = self.pdf_input_box.get(0)   
                self.encrypt_pdf(file_path, entered_password)    # Encrypt the given file path
                self.pdf_input_box.delete(0)            # Delete this file path from the input box
            

    def encrypt_pdf(self, file_path, entered_password):
        '''Encrypts each PDF file path provided'''
        
        # Open the PDF file, create a new PDF writer object
        pdf = PdfReader(file_path)
        writer = PdfWriter()

        # Pass the PDF to the writer object and encrypt the file with a password
        writer.append_pages_from_reader(pdf)
        writer.encrypt(entered_password)

        # Write the encrypted PDF back to the original file
        with open(file_path, "wb") as encrypted_file:
            writer.write(encrypted_file)
        
        # Rename the file to indicate it has been encrypted
        renamed_file_path = file_path[:-4] + "_encrypted.pdf" 
        os.rename(file_path, renamed_file_path)

        file_name = os.path.basename(renamed_file_path)
        self.pdf_output_box.insert(tk.END, file_name)



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()