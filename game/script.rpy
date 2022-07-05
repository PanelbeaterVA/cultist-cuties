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

    scene bg black

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

    scene bg study_with_desk_no_journal

    "The workspace he'd assigned me was small, and required me to sit with my back to him. He still didn't trust me."

    m "This is your last chance to turn away from this dark path, my young friend. Are you sure this is what you desire?"

    menu:
        "Yes":
            call choice_yes
        "No":
            call choice_no

    m "Very well. Feel free to use this space to your liking."

    scene bg study_with_desk_jorunal

    "Our work begins tomorrow. Tonight, be sure to rest well."

    hide mentor happy
    scene bg black

    "My first night as a resident of the Doctor's home was a restless one.
        Despite having slept in his guest room before on many occasions, I found myself plagued with strange thoughts,
        besieged by a yearning for something I had never had and could not identify."

    "I must have slept, but when morning came, I could not recall having closed my eyes."

    m "Given the hour, I trust you're not still dozing, my young friend."

    y "I'm awake, Doctor. Good morning."

    show mentor happy

    m "Good morning."

    m "..."

    m "Unless it offends you, we'll take our breakfast in the study, as is my habit.
        I would prefer not to lose another minute to useless dawdling."

    "The sky was still pink and grey with the colours of the dawn, and yet the Doctor behaved as though I had been lingering in bed until noon."

    "While I had expected it, it still irked me. He seemed, somehow, not to require the same burden of sleep as others,
        and did not seem to understand it as a trait unique to himself rather than a failing of others."

    scene bg study

    m  "You may eat at your desk, if you'd like, or dine with me at mine, if you'd prefer to have company-
        provided you do not interrupt my work with idle chatter."

    "My fingers itched at the chance to examine the Doctor's workspace and materials more closely,
        but it would not do to have him suspect me of any greater ambitions than those necessary to serve his own.
        I knew a quiet and solitary breakfast was wiser, though my curiosity would go unsated."

    menu:
        "Dine Alone.":
            call dine_alone
        "Dine with the Doctor.":
            call dine_together

    "end of story"

    return

label choice_yes:

    "For a moment, my heart wavered. I knew, in that moment, that had I wanted to, I could have simply left that place.
        I could have descended the stairs to the landing, thrown open the front door, and never returned. The Doctor would not have stopped me"

    "But I could not bring myself to. Not when Id worked so hard to find myself there."

label choice_no:

    "I'm sure, Doctor."

    return

label dine_alone:
    "I knew myself well enough to know I would be unable to restrain my curiosity,
        and the Doctor was unlikely to look kindly on my asking too many questions
        on our first day as collaborators."

    "Reluctantly, I sat down to eat alone. The meal was nutritious but unexciting,
        as was to be expected of food supplied by a man who ate only to sustain himself
        and seemed to take little enjoyment in"
    return

label dine_together:
    "Narration"
    return
