from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Niveles con fotos de tu grupo de amigos y mensajes al desbloquear
    niveles = [
        {
            "id": 1,
            "titulo": "Abrazos y risas",
            "img": "/static/img/amigo1.jpg",
            "mensaje": "¡Qué buenos recuerdos!",
            "dificultad": 3  # Matriz 3x3 (9 piezas)
        },
        {
            "id": 2,
            "titulo": "Amor",
            "img": "/static/img/amigo2.jpg",
            "mensaje": "¡Manitos!",
            "dificultad": 3  # Matriz 3x3 (9 piezas)
        },
        {
            "id": 3,
            "titulo": "Olimpiadas amor",
            "img": "/static/img/amigo3.jpg",
            "mensaje": "¡Abrazos y risas!",
            "dificultad": 3
        },
        {
            "id": 4,
            "titulo": "08",
            "img": "/static/img/amigo4.jpg",
            "mensaje": "¡08 por siempre!",
            "dificultad": 3
        },
        # --- NUEVOS NIVELES AQUÍ ---
        {
            "id": 5,
            "titulo": "Fotitos divertidas",
            "img": "/static/img/amigo5.jpg",
            "mensaje": "¡Fotos inolvidables!",
            "dificultad": 3
        }
    ]
    return render_template('index.html', niveles=niveles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)