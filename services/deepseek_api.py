import requests
from googlesearch import search
from config import API_URL, API_KEY

def analyze_text(input_text):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"text": input_text}
    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if "disease" in result:
            return result

    search_query = f"Possible diseases for symptoms: {input_text}"
    search_results = list(search(search_query, num=3, stop=3, pause=2))
    return {"disease": "Unknown condition", "suggestion": "Consult a general physician.", "important_links": search_results}
