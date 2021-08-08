#It is very possible that I add an item tracker somewhere down the line. Sounds like a good idea to me

#This is where all of the orphanage stuff will take place to keep the main block of code from being *too* long
#Basic ideas:
    #Remy basically becomes your servant while you fix up an orphanage. Simple enough, right?
    #Don't make it as annoying as the ECK Anna paper writing game. I'm sorry, but that was not fun

    #The amount you can do at the orphanage is determined by the time you spend on certain activities. Each activity will have ~3 possible activites
    #Each task can be done at any time, and have a set solution
    #Some tasks have red herrings. There will be clues as to what are things you must do.
    #You need to send Remy off to do tasks to complete certain solutions to issues and must wait for him to return
    
    #How many total activities? Let's see how much more I can take of this random branching stuff. I already did SO much for the katsu game...

    #First order of business - Fix the lights. You have 3 options. Replace the bulbs, reset the circuit breaker, or fix the lightswitch
        #For the bulbs, you must send Remy off to the storage room to grab more bulbs
    #Then you need to fix the broken desk. You have options. Apply DWD-40 (Dragon Water Displacement-40), fix the legs of the desk

#Organized List of Items:
#    Supply Closet:
#        Lightbulbs - 1 action
#        Replacement Switch - 2 Actions
#        DWD-40 (Dragon Water Displacement-40) - 1 action
#    Shed:
#        Tools - 1 action
#        Small Spare Parts - 2 actions
#        Large Spare Parts - 3 actions
#        Ladder - 1 action
#    Main Office:
#        Children's folders - 1 action
#        Circuit Breaker - 2 actions
#        Cleaning Spray - 1 action
#
#All possible actions and outcomes:
#    Lights:
#        Replace bulbs - Requires lightbulbs and ladder. Progress + 1
#        Reset circuit breaker - Requires circuit breaker. Progress + 1
#        Replace light switch - Requires light switch. No progress
#    Desk:
#        Apply DWD-40 - Requires DWD-40. Progress + 1
#        Fix desk leg - Requires small spare parts and tools. Progress + 1
#        Fix desk seat - Requires large spare parts and tools. No progress
#    Organize books:
#        Pick up books - No requirements. Progress + 1
#        Fix crumpled pages - No requirements. Progress + 1
#        Sort books - No requirements. Progress + 1
#    Sort through papers:
#        Sort the hatchlings' drawings - Need children's files. Progress + 1
#        Go through paperwork - Need Remy present. Progress + 1
#        Fold newspaper - No requirements. Progress + 1
#    Do some cleaning:
#        Clean the walls - Requires cleaning spray. Progress + 1
#        Clean the desks - Requires cleaning spray. Progress + 1
#        Clean the whiteboard - Requires cleaning spray. Progress + 1

#Maybe use config.menu_include_disabled for this minigame. Just make sure to disable it again later

#Variables and display stuff - COUNT MINUTES BY 15!!!! - It's possible I want to make these more specific to the orphanage
#if I make another mod

#By the way self. The issue is that for everything excpet the lights, the completion condition has to come before the remy returning
#code since that is skipping the completion sequence. The reason it works for lights is because the completion sequence is located within the main game
label eval_orphanage_game_init:

    #Show ECK's extra info display
    show screen evalextrainfo
    $ evalextradisplay = 3

    jump eval_orphanage_game

