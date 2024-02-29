from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
    
@app.route("/")
def holaflask():
    return "<h1>¡hola flask!</h1> <hr>"

#primer punto
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=round((nota1*30)/100+(nota2*30)/100+(nota3*40)/100,2)
    return f"<h1> El resultado es: {resultado}</h1> <hr>"

#segundo punto
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=60):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

#tercer punto
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>") 
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1> El arreglo aleatorio es: {arreglo} </h1> <hr>"    
                       

if __name__ == '__main__':
    app.run(debug=True)