import random
from google import genai
from app.config import Config

client = genai.Client(api_key=Config.GEMINI_API_KEY)

prompts = [
    "Dame una sola frase motivacional para comenzar el día.",
    "Proporcióname una frase motivacional corta y poderosa para inspirar mi día.",
    "Escribe una frase positiva y motivacional para empezar el día con energía.",
    "Dame una frase inspiradora y breve para enfocarme en mis metas hoy.",
    "Proporcióname una frase que me inspire a ser mejor cada día."
]

generated_responses = []

def chat_with_gemini():
    prompt = random.choice(prompts)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    
    if response.text:
        while response.text in generated_responses:
            print("Generando nueva frase...")
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
        
        generated_responses.append(response.text)
        
        print(f"Pregunta: {prompt}")
        print(f"Respuesta de Gemini: {response.text}")
        return response.text
    else:
        print("Error al obtener la respuesta de Gemini.")
        return "¡Sigue adelante y no te detengas!" 
    