#And... game time!
label eval_orphanage_game:
    #Complete the game if the player has done all 5 tasks
    if evalTasksComplete == 5:
        m "I took one last look around the room."
        m "It looks like we had finished just about everything we could."
        show remy normal with dissolvemed
        $ evalOrphanageScore = 2
        jump eval_orphanage_end
    
    #Complete the game if the player runs out of time
    if evalRemainingMinutes <= 0:
        $ evalDisplayVar1 = 0
        Ry "Adine should be here any minute, [player_name]."
        c "But we aren't done!"
        if evalTasksComplete > 3:
            Ry smile "We still did quite a lot in one day. Don't worry, Adine and I can finish the rest in the next few days."
            $ evalOrphanageScore = 1
        else:
            Ry look "Don't worry, Adine and I can finish the rest in the next few days."
            $ evalOrphanageScore = 0
        jump eval_orphanage_end
    
    #Update the display
    $ evalDisplayVar1name = "Remaining Time:"
    $ evalDisplayVar1 = evalRemainingMinutes
    $ evalDisplayVar1unit = " mins"

    if evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    else:
        $ evalDisplayVar2name = "Remy is here!"
        $ evalDisplayVar2 = ""
        $ evalDisplayVar2unit = ""

    $ evalDisplayVar3name = "Tasks Completed:"
    $ evalDisplayVar3 = evalTasksComplete
    $ evalDisplayVar3unit = ""

    #Show Remy when he returns and give the player their item
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        show amely smnormal with easeinright
        show remy normal behind amely with easeinright
        if evalRemyItem != "circuit breaker":
            Ry "We're back with the [evalRemyItem], [player_name]!"
            if evalLightsOnWithoutRemy: #Remy acknowledges that the lights have come back on if he was gone
                Ry "Oh hey! You got the lights working! Nice job, [player_name]!"
                Am "Lights!"
                $ evalLightsOnWithoutRemy = False
        else: #Handles special case where task isn't completed with an item
            Ry "We reset the circuit breaker, [player_name]!"
            $ evalResetBreaker = True
            $ evalRemyOnMission = False
            if evalReplaceBulbs and evalResetBreaker:
                $ evalTasksComplete += 1
                $ evalDisplayVar3 = evalTasksComplete
                play sound "fx/lightswitch.mp3"
                $ renpy.pause (1.5)
                scene evalorphlight
                if not evalRemyOnMission:
                    show remy normal
                    show amely smnormal
                else:
                    $ evalLightsOnWithoutRemy = True
                c "Let there be light!"
                if not evalRemyOnMission:
                    Ry smile "Nice job, [player_name]! Now we can see!"
                    Am "Light!"
        c "Thanks, Remy!"
        $ evalGatheredItems.append(evalRemyItem)
        $ evalRemyOnMission = False
    #Remy warning if he is idling
    elif evalMinutesRemyIsGone == 0: #This probably deserves a bit of variation
        Ry normal "Amely and I are here if you need anything, [player_name]."

    #What the player should ask in the menu
    if evalRemainingMinutes == 15:
        $ evalWhatNextText = "(What should we work on first?)"
    elif evalRemainingMinutes > 5:
        $ evalWhatNextText = "(What should we work on next?)"
    else:
        $ evalWhatNextText = "(We're running out of time. What should we work on next?)"
    
    #Deciding whether the player should ask Remy to fetch an item or work on a task
    menu:
        c "(What should I try to do?)"

        "Ask Remy to get something." if not evalRemyOnMission:
            jump eval_orphanage_remy_item_gather
        
        "Work on tasks.":
            pass

        "Wait.":
            if evalRemyOnMission:
                m "I should wait for Remy to get back."
            else:
                m "I should take a quick break."
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            jump eval_orphanage_game

    #Deciding which task to work on
    $ evalJumpFromMain = True
    menu:
        c "[evalWhatNextText]"
        
        "Fix the lights." if not evalReplaceBulbs or not evalResetBreaker:
            jump eval_orphanage_fix_lights
        
        "Fix the desk." if not evalApplyDWD or not evalFixLeg:
            jump eval_orphanage_fix_desk
        
        "Organize the books." if not evalPickUpBooks or not evalUncrumplePages or not evalSortBooks: #Add conditionals here
            jump eval_orphanage_organize_books
        
        "Sort through papers." if not evalHatchlingArt or not evalPaperwork or not evalFoldNewspaper: #Add conditionals here
            jump eval_orphanage_sort_papers
        
        "Do some cleaning." if not evalCleanWalls or not evalCleanDesks or not evalCleanWhiteboard: #Add conditionals here
            jump eval_orphanage_clean
        
        "[[Go back]":
            jump eval_orphanage_game

