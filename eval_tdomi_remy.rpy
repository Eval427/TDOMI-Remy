label eval_tdomi_remy:

    #So you're taking a peek at the code, eh? Well, enjoy all my comments, cause I'm not gonna delete anything

    #Current Issues:
        #Custom sounds and backgrounds arent working FIXED - NEVERMIND NOT FIXED - HAHA FIXED
        #I have no idea what to do for the orphanage <-- getting there, but I don't feel like tackling this quite yet
        #You can't pause or save during the mod? What? FIXED
        #Music stops when scrolling through previous text FIXED
        #Is it possible to change scenes without fading out characters? From what I've seen. Sorta.

    #TODO:
        #Add music - working on it!
        #Add skips
        #Add transitional pans to scenes
        #Adjust transitions to be smoother
        #Custom credits
        #Finish this lol
        #Reference an earlier node and change the dialogue so that Remy doesn't say he's spending more time w/ Adine? Idk, implies romance to me.

    #Plot issue of other kids in the orphanage:
        #After the incident at the portal, the children were put into emergency foster care outside of the town and still have not returned
        #Amely stayed because they couldn't find a place for her, but Remy and Adine agreed to take care of her
        #And... Implemented.
    
    #Things to remember to add to credits:
        #ECK for backgrounds and his amazing displays
        #AwBH Discord for feedback/motivation
        #Grissess for politely telling me I'm doing it all wrong and making me write better code

    #Future plans. MASSIVE SPOILERS: Welp, this is all out of date now. Not deleting it yet though
        #I need to write this down somewhere so I don't forget it. Please, if you're playing this and this content isn't released. I HIGHLY recommend
        #not reading this next wall of text. It'll ruin it, I promise.

        #After completing the game with a perfect score in both minigames, a good ending, and agreeing to meet with Xith,
        #a new ending unlocks for Remy's solo ending. In this ending, the player sees the ghost of vara manifest in front of
        #Remy. Player freaks out about it, Remy looks concerned, and the two of them plan to meet the next day and talk with Adine.
        #Tell Adine and Remy about the time travel element or Adine recalls her strange dreams and how they can relate to the past, present,
        #or future. If you have met with Xith before, you will have the option to talk with him as well. In exchange for giving him answers, he
        #will reveal that he has intereviewed a few other dragons, including Bryce, seb, and naomi if you have the mod, and maybe a few others
        #and they all have also experienced these visions. Go back home to find Remy waiting there. You talk with him, and he recalls seeing Vara
        #alive as well in a dream. He then thinks about his thoughts on alternate time lines, and asks you to promise that you
        #will save vara in the next timeline. You agree, and upon the next playthrough, Remy's ending is changed to where Vara survives, and this unlocks a FINAL
        #Ending with all 5 characters getting ice cream. Note this ending will not have the orphanage minigame since Adine will get paid leave to take care of Amely
        #and Vara. However, it will have the Katsu minigame with more bonus cutscenes and maybe extra characters thrown in for fun.
        #Also Vara isn't actually a ghost, but rather an appirition from another possible timeline where she survives OOOHHHH "An apparition from the present. a manifestation of another timeline in ours. Not a ghost, but a reality" <-- that's deep

        #Then... that's it. That's where this mod will end and I will finally be free.

    #Possible Acheivements:
        #Get Remy's solo good ending
        #Get Remy and Amely's good ending
        #Get the trio together
        #Get a perfect score in Katsuharu's minigame
        #Get the worst score in Katsuharu's minigame
        #Fix everything in the orphanage
        #Fix nothing in the orphanage
        #Get slapped by Adine twice
        #Become a pumpkin?
        #Try to give Amely 3 scoops of ice cream
        #Fail to get ice cream
        #It's like the pasta kiss, except with ice cream
        #Maximum meetups (get every extra cutscene with customers)

    stop music fadeout 2.0
    scene black with dissolveslow

    $ renpy.pause (1.0)

    nvl clear
    m "Wait a minute!" with Shake ((0, 0, 0, 0), 2, dist=10)
    $ renpy.pause (1.0)
    scene park2 with dissolvemed
    show remy look with dissolve
    $ renpy.pause (0.5)

    #Options for music: clouds, fountain, fun, funness. Also I need to somehow fix the sound when scrolling back. Don't know if that's a game bug or I'm doing something wrong
    Ry "What is it, [player_name]?"
    c "Before I go back, there is one very important matter that we must attend to."
    Ry sad "Please tell me this isn't anything too serious."
    Ry "I don't think I could take much more at the moment."
    c "There is a dragon..."
    c "And that dragon..."
    $ renpy.pause (2.0)
    play music "mx/jazzy.ogg"
    c "Owes me ice cream."
    Ry look "Ice cream?"
    Ry normal "Oh, you mean Katsuharu. I haven't had anything from him in quite some time."
    c "Well, I was offered as much ice cream as I could eat, and still need to take him up on his offer."
    Ry "Can I ask why exactly he agreed to give you so much ice cream?"
    Ry smile "I've seen your appetite, and it's quite impressive."

    menu:
        "Are you calling me fat?":
            $ evalAskIfFat = True
            c "Are you calling me fat?"
            Ry shy "N... No of course not, I didn't mean it that way... I just meant..."
            c "I'm kidding, don't sweat it."
            Ry normal "Dragons don't sweat."
            c "Noted."
            $ evalSweatJoke = True
        
        "Thanks...":
            c "Thanks..."
            $ evalAskIfFat = True #This basically means the same thing as the first option
            Ry shy "Hey! I didn't mean it that way!"
            c "Sure you didn't."

        "Hey, in my defense, that was some really good cooking.":
            c "Hey, in my defense, that was some really good cooking."
            Ry smile "Why thank you. I have been cooking for myself for a while, it's nice to know that my food still holds up strong with other people."
    
    show remy normal with dissolveslow
    c "Anyways, to make matters short, I gave him some advice about location, and it seemed to put him back on the radar."
    Ry "Where did you tell him to move?"
    c "Here. Tatsu Park."
    Ry look "I find it strange that he didn't think to move to Tatsu Park earlier."
    c "Considering his old spot worked well for forty years, it was probably pretty difficult to decide on a move." #Gonna want to change this a bit
    Ry normal "I guess you're right."
    Ry look 'Wait, are you sure your "all you can eat buffet pass" applies to your friends as well?'
    c "I'm sure it will be fine."
    Ry normal "If your pass extends beyond just yourself, is there anyone else you would like to invite?"

    menu:
        "We should go together.":
            c "Why don't we go with just the two of us? It'll be a nice outing, and maybe we won't eat Katsuharu entirely out of his stock."
            Ry smile "Sounds fun! Lets go."
            stop music fadeout 2.0
            scene black with dissolveslow
            hide remy with dissolvemed
            $ evalCurrentEnding = 1
            jump eval_solo_remy_1
        
        "We should bring Amely along with us.":
            c "Why don't we go together with Amely?"
            c "She's a hatchling, so I'm sure she would love to go and get some ice cream with us. Especially from the renowned Katsuharu."
            Ry smile "Good idea. You know, I'm not even sure if she has ever had ice cream before."
            Ry normal "Usually, the young dragons at the orphanage don't get the opportunity to go out and enjoy even the most basic things like ice cream."
            c "How come?"
            Ry look "The orphanage has been understaffed for quite a while now. I honestly have no clue how Adine has been able to manage all of that work with little to no help."
            Ry normal "She really is an amazing person, working minimum wage to barely support herself while still taking care of the orphans."
            
            menu:
                "I could probably do it.":
                    c "I could probably do it too."
                    Ry look "Hm... I don't really think you understand just how much that dragon struggles to balance her own life and those of the hatchlings she takes care of."
                "It is quite impressive":
                    c "It it quite impressive."
                    Ry "Yes. I couldn't agree more."
                "There's no way I could do anything close to what she does.":
                    c "There is no way that I have the patience or heart to do anything close to what she does."
                    Ry "Agreed. That is one crazy dedicated dragon."
            
            Ry normal "But anyways, the orphanage is on the other side of town. How about you wait here while I pick up Amely?"
            c "Are you sure you don't want me to come as well?"
            Ry smile "Unless you magically sprout wings, I think this is out best bet."
            c "You never know, I'm full of surprises."
            Ry normal "That is something that I cannot disagree with."
            c "Alright, I'll see you in a bit then."
            m "Remy nodded."
            hide remy with dissolvemed
            m "In one swift motion, he launched himself forward, extended his wings, and soared up into the sky."
            stop music fadeout 2.0
            play sound "fx/takeoff.ogg"
            c "(I wish I had the ability to fly anywhere I wanted.)"
            $ evalCurrentEnding = 2
            jump eval_remy_amely_1

        "Why don't we invite Amely and Adine?" if persistent.adinegoodending:
            c "Why don't we take Adine and Amely as well?"
            c "As a little hatchling, I'm sure that Amely would love to go and get some ice cream, and Adine has done so much for the both of us."
            Ry smile "It's been ages since I've had the opportunity to sit down and have a little get-together with everyone."
            Ry normal "Work, especially since Reza, has been particularly chaotic. It would be nice for the four of us to have a nice day out."
            if evalDoingSecretEnding:
                c "Couldn't agree more. I've been so busy in the last few months, I feel like I've missed out on so much."
            else:
                 "Couldn't agree more. Being in a coma for the last few months, I feel like I've missed out on so much."
            c "It would be nice to talk over some nice ice cream."
            Ry look "Hmmm... We may have to wait a little bit, Adine is probably busy on her shift delivering food."
            c "Good point..."
            Ry normal "You know, we could make ourselves useful at the orphanage until she is off her shift."
            Ry "She usually comes down to check on things as soon as she's done, and it may be a nice surprise for her to find us there."
            $ evalCurrentEnding = 3

            menu:
                "Sure.":
                    c "Sure. I've always been curious about the orphanage. I've heard a lot about it, but I haven't gotten the opportunity to visit."
                    Ry smile "Great! Let's go now."
                    jump eval_trip_to_orphanage

                "Sounds boring, lets do something else.":
                    c "That sounds like a pretty boring day out together. Let's do something else instead while we wait for Adine."
                    Ry look "I guess that does sound a bit boring. I still feel bad for the kids though. I'm sure they would have been excited to see us today."
                    c "I wouldn't worry. They're used to being alone, right?"
                    Ry "I suppose."
                    Ry normal "So, what were you thinking?"
                    c "How about a nice walk around the area?"
                    Ry look "You really think that walking is more interesting than taking care of children?"
                    c "It beats the yelling and screaming."
                    Ry angry "You know what? Taking a simple walk sounds like a pretty boring day out together. I think I'd rather go to the orphanage by myself."
                    hide remy with dissolvemed
                    stop music fadeout 2.0
                    play sound "fx/evalgrasswalk1"
                    m "The dragon stormed off and prepared to fly over to the orphanage."
                    
                    menu:
                        "Stop Remy.":
                            c "Wait! Remy!"
                            play sound "fx/evalgrasswalk2"
                            m "Remy looked at me and walked back over."
                            $ renpy.pause (1.0) #This should fix it? No? Fixed. I'm an idiot
                            show remy look with dissolvemed #Wtf is happening here?
                            Ry "What?"
                            play music "mx/jazzy.ogg"
                            c "I'm sorry, you're right. It was extremely selfish of me to prioritize my own enjoyment over that of yours and the childrens'."
                            Ry normal "I'm glad to hear that. I was worried for a second that you really were just that unkind."
                            c "No, I think I just overreacted. Human children can be a complete nightmare sometimes."
                            Ry "Well, so can dragon children, but you just learn to accept that they haven't had as much time on the planet as us, and sometimes have difficulty expressing their emotions in other ways."
                            c "I guess..."
                            Ry smile "Plus, I think this experience will be a lot more fun than you think."
                            c "You're probably right."
                            Ry normal "Great, we can start making our way over there now!"
                            jump eval_trip_to_orphanage
                        
                        "Let him leave.":
                            play sound "fx/takeoff.ogg"
                            m "I silently watched as Remy extended his wings and flew off to the orphanage."
                            "???" "You are an idiot"
                            c "What? Who are you?"
                            "???" "That doesn't matter. What does is how unbelievably selfish you are."
                            "!!!" "Yeah, idiot!"
                            c "What? There's two of you?"
                            "???" "Yeah, and what are you gonna do about it child hater?"
                            c "..."
                            "!!!" "That's what I thought!"
                            $ renpy.pause (0.5)
                            scene black with dissolveslow
                            c "At a loss for words, I made my way back home, crawled into bed, and did nothing for the rest of the day."
                            m "Nice one."
                            return

        "Everyone." if persistent.evalSecretEndingCompleted or evalDoingSecretEnding:
            c "Why don't we bring everyone?"
            Ry look "Everyone?"
            c "Yes. You, Amely, Vara, Adine, and I."
            c "After everything that has happened, we could all use a bit of ice cream."
            Ry normal "That sounds like a great idea, [player_name]!"
            Ry smile "I can't remember the last time I had an outing with this many people."
            Ry look "We may have to wait a bit, though. Adine is probably busy delivering food."
            c "Good point..."
            Ry normal "We could make ourselves useful at the orphanage until she's done."
            Ry "She usually comes to check on the orphanage as soon as she's finished, and it would be a nice surprise for her to find the place spotless."
            $ evalCurrentEnding = 4

            menu: #It's possible that I want to change this more so it's more uniquie, but I'm not sure
                "Sure.":
                    c "Sure. I'd love to help out if I could."
                    Ry smile "Great! Let's go now. Vara and Amely are already there, so they can keep us company as well."
                    jump eval_trip_to_orphanage
                
                "Sounds boring, lets do something else.":
                    c "That sounds like a pretty boring day out together. Let's do something else instead while we wait for Adine."
                    Ry look "I guess that does sound a bit boring. I still feel bad for the kids though. I'm sure they would have been excited to see us today."
                    c "I wouldn't worry. They're used to being alone, right?"
                    Ry "I suppose."
                    Ry normal "So, what were you thinking?"
                    c "How about a nice walk around the area?"
                    Ry look "You really think that walking is more interesting than taking care of children?"
                    c "It beats the yelling and screaming."
                    Ry angry "You know what? Taking a simple walk sounds like a pretty boring day out together. I think I'd rather go to the orphanage by myself."
                    hide remy with dissolvemed
                    stop music fadeout 2.0
                    play sound "fx/evalgrasswalk1"
                    m "The dragon stormed off and prepared to fly over to the orphanage."
                    
                    menu:
                        "Stop Remy.":
                            c "Wait! Remy!"
                            play sound "fx/evalgrasswalk2"
                            m "Remy looked at me and walked back over."
                            $ renpy.pause (1.0) #This should fix it? No? Fixed. I'm an idiot
                            show remy look with dissolvemed #Wtf is happening here?
                            Ry "What?"
                            play music "mx/jazzy.ogg"
                            c "I'm sorry, you're right. It was extremely selfish of me to prioritize my own enjoyment over that of yours and the childrens'."
                            Ry normal "I'm glad to hear that. I was worried for a second that you really were just that unkind."
                            c "No, I think I just overreacted. Human children can be a complete nightmare sometimes."
                            Ry "Well, so can dragon children, but you just learn to accept that they haven't had as much time on the planet as us, and sometimes have difficulty expressing their emotions in other ways."
                            c "I guess..."
                            Ry smile "Plus, I think this experience will be a lot more fun than you think."
                            c "You're probably right."
                            Ry normal "Great, we can start making our way over there now!"
                            jump eval_trip_to_orphanage
                        
                        "Let him leave.":
                            play sound "fx/takeoff.ogg"
                            m "I silently watched as Remy extended his wings and flew off to the orphanage."
                            "???" "You are an idiot"
                            c "What? Who are you?"
                            "???" "That doesn't matter. What does is how unbelievably selfish you are."
                            "!!!" "Yeah, idiot!"
                            c "What? There's two of you?"
                            "???" "Yeah, and what are you gonna do about it child hater?"
                            c "..."
                            "!!!" "That's what I thought!"
                            $ renpy.pause (0.5)
                            scene black with dissolveslow
                            c "At a loss for words, I made my way back home, crawled into bed, and did nothing for the rest of the day."
                            m "Nice one."
                            return

