# app.py

from flask import Flask
import os

app = Flask(__name__)

@app.route('/healthz') 
def healthCheck():
  print("/healthz endpoint llamado")
  return "OK"

if __name__ == "__main__":

    print("Iniciando servidor Flask...")
    
    PORT = os.getenv('PORT') if os.getenv('PORT') else 8080 
    
    app.run(host='0.0.0.0', port=PORT)
    
    print("Servidor Flask inicializado en puerto", PORT)
