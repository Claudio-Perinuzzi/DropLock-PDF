from tkinterdnd2 import TkinterDnD, DND_FILES # Drag-and-drop event for files
from pypdf import PdfReader, PdfWriter
import tkinter as tk
import sys
import os

# Constants
VERSION = "v1.0.0"
APP_DIMENSIONS = "570x670"
MAIN_BG_COLOR = "#323232"
BOX_BG_COLOR = "#1d1d1d"
TITLE = "DropLock PDF"

class App(TkinterDnD.Tk):   # Inherit from TkinterDnD.Tk for drag-and-drop support
    
    ###################################################################################
    # Init methods
    ###################################################################################

    def __init__(self):
        super().__init__()  # Constructor of parent class
        self.init_dnd()     # Initialize drag-and-drop support
        self.init_ui()      # Initialize UI


    def init_dnd(self):
        '''
        Initializes drag-and-drop support for the object
        on_file_drop function called when a drop event occurs
        '''
        
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_file_drop_callback)


    def resource_path(self, relative_path):
        """ Get absolute path to resource - needed for PyInstaller """
        try:
            # PyInstaller has a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def init_ui(self):
        '''Initializes UI elements'''
        
        ##################################################################
        # GENERAL APPEARANCE 
        ##################################################################
        self.title(TITLE)
        self.configure(background=MAIN_BG_COLOR)
        self.geometry(APP_DIMENSIONS)
        try:
            self.app_icon = tk.PhotoImage(file=self.resource_path("lock.png"))
            self.iconphoto(False, self.app_icon)
        except Exception as e:
            print(f"Icon not found: {e}")


        ##################################################################
        # VERSION 
        ##################################################################
        self.version_label = tk.Label(
            self, 
            text=VERSION, 
            fg="#888888",      
            bg=MAIN_BG_COLOR
        )
        self.version_label.pack(side="bottom", anchor="se", padx=10, pady=5)


        ##################################################################
        # ENTER PASSWORD
        ##################################################################
        self.password_instructions = tk.Label(self, 
            text="Enter a Password Below", 
            fg="white", 
            background=MAIN_BG_COLOR)  
        self.password_instructions.pack(pady=(8, 3))

        self.password = tk.Entry(self, show="*", fg="black", bg="white", width=25) 
        self.password.pack(pady=5)

        # Bind the key release event to check strength
        self.password.bind("<KeyRelease>", self.check_password_strength)

        # Strength Bar Container (background of the bar)
        self.bar_container = tk.Frame(self, width=150, height=8, bg="#444444")
        self.bar_container.pack(pady=9)
        self.bar_container.pack_propagate(False) # Prevent the frame from shrinking

        # Actual colored bar
        self.strength_bar = tk.Frame(self.bar_container, width=0, height=8, bg="red")
        self.strength_bar.pack(side="left")

        # Show password state
        self.show_pass_var = tk.BooleanVar()

        # Checkbutton for showing password
        self.show_pass_check = tk.Checkbutton(
            self, 
            text="Show Password", 
            variable=self.show_pass_var,
            command=self.show_password, 
            bg="#323232",                 
            fg="white", 
            selectcolor="#1d1d1d",        
            activebackground="#323232",
            activeforeground="white"
        )
        self.show_pass_check.pack(pady=5)


        ##################################################################
        # INSTRUCTIONS
        ##################################################################
        self.info = tk.Label(self, 
            text="Drag and Drop PDF Files for Encryption Below", 
            fg="white", 
            background=MAIN_BG_COLOR)  
        self.info.pack(pady=9)


        ##################################################################
        # ENCRYPTION BUTTON
        ##################################################################
        if sys.platform == "darwin":  # macOS detected
            self.encrypt_button = tk.Button(
                self, 
                text="ENCRYPT FILES", 
                command=self.encrypt_callback
            )
        else:                         # Windows/else
            self.encrypt_button = tk.Button(
                self, 
                text="ENCRYPT FILES", 
                command=self.encrypt_callback,
                bg="#2980b9",           
                fg="white",             
                font=("Arial", 9, "bold"),
                borderwidth=0,          
                padx=10,                
                pady=5,                
                cursor="hand2",         
                activebackground="#3498db" 
            )
        self.encrypt_button.pack(pady=15)

        # Bind hover events
        self.encrypt_button.bind("<Enter>", self.on_enter)
        self.encrypt_button.bind("<Leave>", self.on_leave)


        ##################################################################
        # MESSAGES & DISPLAY BOXES
        ##################################################################

        # No files were found message
        self.empty_msg = tk.Label(self, text="", fg="red", background=MAIN_BG_COLOR)  
        self.empty_msg.pack()

        # Display box for files dropped 
        self.pdf_input_box = tk.Listbox(self, width=50, height=10, bg=BOX_BG_COLOR, fg='white', highlightthickness=0)
        self.pdf_input_box.pack(pady=10)

        # Placeholder Label (where pdfs are dragged to)
        self.placeholder_label = tk.Label(
            self.pdf_input_box, 
            text="drag pdf files here", 
            fg="#555555", 
            bg=BOX_BG_COLOR,
            font=("Arial", 14, "italic") if sys.platform == "darwin" else ("Arial", 10, "italic")
        )
        self.placeholder_label.place(relx=0.5, rely=0.5, anchor="center")

        # Message for the output listbox
        self.success_msg = tk.Label(self, text="Encryption Output", fg="white", background=MAIN_BG_COLOR)  
        self.success_msg.pack(pady=2)

        # Display box for successfully encrypted files
        self.pdf_output_box = tk.Listbox(self, width=50, height=10, bg=BOX_BG_COLOR, fg='white')  
        self.pdf_output_box.pack(pady=10)

    
    ###################################################################################
    # CALLBACKS
    ###################################################################################

    def on_file_drop_callback(self, event):
        '''
        Callback for handling the file drop event. Function splits the event data into files
        and inserts the files into the pdf_file_box if it is a pdf.
        '''

        files = self.tk.splitlist(event.data)
        for file in files:
            if file.lower().endswith(".pdf"):
                # Hide the placeholder and insert file path
                self.placeholder_label.place_forget() 
                self.pdf_input_box.insert(tk.END, file)


    def encrypt_callback(self):
        '''
        Callback for handling the encrypt button. Function gets a list of file
        paths from the pdf_input_box and encrypts each file path.
        '''
        entered_password = self.password.get()

        if entered_password == "":                      # If no password, display a error
            self.empty_msg.config(text="Please Enter a Password") 
        elif self.pdf_input_box.size() == 0:            # If listbox is empty, display a error
            self.empty_msg.config(text="Please Drop Files Here to Encrypt") 
        else:
            self.empty_msg.config(text="")              # Reset error to an empty string when files are detected
            self.pdf_output_box.delete(0, tk.END)       # Delete all file paths in the ouput box if they exist
            for _ in range(self.pdf_input_box.size()):  
                file_path = self.pdf_input_box.get(0)   
                self.encrypt_pdf(file_path, entered_password)   # Encrypt the given file path
                self.pdf_input_box.delete(0)                    # Delete this file path from the input box
                self.placeholder_label.place(relx=0.5, rely=0.5, anchor="center") # 

    
    ###################################################################################
    # METHODS
    ###################################################################################

    def on_enter(self, e):
        ''' Changes the color of the encrypt button upon hovering on it '''
        self.encrypt_button['background'] = "#3498db"


    def on_leave(self, e):
        ''' Changes the color of the encrypt button when not hovering on it '''
        self.encrypt_button['background'] = "#2980b9" 


    def show_password(self):
        if self.show_pass_var.get():    # Show actual text
            self.password.config(show="")
        else:                           # Hide text w/ *
            self.password.config(show="*")


    def check_password_strength(self, event):
        ''' Method for displaying password strength '''
        
        password = self.password.get()
        score = 0
        
        # Check the length, if a number/special char/uppercase
        if len(password) >= 10: score += 1
        if any(char.isdigit() for char in password) and len(password) >= 5: score += 1
        if any(not char.isalnum() for char in password) and len(password) >= 5: score += 1
        if any(char.isupper() for char in password) and len(password) >= 5: score += 1

        # Map scores to colors and widths
        if score <= 1:
            color = "#ff4d4d" 
            width = 50 if len(password) > 0 else 0
        elif score < 4:
            color = "#ffa500" 
            width = 100
        else:
            color = "#2ecc71" 
            width = 150

        # Update the bar
        self.strength_bar.config(bg=color, width=width)         


    def encrypt_pdf(self, file_path, entered_password):
        '''Creates an encrypted copy of the PDF in the same directory'''
        try:
            renamed_file_path = file_path.lower().replace(".pdf", "_encrypted.pdf")

            pdf = PdfReader(file_path)
            writer = PdfWriter()

            writer.append_pages_from_reader(pdf)
            writer.encrypt(entered_password, algorithm="AES-256")

            with open(renamed_file_path, "wb") as encrypted_file:
                writer.write(encrypted_file)
            
            file_name = os.path.basename(renamed_file_path)
            self.pdf_output_box.insert(tk.END, f"🔒 Created: {file_name}")
            
        except Exception as e:
            self.pdf_output_box.insert(tk.END, f"❌ ERROR: File {os.path.basename(file_path)} was not encrypted")
            print(f"Encryption failed: {e}")



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()