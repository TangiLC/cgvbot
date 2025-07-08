from openai import OpenAI
from dotenv import load_dotenv
import os
 
load_dotenv()
OPENAI_FILE_ID = os.getenv("OPENAI_FILE_ID")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
 
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
 