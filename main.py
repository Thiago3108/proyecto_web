from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mostrar_primeros_auxilios():
    with open("Documento.txt", "r") as archivo:
        contenido = archivo.read()
    return render_template("base.html", contenido=contenido)

@app.route("/Formacion")
def mostrar_contenido():
    with open("Documento2.txt", "r") as archivo:
        contenido = archivo.read()
    return render_template("formacion.html", contenido=contenido)

@app.route("/Emergencia")
def mostrar_numeros_emergencia():
    with open("Documento3.txt", "r") as archivo:
        contenido = archivo.read()
    return render_template("Emergencia.html", contenido=contenido)

if __name__ == "__main__":
    app.run(debug=True)