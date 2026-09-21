from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Niveles con fotos de tu grupo de amigos y mensajes al desbloquear
    niveles = [
        {
            "id": 1,
            "titulo": "Carnaval Juntos",
            "img": "/static/img/amigo1.jpg",
            "mensaje": "¡Qué buenos recuerdos!",
            "dificultad": 3  # Matriz 3x3 (9 piezas)
        },
        {
            "id": 2,
            "titulo": "Carnaval X2",
            "img": "/static/img/amigo5.jpg",
            "mensaje": "¡Los zapatos de Melvin bien perdidos en el taxi!",
            "dificultad": 3  # Matriz 3x3 (9 piezas)
        },
        {
            "id": 3,
            "titulo": "En el cumpleaños de Brit",
            "img": "/static/img/amigo2.jpg",
            "mensaje": "¡Que bien lo pasamos!",
            "dificultad": 3
        },
        {
            "id": 4,
            "titulo": "Partido de la Seleccion Juntos",
            "img": "/static/img/amigo3.jpg",
            "mensaje": "¡Siempre unidos pase lo que pase!",
            "dificultad": 3
        },
        # --- NUEVOS NIVELES AQUÍ ---
        {
            "id": 5,
            "titulo": "Beber en las Peñas",
            "img": "/static/img/amigo4.jpg",
            "mensaje": "¡Videos inolvidables!",
            "dificultad": 3
        }
    ]
    return render_template('index.html', niveles=niveles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)