#This is all of the stuff used to handle Katsuharu's minigame
#If you're looking for correct dialogue options/cheats, scroll down a bit :)

#Reminder to decide if I should add a scoreboard with # of customers served and # of happy customers

#General concept:
    #Player serves ice cream to 10 different customers in line
    #Randomly place 3 characters: Emera, Dramavian, and Kalinth - Could do more or even have every customer actually have artwork using the minor characters
        #How many do I have? 8th, Dramavian, Emera, Grey, Kalinth, Kevin, Leymas, Ophinia, Xith, Lucius - That's 10 right there. Why not?
    #Characters can have 3 moods: In a hurry, don't mind waiting, or very hungry <-- Subject to change. Give user 3 options to satisfy their wants.
        #Give individual dialogue to every character to give hints to their wants
    #Make an underdeveloped side character a reporter and make a scoop pun - I could even do something with this later down the line???
    #I really don't know how to make the evalCustomerScore influence the actual ending here. I'm thinking of adding a final, full ending with ONLY Remy
        #This will unlock after you have done everything else. Maybe some memes as well, we'll see...
#And... Lets go!

label eval_katsu_help_init:
    #Shuffle the customers for a surprise every time!
    $ customers = ["8", "Dram", "Em", "Grey", "Kali", "Kev", "Ley", "Oph", "Xith", "Lucius"]
    $ renpy.random.shuffle(customers)

    $ evalPlayedKatsuGame = True

    #Number of customers already served
    $ evalServedCustomers = 0

    #Give the intro to each character a bit of character
    $ evalRandomNewCustomerDialogue = 0

    #Total score based off of how you satify customer needs. Perfect score is 10
    $ evalCustomerScore = 0

    #How the customer wants their ice cream
    $ evalCharacterMood = 0 #0 - Fast, 1 - Clean, 2 - A lot

    #How you serve the ice cream
    $ evalQualityServed = 0

    #A character's preferred ice cream choice
    $ evalCharacterPreferredFlavor = ""

    #Whether Ophilia comes back for seconds and her position in line
    $ evalOphSeconds = False
    $ evalOphPosition = 0

    #Show ECK's extra info display
    show screen evalextrainfo
    $ evalextradisplay = 2


label eval_katsu_help:
    #Update the display
    $ evalDisplayVar1name = "Customers Served:"
    $ evalDisplayVar1 = evalServedCustomers
    $ evalDisplayVar1unit = ""

    $ evalDisplayVar2name = "Happy Customers:"
    $ evalDisplayVar2 = evalCustomerScore
    $ evalDisplayVar2unit = ""


    #Finish up the minigame or give Ophinia her second scoop
    if evalServedCustomers == 10:
        if evalOphSeconds:
            m "A familiar face walked up to the stand. She still had ice cream in her hand."
            show ophinia normal with easeinright
            c "You know, you really didn't have to wait in line a second time."
            if evalOphPosition == 10:
                Op "But there wasn't even a line anymore! I just walked around the stand."
                c "Good point."
            else:
                Op "Nonsense. I should have to wait like everyone else."
            c "Well, let me get you another scoop then. Same flavor?"
            Op "Well... I..."
            c "Yes. Mango coming right up."
            Op "Thank you."
            m "I turned back to Katsuharu."
            c "One last scoop of mango ice cream."
            if evalCurrentEnding == 4:
                Ka "Alright...{nw}!"
                Vr "I'll do it!"
                m "Vara quickly made the scoop and passed it over to me."
            else:
                Ka "On it!"
                m "The two dragons quickly made the scoop and passed it over to me."
            m "I turned back to the dragon."
            c "Here you are!"
            Op "Thank you!"
            m "She grabbed the cone, then carefully rested it in the box on her head. It seemed to simply disappear."
            c "What the..."
            Op "What?"
            c "How is the ice cream staying in the box?"
            Op "I don't know. I don't like asking those kinds of questions."
            Op "Thank you again for the ice cream!"
            c "No problem..."
            hide ophinia with easeoutleft
            m "With that, she paid and left for a second time."
            c "(That was a very confusing series of events.)"
            $ evalCustomerScore += 1
        hide screen evalextrainfo
        if evalCurrentEnding == 3:
            jump eval_remy_amely_adine_2
        elif evalCurrentEnding == 4:
            jump eval_everyone_2
    
    #Some intermediate dialogue
    if evalServedCustomers == 2:
        m "I noticed that we were starting to catch up with the line of dragons."
    
    if evalServedCustomers == 8:
        m "I noticed that the end of the line was quickly approaching. We were almost done."
    
    #Some fun scenes to throw in
    if evalServedCustomers == 3:
        m "Suddenly, I saw two streaks pass my vision."
        Ad normal b "Amely! Where are you going?"
        show amely smnormal flip with easeinleft
        Am "Wheeeeeeeeeee!!!!"
        hide amely with easeoutright
        $ renpy.pause (1.0)
        show adine annoyed b flip with easeinleft
        Ad "This little dragon is going to be the death of me."
        hide adine with easeoutright
        m "Looks like Adine isn't doing her job very well..."
    
    if evalServedCustomers == 7:
        m "Suddenly, I saw Amely run past the stand."