label eval_trip_to_orphanage:
    c "It's a bit far, is it not? The doctor said I shouldn't be walking too much."
    Ry normal "Well, you could always ride me instead of walking."
    if evalDoingSecretEnding and mp.remyromance:
        c "Maybe not in public, Remy."
    else:
        c "Ummmm..."
    Ry shy "No... Not like that. I mean ride on my back."
    if evalDoingSecretEnding and mp.remyromance:
        c "Damn."
    Ry normal "You're pretty small, and I'm used to carrying around a bunch of books."
    c "I'll take being associated with a bunch of books as a compliment."
    Ry normal "Please do."

    menu:
        "Accept his offer.":
            $ evalRodeRemy = True
            c "Sure, I'll make like a pile of books and hop on."
            hide remy with dissolvemed
            play sound "fx/bed.ogg" #Change Later
            m "Remy got down on all fours."
            m "Making sure not to mess up his tie, I carefully hopped onto his back. He folded his wings back to give me as much room as possible."
            Ry "Oof, maybe you're a bit heavier than the books I'm used to."
            c "Wait a minute..."
            Ry "Hey, books don't complain."
            m "After finding a relatively comfortable spot on his back, Remy lifted his body."
            Ry "How is it back there?"
            c "A bit uncomfortable. I think I need a saddle."
            Ry "Funnily enough, you can actually buy dragon saddles."
            c "That's... Interesting."
            Ry "They exist. I didn't say they were popular."
            stop music fadeout 2.0
            scene black with dissolveslow
            #stop music fadeout 2.0 <- Possibly stop the music here instead
            play sound "fx/steps/rough_gravel.wav"
            m "Remy then slowly started walking forward, picking up speed surprisingly quickly."
            if evalRodeBryce:
                m "It wasn't as uncomfortable as I had first imagined. In a way, it also felt strangely familiar, like I had done this before."
            else:
                m "It wasn't as uncomfortable as I had first imagined. It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "The experience was almost relaxing, with the light breeze and rhythmic thumping of Remy's feet on the grass and pavement."
            $ renpy.pause (0.5)
            m "We made our way through the city with a few dragons giving us strange looks."
            m "It seemed as if it took no time at all to arrive at the orphanage."
            Ry "Ladies and gentledragons, this will be our stop. Please make sure to grab all of your belongings and safely exit the vehicle."
            c "Very funny Remy."
            Ry "Thanks, I can tell that you sincerely mean that."
            play sound "fx/bed.ogg"
            m "I gracefully slid off Remy's back and looked around."
            scene hatchery with dissolveslow
            show remy look with dissolvemed
            Ry "Now, where did Adine leave the key this time?"
            show remy look flip with dissolvemed
            hide remy with easeoutright
            m "He walked over to a flower pot next to the door and tilted it to one side."
            play sound "fx/cling.ogg"
            m "A small, silver key fell out of the dirt and onto the concrete stairs."
            Ry normal "Yep. That's her usual hiding place."
            show remy normal with easeinright
            Ry "Alright, [player_name], follow me."
            hide remy with dissolvemed
            play sound "fx/door/doorchain.ogg"
            m "He placed the key in the lock and opened the door."
            play sound "fx/door/door_open.wav"
            $ renpy.pause (0.5)
            scene evalorphdark with dissolveslow
            play music "mx/donuts.mp3"
            show remy normal with dissolve
            Ry "Well, here we are!"
            if evalDoingSecretEnding:
                jump eval_secret_orphanage_arrival
            Ry "Amely? Are you here?"
            $ renpy.pause (1.0)
            show amely smnormal with easeinright
            Am "Hello!"
            Ry smile "Hello, Amely."
            Am "Dark!"
            Ry normal "I see that, Amely. I wonder who turned the lights off. Usually we leave them on for you."
            c "Wait, is the orphanage just a classroom?"
            Ry look "Sadly, this is most of the space that the orphans get. They play, learn, study, and eat in here or outside for most of the day."
            c "Where do they sleep?"
            Ry normal "Oh, we have some small bedrooms for them down the hall."
            Ry "At the moment the council has it completely closed off."
            c "Is that for any particular reason?"
            Ry "Not exactly. They probably don't want random dragons just waltzing in and taking the childrens' beds."
            c "That makes sense. So what exactly are we doing here today?"
            Ry "Let's take a look."
            hide remy with easeoutleft
            Am "I come!"
            hide amely with easeoutleft
            m "Remy walked over to the corner of the room and flicked the lights on."
            play sound "fx/lightswitch.mp3" #Increase the loudness of the audio
            $ renpy.pause (1.0)
            play sound "fx/lightbreak.mp3"
            $ renpy.pause (2.0)
            Am "Uh oh!"
            Ry look "Well, that's not good."
            play sound "fx/lightswitch.mp3"
            $ renpy.pause (2.0)
            play sound "fx/ligtswitch.mp3"
            $ renpy.pause (2.0)
            show remy normal flip with easeinleft
            show remy normal with dissolvemed
            show amely smnormal flip with easeinleft
            show amely smnormal with dissolvemed
            Ry "I think I know something that we're going to have to do."
            c "Fix the lights?"
            Ry smile "How'd you guess?"
            c "Not sure. Maybe I'm psychic."
            Ry "Well, if you're psychic, do you know what else is wrong here?"
            c "I think my powers only work once a day."
            Ry normal "Alright then. From what I can remember, that desk in the middle of the room is very broken."
            c "How'd that happen?"
            Ry look "Let's just say that we're lucky young dragon skulls are quite thick."
            c "Ouch."
            Ry normal "We should also try to go through the hatchlings' art and the paperwork left around."
            Ry "And finally, just clean up the place a little bit. These walls have seen one too many crayons in their time."
            m "I noticed a plethora of crayon scribbles on the wall that stopped at around Amely's height."
            Ry look "Not to mention that the books in here have seen better days."
            c "How should we do this?"
            Ry normal "Most of the supplies we have here are scattered around in a few locations near this building."
            Ry "So I think you should stay here while I grab things for you."
            Am "I help?"
            Ry smile "Sorry. Amely and I will grab you the supplies you need since we are very familiar with this place."
            Am "Yay!!!"
            c "Sounds like a plan. Let's do this!"
            show remy normal with dissolvemed
            jump eval_orphanage_game_init
            
        "Take a scenic walk to the orphanage.": #Add a skip here
            c "I think we should just walk and enjoy the scenery on our way there."
            Ry look "Are you sure, [player_name]? It's quite a long walk to the orphanage."
            c "Don't worry about me, I feel just fine."
            Ry normal "Sounds good to me."
            Ry "Just let me know if you get tired so we can take a break. Can't have you hurting yourself."
            c "Don't worry, I know how to pace myself."
            stop music fadeout 2.0
            scene black with dissolveslow
            hide remy with dissolvemed
            play sound "fx/steps/rough_gravel.wav"
            m "With that, we started walking."
            m "However, it seemed as if I had greatly overestimated my physical strength."
            m "We continued on at a good pace for about ten minutes. However, I quickly fell victim to exhaustion and found myself struggling to keep up with Remy."
            scene forest1 with dissolveslow
            show remy normal with dissolvemed
            play music "mx/serene.ogg" #Look into changing this
            Ry look "Hey, are you alright? You look winded."
            c "I think I'm alright. Just tired."
            c "I thought I could walk from one end of town to the other, but that coma really did a number on me."
            Ry "I can see that."
            Ry normal "Here, why don't we rest underneath that tree over there so you can regain your strength."
            scene black with dissolveslow
            hide remy with dissolvemed
            play sound "fx/evalgrasswalk1.ogg"
            m "The dragon made his way over to a peaceful little outcrop and laid down."
            m "He beckoned me to follow."
            play sound "fx/evalgrasswalk2.ogg"
            scene evalwildlands with dissolveslow
            if mp.remyromance: #This part may be stupid, contemplating deleting this
                $ evalRemyPillow = True
                m "I collapsed on the ground next to the dragon, my face and his muzzle just inches apart."
                play sound "fx/kiss.wav"
                m "Unprompted, I was given a quick kiss by Remy. He smiled, and then raised his head."
                show remy shy with dissolvemed
                $ renpy.pause (0.5)
                c "What a nice surprise."
                Ry normal "Here, you can use me as a pillow. I don't mind."
                c "Oh boy, my very own full sized dragon pillow equipped with a built in heater!"
                Ry smile "I'm the latest model."
                m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
                Ry normal "Why don't you take a quick nap? I'll keep a lookout for any unwanted visitors."
                c "Can't say no to that."
                scene black with dissolveslow
                hide remy with dissolvemed
                m "I closed my eyes and snuggled closer to Remy, his soft breathing quickly lulling me to sleep."
                stop music fadeout 2.0
            else:
                m "I collapsed on the ground next to the dragon. We looked at each other and smiled."
                show remy normal with dissolve
                c "Wow, this grass is quite comfortable."
                Ry "What? Is the grass back in the human world not like this?"
                c "Well, a lot of people used to have grass that felt like this, but after the collapse of our society, it was near impossible to find."
                Ry look "How come? It seems like a sustainable and easy way to raise livestock. This stuff takes virtually no water."
                c "In our world, grass is the complete opposite. It provides very little nutrients and needs a lot of water to survive."
                Ry normal "Interesting... I would think that since our worlds were so similar, a lot of our plant life would share similar characteristics. I have a few different ideas as to why this strange diversification would have occured. Firstly..."
                scene black with dissolveslow
                hide remy with dissolvemed
                c "A combination of Remy's very interesting speech on grass and the warm sun quickly lulled me to sleep."
                stop music fadeout 2.0
            
            $ renpy.pause (4.0)
            m "I felt a light tap on my shoulder. Slowly opening my eyes, I was met with Remy's face."
            scene evalwildlands2 with dissolveslow
            show remy smile with dissolvemed
            play music "mx/jazzy2.ogg"
            Ry "Hey there sleepy head. You slept for quite awhile."
            c "How long, exactly?"
            Ry normal "Well, you probably would have slept soundly for the next day or two, but I decided it was in our best interest if I were to wake you up before Adine's shift ends so we could meet her at the orphanage." #Try to break this up in the future
            c "Oh, did I really sleep for that long?"
            c "I guess we won't be able to help out today."
            Ry "It's alright, we can do it another time."
            Ry "Actually, all of the hatchlings aren't even there at the moment."
            c "Really? How come?"
            Ry "After the whole incident with Reza, they were put into emergency foster homes until everything cleared up."
            Ry"The council still hasn't given it the OK to let them back in the orphanage."
            c "What about Amely?"
            Ry look "Despite their best attempts, they couldn't find a place for Amely to stay. So Adine and I offered to take care of her instead."
            Ry "We both can't take her home because of our schedules, but young hatchlings are pretty self-sufficient."
            #Its possible I want to add more here, lets see
            Ry "Anyways, we should get going. We don't want to miss Adine."
            scene black with dissolveslow
            hide remy with dissolvemed
            play sound "fx/steps/rough_gravel.wav"
            m "With renewed energy, Remy and I continued to the orphanage."
            stop music fadeout 2.0
            scene hatchery with dissolveslow
            show remy look with dissolvemed
            Ry "Now, where did Adine leave the key this time?"
            show remy look flip with dissolvemed
            hide remy with easeoutright
            m "He walked over to a flower pot next to the door and tilted it to one side."
            play sound "fx/cling.ogg"
            m "A small, silver key fell out of the dirt and onto the concrete stairs."
            Ry "Yep. That's her usual hiding place."
            show remy normal with easeinright
            play sound "fx/door/doorchain.ogg"
            m "He placed the key in the lock and opened the door."
            play sound "fx/door/door_open.wav"
            $ renpy.pause (0.5)
            scene evalorphdark with dissolveslow
            play music "mx/donuts.mp3"
            show remy normal with dissolve
            if evalDoingSecretEnding: #Jumps over to the secret turn of events. Needs words, will work on later.
                jump eval_everyone_1
            Ry "Well, here we are! Amely? Are you here?"
            $ renpy.pause (1.0)
            show amely smnormal with easeinright
            Am "Hello!"
            Ry smile "Hello, Amely."
            Am "Dark!"
            Ry normal "I see that, Amely. I wonder who turned the lights off. Usually we leave them on for you."
            c "Wait, is the orphanage just a classroom?"
            Ry look "Sadly, this is most of the space that the orphans get. They play, learn, study, and eat in here or outside for most of the day."
            c "Where do they sleep?"
            Ry normal "Oh, we have some small bedrooms for them down the hall."
            Ry "At the moment the council has it completely closed off."
            c "Is that for any particular reason?"
            Ry "Not exactly. They probably don't want random dragons just waltzing in and taking the childrens' things or sleeping in their beds."
            c "I see."
            Ry "Here. Let's turn on the lights."
            hide remy with easeoutleft
            Am "I come!"
            hide amely with easeoutleft
            m "Remy walked over to the corner of the room and flicked the lights on."
            play sound "fx/lightswitch.mp3" #Increase the loudness of the audio
            $ renpy.pause (1.0)
            play sound "fx/lightbreak.mp3"
            $ renpy.pause (1.0)
            Am "Uh oh!"
            Ry look "Well, that's not good."
            play sound "fx/lightswitch.mp3"
            $ renpy.pause (2.0)
            play sound "fx/ligtswitch.mp3"
            $ renpy.pause (2.0)
            show remy normal flip with easeinleft
            show remy normal with dissolvemed
            show amely smnormal flip with easeinleft
            show amely smnormal with dissolvemed
            Ry look "I guess the lights in the building are out."
            c "It's a shame we couldn't help with that earlier."
            Ry normal "Hey, I'm just glad you're alright. You didn't look so hot back there."
            c "I guess now all there is to do is wait for Ad..."
            jump eval_remy_amely_adine_1

label eval_solo_remy_1: #Ending with only Remy
    $ evalCurrentEnding = 1
    $ renpy.pause (1.0)
    m "The two of us started wandering around the park. While at first we were worried we would have trouble finding Katsuharu, the massive line of dragons gave us a good indication on where he was located."
    scene town2 with dissolveslow
    show remy normal with dissolvemed
    play music "mx/cruising.ogg"
    Ry "Wow, this is quite an impressive line."
    c "It seems that my advice has paid off for him after all."
    Ry smile "Indeed."
    Ry normal "So, are you planning on waiting in line with everyone else?"

    menu:
        "It would be rude to skip everyone.":
            c "It would be rude to skip everyone."
            Ry "I would have to agree with you. All of these people have been waiting for a long time to get their ice cream, and I'm sure it would make them unhappy if we just skipped ahead."
            c "Looks like the line is about an hour long." #Do I add a mini game??? Tune in next time for //Is Eval Lazy?\\
            m "For the next hour, Remy and I engaged in lighthearted chatter, discussing our interests and the events that had gone on while I was in my coma."
            m "After what seemed like forever, it was finally our turn to get our ice cream."
        
        "I think we can skip the line.":
            c "I think that my unlimited ice cream pass also includes an express pass to the front of the line."
            Ry look "Are you sure? I'm not sure how well some of his customers will react to us cutting them in line."
            c "It'll be alright. I assume they won't complain too much about a human, and I'm sure that Katsuharu will be happy to serve us."
            m "As we passed down the line, we were met with a mix of expressions. Some of the people seemed quite intrigued by my appearance, while others seemed annoyed, probably understanding our intentions to skip the line."
            m "Approaching the stand, I caught the attention of Katsuharu. He waved and beckoned us to come."
        
    scene town7 with dissolveslow
    hide remy with dissolvemed
    show remy normal at right with dissolvemed
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Well, if it isn't the business saving human, [player_name]! Have you come to take up my offer?"

    menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while, hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it."
            c "Hopefully it should all return back to the peaceful way it was."
            c "Everything has more or less resolved itself and the conflict is over." #Ew ugly
            Ka smile flip "Glad to hear that."
            c "Is it alright that I brought Remy along as well?"
            Ka normal flip "Perfectly fine! Although he is going to have to pay for his ice cream."
            Ry look "Umm... [player_name]? I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'm happy to accomodate Remy as well."
            Ry normal "Why thank you Katsuharu. That's very generous of you."
            Ka normal flip "But enough chat-chat, we have to get to the more important matters."
            c "Like?"
            jump eval_ice_cream_choice
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right with dissolvemed
            Ka smile flip "*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka normal flip "I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry "I... guess I do remember being quite excited that day."
            c "Speaking of Remy, is it alright that I brought him along as well?"
            Ka normal flip "Perfectly fine! Although he is going to have to pay for his ice cream."
            Ry look "Umm... [player_name] I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'm happy to accomodate Remy as well."
            Ry normal "Why thank you Katsuharu, that's very generous of you."
            Ka normal "Well, enough about embarrassing childhood memories. Like you said, [player_name], we have to get to the more important matters."
            jump eval_ice_cream_choice

