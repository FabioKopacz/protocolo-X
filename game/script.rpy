# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define power = Character("Power")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/normal.mp3"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "power happy.png" to the images
    # directory.

    show power happy

    # These display lines of dialogue.

    power "Cara pq vc ta aqui?"

    power "Ah, que seja."
    power "O morro do dênde é ruim de invadir."

    return
