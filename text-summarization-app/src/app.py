from flask import Flask, request, jsonify
from utils.data_preprocessing import preprocess_text
from utils.summarization_methods import extractive_summary, abstractive_summary

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Text Summarization App!"

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and (file.filename.endswith('.txt') or file.filename.endswith('.pdf')):
        text = file.read().decode('utf-8') if file.filename.endswith('.txt') else extract_text_from_pdf(file)
        processed_text = preprocess_text(text)
        
        summary_type = request.form.get('summary_type', 'extractive')
        if summary_type == 'extractive':
            summary = extractive_summary(processed_text)
        else:
            summary = abstractive_summary(processed_text)
        
        return jsonify({'summary': summary}), 200
    
    return jsonify({'error': 'Invalid file format'}), 400

def extract_text_from_pdf(file):
    # Function to extract text from PDF file
    import PyPDF2
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == '__main__':
    app.run(debug=True)