import simplegui
import random

# List of card images (front and back)
l1 = ['https://www.clker.com/cliparts/2/7/e/d/11950018381373389108white_c_q.svg.med.png',
      'https://www.clker.com/cliparts/8/d/d/f/11950019381866175679white_d_q.svg.med.png',
      'https://www.clker.com/cliparts/d/0/1/0/1195002039492802872white_h_q.svg.med.png',
      'https://www.clker.com/cliparts/6/0/7/6/11950021591895641769white_s_q.svg.med.png',
      'https://www.clker.com/cliparts/d/c/4/d/11950021521779817159white_s_k.svg.med.png',
      'https://www.clker.com/cliparts/1/8/1/d/1195002031361354547white_h_k.svg.med.png',
      'https://www.clker.com/cliparts/d/8/0/a/11950019312129275767white_d_k.svg.med.png',
      'https://www.clker.com/cliparts/6/0/e/8/11950018301356291291white_c_k.svg.med.png']

l2 = ['https://www.clker.com/cliparts/2/7/e/d/11950018381373389108white_c_q.svg.med.png',
      'https://www.clker.com/cliparts/8/d/d/f/11950019381866175679white_d_q.svg.med.png',
      'https://www.clker.com/cliparts/d/0/1/0/1195002039492802872white_h_q.svg.med.png',
      'https://www.clker.com/cliparts/6/0/7/6/11950021591895641769white_s_q.svg.med.png',
      'https://www.clker.com/cliparts/d/c/4/d/11950021521779817159white_s_k.svg.med.png',
      'https://www.clker.com/cliparts/1/8/1/d/1195002031361354547white_h_k.svg.med.png',
      'https://www.clker.com/cliparts/d/8/0/a/11950019312129275767white_d_k.svg.med.png',
      'https://www.clker.com/cliparts/6/0/e/8/11950018301356291291white_c_k.svg.med.png']

# Full deck of cards (duplicated)
l = l1 + l2
li = [0] * 16  # Keeps track of revealed cards
tracker1 = tracker2 = 0
idx1 = idx2 = 0
state = 0  # Track the state of the game (0 = first card, 1 = second card, 2 = check match)
newgame = 1
turns = 0

# Shuffle the deck at the start
random.shuffle(l)
image2 = 'http://www.silent9.com/blog/uploads/gimp/2source.png'

# Load all the card images once
images = [simplegui.load_image(url) for url in l]

# Load the back image of the card (when it's hidden)
back_image = simplegui.load_image(image2)

# Initialize the game state
def new_game():
    global state, newgame, li, turns
    state = 0
    newgame = 1
    turns = 0
    random.shuffle(l)
    label.set_text("Turns = " + str(turns))
    li = [0] * 16  # Reset all cards to face down

# Define mouse click handler
def mouseclick(pos):
    global state, tracker1, tracker2, idx1, idx2, newgame, turns
    for i in range(16):
        # Check if the click is within the bounds of the current card
        if pos[0] >= 50 * i and pos[0] <= 50 * (i + 1) and not li[i]:
            if newgame:
                if state == 0:
                    li[i] = 1
                    state = 1
                    tracker1 = l[i]
                    idx1 = i
                elif state == 1:
                    li[i] = 1
                    state = 2
                    tracker2 = l[i]
                    idx2 = i
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                elif state == 2:
                    # If cards don't match, hide them again
                    if tracker1 != tracker2:
                        li[idx1] = 0
                        li[idx2] = 0
                    li[i] = 1
                    state = 1
                    tracker1 = l[i]
                    idx1 = i
                    newgame = 0
            else:
                if state == 1:
                    li[i] = 1
                    state = 2
                    tracker2 = l[i]
                    idx2 = i
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                elif state == 2:
                    # If cards don't match, hide them again
                    if tracker1 != tracker2:
                        li[idx1] = 0
                        li[idx2] = 0
                    li[i] = 1
                    tracker1 = l[i]
                    idx1 = i
                    state = 1

# Define draw handler to display cards
def draw(canvas):
    for i in range(16):
        if li[i]:  # Card is revealed, draw the front image
            canvas.draw_image(images[i], (50 / 2, 100 / 2), (50, 100), (50 * i + 25, 100 / 2), (50, 100))
        else:  # Card is hidden, draw the back image
            canvas.draw_image(back_image, (50 / 2, 100 / 2), (50, 100), (50 * i + 25, 100 / 2), (50, 100))

# Create frame, add button and label
frame = simplegui.create_frame("Memory", 800, 200)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# Register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Start the game
new_game()
frame.start()