label eval_solo_remy_2:
    Ka normal flip "And how about you, Remy?"
    if evalChosenFlavor == "vanilla":
        Ry smile "I'll take a scoop of vanilla as well!"
    else:
        Ry normal "I'll just take a scoop of vanilla, nothing too special."

    menu:
        "Your ice cream preference matches you perfectly.":
            c "Your ice cream preference matches you perfectly."
            Ry look "How so?"
            c "Well... white dragon, white ice cream. It all kind of works."
            show katsu exhausted flip with dissolvemed

            if persistent.adinegoodending:
                Ry "*sigh* First with Adine, now with me."
                c "Yep. You can't escape it."
            else:
                Ry "*sigh* I guess you could think about it like that."
        
        "Good choice.":
            c "Good choice."
            Ry normal "Thanks! In my opinion, vanilla is the tried and true classic. You can't go wrong with it."
            
    show remy normal with dissolvemed
    Ka normal flip "Alright, just give me a second to get you your scoops!"
    show katsu normal with dissolvemed #Make him turn around before leaving
    hide katsu with easeoutleft
    m "The dragon walked behind his stand and started preparing the ice cream."
    m "Expecting the dragon to produce some sort of utensil, I was surprised when he suddenly thrust his hand into the vat and pulled out an almost perfectly spherical scoop of ice cream."
    c "(Damn, these dragons can fly, shoot fire, run extremely fast, and even make an amazing scoop of ice cream with their bare hands. This truly is the peak of evolution.)"
    Ka "Y'know, most ice cream vendors use some sort of scoop. But over the years, you learn that your bare hands are faster and more efficient than any of those stupid tools." #Might be a bit pointless to have this
    c "Don't you walk using your hands, Katsuharu?" #Hands, claws, feet, I'm very confused at this point
    Ry look "You know, I never really thought of that."
    Ka "Well, I wash my hands before serving the ice cream of course! I have a little station back here and everything."
    c "(Whew)"
    show remy normal with dissolvemed
    m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top, lightly pushing it down to make sure it didn't fall out."
    c "Interesting, those cones look exactly like the ones back in my world."
    show katsu excited flip at Position (xpos = 0.1) with easeinleft
    Ka "But I am sure that they don't taste half as good as mine!"
    m "Katsuharu then handed me the cone, topped with the [evalChosenFlavor] ice cream."
    show katsu smile flip with dissolvemed
    
    if evalChosenFlavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color." #Kinda bad, should change
    elif evalChosenFlavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif evalChosenFlavor == "strawberry":
        m "The strawberry ice cream looked different from what I was used to back in my world. Instead of a dark red, the scoop was tinted pinkish green, with small specks of what I assumed to be strawberry dotted within it."
    elif evalChosenFlavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif evalChosenFlavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif evalChosenFlavor == "special":
        m "The special was a disgusting mix of all the colors you don't want in your ice cream. It had a rather odd, dark gray color with pink dots speckled inside it, which I presumed was the fish."
    
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "I watched as Katsuharu went back to his stand and repeated the process for Remy's cone."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Here you are Remy."
    Ry smile "It's been so long since I've had ice cream."
    Ka "Well, as promised, this one is on the house."
    c "Thank you Katsuharu."
    Ka smile flip "I should be thanking you. You are the one that saved my business after all."
    c "This ice cream is more than enough to show your gratitude."
    Ka normal flip "Go ahead and stop by anytime you wish. I'll always have plenty of ice cream."
    c "Free of charge?"
    Ka exhausted flip "Well... We'll see. Can't have my business going downhill for a second time."
    c "Come on, we don't eat THAT much ice cream."
    Ka smile flip "Listen, I'm just taking precautions here."
    Ka normal flip "Anyways, I should probably get back to my stand before the people in line start getting too angry."
    Ry "Of course. Thank you Katsuharu."
    Ka "Any time."
    show katsu normal with dissolvemed #Why does katsu do a 360 flip here? Am I just seeing things?
    $ renpy.pause (0.2)
    hide katsu with easeoutleft
    hide remy with dissolvemed
    show remy normal with dissolvemed
    m "Remy and I sat there, cones in hand."
    c "Do you want to take a slow walk for a little while?"
    Ry "As much as I would love to, it's a bit difficult as a quadruped like myself to hold ice cream and walk."
    m "I looked down to see Remy carefully walking on three legs while balancing the cone in his fourth."
    c "Of course, let's find a good place to rest."
    Ry "That area looks nice and peaceful."
    stop music fadeout 2.0
    scene black with dissolveslow
    hide remy with dissolvemed
    m "We made our way over to where Remy was looking and sat down side by side" #A little choppy, should fix this
    scene evalpark1 with dissolveslow
    play music "mx/campfire.ogg"
    show remy normal with dissolvemed
    Ry "We should make a toast."
    c "But we don't have any drinks."
    Ry "I guess our cones will have to suffice."
    c "You were the one who came up with the idea, so you go first."
    Ry smile "Alright then... To our health, both physically and mentally. Both of us have had a rough time in the past, but we have both stayed strong and supported each other."
    if evalChosenFlavor == "vanilla":
        m "The two of us tapped our cones together, our scoops gently rubbing against each other."
        Ry look "Damn, our perfectly spherical scoops!"
    else:
        m "The two of us awkwardly tapped our cones together, careful as to not cross contaminate our different flavors."
    Ry normal "Seriously, though. I have so much to thank you for. Without you, I'm not sure I would be standing here at all today."
    c "Of course, Remy, I'll always be there for you, even when I inevitably have to leave through the portal."
    Ry look "Yeah. I've been thinking about that recently. I really don't know what I am going to do once you leave."
    c "Remember, I'm not leaving. I'm just going back to the day I got here."
    Ry sad "Still, I can't shake off the felling that I won't ever see you again."
    c "What do you mean?"
    Ry "I know I said that I would see you again after you went through the portal, but in a way, I feel like when you enter that portal, you don't go back to my world, but a world exactly like mine with a dragon exactly like me."
    c "I see."
    Ry normal "But in the foreseeable future, you aren't going anywhere, and I am going to appreciate the time that we have together."
    c "So will I."
    Ry "It's your turn now, what do we toast to?"

    menu:
        "To our friendship.":
            c "To our friendship. Ever since I first arrived here, you have always been by my side, and I can say that you are the best friend that I have ever had."
            Ry smile "Wow, do you really mean that?"
            c "Of course, you have helped me more than you could possibly understand."
            Ry normal "I didn't think that I could possibly be much help in any situation, but I can promise that I will always be there for you."
            c "Thank you, Remy."
        "To our love." if mp.remyromance:
            c "To our love. You are the most gorgeous and kindhearted dragon I have ever met."
            Ry shy "That definitely isn't what I expected to hear, but thank you. I can also confirm that you are the most beautiful human that I have ever met."
            c "Not like I'm working with any real competition..."
            Ry normal "Hey, technically there were three humans here. I just sincerely mean what I said."
            c "Thanks, Remy."
        "To this world.":
            c "To this world. You all accepted me with open arms and have shown me just how truly beautiful your civilization is."
            Ry "I'm glad you think of us that way. Of course, you haven't seen the shadier parts, but I would like to think that most of our civilization is like this."
            c "Any civilization is bound to have flaws, I just respect the way that the dragons handle conflict."
            Ry "Is it much different than your own world?"
            c "Here, decisions seem to be made mostly out of interest for the people. Of course, there are some exceptions like Emera, but a lot of diplomatic decisions on the human world are made solely for personal benefit."
            Ry look "That's too bad. We have that here, but most decisions made have the peoples' interests in mind."
            c "You get used to it, I guess."
    
    show remy normal with dissolvemed
    m "This time, we didn't tap our cones together for fear of further ruining our scoops."
    Ry "We should probably start eating our ice cream before it all melts, don't you think?"
    m "I looked down, spotting trickles of the [evalChosenFlavor] ice cream running down the cone and pooling on my hand."
    if evalChosenFlavor == "special":
        m "Somehow, it looked even more disgusting than before."
    c "Good idea."
    if evalChosenFlavor == "special":
        show remy smile with dissolvemed
        m "At the same time, Remy and I took a bite of our ice cream. Instantly, Remy's face lit up in excitement, and mine contorted into disgust."
        if mp.fish:
            c "Wow, this is just as disgusting as I remember it being."
        else:
            c "Wow, this is disgusting."
        Ry look "Are you not a big fan of the special?"
        c "Not to offend anyone, but it's pretty gross."
        Ry normal "It isn't for everyone, , it is for me. Would you like to switch?"

        menu:
            "Sure.":
                c "I mean, if you're okay with it."
                Ry smile "If you're happy, I'm happy."
                show remy normal with dissolvemed
                m "We quickly switched cones, and after a taste of the vanilla, I could see why Katsuharu was so well loved for his craft."
                m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."
                $ evalSwitchedCones = True
            
            "Don't worry about it.":
                c "Don't worry about it. I think I just overreacted. It's not that bad."
                Ry look "Alright then."
                show remy normal with dissolvemed
                m "Remy's cone did not last long. Soon, the only remnants of his ice cream lay in his stomach or dried on his hand."
                m "I on the other hand did not finish quite as quickly. The flavor did glow on me over time, but it was something I definitely did not want to try again."
    else:
        show remy smile with dissolvemed
        m "At the same time, Remy and I took a bite of our ice cream. Instantly, both of us lit up in excitement."
        c "Wow, this really is amazing ice cream!"
        Ry "I forgot just how good Katsuharu is at making this stuff. This is spectacular!"
        m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."
    
    scene evalpark2 with dissolveslow #Ugly transition. How do I change scene w/o hiding Remy?
    show remy normal with dissolvemed
    Ry smile "I would call this outing a complete success!"
    c "Agreed."
    Ry normal "It's getting a bit late, would you like me to walk you back to your place?"
    c "Sure!"
    stop music fadeout 2.0
    scene black with dissolveslow
    hide remy with dissolvemed
    play sound "fx/steps/rough_gravel.wav"
    m "It didn't take us long to make our way back."
    scene evalplayerapt1 with dissolveslow
    show remy normal with dissolvemed
    play music "mx/amb/night.ogg"
    Ry "Here we are, just like the night you first came here."

    menu:
        "Kiss him." if mp.remyromance:
            c "Sure. But on the first night would I do this?"
            play sound "fx/kiss.wav"
            m "I pulled Remy's muzzle to my lips and gave him a big kiss."
            Ry shy "I don't think you would then, but I'm glad you would now."

            if evalSwitchedCones:
                Ry "Your breath smells like vanilla."
                c "And yours of fish. I think I got the shorter end of the stick."
                Ry "I guess fish ice cream and kissing don't mix well together."
            elif evalChosenFlavor == "special":
                c "Your breath smells like vanilla."
                Ry "And yours of fish. I think I got the shorter end of the stick."
                c "Yeah, I guess fish ice cream isn't the best for kissing."
            else:
                c "Your breath smells like vanilla."
                Ry "And yours of [evalChosenFlavor]. Really adds to the kiss if you ask me."

            Ry shy "Hey... Uh, it's quite late, and my house is a bit far away, would you mind if I stayed at your place for the night?"
            c "Of course, the couch is always available."
            Ry "Well... I was thinking more along the lines of sharing the bed together."

            menu:
                "Sure.":
                    c "Well, Remy, sounds like a good time to me."
                    Ry normal "We'll see where things go, [player_name]." #Do I add more to this? Maybe I will in the final ending...
                    scene black with dissolveslow
                    stop music fadeout 2.0
                    $ renpy.pause (4.0)
                    play sound "mx/eveningmelody.ogg"
                    $ persistent.evalSoloRemyEnding = True
                    return
                
                "Sorry, but no.":
                    c "Sorry, but the bed is cramped enough for me as it is."
                    Ry sad "Oh, I understand, I guess the couch will be big enough for me."
                    scene black with dissolveslow
                    stop music fadeout 2.0
                    $ renpy.pause (4.0)
                    play sound "mx/eveningmelody.ogg"
                    m "But why? Why would you choose this in the first place?"
                    return

        "Good memories.":
            c "Those were the times, before everything devolved into madness and chaos."
            Ry "As weird as it sounds, I am almost happy that everything happened. I think that the experienced I shared with you really helped me accept and move on with my past."
            c "I could say the same. A lot of what went on in the past few weeks has really shown me a perspective of humanity that I didn't really care to think about."
            Ry "I best get going. I have to get up early for work tomorrow and night flying isn't really my specialty."
            c "Of course, bye Remy!"
            Ry smile "Bye [player_name]!"
            hide remy with dissolvemed
            play sound "fx/takeoff.ogg"
            $ renpy.pause (0.5)
            scene black with dissolveslow
            stop music fadeout 2.0
            play sound "mx/eveningmelody.ogg"
            $ persistent.evalSoloRemyEnding = True
            return
    
    #And... scene!

label eval_remy_amely_1:
    m "I decided to sit on a nearby park bench while I waited for Remy to return with Amely."
    m "Glancing around the area, I saw what looked like the end of a long line of dragons, assumingly for Katsuharu's ice cream."
    c "Oh boy, I hope that line doesn't take too long."
    $ renpy.pause (2.0)
    m "Looking to my left, I saw that a dragon had been silently sitting on the bench with me."
    $ persistent.seendramavian = True
    show dramavian normal with dissolvemed

    if chap2rested > 0:
        c "Oh, hey again."
        Dr "..."
        c "Do you always sit here?"
        Dr "..."
        m "This was the first time that I noticed that all this dragon audibly said was the word 'dot' three times."
        c "Why do you only say 'dot dot dot'"
        Dr "dot dot dot"
        c "Um..."
        Dr "Goodbye..."
        hide dramavian with dissolvemed
        c "That was an interesting experience..."
        m "I found myself saying the dots out loud as well now."
    else:
        c "Whoah, I didn't see you there. I thought you were a statue or something."
        Dr "..."
        c "Hello?"
        Dr "..."
        c "(Well, maybe it {i}is{/i} a statue. Or I just turned invisible.)"
        c "(I hope it's not the latter.)"
        hide dramavian with dissolvemed
    
    $ renpy.pause (1.0)

    m "All of a sudden, a shadow passed overhead, and Remy landed next to me, clutching onto Amely with his forelegs." #Forelegs? Forearms? Who knows...
    #Add sound here?
    play music "mx/fun.ogg"
    show amely smnormal with dissolvemed
    show remy normal behind amely with dissolvemed
    Ry "Alright Amely, this is our stop."
    Am "Yay!"
    c "So, Amely, are you excited to have your first ever scoop of ice cream?"
    Am smsad "Ice... cream?"
    c "It's like... Well... Um..."
    m "I didn't think it would be so difficult to describe something as simple as ice cream."
    Am smnormal "Sugar?"
    c "Yes, lots of sugar."
    Am "Sugar!!!"
    Ry smile "I'm going to take that as a yes."
    c "I was just thinking, what is Adine going to think when she goes to the orphanage and sees Amely missing?"
    Ry normal "Don't worry, I left her a note saying that we were taking her out to get ice cream."
    c "Ok good. I didn't want to see a panicked Adine flying all across town looking for Amely."
    Ry "I wouldn't hear the end of it if that happened."
    c "We should probably get some ice cream before it gets too late or Amely gets too antsy."
    Am "Sugar!!!"
    Ry "Good idea."
    scene black with dissolveslow
    hide remy with dissolvemed
    hide amely with dissolvemed
    m "It didn't take us long to reach the end of the line."
    scene town2 with dissolveslow
    show amely smnormal with dissolvemed
    show remy normal behind amely with dissolvemed
    Ry "Wow, this is quite an impressive line."
    c "It seems that my advice has paid off for him after all."
    Ry smile "Indeed."
    Ry normal "Wait, are we planning on waiting in line with everyone else? It seems like that might take a while."

    menu:
        "It would be rude to skip everyone.":
            $ evalAmelyAnnoysLine = True
            c "It would be rude to skip everyone."
            Ry "I would have to agree with you. All of these people have been waiting for a long time to get their ice cream, and I'm sure it would make them unhappy if we just skipped ahead."
            c "Looks like the line is about an hour long." #Do I add a mini game??? Tune in next time for //Is Eval Lazy?\\
            hide amely with easeoutleft
            m "For the next hour, Remy and I engaged in lighthearted chatter, discussing our interests and the events that had gone on while I was in my coma."
            m "Amely, on the other hand, spent her time pestering just about every dragon in the line ahead of us. She even managed to get some of them to leave, speeding up the line quite dramatically."
            m "After what seemed like forever, it was just about our turn to get our ice cream."
            Ry "Amely! Ice cream!"
            show amely smnormal at right with dissolvemed
            Am "Sugar!!!"
        
        "I think we can skip the line.":
            c "I think that my unlimited ice cream pass also includes an express pass to the front of the line."
            Ry look "Are you sure? I'm not sure how well some of his customers will react to us cutting them off."
            c "It'll be alright. I assume they won't complain too much about a human, and I'm sure that Katsuharu will be happy to serve us."
            m "As we passed down the line, we were met with a mix of expressions. Some of the dragons seemed quite intrigued by my appearance, while others seemed annoyed, probably understanding our intentions to skip the line."
            m "Approaching the stand, I caught the attention of Katsuharu. He waved and beckoned us to come."
    
    scene town7 with dissolveslow
    show amely smnormal at right with dissolvemed
    show remy normal at right behind amely with dissolvemed
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Well, if it isn't the business saving human, [player_name]! Have you come to take up my offer?"

    menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while, hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it."
            c "Hopefully it should all return back to the peaceful way it was."
            c "Everything has more or less resolved itself and the conflict is over."
            Ka smile flip "Glad to hear that."
            c "Is it alright that I brought Remy and Amely along as well?"
            Ka normal flip "Perfectly fine! Although Remy is going to have to pay for the both of them."
            Ry look "Umm... [player_name]? I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'd be happy to accomodate the two of you as well."
            Ry normal "Why thank you Katsuharu, that's very generous of you."
            Ka "But enough chit-chat, we have to get to the more important matters."
            c "Like?"
            jump eval_ice_cream_choice
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right with dissolvemed
            Ka smile flip"*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka normal flip"I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry "I... guess I do remember being quite excited that day."
            c "Speaking of Remy, is it alright that I brought him along as well?"
            Ka normal flip "Perfectly fine! Although he is going to have to pay."
            Ry look "Umm... [player_name] I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'd be happy to accomodate Remy as well."
            Ry normal "Why thank you Katsuharu, that's very generous of you."
            Ka normal "Well, enough about embarrassing childhood memories, like you said, [player_name], we have to get to the more important matters."
            jump eval_ice_cream_choice

