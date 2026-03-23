import re
import streamlit as st
import joblib
import gdown
import os

# Google Drive File IDs
clf_id = "1pssoPoSI2RZ8r3gXyodXne0euLW4UYvt"
tfidf_id = "1mqeWB4Nt6T6yxQwE2EZwCwUN9v7rcnp0"

# Download model files if not present the model files were too large for github 
if not os.path.exists("clf.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={clf_id}", "clf.pkl", quiet=False)

if not os.path.exists("tfidf.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={tfidf_id}", "tfidf.pkl", quiet=False)



# Load the model and vectorizer
tfidf = joblib.load(open('tfidf.pkl', 'rb'))
clf = joblib.load(open('clf.pkl', 'rb'))



# ---------- TEXT CLEANING FUNCTION ----------
def clean_resume(resume_text):
    cleanText = re.sub('http\S+\s*', ' ', resume_text)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s*', ' ', cleanText)
    cleanText = re.sub('@\S+', ' ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', r' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    cleanText = re.sub('\r\n', ' ', cleanText)
    return cleanText


# ---------- STREAMLIT APP ----------
def main():
    st.title("📄 Resume Screening App")

    uploaded_file = st.file_uploader('Upload Resume', type=['pdf', 'docx', 'doc', 'txt'])

    if uploaded_file is not None:
        # Read uploaded file
        resume_bytes = uploaded_file.read()
        try:
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        # Clean the text
        cleaned_resume = clean_resume(resume_text)

        # Transform using TF-IDF
        cleaned_tfidf = tfidf.transform([cleaned_resume])

        # Predict category
        prediction_id = clf.predict(cleaned_tfidf)[0]

        # Map to category
        category_mapping = {
            0: 'Advocate', 1: 'Arts', 2: 'Automation Testing', 3: 'Blockchain',
            4: 'Business Analyst', 5: 'Civil Engineer', 6: 'Data Science',
            7: 'Database', 8: 'DevOps Engineer', 9: 'DotNet Developer',
            10: 'ETL Developer', 11: 'Electrical Engineering', 12: 'HR',
            13: 'Hadoop', 14: 'Health and Fitness', 15: 'Java Developer',
            16: 'Mechanical Engineer', 17: 'Network Security Engineer',
            18: 'Operations Manager', 19: 'PMO', 20: 'Python Developer',
            21: 'SAP Developer', 22: 'Sales', 23: 'Testing', 24: 'Web Designing'
        }

        category_name = category_mapping.get(prediction_id, 'Unknown')
        st.success(f"✅ Predicted Category: **{category_name}**")


if __name__ == '__main__':
    main()
