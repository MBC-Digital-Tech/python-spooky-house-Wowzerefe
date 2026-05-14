import random
print("The aim of the game is to escape the spooky house")
scary_sounds = ["an echoing sound of doors creaking", "a subtle sound of footsteps", "a quiet whisper in the wind"]

print("You enter a spooky house, dark, and silent. Except for", random.choice(scary_sounds))
print("Two doors sit infront of you: one RED and one BLUE")
choice1 = input("Which door will you choose? (red/blue)").lower()
if choice1 == "red":
    print("The red door creaks open... You see a dusty staircase and a dark hallway.")
    choice2 = input("Do you go UP the stairs or walk STRAIGHT to the hallway? (UP/STRAIGHT)").lower()
    if choice2 == "up":
        print("A radiant beam of light shines through the wooden flooring. A window appears infront of you. You jumped through the window and escaped! Yay!")
    else:
        print("The hallway leads to a locked door... Suddenly subtle footsteps are directed behind you. BOO! GAME OVER!")

if choice1 == "blue":
    print("A hallway is shown with a mirror at the left end. On the right end of the hallway is a beam of light.")
    choice3 = input("at the end of the hallway, do you go LEFT to the mirror, or RIGHT to the beam of light? (LEFT/RIGHT)").lower()
    if choice3 == "left":
        print("A reflection of a person is shown behind you with a weapon. Loading your firsts you punch him right on the temple. He was shown unconscious. You survived the killer. Woohoo!")
    else:
        print("You stare at the beam of light seeing a lamp. WHOOSH! The sound of a fast knife slices through you. You drop to the ground dead. GAME OVER!")