label eval_remy_amely_2:
    Ka normal flip "How about you, Remy?"
    if evalChosenFlavor == "vanilla":
        Ry smile "I'll take a scoop of vanilla as well!"
    else:
        Ry normal "I'll just take a scoop of vanilla, nothing too special."

    menu:
        "Your ice cream preference matches you perfectly.":
            c "Your ice cream preference matches you perfectly."
            Ry look "How so?"
            c "Well... white dragon, white ice cream, it all kind of works."
            show katsu exhausted flip with dissolvemed

            if persistent.adinegoodending:
                Ry "*sigh* First with Adine, now with me."
                c "Yep, you can't escape it."
            else:
                Ry "*sigh* I guess you could think about it like that."
        
        "Good choice.":
            c "Good choice."
            Ry normal "Thanks!"
            Ry "In my opinion, vanilla is the tried and true classic. You can't go wrong with it."
    
    show remy normal with dissolvemed
    Ka smile flip "And what about you, little... Amely, is it?"
    Am smsad "..."
    Ry smile "I think she may be a bit overwhelmed with all of the different flavor choices."
    Ry normal "How about we just get here some chocolate?"
    Ka normal flip "I'm sure she will be quite happy with that choice, Remy."
    Ka "Just give me a second to get you your scoops!"
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    show amely smnormal at right with dissolvemed
    m "The dragon walked behind his stand and started preparing the ice cream."
    m "Expecting the dragon to produce some sort of utensil, I was surprised when he suddenly thrust his hand into the vat and pulled out an almost perfectly spherical scoop of ice cream."
    c "(Damn, these dragons can fly, shoot fire, run extremely fast, and even make an amazing scoop of ice cream with their bare hands. This truly is the peak of evolution.)"
    Ka "Y'know, most ice cream vendors use some sort of scoop. But over the years, you learn that your bare hands are faster and more efficient than any of those stupid tools." #Might be a bit pointless to have this
    c "Don't you walk using your hands?" #Hands, claws, feet, I'm very confused at this point
    Ry look "You know, I never really thought of that."
    Ka "Well, I wash my hands before serving the ice cream of course! I have a little station behind here and everything."
    c "(Whew)"
    show remy normal with dissolvemed
    m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top, ligtly pushing it down to make sure it didn't fall out."
    c "Interesting, those cones look exactly like the ones back in my world."
    show katsu excited flip at Position (xpos = 0.1) with easeinleft
    Ka "But I am sure that they don't taste half as good as mine!"
    m "Katsuharu then handed me the cone, topped with the [evalChosenFlavor] ice cream."
    show katsu smile flip with dissolvemed

    if evalChosenFlavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color." #Kinda bad, should change
    elif evalChosenFlavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif evalChosenFlavor == "strawberry":
        m "The strawberry ice cream looked different from what I was used to back in my world. Instead of a dark red, the scoop was tinted pinkish green, with small specks of what I assumed to be strawberry dotted within it."
    elif evalChosenFlavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif evalChosenFlavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif evalChosenFlavor == "special":
        m "The special was a disgusting mix of all the colors you don't want in your ice cream. It had a rather odd, dark gray color with pink dots speckled inside it, which I presumed was the fish."
    
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "I watched as Katsuharu went back to his stand and repeated the process for Remy and Amely's cones."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Here you go guys!"
    m "Remy and Amely took their cones from Katsuharu. Amely looked at her own in wonder."
    show amely smnormal at right with dissolvemed
    m "The instant her tongue made contact with the chocolate, her eyes lit up in excitement and she took another bite."
    Ry smile "I think she likes it."
    m "Amely was already attacking her cone from all angles."
    Ry normal "So, Amely, how is the ice cream?"
    Am "Ice cream... very good..."
    m "Her words were muffled as she continued devouring her cone."
    Ka "Well, as promised, this one is on the house."
    c "Thank you, Katsuharu."
    Ka smile flip "I should be thanking you. Without you, I wouldn't even have a business."
    c "This ice cream is more than enough to show your gratitude."
    play sound "fx/bite.ogg"
    m "Amely had already finished the scoop of ice cream and had just started working on the cone."
    Ry "Wow, the speed she's eating that ice cream is impressive!"
    Ka "Go ahead and stop by anytime you wish. I'll always have plenty of ice cream."
    c "Free of charge?"
    Ka exhausted flip "Well... We'll see. Amely could probably eat my entire stock and still have room for a full meal."
    Ry smile "I don't doubt that."

    if evalAmelyAnnoysLine:
        Ka normal flip "Anyways, I should probably get back to my stand before the people in line start getting too angry. Amely seems to have upset them enough as it is."
        Ry look "Yeah, sorry about that. Thank you though, Katsuharu."
        Ka "No problem. Any time."
    else:
        Ka normal flip "Anyways, I should probably get back to my stand before the people in line start getting too angry."
        Ry "Of course. Thank you Katsuharu."
        Ka "Anytime"
    
    show katsu normal with dissolvemed
    show remy normal with dissolvemed
    $ renpy.pause (0.2)
    hide katsu with easeoutleft
    c "Do you want to walk for a while?"
    Ry normal "As much as I would love to, it's a bit difficult as a quadruped like myself to hold ice cream and walk."
    m "I looked down to see Remy carefully walking on three legs while balancing the cone with his fourth."
    c "Of course, let's find a good place to rest."
    Ry "That area looks nice and peaceful."
    scene black with dissolveslow
    hide remy with dissolvemed
    hide amely with dissolvemed
    stop music fadeout 2.0
    m "We made our way over to where Remy was looking and sat down side by side." #I'm tempted to separate Remy and Amely for this part
    scene evalpark1 with dissolveslow
    play music "mx/serene.ogg"
    show amely smnormal with dissolvemed
    show remy normal behind amely with dissolvemed
    m "I noticed that Amely had almost completely finished her cone as well, only the bottom remaining."
    Ry "We should make a toast."
    c "But we don't have any drinks."
    Ry "I guess our cones will have to suffice."
    c "You were the one who came up with the idea, so you go first."
    Ry smile "Alright then... To our health, both physically and mentally. Both of us have had a rough time in the past, but we have both stayed strong and supported each other."
    if evalChosenFlavor == "vanilla":
        m "The two of us tapped our cones together, our scoops gently rubbing against each other."
        Ry look "Damn, our perfectly spherical scoops!"
    else:
        m "The two of us awkwardly tapped our cones together, careful as to not cross contaminate our different flavors."
    Ry normal "Seriously, though. I have so much to thank you for. Without you, I'm not sure I would be standing here at all today."
    c "Of course, Remy, I'll always be there for you, even when I inevitably have to leave through the portal."
    Ry look "Yeah. I've been thinking about that recently. I really don't know what I am going to do once you leave."
    c "Remember, I'm not leaving, just going back to the day I got here."
    Ry sad "Still, I can't shake off the felling that I won't ever see you again."
    c "What do you mean?"
    Ry "I know I said that I would see you again after you went through the portal, but in a way, I feel like when you enter that portal, you don't go back to my world, but a world exactly like mine with a dragon exactly like me."
    c "I see."
    Ry normal "But in the foreseeable future, you aren't going anywhere, and I am going to appreciate the time that I have with you."
    c "So will I."
    m "Amely, after finishing every little crumb of her ice cream, ran off to explore the area."
    hide amely with easeoutleft
    c "Well, there she goes."
    Ry "She'll be fine. It's your turn now, what do we toast to?"

    menu:
        "To our friendship.":
            c "To our friendship. Ever since I first arrived here, you have always been by my side, and I can say that you are the best friend that I have ever had."
            Ry smile "Wow, do you really mean that?"
            c "Of course, you have helped me more than you could possibly understand."
            Ry normal "I didn't think that I could possibly be much help in any situation, but I can promise that I will always be there for you."
            c "Thank you, Remy."
        "To our love." if mp.remyromance:
            c "To our love. You are the most gorgeous and kindhearted dragon I have ever met."
            Ry shy "That definitely isn't what I expected to hear, but thank you. I can also confirm that you are the most beautiful human that I have ever met."
            c "Not like I'm working with any real competition..."
            Ry normal "Hey, technically there were three humans here. I just sincerely mean what I said." #Meh, change this
            c "Thanks, Remy."
        "To this world.":
            c "To this world. You all accepted me with open arms and have shown me just how truly beautiful your civilization is."
            Ry "I'm glad you think of us that way. Of course, you haven't seen the shadier parts, but I would like to think that most of our civilization is like this."
            c "Any civilization is bound to have flaws, I just respect the way that the dragons handle conflict."
            Ry "Is it much different than your own world?"
            c "Here, decisions seem to be made mostly out of interest for the people. Of course, there are some exceptions like Emera, but a lot of diplomatic decisions on the human world are made solely for personal benefit."
            Ry look "That's too bad. We have that here, but most decisions made have the peoples' interests in mind."
            c "You get used to it, I guess."
    
    show remy normal with dissolvemed
    m "This time, we didn't tap our cones together for fear of further ruining our scoops."
    Ry "We should probably start eating our ice cream before it all melts, don't you think?"
    m "I looked down, spotting trickles of the [evalChosenFlavor] ice cream running down the cone and pooling on my hand."
    if evalChosenFlavor == "special":
        m "Somehow, it looked even more disgusting than before."
    c "Good idea."
    show amely smnormal with dissolvemed
    m "I noticed that Amely had returned and her focus seemed to have drifted to the ice cream in my hand."

    menu:
        "Let Amely have your ice cream.":
            c "Here, Amely, you can have mine."
            Ry look "Are you sure that's such a good idea? That's a lot of sugar for a small dragon like her."
            c "It should be alright. It's her first time anyways, she deserves a bit extra."
            Ry normal "I guess."
            m "Amely eagerly grabbed the cone from my hands and took a giant bite of the [evalChosenFlavor] ice cream."
            if evalChosenFlavor == "special": #Add a bit extra where MC takes the ice cream back from Amely and tastes it themself
                m "Her face instantly contorted into disgust."
                Am smsad "BAD!!!"
                m "Angrily, the little dragon threw the ice cream onto the ground."
                Am "Ice cream bad... Ice cream bad... Ice cream bad..."
                c "I don't think she's a fan of the special."
                Ry sad "I think you just ruined ice cream for this poor little dragon."
                m "That was mean. You know what you did."
                m "Now, both ice cream-less and much more depressed, Amely and I watched as Remy enjoyed his ice cream."
                Ry smile "I forgot just how good Katsuharu is at making ice cream. This is truly amazing."
                Am "Ice cream bad."
                Ry look "Amely, you should give ice cream another chance. [player_name] just gave you a flavor you didn't like. That's all."
                c "Yeah... Sorry about that."
                m "You aren't sorry. I can tell."
                Am "Ice cream bad."
                Ry normal "Here, Amely, how about we share mine? It's good, I promise."
                Am smnormal "Promise?"
                Ry "I promise."
                m "Amely walked over to Remy and carefully placed her toungue on his ice cream. Instantly, her face lit up in excitement and she took a giant bite."
                Ry smile "Whoah! Save some for me!"
                m "I watched as the two dragons happily enjoyed their ice cream together. While I sat alone on the bench without getting the chance to have any."
                scene black with dissolveslow
                m "You missed the entire point of this mod. Ignoring the fact that you tortured a child, you didn't even get to eat any ice cream. Shame on you."
                return #for now
            else:
                Ry "Wow, I've never seen Amely like something quite that much."
                m "It seemed that the little dragon ate this cone even faster than the first. Ice cream-less, I decided to simply sit and watch the two dragons enjoy their spoils."
                if mp.remyromance:
                    Ry "Hey, [player_name], you look like you could use some ice cream. Want to share mine?"

                    menu:
                        "Sure.":
                            c "Thank you Remy, I would love to."
                            hide amely with dissolvemed
                            m "I moved myself right next to the big dragon. He held out his ice cream between us and beckoned me to take a lick."
                            m "The second my tongue made contact with the smooth vanilla, I lit up in excitement."
                            c "Wow! This is some really amazing ice cream!"
                            Ry normal "It is quite impressive, is it not?"
                            m "The two of us made short work of the scoop. Muzzle and face mere centimeters apart."
                            m "Suddenly, I felt Remy's tongue through the scoop. It seemed as if we had made it to the center"

                            menu:
                                "Sneak in a kiss.":
                                    m "Awkwardly, I pushed my lips onto his."
                                    m "Remy seemed to have caught the memo, pressing his lips onto mine in response and slipping in his tongue."
                                    play sound "fx/kiss.wav"
                                    $ renpy.pause (1.0)
                                    Ry smile "That was the best bite yet!"
                                    c "I could say the same myself."
                                
                                "Pretend it didn't happen.":
                                    pass
                        
                            m "With our combined ice cream eating power, we were able to make quick work of the cone."
                            
                        "Don't worry about it.":
                            c "Don't worry about it Remy, enjoy your ice cream."
                            Ry smile "Whatever you say. I won't give up an opportunity for more ice cream."
                            $ renpy.pause (1.0)
                            m "After a while, I saw Katsuharu start walking over to us."
                            show katsu normal flip at left with easeinleft
                            Ka "Hey [player_name]. Just closing up and had and extra scoop of chocolate. Are any of you interested?"
                            Am "Me! Me!"

                            menu:
                                "Let Amely have a third scoop.":
                                    c "Amely can have it."
                                    Ry look "Okay, two scoops of ice cream was pushing it, but three? This is madness."
                                    c "No. This... Is... SPARTA!"
                                    Am "Ugh!"
                                    hide amely with easeoutleft
                                    $ renpy.pause (1.0)
                                    Ry "What did you just say?"
                                    c "Nevermind, ignore what I just said."
                                    Ry "[player_name], I think it's a bad idea if you let that little dragon have another scoop. She's already bouncing off the walls from all the sugar."
                                    m "Looking around, Amely was, in fact, running around the area like a pinball."
                                    c "You may be right, I guess I'll take it"
                                    show remy normal with dissolvemed
                                    Ka "Anyways, enjoy the chocolate ice cream!"
                                    c "Thanks Katsuharu!"
                                    show katsu normal with dissolvemed
                                    hide katsu with easeoutleft
                                
                                "Take the ice cream.":
                                    c "I'll take it."
                                    Am "No ice cream?"
                                    Ry "Amely, you've already had enough."
                                    hide amely with easeoutleft
                                    c "I'll say."
                                    m "Looking around, Amely was racing around the area like a pinball."
                                    Ka "Anyways, enjoy the chocolate ice cream [player_name]!"
                                    c "Thank you Katsuharu!"
                            
                            m "The second my tongue lay contact with the smooth [flavor], I lit up in excitement."
                            c "Wow! This really is amazing ice cream!"
                            Ry smile "Couldn't agree more."
                            m "The two of us sat for a while, watching the little dragon run around while we finished our cones."

                else:
                    $ renpy.pause (1.0)
                    m "After a while, I saw Katsuharu start walking over to us."
                    show katsu normal flip at left with easeinleft
                    Ka "Hey [player_name]. Just closing up and had and extra scoop of chocolate. Are any of you interested?"
                    Am "Me! Me!"

                    menu:
                        "Let Amely have a third scoop.":
                            c "Amely can have it."
                            Ry look "Okay, two scoops of ice cream was pushing it, but three? This is madness."
                            c "No. This... Is... SPARTA!"
                            Am "Ugh!"
                            hide amely with easeoutleft
                            $ renpy.pause (1.0)
                            Ry "What did you just say?"
                            c "Nevermind, ignore what I just said."
                            Ry "[player_name], I think it's a bad idea if you let that little dragon have another scoop. She's already bouncing off the walls from all the sugar."
                            m "Looking around, Amely was, in fact, running around the area like a pinball."
                            c "You may be right, I guess I'll take it"
                            show remy normal with dissolvemed
                            Ka "Anyways, enjoy the chocolate ice cream!"
                            c "Thanks Katsuharu!"
                            show katsu normal with dissolvemed
                            hide katsu with easeoutleft
                        
                        "Take the ice cream.":
                            c "I'll take it."
                            Am "No ice cream?"
                            Ry "Amely, you've already had enough."
                            hide amely with easeoutleft
                            c "I'll say."
                            m "Looking around, Amely was racing around the area like a pinball."
                            Ka "Anyways, enjoy the chocolate ice cream [player_name]!"
                            c "Thank you Katsuharu!"
                    
                    m "The second my tongue lay contact with the smooth [flavor], I lit up in excitement."
                    c "Wow! This really is amazing ice cream!"
                    Ry smile "Couldn't agree more."
                    m "The two of us sat for a while, watching the little dragon run around while we finished our cones."
        "Keep the ice cream.":
            m "I decided that one scoop of ice cream was enough sugar for Amely."
            c "Sorry, Amely, but I think you have already had enough ice cream for today."
            Am smsad "Pllleeeaaassseeee?"
            c "Sorry, but I don't think a little dragon like you should be having that much sugar in one sitting."
            Ry "Don't worry, Amely. We'll do this again sometime."
            Am "Fineeee."
            hide amely with easeoutleft
            m "The hatchling wandered off. Her attention seemed to drift to a group of what seemed to be butterflies. They were similar to what I had seen at home, but something about them was slightly... Off."
            Ry "And... there she goes."
            c "I guess we should enjoy our ice cream now before it all melts."
            if evalChosenFlavor == "special":
                show remy smile with dissolvemed
                m "At the same time, Remy and I took a bite of our ice cream. Instantly, Remy's face lit up in excitement, and mine contorted into disgust."
                if mp.fish:
                    c "Wow, this is just as disgusting as I remember it being."
                else:
                    c "Wow, this is disgusting."
                Ry look "Are you not a big fan of the special?"
                c "Not to offend anyone, but it's pretty gross."
                Ry normal "It isn't for everyone, but luckily, it is for me. Would you like to switch?"

                menu:
                    "Sure.":
                        c "I mean, if you're okay with it."
                        Ry smile "If you're happy, I'm happy."
                        show remy normal with dissolvemed
                        m "We quickly switched cones, and after a taste of the vanilla, I could see why Katsuharu was so well loved for his craft."
                        m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."
                        $ evalSwitchedCones = True
                    
                    "Don't worry about it.":
                        c "Don't worry about it. I think I just overreacted. It's not that bad."
                        Ry look "Alright then."
                        show remy normal with dissolvemed
                        m "Remy's cone did not last long. Soon, the only remnants of his ice cream lay in his stomach or dried on his hand."
                        m "I on the other hand did not finish quite as quickly. The flavor did glow on me over time, but it was something I definitely did not want to try again."
            else:
                show remy smile with dissolvemed
                m "At the same time, Remy and I took a bite of our ice cream. Instantly, both of us lit up in excitement."
                c "Wow, this really is amazing ice cream!"
                Ry "I forgot just how good Katsuharu is at making this stuff. This is spectacular!"
                m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."

    #Wow that was a long and confusing series of events to program, hopefully it isn't all messed up - It was, I fixed it I think
    scene evalpark2 with dissolveslow
    show remy normal with dissolvemed
    Ry "It's getting pretty late, [player_name]. I should probably be getting little Amely back to the orphanage."
    c "I didn't even notice how late it was! I should probably go back to my place as well."
    Ry "Amely? Where are you?"
    show amely smnormal flip with easeinleft
    show amely smnormal with dissolvemed
    Am "Ice cream?"
    Ry smile "No, Amely, you've had enough ice cream for today."
    Am smsad "Awwww."
    show amely smnormal with dissolvemed
    Ry normal "Well, I guess this is our goodbye. It was fun [player_name]!"
    c "It sure was. We should do this sort of thing more often. Especially if it involves ice cream."
    Ry smile "I second the ice cream part."
    hide amely with dissolvemed
    hide remy with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/takeoff.ogg"
    m "I watched as Remy carefully positioned Amely in his claws and gracefully took off into the night sky."
    m "I, on the other hand, started making my way back home."
    scene black with dissolveslow
    $ renpy.pause (0.5)
    scene evalplayerapt1 with dissolveslow
    m "When approaching the door, I found Remy standing next to it."
    show remy normal with dissolvemed
    c "Hey, what are you doing here?"
    Ry smile "I thought it would be rude to just run, or I guess in this case fly, off like that."
    c "How thoughtful."

    menu:
        "Would you like to come inside?":
            c "Would you like to come in? It's a bit chilly out here."
            Ry smile "Sure!"
            scene black with dissolveslow
            $ renpy.pause (0.5)
            scene o3 with dissolveslow #Add pan
            show remy normal with dissolvemed
            Ry look "This place really hasn't changed much since I was last in here, [player_name]. You've really got to spice it up every once and a while."
            c "I haven't had the time to get around to that. With the whole coma and world saving stuff going on."
            Ry normal "Right, that probably did take up a lot of your free time."
            c "I wonder if they deactivated my ambassador card yet."
            Ry smile "I haven't heard anything about it. You might want to do some last minute furniture shopping before they do though."
            c "Good idea."
            Ry normal "Hey, now that I'm here, would you mind if I slept here for the night? Night flying isn't really my specialty."
            c "Of course you can Remy, you're always welcome here."
            Ry smile "Thanks, [player_name]!"
            m "He started to make his way over to the couch."

            menu:
                "Offer to share the bed.":
                    c "Wait, Remy."
                    Ry look "Yes?"
                    c "You could sleep in bed with me if you like. It's a bit small, but it should work."
                    Ry shy "That... Well, I would love to [player_name]!"
                    c "Glad to hear it. Maybe we could have some fun as well."
                    Ry smile "We'll see where things go, [player_name]."
                    hide remy with dissolvemed
                    m "The dragon and I made our way to the bedroom. Without hesitation, Remy removed his tie and rested it on the nightstand."
                    show remy normal b with dissolvemed
                    Ry "Can't have this thing one while I sleep."
                    c "Doesn't look like the most comfortable sleeping attire."
                    hide remy with dissolvemed
                    play sound "fx/undress.ogg"
                    m "I got undressed, and the two of us got into the bed together."
                    c "A bit cramped, don't you think?"
                    m "Remy grabbed me and pulled me in closer to him, engulfing me in his soft, white scales."
                    Ry "Better?"
                    c "Much."
                    #Add something to do with the dragon pillow variable
                    m "More to this epic romance tale coming soon because I suck at writing this stuff!" #Add more here later
                    stop music fadeout 2.0
                    scene black with dissolveslow
                    $ persistent.evalAmelyEnding = True
                    return
                
                "Let him have the couch.":
                    c "The couch is pretty big. You should be quite comfortable sleeping there for the night."
                    Ry "I guess so."
                    hide remy with dissolvemed
                    m "The dragon clambered up onto the couch, resting his head down on the armrest."
                    m "I turned off the lights, then made my way to the bedroom."
                    Ry "Good night, [player_name]."
                    m "Good night, Remy."
                    scene black with dissolveslow
                    stop music fadeout 2.0
                    $ persistent.evalAmelyEnding = True
                    return
        
        "It's quite late, you best be getting home.":
            c "You should probably make your way home, Remy. It's getting quite dark."
            Ry look "Hmmm, I guess you're right. Night flying isn't really my specialty."
            c "It was a fun outing today."
            Ry normal "It sure was, we definitely need to do that more often. Especially since the date of your departure seems to be creeping up."
            c "Let's just ignore that for the moment and enjoy the time we have together now."
            Ry "You're right. I'm getting ahead of myself again."
            Ry smile "Anyways, see you around!"
            c "Bye, Remy!"
            hide remy with dissolvemed
            play sound "fx/takeoff.ogg"
            m "Just like that, the dragon gracefully took off into the air, soaring away over the trees."
            scene black with dissolveslow
            stop music fadeout 2.0
            $ persistent.evalAmelyEnding = True
            return

