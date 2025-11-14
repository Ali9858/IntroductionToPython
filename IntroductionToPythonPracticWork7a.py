
# Полный код Bubble Shooter
import simplegui
import random
import math

# -----------------------------
# Global constants
# -----------------------------

WIDTH = 600
HEIGHT = 400

# Firing position (fixed bottom point)
firing_pos = [WIDTH // 2, HEIGHT - 20]

# Initial firing angle (in radians)
firing_angle = -math.pi / 2   # straight up

ANGLE_SPEED = 0.05            # speed of angle rotation
BUBBLE_SPEED = 5              # bubble speed magnitude


# -----------------------------
# Helper functions
# -----------------------------

def angle_to_vector(ang):
    """Convert angle to unit direction vector."""
    return [math.cos(ang), math.sin(ang)]


# -----------------------------
# Bubble class
# -----------------------------

class Bubble:
    def __init__(self, sound=None):
        self.pos = firing_pos[:]   # starts at firing position
        self.vel = [0, 0]
        self.color = random.choice(["Red", "Green", "Blue", "Yellow", "Purple"])
        self.sound = sound

    def update(self):
        # movement
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # bounce from walls
        if self.pos[0] <= 10 or self.pos[0] >= WIDTH - 10:
            self.vel[0] = -self.vel[0]

    def fire(self, vel):
        """Assign velocity and play sound"""
        self.vel = vel[:]
        if self.sound:
            self.sound.play()

    def draw(self, canvas):
        canvas.draw_circle(self.pos, 10, 2, self.color, self.color)


# -----------------------------
# Global bubble object
# -----------------------------

bubble_shot_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/week7-shot2.mp3"
)

a_bubble = Bubble(bubble_shot_sound)


# -----------------------------
# Event Handlers
# -----------------------------

def keydown(key):
    global firing_angle

    if key == simplegui.KEY_MAP["left"]:
        firing_angle -= ANGLE_SPEED

    elif key == simplegui.KEY_MAP["right"]:
        firing_angle += ANGLE_SPEED

    elif key == simplegui.KEY_MAP["space"]:
        # Fire bubble
        dir_vec = angle_to_vector(firing_angle)
        velocity = [dir_vec[0] * BUBBLE_SPEED, dir_vec[1] * BUBBLE_SPEED]
        a_bubble.fire(velocity)


def draw(canvas):
    # compute firing direction
    dir_vec = angle_to_vector(firing_angle)

    # top of firing line on circle radius 60
    top = [firing_pos[0] + 60 * dir_vec[0],
           firing_pos[1] + 60 * dir_vec[1]]

    # draw firing line
    canvas.draw_line(firing_pos, top, 4, "White")

    # update + draw bubble
    a_bubble.update()
    a_bubble.draw(canvas)


# -----------------------------
# Frame
# -----------------------------

frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()
