# 🧠 Smart Summarizer

Smart Summarizer is a powerful AI-based web application that intelligently summarizes content from multiple formats, including plain text, PDFs, images, `.txt` files, and blog/article links. With user-defined prompt support and clean, downloadable summaries, it's perfect for productivity and knowledge compression.

🔗 **Live App:**  
👉 [Smart Summarizer on Google Cloud Run](https://smart-summarizer-259284759346.us-central1.run.app)

---

## ✨ Highlights

- 🧠 **Summarization with BART**: Uses `facebook/bart-large-cnn` via Hugging Face Transformers for high-quality extractive summaries.
- 💬 **Prompt-based Customization**: Accepts natural instructions like:
  - "Summarize in bullet points"
  - "Limit to 100 words"
  - "Make it sound professional"
- 🖼️ **Supports Various Input Types**:
  - Text 📝
  - PDF files 📄
  - Images (OCR with EasyOCR) 🖼️
  - .TXT files 📃
  - Blog/article URLs 🌐
- ☁️ **Cloud Uploads**:
  - Summaries downloadable as `.txt` and `.pdf`
  - Stored via pre-signed AWS S3 URLs
- 🎨 **Responsive UI**:
  - Bootstrap 5 frontend
  - Adaptive layout with scrollable output
  - Modern UX with clean prompt controls
- 🔐 **Security Built-In**:
  - CSRF protection via Flask-WTF
  - Rate limiting via Flask-Limiter

---

## 🛠️ Tech Stack

| Layer          | Tech                                |
|----------------|--------------------------------------|
| ⚙️ Backend      | Flask (Python)                       |
| 🤖 Model        | Hugging Face Transformers (BART)     |
| 🌐 Frontend     | HTML, Bootstrap 5                    |
| 📦 Deployment   | Google Cloud Run (4GiB RAM, 1 CPU)   |
| ☁️ Storage      | AWS S3 for file uploads              |
| 🧠 OCR          | EasyOCR (Python)                     |
| 🔐 Security     | Flask-WTF, Flask-Limiter             |

---

## ⚡ Performance Optimizations

- 🚀 Lazy loading of BART & EasyOCR reduces startup memory usage
- 🧠 Concurrency limited to 1 per instance to avoid memory crashes
- 💸 Cloud Run autoscaling limited to 2 instances for free-tier safety
- 🧹 Garbage filtering on OCR (removes unwanted links like CNN, Twitter)

---

<details>
<summary>📁 Click to view project structure</summary>

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

</details>

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
