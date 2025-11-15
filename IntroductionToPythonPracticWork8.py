# Check if the bubble is stuck against the top wall
def is_stuck(bubble, top_wall_y):
    return bubble.y <= top_wall_y


# Global flag to track whether a bubble is stuck
bubble_stuck = True

# This function handles creating a new bubble when the space bar is pressed
def create_bubble():
    global bubble_stuck
    if bubble_stuck:
        # Create a new bubble and set bubble_stuck to False
        bubble_stuck = False
        # Create new bubble and set its initial position (e.g., at the bottom of the screen)
        a_bubble = Bubble(x, y)
        return a_bubble
    else:
        return None  # No new bubble until the current one is stuck


# A set to hold all the bubbles that are stuck
stuck_bubbles = set()

# When a bubble sticks, add it to the stuck_bubbles set
def add_to_stuck_bubbles(bubble):
    stuck_bubbles.add(bubble)


import math

# Function to check if two bubbles collide
def collide(self, other_bubble):
    distance = dist(self.x, self.y, other_bubble.x, other_bubble.y)
    return distance < (self.radius + other_bubble.radius)  # Assuming radius is a property of the bubbles


class Bubble:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Global flag to track whether a bubble is stuck
bubble_stuck = True
stuck_bubbles = set()

# Function to create a new bubble
def create_bubble():
    global bubble_stuck
    if bubble_stuck:
        bubble_stuck = False
        # Create a new bubble at the bottom of the screen
        new_bubble = Bubble(x=300, y=500)  # Replace with actual starting position
        return new_bubble
    else:
        return None  # No new bubble until the previous one is stuck

# Function to add a bubble to stuck_bubbles
def add_to_stuck_bubbles(bubble):
    stuck_bubbles.add(bubble)

# Function to check if a bubble is stuck
def is_stuck(bubble, top_wall_y, stuck_bubbles):
    # Check for collision with the top wall
    if bubble.y <= top_wall_y:
        return True
    # Check for collision with other stuck bubbles
    for stuck_bubble in stuck_bubbles:
        if collide(bubble, stuck_bubble):
            return True
    return False

# Function to handle bubble collisions
def collide(self, other_bubble):
    distance = dist(self.x, self.y, other_bubble.x, other_bubble.y)
    return distance < (self.radius + other_bubble.radius)

# Example of draw handler
def draw_handler():
    global bubble_stuck, a_bubble
    top_wall_y = 50  # Y-position of the top wall
    if a_bubble is not None:
        if is_stuck(a_bubble, top_wall_y, stuck_bubbles):
            add_to_stuck_bubbles(a_bubble)
            bubble_stuck = True  # Set the flag to allow the next bubble
            a_bubble = None  # Reset a_bubble to wait for the next bubble