#        show amely smnormal at Position(xpos=.0, xanchor='right') with easeinright
        show amely smnormal at Position(xpos=.99, xanchor='left') with easeinright
        hide amely with easeoutleft
        $ renpy.pause (1.0)
        m "Wait. Where did Adine go?"
        play sound "fx/takeoff.ogg" #Might want to change
        m "A yellow streak flew in from the air and snatched up the little dragon."
        Ad normal c "Gotchya!"
        Am smsad "Let go!"
        Ad "No way, Amely. I've already made that mistake today."
    
    #Give it a bit of character
    $ evalRandomNewCustomerDialogue = renpy.random.randint(0, 2)
    if evalServedCustomers == 0:
        c "Our first customer walked up to the stand."
    elif evalRandomNewCustomerDialogue == 0:
        c "Another customer walked up to the stand."
    elif evalRandomNewCustomerDialogue == 1:
        c "The next dragon made their way to the stand."
    else:
        c "The next customer in line walked up to the stand."
    
    $ evalCharacterMood = renpy.random.randint(0, 2) #0 - Fast, 1 - Clean, 2 - A lot

    #Oh god...
    if customers[evalServedCustomers] == "8":
        jump eval_help_8th
    elif customers[evalServedCustomers] == "Dram":
        jump eval_help_dram
    elif customers[evalServedCustomers] == "Em":
        jump eval_help_em
    elif customers[evalServedCustomers] == "Grey":
        jump eval_help_grey
    elif customers[evalServedCustomers] == "Kali":
        jump eval_help_kali
    elif customers[evalServedCustomers] == "Kev":
        jump eval_help_kev
    elif customers[evalServedCustomers] == "Ley":
        jump eval_help_ley
    elif customers[evalServedCustomers] == "Oph":
        jump eval_help_oph
    elif customers[evalServedCustomers] == "Lucius":
        jump eval_help_luc
    elif customers[evalServedCustomers] == "Xith":
        jump eval_help_xith
    
label eval_katsu_help_2:
    #I might add a bit of random variation in the text to spice this up, although it's also fine how it is now IMO
    m "I turned back to Katsuharu."

    menu:
        c "(How should I tell Katsuharu to make the ice cream?)"
        "Make it quickly.":
            c "One scoop of [evalCharacterPreferredFlavor] Katsuharu! Let's go a bit quickly on this one!"
            Ka "On it!"
            if evalCurrentEnding == 4:
                m "Remy grabbed a sugar cone while Vara took out a scoop of [evalCharacterPreferredFlavor] and placed it on top."
            else:
                m "The dragon quickly grabbed a sugar cone while Remy took out a scoop of [evalCharacterPreferredFlavor] and placed it on top."
            m "It wasn't perfect, but it still looked okay."
            $ evalQualityServed = 0
        
        "Make it carefully.":
            c "One scoop of [evalCharacterPreferredFlavor] Katsuharu! Let's take our time on this one and make it look good!"
            Ka "On it!"
            if evalCurrentEnding == 4:
                m "Remy grabbed a sugar cone from the pile. Katsuharu grabbed it from Remy's grasp and threw it away."
                Ka "That cone didn't look great. Let's get another."
                m "Remy carefully chose another cone and handed it to Vara, who took a scoop of [evalCharacterPreferredFlavor] and carefully rested it on top."
            else:
                m "The dragon grabbed a sugar cone, inspected it, and then chose another. Remy then took a scoop of [evalCharacterPreferredFlavor] and carefully rested it on top."
            m "It looked remarkable. I was tempted to take a bite myself."
            $ evalQualityServed = 1
        
        "Make it large.":
            c "A nice, large helping of [evalCharacterPreferredFlavor], Katsuharu!"
            Ka "On it!"
            if evalCurrentEnding == 4:
                m "Remy grabbed a sugar cone while Vara took out a large scoop of [evalCharacterPreferredFlavor] and placed it on top."
                m "Katsuharu looked at the cone for a second."
                Ka "Let's add a bit more."
                m "Katsuaru dipped his claw into the vat of [evalCharacterPreferredFlavor] and added a bit more to the top."
                Ka "Perfect."
            else:
                m "The dragon grabbed a sugar cone while Remy took out a large scoop of [evalCharacterPreferredFlavor] and placed it on top."
                m "Katsuharu looked at the cone for a second."
                Ka "Let's add a bit more."
                m "Remy added a bit more ice cream to the top."
                Ka "Perfect. Nice job Remy."
                Ry "Thanks!"
            $ evalQualityServed = 2

    m "Katsuharu handed me the cone."
    return


#Character dialogue - I think the dialogue is a bit lackluster at the moment. I should try to give it more character once everyone is done.
#Oh god this is gonna be a lot of writing - 70 branches of dialogue. Oof.
#It is surprisungly difficult to write the same thing 10 times over with each feeling unique.

#Note to self going forward. Don't be shy to reuse more concepts in different branches. Playtesting through, I think it works well reusing the content

