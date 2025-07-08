from openai import OpenAI
from dotenv import load_dotenv
import os
 
load_dotenv()
 
OPENAI_FILE_ID = "file-3jHzjcLMQXJmxPfQeTThW8"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"
print("Using training file ID:", OPENAI_FILE_ID)
 
client = OpenAI()
 
ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model="gpt-4.1-nano-2025-04-14"
)
 
try:
    ft_job = client.fine_tuning.jobs.create(
        training_file=OPENAI_FILE_ID,
        model=OPENAI_MODEL
    )
    
    print("Fine Tune Job has been created with id", ft_job.id)
except Exception as e:
    print("Error creating fine tune job:", e)
 