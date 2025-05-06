# TLDV Conversation Extractor

A simple tool to extract clean conversation transcripts from TLDV HTML.

## Features

- Extract speaker names and dialogue from TLDV transcripts
- Format conversations in a clean, readable format
- Works entirely in the browser - no data is sent to any server
- Download the extracted conversation as a text file
- Copy the extracted conversation to clipboard

## How to Use

1. Go to your TLDV transcript page
2. Right-click on the transcript container and select "Inspect Element"
3. Find the `<div id="transcript-container">` element
4. Right-click on it and select "Copy" → "Copy outerHTML"
5. Paste the copied HTML into the tool
6. Click "Extract Conversation" to process the transcript
7. Use the "Download" button to save the result as a text file

## Privacy

This tool works entirely in your browser. No data is sent to any server.