#If you're looking for "cheats" for this minigame, you're in the right place.
label eval_help_8th:
    $ evalCharacterPreferredFlavor = "strawberry"
    show 8th normal with easeinright
    Ei "Hello. You must be [player_name]."
    c "Sure am!"
    Ei "I guess it's hard to mix you up with anyone else. Being the only human and all."
    c "True."
    if evalCharacterMood == 0:
        Ei "I'm in a bit of a rush at the moment. This line took much longer than expected."
        c "Sorry about that. What would you like?"
    elif evalCharacterMood == 1:
        Ei "The line was a bit long, but I didn't mind. It was nice chatting with the other dragons."
        c "Glad to hear that. What would you like?"
    elif evalCharacterMood == 2:
        Ei "All this waiting has really gotten to my stomach."
        c "I can relate. What would you like?"
    Ei "Could I get a scoop of strawberry, please?"
    c "Yep. One scoop of strawberry coming right up."
    call eval_katsu_help_2 from eval_help_8th_2
    c "Here you are. Enjoy!"

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Ei "Ah, thank you! Great service too!"
            c "Thank you!"
            $ evalCustomerScore += 1
        else:
            Ei "Hm, looks great, but I really need to get going now."
            c "Of course. Have a nice day."
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Ei "Thank you! This looks amazing!"
            c "Of course! We took extra care to make this one."
            Ei "It really shows!"
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Ei "Looks good, but Katsuharu might be losing his magical touch."
            c "Is everything alright with it?"
            Ei "Yes. It just looks a bit different from what I remember."
        else:
            Ei "This looks amazing, but I doubt I'm going to be able to eat it all!"
    else:
        if evalCharacterMood == evalQualityServed:
            Ei "Wow! That's a lot of delicious looking ice cream! Thanks!"
            $ evalCustomerScore += 1
        else:
            Ei "Thank you, this looks really good! I should have ordered more, though."
            c "You can order another cone if you like."
            Ei "It's alright. I don't want to hold up the line any longer."
    
    hide 8th with easeoutleft
    m "With that, he paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_dram: #... dot dot dot ...
    $ evalCharacterPreferredFlavor = "mango"
    show dramavian normal with easeinright
    Dr "..."

    if persistent.evalSeenDramavian:
        c "Hello again..."
        Dr "..."
        m "I already knew how this was going to go."
        c "What can I get for you?"
    else:
        c "Hello?"
        Dr "..."
        m "Why does this guy only say the word 'dot' three times?"
        c "Ummm... Can I help you?"
    
    m "The dragon pointed at the vat containing the mango ice cream."
    c "I assume that you want the mango?"
    Dr "..."
    m "He nodded."

    if evalCharacterMood == 0:
        if persistent.evalSeenDramavian:
            Dr "Quick..."
            c "Did you just say something?"
            Dr "..."
            c "Nevermind."
        else:
            Dr "..."
            m "He looked down to where one would normally wear a watch."
    elif evalCharacterMood == 1:
        if persistent.evalSeenDramavian:
            Dr "Good..."
            c "Did you just say something?"
            Dr "..."
            c "Nevermind."
        else:
            Dr "..."
            m "He looked around, seeming to judge the scoops others had received before him."
    elif evalCharacterMood == 2:
        if persistent.evalSeenDramavian:
            Dr "Big..."
            c "Did you just say something?"
            Dr "..."
            c "Nevermind."
        else:
            Dr "..."
            m "He continued looking at the mango ice cream, drool welling up on his muzzle."
    
    call eval_katsu_help_2 from eval_help_dram_2
    c "Here you go..."
    if persistent.evalSeenDramavian:
        m "I purposely said the three dots out loud."
    else:
        m "I found myself also saying the three dots out loud."
    
    if evalCharacterMood == evalQualityServed:
        Dr "..."
        if persistent.evalSeenDramavian:
            Dr "Thanks..."
            m "I smiled."
            c "Any time."
            Dr "..."
        
        $ evalCustomerScore += 1
    else:
        Dr "..."
        if persistent.evalSeenDramavian:
            Dr "Good..."
            c "Glad to hear it."
    
    hide dramavian with easeoutleft
    m "With that, he paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_em:
    $ evalCharacterPreferredFlavor = "cherry"
    show emera normal with easeinright
    Em laugh "Why, what a surprise! What are you doing here [player_name]?"
    c "Just helping out Katsuharu for a while."
    Em normal "Well. I'm quite happy to see you recovered. I was worried about you."
    c "Thanks for the concern. Other than being a bit tired, I'm fine."

    if evalCharacterMood == 0: #For 2 say she just got out of a business meeting
        Em "Sorry to cut our chat short, but I've got a business meeting quite soon."
        c "No problem. What can I get you?"
        Em ques "I'll take the cherry please. It is quite a sophisticated flavor if you ask me."
    elif evalCharacterMood == 1:
        Em "Sorry, but much as I would love to spend all day chatting, I don't think it would look good on my record to hold up the line." #This might be a little too confusing
        c "Of course. What can I get you?"
        Em ques "I'll take only your finest scoop of cherry, please. It is quite a sophisticated flavor if you ask me."
    elif evalCharacterMood == 2:
        Em "But enough about you. I just got out of a heated meeting and I'm quite hungry."
        c "Of course. What can I get you?"
        Em ques "I'll take the cherry please. It is quite a sophisticated flavor if you ask me."
    
    c "One scoop of cherry coming right up!"
    call eval_katsu_help_2 from eval_help_em_2
    c "Here you go. Enjoy!"

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Em laugh "Thank's for making it fast. Now I should have plenty of time to make it to the meeting."
            c "Happy to help."
            $ evalCustomerScore += 1
        else:
            Em frown "Hm, this looks good, but I really have to get going now. This took longer than I expected."
            c "I understand. Have a nice day."
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Em laugh "Wow, Katsuharu still manages to make his ice cream look absolutely stunning."
            c "I'm glad to see that you like it."
            Em normal "Please make sure to tell Katsuharu that."
            c "I will."
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Em frown "Looks good, but I don't really think it's up to my standards."
            c "Should I get you another?"
            Em "Don't bother. This will suffice."
        else:
            Em frown "This is a lot of ice cream. Are you implying I look fat?"
            c "N... No. Of course not! I just thought that a bit of extra ice cream never hurt."
            if askiffat:
                m "So this is how Remy felt earlier."
            Em normal "I will choose to believe your statement this time, [player_name]."
    else:
        if evalCharacterMood == evalQualityServed:
            Em laugh "Wow! That's definitely enough to cool off after that meeting."
            $ evalCustomerScore += 1
        else:
            Em "Thank you, this looks quite good. In hindsight I should have asked for a bit more. That meeting really did a number on me."
            c "You could order another if you like."
            Em "It is quite alright. I don't want to anger anyone else behind me."
    
    hide emera with easeoutleft
    m "With that, she paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_grey:
    $ evalCharacterPreferredFlavor = "vanilla"
    show grey normal with easeinright
    Gr "Oh! Fancy meeting you here again!"
    c "Quite a conincidence that both times we've met, I've been working with Katsuharu."
    Gr "Indeed."
    if evalCharacterMood == 0:
        Gr "Sorry to be so cut and dry, but I'm running late to an art showing."
        c "No worries! What can I get you?"
        Gr "Could I get a scoop of vanilla, please?"
    elif evalCharacterMood == 1:
        Gr "Did you notice how many people are here today? Sometimes, it's nice to just be able to hang out and talk. Especially if ice cream is involved as well."
        c "Couldn't agree more. What flavor would you like?"
        Gr "I'll take the vanilla, please."
    elif evalCharacterMood == 2:
        Gr "I haven't had any of Katsuharu's ice cream since I last saw you, actually."
        m "The dragon hungrily looked down at the vanilla."
        c "I assume by your stares that you would like the vanilla."
        Gr "Yes please!"
    
    c "Perfect. Let me get that for you."
    call eval_katsu_help_2 from eval_help_grey_2
    c "Here you go!"

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Gr "Great! Thanks for making it quick!"
            c "Of course. Didn't want you to be late."
            Gr "Thank you! This could make or break my career as an artist!"
            c "I would say good luck, but I doubt you need it."
            Gr "How so?"
            c "I think I've seen some of your work. It's magnificent."
            Gr "Thank you! I should probably get going now."
            $ evalCustomerScore += 1
        else:
            Gr "That looks good. Thanks!"
            c "No problem."
            Gr "I should really get going now, this meeting is really important."
            c "Of course. Good luck!"
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Gr "Wow! I know that Katsuharu puts a lot of time and dedication into his craft, but this is a true work of art."
            c "Coming from an artist like yourself, I assume we should take that as quite the compliment."
            Gr "Absolutely!"
            c "Well, thank you. I'll make sure to tell Katsuharu how much you appreciate his work."
            Gr "Please do. I should get going before the dragons behind me start getting too angry."
            c "Good plan. It was nice seeing you again!"
            Gr "You too!"
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Gr "This doesn't quite look like how it did when I came here before."
            c "Is everything alright with it?"
            Gr "Yes. I guess I shouldn't blame Katsuharu. He seems really busy right now, so he probably doesn't have the time to be as careful and precise as he normally is."
            c "We are quite busy today."
            Gr "Don't worry, I totally understand. Have a nice day!"
        else:
            Gr "This looks great! How am I ever going to eat all of this, though?"
            c "No worries. I gave you a bit extra, it's on the house."
            Gr "Oh, thank you! Still, I hate to waste perfectly good ice cream."
            Gr "Anyways, I best get going. I have an art meeting soon and I should try to get there early."
            c "Oh course, have a nice day!"
            Gr "You too!"
    else:
        if evalCharacterMood == evalQualityServed:
            Gr "Wow! That's a lot of ice cream! Perfect to calm the nerves before my art showcase later today."
            c "Art showcase?"
            Gr "Yeah! A bunch of the higher ups like Emera are interested in my artwork!"
            c "That's great! I'm sure they'll love it."
            Gr "I sure hope so. Have a nice day!"
            $ evalCustomerScore += 1
        else:
            Gr "This looks amazing! I should have ordered more. This might not be enough to calm my nerves before my art showcase later today."
            c "Art showcase?"
            Gr "Yeah! A bunch of the higher ups like Emera are interested in my artwork!"
            c "You could order another cone to calm your nerves."
            Gr "Don't worry about it. This should be enough, and I don't want to hold up the line any longer."
    
    hide grey with easeoutleft
    m "With that, Grey paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_kali:
    $ evalCharacterPreferredFlavor = "chocolate"
    show kalinth normal with easeinright
    Kl "Oh! Hello again, [player_name]."
    c "Hello Kalinth. It's nice to meet you in a less... stressful environment."
    Kl "Likewise. I had to sort more papers in these past few weeks than I have in my entire career as an archivist."
    c "Sounds like a lot of fun."
    Kl "So much fun..."
    if evalCharacterMood == 0:
        Kl "This line was much longer than I was anticipating, and Bryce wants me at the police station to finish up on the investigation papers, so I shouldn't stay too long."
        c "You still aren't done?"
        Kl "This may be the biggest investigation in dragon history. There was bound to be endless paperwork."
        c "Understandable. I'll try not to keep you too long. What flavor did you have in mind?"
    elif evalCharacterMood == 1:
        Kl "Although I must say, despite this line being quite long, it was nice to get out of the station for a while."
        Kl "I'm in no rush to go back into that stuffy building."
        c "They should really open a few windows in there."
        Kl "Right?"
        c "Anyways, which flavor would you like?"
    elif evalCharacterMood == 2:
        Kl "I must say, all that paperwork really works up a person's appetite. I can't wait to get my claws on some ice cream!"
        c "Well. you're definitely in the right place."
        Kl "Wow, thank you detective."
        c "Anytime. What can I get you?"
    Kl "I'll take a scoop of chocolate, if you don't mind."
    c "Coming right up!"
    call eval_katsu_help_2 from eval_help_kali_2
    c "Here's your chocolate ice cream."

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Kl "Perfect! I should probably get going before Bryce throws a fit."
            c "He is not the kind of dragon I would want to see mad."
            Kl "It's not pretty, I've seen it before."
            $ evalCustomerScore += 1
        else:
            Kl "Looks wonderful, but I've really got to get going now. Bryce is probably going to throw a fit."
            c "That doesn't sound pretty."
            Kl "It's not, I promise."
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Kl "This looks beautiful! Thank you!"
            c "For all of your hard work on the case I thought spending a bit of extra time to make it perfect was the least we could do."
            Kl "I appreciate that. It's things like this that make the job worth it."
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Kl "This looks good, [player_name], but Katsuharu might want to slow down a bit."
            c "Why? Is something wrong?"
            Kl "Nothing is wrong. It's just a bit sloppier than I'm used to."
            c "Would you like us to remake it?"
            Kl "Don't worry about it. I'm sure you guys are under a lot of pressure with the massive amount of customers that have come today, and I don't want to add to that." #Meh, this is a bit sloppy
            c "I think you're right. I'm really sorry about the ice cream."
            Kl "Please, don't worry. It's still perfectly good ice cream. It was rude of me to say anything in the first place."
        else:
            Kl "This looks magnificent, [player_name]! How am I going to eat all of this?"
            c "I thought you could use a bit extra to help with all the paperwork."
            Kl "Maybe you're right."
    else:
        if evalCharacterMood == evalQualityServed:
            Kl "That's quite an impressive scoop!"
            c "I thought you could use a bit of extra ice cream to help you through the monotony of your paperwork."
            Kl "Oh boy could I ever."
            $ evalCustomerScore += 1
        else:
            Kl "Thank you, [player_name]! This looks really good. In hindsight I probably should have ordered more!"
            c "You still can if you wish."
            Kl "Thanks, but I think I'll pass. I've already held up the line, and Bryce is probably going to throw a fit if I don't get back to the office soon."
            c "Oh. I would go. I don't think that would be pretty."
            Kl "I've experienced it firsthand. It's not."
    
    c "Well, it was nice seeing you."
    Kl "You too. Maybe we'll meet again."

    hide kalinth with easeoutleft
    m "With that, she paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

