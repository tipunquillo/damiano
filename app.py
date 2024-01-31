from flask import Flask
app = Flask(__name__)

@app.route('/healthz') 
def healthCheck():
    return "OK"

if __name__ == "__main__":
   app.run(host ='0.0.0.0', PORT = 3000)
