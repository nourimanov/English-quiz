print("Hi, welcome to our English 📚 quiz!")
name = input("What's your name 👤: ")

words = ("example", "silent", "useful", "unlimited", "famous", "client",
         "terminate", "cooking", "kinder", "school", "children", "shopping",
         "notebook", "telephone", "friendly", "interesting", "question")

life, score = 3, 0
flag = True

while flag:
    count = 0
    for word in words:
        count += 1
        length = len(word) - 2
        print("\nSecret word 🔒:", word[:1:] + length * ' * ' + word[len(word)-1:])
        true_word = input("Can you guess this word 🔤: ")

        if word == true_word:
            print("Congrats ✅ indeed this word", word)
            score += 3
        else:
            print("Sorry ❌ this word", word)
            life -= 1
            if life == 0:
                flag = False
                break
    if score == len(words) * 3:
        print("\nYou're perfect 🔥 your score:", score)
        break
    elif count == len(words):
        print("\nGame over 👍 your score:", score)
        break
    else:
        print("\nYou haven't life for playing game ☹️\n"
              "Your score:", score)
