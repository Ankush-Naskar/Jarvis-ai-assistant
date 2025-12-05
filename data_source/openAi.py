from openai import OpenAI
import user_settings

def AI(prompt):
    try:
        client = OpenAI(api_key=user_settings.OPENAI_API_KEY)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return completion.choices[0].message.content.strip()
    
    except Exception as e:
        return "Sorry, I couldn't process that right now."