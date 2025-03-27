import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="📖 Sangam Magazine", layout="wide")

# Load PDF
PDF_FILE = "Sangammain.pdf"  # Ensure this file is in the same directory

st.title("📖 Sangam Annual Magazine 2023-24")

# Open PDF
pdf = fitz.open(PDF_FILE)

# Zoom slider
zoom = st.slider("🔍 Zoom Level", 1.0, 3.0, 2.0, 0.1)  # Default zoom = 2.0

# Search box
search_query = st.text_input("🔎 Search for text in the magazine", "")

# Page navigation
page_num = st.number_input("📖 Go to page", min_value=1, max_value=len(pdf), step=1) - 1

# Load selected page
page = pdf.load_page(page_num)
pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))  # Apply zoom
img = Image.open(io.BytesIO(pix.tobytes("png")))

# Display page
st.image(img, use_container_width=True)

# Search Functionality
if search_query:
    st.subheader("📌 Search Results:")
    found_pages = []
    for i, p in enumerate(pdf):
        text = p.get_text("text")
        if search_query.lower() in text.lower():
            found_pages.append(i + 1)  # Store 1-based index

    if found_pages:
        st.write(f"✅ Found `{search_query}` on pages: {', '.join(map(str, found_pages))}")
    else:
        st.write(f"❌ No results found for `{search_query}`.")

st.success("🎉 You have reached the end of the magazine!")
