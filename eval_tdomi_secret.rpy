#Changes dialogue for when you arrive at the orphanage
#Incorporate a Vara mood counter for how she reacts? Oh god that sounds not fun
label eval_secret_orphanage_arrival:
    Ry "Amely? Vara? Are you two here?"
    show amely smnormal with easeinright
    Am "Hello!"
    Ry smile "Hello, Amely."
    Ry normal "Do you know where Vara is?"
    Am "She is coming."
    show vara smnormal behind amely with easeinright
    Vr "..."
    c "Hi, Vara."
    Vr "Hello."
    Ry "She's been talking much more since you last saw her, [player_name]."
    c "That's great to hear."
    Vr "It's dark."
    Ry "I see that, Vara. I wonder who turned the lights off. Usually we leave them on for you."
    c "Wait, is the orphanage just a classroom?"
    Ry look "Sadly, this is most of the space that the orphans get. They play, learn, study, and eat in here or outside for most of the day."
    c "Where do they sleep?"
    Ry normal "We have some small bedrooms for them down the hall."
    Ry "At the moment, the council has it completely closed off."
    c "Is that for any particular reason?"
    Ry "Not exactly. They probably don't want random dragons just waltzing in and taking the childrens' beds."
    c "That makes sense. So what exactly are we doing here today?"
    Ry "Let's take a look."
    hide remy with easeoutleft
    Am "I come!"
    hide amely with easeoutleft
    m "Vara stayed by my side as the two dragons went to the lightswitch."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (1.0)
    play sound "fx/lightbreak.mp3"
    $ renpy.pause (2.0)
    Am "Uh oh!"
    show vara smshocked with dissolvemed
    Ry look "Well, that's not good."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    show remy normal flip behind vara with easeinleft
    show remy normal behind vara with dissolvemed
    show amely smnormal flip with easeinleft
    show amely smnormal with dissolvemed
    show vara smnormal behind amely with dissolvemed
    Ry "I think I know something that we're going to have to do."
    c "Fix the lights?"
    Ry smile "How'd you guess?"
    c "Not sure. Maybe I'm psychic."
    Ry "Well, if you're psychic, do you know what else is wrong here?"
    c "I think my powers only work once a day."
    Ry normal "Alright then. From what I can remember, that desk in the middle of the room is very broken."
    c "How'd that happen?"
    Ry look "You know how I said that learning to control fire or acid breath can be difficult for young dragons?"
    Ry "Well, Vara managed to melt one of the legs of the desk."
    Am "It was cool!"
    Vr smsad "I didn't mean to..."
    Ry normal "Don't feel bad, Vara. You were still learning and nobody got hurt."
    Vr "..."
    Vr smnormal "Okay..."
    Ry normal "Anyways, we should also try to go through the hatchlings' art and the paperwork left around."
    Ry "And finally, just clean up the place a little bit. These walls have seen one too many crayons in their time."
    m "I noticed a plethora of crayon scribbles on the wall that stopped at around Amely's height."
    Ry look "Not to mention that the books in here have seen better days."
    c "How should we do this?"
    Ry normal "Most of the supplies we have here are scattered around in a few locations near this building."
    Ry "So I think you should stay here while I grab things for you."
    Am "I help?"
    Ry "Sure, Amely."
    Am "Yay!!!"
    Ry "Would you like to come along as well, Vara?"
    Vr "I stay here."
    c "It'll be nice to have an extra set of hands, or I guess claws, to help."
    Ry smile "Sounds like a plan. Let's do this!"
    show remy normal behind vara with dissolvemed
    jump eval_secret_orphanage_game_init

label eval_everyone_1:
    m "This content is currently under development. Check back in 3-5 business days."
    return