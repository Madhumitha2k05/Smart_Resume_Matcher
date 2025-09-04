# app.py

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import our custom modules from the src folder
from src.resume_parser import read_resume
from src.text_processor import clean_text
from src.semantic_matcher import get_match_score

# Configure the upload folder
UPLOAD_FOLDER = 'data/resumes/'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# A simple function to check for allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    """Renders the main upload page."""
    return render_template('index.html')

# IMPORTANT: The route is changed from /match to /find_role
@app.route('/find_role', methods=['POST'])
def find_role():
    """Handles the form submission, finds the best role for a single resume."""
    if 'job_descriptions' not in request.form or 'resume' not in request.files:
        return redirect(request.url)

    job_descriptions_text = request.form['job_descriptions']
    resume_file = request.files['resume']

    # Check if the user submitted the form without files/text
    if not job_descriptions_text or resume_file.filename == '':
        return redirect(request.url)
    
    # --- NEW LOGIC STARTS HERE ---

    results = []
    
    # 1. Process the uploaded resume
    if resume_file and allowed_file(resume_file.filename):
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)

        resume_text = read_resume(filepath)
        cleaned_resume = clean_text(resume_text)

        # 2. Split the job descriptions text into a list
        # We use '---' as a separator for different jobs
        job_descriptions = job_descriptions_text.split('---')

        # 3. Loop through each job description and find the score
        for jd_text in job_descriptions:
            if jd_text.strip():  # Make sure it's not an empty string
                cleaned_jd = clean_text(jd_text)
                
                # Use the first line of the JD as its title
                # Or set a default title if the JD is empty
                job_title = jd_text.strip().split('\n')[0] or "Untitled Job"

                score = get_match_score(cleaned_jd, cleaned_resume)
                
                results.append({'job_title': job_title, 'score': score})
    
        # 4. Sort the results by score in descending order
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # Pass the resume filename to the template to display it
        return render_template('results.html', results=results, resume_filename=filename)

    return redirect(request.url)


if __name__ == '__main__':
    # Create the upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)