label eval_orphanage_remy_item_gather:
    c "Could you grab something for me, Remy?"
    Ry "Sure! Where from?"

    label eval_orphanage_reselect_gather_area:
        menu:
            "Supply Closet." if "lightbulbs" not in evalGatheredItems or "lightswitch" not in evalGatheredItems or "DWD-40" not in evalGatheredItems:

                menu:
                    "Lightbulbs." if "lightbulbs" not in evalGatheredItems:
                        $ evalRemyItem = "lightbulbs"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "I think we should get some lightbulbs to replace the broken lights."
                        Ry "Sounds like a good idea. Let's go, Amely!"
                        Am "Light!"
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                        Ry "Whoah! Wait for me, Amely!"
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright

                    "Replacement Lightswitch." if "lightswitch" not in evalGatheredItems:
                        $ evalRemyItem = "lightswitch"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "We should try replacing the lightswitch with a new one."
                        Ry "Good idea, [player_name]! I didn't think of that possibility."
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "DWD-40." if "DWD-40" not in evalGatheredItems:
                        $ evalRemyItem = "DWD-40"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "We should grab some WD-40. That stuff always comes in handy."
                        Ry look "Do you mean DWD-40?"
                        c "What does that even stand for?"
                        Ry normal "Dragon Water Displacement 40, obviously."
                        c "(I guess that's what the WD stands for.)"
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_orphanage_reselect_gather_area
                
                jump eval_orphanage_game

            "Shed." if "tools" not in evalGatheredItems or "small spare parts" not in evalGatheredItems or "large spare parts" not in evalGatheredItems or "ladder" not in evalGatheredItems:

                menu:
                    "Tools." if "tools" not in evalGatheredItems:
                        $ evalRemyItem = "tools"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Would you mind getting some tools? That sounds like it'll come in handy."
                        Ry "Sure thing! Come on Amely!"
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Small Spare Parts." if "small spare parts" not in evalGatheredItems:
                        $ evalRemyItem = "small spare parts"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "I think we should grab some small spare parts."
                        Ry "Good idea! We're on it, right Amely?"
                        Am "Yes!"
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                    
                    "Large Spare Parts." if "large spare parts" not in evalGatheredItems:
                        $ evalRemyItem = "large spare parts"
                        $ evalMinutesRemyIsGone = 45
                        $ evalRemyOnMission = True
                        c "We should probably get a few large parts to replace any odds or ends."
                        Ry "This might take a second, those parts are heavy!"
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Ladder." if "ladder" not in evalGatheredItems:
                        $ evalRemyItem = "ladder"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "I think a ladder would be beneficial."
                        Ry "One ladder coming right {i}up{/i}!"
                        c "I see what you did there..."
                        Ry smile "There's a lot more where that came from."
                        c "Oh no."
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_orphanage_reselect_gather_area
                
                jump eval_orphanage_game
            
            "Main Office." if "folders" not in evalGatheredItems or "circuit breaker" not in evalGatheredItems or "cleaning spray" not in evalGatheredItems:

                menu:
                    "Hatchlings' folders" if "folders" not in evalGatheredItems:
                        $ evalRemyItem = "folders"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Why don't we sort through the hatchlings' things?"
                        Ry "Sounds good to me, let me grab their folders for you."
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Circuit breaker." if "circuit breaker" not in evalGatheredItems:
                        $ evalRemyItem = "circuit breaker"
                        $ evalMinutesRemyIsGone = 30
                        $ evalRemyOnMission = True
                        c "Actually, instead of grabbing something, could you try resetting the circuit breaker?"
                        Ry "Good idea! I didn't think about that."
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "Cleaning spray." if "cleaning spray" not in evalGatheredItems:
                        $ evalRemyItem = "cleaning spray"
                        $ evalMinutesRemyIsGone = 15
                        $ evalRemyOnMission = True
                        c "Let's grab some cleaning spray so we can work on cleaning the walls."
                        Ry look "A lot of those scribbles have been there for years."
                        Ry normal "It'll be nice to finally clean them off."
                        show remy normal flip with dissolvemed
                        hide remy with easeoutright
                        show amely smnormal flip with dissolvemed
                        hide amely with easeoutright
                    
                    "[[Go Back]":
                        jump eval_orphanage_reselect_gather_area
                    
                jump eval_orphanage_game

            "[[Go back]":
                jump eval_orphanage_game
            
                                        
