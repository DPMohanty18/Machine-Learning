import streamlit as st
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        return f"Error extracting text: {e}"
    return text

st.title("PDF Scraper")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
output_file = st.text_input("Enter output text file name (with .txt extension):")

if st.button("Extract and Save Text"):
    if uploaded_file and output_file:
        extracted_text = extract_text_from_pdf(uploaded_file)
        if extracted_text:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(extracted_text)
            st.success(f"Text extracted and saved to {output_file}")
        else:
            st.error("Failed to extract text from the PDF.")
    else:
        st.error("Please upload a PDF and provide an output file name.")
