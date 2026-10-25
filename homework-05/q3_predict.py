# Q3 Code - Conversion probability (loaded model)

import pickle

# Load the frozen pipeline artifact
with open('pipeline.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Question 3 Lead Sample
lead_q3 = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41
}

# Compute conversion probability (class 1)
conversion_prob = pipeline.predict_proba([lead_q3])[0, 1]
print(f"Q3 Conversion Probability: {conversion_prob:.3f}")