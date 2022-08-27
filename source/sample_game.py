# Wczytujemy moduł pgzrun
import pgzrun
from random import choice


# Definiujemy funkcje dodatkowe
def update_ball_position():
    # Aktualizujemy pozycję w osi X
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    # Aktualizujemy pozycję w osi Y
    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    # Sprawdzamy, czy piłeczka "odbije się"
    # od lewej lub prawej krawędzi okna
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    # oraz od górnej i dolnej
    if ball.y < 5:
        ball.direction_y = "down"
    elif ball.y > HEIGHT - 5:
        ball.direction_y = "up"


def update_ball_speed():
    if keyboard.a:
        ball.speed += 1
    elif keyboard.s:
        ball.speed -= 1


def update_ball_direciotn():
    if keyboard.up:
        ball.direction_y = "up"
    elif keyboard.down:
        ball.direction_y = "down"
    elif keyboard.left:
        ball.direction_x = "left"
    elif keyboard.right:
        ball.direction_x = "right"


def check_winner():
    if ball.winner:
        winner_txt = f"And the winner is: {ball.winner}"
        screen.draw.text(
            winner_txt, (WIDTH // 3, HEIGHT // 2), color="red", fontsize=60
        )


# Start programu
WIDTH = 640
HEIGHT = 360
TITLE = "PONG - inny niż wszystkie."

# Definiujemy wyświetlane obiekty i ich współrzędne X oraz Y
ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2

# Dodajemy własne właściwości
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 0


# Najważniejsze funkcje sterujące
def update():
    update_ball_speed()
    update_ball_direciotn()
    update_ball_position()


def draw():
    screen.blit("code-7198654_640.jpg", (0, 0))
    # LOGO PTI / SIS
    screen.blit("logo_pti_small.png", (10, 10))
    screen.blit("logo_sis.png", (WIDTH - 150, 10))
    ball.draw()


# Uruchomienie modułu Pygame Zero
pgzrun.go()
