# Q4 Code - Conversion probability (API)

import requests

url = 'http://localhost:9696/predict'

lead_q4 = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
}

response = requests.post(url, json=lead_q4).json()
print("Q4 API Response:", response)

prob = response['conversion_probability']
print(f"Conversion Probability: {prob:.3f}")