label eval_remy_amely_adine_1: #Ending where "everyone" is here! Totally everyone, idk what you're talking about.
    #Going to use this twice, one where you DO ride remy beforehand and when you DO help at the orphanage. That's gonna be a lot of refactoring...
    play sound "fx/wooshes.ogg"
    $ renpy.pause (3.0)
    Ry smile "I wonder who that could be?"
    play sound "fx/door/door_open.wav"
    hide amely with dissolvemed
    hide remy with dissolvemed
    show amely smnormal at right with dissolvemed
    show remy normal behind amely at right with dissolvemed
    show adine normal c flip at left with dissolvemed
    play music "mx/cruising.ogg"
    Ad "Hey guys! What are you doing here?"
    Ry "Looking for you!"
    m "Adine took off her goggles."
    show adine giggle b flip at left with dissolvemed
    Ad "Well, I guess you found me, or rather, I found you."

    if not evalReplaceBulbs or not evalResetBreaker: #If the lights are still broken
        Ad think b flip "Hey, Remy. Why are the lights turned off?"
        Ry look "Well... They're broken."
        Ad disappoint b flip "Oh. Poor Amely was stuck in the dark all this time?"
        Am smsad "Dark!"
        Ad sad b flip "Oh, I'm so sorry Amely! I didn't know!"
        Ry "I wouldn't worry too much, Adine. She's fine."
        Ad disappoint b flip "I guess..."
    
    if evalOrphanageScore == 2: #If the player did perfectly on the minigame
        Ad think b flip "Wait a minute..."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine think b flip with dissolvemed
        Ad giggle b flip "What did you guys do? The orphanage looks amazing!"
        Ry smile "Well, [player_name] and I wanted to surprise you by cleaning up the place a little bit."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine giggle b flip with dissolvemed
        Ad "This isn't real. My eyes are deceiving me."
        c "You don't believe us?"
        Ad normal b flip "Are you kidding me? This place hasn't looked this good in years!"
        Ad "How did you manage to do all of this so quickly?"
        Ry normal "Teamwork. Amely and I gathered supplies and [player_name] did all the handiwork."
        Ad "[player_name], you do not understand how grateful I am that you did this."
        hide adine with dissolvemed
        play sound "fx/hug.mp3"
        m "Adine walked up and gave me a big hug." #The wyvern gives you a hug. Mission complete.
        m "With wings as arms, I was engulfed completely."
        play sound "fx/hug.mp3"
        m "She then walked over to Remy and repeated the process."
        show remy shy behind amely at right with dissolvemed
        Am "Me! Me!"
        play sound "fx/hug.mp3"
        m "Adine got down on her knees and completely hid the little dragon within her wings."
        show adine normal b flip at left with dissolvemed
        Ad "Now, I know the real reason you came here wasn't just to clean up the place."
        c "Alright you got me."
        Ad "Well. Why are you here then?" 
    elif evalOrphanageScore == 1:
        Ad "Wait... Did you guys do something here?"
        Ry smile "Well, [player_name] and I did a bit of work while we were wating for you."
        Ad "Really? That's so kind of you! What were you waiting on me for?"
    else:
        Ad normal b flip "I expected to find you here Remy, but what is [player_name] doing here?"
    c "Ice cream."
    show remy look at right with dissolvemed
    Ad annoyed b flip "What?"
    c "Katsuharu owes me as much ice cream as I want, and I thought who better to bring than you two and Amely?"
    Ad think b flip "I have never heard of that dragon giving anyone free ice cream."
    Ad "You must have done something quite spectacular to get a deal like that."
    show remy normal at right with dissolvemed
    c "Just a little bit of business advice. I told him to move his stand down to Tatsu Park."
    Ad "You're telling me that you get an infinite supply of the world's best ice cream for free because you told him to move to Tatsu Park?"
    c "Well, not infinite. He said I could come by and get some ice cream when I felt like it."
    Ad normal b flip "So it's more of a one time deal. I get it. Count me in."
    Ry smile "That's great! This is going to be fun!"
    Ad giggle b flip "Two dragons, a human with a big appetite, and a hatchling with unlimited access to delicious ice cream. I sure hope Katsuharu has enough stock."
    c "We couldn't possibly eat {i}that{/i} much ice cream, could we?"
    Ad normal b flip "Coming from someone who has had three scoops in one sitting before, it is definitely possible."
    Ry smile "So, Amely, are you excited to have your first ever scoop of ice cream?"
    Am smsad "Ice... cream?"
    c "Ice cream is kind of like... Well... Um..."
    m "I didn't think it would be so difficult to describe something as simple as ice cream."
    Am smnormal "Sugar?"
    c "Yes, lots of sugar."
    Am "Sugar!!!"
    Ad giggle b flip "I'm going to take that as a yes."
    if not evalOrphanageScore == 2:
        Ry look "What about the orphanage, Adine?"
        Ad normal b flip "We can do the maintenance work any time we want. I don't know how many other opportunities Amely would get to experience something like this."
        Ry normal "Good point."
    Ad think b flip "Wait a minute."
    Ad "How are we supposed to get back to Tatsu Park?"
    Ad "I can fly Amely over, but how is [player_name] going to make it there in a reasonable amount of time?"
    Ry normal "[player_name] could just ride me."
    Ad giggle b flip "[player_name] could ride you, Remy? Is this really the time?"
    Ry shy "Why does everyone keep taking this the wrong way? I didn't mean it like {i}that{/i} Adine!"
    m "I chuckled softly."
    Ad "Sure you didn't, Remy."
    Ry "Adine..."
    Ad normal b flip "Okay, I'll stop. For now."
    Ry look "Great... Let's just get going."
    Ad "Alright, Amely, let's go."
    Am "Sugar!!!"
    hide amely with easeoutleft
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    Ad "Whoah! Wait for me Amely! I'm the one with wings here!"
    show adine normal b with dissolvemed
    hide adine with easeoutleft
    $ renpy.pause (1.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.5)
    play sound "fx/takeoff.ogg"
    m "After a moment, Adine caught up with Amely. Clutching the little hatchling in her claws, she took off and soared into the air."
    hide remy with dissolvemed
    show remy normal with dissolvemed
    if not evalRodeRemy:
        c "Well, are we going to fly off after them?"
        Ry normal "Not to be rude, but I doubt I could fly around with you on my back."
        c "Are you calling me fat?"

        if evalAskIfFat:
            Ry look "Not this again, [player_name]."
            c "Fine, you got me there."
        else:
            Ry shy "N... No of course not. I didn't mean it that way... I just meant..."
            c "I'm kidding, don't sweat it."
            Ry normal "Dragons don't sweat."
            c "Noted."
            $ evalSweatJoke = True

        Ry normal "I was thinking that instead of flying, I could just run."
        c "Are you fast on the ground?"
        Ry "Not as fast as a runner, but I'm still quite quick."
        c "Alright then, let's see how quick those legs really are."
    else:
        Ry "Well, are you ready, [player_name]."
        c "Sure am."
    hide remy with dissolvemed
    play sound "fx/bed.ogg"
    m "Remy got down on all fours."
    m "Making sure not to mess up his tie, I carefully hopped onto his back. He folded his wings back to give me as much room as possible."
    if not evalRodeRemy:
        Ry "Oof, if I had any hopes of taking off before, they are all gone now."
        c "Wait a minute..."
        Ry "Goodness, stop being such a softie."
    m "After finding a relatively comfortable spot on his back, Remy lifted his body."
    Ry "How is it back there?"
    if not evalRodeRemy:
        c "A bit uncomfortable. I think I need a saddle."
        Ry "Funnily enough, you can actually buy dragon saddles."
        c "That's... Interesting."
        Ry "They exist. I didn't say they were popular."
    else:
        c "I'm seriously considering the saddle now."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (3.0)
    play sound "fx/door/door_open.wav"
    scene hatchery with dissolveslow
    Ry "Would you mind locking the door and hiding the key again?"
    c "Sure."
    m "Not wanting to repeat the process of getting on Remy, I grabbed the key and stretched my arm towards the door."
    play sound "fx/door/doorchain.ogg"
    m "With some difficulty, I managed to slip in the key and lock the door."
    c "How do I get the key back under the pot?"
    Ry "Like this."
    m "Remy walked over to the pot and tilted it up with his muzzle."
    m "I put the key back, and he carefully rested the pot back in it's upright position."
    Ry "Perfect! Let's go!"
    play sound "fx/steps/rough_gravel.wav"
    if not evalRodeRemy:
        m "Remy then slowly started walking forward, picking up speed surprisingly quickly."
        $ evalRodeRemy = True
    else:
        m "Remy walked forward and quickly picked up speed."

    if not evalRodeRemy:
        if evalRodeBryce:
            m "It wasn't as uncomfortable as I had first imagined."
            m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "In a way, it also felt strangely familiar, like I had done this before."
            m "The experience was almost relaxing, with the light breeze and rhythmic thumping of Remy's feet on the grass and pavement."
        else:
            m "It wasn't as uncomfortable as I had first imagined."
            m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
    else:
        m "As a seasoned dragon rider. I sat back and gazed up at the sky." #Is this too... weird?
    
    $ renpy.pause (0.5)
    m "It seemed as if it took mere minutes to arrive back at Tatsu Park."
    Ry "Ladies and gentledragons, this will be our final stop. Please make sure to grab all of your belongings and safely exit the vehicle."
    if not evalRodeRemy:
        c "Very funny Remy."
        Ry "Thanks, I can tell that you sincerely mean that."
    else:
        c "Saying the same joke twice doesn't make it funnier, Remy."
        Ry "Nonsense."
    play sound "fx/bed.ogg"
    m "I slid off of Remy's back."
    scene park2 with dissolveslow
    show remy normal with dissolvemed
    play music "mx/funness.ogg"
    if evalRodeRemy:
        c "That was fun! I should ride you around more often!"
    else:
        c "Damn, why didn't I just ride you over to the orphanage as well. That was fun!"
    Ry smile "Wow, [player_name], I didn't know you wanted to ride me so badly."
    m "My face turned bright red."
    Ry "You look like a tomato."
    c "I'll get you back for this, Remy."
    Ry "I'm sure you will."
    m "I spotted Adine and Amely walking over to us."
    hide remy with dissolvemed
    show remy normal at right with dissolvemed
    show amely smnormal flip at left with dissolvemed
    show adine normal b flip behind amely at left with dissolvemed
    Ad "Took you guys long enough to get here."
    Ad "I don't suppose you had a bit of fun did you?"
    m "My face, just about to return to it's normal shade, became bright red once again."
    Ry shy "Adine, this is getting old."
    Ad giggle b flip "Then why are both of you bright red?"
    c "Nothing happened. We had to lock up the orphanage."
    Ad normal b flip "Okay, okay, I'll stop pestering you two about it."
    Ry look "Finally."
    m "Something in Adine's eyes told me that she would not stop pestering us about it."
    Ad "So, you said Katsuharu relocated here. Any idea where he is?"
    m "Suddenly, inspiration struck me as Adine idly moved her tail in my direction."
    c "Not sure, Adine. Why don't we call and find out?"
    m "I stepped and grabbed the end of Adine's tail."
    Ad think b flip "What the..."
    Ry look "[player_name], what are you doing?"
    m "I held the crescent moon end of Adine's tail up to my ear like a telephone."
    c "Hey, is this Katsuharu? We were just wondering where you set up for the day."
    Ry smile "Ah, the ol' banana phone."
    Ad annoyed b flip "This is so unbelievably stupid."
    c "Oh, you're at the front of that long line of dragons over there? Thanks!"
    $ evalAdineSlaps += 1
    play sound "fx/slap1.wav"
    m "The second I released my grip, Adine flicked her tail and slapped me square in the face."
    Am "Ouch!"
    c "Totally worth it."
    Ry "I have to admit, that was pretty funny."
    Ad "I hate you both."
    c "Hey! You were asking for it."
    Ad "I guess I was. But still, screw you guys."
    Ry normal "Now we're even."
    Ad giggle b flip "Oh, you think this is over? This is only the beginning."
    c "Oh no."
    Am "Ice cream?"
    Ry "I almost forgot about the ice cream! We should probably go before Katsuharu closes up for the day."
    scene black with dissolveslow
    hide amely with dissolvemed
    hide remy with dissolvemed
    hide adine with dissolvemed
    m "We made our way to the end of the line of dragons I had seen earlier."
    scene town2 with dissolveslow
    show remy normal at right with dissolvemed
    show amely smnormal flip at left with dissolvemed
    show adine normal b flip behind amely at left with dissolvemed
    Ry "Wow, this is quite an impressive line."
    c "It seems that my advice has paid off for him after all."
    Ry smile "Indeed."
    Ad "So, are we planning on waiting in line with everyone else?"

    menu:
        "It would be rude to skip everyone.":
            c "It would be rude to skip everyone."
            Ry "I would have to agree with you. All of these people have been waiting for a long time to get their ice cream, and I'm sure it would make them unhappy if we just skipped ahead."
            Ad think b flip "I'm not too sure."
            Ad "If Katsuharu was willing to give you free ice cream, I'm sure he would be more than willing to let you skip the line as well."
            Ry normal "It's not that. I just don't think we should be attracting so much attention to ourselves, especially with [player_name]."
            Ad normal b flip "True."
            c "Looks like the line is about an hour long." #Do I add a mini game??? Tune in next time for //Is Eval Lazy?\\
            m "For the next hour, Remy, Adine and I engaged in lighthearted chatter, discussing our interests and the events that had gone on while I was in my coma."
            m "Amazingly enough, not a single innuendo or banana phone joke was made."
            m "After what seemed like forever, it was finally our turn to get ice cream."
        
        "I think we can skip the line.":
            c "I think that my unlimited ice cream pass also includes an express pass to the front of the line."
            Ry look "Are you sure? I'm not sure how well some of his customers will react to us cutting them in line."
            Ad "If Katsuharu was willing to give [player_name] free ice cream, then I'm sure he would be more than willing to let him skip the line as well."
            Ry "I guess. I just feel like we shouldn't be attracting so much attention to ourselves, especially with [player_name]."
            Ad "Most of the concern and interest in humans has already died off. Sure, we might get a few stares here or there, but nothing more."
            Ry normal "I suppose you're right."
            c "You guys have had front row seats to the whole human show as well though. You might be a bit more used to me than everyone else."
            Ad "With the amount of press about your arrival. I'm sure just about every person in this line has seen or read everything about you."
            c "Wow, I'm famous."
            Ry "Don't let it get to your head."
            c "Too late, I think it already has."
            m "As we passed down the line, we were met with a mix of expressions. Some of the people seemed quite intrigued by my appearance, while others seemed annoyed, probably understanding our intentions to skip the line."
            m "Approaching the stand, I caught the attention of Katsuharu. He waved and beckoned us to come."
    
    scene town7 with dissolveslow
    show amely smnormal at right with dissolvemed
    show remy normal behind amely at right with dissolvemed
    show adine normal b behind remy at Position (xpos=0.6) with dissolvemed
    show katsu normal flip at Position (xpos=0.1) with easeinleft

    Ka "Well, if it isn't the business saving human, [player_name]! Have you come to take up my offer?"

    menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while, hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it."
            c "Hopefully it should all return back to the peaceful way it was."
            c "Everything has more or less resolved itself and the conflict is over."
            Ka smile flip "Glad to hear that."
            c "Is it alright if I brought these three along as well?"
            Ka exhausted flip "Wow... When I offered you that ice cream, I didn't think you would bring all of your friends as well."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka "Hmmm..."
            Ka smile flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this?"
            Ka "You four get as much ice cream as you desire. But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream."
            Ad normal b "It might even be fun."
            Am "Ice cream!"
            Ry "I guess it's really up to you, [player_name]. This was your idea after all."
        
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right behind amely with dissolvemed
            show adine annoyed b at Position (xpos=0.6) behind remy with dissolvemed
            Ka smile flip "*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka normal flip"I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry normal "I... guess I do remember being quite excited that day."
            Ka "I also remember Adine's first time as well."
            Ad giggle b "You do?"
            Ka "Of course. You really, really wanted three cones that day."
            Ka "It was quite entertaining watching you hop away on one foot while holding ice cream in your hands and other foot."
            Ad "I remember getting a lot of strange looks from other dragons that day."
            Ry smile "I think I remember that too. Didn't you almost fall."
            Ad annoyed b "Of course I didn't. My feet are very dextrous. Walking on one foot isn't a big deal."
            Ry normal "How sanitary is holding ice cream with your feet though, Adine?"
            Ad normal b "I was a kid, you really think I was worrying about something like that?"
            Ka "Well, enough about embarrassing childhood memories. [player_name], when I gave you that offer for ice cream, I didn't expect you to bring all of your friends."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka normal flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this? You four get as much ice cream as you desire."
            Ka "But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream. It might even be fun."
            Am "Ice cream!"
            Ry "I guess it's really up to you, [player_name]. This was your idea after all."
    
    menu:
        "Help out Katsuharu.":
            c "You really think I would leave you guys like that? Of course we can help you, Katsuharu."
            show remy normal at right behind amely with dissolvemed
            show adine normal b at Position (xpos=0.6) behind remy with dissolvemed
            Ka exhausted flip "Thank goodness. Today has been quite rough, and It'll be nice to have some extra hands."
            Am "Ice cream?"
            Ry smile "Soon, Amely. First we have to help serve it."
            Am smsad "Why?"
            Ad giggle b "Because then you get two scoops of ice cream instead of one!"
            Am smnormal "More sugar?"
            Ad normal b "Yes, much more sugar."
            Am "I help! I help!"
            Ka excited flip "That's the spirited staff I want! Let's get to work!"
            m "The four dragons made their way behind the cart. I followed closely behind."
            show katsu normal at Position (xpos=0.1) with dissolvemed
            hide katsu with easeoutleft
            hide adine with easeoutleft
            hide remy with easeoutleft
            hide amely with easeoutleft
            scene black with dissolveslow
            scene evalkatsucart with dissolveslow
            Ka normal "Alright, here's the plan everyone."
            Ka "Remy, grab a scoop from that drawer there."
            Ka "[player_name], you take orders."
            Ka "And Adine..."
            Ka "Just make sure Amely doesn't cause too much chaos."
            Ry normal "Yes sir!"
            Ad giggle b "Sounds good, Katsuharu."
            Ka "Quick tip, [player_name]. Customers don't always want the same thing. Try adapting to their interests."
            c "Seems simple enough."
            jump eval_katsu_help_init

        "Enjoy your ice cream alone.":
            stop music fadeout 2.0
            if evalHelpOrphanage:
                c "I think I've already done enough work today helping at the orphanage."
            else:
                c "That seems like a lot more work than I want to put up with at the moment."
            
            Ka exhausted flip "I was looking forward to the extra help."
            Ry sad "Oh, I see, [player_name]."
            Am smsad "Ice cream?"
            Ry "Sorry, Amely. I guess not today."
            Am "Awwwwww."
            show remy sad flip with dissolvemed
            show amely smsad flip with dissolvemed
            hide remy with easeoutright
            hide amely with easeoutright
            m "With his head hung low, Remy walked away with Amely."
            Ka "I'll... go get you your ice cream, [player_name]."
            show katsu exhausted with dissolvemed
            hide katsu with easeoutleft
            Ad frustrated b "Did you seriously make us come all the way just to flake out on us?"
            c "Sorry, Adine. I just really don't feel like doing this right now."
            c "Also, can't you just wait in line and get the ice cream for yourselves."
            Ad "Ugh. It isn't about the ice cream any more, [player_name]! It was about spending time together."
            Ad sad b "But I see how it is. You care more about yourself than your friends."
            Ad annoyed b "I can't believe that I ever thought you were a friend of mine."
            Ad sad b "If you will excuse me, I'm going to go talk to Remy. You really hurt him with that, [player_name]."
            c "I..."
            Ad annoyed b "Shut up."
            show adine disappoint b flip with dissolvemed
            hide adine with easeoutright
            Ad sad b "Remy, are you alright?"
            m "I could hear faint crying in the distance."
            show katsu exhausted flip with easeinleft
            Ka "Well... Here you are."
            c "Thanks, Katsuharu."
            show katsu exhausted with dissolvemed
            hide katsu with easeoutleft
            m "Without another word, the old dragon returned to his stand."
            m "Watching him work, I spotted a single tear roll down one of his cheeks."
            m "As I looked behind me, I noticed that the attention of just about every dragon in line had shifted to me. They had seen everything."
            m "Shamefully, I started on my way back to my place."
            "???" "Did you see what that human just did? That was horrible!"
            "???" "I can't believe someone could be that selfish!"
            m "Hearing these comments, I picked up my pace."
            scene black with dissolveslow
            m "Wow, that was mean!"
            return
            #Add a bit more to this? Maybe, but now I'm sad. After playtesting, I really do. But now I'm sad again :'(