label eval_orphanage_fix_lights:
    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        if evalReplaceBulbs and evalResetBreaker:
            $ evalTasksComplete += 1
            $ evalDisplayVar3 = evalTasksComplete
            $ renpy.pause (1.5)
            play sound "fx/lightswitch.mp3"
            scene evalorphlight
            if not evalRemyOnMission:
                show remy normal
                show amely smnormal
            else:
                $ evalLightsOnWithoutRemy = True
            c "Let there be light!"
            if not evalRemyOnMission:
                Ry smile "Nice job, [player_name]! Now we can see!"
                Am "Light!"
        jump eval_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I walked over to the lightswitch."
        $ evalJumpFromMain = False
    else:
        m "I walked back over to the lightswitch."

    #Handle completion of the lights
    if evalReplaceBulbs and evalResetBreaker:
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        $ renpy.pause (1.5)
        play sound "fx/lightswitch.mp3"
        scene evalorphlight
        if not evalRemyOnMission:
            show remy normal
            show amely smnormal
        else:
            $ evalLightsOnWithoutRemy = True
        c "Let there be light!"
        if not evalRemyOnMission:
            Ry smile "Nice job, [player_name]! Now we can see!"
            Am "Light!"
        jump eval_orphanage_game

    play sound "fx/lightswitch.mp3"
    $ renpy.pause (1.0)
    m "The lights are busted, but the switch seems intact."
    
    menu:
        c "(What should I try fixing?)"

        "Replace the lightbulbs." if not evalReplaceBulbs:
            if "lightbulbs" in evalGatheredItems and "ladder" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalReplaceBulbs = True
                play sound "fx/lightscrewunscrew.mp3"
                m "One by one, I walked up to each bulb, placed down the ladder, and reinstalled the lightbulbs."
                $ renpy.pause (1.0)
                play sound "fx/lightswitch.mp3"
                jump eval_orphanage_fix_lights
            elif "lightbulbs" in evalGatheredItems and "ladder" not in evalGatheredItems:
                m "I need a ladder to reach the lights."
                jump eval_orphanage_game
            elif "lightbulbs" not in evalGatheredItems and "ladder" in evalGatheredItems:
                m "I can reach the lights, but I have nothing to replace them with."
                jump eval_orphanage_game
            else:
                m "I need some way to reach the lights and something to replace them with."
                jump eval_orphanage_game
        
        "Reset the circuit breaker." if not evalResetBreaker:
            m "It would be a good idea to reset the circuit breaker, but I have no idea where it is."
            m "Maybe Remy could do that for me."
            jump eval_orphanage_game
        
        "Replace the lightswitch." if not evalReplaceSwitch:
            if "lightswitch" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalReplaceSwitch = True
                play sound "fx/rummage.wav"
                m "I quickly replaced the lightswitch with the one Remy had given me."
                play sound "fx/lightswitch.mp3"
                m "Doesn't look like it did anything."
                jump eval_orphanage_fix_lights
            else:
                m "I need a new lightswitch if I'm going to replace the old one."
                jump eval_orphanage_game
        
        "[[Go Back]":
            jump eval_orphanage_game

