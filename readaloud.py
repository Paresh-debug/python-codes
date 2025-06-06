import pyttsx3
import time
import re

def split_to_short_sentences(text, max_words=15):
    # Split the text into sentences at punctuation marks
    sentences = re.split(r'(?<=[.!?])\s+', text)
    short_sentences = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > max_words:
            # Break long sentences into chunks of up to max_words words
            for i in range(0, len(words), max_words):
                short_sentences.append(' '.join(words[i:i+max_words]))
        else:
            short_sentences.append(sentence)
    return short_sentences

def read_assignment(file_path):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)  # Adjust narration speed
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            text = line.strip()
            if text:  # Only process non-empty lines
                # Split the line into shorter sentences
                sentences = split_to_short_sentences(text, max_words=15)
                for sentence in sentences:
                    print(f"Reading: {sentence}")
                    engine.say(sentence)
                    engine.runAndWait()
                    time.sleep(5)  # Pause to give you time to write

# Use a raw string for Windows file path
file_path = r"C:\Users\pares\Downloads\WhatsApp ede\assignment.txt"
read_assignment(file_path)

