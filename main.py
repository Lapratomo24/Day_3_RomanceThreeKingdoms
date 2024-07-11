print('''
                                 |--__
                                 |
                                 X
                        |-___   /        |--__
                        |      =====      |
                        X      | .:|      X
                        /      | O |     / 
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW______"""______WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _                                       
''')
print("Welcome to Romance of the Three Kingdoms!")

print("")
print("You fell in love with two beautiful princesses from two different kingdoms, but you can only choose one!")
print("")
print("One is waiting for you inside the Crimson Fortress of the Eastern Kingdom, and the other is similarly waiting inside the Scarlet Castle of the Western Kingdom.")
print("")
print("You started the journey and are now at a three-way intersection.")

choice = input("Where will you go? --> Type left, right, or straight: ").lower()
print("")

# Lisbeth's route

if choice == "right":
    print("You crossed the bridge and arrived at the front gate of the Scarlet Castle.")
    print("The guards informed you that princess Lisbeth is waiting for you at the garden, but your first trial awaits.")
    flower = input("--> You have to pick between two flowers. Rose or Peony? ").lower()
    print("")
    if flower == "rose":
        print("The rose has been doused with a deadly toxin by a jealous prince from another kingdom. You were killed.")
    elif flower == "peony":
        print("You chose the flower that Lisbeth loves and the guards then led you to the garden.")
        print("Now the second and final trial is upon you. Before the garden lies two front gates. Which one will you enter from?")
        gate = input("--> Choose between red or blue gate: ").lower()
        print("")
        if gate == "red":
            print("You finally met with Princess Lisbeth. You confessed your love for her and the feeling was mutual! Congratulations!!")
            print("")
            print("- Your love journey ends happily ever after! -")
        elif gate == "blue":
            print("You entered a maze and took too long to escape. Princess Lisbeth has already left the castle with the rival prince from another kingdom.")

# Myra's route

elif choice == "left":
    print("You climbed the steep stairs and arrived at the front gate of the Crimson Fortress.")
    print("The guards welcomed you with a message: Two trials set up by Princess Myra herself await.")
    animal = input("You have to tame a monster in the dungeon. Which one will you tame: a ferocious rabbit or a feisty cat? --> Type rabbit or cat: ").lower()
    print("")
    if animal == "cat":
        print("You tamed the cat, but Princess Myra would have preferred you tame the rabbit instead. She was disappointed and told you to leave.")
    elif animal == "rabbit":
        print("You tamed the rabbit easily, and you made Princess Myra's heart flutter.")
        print("The princess asked you to beat her record in rock climbing. You now have to pick between two items to help you climb.")
        item = input("--> Will you pick the chalk or the shoes? ").lower()
        print("")
        if item == "chalk":
            print("The chalk provided you with better grip despite being barefoot and you passed the trial with ease.")
            print("Princess Myra fell in love with you and you also confessed your love for her! Congratulations!!")
            print("")
            print("- Your love journey ends happily ever after! -")
        elif item == "shoes":
            print("Your hands got slippery and eventually you slipped and fell. The princess was not impressed and you failed the trial.")

# third route

else:
    print("You went into a dark cave and fell into a goblin's trap. You were killed.")

