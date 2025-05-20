# 🧠 Smart Summarizer

Smart Summarizer is a powerful AI-based web application that enables users to generate custom summaries from a wide range of content inputs including text, PDFs, images, TXT files, and blog/article links. With support for user-defined prompts and dynamic formatting, the app delivers clean, downloadable summaries using secure AWS S3 integration.

> 🔒 Built with production-grade security, responsive UI, and a modular architecture — this project demonstrates real-world cloud, AI, and web development skills.

---

## 🚀 Live Demo

🔗 [Smart Summarizer App]()  

---

## ✨ Project Highlights

- 🧠 **AI Summarization with BART**: Uses `facebook/bart-large-cnn` via Hugging Face Transformers for high-quality, extractive text summarization.
- 💬 **User-Prompt Driven**: Accepts natural language instructions like:
  - “Summarize in 150 words”
  - “Bullet points only”
  - “Make it sound persuasive”
- 🖼️ **Multi-format Input Support**:
  - Plain text
  - PDF files
  - Images (OCR using Tesseract)
  - `.txt` documents
  - Blog/article links (scraped using BeautifulSoup)
- ☁️ **Cloud Integration**:
  - Summaries can be downloaded as `.txt` or `.pdf` files
  - Files are served through **pre-signed AWS S3 URLs**
- 🎨 **Modern UI/UX**:
  - Fully responsive Bootstrap 5 layout
  - Adaptive design for all screen sizes
  - Dropdown download options and smooth scrolling
- 🔐 **Security Features**:
  - CSRF protection (via Flask-WTF)
  - Rate limiting to prevent abuse (via Flask-Limiter)

---

## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| ⚙️ Backend   | Flask (Python) |
| 🧠 AI Model | Hugging Face Transformers (BART) |
| 🌐 Frontend | HTML, Bootstrap 5 |
| ☁️ Cloud    | AWS S3 for file delivery |
| 🧰 Utilities | Tesseract OCR, PyMuPDF, pdf2image |
| 🔐 Security | Flask-WTF (CSRF), Flask-Limiter |
| 📦 Deployment | Render (free-tier cloud app platform) |

---

## 📁 Project Structure

smart_summarizer/
├── app.py # Main Flask app
├── config.py # Config & environment variables
├── models/
│ └── summarizer.py # Summarization using BART
├── templates/
│ ├── index.html # Input UI
│ └── result.html # Output display
├── utils/
│ ├── ocr_utils.py # Image to text (OCR)
│ ├── pdf_utils.py # PDF text extraction & download
│ ├── txt_utils.py # TXT file reading
│ ├── link_utils.py # Blog/article scraping
│ └── s3_utils.py # AWS S3 upload/download logic
├── static/
│ └── style.css # Custom styles (Bootstrap-enhanced)
├── requirements.txt # Python dependencies
├── runtime.txt # Required for Render deployment
└── README.md

## 🧪 How to Run Locally

```bash
git clone https://github.com/charanp11/smart_summarizer.git
cd smart_summarizer
python -m venv venv
source venv/bin/activate  or use venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

You’ll need to create a .env file with:

SECRET_KEY=your_flask_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=your_region
