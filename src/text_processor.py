# src/text_processor.py

import re

def clean_text(text):
    """Cleans the input text by converting to lowercase and removing extra whitespace."""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespaces with a single space
    text = text.strip()  # Remove leading/trailing whitespace
    return text