#OHHHHH WE'RE HALFWAY THEREEEEE *AHHHH* *AHHH* THIS IS SO TE-DI-OUS!!!

label eval_help_kev:
    $ evalCharacterPreferredFlavor = "chocolate"
    show kevin normal with easeinright
    if not kevinunplayed: #Stuff to see if you've played kevin
        Kv "Fancy seeing you here, [player_name]!"
        c "Oh, hey again Kevin! Did you manage to find a place to stay?"
        Kv ramble "Yep. A friend of mine is letting me sleep on his couch."
        c "I'm sure you're giving him all the insider scoop on all this college stuff, aren't you?"
        Kv face "I see what you did there..."
        c "What?"
        Kv normal "Nevermind."
    else:
        Kv "Oh, didn't expect to find the infamous human working Katsuharu's stand today!"
        c "Surprise!"
    
    if evalCharacterMood == 0:
        Kv ramble "As much as I would love to ramble on, I've really got to get going soon."
        if not kevinunplayed:
            c "No problem. I think I've heard everything there is to dragon college already anyways."
            Kv normal "Probably."
            c "So, which flavor would you like?"
        else:
            c "No worries. What can I get you?"
    elif evalCharacterMood == 1:
        Kv "Today has been quite productive for me. You wouldn't believe the amount of flyers I've been able to give to these dragons waiting in line."
        if not kevinunplayed:
            c "I'm sure they were all very excited."
            Kv face "Some were... Less excited than others, to say the least."
            c "Sounds about right. Anyways, which flavor would you like??"
        else:
            c "Flyers?"
            Kv ramble "Yeah! I took up a summer job as a recruiter for Midwest Institution."
            c "Is that some kind of religious thing?"
            Kv "Not at all! It's a college"
            c "College. Wonderful times."
            Kv brow "Is that sarcasm?"
            c "Maybe. Anyways, what flavor would you like?"
    elif evalCharacterMood == 2:
        Kv "I've been running around like crazy giving dragons flyers, so I've really worked up an appetite."
        if not kevinunplayed: #HAHA I GOT TO COPY PASTE THIS LETS GO LAZINESS
            c "I'm sure they were all very excited."
            Kv face "Some were... Less excited than others, to say the least."
            c "I can relate. Anyways, which flavor would you like?"
        else:
            c "Flyers?"
            Kv ramble "Yeah! I took up a summer job as a recruiter for Midwest Institution."
            c "Is that some kind of religious thing?"
            Kv "Not at all! It's a college"
            c "College. Wonderful times."
            Kv brow "Is that sarcasm?"
            c "Maybe. Anyways, what flavor would you like?"
    Kv ramble "I'll take a scoop of chocolate, please."
    c "On it!"
    call eval_katsu_help_2 from eval_help_kev_2
    c "Here you go."

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Kv normal "Thanks for making it quick, I've really got to go."
            if not kevinunplayed:
                c "Go do me proud and give out those flyers."
                Kv face "I'll do it for you, [player_name], but only you"
                show kevin normal with dissolvemed
            else:
                c "Of course. Have a nice day!"
            $ evalCustomerScore += 1
        else:
            Kv normal "That took a little bit! I might be late if I don't go..."
            m "Kevin looked at his wrist where one would normally wear a watch."
            Kv face "Right now! I'm probably late! Thank you! Bye!"
            show kevin normal with dissolvemed
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Kv normal "Wow! This looks spectacular! You can really tell that Katsuharu cares about his craft."
            c "I'll make sure to put in a good word on your behalf."
            Kv "Please do!"
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Kv normal "That was fast, maybe even a little too fast."
            c "Is everything alright?"
            Kv face "Yes. I shouldn't have said anything at all. That was quite rude."
            Kv normal "Normally, Katsuharu spends a lot of time making his ice cream look perfect."
            Kv "But with the line, I can excuse the sloppiness."
            c "I could get you another if you wish."
            Kv "Please, don't worry about it. I don't want to hold up the line any longer. And it's not like presentation makes the actual ice cream any worse!"
        else:
            Kv normal "Wow, that's a lot of ice cream! I'm not even sure I can eat all of this!"
    else:
        if evalCharacterMood == evalQualityServed:
            Kv normal "Wow! That's a ton of ice cream. Thanks!"
            c "I thought you could use a bit extra after a busy day."
            Kv ramble "Boy could I ever."
            show kevin normal with dissolvemed
            $ evalCustomerScore += 1
        else:
            Kv normal "Thank you, this looks great! In hindsight, I should have ordered a bit more."
            Kv "Giving out flyers is hard work, y'know?"
            c "You could always order more now."
            Kv "I don't want to hold up the line and get anyone in line too angry. Those are potential college-goers!"
            m "A real one track mind it seems."
    
    hide kevin with easeoutleft
    m "With that, he paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_ley: #Ask for a tape measure for poking Adine
    $ evalCharacterPreferredFlavor = "mango"
    show leymas normal with easeinright
    Le "Hello again, human. Fancy seeing you behind the counter once more."
    c "I don't think I ever caught your name before."
    Le "Leymas. I work in the construction field around these parts."
    c "I'm [player_name]."
    Le "Well, [player_name]. Last time I was here I just got a couple waters."
    Le "This time, however, I'm here for the ice cream!"
    c "Luckily, we happen to serve that as well."
    if evalCharacterMood == 0:
        Le "Lucky me I guess."
        Le "Though, I should really be getting back on site soon. My crew is probably wondering where I am."
    elif evalCharacterMood == 1:
        Le "Lucky me!"
        Le "I haven't seen a congregation of dragons this big in quite a long time! It's been nice relaxing and talking with everyone!"
        c "Isn't Katsuharu always this busy?"
        Le "Never! Of course, he {i}is{/i} very popular, but today seems to be some sort of special occasion."
    elif evalCharacterMood == 2:
        Le "Perfect, standing in that long line really worked up my appetite."
        c "It's strange just how hungry standing in a line can make a person."
        Le "Right?"
    c "Anyways, which flavor would you like?"
    Le "I'm thinking that the mango sounds good right now."
    c "It matches your hard hat quite nicely."
    Le "Thanks?"
    call eval_katsu_help_2 from eval_help_ley_2
    c "Here's your mango ice cream!"

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Le "Nice and quick! Thanks, [player_name]!"
            c "Can't have your colleagues getting angry at you."
            Le "Thanks for looking out for me."
            $ evalCustomerScore += 1
        else:
            Le "Thank you. It looks wonderful, but I've really got to get going now."
            c "I understand. See you around hopefully."
            m "The dragon muttered something about his colleagues being unhappy." #Meh, might want to change this
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Le "Wow, this looks so good, I don't know if I even want to eat it!"
            c "Well, if you don't eat it, the sun will make quick work of it instead."
            Le "Good point."
            Le "Have a nice day, [player_name]!"
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Le "This looks delicious! Although I recall the ice cream looking more presentable in the past."
            c "Is it alright? I can always get you another."
            Le "Please, don't bother. It's still perfectly good ice cream, and I really shouldn't be holding up the line any longer."
        else:
            Le "That's quite the amount of mango ice cream you have there, [player_name]!"
            Le "How am I even supposed to eat all of that?"
            c "I thought you could use a bit extra. It's a little warm today."
            Le "I guess so. Thanks!"
    else:
        if evalCharacterMood == evalQualityServed:
            Le "That's a lot of mango ice cream, [player_name]!"
            c "You said you were hungry, so I added a bit extra."
            Le "Thanks a ton! I really needed some extra ice cream today!"
            $ evalCustomerScore += 1
    
    if evalCharacterMood == evalQualityServed and evalCurrentEnding == 4:
        m "Looking at Leymas' toolbelt, an idea struck me."
        c "Leymas, would you mind if I borrowed your tape measure?"
        Le "What for?"
        c "Measuring, of course."
        Le "That is very vague."
        c "I know, but if I explained what I wanted to do, it wouldn't make sense."
        Le "Well, I guess I'm not going to be using it today."
        Le "I'll agree if you promise you can return it by tomorrow."

        menu:
            "I promise.":
                c "Sure, I can do that."
                Le "Alright then, here you go."
                $ evalTapeMeasure = True
                play sound "fx/sys.wav"
                s "You got a tape measure! What could that be used for?"

            "Nevermind.":
                c "Nevermind, I think I might be too busy to return it to you."
                Le "Alright then."

    hide leymas with easeoutleft
    m "With that, Leymas paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_oph:
    #chap2storebread is false if you meet her earlier
    #Make her have actions instead of dialogue to signify how she feels
    $ evalCharacterPreferredFlavor = "mango"
    show ophinia normal with easeinright
    if not chap2storebread:
        Op "Oh hey. You again!"
        c "Hello."
        c "Just out of curiosity, what did you end up choosing in the store?"
        Op "You mean a few weeks ago?"
        Op "Nothing."
        c "What?"
        Op "Yes, I had Zhong pick it for me."
        c "Ah, I see."
    else:
        Op "Hey there!"
        c "Hello."
    c "So, what flavor can I get you?"
    Op "Flavor?"
    c "Yes. We have a few flavors you can choose from."
    Op "Ummmm..."
    m "The dragon glanced over the flavors."
    Op "Well, I have no idea what I want. What do you recommend?"
    if not chap2storebread:
        c "You know what? Maybe this should be a test."
        c "I won't give you any input. You have to decide on your own."
        Op "Oh, well..."
        m "Once again looking at the flavors, I could see her brows furl in concentration."
        Op "I think..."
        m "Her hand went up to her muzzle and the tip of her tongue escaped the side of her mouth."
        Op "I'll have..."
        m "Her face suddenly lit up and her facial features returned to normal."
        Op "The mango, please."
        c "Wow! I'm impressed. Why the mango?"
        Op "Like you said before, I just went with the one I thought I would like the most."
        c "I'm glad that my words of wisdom came in handy."
    else:
        c "Hmmm... I think a dragon like you would like the mango."
        Op "You're probably right. I do like fruits."
    
    if evalCharacterMood == 0:
        if not chap2storebread:
            Op "Thanks for helping me decide on my own. I've been waiting in that line so long my head isn't quite clear."
            m "Is her head ever clear with that box on top of it?"
        else:
            Op "Oh! Speaking of fruits, I have a couple with me that I would like to get home soon."
            c "Where?"
            Op "In the box, of course."
            m "How are there fruits in an upside down box?"
            m "I guess now isn't the time to ask questions."
    elif evalCharacterMood == 1:
        if not chap2storebread:
            Op "Thank you so much for helping me make my own decision. I can't wait to get an amazing looking scoop of ice cream!"
        else:
            Op "I can't wait to get an amazing looking scoop of mango!"
    elif evalCharacterMood == 2:
        if not chap2storebread:
            Op "All that intense decision making has left me starving!"
        else:
            Op "All of this waiting in line has left me starving!"
    
    c "Well, one scoop of mango ice cream coming right up!"
    call eval_katsu_help_2 from eval_help_oph_2
    c "Here's your ice cream!"

    #This is gonna be fun...
    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            if not chap2storebread:
                Op "Thanks for making it quick. I don't know how much longer I could stand before falling over!"
            else:
                Op "Thanks a ton! Now, I should really get going. I've got to put these fruits in the fridge!"
            $ evalCustomerScore += 1
        else:
            play sound "fx/impact3.ogg"
            hide ophinia with easeoutbottom
            m "As soon as I tried to give the dragon her ice cream, she toppled over."
            c "Are you alright?"
            show ophinia normal with easeinbottom
            Op "Perfectly fine! I've just been standing for too long, that's all!"
            m "She took the ice cream from my hand like nothing had happened."
            Op "Thanks for the ice cream!"
            if chap2storebread:
                m "How did her fruits not fall out of the box?"
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Op "Wow, this looks absolutely stunning! Thank you!"
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            if chap2storebread:
                Op "Maybe I made the wrong decision. This doesn't look as good as the other flavors any more."
                c "Looks can be deceiving."
                Op "You're right! Like this box on my head makes me look crazy, but in reality I'm perfectly sane!"
                m "I'm not so sure about that."
            else:
                Op "Hmm... This doesn't look as good as the other flavors any more."
                c "Would you like to change your order?"
                Op "No. No. How would I ever choose?"
        else:
            Op "That is a lot of ice cream. No way this will all fit in my stomach!"
    else:
        if evalCharacterMood == evalQualityServed:
            Op "That's a lot of ice cream! Thanks a ton!"
            $ evalCustomerScore += 1
        else:
            Op "That looks so good!"
            Op "I might just have to wait in line another time to get more!" #Do I actually have here come back? Hell yeah lol
            c "I could just give you a bit more now."
            Op "No, it's okay. I'll wait."
            $ evalOphSeconds = True
    
    hide ophinia with easeoutleft
    m "With that, she paid and left."

    $ evalServedCustomers += 1
    $ evalOphPosition = evalServedCustomers
    jump eval_katsu_help

