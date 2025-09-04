# Smart_Resume_Matcher

An intelligent recruitment tool built with Flask and powered by semantic search to streamline the initial candidate screening process. This project goes beyond simple keyword matching to understand the contextual meaning of resumes and job descriptions, providing a ranked and detailed analysis of candidates.

### ✨ Live Demo

**You can view the live deployed application here:** [https://hr-intelligence-dashboard.onrender.com](https://hr-intelligence-dashboard.onrender.com) 
*(Note: The app is hosted on a free tier and may take 30-60 seconds to wake up on the first visit.)*

---

### ## 📸 Application Preview


*(A screenshot of the main dashboard showing a ranked list of candidates with detailed insights.)*

---

## 💡 Key Features

* **Semantic Search:** Utilizes `sentence-transformers` to understand the contextual similarity between resumes and job descriptions, providing a more accurate match score than traditional keyword search.
* **Ranked HR Dashboard:** Upload a single job description and multiple resumes to receive an instantly ranked dashboard of the best-fit candidates.
* **Explainable AI (XAI):** Doesn't just provide a score, but explains *why* a candidate is a good match by performing a detailed skill-gap analysis.
* **Side-by-Side Skill Comparison:** A visual UI that highlights matching skills (✅) and missing skills (❌) for quick and easy evaluation.
* **Achievement Extraction:** Automatically identifies and extracts quantifiable achievements (e.g., "Increased sales by 20%") from resumes to give a deeper insight into a candidate's impact.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **ML/NLP:** PyTorch, Sentence-Transformers, Scikit-learn
* **Frontend:** HTML, Bootstrap 5
* **Deployment:** Gunicorn, Render

---

## 📂 Project Structure

smart_resume_matcher/
|
|-- app.py                   # Main Flask application and dashboard logic.
|-- requirements.txt         # Project dependencies.
|-- skills.json              # Keywords for skill extraction.
|-- README.md                # You are here!
|
|-- src/                     # Core processing logic modules.
|   |-- init.py
|   |-- resume_parser.py     # Reads text from .pdf and .docx files.
|   |-- text_processor.py    # Cleans the raw text.
|   |-- semantic_matcher.py  # Calculates the semantic similarity score.
|   +-- keyword_extractor.py # Extracts skills and achievements.
|
|-- templates/               # HTML web pages.
|   |-- index.html           # The main upload page.
|   +-- dashboard.html       # The results dashboard with all features.
|
|-- data/
+-- resumes/             # Folder for temporary resume uploads.

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Madhumitha2k05/Smart_Resume_Matcher.git](https://github.com/Madhumitha2k05/Smart_Resume_Matcher.git)
    cd Smart_Resume_Matcher
    ```

2.  **Create and activate a virtual environment:**
    * On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```
    Open your browser and go to `http://127.0.0.1:5000`.

---

## 📖 How to Use

1.  Navigate to the homepage.
2.  Paste the full job description into the text area.
3.  Upload one or more resumes using the file selector.
4.  Click "Analyze Candidates" to view the interactive dashboard.

DEPLOYMENT LINK : https://smart-resume-matcher-3.onrender.com
