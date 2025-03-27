import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="📖 Sangam Magazine", layout="wide")

# Load PDF
PDF_FILE = "sangam.pdf"  # Make sure this file is in the same directory

st.title("📖 Sangam Annual Magazine 2023-24")

# Convert PDF pages to images
pdf = fitz.open(PDF_FILE)

st.info(f"Loaded {len(pdf)} pages. Scroll down to read! 📜")

for page_num in range(len(pdf)):
    page = pdf.load_page(page_num)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # High-quality images
    img = Image.open(io.BytesIO(pix.tobytes("png")))

    st.image(img, use_container_width=True)  # Display each page as an image

st.success("🎉 You have reached the end of the magazine!")