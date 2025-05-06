# TLDV Conversation Extractor

A tool to extract clean conversation transcripts from TLDV HTML, available as both a web app and a Python script.

## 🚀 Live Demo

Try the web version: [TLDV Conversation Extractor](https://nimble-dango-bba094.netlify.app)

## 🎯 What It Does

This tool extracts clean, readable conversation transcripts from TLDV (The Long Distance Video) meeting recordings. It processes the HTML of a TLDV transcript and converts it into a simple text format with speaker names and their dialogue.

## 📋 Example Output

```
Speaker 1: Not at the moment. No. Yeah, that's
Speaker 2: It. Listen, listen. Now and Another another project too. Pretty cool. Eh
Speaker 1: Um, what are you talking about this page?
```

## 🌐 Web Version

### Features
- Works entirely in your browser - no data is sent to any server
- Privacy-focused: all processing happens locally
- Download the extracted conversation as a text file
- Copy the extracted conversation to clipboard
- No installation or dependencies required

### How to Use the Web Version
1. Visit [TLDV Conversation Extractor](https://nimble-dango-bba094.netlify.app)
2. Go to your TLDV transcript page
3. Right-click on the transcript container and select "Inspect Element"
4. Find the `<div id="transcript-container">` element
5. Right-click on it and select "Copy" → "Copy outerHTML"
6. Paste the copied HTML into the tool
7. Click "Extract Conversation" to process the transcript
8. Use the "Download" or "Copy to Clipboard" buttons as needed

### Installation (For Developers)

Want to host your own version? You have several options:

#### Netlify
1. Fork this repository
2. Sign up for [Netlify](https://app.netlify.com/)
3. Click "New site from Git" and select your forked repository
4. Configure build settings (leave defaults)
5. Click "Deploy site"

#### Cloudflare Pages
1. Fork this repository
2. Sign up for [Cloudflare Pages](https://pages.cloudflare.com/)
3. Create a new project and connect your GitHub account
4. Select your forked repository
5. Configure with these settings:
   - Build command: (leave empty)
   - Build output directory: `/`
6. Click "Save and Deploy"

#### Vercel
1. Fork this repository
2. Sign up for [Vercel](https://vercel.com/)
3. Create a new project and import your forked repository
4. Configure with default settings
5. Click "Deploy"

## 💻 Python Script Version

For those who prefer a command-line tool or want to process files in batch, we provide a Python script.

### Requirements
- Python 3.6+
- BeautifulSoup4 (`pip install beautifulsoup4`)

### Installation
```bash
# Clone the repository
git clone https://github.com/barshy/tldv-transcript-extractor-.git

# Navigate to the directory
cd tldv-transcript-extractor-

# Install dependencies
pip install -r requirements.txt
```

### Usage
```bash
# Process a single file
python extract_conversation.py input_file.txt [output_file.txt]

# If output file is not specified, result is printed to console
python extract_conversation.py conversation1.txt
```

### Python Script Features
- Process TLDV transcript HTML files from the command line
- Save output to a file or print to console
- Can be integrated into other Python projects
- Suitable for batch processing multiple files

## 🔒 Privacy

Both versions (web and Python) process all data locally. Your transcript data never leaves your computer.

## 💡 Technical Details

- Web version: Built with vanilla HTML, CSS, and JavaScript
- Python version: Uses BeautifulSoup4 for HTML parsing
- No external API calls or data collection

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
