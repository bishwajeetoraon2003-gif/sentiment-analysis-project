\# Sentiment Analysis Project



\## 1. Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to classify customer reviews into three sentiment categories: Positive, Negative, and Neutral.



\## 2. Dataset

The project uses a dataset containing 10,000 customer reviews.



The dataset includes:

\- `review\_id`

\- `review\_text`

\- `sentiment`

\- `category`

\- `source`



\## 3. Technologies Used

\- Python

\- Pandas

\- Scikit-learn

\- TF-IDF Vectorization

\- Logistic Regression

\- Multinomial Naive Bayes

\- Streamlit

\- Joblib



\## 4. Project Features

\- Data cleaning and exploration

\- Sentiment distribution visualization

\- Text preprocessing

\- TF-IDF feature extraction

\- Machine Learning model training and evaluation

\- Cross-validation and hyperparameter tuning

\- Saved Machine Learning pipeline

\- Interactive Streamlit web application



\## 5. Project Structure

\- `Data/` — Dataset files

\- `models/` — Saved Machine Learning model

\- `notebook/` — Jupyter Notebook

\- `app.py` — Streamlit application

\- `requirements.txt` — Required Python libraries

\- `README.md` — Project documentation



\## 6. How to Run the Project



Install the required libraries:



```bash

pip install -r requirements.txt

```



Run the Streamlit application:



```bash

streamlit run app.py

```



Open the local URL shown in the terminal to use the application.



\## 7. How to Use

1\. Open the Streamlit application.

2\. Enter a customer review in the text box.

3\. Click \*\*Analyze Sentiment\*\*.

4\. View the predicted sentiment.



\## 8. Output

The application predicts one of three classes:

\- Positive

\- Negative

\- Neutral



\## 9. Notes

Model performance should be interpreted carefully because the dataset contains many repeated review texts. Performance on new, unseen real-world reviews may differ.

