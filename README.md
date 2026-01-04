# DropLock PDF

This is a Python-based graphical user interface (GUI) application using `tkinter` allowing users to upload PDF files by dragging and dropping them into the application window. The app displays the file name of the dropped PDF file and allows users to encrypt the selected PDF using a password. The purpose of this application is to mass encrypt multiple PDF files at once without having to manually enter a password for each PDF.

## Encryption

The application uses **AES-256 bit encryption**. All encryption happens locally on your machine. Your files are never uploaded to a server, ensuring total privacy.

## Features

- Drag and drop PDF files into the app.
- Displays the name of the dropped file.
- Encrypts the PDF file using a password provided by the user.
- Simple and user-friendly interface with error handling.

## Installation

1. Clone or download this repository to your local machine.

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

## Usage

Once the application is running:

1. **Drag and Drop:**
    - Drag any PDF file and drop it into the app's window.
    - The name of the file will be extracted and displayed in the input box.

2. **Password Input:**
    - Enter a password in the password input field. This password will be used to encrypt the PDF file.

3. **Encrypt the PDF:**
    - After entering the password, click the "Encrypt" button to encrypt the PDF.
    - The encrypted file will be saved with a modified name to indicate that it is encrypted.

## Demo

Here is an example of how the app looks when running:

![Example Image](example_assets/mac_img.png)