label eval_orphanage_fix_desk:
    #Handle completion of the desk
    if evalApplyDWD and evalFixLeg:
        m "I sat back down at the desk Remy said was broken."
        m "It seemed perfectly fine now. It no longer made hideous squeaking noises and it didn't rock when I moved around."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        jump eval_orphanage_game
        if not evalRemyOnMission:
            Ry "Now I won't be tormented by those horrible squeaks. Nice going, [player_name]."
            c "Thanks!"
        jump eval_orphanage_game
    
    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    
    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I sat down at the desk Remy said was broken."
        $ evalJumpFromMain = False
    else:
        m "I sat back down at the desk Remy said was broken."

    #Handle hints as to what is wrong with the desk
    if not evalApplyDWD and not evalFixLeg:  
        play sound "fx/chairsqueak.mp3"
        $ renpy.pause (1.0)
        m "The desk rocked so violently that I almost fell off."
        m "It looked like one of the legs of the desk had been severely bent."
        c "(I feel bad for whoever's head hit that.)"
    elif not evalApplyDWD and evalFixLeg:
        play sound "fx/chairsqueak.mp3"
        $ renpy.pause (1.0)
        m "That sounds horrible."
    elif evalApplyDWD and not evalFixLeg:
        m "The desk rocked so violently that I almost fell off."
        m "It looked like one of the legs of the desk had been severely bent."
        c "(I feel bad for whoever's head hit that.)"
    
    #Handle player fix options
    menu:
        c "(What should I try fixing?)"

        "Apply lubricant." if not evalApplyDWD:
            if "DWD-40" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalApplyDWD = True
                play sound "fx/DWDspray.mp3"
                m "I gave the desk a quick coat of DWD-40."
                jump eval_orphanage_fix_desk
            else:
                m "I need some sort of lubricant to stop the squeaking."
                jump eval_orphanage_game
        
        "Fix the desk leg." if not evalFixLeg:
            if "small spare parts" in evalGatheredItems and "tools" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalFixLeg = True
                play sound "fx/screwin.mp3"
                m "I quickly replaced the bent desk leg with a new one."
                jump eval_orphanage_fix_desk
            elif "small spare parts" in evalGatheredItems and "tools" not in evalGatheredItems:
                m "I have the new desk leg, but I need tools to install it."
                jump eval_orphanage_game
            elif "small spare parts" not in evalGatheredItems and "tools" in evalGatheredItems:
                m "I have some tools, but I also need a replacement desk leg. I think it's pretty small as well."
                jump eval_orphanage_game
            else:
                m "I need tools and a replacement desk leg to fix this. The legs look quite small."
                jump eval_orphanage_game
        
        "Fix the desk seat." if not evalFixSeat:
            if "large spare parts" in evalGatheredItems and "tools" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalFixSeat = True
                play sound "fx/screwin.mp3"
                m "I replaced the desk seat with a new one."
                m "I'm not too sure that accomplished much."
                jump eval_orphanage_fix_desk
            elif "large spare parts" in evalGatheredItems and "tools" not in evalGatheredItems:
                m "I have a seat to replace the old one, but I also need tools to install it."
                jump eval_orphanage_game
            elif "large spare parts" not in evalGatheredItems and "tools" in evalGatheredItems:
                m "I have tools, but I need a replacement seat for the desk. I's quite a large piece."
                jump eval_orphanage_game
            else:
                m "I need tools and a replacement for the desk seat. The desk seat is decently large."
                jump eval_orphanage_game
        
        "[[Go Back]":
            jump eval_orphanage_game

label eval_orphanage_organize_books:
    #Handle completion of book organization
    if evalPickUpBooks and evalUncrumplePages and evalSortBooks: #yyy
        m "I walked a few steps back and admired my work."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        $ renpy.pause (2.0)
        m "Everything looked perfect. The books were neatly stacked on the shelves."
        if not evalRemyOnMission:
            Ry smile "You did a great job organizing those books, [player_name]!"
            if persistent.c1booksort:
                c "Well, I've already had plenty of practice in the library."
                Ry normal "I almost forgot about that!" #This is a bit ugly might want to change later
        jump eval_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"
    
    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I looked at the bookshelf at the back of the room." #Might want to dumb this down to maintain coherence when jumping back to this label
        $ evalJumpFromMain = False
    else:
        m "I walked a few steps back and admired my work."

    #Really fun if/elif/else chain to portray how the books look
    if not evalPickUpBooks and not evalUncrumplePages and not evalSortBooks: #nnn
        m "The books were strewn across the floor, their pages wrinkled."
    elif not evalPickUpBooks and not evalUncrumplePages and evalSortBooks: #nny
        m "The books were neatly sorted on the ground, their pages somewhat wrinkled."
    elif not evalPickUpBooks and evalUncrumplePages and evalSortBooks: #nyy
        m "The books were neatly sorted on the ground, with only faint wrinkles showing on their pages."
    elif evalPickUpBooks and not evalUncrumplePages and not evalSortBooks: #ynn
        m "The books rested on the shelves in no particular order and had wrinkled pages."
    elif evalPickUpBooks and evalUncrumplePages and not evalSortBooks: #yyn
        m "The books rested on the shelves in no particular order."
    elif evalPickUpBooks and not evalUncrumplePages and evalSortBooks: #yny
        m "The books were neatly sorted on the shelves. However, their pages still looked wrinkled."
    elif not evalPickUpBooks and evalUncrumplePages and not evalSortBooks: #nyn
        m "The books lay strewn across the floor, their pages freshly unwrinkled."
    
    menu:
        c "(What should I do with the books?)"

        "Pick up the books." if not evalPickUpBooks:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalPickUpBooks = True
            play sound "fx/rummage3.ogg"
            m "I picked up the books and rested them on the shelves."
            jump eval_orphanage_organize_books
        
        "Fix crumpled pages." if not evalUncrumplePages:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalUncrumpleProgress += 1
            if evalUncrumpleProgress == 2:
                m "I finished uncrumpling the pages of the last few books."
                $ evalUncrumplePages = True
            else:
                play sound "fx/paper2.ogg"
                m "I started removing the wrinkles from the books' pages."
                play sound "fx/paper2.ogg"
                m "This was going to take longer than I expected."
            jump eval_orphanage_organize_books
        
        "Sort the books." if not evalSortBooks:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalSortBooks = True
            play sound "fx/placebook.mp3"
            if persistent.c1booksort:
                if evalPickUpBooks:
                    m "Just like I had at the library, I organized the books on the shelf."
                else:
                    m "Just like I had at the library, I organized the books on the floor."
            else:
                if evalPickUpBooks:
                    m "I organized the books on the shelf in alphabetical order."
                else:
                    m "I organized the books on the floor in alphabetical order."
                c "(Not sure if this is how I should do it, but it should be fine.)"
            jump eval_orphanage_organize_books
        
        "[[Go Back]":
            jump eval_orphanage_game

