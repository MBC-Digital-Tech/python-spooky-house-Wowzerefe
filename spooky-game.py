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
    print("A hallway is shown with a mirror at the end. ")