label eval_remy_amely_adine_2:
    m "I looked out across the park. It seemed that every dragon was happily eating their ice cream."
    c "I think we're done, guys!"
    Ka "Awesome!"
    stop music fadeout 2.0
    scene black with dissolveslow
    scene town7 with dissolveslow
    $ renpy.pause (1.0)
    show katsu normal flip at Position (xpos=0.1) with dissolvemed
    show remy normal at right with dissolvemed
    play music "mx/jazzy2.ogg"
    Ka excited flip "Everyone did absolutely fantastic!"
    Ka smile flip "Remy, I must say. You really have a knack for making ice cream."
    Ry smile "Thank you, Katsuharu! I guess I learned from watching you."
    c "Hey, where are Adine and Amely?"
    Ry normal "Look up."
    m "I looked up in the sky. It took a second, but I found Adine flying in circles with Amely in her claws."
    Ry "Hold on, let me grab them."
    show remy normal flip with dissolvemed
    hide remy with easeoutright
    play sound "fx/takeoff.ogg"
    m "Remy took a few steps, then flew into the air."
    m "He caught up to Adine, and the two hovered in place for a moment before landing next to Katsuharu and I."
    show amely smnormal at right with easeinright
    show remy normal behind amely at right with easeinright
    show adine normal c behind remy at Position (xpos=0.6) with easeinright
    Ad "Hey guys! How'd it go!"
    c "It was a lot of work, but in a way, it was also nice talking to all the locals."
    Ry smile "And I think I'm now a certified ice cream scooper!"
    Ka "That you are, Remy."
    Ka exhausted flip "That was exhausting. I cannot thank you enough for your help."
    Ry normal "Glad we could help, Katsuharu."
    Ka smile flip "I think Adine had the hardest job here, though."
    m "Adine removed her goggles."
    Ad annoyed b "Ugh. It's impressive just how much chaos such a small dragon can cause."
    c "I saw you a few times. It looked like you two were having fun."
    Am "Very fun!"
    Ad giggle b "Maybe for her, yes."
    if evalCustomerScore == 10:
        Ka smile flip "[player_name], you did a wonderful job serving everyone. I don't think I saw a single unhappy customer!"
        c "Thanks, Katsuharu, but I couldn't have done it without all of you as well."
        Ad normal b "Even though I was busy coralling Amely the whole time?"
        c "If you weren't, I'm sure Amely would make a few of the customers unhappy."
        Ad giggle b "Good point."
    elif evalCustomerScore > 6:
        Ka normal flip "Great job serving everyone, [player_name]. I saw a lot of happy customers walking off."
        c "Thanks, Katsuharu."
    else:
        Ka normal flip "You did well serving everyone, [player_name]. There were a few happy customers I saw walking off."
        c "Thanks, Katsuharu."
    show adine normal b with dissolvemed
    Ka "And Remy, you're quite talented with that scoop."
    Ry smile "Thanks, Katsuharu! You actually taught me a while back, if you remember."
    Ka smile flip "Of course I do! I'm glad to see that talent never left you."
    Ka "Maybe you'll stop by more often to help me."
    Ry "That was actually a lot of fun. If I have a day off I'll make sure to come over here and see if you're open."
    Ka normal flip "Now, while I would love to keep chatting with you four all day, I still owe you some ice cream!"
    Ad "I could really use some of that right now."
    Ry normal "I second that."
    Am "Ice cream!"
    Ka "Let's start with [player_name]."
    $ evalCurrentEnding = 3 #DELETE THIS LATER THIS IS TEMPORARY BECAUSE IM TOO LAZY TO GO BACK AND DO BOTH MINIGAMES AGAIN!!!!!
    jump eval_ice_cream_choice

