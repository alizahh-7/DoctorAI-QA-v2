from google import genai

client = genai.Client(
    api_key="AIzaSyBNZK03Q8Q_q9NRQ1F5yyIqlctUEoB4Lew",
    http_options={"api_version": "v1"}   # 🔥 THIS IS THE FIX
)

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Say hello"
)

print(response.text)