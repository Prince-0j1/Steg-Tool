# StegApp Web 🔐

<div align="center">

![StegApp Logo](https://img.shields.io/badge/StegApp-Web-blue?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)

**Hide secrets in plain sight. All in your browser.**

[Live Demo](https://yourusername.github.io/stegapp) • [Report Bug](https://github.com/yourusername/stegapp/issues) • [Request Feature](https://github.com/yourusername/stegapp/issues)

</div>

---

## ✨ Features

<table>
<tr>
<td>

### 📸 **Image LSB Steganography**
Hide text in PNG/BMP images using Least Significant Bit encoding.

### 🎵 **Audio LSB Steganography**
Embed secrets in 16-bit PCM WAV files with minimal quality loss.

### 📝 **Zero-Width Text Encoding**
Conceal messages in plain text using invisible Unicode characters.

### 📁 **File Append Method**
Append any data to any file type for maximum flexibility.

</td>
<td>

### 🔒 **Password Protection**
Strong encryption using Web Crypto PBKDF2 + AES-GCM.

### 🚀 **100% Client-Side**
No servers, no uploads - complete privacy and security.

### 🌍 **Cross-Platform**
Works on any modern browser with JavaScript support.

### 🎨 **Modern UI**
Clean, responsive interface with dark/light mode support.

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/stegapp.git

# Navigate to the project directory
cd stegapp

# Open in your browser
open index.html
```

Or simply open `index.html` in any modern browser. No build tools required!

---

## 📖 How It Works

### Encoding Process 🔄

1. **Select Carrier File** - Choose an image, audio file, text document, or any file
2. **Enter Secret Message** - Type or paste your hidden text
3. **Choose Method** - Select the steganography technique
4. **Optional Password** - Encrypt your message with a password
5. **Encode & Download** - Save the stego file with your hidden message

### Decoding Process 🔍

1. **Upload Stego File** - Select the file containing hidden data
2. **Select Method** - Choose the same technique used for encoding
3. **Enter Password** - If protected, enter the password
4. **Extract** - Reveal the hidden message instantly

---

## 🛠️ Technology Stack

<div align="center">

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Encryption** | Web Crypto API (PBKDF2, AES-GCM) |
| **Audio Processing** | Web Audio API |
| **Image Processing** | Canvas API |
| **File Handling** | File API, Blob API |

</div>

---

## 🎯 Use Cases

### 🔐 **Private Communication**
Share sensitive information through innocent-looking files.

### 📚 **Digital Watermarking**
Protect your intellectual property with hidden signatures.

### 🎓 **Educational Purposes**
Learn about steganography and information hiding techniques.

### 🔬 **Data Forensics**
Practice extracting hidden information from files.

---

## 💻 Browser Support

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full Support |
| Firefox | ✅ Full Support |
| Safari | ✅ Full Support |
| Edge | ✅ Full Support |
| Opera | ✅ Full Support |

---

## 🚧 Roadmap

- [ ] Support for more image formats (JPEG, GIF)
- [ ] Video steganography support
- [ ] Drag-and-drop interface
- [ ] Batch processing
- [ ] Steganalysis tools
- [ ] Mobile app version
- [ ] Browser extension
- [ ] API for developers

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🔧 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

### Development Setup

```bash
# Install development dependencies
npm install -g live-server

# Start development server with live reload
live-server
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yourusername/stegapp/blob/main/LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by classical steganography techniques
- Built with modern web technologies
- Security principles from Web Crypto API specifications

---

## 📧 Contact

**Your Name** - [@yourusername](https://twitter.com/yourusername) - email@example.com

Project Link: [https://github.com/yourusername/stegapp](https://github.com/yourusername/stegapp)

---

<div align="center">

### ⭐ Star us on GitHub — it helps!

Made with ❤️ and JavaScript

</div>

---

## 🎨 Preview

<table>
<tr>
<td width="50%">
<h3 align="center">Encoding Interface</h3>
<img src="https://raw.githubusercontent.com/yourusername/stegapp/main/screenshots/encode.png" alt="Encoding Interface">
</td>
<td width="50%">
<h3 align="center">Decoding Interface</h3>
<img src="https://raw.githubusercontent.com/yourusername/stegapp/main/screenshots/decode.png" alt="Decoding Interface">
</td>
</tr>
<tr>
<td width="50%">
<h3 align="center">File Selection</h3>
<img src="https://raw.githubusercontent.com/yourusername/stegapp/main/screenshots/file-select.png" alt="File Selection">
</td>
<td width="50%">
<h3 align="center">Extracted Message</h3>
<img src="https://raw.githubusercontent.com/yourusername/stegapp/main/screenshots/extracted.png" alt="Extracted Message">
</td>
</tr>
</table>

---

## 🔒 Security Note

StegApp processes all data locally in your browser. No information is ever transmitted to any server. The encryption uses industry-standard algorithms and best practices.

### Security Features:

- ✅ Client-side processing only
- ✅ No data uploaded to servers
- ✅ Strong AES-GCM encryption
- ✅ PBKDF2 key derivation with configurable iterations
- ✅ No tracking or analytics

---

## 📚 Resources

- [Steganography 101](https://en.wikipedia.org/wiki/Steganography)
- [Web Crypto API Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)
- [LSB Steganography Explained](https://www.geeksforgeeks.org/lsb-based-image-steganography/)
- [WAV Audio Format](https://en.wikipedia.org/wiki/WAV)
- [Zero-Width Characters](https://en.wikipedia.org/wiki/Zero-width_character)

---

## 🏆 Contributors

<a href="https://github.com/yourusername/stegapp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/stegapp" />
</a>

---

<div align="center">

![Visitors](https://api.visitorbadge.io/api/visitors?path=yourusername%2Fstegapp&label=Visitors&countColor=%23263759)

</div>
