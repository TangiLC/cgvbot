from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
fine_tuned_model = "ft:gpt-4.1-nano-2025-04-14:jn-formation::Bqy2C4rj"

response = client.responses.create(
    model=fine_tuned_model,
    #model="gpt-4.1-nano-2025-04-14",
    input="Puis-je être livré hors de France métropolitaine ?"
)

print(response.output_text)