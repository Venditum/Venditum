import tkinter as tk
import math
import random

# --- Konfiguration ---
WIDTH = 800
HEIGHT = 500
BG_COLOR = "black"
FG_COLOR = "white"

# Paddle Einstellungen
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
PADDLE_OFFSET = 30
PADDLE_SPEED = 12.0 # Geschwindigkeit, mit der die Paddles sich pro Frame bewegen

# Ball Einstellungen
BALL_SIZE = 15
START_SPEED = 6.0
MAX_SPEED = 18.0
SPEED_INCREMENT = 1.05

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong – Keyboard Control & Original Physics")
        self.root.resizable(False, False)
        self.qtablel = {}
        self.laststatel = []
        self.rewardl = 0
        self.movel = 0
        self.expl = 1
        self.qtabler = {}
        self.laststater = []
        self.rewardr = 0
        self.mover = 0
        self.expr = 1

        
        # Cursor wieder sichtbar machen (optional, aber nützlich)
        self.root.config(cursor="") 

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        # --- Grafikelemente ---
        self.draw_court()
        
        # Linkes Paddle (Spieler 1 - WASD)
        self.left_paddle = self.canvas.create_rectangle(
            PADDLE_OFFSET, HEIGHT//2 - PADDLE_HEIGHT//2,
            PADDLE_OFFSET + PADDLE_WIDTH, HEIGHT//2 + PADDLE_HEIGHT//2,
            fill=FG_COLOR
        )

        # Rechtes Paddle (Spieler 2 - Pfeiltasten)
        self.right_paddle = self.canvas.create_rectangle(
            WIDTH - PADDLE_OFFSET - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2,
            WIDTH - PADDLE_OFFSET, HEIGHT//2 + PADDLE_HEIGHT//2,
            fill=FG_COLOR
        )

        # Ball
        self.ball = self.canvas.create_oval(
            WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2,
            WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2,
            fill=FG_COLOR
        )

        # Score
        self.score_left = 0
        self.score_right = 0
        self.score_display = self.canvas.create_text(
            WIDTH//2, 50, text="0  0", fill=FG_COLOR,
            font=("Courier New", 40, "bold")
        )

        # --- Variablen ---
        self.ball_pos = [WIDTH/2, HEIGHT/2] 
        self.ball_vel = [0, 0]
        self.current_speed = START_SPEED
        self.game_running = True
        
        # Tasten-Status-Dictionary für gleichzeitiges Drücken
        self.keys = {"w": False, "s": False, "Up": False, "Down": False}

        # --- Bindings ---
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        
        # Sauberes Beenden
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.bind("<Escape>", lambda e: self.on_close())

        self.reset_ball()
        self.animate()

    # --- Input-Handling ---
    def on_key_press(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = True

    def on_key_release(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = False

    def returnstatel(self):
        return [round((self.canvas.coords(self.ball)[1] - self.canvas.coords(self.left_paddle)[1]) / 100)]
    def returnstater(self):
        return [round((self.canvas.coords(self.ball)[1] - self.canvas.coords(self.right_paddle)[1]) / 50), self.ball_vel[0] < 0, self.ball_vel[1] < 0]
    # --- Steuerungs-Logik ---
    def move_paddle(self, paddle, dy):
        """Bewegt das Paddle und prüft die Wände."""
        self.canvas.move(paddle, 0, dy)
        coords = self.canvas.coords(paddle)
        
        # Wand-Begrenzung
        if coords[1] < 0:
            self.canvas.move(paddle, 0, -coords[1])
        elif coords[3] > HEIGHT:
            self.canvas.move(paddle, 0, HEIGHT - coords[3])

    def aimovel(self):
        state = self.returnstatel()
        self.laststatel = self.returnstatel()
        stateinlist = False
        for key in self.qtablel.keys():
            if key == str(state):
                stateinlist = True
        if stateinlist:
            if random.random() > self.expl:
                return max(range(len(self.qtablel[str(state)])), key= self.qtablel[str(state)].__getitem__)
            else:
                return random.randint(0, 2)
        else:
            self.qtablel[str(state)] = [0, 0, 0]
            return random.randint(0, 2)
        
    def aimover(self):
        state = self.returnstater()
        self.laststater = self.returnstater()
        stateinlist = False
        for key in self.qtabler.keys():
            if key == str(state):
                stateinlist = True
        if stateinlist:
            if random.random() > self.expr:
                return max(range(len(self.qtabler[str(state)])), key= self.qtabler[str(state)].__getitem__)
            else:
                return random.randint(0, 2)
        else:
            self.qtabler[str(state)] = [0, 0, 0]
            return random.randint(0, 2)  
    def update_paddles(self):
        self.movel = self.aimovel()
        self.rewardl = -5
        if self.movel == 1:
            self.move_paddle(self.left_paddle, -PADDLE_SPEED)
        if self.movel == 2:
            self.move_paddle(self.left_paddle, PADDLE_SPEED)     
        if self.movel == 0:
            self.rewardl = 2 
        # Rechtes Paddle (Pfeiltasten)
        self.mover = self.aimover()
        if self.mover == 1:
            self.move_paddle(self.right_paddle, -PADDLE_SPEED)
        if self.mover == 2:
            self.move_paddle(self.right_paddle, PADDLE_SPEED) 
        if self.mover == 0:
            self.rewardr = 1

    # --- Spiel-Logik (unverändert) ---
    def on_close(self):
        self.game_running = False
        try:
            self.root.destroy()
        except tk.TclError:
            pass

    def draw_court(self):
        self.canvas.create_line(WIDTH//2, 0, WIDTH//2, HEIGHT, fill=FG_COLOR, dash=(15, 25))

    def reset_ball(self):
        if not self.game_running: return
        
        self.ball_pos = [WIDTH/2, HEIGHT/2]
        self.ball_vel = [0, 0]
        self.current_speed = START_SPEED
        
        r = BALL_SIZE / 2
        self.canvas.coords(self.ball, 
                           self.ball_pos[0]-r, self.ball_pos[1]-r,
                           self.ball_pos[0]+r, self.ball_pos[1]+r)
        
        if self.game_running:
            self.root.after(10, self.serve_ball)

    def serve_ball(self):
        if not self.game_running: return
        
        direction_x = random.choice([-1, 1])
        angle = random.uniform(-math.radians(30), math.radians(30))
        
        self.ball_vel[0] = self.current_speed * math.cos(angle) * direction_x
        self.ball_vel[1] = self.current_speed * math.sin(angle)

    def update_physics(self):
        if self.ball_vel == [0, 0]: return

        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]
        r = BALL_SIZE / 2
        self.rewardr = 0
        self.rewardl = 0

        if self.ball_pos[0] < 0:
            self.score_right += 1
            self.update_score()
            self.reset_ball()
        elif self.ball_pos[0] > WIDTH:
            self.score_left += 1
            self.update_score()
            self.reset_ball()

        # Wände (Oben/Unten)
        if self.ball_pos[1] - r <= 0:
            self.ball_pos[1] = r
            self.ball_vel[1] *= -1
        elif self.ball_pos[1] + r >= HEIGHT:
            self.ball_pos[1] = HEIGHT - r
            self.ball_vel[1] *= -1

        # Paddle Kollisionen
        l_pad = self.canvas.coords(self.left_paddle)
        r_pad = self.canvas.coords(self.right_paddle)

        # Linkes Paddle
        if (self.ball_vel[0] < 0 and 
            self.ball_pos[1] >= l_pad[1] and self.ball_pos[1] <= l_pad[3] and
            self.ball_pos[0] - r <= l_pad[2] and self.ball_pos[0] - r >= l_pad[0] - 10):
            self.handle_paddle_bounce(l_pad, 1)
            if self.movel == 0:
                self.rewardl = 300
            self.rewardl = 10
            self.expl -= 0.02
            print(self.qtablel)

        # Rechtes Paddle
        elif (self.ball_vel[0] > 0 and 
            self.ball_pos[1] >= r_pad[1] and self.ball_pos[1] <= r_pad[3] and
            self.ball_pos[0] + r >= r_pad[0] and self.ball_pos[0] + r <= r_pad[2] + 10):
            self.handle_paddle_bounce(r_pad, -1)
            self.rewardr = 30
            self.expr -= 0.01


        statel = self.returnstatel()
        stateinlist = False
        for key in self.qtablel.keys():
            if key == str(statel):
                stateinlist = True
        if not stateinlist:
            self.qtablel[str(statel)] = [0, 0, 0]
        self.qtablel[str(self.laststatel)][self.movel] = (1 - 0.1) * self.qtablel[str(self.laststatel)][self.movel] + 0.1 * (self.rewardl + 0.8 * max(self.qtablel[str(statel)]))
        stater = self.returnstater()
        stateinlist = False
        for key in self.qtabler.keys():
            if key == str(stater):
                stateinlist = True
        if not stateinlist:
            self.qtabler[str(stater)] = [0, 0, 0]
        self.qtabler[str(self.laststater)][self.mover] = (1 - 0.1) * self.qtabler[str(self.laststater)][self.mover] + 0.1 * (self.rewardr + 0.8 * max(self.qtabler[str(stater)]))

        self.canvas.coords(self.ball, 
                           self.ball_pos[0]-r, self.ball_pos[1]-r,
                           self.ball_pos[0]+r, self.ball_pos[1]+r)


    def handle_paddle_bounce(self, paddle_coords, direction_x):
        paddle_center_y = (paddle_coords[1] + paddle_coords[3]) / 2
        diff = self.ball_pos[1] - paddle_center_y
        normalized_diff = diff / (PADDLE_HEIGHT / 2)
        normalized_diff = max(-1.0, min(1.0, normalized_diff))
        
        # Max 45 Grad Abprallwinkel (Pong Klassiker)
        bounce_angle = normalized_diff * (math.pi / 4)
        
        #if self.current_speed < MAX_SPEED:
        self.current_speed *= SPEED_INCREMENT
            
        self.ball_vel[0] = self.current_speed * math.cos(bounce_angle) * direction_x
        self.ball_vel[1] = self.current_speed * math.sin(bounce_angle)

    def update_score(self):
        if not self.game_running: return
        self.canvas.itemconfig(self.score_display, 
                               text=f"{self.score_left}  {self.score_right}")

    def animate(self):
        if not self.game_running:
            return

        try:
            self.update_paddles() # NEU: Tasten-Paddles bewegen
            self.update_physics()
            
            self.root.after(1, self.animate)
            
        except tk.TclError:
            print("Spiel beendet.")
            self.game_running = False

if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()