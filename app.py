from flask import Flask, render_template_string
import os
import glob

app = Flask(__name__)

def get_photos():
    """Obtiene todas las fotos de la carpeta static/photos/"""
    photo_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp']
    photos = []
    
    photos_dir = os.path.join('static', 'photos')
    if os.path.exists(photos_dir):
        for extension in photo_extensions:
            photos.extend(glob.glob(os.path.join(photos_dir, extension)))
            photos.extend(glob.glob(os.path.join(photos_dir, extension.upper())))
    
    # Solo tomar el nombre del archivo para la URL
    photo_names = [os.path.basename(photo) for photo in photos]
    return photo_names[:22]  # Máximo 22 fotos

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

# Template HTML principal
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feliz Cumpleaños Katherine ✨</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='45' fill='%23ff69b4'/><circle cx='35' cy='35' r='15' fill='%23ff1493'/><circle cx='65' cy='35' r='15' fill='%23ff1493'/><circle cx='35' cy='65' r='15' fill='%23ff1493'/><circle cx='65' cy='65' r='15' fill='%23ff1493'/><circle cx='50' cy='50' r='20' fill='%23ffc0cb'/><circle cx='50' cy='50' r='8' fill='%23ffb6c1'/></svg>" type="image/svg+xml">
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #ffeef8 0%, #ffc7e8 50%, #ff9cc7 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Pétalos flotantes animados */
        .petal {
            position: fixed;
            width: 20px;
            height: 20px;
            background: radial-gradient(ellipse at center, #ff69b4 0%, #ff1493 100%);
            border-radius: 50% 0 50% 0;
            animation: float 8s infinite linear;
            z-index: 1;
        }

        @keyframes float {
            0% {
                transform: translateY(-100vh) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) rotate(360deg);
                opacity: 0;
            }
        }

        /* Header principal */
        .header {
            text-align: center;
            padding: 60px 20px;
            position: relative;
            z-index: 2;
        }

        .main-title {
            font-family: 'Dancing Script', cursive;
            font-size: 4.5rem;
            color: #d63384;
            text-shadow: 3px 3px 6px rgba(214, 51, 132, 0.3);
            margin-bottom: 20px;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 3px 3px 6px rgba(214, 51, 132, 0.3); }
            to { text-shadow: 3px 3px 20px rgba(214, 51, 132, 0.8); }
        }

        .date-info {
            font-size: 1.5rem;
            color: #ad1457;
            margin-bottom: 10px;
            font-weight: 300;
        }

        .relationship-info {
            font-size: 1.2rem;
            color: #c2185b;
            margin-bottom: 30px;
            font-style: italic;
        }

        /* Sección de dedicatoria especial */
        .special-message {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border-radius: 25px;
            padding: 40px;
            margin: 40px auto;
            max-width: 800px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(214, 51, 132, 0.2);
            border: 2px solid rgba(255, 182, 193, 0.5);
            position: relative;
            z-index: 2;
        }

        .special-message::before {
            content: '🌸';
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 2rem;
            background: white;
            padding: 10px;
            border-radius: 50%;
        }

        .quote {
            font-family: 'Dancing Script', cursive;
            font-size: 2.2rem;
            color: #ad1457;
            font-weight: 700;
            line-height: 1.4;
            margin-bottom: 20px;
        }

        .quote-author {
            font-size: 1.1rem;
            color: #c2185b;
            font-style: italic;
        }

        /* Grid de fotos */
        .photos-section {
            padding: 60px 20px;
            position: relative;
            z-index: 2;
        }

        .section-title {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #d63384;
            text-align: center;
            margin-bottom: 50px;
            text-shadow: 2px 2px 4px rgba(214, 51, 132, 0.3);
        }

        .photos-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .photo-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(214, 51, 132, 0.2);
            transition: all 0.3s ease;
            position: relative;
        }

        .photo-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(214, 51, 132, 0.4);
        }

        .photo-placeholder {
            width: 100%;
            height: 300px;
            background: linear-gradient(45deg, #ffc0cb, #ff69b4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }

        .photo-placeholder::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            animation: shimmer 2s infinite;
        }

        .photo-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 20px 20px 0 0;
        }

        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .photo-caption {
            padding: 20px;
        }

        .photo-title {
            font-family: 'Dancing Script', cursive;
            font-size: 1.5rem;
            color: #d63384;
            margin-bottom: 10px;
        }

        .photo-description {
            color: #666;
            line-height: 1.5;
            font-size: 0.95rem;
        }

        /* Sección de dedicatorias */
        .quotes-section {
            padding: 60px 20px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
            position: relative;
            z-index: 2;
        }

        .quotes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .quote-card {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(214, 51, 132, 0.15);
            border-left: 5px solid #ff69b4;
            transition: transform 0.3s ease;
        }

        .quote-card:hover {
            transform: translateY(-5px);
        }

        .quote-text {
            font-family: 'Dancing Script', cursive;
            font-size: 1.8rem;
            color: #ad1457;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .quote-subtitle {
            color: #c2185b;
            font-size: 1rem;
            font-style: italic;
        }

        /* Footer romántico */
        .footer {
            text-align: center;
            padding: 40px 20px;
            background: rgba(214, 51, 132, 0.1);
            position: relative;
            z-index: 2;
        }

        .footer-text {
            font-family: 'Dancing Script', cursive;
            font-size: 1.8rem;
            color: #d63384;
            margin-bottom: 10px;
        }

        .footer-subtitle {
            color: #ad1457;
            font-size: 1.1rem;
        }

        /* Efectos responsivos */
        @media (max-width: 768px) {
            .main-title {
                font-size: 3rem;
            }
            
            .quote {
                font-size: 1.8rem;
            }
            
            .photos-grid {
                grid-template-columns: 1fr;
            }
            
            .quotes-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Control de música */
        .music-control {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: rgba(214, 51, 132, 0.9);
            color: white;
            border: none;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(214, 51, 132, 0.4);
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .music-control:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(214, 51, 132, 0.6);
        }
        
        /* Modal para imagen completa */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
            backdrop-filter: blur(5px);
        }

        .modal-content {
            position: relative;
            margin: auto;
            display: block;
            width: 90%;
            max-width: 900px;
            max-height: 90%;
            object-fit: contain;
            border-radius: 15px;
            top: 50%;
            transform: translateY(-50%);
        }

        .modal-controls {
            position: absolute;
            top: 15px;
            right: 15px;
            display: flex;
            gap: 10px;
        }

        .modal-btn {
            background: rgba(255, 105, 180, 0.9);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .modal-btn:hover {
            background: rgba(255, 105, 180, 1);
            transform: scale(1.05);
        }

        .close {
            background: rgba(220, 20, 60, 0.9);
        }

        .photo-overlay {
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            gap: 5px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .photo-card:hover .photo-overlay {
            opacity: 1;
        }

        .photo-btn {
            background: rgba(255, 105, 180, 0.9);
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .photo-btn:hover {
            background: rgba(255, 105, 180, 1);
            transform: scale(1.05);
        }
        
        /* Peonías animadas con scroll */
        .peony-container {
            position: fixed;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }

        .peony {
            position: absolute;
            animation: growAndFade 4s ease-in-out forwards;
            transform-origin: center bottom;
        }

        .peony-flower {
            width: 60px;
            height: 60px;
            position: relative;
            transform-origin: center;
            animation: gentleRotate 8s ease-in-out infinite;
        }

        /* Pétalos de la peonía */
        /* Pétalos flotantes animados */
        .petal {
            position: fixed;
            width: 20px;
            height: 20px;
            background: radial-gradient(ellipse at center, #ff69b4 0%, #ff1493 100%);
            border-radius: 50% 0 50% 0;
            animation: float 8s infinite linear;
            z-index: 1;
        }

        /* Peonías completas animadas */
        .peony-scroll {
            position: fixed;
            width: 80px;
            height: 80px;
            pointer-events: none;
            z-index: 1;
            animation: peonyAppear 5s ease-out forwards;
        }

        .peony-flower {
            position: relative;
            width: 80px;
            height: 80px;
            animation: gentleSpin 10s ease-in-out infinite;
        }

        .peony-petal {
            position: absolute;
            width: 25px;
            height: 35px;
            border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
            transform-origin: center bottom;
        }

        .peony-petal:nth-child(1) {
            background: linear-gradient(45deg, #ff69b4, #ff1493);
            top: 10px;
            left: 27px;
            transform: rotate(0deg);
        }

        .peony-petal:nth-child(2) {
            background: linear-gradient(45deg, #ff1493, #dc143c);
            top: 15px;
            left: 45px;
            transform: rotate(45deg);
        }

        .peony-petal:nth-child(3) {
            background: linear-gradient(45deg, #ff69b4, #ff20b2);
            top: 30px;
            left: 50px;
            transform: rotate(90deg);
        }

        .peony-petal:nth-child(4) {
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            top: 45px;
            left: 45px;
            transform: rotate(135deg);
        }

        .peony-petal:nth-child(5) {
            background: linear-gradient(45deg, #ff20b2, #ff69b4);
            top: 50px;
            left: 27px;
            transform: rotate(180deg);
        }

        .peony-petal:nth-child(6) {
            background: linear-gradient(45deg, #ff69b4, #ff1493);
            top: 45px;
            left: 10px;
            transform: rotate(225deg);
        }

        .peony-petal:nth-child(7) {
            background: linear-gradient(45deg, #ff1493, #dc143c);
            top: 30px;
            left: 5px;
            transform: rotate(270deg);
        }

        .peony-petal:nth-child(8) {
            background: linear-gradient(45deg, #ff20b2, #ff69b4);
            top: 15px;
            left: 10px;
            transform: rotate(315deg);
        }

        .peony-center {
            position: absolute;
            top: 70px;
            left: 70px;
            transform: translate(-50%, -50%);
            width: 16px;
            height: 16px;
            background: radial-gradient(circle, #ffff00, #ffd700);
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
            animation: centerPulse 2s ease-in-out infinite;
            z-index: 10;
        }

        @keyframes peonyAppear {
            0% {
                transform: scale(0) rotate(0deg);
                opacity: 0;
            }
            20% {
                transform: scale(1.2) rotate(90deg);
                opacity: 1;
            }
            80% {
                transform: scale(1) rotate(270deg);
                opacity: 1;
            }
            100% {
                transform: scale(0) rotate(360deg);
                opacity: 0;
            }
        }

        @keyframes gentleSpin {
            0%, 100% { transform: rotate(0deg); }
            50% { transform: rotate(5deg); }
        }

       @keyframes centerPulse {
            0%, 100% { 
                box-shadow: 0 0 15px rgba(255, 215, 0, 0.8);
                transform: translate(-50%, -50%) scale(1);
            }
            50% { 
                box-shadow: 0 0 25px rgba(255, 215, 0, 1);
                transform: translate(-50%, -50%) scale(1.1);
            }
        }
        .petal-1 {
            background: linear-gradient(45deg, #ff69b4, #ff1493);
            top: 5px;
            left: 20px;
            transform: rotate(0deg);
            animation: petalDance1 6s ease-in-out infinite;
        }

        .petal-2 {
            background: linear-gradient(45deg, #ff1493, #dc143c);
            top: 10px;
            left: 35px;
            transform: rotate(45deg);
            animation: petalDance2 6s ease-in-out infinite 0.5s;
        }

        .petal-3 {
            background: linear-gradient(45deg, #ff69b4, #ff20b2);
            top: 25px;
            left: 40px;
            transform: rotate(90deg);
            animation: petalDance3 6s ease-in-out infinite 1s;
        }

        .petal-4 {
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            top: 40px;
            left: 35px;
            transform: rotate(135deg);
            animation: petalDance1 6s ease-in-out infinite 1.5s;
        }

        .petal-5 {
            background: linear-gradient(45deg, #ff20b2, #ff69b4);
            top: 45px;
            left: 20px;
            transform: rotate(180deg);
            animation: petalDance2 6s ease-in-out infinite 2s;
        }

        .petal-6 {
            background: linear-gradient(45deg, #ff69b4, #ff1493);
            top: 40px;
            left: 5px;
            transform: rotate(225deg);
            animation: petalDance3 6s ease-in-out infinite 2.5s;
        }

        .petal-7 {
            background: linear-gradient(45deg, #ff1493, #dc143c);
            top: 25px;
            left: 0px;
            transform: rotate(270deg);
            animation: petalDance1 6s ease-in-out infinite 3s;
        }

        .petal-8 {
            background: linear-gradient(45deg, #ff20b2, #ff69b4);
            top: 10px;
            left: 5px;
            transform: rotate(315deg);
            animation: petalDance2 6s ease-in-out infinite 3.5s;
        }

        /* Centro de la peonía */
        .peony-center {
            position: absolute;
            top: 50px;
            left: 50px;
            width: 16px;
            height: 16px;
            background: radial-gradient(circle, #ffff00, #ffd700);
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.8);
            animation: centerGlow 3s ease-in-out infinite;
        }

        /* Tallo */
        .peony-stem {
            position: absolute;
            bottom: 0;
            left: 29px;
            width: 2px;
            height: 40px;
            background: linear-gradient(to bottom, #228b22, #006400);
            border-radius: 1px;
            transform-origin: bottom;
            animation: stemSway 4s ease-in-out infinite;
        }

        /* Hojas */
        .peony-leaf {
            position: absolute;
            width: 12px;
            height: 8px;
            background: linear-gradient(45deg, #32cd32, #228b22);
            border-radius: 50% 0 50% 0;
            bottom: 15px;
        }

        .leaf-left {
            left: 20px;
            transform: rotate(-30deg);
            animation: leafRustle1 5s ease-in-out infinite;
        }

        .leaf-right {
            right: 20px;
            transform: rotate(30deg);
            animation: leafRustle2 5s ease-in-out infinite 1s;
        }

        /* Animaciones */
        @keyframes growAndFade {
            0% {
                transform: scale(0) translateY(20px);
                opacity: 0;
            }
            20% {
                transform: scale(1) translateY(0);
                opacity: 1;
            }
            80% {
                transform: scale(1) translateY(0);
                opacity: 1;
            }
            100% {
                transform: scale(0.8) translateY(-10px);
                opacity: 0;
            }
        }

        @keyframes gentleRotate {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(2deg); }
            75% { transform: rotate(-2deg); }
        }

        @keyframes petalDance1 {
            0%, 100% { transform: scale(1) rotate(var(--rotation, 0deg)); }
            50% { transform: scale(1.05) rotate(calc(var(--rotation, 0deg) + 3deg)); }
        }

        @keyframes petalDance2 {
            0%, 100% { transform: scale(1) rotate(var(--rotation, 0deg)); }
            50% { transform: scale(0.95) rotate(calc(var(--rotation, 0deg) - 2deg)); }
        }

        @keyframes petalDance3 {
            0%, 100% { transform: scale(1) rotate(var(--rotation, 0deg)); }
            50% { transform: scale(1.02) rotate(calc(var(--rotation, 0deg) + 1deg)); }
        }

        @keyframes centerGlow {
            0%, 100% { box-shadow: 0 0 10px rgba(255, 215, 0, 0.8); }
            50% { box-shadow: 0 0 20px rgba(255, 215, 0, 1); }
        }

        @keyframes stemSway {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(1deg); }
            75% { transform: rotate(-1deg); }
        }

        @keyframes leafRustle1 {
            0%, 100% { transform: rotate(-30deg); }
            50% { transform: rotate(-25deg); }
        }

        @keyframes leafRustle2 {
            0%, 100% { transform: rotate(30deg); }
            50% { transform: rotate(35deg); }
        }   
    </style>
</head>
<body>
    <!-- Audio de fondo -->
    <audio id="backgroundMusic" loop>
        <source src="{{ url_for('static', filename='birthday_music.mp3') }}" type="audio/mpeg">
        <!-- Fallback: música de fondo romántica desde CDN -->
        <source src="https://www.soundjay.com/misc/sounds/bell-ringing-05.wav" type="audio/wav">
    </audio>

    <!-- Pétalos flotantes -->
    <div class="petals-container"></div>

    <!-- Header principal -->
    <div class="header">
        <h1 class="main-title">Feliz Cumpleaños Katherine</h1>
        <p class="date-info">17 de Junio - Tu día especial 🎂</p>
        <p class="relationship-info">Nuestra historia comenzó el 1° de Junio ❤️</p>
    </div>

    <!-- Mensaje especial -->
    <div class="special-message">
        <p class="quote">"Gracias por tomar mi mano y caminar juntos en esta historia llamada vida"</p>
        <p class="quote-author">— Con todo mi amor de parte de Mark ❤️</p>
    </div>

    <!-- Sección de fotos -->
    <div class="photos-section">
        <h2 class="section-title">Nuestros Momentos Especiales 📸</h2>
        <div class="photos-grid">
            {% for i in range(photos|length) %}
            <div class="photo-card">
                <div style="position: relative;">
                    <img src="{{ url_for('static', filename='photos/' + photos[i]) }}" 
                        alt="Foto {{ i+1 }}" 
                        class="photo-image"
                        onerror="this.style.display='none'; this.parentElement.nextElementSibling.style.display='flex'">
                    <div class="photo-overlay">
                        <button class="photo-btn" onclick="openModal('{{ url_for('static', filename='photos/' + photos[i]) }}', '{{ captions[i+1]['title'] if captions[i+1] else 'Momento ' + (i+1)|string }}')">👁️ Ver</button>
                        <button class="photo-btn" onclick="downloadImage('{{ url_for('static', filename='photos/' + photos[i]) }}', 'Katherine_Foto_{{ i+1 }}.jpg')">💾 Descargar</button>
                    </div>
                </div>
                <div class="photo-placeholder" style="display: none;">
                    <span>Foto {{ i+1 }}/22<br>💕 Memoria Especial 💕</span>
                </div>
                <div class="photo-caption">
                    <h3 class="photo-title">{{ captions[i+1]['title'] if captions[i+1] else 'Momento ' + (i+1)|string }}</h3>
                    <p class="photo-description">{{ captions[i+1]['description'] if captions[i+1] else 'Una memoria especial de nuestro amor que siempre llevaré en mi corazón.' }}</p>
                </div>
            </div>
            {% endfor %}
            
            <!-- Placeholders para fotos faltantes -->
            {% for i in range(photos|length, 22) %}
            <div class="photo-card">
                <div class="photo-placeholder">
                    <span>Foto {{ i+1 }}/22<br>💕 Próxima Memoria 💕</span>
                </div>
                <div class="photo-caption">
                    <h3 class="photo-title">{{ captions[i+1]['title'] if captions[i+1] else 'Momento ' + (i+1)|string }}</h3>
                    <p class="photo-description">{{ captions[i+1]['description'] if captions[i+1] else 'Un espacio esperando ser llenado con nuestros próximos momentos especiales.' }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- Sección de dedicatorias -->
    <div class="quotes-section">
        <h2 class="section-title">Dedicatorias del Corazón 💖</h2>
        <div class="quotes-grid">
            <div class="quote-card">
                <p class="quote-text">"Eres la razón por la que creo en los cuentos de hadas"</p>
                <p class="quote-subtitle">Tu sonrisa ilumina mis días</p>
            </div>
            <div class="quote-card">
                <p class="quote-text">"Contigo, cada día es una nueva aventura llena de amor"</p>
                <p class="quote-subtitle">Gracias por ser mi compañera de vida</p>
            </div>
            <div class="quote-card">
                <p class="quote-text">"Tu amor es el regalo más hermoso que he recibido"</p>
                <p class="quote-subtitle">Feliz cumpleaños, mi amor</p>
            </div>
            <div class="quote-card">
                <p class="quote-text">"Eres perfecta tal como eres, nunca cambies"</p>
                <p class="quote-subtitle">Tu esencia es mi inspiración</p>
            </div>
            <div class="quote-card">
                <p class="quote-text">"Juntos hemos creado la historia de amor más bonita"</p>
                <p class="quote-subtitle">Y esto es solo el comienzo</p>
            </div>
            <div class="quote-card">
                <p class="quote-text">"Que este nuevo año de vida esté lleno de sueños cumplidos"</p>
                <p class="quote-subtitle">Te amo más de lo que las palabras pueden expresar</p>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <p class="footer-text">Con amor infinito para Katherine</p>
        <p class="footer-subtitle">El mejor regalo eres tú en mi vida 🌸</p>
    </div>

    <!-- Control de música -->
    <button class="music-control" onclick="toggleMusic()" id="musicBtn">🎵</button>

    <script>
        // Crear pétalos flotantes
        function createPetal() {
            const petal = document.createElement('div');
            petal.className = 'petal';
            petal.style.left = Math.random() * 100 + 'vw';
            petal.style.animationDuration = (Math.random() * 3 + 5) + 's';
            petal.style.opacity = Math.random();
            document.body.appendChild(petal);

            setTimeout(() => {
                petal.remove();
            }, 8000);
        }

        // Crear pétalos continuamente
        setInterval(createPetal, 300);

        // Control de música
        const music = document.getElementById('backgroundMusic');
        const musicBtn = document.getElementById('musicBtn');
        let isPlaying = false;

        function toggleMusic() {
            if (isPlaying) {
                music.pause();
                musicBtn.textContent = '🎵';
                musicBtn.style.opacity = '0.7';
            } else {
                music.play().catch(e => {
                    console.log('No se pudo reproducir la música automáticamente');
                });
                musicBtn.textContent = '🎶';
                musicBtn.style.opacity = '1';
            }
            isPlaying = !isPlaying;
        }

        // Intentar reproducir música al cargar la página
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(() => {
                music.play().catch(e => {
                    console.log('Reproducción automática bloqueada - el usuario debe interactuar primero');
                });
            }, 1000);
        });

        // Reproducir música al hacer click en cualquier parte
        document.addEventListener('click', function() {
            if (!isPlaying) {
                toggleMusic();
            }
        }, { once: true });

        // Efectos de scroll suave
        document.querySelectorAll('.photo-card').forEach((card, index) => {
            card.style.animationDelay = (index * 0.1) + 's';
            card.style.animation = 'fadeInUp 0.6s ease forwards';
        });
    </script>

    <style>
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    <!-- Modal para imagen completa -->
    <div id="imageModal" class="modal">
        <div class="modal-controls">
            <button class="modal-btn" onclick="downloadCurrentImage()">💾 Descargar</button>
            <button class="modal-btn close" onclick="closeModal()">✕ Cerrar</button>
        </div>
        <img class="modal-content" id="modalImage">
    </div>

    <script>
    let currentImageSrc = '';
    let currentImageName = '';

    function openModal(imageSrc, imageTitle) {
        const modal = document.getElementById('imageModal');
        const modalImg = document.getElementById('modalImage');
        modal.style.display = 'block';
        modalImg.src = imageSrc;
        currentImageSrc = imageSrc;
        currentImageName = imageTitle;
    }

    function closeModal() {
        document.getElementById('imageModal').style.display = 'none';
    }

    function downloadImage(imageSrc, filename) {
        const link = document.createElement('a');
        link.href = imageSrc;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }

    function downloadCurrentImage() {
        if (currentImageSrc) {
            downloadImage(currentImageSrc, currentImageName + '.jpg');
        }
    }

    // Cerrar modal con ESC
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeModal();
        }
    });

    // Cerrar modal clickeando fuera de la imagen
    document.getElementById('imageModal').addEventListener('click', function(event) {
        if (event.target === this) {
            closeModal();
        }
    });
    
    // Crear peonías animadas con scroll
    let peonyContainer;

    function initPeonies() {
        peonyContainer = document.createElement('div');
        peonyContainer.className = 'peony-container';
        document.body.appendChild(peonyContainer);
    }

    function createPeony(x, y) {
        const peony = document.createElement('div');
        peony.className = 'peony';
        peony.style.left = x + 'px';
        peony.style.top = y + 'px';
        
        peony.innerHTML = `
            <div class="peony-flower">
                <div class="petal petal-1" style="--rotation: 0deg;"></div>
                <div class="petal petal-2" style="--rotation: 45deg;"></div>
                <div class="petal petal-3" style="--rotation: 90deg;"></div>
                <div class="petal petal-4" style="--rotation: 135deg;"></div>
                <div class="petal petal-5" style="--rotation: 180deg;"></div>
                <div class="petal petal-6" style="--rotation: 225deg;"></div>
                <div class="petal petal-7" style="--rotation: 270deg;"></div>
                <div class="petal petal-8" style="--rotation: 315deg;"></div>
                <div class="peony-center"></div>
            </div>
            <div class="peony-stem"></div>
            <div class="peony-leaf leaf-left"></div>
            <div class="peony-leaf leaf-right"></div>
        `;
        
        peonyContainer.appendChild(peony);
        
        // Eliminar la peonía después de la animación
        setTimeout(() => {
            if (peony.parentNode) {
                peony.parentNode.removeChild(peony);
            }
        }, 4000);
    }

    // Crear peonías al hacer scroll
    let lastScrollTime = 0;
    function handleScroll() {
        const now = Date.now();
        if (now - lastScrollTime > 300) { // Throttle para performance
            lastScrollTime = now;
            
            // Crear peonía en posición aleatoria
            const x = Math.random() * (window.innerWidth - 60);
            const y = Math.random() * (window.innerHeight - 100);
            
            createPeony(x, y);
        }
    }

    // Crear peonías automáticamente cada 3 segundos
    function createRandomPeony() {
        const x = Math.random() * (window.innerWidth - 60);
        const y = Math.random() * (window.innerHeight - 100);
        createPeony(x, y);
    }

    // Inicializar cuando carga la página
    document.addEventListener('DOMContentLoaded', function() {
        initPeonies();
        
        // Peonías con scroll
        window.addEventListener('scroll', handleScroll);
        
        // Peonías automáticas cada 3 segundos
        // Crear pétalos continuamente
        setInterval(createPetal, 300);

        // Sistema de peonías con scroll
        let lastPeonyTime = 0;

        function createScrollPeony() {
            const now = Date.now();
            if (now - lastPeonyTime < 800) return; // No más de una peonía cada 800ms
            
            lastPeonyTime = now;
            
            const peony = document.createElement('div');
            peony.className = 'peony-scroll';
            
            // Posición aleatoria
            peony.style.left = Math.random() * (window.innerWidth - 80) + 'px';
            peony.style.top = Math.random() * (window.innerHeight - 80) + 'px';
            
            // Crear la estructura de la peonía
            peony.innerHTML = `
                <div class="peony-flower">
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-petal"></div>
                    <div class="peony-center"></div>
                </div>
            `;
            
            document.body.appendChild(peony);
            
            // Eliminar después de la animación
            setTimeout(() => {
                if (peony.parentNode) {
                    peony.parentNode.removeChild(peony);
                }
            }, 5000);
        }

        // Crear peonías al hacer scroll
        window.addEventListener('scroll', createScrollPeony);

        // Crear peonías automáticamente cada 4 segundos
        setInterval(createScrollPeony, 4000);

        // Crear una peonía inicial después de 2 segundos
        setTimeout(createScrollPeony, 2000);
        
        // Crear algunas peonías iniciales
        setTimeout(() => createRandomPeony(), 1000);
        setTimeout(() => createRandomPeony(), 2000);
    });
    </script>
    
</body>
</html>
'''

@app.route('/')
def index():
    photos = get_photos()
    return render_template_string(HTML_TEMPLATE, photos=photos, captions=PHOTO_CAPTIONS)

if __name__ == '__main__':
    # Crear carpetas necesarias si no existen
    directories = ['static', 'static/photos']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Carpeta creada: {directory}")
    
    print("🌸 Servidor iniciado para Katherine 🌸")
    print("📱 Visita: http://localhost:5000")
    print("📸 Para agregar fotos:")
    print("   1. Pon tus fotos en la carpeta: static/photos/")
    print("   2. Formatos: .jpg, .jpeg, .png, .gif, .webp")
    print("   3. ¡Las fotos aparecerán automáticamente!")
    print("🎵 Para música: pon tu archivo como static/birthday_music.mp3")
    print("💕 ¡Feliz cumpleaños Katherine! 💕")
    
    app.run(debug=True, host='0.0.0.0', port=5000)