import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def def_ciber():
     limite = 100
     a = 1
     b = 0
     numero = 0

     testeprimo = "2,"

     while b < limite:
     	primo = 1

     	for i in range(2,numero):
     		if numero % i == 0:
     			primo = 0
     			break
     	if (primo):
     		testeprimo = testeprimo + str(numero) + ","
     		b += 1
     		if(b % 10 == 0):
     			testeprimo = testeprimo + "</p>"
     	numero +=1
     return testeprimo

if __name__ == "__main__":
        app.debug = True
        app.run()
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port= port)

