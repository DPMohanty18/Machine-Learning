import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_website(url, output_file):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        text_content = soup.get_text()
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text_content)
        
        return f"Data successfully scraped and saved to {output_file}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Web Scraper")

url = st.text_input("Enter the website URL:")
output_file = st.text_input("Enter the output file name (with .txt extension):")

if st.button("Scrape Website"):
    if url and output_file:
        message = scrape_website(url, output_file)
        st.success(message)
    else:
        st.error("Please provide both a URL and an output file name.")