label eval_orphanage_sort_papers:
    #Handle completion of paper sorting.
    if evalHatchlingArt and evalPaperwork and evalFoldNewspaper:
        m "I stood back and took a look at my work."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        m "All of the papers were properly sorted, and the hatchlings' artwork was safe in their respective folders."
        m "The newspaper was also folded and ready for another art project."
        if not evalRemyOnMission:
            $ evalAmelyPicture = False
            Ry smile "I can't remember the last time this desk ever looked this clean!"
            c "Oh, Remy. Look what I found!"
            m "I showed him Amely's drawing."
            m "Amely must have seen it as well."
            Am "Give Remy."
            Ry "A gift for me, Amely? Thanks!"
            m "Remy took the drawing and looked at it for a long time before slipping it under his wing."
            Ry "Wow, Amely, this looks really good!"
            Am "Thanks!"
            #Is it possible I actually draw something for this? Maybe :) Or ask the creator of the Remy Hatchlings mod
        jump eval_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I glanced at the papers on the large desk at the front of the room."
        $ evalJumpFromMain = False
    else:
        m "I stood back and took a look at my work."
    
    #Portraying how the papers look. Once again, this will not be fun
    if not evalHatchlingArt and not evalPaperwork and not evalFoldNewspaper:
        m "The desk was littered with papers of all sorts, ranging from important documents to crayon drawings."
        m "There was also newspaper crammed into one of the lower drawers. Probably for art projects."
    elif not evalHatchlingArt and not evalPaperwork and evalFoldNewspaper:
        m "The desk was covered in papers ranging from important documents to crayon drawings."
        m "However, the newspaper was folded neatly in the bottom drawer."
    elif not evalHatchlingArt and evalPaperwork and evalFoldNewspaper:
        m "I had managed to sort through all of the important documents and pile them neatly."
        m "The newspapers were also neatly folded in the desk drawer."
        m "However, the hatchlings' artwork still lay haphazardly on the table."
    elif evalHatchlingArt and not evalPaperwork and not evalFoldNewspaper:
        m "The artwork that had littered the table was now correctly sorted into the hatchlings' folders."
        m "However, the documents and newspaper still lay untouched."
    elif evalHatchlingArt and evalPaperwork and not evalFoldNewspaper:
        m "The papers on the top of the desk were completely organized."
        m "However, the newspaper in the lower drawer still lay crumpled."
    elif evalHatchlingArt and not evalPaperwork and evalFoldNewspaper:
        m "The hatchlings' artwork was properly sorted and the newspaper in the bottom drawer was folded nicely."
        m "However, I still had to go through the many important documents."
    elif not evalHatchlingArt and evalPaperwork and not evalFoldNewspaper:
        m "The important documents were neatly stacked and sorted on the desk."
        m "However, the hatchlings' artwork lay untouched, and the newspaper was still crammed tightly in a lower drawer."
    
    menu:
        c "(What should I do with the papers?)"

        "Sort the hatchlings' drawings." if not evalHatchlingArt:
            if "folders" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalHatchlingArt = True
                play sound "fx/pages.ogg"
                m "It was quite simple sorting through the hatchlings' art."
                m "Some of the art was also quite impressive."
                m "Wait, what's this? A drawing of Remy by Amely? I should keep this."
                $ evalAmelyPicture = True
                jump eval_orphanage_sort_papers
            else:
                m "I need something to organize this artwork in."
                m "Maybe there's some folders the hatchlings keep their art in?"
                jump eval_orphanage_game
        
        "Sort the important documents." if not evalPaperwork:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalPaperwork = True
            play sound "fx/pages.ogg"
            m "I sorted through the important documents at a reasonable pace."
            m "Not sure how exactly to organize them, I based my assumptions off of brief glances at the content."
            m "There's a surprising lack of adoption forms here. How sad."
            jump eval_orphanage_sort_papers
        
        "Fold the newspaper." if not evalFoldNewspaper:
            $ evalRemainingMinutes -= 15
            if evalRemyOnMission:
                $ evalMinutesRemyIsGone -= 15
            $ evalFoldNewspaper = True
            play sound "fx/pages.ogg"
            m "I quickly smoothed out the newspaper and folded it nicely."
            m "Once finished, the paper took up significantly less space in the drawer."
            jump eval_orphanage_sort_papers
        
        "[[Go Back]":
            jump eval_orphanage_game