label eval_help_luc:
    $ evalCharacterPreferredFlavor = "the special"
    show lucius normal with easeinright
    Lu "Hello again, human."
    c "It's [player_name]."
    Lu "Lucius."

    if not chap2park3unvisited:
        Lu "Hey, I apologize again for what happened at the park before."
        c "No worries. I almost forgot it even happened."
        Lu "Am I just that forgettable?"
        c "No, I just don't hold grudges."
    
    if evalCharacterMood == 0:
        Lu "I hate to rush you, but I have to be getting home. This line took way longer than I thought it would."
        c "No problem, I understand."
        Lu "I've had my eye on Katsuharu's newest flavor for a while. Could I get that?"
    elif evalCharacterMood == 1:
        Lu "Did you see those dragons over there?"
        m "He pointed to a few younger dragons on skateboards."
        Lu "They're pretty good, aren't they."
        c "Can't say I've really been watching. But they seem alright."
        Lu "Not as good as me, but they're pretty close. I had a great time watching them while I was in line."
        c "That's a good way to pass the time."
        Lu "Anyways, do you think I could try Katsuharu's new flavor?"
    elif evalCharacterMood == 2:
        Lu "I skated halfway across town for this ice cream, I'm starving!"
        c "You must really like it if you traveled that far."
        Lu "Well, I've actually been very interested in trying Katsuharu's new flavor."
    
    c "Newest flavor?"
    Lu "Yes. The 'special', as he calls it."
    c "What makes it so special?"
    Lu "No clue! He says it was inspired by the local diner, but that's all I know about it."
    if mp.fish:
        m "Oh no, I think I might know what the special is referring to."
    c "Well then, one special coming right up!"
    call eval_katsu_help_2 from eval_help_luc_2
    c "Here's your 'special' scoop of ice cream. I hope it's good!"
    
    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Lu "Thank you for making it quickly!"
            c "Happy to help. I hate being late myself."
            $ evalCustomerScore += 1
        else:
            Lu "Thank you! I've really, really got to go now."
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Lu "Wow, this looks awesome!"
            c "I had Katsuharu take special care in making your 'special' scoop."
            Lu "Very funny, [player_name]."
            c "Thank you! I pride myself in my humor."
            Lu "With jokes like that, I'd be worried."
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Lu "Thanks, but it looks a bit different from what I'm used to."
            c "Maybe because it's a 'special' flavor?"
            Lu "I don't think that's it. It just looks a bit... Off."
            c "Would you like another?"
            Lu "Don't worry about it. I shouldn't judge a book by it's cover."
        else:
            Lu "No way I'm going to be able to eat a scoop of ice cream that big in one sitting! Thanks, though!"
    else:
        if evalCharacterMood == evalQualityServed:
            Lu "Wow! I'm so glad I asked for a bit more. That looks perfect!"
            $ evalCustomerScore += 1
        else:
            Lu "I can't wait to try this new flavor! Although it already looks so good, I'm wondering if I should have ordered another."
            c "You still could."
            Lu "I shouldn't hold up the line any longer."
    
    m "The dragon then took a quick taste of the 'special'."
    if mp.fish:
        m "I was quite interested to see if something like that fish I had could possibly be good as ice cream."
    else:
        m "I was quite interested to see if the 'special' was any good."
    m "He flicked his tongue on the side of the scoop and smacked his lips a few times."
    Lu "Wow! This really is something special!"
    c "Is it good?"
    Lu "It's delicious, but I have no clue how to describe the flavor."
    c "Interesting."
    hide lucius with easeoutleft
    m "With that, he paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

