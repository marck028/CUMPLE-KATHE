from flask import Flask, render_template
import os

app = Flask(__name__)

# Configuración para producción
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Títulos y descripciones personalizables para cada foto
PHOTO_CAPTIONS = {
    1: {"title": "Nuestro Primer Encuentro", "description": "El momento en que nuestros corazones se reconocieron por primera vez."},
    2: {"title": "Tu Sonrisa", "description": "Esa sonrisa que ilumina mis días y hace que todo valga la pena."},
    3: {"title": "Apoyo Mutuo", "description": "Siempre estaré aquí para ti, como tú lo estás para mí."},
    4: {"title": "Momento de Risa", "description": "Porque contigo hasta los días grises se vuelven coloridos."},
    5: {"title": "Nuestro Lugar Especial", "description": "Ese rincón del mundo que se volvió mágico cuando llegaste tú."},
    6: {"title": "Miradas Cómplices", "description": "Esas miradas que dicen más que mil palabras."},
    7: {"title": "Atardecer Juntos", "description": "Viendo el sol esconderse, sabiendo que mañana será otro día contigo."},
    8: {"title": "Tu Felicidad", "description": "Verte feliz es mi mayor logro y mi razón de ser."},
    9: {"title": "Aventuras", "description": "Cada salida contigo es una nueva aventura por descubrir."},
    10: {"title": "Complicidad", "description": "Somos el equipo perfecto en esta hermosa travesía."},
    11: {"title": "Dulces Momentos", "description": "Los pequeños detalles que hacen grande nuestro amor."},
    12: {"title": "Tu Esencia", "description": "Eres auténtica, hermosa y perfecta tal como eres."},
    13: {"title": "Creciendo Juntos", "description": "Aprendiendo y creciendo de la mano día a día."},
    14: {"title": "Nuestros Sueños", "description": "Construyendo un futuro lleno de amor y esperanza."},
    15: {"title": "Conexión Especial", "description": "Esa conexión única que solo nosotros entendemos."},
    16: {"title": "Momentos Íntimos", "description": "Los susurros, las caricias y la ternura compartida."},
    17: {"title": "Celebrando", "description": "Cada logro tuyo es también una celebración mía."},
    18: {"title": "Caminando Juntos", "description": "De la mano, enfrentando el mundo y creando nuestra propia historia."},
    19: {"title": "Naturalidad", "description": "Contigo puedo ser yo mismo sin máscaras ni pretensiones."},
    20: {"title": "Amor Verdadero", "description": "Lo que tenemos es real, puro y para toda la vida."},
    21: {"title": "Nuestro Presente", "description": "Viviendo cada momento como si fuera el más importante."},
    22: {"title": "Hacia el Futuro", "description": "Con la certeza de que lo mejor está por venir."}
}

@app.route('/')
def home():
    return render_template('index.html', captions=PHOTO_CAPTIONS)

if __name__ == '__main__':
    app.run(debug=False)