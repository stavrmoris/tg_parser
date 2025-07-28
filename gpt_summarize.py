from google import genai
from config import *

client = genai.Client(api_key="AIzaSyDCdidFUZOuPfSxHwIAkvG7JwROdX9NwlQ")


def summ(posts):
    formatted_posts = "\n".join([f"- {post[1]}" for post in posts if post[1]])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{PROMPT}\n\n{formatted_posts}",
    )
    return response.text