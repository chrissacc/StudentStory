# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")


# The game starts here.

label start:

    #BACKGROUND CLOSET
    scene bgdoornew2
    show mainnew


    e "I hid in the cloest hoping they wouldn't find me under the blankets and clothes."

    e "Keeping as still as I can."

    #change background to have more light?
    e "I notice a faint light coming from the floor of my closet."

    #maybe change to open door
    #show shadowy figure

    e "The door creaked open as a shadowy figure walked in."
    scene figure1new
    pause
    #show main character holding wire hangar

    scene bgdoornew2
    show hanger2new
    e "My grasp on the wire hangar tightens waiting for a clear shot."

    #show shadowy figure having pearly eyes

    e "Suddely the shadowy figure stop and look at me with its dark pearly eyes."
    scene figure2new
    #show character with gun
    pause
    scene bgdoornew2

    show gunnew
    pause
    show figure3new
    e "Frozen with fear, I hesitate to shoot as its eyes stare deeper into my soul."

    e "Then I just decided to run."
    scene stairsnew
    show mainnew
    e "I tried my best not to stumble down the stairs as my heart tried to jump out of my chest."
    scene policebgnew
    show mainnew
    e "I quietly ran out of my house and went to the police."

    scene policenew
    pause
    e "The advice they gave was minimal, and no action was taken."


    e "Now I feel I must find what was watching me, I will try to hunt this creature down."

    scene bush1new

    e "I then hid in the bushes, recording on my phone, the plan would be to catch this guy by surprise... "
    scene bushnew
    e "but how can I catch something that is unknown..."
    scene final1new
    pause
    e "even if I know, I know deep down others wouldn't"
    scene final2new
    e "because the monster did not exist, it was inside me all along."
    scene final3new
    pause
    scene paperstory
    e "Story made by a collection of LIU students"

    return
