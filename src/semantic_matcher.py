# src/semantic_matcher.py

from sentence_transformers import SentenceTransformer, util

# Load the pre-trained model. This will be downloaded on the first run.
# 'all-MiniLM-L6-v2' is a fast and good model for semantic similarity.
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(job_description_text, resume_text):
    """
    Calculates the semantic similarity score between a job description and a resume.
    """
    # Encode the texts into vectors (embeddings)
    embedding1 = model.encode(job_description_text, convert_to_tensor=True)
    embedding2 = model.encode(resume_text, convert_to_tensor=True)

    # Calculate the cosine similarity score
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
    
    # The score is a tensor, get the numerical value and return it
    score = cosine_scores.item()
    
    return score