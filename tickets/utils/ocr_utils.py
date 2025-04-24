from PIL import Image
import pytesseract
import re

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def find_total_cost(text):
    lines = text.split('\n')
    candidates = []
    for line in lines:
        if 'total' in line.lower():
            numbers = re.findall(r'\d+[\.,]?\d*', line)
            if numbers:
                try:
                    num = float(numbers[-1].replace(',', '').replace(' ', ''))
                    candidates.append(num)
                except ValueError:
                    pass
    return candidates[-1] if candidates else None
