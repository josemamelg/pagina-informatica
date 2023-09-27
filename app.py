from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Puedes agregar tu lógica de Python aquí para generar contenido dinámico.
    contenido_python = "¡Hola desde Python!"

    return render_template('index.html', contenido_python=contenido_python)

if __name__ == '__main__':
       app.run(debug=True)