label eval_help_xith:
    $ evalCharacterPreferredFlavor = "cherry"
    show xith normal with easeinright
    Xi "Oh, a human!"
    c "Oh, a dragon!"
    Xi "Deeply sorry. I'm sure that happens to you all the time."
    c "Don't worry about it, I was just making a lighthearted joke."

    if evalCharacterMood == 0:
        Xi "As much as I would love to continue pointing out your lack of being a dragon, I'm quite busy today."
        c "I understand. This line seems like it's much longer than it normally is."
    elif evalCharacterMood == 1:
        Xi "Well, we could continue this banter all day if you like. I set aside a lot of time to enjoy this ice cream."
        c "Let's not. For the sake of the people in line."
        Xi "You're just worried I have more jokes lined up than you do."
        c "Maybe."
    elif evalCharacterMood == 2:
        Xi "As much as I would love continuing this banter, I'm starving."
        c "Starving for more jokes?"
        Xi "No. I'd rather save room for ice cream."
    
    c "Alright then, what can I get you?"
    Xi "I usually have the vanilla, but I think I want to spice it up a little today. How about I get the cherry instead?"
    c "Sure thing!"
    call eval_katsu_help_2 from eval_help_xith_2
    c "Here's the cherry ice cream you asked for!"

    if evalCharacterMood == 0:
        if evalCharacterMood == evalQualityServed:
            Xi "Ah, thanks for making it quick."
            c "Of course. Can't let you be late."
            $ evalCustomerScore += 1
        else:
            Xi "Looks spectacular, but I've go to go to make it to my appointment on time."
    elif evalCharacterMood == 1:
        if evalCharacterMood == evalQualityServed:
            Xi "This is quite a stunning specimen of ice cream!"
            c "Thank Katsuharu. He gave this one a bit of extra love."
            Xi "I can tell."
            $ evalCustomerScore += 1
        elif evalQualityServed == 0:
            Xi "It looks good, but Katsuharu might be losing his touch."
            c "Is everything alright?"
            Xi "Oh yes. I just have a bad habit of judging foods at face value without trying them."
        else:
            Xi "Did you give me an ice cream scoop or an ice cream mountain?"
            c "I did add a bit extra to it."
            Xi "I can tell! No way my stomach can fit all of this!"
    else:
        if evalCharacterMood == evalQualityServed:
            Xi "That's not just an ice cream scoop. That's an ice cream mountain."
            Xi "I'm so hungry, too. Thanks!"
            $ evalCustomerScore += 1
        else:
            Xi "Damn, I should have requested more ice cream."
            c "You still could if you want."
            Xi "I think I'll have to pass. I should be cutting back on my sugar intake anyways."
    
    hide xith with easeoutleft
    m "With that, he paid and left."

    $ evalServedCustomers += 1
    jump eval_katsu_help

#I'M DONE!!!!!!!!!!!! YES!!!!!!!!!!!!