label eval_remy_amely_adine_3:
    Ka normal flip "You're up next, Remy. What will you have?"
    if evalChosenFlavor == "vanilla":
        Ry smile "I'll have a scoop of vanilla as well!"
    else:
        Ry normal "I'll just take a scoop of vanilla, nothing too special."

    menu:
        "Your ice cream preference matches you perfectly.":
            c "Your ice cream preference matches you perfectly."
            Ry look "How so?"
            c "Well... white dragon, white ice cream, it all kind of works."
            show katsu exhausted flip at Position (xpos=0.1) with dissolvemed

            if persistent.adinegoodending and evalCurrentEnding != 3:
                Ry "*sigh* First with Adine, now with me."
                c "Yep, you can't escape it."
            elif evalCurrentEnding == 3:
                Ry "*sigh* I guess you could think about it like that."
                Ad giggle b "See, Remy? I'm not the only one who thinks that!"
                c "Am I missing something?"
                Ad normal b "When we used to get ice cream as kids, everyone would always call Remy the 'Vanilla Dragon'."
                Ry "Yes, a name I would like to leave in the past."
                Ad giggle b "Too late, Remy. [player_name] brought it back to light."
                if evalAdineSlaps == 2:
                    Ry smile "Well Adine, now that both of us have a flavor associated with us, what should [player_name]'s flavor be?"
                    Ad think b "That's a good question."
                    Ad "That skin tone isn't exactly the most appealing in the form of food, so I can't say there's many options."
                    Ry look "Pumpkin?"
                    Ad "Too orange. Plus that's not an ice cream flavor."
                    Ka normal flip "You know, that doesn't sound half bad."
                    Ka smile flip "Check back this fall. You might just see that on the menu."
                    Ad normal b "Really? That sounds quite good!"
                    Ry normal "Well. I'm stumped on [player_name]'s flavor."
                    Ad "Same here."
            else:
                Ry "*sigh* I guess you could think about it like that."
        
        "Good choice.":
            c "Good choice."
            Ry normal "Thanks!"
            Ry "In my opinion, vanilla is the tried and true classic. You can't go wrong with it."

    Ka normal flip "Okay, Adine. What can I get you?"
    if evalChosenFlavor == "special":
        Ad normal "I'm curious to try the 'special' with [player_name]."
    else:
        Ad normal b "I think I'll try the 'special'."
    Ka "Good choice! I think you'll like it."
    Ad giggle b "I've served the dish enough times. I'm curious to see how it is as ice cream."
    Ka smile flip "Much better. I promise."
    show adine normal b with dissolvemed
    Ka normal flip "And what about you, Amely?"
    Am smsad "..."
    Ry smile "I think she may be a bit overwhelmed with all of the different flavor choices."
    Ry normal "How about we get her some chocolate?"
    Ka "I'm sure she will be quite happy with that choice, Remy."
    Ka "Just give me a moment to get all of you your scoops!"
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    show amely smnormal at right with dissolvemed
    m "The dragon walked behind his stand and started preparing the ice cream."
    m "Expecting the dragon to produce some sort of utensil, I was surprised when he suddenly thrust his hand into the vat and pulled out an almost perfectly spherical scoop of ice cream."
    c "(Damn, these dragons can fly, shoot fire, run extremely fast, and even make an amazing scoop of ice cream with their bare hands. This truly is the peak of evolution.)"
    Ka "Y'know, most ice cream vendors use some sort of scoop. But over the years, you learn that your bare hands are faster and more efficient than any of those stupid tools." #Might be a bit pointless to have this
    c "Don't you walk using your hands?" #Hands, claws, feet, I'm very confused at this point
    Ry look "You know, I never really thought of that."
    Ka "Well, I wash my hands before serving the ice cream of course! I have a little station behind here and everything."
    c "(Whew)"
    show remy normal with dissolvemed
    m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top, ligtly pushing it down to make sure it didn't fall out."
    c "Interesting, those cones look exactly like the ones back in my world."
    show katsu excited flip at Position (xpos = 0.1) with easeinleft
    Ka "But I am sure that they don't taste half as good as mine!"
    m "Katsuharu then handed me the cone, topped with the [evalChosenFlavor] ice cream."
    show katsu smile flip with dissolvemed

    if evalChosenFlavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color." #Kinda bad, should change
    elif evalChosenFlavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif evalChosenFlavor == "strawberry":
        m "The strawberry ice cream looked different from what I was used to back in my world. Instead of a dark red, the scoop was tinted pinkish green, with small specks of what I assumed to be strawberry dotted within it."
    elif evalChosenFlavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif evalChosenFlavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif evalChosenFlavor == "special":
        m "The special was a disgusting mix of all the colors you don't want in your ice cream. It had a rather odd, dark gray color with pink dots speckled inside it, which I presumed was the fish."

    m "I watched as Katsuharu went back to his stand and repeated the process for Remy, Adine, and Amely."
    show katsu normal at Position (xpos=0.1) with dissolvemed
    hide katsu with easeoutleft
    $ renpy.pause (2.0)
    show katsu normal flip at Position (xpos=0.1) with easeinleft
    Ka "Here you go everyone!"
    m "The three dragons took their cones from Katsuharu. Amely looked at her own in wonder."
    show amely smnormal at right with dissolvemed
    m "The instant her tongue made contact with the chocolate, her eyes lit up in excitement and she took another bite."
    Ad giggle b "Well, I think someone likes ice cream."
    m "Amely was already attacking her cone from all angles."
    Ry normal "So, Amely, how's the ice cream?"
    Am "Ice cream... very good..."
    m "Her words were muffled as she continued devouring her cone."
    Ad normal b "I've never seen her eat something so fast!"
    Ka "Well, as a thank you for your help today, this is on the house."
    c "Thank you, Katsuharu."
    Ka smile flip "I should be thanking you. Without you, I wouldn't even have a business."
    c "This ice cream is more than enough to show your gratitude."
    play sound "fx/bite.ogg"
    m "Looking down to Amely, I noticed that she had already finished her ice cream."
    Ad giggle b "Wait, is she already done?"
    Ry smile "Seems like it."
    Am "More?"
    Ry look "We did promise to give her two, didn't we."
    Ad normal b "I guess we did. Would you like another scoop of chocolate, Amely?"
    Am "Yes!"
    Ka normal flip "Another scoop of chocolate coming right up!"
    show katsu normal at Position (xpos=0.1) with dissolvemed
    hide katsu with easeoutleft
    show remy normal behind amely at right with dissolvemed
    $ renpy.pause (2.0)
    show katsu normal flip at Position (xpos=0.1) with easeinleft
    Ka smile flip "Here you go, Amely."
    Ad "What do we say, Amely?"
    Am "Thank you!"
    m "The little dragon attacked her cone with the same ferocity as the last."
    Ka normal flip "Well, I best start packing up my cart and heading back home."
    Ka smile flip "Thank you again for the help."
    Ry normal "Anytime, Katsuharu. We're always here to help if you need."
    Ka exhausted flip "I might have to take you up on that every once and a while."
    Ad "We should also start eating our ice cream before it all melts."
    m "Looking down, pools of the [evalChosenFlavor] ice cream were running down the cone and pooling on my hand."
    Ry "I see a nice spot to sit down over there."
    Ad "Looks good to me, come on Amely!"
    Am "Mhphkay!"
    m "Her mouth was stuffed with ice cream."
    Ka "Wait, [player_name]!"
    c "Yes?"
    Ka smile flip "There's something wrong with your ice cream, let me fix it quickly."
    c "Sure. I'll meet you guys there."
    Ry smile "Alright."
    show amely smnormal flip with dissolvemed
    hide amely with easeoutright
    show remy smile flip with dissolvemed
    hide remy with easeoutright
    show adine normal b flip with dissolvemed
    hide adine with easeoutright
    hide katsu with dissolvemed
    show katsu normal with dissolvemed
    Ka "I wanted to speak privately with you for a moment, [player_name]."
    c "What about?"
    Ka exhausted "Well, it's about my business. If today has taught me anything, it's that I can't do this alone anymore."
    c "What do you mean?"
    Ka "Without you three, there is no way I would be able to serve everybody."
    Ka "And that's never happened before in the forty years I've worked at this cart."
    c "Maybe it was just a busy day."
    Ka "Still. In my prime, I could take on anything."
    Ka normal "I hate to ask more of you. But is it possible that you could try to spread the word that I need help?"
    c "How would I do that?"
    Ka "I'm not quite sure myself. You can say that I pay well."
    c "Hmmm..."
    if not kevinunplayed: #This is kinda dumb tbh
        m "Suddenly, it hit me."
        c "You know what? I think I know the perfect way to help you!"
        Ka "How so?"
        c "I just happen to know a dragon who hands out flyers as a job."
        Ka "Who?"
        c "His name is Kevin. He's passing out flyers as a summer job for his college."
        Ka smile "Why would he help?"
        c "He's a nice guy, and he loves your ice cream."
        Ka normal "Well, if you could get him to help, I would greatly appreciate that."
        c "I'll try."
        Ka smile "Thank you for everything, [player_name]."
        c "Of course, Katsuharu."
    else:
        m "I felt as if I had seen someone who could help us."
        m "I just couldn't remember who it was."
        c "I could help out myself."
        Ka "I can't ask that of you. You've already done so much for me."
        Ka smile "Here, I'll go around every so often and see if I can recruit anyone."
        c "Are you sure?"
        Ka normal "Positive."
        c "Well, quick tip. You might get more people if you agree to pay in ice cream."
        Ka smile "You may be right about that."
    c "Well, I best be going before my ice cream completely melts."
    Ka exhausted "You might be a bit too late."
    m "Looking down, the scoop of [evalChosenFlavor] ice cream had become the consistency of soup."
    Ka smile "Let me get you another."
    c "Thanks, Katsuharu."
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    $ renpy.pause (2.0)
    show katsu normal flip with easeinleft
    show katsu normal with dissolvemed
    Ka "Here you go."
    c "This one somehow looks even better than the last."
    Ka smile "Thank you!"
    c "Well, it's been nice talking to you."
    Ka normal "And you as well, [player_name]. Thank you for everything."
    c "No problem."
    if not kevinunplayed:
        c "And I'll make sure to tell Kevin to help you. I'm sure he will be more than willing to do so."
        Ka exhausted "I hope so."
        Ka smile "Hopefully I'll see you around as well."
        c "I'll be here for a while longer, so count on it."
    scene black with dissolveslow
    m "I walked over to where Remy, Adine, and Amely were sitting."
    scene evalpark1 with dissolveslow
    show amely smnormal at right with dissolvemed
    show remy normal at right behind amely with dissolvemed
    show adine normal b flip at left with dissolvemed
    Ry smile "Sorry, [player_name]. You took so long we had to start eating our ice cream before it all melted!"
    c "No worries. Katsuharu took a bit of time remaking mine as well."
    Ad "Well it shows. That looks like a perfect scoop of ice cream!"
    c "It looks so good I almost don't wnat to eat it."
    Ad giggle b flip "Well, you probably should before it melts."
    c "Good point."
    show adine normal b flip with dissolvemed
    if evalChosenFlavor == "special":
        m "I took a small bite of the special ice cream. Instantly, my face involuntarily contorted into disgust."
        if mp.fish:
            c "Wow, this is just as disgusting as I remember it being."
            Ad giggle b flip "Well, I guess you didn't like it better in ice cream form after all."
        else:
            c "Wow, this is disgusting."
            Ad giggle b flip "Well, I guess you also won't like the special we serve at the diner as well."
        c "You actually like this, Adine?"
        Ad normal b flip "Yeah! I think it's really good!"
        c "I find that hard to believe."
        Ry look "I have to agree with [player_name] here. Ice cream or not, the special is disgusting."
        Ad giggle b flip "Suit yourselves. That just leaves more ice cream for me!"
        Ry "Well, what are you going to do now?"
        Ry normal "I would give you some of mine, but I've already finished."
        c "No worries, Remy."
        c "Ice cream was never really my end goal today. It was hanging out with you guys."
        Ad sad b flip "That's so sweet, [player_name]." #Second wyvern hug? Maybe.
        Ad normal b flip "I had a lot of fun today."
        Ry smile "I guess the ice cream was more of a bonus rather than an end goal."
        Ka "Did I hear an unhappy customer?"
        hide adine with dissolvemed
        show adine normal b at Position (xpos=0.6) behind remy with dissolvemed
        show remy normal at right behind amely with dissolvemed
        show katsu normal flip with easeinleft
        c "How did you know?"
        Ka smile "I have a sixth sense for customer satisfaction."
        m "Katsuharu reached out and handed me a fresh scoop of vanilla."
        c "Wow, thank you Katsuharu!"
        c "What should I do with this scoop of the special, though?"
        Am "Me!"
        Ry look "I'm not sure you would like that flavor very much, Amely."
        Ad giggle b "I'll take it if you don't want it."
        c "Be my guest, Adine."
        Ad normal b "A little bit of extra ice cream never hurt anybody."
        Ka normal "Well, I really best get going now. I have to make more ice cream for tomorrow!"
        show katsu normal with dissolvemed
        hide katsu with easeoutleft
        hide adine with dissolvemed
        show adine normal b flip at left with dissolvemed
        m "Katsuharu winked and returned to his cart."
        Ry look "Do you think he needs help with that?"
        Ad "He looks like he's got it under control."
        Ry normal "Well, [player_name], try the vanilla and see how it is."
        m "Cautiously, I took a small bite of the ice cream."
    else:
        m "I took a small bite of the [evalChosenFlavor] ice cream."
    m "As the cool ice cream dissolved on my tongue, my face lit up in excitement."
    Ad giggle b flip "Now that's the reaction I would expect from Katsuharu's ice cream."
    c "This is really good!"
    m "I quickly devoured the cone, rivaling Amely in speed."
    scene evalpark2 with dissolveslow
    show amely smnormal at right with dissolvemed
    show remy normal behind amely at right with dissolvemed
    show adine normal b flip at left with dissolvemed
    Ad think b flip "It's getting quite late. It's almost Amely's bedtime."
    Ry "I didn't even notice the time! I have work tomorrow!"
    c "I guess this is where we part ways."
    Ad normal b flip "I guess so."
    Ad giggle b flip "But this was a lot of fun. We have to do this sort of thing more often."
    Ry smile "Count me in as well!"
    Ad normal b flip "Alright, Amely, it's time to go!"
    Am "Catch me!"
    hide amely with easeoutleft
    Ad annoyed b flip "Not this again..."
    show adine annoyed b with dissolvemed
    hide adine with easeoutleft
    play sound "fx/takeoff.ogg"
    m "Adine took a few steps and took flight into the air."
    m "After gaining altitude, she tucked in her wings and zeroed in on Amely."
    m "In the next instant, Adine had Amely firmly in her claws and took off towards the orphanage."
    Ry normal "That was entertaining."
    c "Very."
    Ry "Well, I'll take you home."
    c "Thanks, Remy."
    Ry "Your dragon chariot awaits, [player_name]."
    c "A noble steed indeed."
    hide remy with dissolvemed
    play sound "fx/bed.ogg"
    c "I climbed onto Remy's back and we made our way to my place."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (3.0)
    scene evalplayerapt1 with dissolveslow
    play music "mx/campfire.ogg"
    show remy normal with dissolvemed
    Ry "Well, I guess that concludes our day out."
    c "I had a lot of fun."
    Ry smile "So did I."
    if evalOrphanageScore == 2:
        Ry look "I don't think I ever really thanked you for your help at the orphanage earlier."
        c "Don't sweat it."
        if evalSweatJoke:
            Ry smile "[player_name], dragons don't sweat."
            c "Right, I totally forgot."
        else:
            Ry smile "Dragons don't sweat."
            c "Noted."
        Ry normal "I don't think you understand just how much help you really were."
        Ry "That may have been a couple of simple tasks for you, but in my case when your arms are also your legs or wings, those tasks could take days or even weeks." #Shorten this a bit
        c "You know, I didn't think about that."
        c "Although don't go crying to me about cool traits. You can shoot fire and fly."
        Ry smile "I guess you're right, but I've lost track of the amount of times I wish I had opposable thumbs like you or a runner."
        c "I've never had to think about life without them. Back in my world, we don't have the drastic physical variations that you have here."
        stop music fadeout 2.0
        $ renpy.pause (2.0)
        play music "mx/gravity.ogg" #Could possibly change to sadder music
        Ry sad "Sometimes, I wish that were the case here."
        c "How come?"
        Ry shy "People, and especially Emera make fun of me while I'm trying to do my work."
        Ry "It's extremely demotivating when you are constantly belittled by your superior for something completely out of your control."
        Ry sad "I love the library, and I love my job. But my physiology makes me look clumsy and awkward."
        c "Yet you've managed to pull through it for all this time."
        Ry "Without you, I wouldn't have."

        menu:
            "[[Hug Remy]": #Hmm... Liking where this is going, but I'm not sure I'm entierly happy with the message
                play sound "fx/hug.mp3"
                m "I walked up to Remy and wrapped my arms around his body."
                m "He rested his head on my shoulder and wrapped his wings around me."
                m "I felt a single tear drip down his muzzle and onto my arm."
                m "We stood there for a few moments before he rested his wings back on his body."
                Ry shy "Thank you, [player_name]. I really needed that."
                c "You've gone through a lot. Don't let your physical limitations impact you."
                Ry sad "But how? They torment my day to day life."
                c "Do you get any complaints about your work?"
                Ry "When I first started? Many."
                Ry "But over time I've learned how to avoid accidents."
                c "So you're telling me that despite all of the oods being stacked against you, you pushed through?"
                Ry "I guess you can think about it like that, yes."
                c "You didn't let your physical limitations stop you from doing what you loved."
                Ry look "I wouldn't say I love what I'm currently doing."
                c "I think we both know that you didn't take your current job because you loved it."
                c "But what was the real reason you work at the library?"
                Ry shy "To meet you, of course."
                c "Me?"
                Ry "Not you in particular, but a human. I've been so isolated and disconnected, I hardly know any dragons."
                Ry "I thought that maybe I could have a better chance connecting with someone of a different species entirely. Like a fresh start."
                Ry look "I tried with Reza, but since his arrival was a public spectacle, I was never able to really talk with him."
                Ry "With you, it was different. I know I said this before, but it was, and is, truly special being able to talk with you."
                c "Well, I guess your idea worked out quite well in the end."
                Ry "I guess it did. Didn't it?"
                if mp.remyromance:
                    play sound "fx/kiss.wav"
                    m "Suddenly, Remy gave me a big kiss on the lips."
                    Ry shy "Thank you for everything, [player_name]."
                    c "Of course, Remy."
                else:
                    Ry "Thank you for everything, [player_name]."
                    c "Of course, Remy."
                Ry shy "Sorry for putting that emotional burden on your shoulders."
                Ry "I've just kept it brewing inside me for so long I had to get it out."
                c "Don't worry, I'm just happy I could help."
                Ry normal "I best get going before it gets any darker. Night flying isn't really my specialty."
                jump eval_remy_amely_adine_sleep_select
            
            "Nonsense.":
                c "Of course not Remy. You're strong, I know that."
                Ry "Maybe not as strong as you have come to believe [player_name]."
                m "Remy took a deep breath."
                Ry normal "I'm sorry for putting this emotional burden on your shoulders."
                Ry "I've just kept it brewing inside me for so long I had to get it out."
                c "Don't worry about it."
                Ry look "It's getting really late, I should best get going."
                c "I understand. Bye Remy!"
                Ry smile "Bye, [player_name]."
                hide remy with dissolvemed
                play sound "fx/takeoff.ogg"
                m "With that, Remy took off into the starry night sky."
                m "I headed back inside and prepared for bed."
                stop music fadeout 2.0
                scene black with dissolveslow
                return
    else:
        Ry normal "But I should really get going. Night flying really isn't my specialty."
        jump eval_remy_amely_adine_sleep_select

