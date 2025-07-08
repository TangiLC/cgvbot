import mysql.connector as mysql

def get_connection():
    utilisateurs=[]
    bdd=mysql.connect(
        host='localhost',
        password='example',
        database='logs',
        port=3306
    )
    cursor=bdd.cursor()
    
    query="SELECT * FROM utilisateurs"
    
    