label eval_orphanage_clean:
    #Handle completion of the room cleaning
    if evalCleanWalls and evalCleanDesks and evalCleanWhiteboard:
        m "I looked back at what I had just cleaned."
        $ evalTasksComplete += 1
        $ evalDisplayVar3 = evalTasksComplete
        m "Everything was spotless. The walls no longer bore the mark of the hatchlings and the desks shined."
        if not evalRemyOnMission:
            Ry "Wow, [player_name]! This looks wonderful!"
            c "How long do you think it'll stay like this?"
            Ry smile "Give the hatchlings a week. It'll be destroyed again by then."
        jump eval_orphanage_game

    #A bunch of code to increase continuity and kill bugs
    if evalRemyOnMission and evalMinutesRemyIsGone == 0:
        jump eval_orphanage_game
    elif evalMinutesRemyIsGone > 0:
        $ evalDisplayVar2name = "Remy returns in"
        $ evalDisplayVar2 = evalMinutesRemyIsGone
        $ evalDisplayVar2unit = " mins"

    $ evalDisplayVar1 = evalRemainingMinutes

    if evalJumpFromMain:
        m "I looked around the room."
        $ evalJumpFromMain = False
    else:
        m "I looked back at what I had just cleaned."
    
    #Handle how the room looks. WHY DO I DO THIS TO MYSELF
    if not evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The walls, desks, and whiteboard were a complete mess."
    elif not evalCleanWalls and not evalCleanDesks and evalCleanWhiteboard:
        m "The walls and desks still bore the scars of countless crayons and markers."
        m "The whiteboard, on the other hand, sparkled like new."
    elif not evalCleanWalls and evalCleanDesks and evalCleanWhiteboard:
        m "The desks and the whiteboard shone like new."
        m "The walls, however, were still covered in crayon."
    elif evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The room looked much nicer without the crayon scribbles on the wall."
        m "However, the desks and whiteboard were still dirty."
    elif evalCleanWalls and evalCleanDesks and not evalCleanWhiteboard:
        m "The walls and desk were devoid of crayon and marker scribbles."
        m "The whiteboard, on the other hand, still needed a good cleaning."
    elif evalCleanWalls and not evalCleanDesks and not evalCleanWhiteboard:
        m "The walls and whiteboard looked brand new."
        m "The desks, however, still bore the scars of a thousand markers."
    elif not evalCleanWalls and evalCleanDesks and not evalCleanWhiteboard:
        m "The desks looked like they were almost brand new."
        m "However, the whiteboard and walls were still a mess."
    
    menu:
        c "(What do I clean?)"

        "Clean the walls" if not evalCleanWalls:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanWalls = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped the crayon markings off the wall."
                jump eval_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to get these crayon markings off the wall."
                jump eval_orphanage_game
        
        "Clean the desks." if not evalCleanDesks:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanDesks = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped down the desks."
                m "The crayon and marker stains seemed to lift right off of the wood."
                jump eval_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to clean off these desks."
                jump eval_orphanage_game
        
        "Clean the whiteboard." if not evalCleanWhiteboard:
            if "cleaning spray" in evalGatheredItems:
                $ evalRemainingMinutes -= 15
                if evalRemyOnMission:
                    $ evalMinutesRemyIsGone -= 15
                $ evalCleanWhiteboard = True
                play sound "fx/spraybottle.mp3"
                m "Using the cleaning spray, I wiped the marker residue off of the whiteboard."
                jump eval_orphanage_clean
            else:
                m "I need some cleaning spray if I'm going to clean the whiteboard."
                jump eval_orphanage_game
        
        "[[Go Back]":
            jump eval_orphanage_game

