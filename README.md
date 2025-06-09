# A website which tells what environment, factors, and hyperaramenters are needed for a food crop to grow better. It will use pytorch to train the models of recommending the factors upon telling the crop's name or picture. more to be added....
# 🌾 Krishi Mitr – Smart Crop Recommendation App

## 📌 About
Krishi Mitr is a Streamlit-powered web application that helps farmers and planners determine the most suitable crop to cultivate based on environmental conditions and soil nutrients.

## 🧠 Features
- 🔍 Search crop by name, state, and season
- 📊 Display of average agricultural requirements
- 🤖 ML-powered crop recommendation using TensorFlow
- 🖼️ Image preview of selected crop

## 📁 Dataset
The model and app use `merged_crop_data.csv`, which includes:
- Soil nutrients (N, P, K)
- Temperature, humidity, pH, rainfall
- Crop label, State, Season, Fertilizer, Pesticide usage

## 🛠️ Technologies
- Python, Pandas, NumPy
- TensorFlow + Keras
- Streamlit
- PIL for images

## 🚀 How to Run
```bash
streamlit run app.py
