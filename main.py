import streamlit as st
from PIL import Image
import pytesseract
import re

def extract_text_from_image(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def find_total_cost(extracted_text):
    lines = extracted_text.split('\n')
    candidates = []
    
    for line in lines:
        if 'total' in line.lower():
            numbers = re.findall(r'\d+[\.,]?\d*', line)
            if numbers:
                last_number_str = numbers[-1]
                last_number_clean = last_number_str.replace(',', '').replace(' ', '')
                try:
                    last_number = float(last_number_clean)
                    candidates.append(last_number)
                except ValueError:
                    continue
    
    return candidates[-1] if candidates else None

def main():
    st.title("Bill Text Extraction using OCR")
    st.write("Upload an image of a bill, and we'll extract the text and total cost for you!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Bill", use_container_width=True)

        extracted_text = extract_text_from_image(image)
        
        st.write("Extracted Text:")
        st.write(extracted_text)

        total_cost = find_total_cost(extracted_text)
        if total_cost is not None:
            st.success(f"**Total Cost:** Rs {total_cost:.2f}")
        else:
            st.warning("Could not find the total cost in the extracted text.")

if __name__ == "__main__":
    main()