label eval_orphanage_end: #Change the music
    hide screen evalextrainfo
    stop music fadeout 2.0
    $ renpy.pause (3.0)
    play music "mx/serene.ogg"
    if evalOrphanageScore == 2:
        Ry smile "Wow, [player_name]! This place hasn't look this good in years!"
        c "Couldn't have done it without you, Remy."
        Am smsad "Hey!"
        c "Sorry! Couldn't have done it without you either, Amely."
        Am smnormal "Yes. I help."
        Ry normal "Well. It looks like we still have a bit of time to kill."
        Ry "Is there anything else you would like to do?"
        c "That was exhausting, I think I'm too tired to do anything else."
        if evalRemainingMinutes > 30:
            Ry look "I forgot that you aren't as strong as you usually are."
            Ry normal "How about you and Amely take a nap together. She looks like she could use one as well."
            Am smsad "No!"
            m "Amely then let out a huge yawn."
            Am smnormal "Maybe..."
            c "Where should we sleep? On the floor?"
            Ry "You guys can sleep on me if you like."
            c "Oh boy, my very own full sized dragon pillow equipped with a built in heater!"
            Ry smile "I'm the latest model."
            m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
            m "Amely then crawled up next to me and laid her head on my shoulder."
            Am smnormal "Goodnight."
            m "In an instant, the little dragon was fast asleep."
            c "Wow! I wish I could do that."
            Ry normal "So do I."
            Ry "Go ahead and sleep. I'll wake you up before Adine gets here."
            c "Thanks, Remy."
            scene black with dissolveslow
            hide remy with dissolvemed
            m "I closed my eyes and snuggled closer to Remy."
            m "I wrapped one of my arms around Amely."
            m "Remy's soft breathing quickly lulled me to sleep."
            stop music fadeout 2.0
            $ renpy.pause (3.0)
            m "I was awoken when my dragon pillow suddenly started moving."
            scene evalorphlight with dissolveslow
            show amely smnormal with dissolvemed
            show remy normal behind amely with dissolvemed
            c "Hey! Pillows aren't supposed to move!"
            Ry smile "Would you rather miss out on ice cream?"
            c "I guess not..."
            Ry normal "I woke you up just before Adine's shift ends. She should be here any minute now..."
            jump eval_remy_amely_adine_1
        else:
            Ry look "I forgot that you aren't as strong as you usually are."
            Ry normal "How about you and Amely sit down and rest for a while. She looks exhausted as well."
            Am smsad "No!"
            m "Amely then let out a small yawn."
            Am smnormal "Maybe..."
            m "I made my way to take a seat at a desk."
            Ry "Wait, [player_name]. You can rest on me if you like."
            Ry smile "I'm probably much more comfortable than any old desk."
            c "Oh boy, my very own full sized dragon pillow equipped with a built in heater!"
            Ry "I'm the latest model."
            m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
            m "Amely then crawled up next to me and laid her head on my shoulder."
            Am smnormal "Goodnight."
            m "In an instant, the little dragon was fast asleep."
            c "Wow! I wish I could do that."
            Ry normal "So do I."
            c "Is she a deep sleeper?"
            Ry "Very. We can talk."
            m "For the next while, Remy and I engaged in lighthearted chatter, discussing our interests and the events that had gone on while I was in my coma."
            stop music fadeout 2.0
            jump eval_remy_amely_adine_1
    else:
        "Well, Adine should be here any minute now..."
        jump eval_remy_amely_adine_1
    
