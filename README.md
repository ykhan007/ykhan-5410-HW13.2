# LZW Text Compression 

This project is a simple implementation of the **Lempel–Ziv–Welch (LZW)** compression algorithm.  
I built it for my Algorithms class to understand how dictionary-based compression actually works.

The program reads a text file (I used *alice.txt*), compresses it using LZW, saves the result with Python’s `pickle`, loads it again, and then decompresses it to make sure the output matches the original.

---

## 📌 Project Overview

- Reads a `.txt` file  
- Cleans the text to remove non-ASCII characters  
- Compresses the file using LZW  
- Saves compressed data using `pickle`  
- Loads the compressed data again  
- Decompresses back to normal text  
- Prints the **first 45 characters** of the decoded text to verify correctness

---

## 🛠 How the Algorithm Works

### 1. **Compression**
- Starts with a dictionary containing ASCII chars (`0–255`)
- Reads characters one by one
- Builds longer sequences dynamically
- Converts sequences into integers
- Produces a list of compressed codes

### 2. **Output**
Original text length: 143831
Compressed length: 32351

First 45 characters of decoded text:
CHAPTER I.
Down the Rabbit-Hole
Alice was beg
