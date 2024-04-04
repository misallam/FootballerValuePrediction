import streamlit as st
import pandas as pd
import pickle

with open('linear_fifa_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler_fifa.pkl', 'rb') as file:
    scaler = pickle.load(file)

df = pd.read_csv("fifa_dataset.csv")
data_cleaned = df.dropna(subset=['Value'])
feature_names = data_cleaned.drop(columns=['ID', 'Name', 'Nationality', 'Club', 'Preferred Foot', 'Position', 'Contract Valid Until', 'Value', 'Wage'])
feature_names = feature_names.columns.tolist()

def predict_value(input_features):
    input_df = pd.DataFrame([input_features], columns=feature_names)
    input_scaled = scaler.transform(input_df)
    return model.predict(input_scaled)[0]

st.title('FIFA Player Value Prediction')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age (int)', min_value=16, max_value=45, value=25, step=1)
    overall = st.number_input('Overall (int)', min_value=46, max_value=94, value=70, step=1)
    potential = st.number_input('Potential (int)', min_value=48, max_value=95, value=75, step=1)

with col2:
    international_reputation = st.number_input('International Reputation (1-5)', min_value=1, max_value=5, value=1, step=1)
    skill_moves = st.number_input('Skill Moves (1-5)', min_value=1, max_value=5, value=3, step=1)
    height = st.number_input('Height (feet)', min_value=float(5.08), max_value=float(6.75), value=5.8, format="%.2f")

with col3:
    weight = st.number_input('Weight (lbs)', min_value=110, max_value=243, value=165, step=1)
    joined = st.number_input('Joined (Year)', min_value=1991, max_value=2018, value=2010, step=1)
    release_clause = st.number_input('Release Clause (€K)', min_value=13, max_value=228100, value=5000, step=100)

if st.button('Predict Player Value'):
    features = {
        'Age': age,
        'Overall': overall,
        'Potential': potential,
        'International Reputation': international_reputation,
        'Skill Moves': skill_moves,
        'Height': height,
        'Weight': weight,
        'Joined': joined,
        'Release Clause': release_clause
    }
    
    prediction = predict_value(features)
    st.subheader(f'Player Value is Nearly: {prediction:,.2f} $')
