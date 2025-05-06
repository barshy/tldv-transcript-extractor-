#!/usr/bin/env python3
import re
import sys
from bs4 import BeautifulSoup
from collections import defaultdict

def extract_conversation(file_path):
    """
    Extract conversation from tldv.io transcript HTML file
    and format it as clean text with speaker names.
    """
    # Read the input file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all paragraph elements that contain dialogue
    paragraphs = soup.find_all('p', {'data-index': True})
    
    conversation = []
    current_speaker = None
    current_text = []
    
    for p in paragraphs:
        # Extract speaker name
        speaker_element = p.find('span', {'data-speaker': 'true'})
        if speaker_element and speaker_element.find('span'):
            speaker = speaker_element.find('span').get_text()
            
            # If we have a new speaker, save the previous one's text
            if current_speaker and current_speaker != speaker and current_text:
                conversation.append((current_speaker, ' '.join(current_text)))
                current_text = []
            
            current_speaker = speaker
        
        # Extract all text spans in this paragraph
        text_spans = p.find_all('span', {'data-speaker': 'false'})
        for span in text_spans:
            text = span.get_text().strip()
            if text:
                current_text.append(text)
    
    # Add the last speaker's text
    if current_speaker and current_text:
        conversation.append((current_speaker, ' '.join(current_text)))
    
    return conversation

def format_conversation(conversation):
    """Format the conversation as requested"""
    formatted = []
    for speaker, text in conversation:
        formatted.append(f"{speaker}: {text}")
    return '\n'.join(formatted)

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_conversation.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        conversation = extract_conversation(input_file)
        formatted = format_conversation(conversation)
        
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(formatted)
            print(f"Conversation extracted and saved to {output_file}")
        else:
            print(formatted)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
