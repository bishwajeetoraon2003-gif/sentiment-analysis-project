
import streamlit as st
import joblib
import os

# Page settings
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬"
)

# Load the saved model
MODEL_PATH = os.path.join("models", "sentiment_pipeline.pkl")
model = joblib.load(MODEL_PATH)

# App title
st.title("💬 Sentiment Analysis App")
st.write("Enter a review below to predict its sentiment.")

# User input
review = st.text_area("Write your review here:")

# Predict sentiment
if st.button("Analyze Sentiment"):
    if review.strip():
        prediction = model.predict([review])[0]

        st.subheader("Prediction")

        if prediction == "Positive":
            st.success("😊 Positive Sentiment")
        elif prediction == "Negative":
            st.error("😞 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")
    else:
        st.warning("Please enter a review first.")
