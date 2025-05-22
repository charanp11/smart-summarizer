from flask import Flask, render_template, request, redirect
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename
import os
import uuid
import config

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = config.SECRET_KEY

csrf = CSRFProtect(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

@app.route('/')
def index():
    token = generate_csrf()
    return render_template('index.html', csrf_token=token)

@app.route('/summarize', methods=['POST'])
def summarize():
    from models.summarizer import generate_summary
    from utils.ocr_utils import extract_text_from_image
    from utils.link_utils import extract_from_url
    from utils.pdf_utils import extract_text_from_pdf
    from utils.txt_utils import extract_text_from_txt

    input_text = request.form.get('input_text', '').strip()
    instruction = request.form.get('instruction', '').strip()
    file = request.files.get('file')
    extracted_text = ""

    if input_text.startswith("http"):
        extracted_text = extract_from_url(input_text)

    elif file and file.filename != '':
        filename = secure_filename(file.filename)
        local_path = os.path.join("/tmp", filename)  
        
        try:
            file.save(local_path)

            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                extracted_text = extract_text_from_image(local_path)
            elif filename.lower().endswith('.pdf'):
                extracted_text = extract_text_from_pdf(local_path)
            elif filename.lower().endswith('.txt'):
                extracted_text = extract_text_from_txt(local_path)
            else:
                extracted_text = "⚠️ Unsupported file type."

        except Exception as e:
            print("❌ Error extracting file text:", e)
            extracted_text = f"⚠️ Failed to process uploaded file: {str(e)}"

        finally:
            if os.path.exists(local_path):
                os.remove(local_path)

    else:
        extracted_text = input_text

    if not extracted_text or extracted_text.startswith("⚠️"):
        summary = extracted_text if extracted_text else "⚠️ No content available to summarize."
    else:
        summary = generate_summary(extracted_text, instruction)

    print("Extracted text (preview):", extracted_text[:200])
    return render_template('result.html', summary=summary)


@app.route('/download_txt', methods=['POST'])
def download_txt():
    from utils.txt_utils import save_summary_as_txt
    from utils.s3_utils import upload_file_to_s3

    summary = request.form['summary']
    filename = f"{uuid.uuid4()}.txt"
    local_path = os.path.join("/tmp", filename)
    save_summary_as_txt(summary, local_path)
    s3_url = upload_file_to_s3(local_path, filename)
    os.remove(local_path)
    return redirect(s3_url)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    from utils.pdf_utils import save_summary_as_pdf
    from utils.s3_utils import upload_file_to_s3

    summary = request.form['summary']
    filename = f"{uuid.uuid4()}.pdf"
    local_path = os.path.join("/tmp", filename)
    save_summary_as_pdf(summary, local_path)
    s3_url = upload_file_to_s3(local_path, filename)
    os.remove(local_path)
    return redirect(s3_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
