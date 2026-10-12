import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#d4f1d4")
screen.title("Durga Maa - Detailed Sketch")
screen.setup(width=1000, height=1000)

t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.hideturtle()

# Helper functions
def draw_circle(x, y, radius, color, filled=True):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    if filled:
        t.fillcolor(color)
        t.begin_fill()
    t.circle(radius)
    if filled:
        t.end_fill()

def draw_oval(x, y, width, height, color, filled=True):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    if filled:
        t.fillcolor(color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if filled:
        t.end_fill()

def draw_line(x1, y1, x2, y2, color, width=2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.width(width)
    t.goto(x2, y2)

# Background glow effect
t.penup()
t.goto(0, -400)
t.pendown()
t.color("#e8f5b5")
t.fillcolor("#e8f5b5")
t.begin_fill()
t.circle(450)
t.end_fill()

# Grass at bottom
t.penup()
t.goto(-500, -300)
t.pendown()
t.color("#4a9d3f")
t.fillcolor("#4a9d3f")
t.begin_fill()
t.goto(500, -300)
t.goto(500, -450)
t.goto(-500, -450)
t.goto(-500, -300)
t.end_fill()

# Grass details
t.penup()
t.color("#3d8a33")
t.width(3)
for x in range(-500, 501, 30):
    t.goto(x, -300)
    t.pendown()
    t.setheading(90)
    t.forward(40)
    t.penup()

# Flowers in grass
flower_positions = [(-350, -320), (-200, -310), (50, -315), (280, -320), (400, -310)]
for fx, fy in flower_positions:
    t.penup()
    t.goto(fx, fy)
    t.pendown()
    t.color("#ffd700")
    t.fillcolor("#ffd700")
    t.begin_fill()
    t.circle(12)
    t.end_fill()
    t.penup()
    t.goto(fx, fy + 12)
    t.pendown()
    t.color("#ff69b4")
    for _ in range(5):
        t.forward(8)
        t.right(72)

# Tiger body - sitting position
t.penup()
t.goto(-60, -50)
t.pendown()
t.color("#ff8c42")
t.fillcolor("#ff8c42")
t.begin_fill()
t.circle(80)
t.end_fill()

# Tiger stripes
t.penup()
t.color("#333333")
t.width(4)
for offset in [-40, -20, 0, 20, 40]:
    t.goto(-60 + offset, 30)
    t.pendown()
    t.setheading(-90)
    t.forward(160)
    t.penup()

# Tiger head
t.penup()
t.goto(-60, 60)
t.pendown()
t.color("#ff8c42")
t.fillcolor("#ff8c42")
t.begin_fill()
t.circle(50)
t.end_fill()

# Tiger mane
for i in range(12):
    angle = i * 30
    x = -60 + 60 * math.cos(math.radians(angle))
    y = 60 + 60 * math.sin(math.radians(angle))
    t.penup()
    t.goto(-60, 60)
    t.pendown()
    t.color("#ff6b1a")
    t.fillcolor("#ff6b1a")
    t.begin_fill()
    t.goto(x, y)
    t.circle(15)
    t.end_fill()

# Tiger face details
draw_circle(-75, 85, 8, "#ffffff", True)
draw_circle(-45, 85, 8, "#ffffff", True)
draw_circle(-75, 85, 5, "#000000", True)
draw_circle(-45, 85, 5, "#000000", True)
draw_circle(-60, 65, 6, "#ff69b4", True)

# Tiger mouth
t.penup()
t.goto(-60, 60)
t.pendown()
t.color("#333333")
t.width(3)
t.setheading(-90)
t.forward(15)

# Goddess Durga - Main body (10 arms)
# Central body
t.penup()
t.goto(0, 80)
t.pendown()
t.color("#f5c89a")
t.fillcolor("#f5c89a")
t.begin_fill()
t.circle(60)
t.end_fill()

# Red saree/dress
t.penup()
t.goto(-80, 20)
t.pendown()
t.color("#dc143c")
t.fillcolor("#dc143c")
t.begin_fill()
t.goto(80, 20)
t.goto(100, -200)
t.goto(-100, -200)
t.end_fill()

# Gold border on saree
t.penup()
t.goto(-80, 20)
t.pendown()
t.color("#ffd700")
t.width(4)
t.goto(80, 20)
t.penup()
t.goto(-85, 0)
t.pendown()
t.goto(85, 0)

# Saree pattern details
t.penup()
t.color("#ff69b4")
t.width(2)
for x in range(-70, 71, 20):
    t.goto(x, 20)
    t.pendown()
    t.setheading(-90)
    t.forward(30)
    t.penup()

# Neck and jewelry
draw_circle(0, 95, 30, "#f5c89a", True)
t.penup()
t.goto(-40, 110)
t.pendown()
t.color("#ffd700")
t.width(3)
t.setheading(0)
t.circle(40)

# Face
t.penup()
t.goto(0, 140)
t.pendown()
t.color("#f5c89a")
t.fillcolor("#f5c89a")
t.begin_fill()
t.circle(45)
t.end_fill()

# Tilak (red mark on forehead)
t.penup()
t.goto(0, 175)
t.pendown()
t.color("#8b0000")
t.fillcolor("#8b0000")
t.begin_fill()
t.circle(8)
t.end_fill()

# Eyes
draw_circle(-20, 150, 8, "#000000", True)
draw_circle(20, 150, 8, "#000000", True)
draw_circle(-20, 152, 3, "#ffffff", True)
draw_circle(20, 152, 3, "#ffffff", True)

# Eyebrows
t.penup()
t.goto(-30, 160)
t.pendown()
t.color("#1a1a1a")
t.width(3)
t.setheading(0)
t.circle(15, 180)
t.penup()
t.goto(30, 160)
t.pendown()
t.setheading(0)
t.circle(-15, 180)

# Nose
draw_line(0, 145, 0, 130, "#d4a574", 2)

# Mouth
t.penup()
t.goto(-15, 120)
t.pendown()
t.color("#ff1493")
t.width(2)
t.setheading(0)
t.circle(15, 180)

# Crown
t.penup()
t.goto(-50, 195)
t.pendown()
t.color("#daa520")
t.fillcolor("#daa520")
t.begin_fill()
t.goto(50, 195)
t.goto(45, 240)
t.goto(0, 260)
t.goto(-45, 240)
t.end_fill()

# Crown jewels
for cx in [-30, 0, 30]:
    draw_circle(cx, 230, 8, "#ff0000", True)

# Hair
t.penup()
t.goto(-50, 175)
t.pendown()
t.color("#1a1a1a")
t.fillcolor("#1a1a1a")
t.begin_fill()
t.circle(50, 180)
t.end_fill()

# Ears and earrings
draw_circle(-45, 145, 12, "#f5c89a", True)
draw_circle(45, 145, 12, "#f5c89a", True)
draw_circle(-45, 130, 8, "#ffd700", True)
draw_circle(45, 130, 8, "#ffd700", True)

# 10 ARMS with weapons
# Each arm position and weapon
arm_data = [
    # (arm_start_x, arm_start_y, arm_end_x, arm_end_y, weapon_x, weapon_y, weapon_type, color)
    (-90, 100, -140, 80, -160, 70, "trident", "#8b7355"),
    (-80, 120, -150, 150, -170, 160, "sword", "#c0c0c0"),
    (-50, 145, -100, 180, -120, 200, "lotus", "#ff69b4"),
    (-30, 150, -60, 190, -80, 210, "chakra", "#ffd700"),
    (30, 150, 60, 190, 80, 210, "chakra", "#ffd700"),
    (50, 145, 100, 180, 120, 200, "lotus", "#ff69b4"),
    (80, 120, 150, 150, 170, 160, "sword", "#c0c0c0"),
    (90, 100, 140, 80, 160, 70, "trident", "#8b7355"),
    (-70, 80, -120, 40, -140, 20, "bow", "#8b4513"),
    (70, 80, 120, 40, 140, 20, "bow", "#8b4513"),
]

# Draw arms
for ax_start, ay_start, ax_end, ay_end, _, _, _, _ in arm_data:
    # Arm
    draw_line(ax_start, ay_start, ax_end, ay_end, "#f5c89a", 8)
    # Hand
    draw_circle(ax_end, ay_end, 10, "#f5c89a", True)
    # Bangles
    for b in range(3):
        t.penup()
        t.goto(ax_end - 5 - b*8, ay_end)
        t.pendown()
        t.color("#ffd700")
        t.width(3)
        t.setheading(45)
        t.circle(8, 180)

# Draw weapons on hands
weapons = [
    (-160, 70, "trident", "#8b7355"),
    (-170, 160, "sword", "#c0c0c0"),
    (-120, 200, "lotus", "#ff69b4"),
    (-80, 210, "chakra", "#ffd700"),
    (80, 210, "chakra", "#ffd700"),
    (120, 200, "lotus", "#ff69b4"),
    (170, 160, "sword", "#c0c0c0"),
    (160, 70, "trident", "#8b7355"),
    (-140, 20, "bow", "#8b4513"),
    (140, 20, "bow", "#8b4513"),
]

for wx, wy, wtype, wcolor in weapons:
    if wtype == "trident":
        # Handle
        draw_line(wx, wy, wx, wy - 40, wcolor, 4)
        # Three prongs
        draw_line(wx, wy - 40, wx - 15, wy - 60, wcolor, 3)
        draw_line(wx, wy - 40, wx, wy - 65, wcolor, 3)
        draw_line(wx, wy - 40, wx + 15, wy - 60, wcolor, 3)
    elif wtype == "sword":
        # Blade
        draw_line(wx, wy, wx, wy - 50, "#c0c0c0", 4)
        # Hilt
        draw_circle(wx, wy + 8, 6, "#8b4513", True)
    elif wtype == "lotus":
        draw_circle(wx, wy, 15, "#ff69b4", True)
        draw_circle(wx, wy, 10, "#ffff00", True)
        draw_circle(wx, wy, 5, "#ff1493", True)
    elif wtype == "chakra":
        # Draw circular chakra
        t.penup()
        t.goto(wx, wy)
        t.pendown()
        t.color(wcolor)
        t.width(3)
        t.setheading(0)
        t.circle(18)
        # Spokes
        for angle in range(0, 360, 30):
            t.penup()
            t.goto(wx, wy)
            t.setheading(angle)
            t.forward(18)
            t.pendown()
            t.forward(-36)
    elif wtype == "bow":
        # Bow curve
        t.penup()
        t.goto(wx, wy)
        t.pendown()
        t.color(wcolor)
        t.width(3)
        t.setheading(45)
        t.circle(25, 180)

# Halo/Aura behind goddess
t.penup()
t.goto(0, 150)
t.pendown()
t.color("#ffff99")
t.width(2)
t.setheading(0)
t.circle(130)

# Decorative particles/sparkles around
t.penup()
t.color("#ffff00")
for _ in range(20):
    import random
    sx = random.randint(-300, 300)
    sy = random.randint(-200, 280)
    t.goto(sx, sy)
    t.dot(4, "#ffff00")

# Title at bottom
t.penup()
t.goto(0, -420)
t.pendown()
t.color("#1a1a1a")
t.write("Om Jai Durga Mata", align="center", font=("Arial", 20, "bold"))

screen.update()
turtle.done()
