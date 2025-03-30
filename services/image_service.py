import random
import requests
from app.config import Config

def get_image_from_pexels(query):
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": Config.PEXELS_API_KEY
    }
    params = {
        "query": query,
        "per_page": 10, 
        "page": 1  
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if data['total_results'] == 0:
            return None  

        total_pages = (data['total_results'] // 10) + (1 if data['total_results'] % 10 > 0 else 0)

        params["page"] = random.randint(1, total_pages)

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if 'photos' in data and len(data['photos']) > 0:
            image_url = random.choice(data['photos'])['src']['original']
            return image_url

    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API de Pexels: {e}")
        return None

    return None  
