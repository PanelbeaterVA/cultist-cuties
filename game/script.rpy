# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mentor")
define y = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mentor happy

    # These display lines of dialogue.

    m "Ah! Good, you're here. I'd thought you might've gotten cold feet after our last conversation."

    m "..."

    m "You're all set, then? There's no turning back now."

    y "Yes, Doctor."

    "They stepped aside to allow me in, revealing a small but well-appointed entry hall"

    "I had, of course, visited the Doctor's home in the past. This would be the first time they allowed me into their study."

    "Months of preparation, of ingratiation, of scrutiny and denial: it had all led to this."

    scene bg study

    "The study was underwhelming, at first. I suppose some part of me must have expected to find the walls 
        filled with scrawled drawings and frantic notes as to the hidden nature of reality." 
    
    "If not for the strangely titled books on the shelves, I might not have been able to tell it apart from the study of any other academic."

    "At a glance, it was tidy and unassuming, like the Doctor themself."

    show mentor happy

    m "You'll be working here, by the window"

    scene bg study_variant_1

    "The workspace he'd assigned me was small, and required me to sit with my back to him. He still didn't trust me."

    m "This is your last chance to turn away from this dark path, my young friend. Are you sure this is what you desire?"

    menu:
        "Yes":
            jump choice_yes
        "No":
            jump choice_no
    
    label choice_yes:

        scene bg study

        "For a moment, my heart wavered. I knew, in that moment, that had I wanted to, I could have simply left that place. 
            I could have descended the stairs to the landing, thrown open the front door, and never returned. The Doctor would not have stopped me"

        "But I could not bring myself to. Not when Id worked so hard to find myself there."

        jump choice_no

    label choice_no:

        scene bg study

        "I'm sure, Doctor."



    # This ends the game.

    return
