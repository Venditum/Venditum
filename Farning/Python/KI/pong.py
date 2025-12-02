import tkinter as tk

# --- Fenster ---
root = tk.Tk()
root.title("Pong – Smooth Paddles")

WIDTH = 800
HEIGHT = 400

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Paddles ---
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
SPEED = 6

left_paddle = canvas.create_rectangle(
    30, HEIGHT//2 - PADDLE_HEIGHT//2,
    30 + PADDLE_WIDTH, HEIGHT//2 + PADDLE_HEIGHT//2,
    fill="white"
)

right_paddle = canvas.create_rectangle(
    WIDTH - 30 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2,
    WIDTH - 30, HEIGHT//2 + PADDLE_HEIGHT//2,
    fill="white"
)

# --- Ball (statisch) ---
BALL_SIZE = 20
ball = canvas.create_oval(
    WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2,
    WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2,
    fill="white"
)

# --- Tastenstatus ---
keys = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}

def on_key_press(event):
    if event.keysym in keys:
        keys[event.keysym] = True

def on_key_release(event):
    if event.keysym in keys:
        keys[event.keysym] = False

root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# --- Paddle Movement ---
def move_paddle(paddle, dy):
    canvas.move(paddle, 0, dy)
    x1, y1, x2, y2 = canvas.coords(paddle)
    if y1 < 0:
        canvas.move(paddle, 0, -y1)
    elif y2 > HEIGHT:
        canvas.move(paddle, 0, HEIGHT - y2)

# --- Spiel-Loop ---
def game_loop():
    # Linkes Paddle
    if keys["w"]:
        move_paddle(left_paddle, -SPEED)
    if keys["s"]:
        move_paddle(left_paddle, SPEED)

    # Rechtes Paddle
    if keys["Up"]:
        move_paddle(right_paddle, -SPEED)
    if keys["Down"]:
        move_paddle(right_paddle, SPEED)

    root.after(16, game_loop)  # ~60 FPS

game_loop()
root.mainloop()