label eval_remy_amely_adine_sleep_select:
    menu:
        "Let him stay for the night.":
            c "Wait, Remy."
            Ry look "What is it, [player_name]?"
            c "You could stay here for the night."
            Ry normal "Really? That sounds wonderful."
            Ry "But where would I sleep?"

            menu:
                "Share the bed.":
                    c "I was thinking that we could share the bed."
                    Ry shy "Oh, well..."
                    c "If you're uncomfortable with that the couch is still available."
                    Ry normal "No, I would love to share the bed with you, [player_name]."
                    if mp.remyromance:
                        Ry shy "Maybe we could even have some fun while we're at it."
                        c "Getting ahead of ourselves I see. Let's see how things go, Remy."
                    $ evalRemyShareBed3 = True

                "Offer the couch.":
                    c "The couch is quite large. You should be quite comfortable on it."
                    Ry "Thanks, [player_name]."

            scene black with dissolveslow
            m "We made our way into the apartment."
            play sound "fx/door/doorchain.ogg"
            scene o3 with dissolveslow
            show remy normal with dissolvemed
            c "Well, here we are. Home sweet home."
            Ry look "This place really hasn't changed much since I was last in here, [player_name]. You've really got to spice it up every once and a while."
            c "I haven't had the time to get around to that. With the whole coma and world saving stuff going on."
            Ry normal "Right, that probably did take up a lot of your free time."
            c "I wonder if they deactivated my ambassador card yet."
            Ry smile "I haven't heard anything about it. You might want to do some last minute furniture shopping before they do though."
            c "Good idea."
            $ renpy.pause (2.0)
            if evalOrphanageScore == 2 and evalCustomerScore == 10 and evalXithReporter and persistent.evalSoloRemyEnding and persistent.evalAmelyEnding:
                scene black with dissolvemed
                m "My vision suddenly went dark."
                scene o3 with dissolveslow
                show remy look with dissolvemed
                show vara smnormal ghost with dissolvemed
                Ry "Are you alright, [player_name]?"
                c "Vara?"
                Ry look "[player_name], what are you talking about?"
                c "Vara... She's next to you, Remy."
                Ry sad "Don't do this to me, [player_name]."
                hide vara with dissolvemed
                c "No, Remy. I just saw Vara. She looked almost like a ghost."
                Ry "Maybe that ice cream isn't sitting well with you."
                c "I saw Vara, Remy. There is no denying that."
                Ry angry "Enough, [player_name]! Her death has hurt us all, especially me."
                Ry "Do you know how many sleepless nights I've had?"
                Ry "I blame myself for her death."
                c "Remy, Vara is still here. She's somewhere."
                Ry sad "What do you mean? She's dead."
                c "I can't explain this."
                Ry look "I have no reason to believe anything you just said."
                Ry "But for some reason, I still believe you."
                Ry sad "Maybe in some other world, Vara is still here with us."
                c "We can only hope, Remy."
                m "Remy took a deep breath and regained his composure."
                Ry normal "Let's go to bed, [player_name]."
                c "Agreed."
                if evalRemyShareBed3:
                    hide remy with dissolvemed
                    m "The two of us made our way to the bedroom."
                    play sound "fx/undress.ogg"
                    m "I got undressed while Remy removed his tie."
                    show remy smile b with dissolvemed
                    Ry "This may surprise you, but a tie isn't the most comfortable sleeping attire."
                    c "Not one bit."
                    hide remy with dissolvemed
                    play sound "fx/bed.ogg"
                    m "The two of us climbed into bed."
                    c "Oof. I don't think this bed was made to fit a human and a big dragon."
                    m "Remy grabbed me and pulled me into his soft embrace."
                    Ry "Is this better."
                    c "You are a very comfortable dragon pillow, Remy."
                    if mp.remyromance:
                        m "Looking up, I found Remy's muzzle was mere millimeters from my face."
                        play sound "fx/kiss.wav"
                        m "I gave the dragon a big kiss."
                        m "He responded by further pressing his lips into my own."
                    c "Remy, please don't blame yourself for Vara's death."
                    c "There is no way you could have thought she would follow you."
                    Ry sad "I can't make any promises. I really feel like I could have done something."
                    c "There was nothing we could do, Remy."
                    c "I'll be here for you. I'm not going anywhere in the foreseeable future."
                    Ry "I hope so. For your sake and mine."
                    Ry "Goodnight, [player_name]."
                    m "I snuggled up closer to Remy."
                    c "Goodnight, Remy."
                    scene black with dissolveslow
                    m "I slowly closed my eyes, Remy's warmth and gentle breathing lulling me to sleep."
                else:
                    hide remy with dissolvemed
                    m "Remy removed his tie and placed it on the desk next to the couch."
                    show remy smile b with dissolvemed
                    Ry "This may surprise you, but a tie isn't the most comfortable sleeping attire."
                    c "Not one bit."
                    hide remy with dissolvemed
                    m "I started making my way to the bedroom, but I called out to Remy before entering."
                    c "Remy, please don't blame yourself for Vara's death."
                    c "There is no way you could have thought she would follow you."
                    Ry sad "I can't make any promises. I really feel like I could have done something."
                    c "There was nothing we could do, Remy."
                    c "I'll be here for you. I'm not going anywhere in the foreseeable future."
                    Ry "I hope so. For your sake and mine."
                    play sound "fx/undress.ogg"
                    m "I undressed and crawled into bed."
                    m "I heard Remy call out from the main room."
                    Ry "Goodnight, [player_name]."
                    c "Goodnight, Remy."
                stop music fadeout 2.0
                $ persistent.evalSecretEndingUnlocked = True

            else:
                c "Why don't we get ready for bed now?"
                m "Remy let out a yawn."
                Ry "I wouldn't mind that."
                if evalRemyShareBed3:
                    hide remy with dissolvemed
                    m "The two of us made our way to the bedroom."
                    play sound "fx/undress.ogg"
                    m "I got undressed while Remy removed his tie."
                    show remy smile b with dissolvemed
                    Ry "This may surprise you, but a tie isn't the most comfortable sleeping attire."
                    c "Not one bit."
                    hide remy with dissolvemed
                    play sound "fx/bed.ogg"
                    m "The two of us climbed into bed."
                    c "Oof. I don't think this bed was made to fit a human and a big dragon."
                    m "Remy grabbed me and pulled me into his soft embrace."
                    Ry "Is this better."
                    c "Much."
                    c "Goodnight, Remy."
                    Ry "Goodnight, [player_name]"
                    scene black with dissolveslow
                    stop music fadeout 2.0
                    m "I slowly closed my eyes, Remy's warmth and gentle breathing lulling me to sleep."
                    return
                else:
                    hide remy with dissolvemed
                    m "I made my way to the bedroom while Remy removed his tie."
                    show remy smile b with dissolvemed
                    Ry "This may surprise you, but a tie isn't the most comfortable sleeping attire."
                    c "Not one bit."
                    hide remy with dissolvemed
                    play sound "fx/undress.ogg"
                    m "I undressed and crawled into bed."
                    m "I heard Remy call out from the main room."
                    Ry "Goodnight, [player_name]."
                    c "Goodnight, Remy."
                    stop music fadeout 2.0
                    scene black with dissolveslow
                    return

        "Let him leave.":
            c "I understand. Bye Remy!"
            Ry smile "Bye, [player_name]."
            hide remy with dissolvemed
            play sound "fx/takeoff.ogg"
            m "With that, Remy took off into the starry night sky."
            m "I headed back inside and prepared for bed."
            stop music fadeout 2.0
            scene black with dissolveslow
            return

label eval_ice_cream_choice: #mp.fish <-- variable for whether player has had the special
    Ka "What flavor would you like?"

    menu:
        "Vanilla":
            $ evalChosenFlavor = "vanilla"
            c "I'll take vanilla please."
            Ka smile flip "Ah, a simple flavor for a refined palette, good choice."
        
        "Chocolate":
            $ evalChosenFlavor = "chocolate"
            c "I'll take chocolate please."
            Ka smile flip "Chocolate, perfect on its own, but even better in ice cream."
        
        "Strawberry":
            $ evalChosenFlavor = "strawberry"
            c "I'll take strawberry please."
            Ka smile flip "You can never go wrong with a bit of berries in your ice cream."
        
        "Mango":
            $ evalChosenFlavor = "mango"
            c "I'll take mango please."
            Ka smile flip "A bit tropical, I like your choice."
            if persistent.adinegoodending and evalCurrentEnding != 3:
                Ry smile "Adine would slap you if she were here."
                c "I know."
            elif evalCurrentEnding == 3:
                Ad think b "That's an interesting flavor choice, [player_name]. Why mango?"

                menu:
                    "Because you're a mango dragon.":
                        c "I felt obligated to get the mango flavor with a mango colored dragon right next to me!"
                        Ad annoyed b "You're not funny, [player_name]."
                        play sound "fx/slap1.wav"
                        if evalAdineSlaps > 0:
                            m "Adine once again flicked her tail and slapped me in the face."
                        else:
                            m "Adine flicked her tail and slapped my face."
                        $ evalAdineSlaps += 1
                        Ry smile "I'm not so sure, Adine. That was pretty funny."
                        play sound "fx/slap1.wav"
                        m "Remy suffered the same punishment as myself."
                        Ry look "Ow!"
                        Ad "I hate you both."

                        menu:
                            "Love you too, Adine.":
                                c "Love you too, Adine."
                            
                            "I guess you could say you're {i}Adone{/i} with this joke.":
                                c "I guess you could say you're {i}Adone{/i} with this joke, Adine."
                                $ evalAdineSlaps += 1
                                play sound "fx/slap1.wav"
                                Ad "I can't believe you just said that."
                                c "Ow! I'm going to have a big, banana shaped bruise on my face tomorrow, Adine."
                                Ad giggle b "Good, you deserve it."
                                c "I probably do..."

                        m "Adine sighed."
                        if evalOrphanageScore == 2:
                            Ad normal b "Ugh. It's hard to stay mad at you when you did so much work at the orphanage."
                        else:
                            Ad normal b "I'll get you back for this. Just you wait."
                    
                    "I wanted something tropical.":
                        c "I just thought that a tropical flavor sounded interesting at the moment."
                        Ad "Are you sure that's the {i}only{/i} reason you choose that flavor?"
                        c "Positive."
                        Ad normal b "I still don't believe you, but I'll let it slide this time."
                
                Ka smile flip "You three are something else."
            
        "Cherry":
            $ evalChosenFlavor = "cherry"
            c "I'll take cherry please."
            Ka smile flip "You know, cherries are my favorite fruit. If you can get around the pit, they are delicious."
        
        'The "Special"' if evalShowSpecialFlavor: #Oh no...
            $ evalChosenFlavor = "special"
            c "I'll take the special, whatever that means."
            Ka smile flip "Ah, probably my most unique flavor."
            c "How so?"
            Ka normal flip "Have you been to our local diner?"
            c "Yes."
            Ka "Have you had the fish special?"

            if mp.fish:
                if evalCurrentEnding == 3:
                    Ad think b "Ummm... [player_name], are you sure you want to have this flavor?"
                    Ka "What's wrong?"
                    Ad normal b "[player_name] had the fish at the diner a little while ago, and I don't think they liked it very much."
                    c "Yeah. It was quite awful."
                    Ka normal flip "Well, with the power of a blender and some ice cream magic, you can now have that wonderful flavor in ice cream form!"
                    c "Yay?"
                    Ry look "That is a little bit... Interesting. I don't remember that being on your menu before."
                    Ka "It's a recent addition."
                    Ka "Well, what do you say, [player_name]?"
                else:
                    c "Oh please, don't remind me."
                    Ka exhausted flip "What? Did you not like it?"
                    c "Lets just say that it... Well... I guess all I can say is that it was quite awful."
                    Ka normal flip "Well, with the power of a blender and some ice cream magic, you can now have that wonderful flavor in ice cream form!"
                    c "Yay?"
                    Ry look "That is a little bit... Interesting. I don't remember that being on your menu before."
                    Ka "It's a recent addition."
                    Ka "Well, what do you say, [player_name]?"
            else:
                c "Can't say I have."
                Ka smile flip "Well, they serve this wonderful fish dish that I loved so much, I decided to blend up and turn into an ice cream flavor!"
                c "Sounds a bit gross."
                Ry look "I would have to agree."
                if evalCurrentEnding == 3:
                    Ad think b "As someone who has served this dish countless times, [player_name], all I can say is that it's not for everyone."
                    c "That's concerning."
                Ka normal flip "It's better than it sounds. I promise. So, what do you say?"
            
            menu:
                "Maybe it's better as ice cream." if mp.fish:
                    c "You know what? Maybe it's better in ice cream form."
                    Ka smile flip "That's the spirit!"

                "I'm feeling adventurous." if not mp.fish:
                    c "You know what? I'm feeling adventurous today, I'll try it!"
                    Ka smile flip "That's the spirit!"

                "Maybe I should rethink my choice.":
                    $ evalShowSpecialFlavor = False
                    show remy normal with dissolvemed
                    jump eval_ice_cream_choice

    if evalCurrentEnding == 1:
        jump eval_solo_remy_2
    elif evalCurrentEnding == 2:
        jump eval_remy_amely_2
    elif evalCurrentEnding == 3:
        jump eval_remy_amely_adine_3