
<div align="center">
<h1>DropLock PDF</h1>
  <img src="lock.png" alt="Logo" width="150"/>
  <h3>Your all in one PDF encryption utility.<h3>
  <br>
  <h1>About<h1>
  <p>
    <font size="2">
        DropLock PDF is a Python-based graphical user interface (GUI) application that efficiently encrypts multiple PDFs simultaneously, allowing users to save time by securely encrypting files in bulk. Users can bulk upload PDF files by dragging and dropping them into the application window. The app displays the file name of the dropped PDF files and allows users to encrypt the selected PDFs using a password. The purpose of this application is to mass encrypt multiple PDF files at once without having to manually enter a password for each PDF or upload files one by one.
    </font>
  </p>
</div>

<br>
<br>
<div align="center">
<h1>Both Windows and MacOS Compatible:</h1>
  <img src="example_assets/mac_img.png" alt="Logo" width="500"/>
  <img src="example_assets/windows_img.png" alt="Logo" width="490"/>
  <br>
  <br>
  <br>
</div>

## 🔒 Encryption

The application uses **AES-256 bit encryption**. All encryption happens locally on your machine meaning your files are never uploaded to a server, ensuring total privacy.

## ⭐ Features

- Drag and drop PDF files into the app.
- Displays the name of the dropped file.
- Encrypts the PDF file using a password provided by the user.
- Simple and user-friendly interface with error handling.

## 📄 Usage

Once the application is running:

1. **Drag and Drop:**
    - Drag any PDF file and drop it into the app's window.
    - The name of the file will be extracted and displayed in the input box.

2. **Password Input:**
    - Enter a password in the password input field. This password will be used to encrypt the PDF file.

3. **Encrypt the PDF:**
    - After entering the password, click the "Encrypt" button to encrypt the PDF.
    - The encrypted file will be saved with a modified name to indicate that it is encrypted.

## ⬇️ Installation

### 🍎 MacOS
1. Download the [DMG Installer](https://github.com/Claudio-Perinuzzi/DropLock-PDF/releases/tag/v1.0.0).
2. Open the `.dmg` file and drag the application to your **Applications** folder.

### 🪟 Windows
1. Download the [Windows Executable](https://github.com/Claudio-Perinuzzi/DropLock-PDF/releases/tag/v1.0.0).
2. Double-click the `.exe` file to run the application.

---

### 🛠️ Build from Source

Follow these steps to run the python application directly from the source code:

1. **Clone the repository**
   ```bash
   git clone git@github.com:Claudio-Perinuzzi/DropLock-PDF.git
   cd DropLock-PDF
   ```
2. **Install the required Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application**
    ```bash
    python app.py
    ```

## ⚖️ MIT License

Distributed under the MIT License. 


Copyright (c) 2026 Claudio Perinuzzi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 