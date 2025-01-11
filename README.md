# File Compression and Decompression Tool

This project is a web-based application built using **Python** and **Flask**. It allows users to compress and decompress files of various types directly through a simple and intuitive interface.

## Features

- **Compress Files**: Upload any file to compress it into a smaller size for easy storage and transfer.
- **Decompress Files**: Restore compressed files to their original form.
- **User-Friendly Web Interface**: A sleek and responsive interface with a dark theme.
- **Dynamic Effects**: Animated welcome page with interactive elements.

---

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **File Handling**: Python's built-in file handling and `zipfile` module

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python (version 3.7 or later)
- Flask library (`pip install flask`)

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yatheesh2225/Compression_Tool.git
   cd project
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Project Structure

```plaintext
project
├── templates/
│   ├── index.html       # Compressor and Decompressor Page
│   ├── welcome.html     # Welcome Page
├── app.py               # Main Flask Application
├── README.md            # Project Documentation
```

---

## Usage

1. **Welcome Page**:
   - The app opens with a stylish welcome page.
   - Click the "Go to Tools" button to access the file compressor and decompressor.

2. **Compress Files**:
   - Choose any file and upload it to compress.
   - The app will generate and download a compressed `.zip` file.

3. **Decompress Files**:
   - Upload a `.zip` file to decompress.
   - The app will restore and download the original file.

---
