# 📄 Resume Screening App

An intelligent resume screening system that automatically classifies resumes into job categories using Machine Learning (TF-IDF + SVM). Built with Python, Scikit-learn, and Streamlit.

---

## 🚀 Demo

Upload a resume in PDF, DOCX, or TXT format and instantly get the predicted job category.

Live Demo:[Click Here](https://urd2bwhnk3gjzhkrqtspzv.streamlit.app/)

---

## 📌 Features

- Supports resume upload in **PDF**, **DOCX**, and **TXT** formats
- Cleans and preprocesses raw resume text (removes URLs, hashtags, special characters)
- Classifies resumes into **25 job categories** using a trained SVM model
- Interactive web UI built with **Streamlit**
- Option to view extracted text from the uploaded resume

---

## 🗂️ Job Categories Supported

| | | |
|---|---|---|
| Data Science | Java Developer | DevOps Engineer |
| HR | Business Analyst | Network Security Engineer |
| Advocate | SAP Developer | PMO |
| Arts | Automation Testing | Database |
| Web Designing | Electrical Engineering | Hadoop |
| Mechanical Engineer | Operations Manager | ETL Developer |
| Sales | Python Developer | DotNet Developer |
| Health and Fitness | Civil Engineer | Blockchain |
| Testing | | |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| ML Model | SVM (Support Vector Classifier) |
| Vectorization | TF-IDF |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |

---

## 📁 Project Structure

```
resume-screening-app/
│
├── app.py                          # Streamlit web app
├── resume_screening.ipynb  # Model training notebook
├── requirements.txt                # Project dependencies
│
├── UpdatedResumeDataSet.csv        # Dataset (download separately)
│
├── clf.pkl                         # Trained SVM model (generated after training)
├── tfidf.pkl                       # TF-IDF vectorizer (generated after training)
└── encoder.pkl                     # Label encoder (generated after training)
```

> ⚠️ The `.pkl` model files are not included in this repository. You need to generate them by running the notebook first (see Setup instructions below).

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-screening-app.git
cd resume-screening-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
pip install streamlit PyPDF2 python-docx
```

### 3. Download the Dataset
Download `UpdatedResumeDataSet.csv` from [Kaggle](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset) and place it in the project root folder.

### 4. Train the Model (Generate `.pkl` files)
Open and run all cells in the Jupyter notebook:
```bash
jupyter notebook Resume_Screening_with_Python.ipynb
```
This will generate `clf.pkl`, `tfidf.pkl`, and `encoder.pkl` in your project folder.

### 5. Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **Data Loading** — Loads `UpdatedResumeDataSet.csv` containing resumes across 25 job categories
2. **Class Balancing** — Oversamples minority categories to prevent bias
3. **Text Cleaning** — Removes URLs, mentions, hashtags, special characters, and extra whitespace
4. **Encoding** — Converts category labels to numeric values using `LabelEncoder`
5. **Vectorization** — Transforms cleaned resume text into TF-IDF feature vectors
6. **Model Training** — Trains and compares KNN, SVM, and Random Forest classifiers
7. **Saving** — Best model (SVM) along with TF-IDF and encoder are saved as `.pkl` files
8. **Prediction** — Streamlit app loads the saved model and predicts category for new resumes

---

## 📊 Model Performance

Three classifiers were trained and evaluated:

| Model | Notes |
|-------|-------|
| K-Nearest Neighbors (KNN) | Baseline model |
| **Support Vector Machine (SVM)** ✅ | **Best performer — used in production** |
| Random Forest | Ensemble approach |

---

## 🖼️ App Preview

```
📤 Upload a resume (PDF / DOCX / TXT)
       ↓
🧹 Text extraction & cleaning
       ↓
🔢 TF-IDF vectorization
       ↓
🤖 SVM prediction
       ↓
✅ Predicted Category: "Data Science"
```

---

## 📦 Requirements

See `requirements.txt`. Key packages:
- **'streamlit'
'scikit-learn'
'pandas'
'numpy'
'joblib'
'gdown'**

---

## 🙋‍♀️ Author

**Neelu Kushwaha**  
B.Tech CSE (AI & ML) | Dronacharya College of Engineering, Gurgaon  
🔗 [GitHub](https://github.com/neelu741) • [Portfolio](https://neelukushwaha.netlify.app)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
