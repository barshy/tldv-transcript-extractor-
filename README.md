# TLDV Conversation Extractor

A simple tool to extract clean conversation transcripts from TLDV HTML.

## 🚀 Live Demo

Try it now: [TLDV Conversation Extractor](https://tldv-transcript-extractor.netlify.app)

## 🎯 What It Does

This tool helps you extract clean, readable conversation transcripts from TLDV (The Long Distance Video) meeting recordings. It takes the HTML of a TLDV transcript and converts it into a simple text format with speaker names and their dialogue.

## ✨ Features

- Extract speaker names and dialogue from TLDV transcripts
- Format conversations in a clean, readable format
- Works entirely in the browser - no data is sent to any server
- Download the extracted conversation as a text file
- Copy the extracted conversation to clipboard
- Privacy-focused: all processing happens locally in your browser
- No account or login required

## 🔍 How to Use

1. Go to your TLDV transcript page
2. Right-click on the transcript container and select "Inspect Element"
3. Find the `<div id="transcript-container">` element
4. Right-click on it and select "Copy" → "Copy outerHTML"
5. Paste the copied HTML into the tool
6. Click "Extract Conversation" to process the transcript
7. Use the "Download" button to save the result as a text file or "Copy to Clipboard" to copy it

## 📋 Example Output

```
Stuart Spratt: Not at the moment. No. Yeah, that's
Fernando Barsh: It. Listen, listen. Now and Another another project too. Pretty cool. Eh
Stuart Spratt: Um, what are you talking about this page?
Fernando Barsh: But this there's something that it looks really cool, too.
```

## 🔒 Privacy

This tool works entirely in your browser. No data is sent to any server. Your transcript data never leaves your computer.

## 💻 Technical Details

- Built with vanilla HTML, CSS, and JavaScript
- No external dependencies or frameworks
- Uses the browser's built-in DOMParser to process HTML
- Implements the Blob API for file downloads

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [TLDV](https://tldv.io) for their meeting recording service
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for inspiring the HTML parsing approach
