import tkinter as tk
import random
import math

# --- Fenster ---
root = tk.Tk()
root.title("Pong – Complete Logic")

WIDTH = 800
HEIGHT = 400

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Paddles ---
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
SPEED = 10
MAX_SPEED = 12       # Maximum speed limit
START_SPEED = 7      # Initial speed
BOUNCE_RANDOMNESS = 1.5  # Random jitter pixels added to dy

# Current velocity variables
ball_speed = START_SPEED
ball_dx = START_SPEED
ball_dy = START_SPEED

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

# --- Ball & Game State ---
BALL_SIZE = 20
ball = canvas.create_oval(
    WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2,
    WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2,
    fill="white"
)

# Scores
score_left = 0
score_right = 0

# Score Display
score_display = canvas.create_text(
    WIDTH//2, 40,
    text="0 : 0",
    fill="white",
    font=("Courier New", 30, "bold")
)

# --- Tastenstatus ---
keys = {
    "w": False, "s": False,
    "Up": False, "Down": False
}

def on_key_press(event):
    if event.keysym in keys:
        keys[event.keysym] = True

def on_key_release(event):
    if event.keysym in keys:
        keys[event.keysym] = False

root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# --- Helper Functions ---

def move_paddle(paddle, dy):
    canvas.move(paddle, 0, dy)
    x1, y1, x2, y2 = canvas.coords(paddle)
    # Wall collision for paddles
    if y1 < 0:
        canvas.move(paddle, 0, -y1)
    elif y2 > HEIGHT:
        canvas.move(paddle, 0, HEIGHT - y2)

def reset_ball():
    global ball_dx, ball_dy, ball_speed
    
    # 1. Reset Position
    canvas.coords(ball, 
                  WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2,
                  WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2)
    
    # 2. Reset Speed
    ball_speed = START_SPEED
    
    # 3. Randomize Serve Direction (Left or Right)
    dir_x = random.choice([-1, 1])
    # Randomize start angle slightly so it's not always perfectly straight
    angle = random.uniform(-math.radians(30), math.radians(30))
    
    ball_dx = ball_speed * math.cos(angle) * dir_x
    ball_dy = ball_speed * math.sin(angle)

def update_score_display():
    canvas.itemconfig(score_display, text=f"{score_left} : {score_right}")

def check_collision(ball_pos, paddle_pos):
    # Axis-Aligned Bounding Box (AABB) collision detection
    # ball_pos = [x1, y1, x2, y2]
    # paddle_pos = [x1, y1, x2, y2]
    
    return (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and
            ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3])

def handle_paddle_collision(ball_pos, paddle_pos, paddle_side):
    global ball_dx, ball_dy, ball_speed

    # 1. Calculate the center Y of the ball and the paddle
    ball_center_y = (ball_pos[1] + ball_pos[3]) / 2
    paddle_center_y = (paddle_pos[1] + paddle_pos[3]) / 2

    # 2. Calculate offset (how far from the center did we hit?)
    # Value ranges roughly from -1.0 (top edge) to 1.0 (bottom edge)
    offset = (ball_center_y - paddle_center_y) / (PADDLE_HEIGHT / 2)

    # 3. Calculate bounce angle (Max 60 degrees to prevent vertical infinite loops)
    # We invert the sign because in computer graphics, Y goes down.
    bounce_angle = offset * math.radians(60) 

    # 4. Increase speed slightly (Gameplay progression)
    if ball_speed < MAX_SPEED:
        ball_speed += 0.5

    # 5. Calculate new velocity vector based on angle
    # direction (1 for left paddle hitting right, -1 for right paddle hitting left)
    direction = 1 if paddle_side == "left" else -1
    
    new_dx = ball_speed * math.cos(bounce_angle) * direction
    new_dy = ball_speed * math.sin(bounce_angle)

    # 6. Add the "Random" factor user requested
    new_dy += random.uniform(-BOUNCE_RANDOMNESS, BOUNCE_RANDOMNESS)

    return round(new_dx), round(new_dy)

class agent:
    def __init__(self, paddle):
        self.paddle = paddle
        self.qTable = []
        

# --- Game Loop ---
def game_loop():
    global ball_dx, ball_dy, score_left, score_right

    # --- 1. Move Paddles ---
    if keys["w"]: move_paddle(left_paddle, -SPEED)
    if keys["s"]: move_paddle(left_paddle, SPEED)
    if keys["Up"]: move_paddle(right_paddle, -SPEED)
    if keys["Down"]: move_paddle(right_paddle, SPEED)

    # --- 2. Move Ball ---
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)      # [x1, y1, x2, y2]
    
    # --- 3. Physically Correct Wall Collision ---
    # Top Wall
    if ball_pos[1] <= 0:
        # Snap ball to edge (Position Correction) to prevent sticking
        overlap = 0 - ball_pos[1]
        canvas.move(ball, 0, overlap) 
        ball_dy = abs(ball_dy) # Force direction DOWN

    # Bottom Wall
    elif ball_pos[3] >= HEIGHT:
        # Snap ball to edge
        overlap = ball_pos[3] - HEIGHT
        canvas.move(ball, 0, -overlap)
        ball_dy = -abs(ball_dy) # Force direction UP

    # --- 4. Advanced Paddle Collision ---
    left_pad_pos = canvas.coords(left_paddle)
    right_pad_pos = canvas.coords(right_paddle)

    # Check Left Paddle
    if check_collision(ball_pos, left_pad_pos):
        ball_dx, ball_dy = handle_paddle_collision(ball_pos, left_pad_pos, "left")
        # Safety: Push ball out of paddle to prevent 'gluing'
        canvas.move(ball, (left_pad_pos[2] - ball_pos[0]) + 2, 0)

    # Check Right Paddle
    elif check_collision(ball_pos, right_pad_pos):
        ball_dx, ball_dy = handle_paddle_collision(ball_pos, right_pad_pos, "right")
        # Safety: Push ball out of paddle
        canvas.move(ball, (right_pad_pos[0] - ball_pos[2]) - 2, 0)

    # --- 5. Scoring ---
    if ball_pos[0] <= 0:
        score_right += 1
        update_score_display()
        reset_ball()
    elif ball_pos[2] >= WIDTH:
        score_left += 1
        update_score_display()
        reset_ball()

    root.after(16, game_loop)

# Ensure reset_ball is called once to start
reset_ball()
game_loop()
root.mainloop()