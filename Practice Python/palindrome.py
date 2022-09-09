from time import sleep

time = 1
while True:
    word = input("Please enter a palindrome to exit the program: ")

    if word.find(" ") != -1:
        print(
            f"{word.capitalize()} is more than one word.\nTime penalty! Please try again in {time} seconds.\n")
        sleep(time)
        time += 1

    elif word.lower() != word.lower()[::-1]:
        print(
            f"{word.capitalize()} is not a palindrome.\nTime penalty! Please try again in {time} seconds.\n")
        sleep(time)
        time += 1

    else:
        print(f"Success! {word} is a palindrome!")
        break
