number = 3
user_input = int(input("Guess the number: "))
while user_input != number:
    if user_input >= 10:
        print("Too cold")
        user_input = int(input("Try again: "))
    else:
        print("Very close")
        user_input = int(input("Try again: "))
print("Congratulations! This is the right number!")
