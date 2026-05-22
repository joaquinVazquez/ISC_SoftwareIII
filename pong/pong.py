import turtle

screen = turtle.Screen()
screen.title('Pong — ISC Software III')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# ── RAQUETA JUGADOR 1 (izquierda) ────────────────
raqueta_a = turtle.Turtle()
raqueta_a.speed(0)          # Velocidad de animación: 0 = instantáneo
raqueta_a.shape('square')   # Forma cuadrada
raqueta_a.color('cyan')    # Color blanco
raqueta_a.shapesize(stretch_wid=5, stretch_len=1)  # 5x alta, 1x ancha
raqueta_a.penup()           # No dibuja líneas al moverse
raqueta_a.goto(-350, 0)     # Posición: izquierda, centrada

# ── RAQUETA JUGADOR 2 (derecha) ──────────────────
raqueta_b = turtle.Turtle()
raqueta_b.speed(0)
raqueta_b.shape('square')
raqueta_b.color('red')
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup()
raqueta_b.goto(350, 0)      # Posición: derecha, centrada

# ── LA PELOTA ────────────────────────────────────
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape('square')
pelota.color('white')
pelota.penup()
pelota.goto(0, 0)           # Inicia en el centro

# Velocidad de la pelota (atributos personalizados)
pelota.dx = 0.4             # Velocidad horizontal
pelota.dy = 0.4             # Velocidad vertical

# ── PUNTUACIÓN ───────────────────────────────────
score_a = 0    # Puntos del Jugador A
score_b = 0    # Puntos del Jugador B
# Tortuga para escribir el marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color('white')
marcador.penup()
marcador.hideturtle()        # La tortuga es invisible
marcador.goto(0, 260)        # Posición: arriba, centrado
marcador.write(
    f'Jugador A: {score_a}    Jugador B: {score_b}',
    align='center',
    font=('Courier', 22, 'normal')
)

# ── FUNCIONES DE MOVIMIENTO ──────────────────────
def raqueta_a_arriba():
    y = raqueta_a.ycor()
    if y < 250:              # Límite superior
        raqueta_a.sety(y + 20)

def raqueta_a_abajo():
    y = raqueta_a.ycor()
    if y > -240:             # Límite inferior
        raqueta_a.sety(y - 20)

def raqueta_b_arriba():
    y = raqueta_b.ycor()
    if y < 250:
        raqueta_b.sety(y + 20)

def raqueta_b_abajo():
    y = raqueta_b.ycor()
    if y > -240:
        raqueta_b.sety(y - 20)

# ── ESCUCHAR EL TECLADO ───────────────────────────
screen.listen()                              # Activar escucha de teclas
screen.onkeypress(raqueta_a_arriba, 'w')     # W = Jugador A sube
screen.onkeypress(raqueta_a_abajo,  's')     # S = Jugador A baja
screen.onkeypress(raqueta_b_arriba, 'Up')    # ↑ = Jugador B sube
screen.onkeypress(raqueta_b_abajo,  'Down')  # ↓ = Jugador B baja

# ── LÍNEA CENTRAL PUNTEADA ────────────────────────
linea = turtle.Turtle()
linea.speed(0)
linea.color('white')
linea.penup()
linea.hideturtle()

# Dibujar 30 segmentos desde arriba hasta abajo
for i in range(30):
    linea.goto(0, 290 - (i * 20))   # Posición de cada segmento
    linea.pendown()
    linea.forward(10)                # Dibuja 10px hacia abajo
    linea.penup()

# ── DENTRO DEL while True, al detectar rebote ──────
# Puedes usar el módulo winsound en Windows:
# import winsound
# winsound.Beep(440, 50)  # frecuencia 440hz, 50ms


# ── GAME LOOP ────────────────────────────────────
while True:
    screen.update()   # Redibujar la pantalla
    
    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

        # ── REBOTES EN PAREDES (arriba y abajo) ────────
    if pelota.ycor() > 290:      # Toca el techo
        pelota.sety(290)         # Reposicionar dentro del límite
        pelota.dy *= -1          # Invertir dirección vertical
    
    if pelota.ycor() < -290:     # Toca el suelo
        pelota.sety(-290)
        pelota.dy *= -1

        # ── PUNTUACIÓN ───────────────────────────────────
    # Pelota sale por la derecha → anota Jugador A
    if pelota.xcor() > 390:
        score_a += 1
        marcador.clear()
        marcador.write(
            f'Jugador A: {score_a}    Jugador B: {score_b}',
            align='center', font=('Courier', 22, 'normal')
        )
        pelota.goto(0, 0)    # Regresar al centro
        pelota.dx *= -1      # Invertir dirección
    
    # Pelota sale por la izquierda → anota Jugador B
    if pelota.xcor() < -390:
        score_b += 1
        marcador.clear()
        marcador.write(
            f'Jugador A: {score_a}    Jugador B: {score_b}',
            align='center', font=('Courier', 22, 'normal')
        )
        pelota.goto(0, 0)
        pelota.dx *= -1

        # ── COLISIÓN: PELOTA CON RAQUETA B (derecha) ────
    if (pelota.xcor() > 340 and
        pelota.xcor() < 360 and
        pelota.ycor() < raqueta_b.ycor() + 50 and
        pelota.ycor() > raqueta_b.ycor() - 50):
        pelota.setx(340)      # Evitar que traverse la raqueta
        pelota.dx *= -1       # Rebotar

        # ── COLISIÓN: PELOTA CON RAQUETA A (izquierda) ──
    if (pelota.xcor() < -340 and
        pelota.xcor() > -360 and
        pelota.ycor() < raqueta_a.ycor() + 50 and
        pelota.ycor() > raqueta_a.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1



