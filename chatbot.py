from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
INPUT_FILE = "train.jsonl"

client = OpenAI()


################### Saisie du prompt par l'utilisateur ########################
def saisie_utilisateur():
    pr=input("Comment puis-je vous aider ?")
    return pr

################### Validation de l'existance du prompt dans la BDD ##########
def existe_en_bdd(prompt):
    resp = None   #SQL QUERY
    # SELECT EXISTS (SELECT response FROM logs WHERE prompt==prompt);
    # To Do Connecteur SQL, validation ?  else return None
    return resp

################### Envoi du prompt au chatbot ################################
def envoi_au_chatbot(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-nano-2025-04-14",
            input=prompt
        )
    except Exception as e:
        affiche_message(f"Erreur lors de l'envoi au chatbot : {e}")
        return None
    else :
       stockage_log(prompt,response)
       affiche_message(response)
       

################### Affichage d'un message dans le terminal ###################       
def affiche_message(mssg):
  print(f"%>{mssg}")
  
################### Stockage d'une nouvelle entrée dans les logs ##############
def stockage_log(prompt,response):
    #mysql-bdd 
    #INSERT in Logs(date,prompt,response)
    #VALUES (CURRENT_TIMESTAMP,prompt,response);
    return

################### Proposition d'une nouvelle question #######################
def nouvelle_question():
  new = input("Souhaitez-vous poser une autre question (O/N) ? ")
  if new.lower() == "o":
    return True
  else:
    return False
  
################### MAIN ######################################################
def main():
  new_try=True
  while new_try:
    prompt=saisie_utilisateur()
    
    try :resp=existe_en_bdd(prompt)
    except Exception as e:
      affiche_message("Erreur accès BDD")
      continue
    else : 
      if resp !=None :
        affiche_message(resp)
      else : 
        resp=envoi_au_chatbot(prompt)
        
    new_try = nouvelle_question()
      

################### Lancement de Main #########################################
if __name__ == "__main__":
    main()  
  