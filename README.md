# 🖼️ HEIC Converter (Terminal Edition)

A simple Python-based CLI tool that converts `.heic` image files into `.jpg` format.  
More output formats (like `.png`, `.webp`, etc.) may be supported in future versions.

## 📦 Features

- ✅ Converts .heic files to .jpg using a simple terminal interface
- 📁 Accepts either a single file or an entire folder as input
- 🔍 Automatically detects all .heic images inside a given folder
- 🧠 Skips unsupported or invalid files with clear error messages
- 📂 Saves output images to a converted_images/ folder
- 🔁 Adds numeric suffixes (e.g. _1, _2, etc.) if duplicate filenames are detected
- 📈 Displays a summary: converted/total (e.g., 4/5 converted)
- ⚠️ Shows the filenames of any files that failed conversion
- 🕒 Displays total time taken for conversion
- 📝 For single file conversions, shows both the original and converted file paths

## 🚀 Getting Started

### 🧰 Requirements

- Python 3.8+
- `pillow` and `pillow-heif` for image handling

### Installation

```bash
git clone https://github.com/davmz/heic-converter.git
cd heic-converter
pip install -r requirements.txt
