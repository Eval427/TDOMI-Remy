#Things to remember because I forgetful
#PS, as soon as I write this down, I will never forget it because I only forget things when I don't write them down
#Tape measure - If you use it, adine will secretly switch the special and the mango vats, so you get the special

#Changes dialogue for when you arrive at the orphanage
#Incorporate a Vara mood counter for how she reacts? Oh god that sounds not fun
label eval_secret_orphanage_arrival:
    if evalVaraHere:
        Ry "Amely? Are you here?"
        show amely smnormal with easeinright
        show vara behind amely with None
        Am "Hello!"
        Ry smile "Hello, Amely."
    else:
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
    show vara smshocked with dissolvemed
    Am "Uh oh!"
    Ry look "Well, that's not good."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    show remy normal flip behind vara with easeinleft
    show remy normal behind vara
    show amely smnormal flip with easeinleft
    show amely smnormal
    show vara smnormal behind amely
    Ry "I think I know something that we're going to have to do."
    c "Fix the lights?"
    Ry smile "How'd you guess?"
    c "Not sure. Maybe I'm psychic."
    Ry normal "Well, if you're psychic, do you know what else is wrong here?"
    c "I think my powers only work once a day."
    Ry normal "Alright then. From what I can remember, that desk in the middle of the room is very broken."
    c "How'd that happen?"
    Ry look "Learning to control fire or acid breath can be difficult for young dragons."
    Ry "And, well, Vara managed to melt one of the legs of the desk."
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
    Vr "I'll stay here."
    c "It'll be nice to have an extra set of hands, or I guess claws, to help."
    Ry smile "Sounds like a plan. Let's do this!"
    if persistent.evalEndingD:
        play sound "fx/system3.wav"
        s "It turns out you've already played this minigame. Would you like to skip it?"
        menu:
            "Yes.":
                s "Would you like to beat it?"
                menu:
                    "Yes.":
                        $ evalOrphanageScore = 2
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        stop music fadeout 2.0
                        scene black with dissolveslow
                        $ evalReplaceBulbs = True
                        $ evalResetBreaker = True
                        scene evalorphlight with dissolveslow

                    "No.":
                        $ evalCustomerScore = 1
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        stop music fadeout 2.0
                        scene black with dissolveslow
                        scene evalorphdark with dissolveslow

                show remy normal
                show vara smnormal
                show amely smnormal
                with dissolvemed
                jump eval_everyone_1
            
            "No.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                pass
    show remy normal behind vara with dissolvemed
    jump eval_secret_orphanage_game_init

label eval_everyone_sleep:
    Ry "Well, here we are!"
    $ renpy.pause (1.0)
    if evalVaraHere:
        Ry "Amely? Are you here?"
        show amely smnormal with easeinright
        show vara behind amely with None
        Am "Hello!"
        Ry smile "Hello, Amely."
    else:
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
    Ry normal "I see that, Vara. I wonder who turned the lights off. Usually we leave them on for you."
    c "Wait, is the orphanage just a classroom?"
    Ry look "Sadly, this is most of the space that the orphans get. They play, learn, study, and eat in here or outside for most of the day."
    c "Where do they sleep?"
    Ry normal "Oh, we have some small bedrooms for them down the hall."
    Ry "At the moment the council has it completely closed off."
    c "Is that for any particular reason?"
    Ry "Not exactly. They probably don't want random dragons just waltzing in and taking the childrens' beds."
    c "That makes sense. So where do Amely and Vara sleep?"
    Ry "Adine is letting Amely sleep with her overnight and Vara is actually staying overnight with me."
    Ry smile "At this point, Amely is spending so much time with Adine that it already looks like they're a family."
    c "That sounds adorable."
    Ry normal "I do hope she considers adoption at one point."
    c "Are you considering adoption as well?"
    Ry "Possibly."
    Ry "Anyways, let's turn on the lights."
    c "I see."
    Ry "Here. Let's turn on the lights."
    hide remy with easeoutleft
    Am "I come!"
    hide amely with easeoutleft
    m "Remy walked over to the corner of the room and flicked the lights on."
    play sound "fx/lightswitch.mp3" #Increase the loudness of the audio
    $ renpy.pause (1.0)
    play sound "fx/lightbreak.mp3"
    $ renpy.pause (2.0)
    show vara smshocked with dissolvemed
    Am "Uh oh!"
    Ry look "Well, that's not good."
    play sound "fx/lightswitch.mp3"
    $ renpy.pause (2.0)
    play sound "fx/ligtswitch.mp3"
    $ renpy.pause (2.0)
    show remy look flip behind vara with easeinleft
    show remy look behind vara with dissolvemed
    show amely smnormal flip with easeinleft
    show amely smnormal with dissolvemed
    show vara smnormal with dissolvemed
    Ry "I guess the lights in the building are out."
    c "It's a shame we couldn't help with that earlier."
    Ry normal "Hey, I'm just glad you're alright. You didn't look so hot back there."
    c "I guess now all there is to do is wait for Ad..."
    stop music fadeout 2.0
    jump eval_everyone_1

label eval_everyone_1:
    play sound "fx/wooshes.ogg"
    $ renpy.pause (3.0)
    Ry smile "I wonder who that could be?"
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)
    show remy normal at right
    show vara smnormal at right
    show amely smnormal at right
    with move
    show adine normal c flip behind amely at left with easeinleft
    
    if persistent.evalD1Skip:
        $ renpy.pause (0.5)
        play sound "fx/system3.wav"
        call syscheck from evalSysCheckD1
        call skiptut from evalSkipTutD1
        if skipbeginning == False:
            if system == "normal":
                s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip to the end?"
            elif system == "advanced":
                s "It looks like you've seen this before. Skip to the end of this scene?"
            else:
                s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the end of this scene."

        $ skipbeginning = False

        menu:
            "Yes. I want to skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                show black with dissolvemed
                $ renpy.pause (1.0)
                $ persistent.skipnumber += 1
                call skipcheck from evalSkipCheckD1
                play music "mx/funness.ogg"
                $ evalAdineSlaps += 1
                jump eval_skip_D1

            "No. Don't skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

    play music "mx/cruising.ogg"
    Ad "Hey you guys how's it g{nw}"
    Am "Adine!"
    show amely smnormal at left with move
    m "The little dragon ran up to Adine and gave her a big hug."
    show amely smnormal flip at left with dissolvemed
    Ad giggle c flip "Hello, Amely. you're acting like I just came back from a long trip when I just saw you this morning."
    Am "I missed you!"
    play sound "fx/undress.ogg"
    show adine giggle b flip with dissolvemed
    Ad normal b flip "Anyways, hey guys! What are you doing here?"
    Ry "Looking for you!"
    Ad giggle b flip "Well, I guess you found me, or rather, I found you."

    if not evalReplaceBulbs or not evalResetBreaker:
        Ad think b flip "Hey, Remy. Why are the lights turned off?"
        Ry look "Well... they're broken."
        Ad sad b flip "Oh, Poor Amely and Vara. They were stuck in the dark all this time?"
        Am "Dark!"
        Vr smnone "Very dark."
        Ad "Oh, I'm so sorry you two. I didn't know."
        Ry "I wouldn't worry too much, Adine. They both seem quite alright."
        Ad disappoint b flip "I guess..."
        show vara smnormal at right with dissolvemed
    
    if evalOrphanageScore == 2:
        Ad think b flip "Wait a minute..."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine think b flip with dissolvemed
        Ad giggle b flip "What did you guys do? The orphanage looks amazing!"
        Ry "Well, [player_name] and I wanted to surprise you by cleaning up the place a little bit."
        show adine think b with dissolvemed
        $ renpy.pause (0.5)
        show adine giggle b flip with dissolvemed
        $ adinestatus="good"
        Ad "This isn't real. My eyes are deceiving me."
        c "You don't believe us?"
        Ad normal b flip "Are you kidding me? This place hasn't looked this good in years!"
        Ad "How did you two manage to do all of this so quickly?"
        Vr "Hey! We helped!"
        Am "Yeah!"
        Ad giggle b flip "I'm sorry. How did you {i}four{/i} manage to do all of this so quickly."
        Ry normal "Teamwork. Amely and I gathered supplies while [player_name] and Vara did all the handiwork."
        Ad normal b flip "You do not understand how grateful I am that you did this."
        hide adine with dissolvemed
        play sound "fx/hug.mp3"
        m "Adine walked up and gave me a big hug." #The wyvern gives you a hug. Mission complete.
        m "With wings as arms, I was engulfed completely."
        play sound "fx/hug.mp3"
        m "She then walked over to Remy and repeated the process."
        show remy shy behind vara at right with dissolvemed
        Am "Me! Me!"
        Vr smsmile "Me too!"
        hide adine with dissolvemed
        hide amely
        hide vara
        with dissolvemed
        play sound "fx/hug.mp3"
        m "Adine got down on her knees and completely hid the two little dragons within her wings."
        show adine normal b flip at left
        show amely smnormal flip at left
        show vara smsmile at right
        with dissolvemed
        Ad "Now, I know the real reason you came here wasn't just to clean up the place."
        c "Alright you caught us."
        Ad "What was your real motive, then?"
        Ry normal "Hey! We wanted to surprise you by cleaning up the place as well."
        Ad giggle b flip "I'm just messing with you guys."
    elif evalOrphanageScore == 1:
        Ad "Wait... Did you guys do something here?"
        Ry smile "Well, [player_name] and I did a bit of work while we were waiting for you."
        if adinestatus != "good":
            $ adinestatus = "neutral"
        Ad "Really? That's so kind of you! What were you waiting on me for?"
    else:
        Ad normal b flip "I expected to find you here Remy, but what is [player_name] doing here?"
    c "We have come to offer you the deal of a lifetime."
    c "Free ice cream from the world renowned Katsuharu!"
    if adinestatus != "good":
        $ adinestatus = "neutral"
    Ad giggle b flip "Can't say I expected that."
    Ad think b flip "I have never heard of that dragon giving anyone free ice cream."
    Ad "You must have done something quite spectacular to get a deal like that."
    c "Just a little bit of business advice. I told him to move his stand down to Tatsu Park."
    Ad "That's it?"
    c "Does there need to be more?"
    Ad normal b flip "I guess not. Count me in."
    Ry smile "That's great! This is going to be fun!"
    Ad giggle b flip "Two dragons, a human with a big appetite, and two little hatchlings with unlimited access to delicious ice cream. I sure hope Katsuharu has enough stock."
    c "We couldn't possibly eat {i}that{/i} much ice cream, could we?"
    Ad normal b flip "Coming from someone who has had three scoops in one sitting, it is definitely possible."
    Ry normal "So, Amely and Vara, are you excited to have your first ever scoop of ice cream?"
    Vr "Ice cream!"
    Am smsad flip "Ice cream?"
    c "Well, Amely. Ice cream is kind of like... Well... Um..."
    m "I didn't think it would be so difficult to describe something as simple as ice cream."
    Vr "Soft, frozen dessert!"
    c "Yes, Vara described it perfectly."
    m "Vara gave us a proud expression."
    Vr "I read about it in a book!"
    c "Have you tried it before?"
    Vr smnone "No..."
    Ry "Well, I'm sure you'll love it, Vara."
    Vr smsmile "Okay."
    m "Amely still didn't look completely sold on the idea of ice cream."
    Am "Sugar?"
    c "Yes, lots of sugar."
    Am smnormal flip "Sugar!!!"
    if evalOrphanageScore != 2:
        Ry look "What about the orphanage, Adine?"
        Ad normal b flip "We can do the maintenance work any time we want. I don't know how many other opportunities these two little dragons would get to experience something like this."
        Ry normal "Good point."
    Ad think b flip "Wait a minute."
    Ad "How are we supposed to get over to Tatsu Park?"
    Ad "I can fly Amely over, but how are [player_name] and Vara going to make it there in a reasonable amount of time?"
    Ry normal "They could just ride on my back."
    Ad giggle b flip "What are you? A dragon shuttle?"
    Ry smile "I charge my clients in ice cream."
    Ad "What a coincidence."
    Ry normal "Quite the coincidence indeed."
    Ad normal b flip "Alright, Amely, let's go."
    Am "Sugar!!!"
    hide amely with easeoutright
    play sound "fx/door/door_open.wav"
    $ renpy.pause (0.5)
    Ad "Whoah! Wait for me, Amely! I'm the one with wings here!"
    hide adine with easeoutright
    $ renpy.pause (1.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.5)
    play sound "fx/takeoff.ogg"
    m "After a moment, Adine caught up with Amely. Clutching the little hatchling in her claws, she took off and soared into the air."
    if not evalRodeRemy:
        Ry "Before you say anything, we are not going to take another scenic walk back to Tatsu Park."
        c "Damn, but it was so pretty coming over here!"
        Ry "I don't want to arrive at the park carrying a passed out human on my back. I think I would get a lot of strange looks from other people."
        c "Fine."
    Ry normal "Well, are you two ready?"
    Vr "Yes!"
    c "Sure am."
    hide remy
    hide vara
    with dissolvemed
    play sound "fx/bed.ogg"
    m "Remy lowered his body."
    m "Making sure not to mess up his tie, I carefully hopped onto his back. He folded his wings back to give me as much room as possible."
    m "Vara sat on her hind legs and stretched her arms towards me. I lifted her up and placed her in front of me on Remy's back."
    Ry "How is it back there?"
    Vr smsmile "Fun!"
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
    m "Even with Vara in front of me, I managed to slip in the key and lock the door."
    c "How do I get the key back under the pot?"
    Ry "Like this."
    m "Remy walked over to the pot and tilted it up with his muzzle."
    m "I put the key back, and he carefully rested the pot back in it's upright position."
    Ry "Perfect! Let's go!"
    if evalRodeRemy:
        m "Remy walked forward and quickly picked up speed."
        m "As a seasoned dragon rider. I sat back and gazed up at the sky, gently holding onto Vara to keep her safe." #Is this too... weird?
    else:
        m "Remy then slowly started walking forward, picking up speed surprisingly quickly."
        m "It wasn't as uncomfortable as I had first imagined."
        m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
        if evalRodeBryce:
            m "In a way, it also felt strangely familiar, like I had done this before."
            m "The experience was almost relaxing, with the light breeze and rhythmic thumping of Remy's feet on the grass and pavement."
            m "I gently held onto Vara to keep her safe as I watched the dragon world pass by me."
        else:
            m "It wasn't as uncomfortable as I had first imagined."
            m "It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "I gently held onto Vara to keep her safe as I watched the dragon world pass by me."
        m "I sat back and gazed up at the sky, gently holding onto Vara to keep her secure on Remy's back."
    $ renpy.pause (0.5)
    m "It seemed as if it took mere minutes to arrive back at Tatsu Park."
    Ry "Ladies and gentlemen, this will be our final stop. Please make sure to grab all of your belongings and safely exit the vehicle."
    if not evalBadRemyJoke:
        c "Very funny, Remy."
        Ry "Thanks, I can tell that you sincerely mean that."
    else:
        c "Saying the same joke twice doesn't make it funnier, Remy."
        Ry "Nonsense."
    play sound "fx/bed.ogg"
    m "I gracefully slid off of Remy's back."
    m "I then grabbed Vara and gently rested her on the ground."
    show remy normal
    show vara smnormal
    with dissolvemed
    play music "mx/funness.ogg"
    if evalRodeRemy:
        c "That was fun! I should ride you around more often!"
    else:
        $ evalRodeRemy = True
        c "Damn, why didn't I just ride you over to the orphanage as well. That was fun!"
    $ evalRodeRemy = True
    Ry smile "Wow, [player_name], I didn't know you wanted to ride me so badly."
    m "My face turned bright red."
    Ry "You look like a tomato."
    c "I'll get you back for this, Remy."
    Ry "I'm sure you will."
    m "I spotted Adine and Amely walking over to us."
    show remy normal at right
    show vara smnormal at right
    with move
    show amely smnormal flip at left
    show adine normal b flip behind amely at left
    with easeinleft
    Ad "Took you three long enough to get here."
    Ad giggle b flip "I don't suppose you had to make any other stops or pick up any more passengers on your way over here, Remy."
    Ry "Nope. We just had to lock up the orphanage on our way out."
    Ad normal b flip "So, you said Katsuharu relocated here. Any idea where he is?"
    c "He didn't give me an exact location..."
    menu:
        "[[Make a banana phone joke.]":
            m "Suddenly, inspiration struck me as Adine idly moved her tail in my direction."
            c "Not sure, Adine. Why don't we call and find out?"
            m "I stepped and grabbed the end of Adine's tail."
            Ad think b flip "What the..."
            Ry look "[player_name], what are you doing?"
            m "I held the crescent moon end of Adine's tail up to my ear like a telephone."
            c "Hey, is this Katsuharu? We were just wondering where you set up for the day."
            Ry smile "Ah, the ol' banana phone."
            Ad annoyed b flip "This is so unbelievably stupid."
            Vr smsmile "Banana phone!"
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
            Ad normal b flip "Oh no indeed."
            Am "Ice cream?"
            Ry "I almost forgot about the ice cream! We should probably go before Katsuharu closes up for the day."
        "There's a long line of dragons over there.":
            c "Maybe he's at the front of that line of dragons over there. What else would they be lining up for?"
            Ad giggle b flip "I don't think anyone would want to wait in a line that long if anything but ice cream was at the other end."
    scene black with dissolveslow
    m "We made our way to the end of the line of dragons I had seen earlier."
    scene town2 with dissolveslow
    show vara smnormal at right
    show remy normal behind vara at right
    show amely smnormal flip at left
    show adine normal b flip behind amely at left
    with dissolvemed
    Ry "Wow! This is quite the line!"
    c "I think my advice has paid off for him after all."
    Ry smile "It seems so."
    Ad "So, are we planning on waiting in line with everyone else?"
    Ad think b flip "I would think that Katsuharu would be alright letting his special customer cut in line."

    menu:
        "It would be rude to skip everyone.":
            c "It would be rude to skip everyone."
            Ry normal "I would have to agree with you. All of these people have been waiting for a long time to get their ice cream, and I'm sure it would make them unhappy if we just skipped ahead."
            Ad think b flip "I'm not too sure."
            Ad "If Katsuharu was willing to give you free ice cream, I'm sure he would be more than willing to let you skip the line as well."
            Ry normal "It's not that. I just don't want to attract too much attention to ourselves."
            Ad normal b flip "I guess."
            c "Looks like the line is about an hour long." #Do I add a mini game??? Tune in next time for //Is Eval Lazy?\\ Yes I am no minigame for you.
            m "For a few minutes, Remy, Adine and I engaged in lighthearted chatter, discussing the events that had gone on while I was in my coma."
            show amely smnormal at left with dissolvemed
            hide amely with easeoutleft
            m "However, our conversation was rudely interrupted when I noticed Amely running off."
            c "Ummm, Adine? Where is Amely going?"
            Ad annoyed b flip "Good question. I'll go grab her."
            show adine annoyed b with dissolvemed
            hide adine with easeoutleft
            Ry "Well, what do we do now?"
            c "Why not talk more?"
            Ry look "I think I'm fresh out of topics."
            Vr smnone "I talk."
            Ry normal "What about?"
            Vr smsmile "Cooking!"
            c "Go ahead, Vara. We're all ears."
            show vara smnone with dissolvemed
            m "At first, her words came out nervously, and she was almost inaudible."
            show vara smnormal with dissolvemed
            m "However, as she continued, she spoke with more clarity and confidence."
            m "By the time we reached the front of the line, I felt like a chef."
            show adine normal b flip at left
            show amely smnormal flip at left
            with dissolveslow
            Ad "We're back."
            Ry "Just in time too, I think it's our turn."
        
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
    
    label eval_skip_D1:
        pass
    $ persistent.evalD1Skip = True
        
    scene town7 with dissolveslow
    show amely smnormal at right
    show vara smnormal behind amely at right
    show remy normal behind vara at right
    show adine normal b behind remy at Position (xpos=0.6)
    with dissolvemed
    show katsu normal flip at Position (xpos=0.1) with easeinleft

    Ka "Well, if it isn't the business saving human, [player_name]! What brings you here today?"

    menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while, hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it."
            c "Hopefully it should all return back to the peaceful way it was."
            c "Everything has more or less resolved itself and the conflict is over."
            Ka smile flip "Glad to hear that."
            c "Is it alright if I brought these four along as well?"
            Ka exhausted flip "Wow... When I offered you that ice cream, I didn't think you would bring all of your friends as well."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka "Hmmm..."
            Ka smile flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this?"
            Ka "You four get as much ice cream as you want. But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream."
            Ad normal b "It might even be fun."        
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right behind amely
            show adine annoyed b at Position (xpos=0.6) behind remy
            with dissolvemed
            Ka smile flip "Well, I guess I can't blame you for the enthusiasm."
            Ka normal flip "I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry normal "I... guess I do remember being quite excited that day."
            Ka "I also remember Adine's first time as well."
            Ad giggle b "You do?"
            Ka "Of course. You really, really wanted three cones that day."
            Ka "It was quite entertaining watching you hop away on one foot while holding ice cream in your hands and other foot."
            Ad "I remember getting a lot of strange looks from other dragons that day."
            Ry smile "I think I remember that too. Didn't you almost fall?"
            Ad annoyed b "Of course I didn't. My feet are very dextrous. Walking on one foot isn't a big deal."
            Ry normal "How sanitary is holding ice cream with your feet though, Adine?"
            Ad normal b "I was a kid, you really think I was worrying about something like that?"
            Ka "Well, enough about embarrassing childhood memories. [player_name], when I gave you that offer for ice cream, I didn't expect you to bring all of your friends."
            Ry look "Listen, Katsuharu. If it's too much, just give [player_name] their ice cream."
            Ka normal flip "You know, not once in my time working this cart have I ever left a potential customer hungry."
            Ka "How about this? You four get as much ice cream as you want."
            Ka "But first, you have to help me serve some customers for a while."
            Ry normal "That doesn't sound that bad."
            Ad think b "Yeah, I honestly wouldn't mind doing that for some ice cream. It might even be fun."
    Vr smsmile "I want to make ice cream!"
    Am "Ice cream!"
    Ry "I guess it's really up to you, [player_name]. This was your idea after all."
    
    menu:
        "[[Help out Katsuharu]":
            c "You really think I would leave you guys like that? Of course we can help you, Katsuharu."
            show remy normal at right behind amely
            show adine normal b at Position (xpos=0.6) behind remy
            with dissolvemed
            Ka exhausted flip "Thank goodness. Today has been quite rough, and It'll be nice to have some extra hands and claws."
            Am "Ice cream?"
            Ry smile "Soon, Amely. First we have to help serve it."
            Am smsad "Why?"
            Ad giggle b "Because then you get two scoops of ice cream instead of one!"
            Am smnormal "More sugar?"
            Ad normal b "Yes, much more sugar."
            Am "I help! I help!"
            Ka excited flip "That's the spirited staff I'm looking for! Let's get to work!"
            m "The five dragons made their way behind the cart. I followed closely behind."
            show katsu normal with dissolvemed
            hide katsu with easeoutleft
            hide adine with easeoutleft
            hide remy with easeoutleft
            hide vara with easeoutleft
            hide amely with easeoutleft
            $ renpy.music.set_pause(True, "music")
            scene black with dissolveslow
            scene evalkatsucart with dissolveslow
            if persistent.evalEndingD:
                play sound "fx/system3.wav"
                s "It turns out you've already played this minigame enough. Would you like to skip it?"
                menu:
                    "Yes.":
                        s "Would you like a perfect score?"
                        menu:
                            "Yes.":
                                $ evalCustomerScore = 10
                                $ evalReplaceBulbs = True
                                $ evalResetBreaker = True

                            "No.":
                                $ evalCustomerScore = 5
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        stop music fadeout 2.0
                        scene black with dissolveslow
                        scene evalkatsucart with dissolveslow
                        jump eval_everyone_2
                    
                    "No.":
                        play sound "fx/system3.wav"
                        s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                        pass

            Ka normal "Before we start, would you mind if I put on some music for us to listen to? I have a small cassette player in my cart that I use to pass the time."

            menu:
                "Sure.":
                    stop music
                    $ renpy.music.set_pause(False, "music")
                    c "Sure! I'd love to listen to some of your music!"
                    Ka smile "Great! I've got some amazing stuff here!"
                    $ evalKatsuMusic = True
                    queue music ["mx/cassette.mp3", "mx/cozysnail.mp3", "mx/neonlights.mp3", "mx/nurture.mp3", "mx/tunnel.mp3"]
                    m "With a soft click, Katsuharu slid a cassette into the player and hit play."
                    Ka "How's that?"

                    menu:
                        "I like it!":
                            c "You have good taste in music, Katsuharu."
                            Ka "Thanks!"
                        
                        "Actually, why don't we turn it off.":
                            c "Sorry, Katsuharu, but I think that might distract me while I work."
                            Ka "It's okay! I understand."
                            stop music fadeout 2.0
                            m "Katsuharu reached down and paused his cassette player."
                            play sound "fx/system3.wav"
                            s "Back to your regularly scheduled programming."
                            play music "mx/funness.ogg"
                            $ renpy.pause (2.0)
                            s "Actually, why not go even further? Would you like to play this minigame out in complete silence?"

                            menu:
                                "Yes.":
                                    s "Well, this is going to be awkward, but suit yourself."
                                    stop music fadeout 2.0
                                
                                "No.":
                                    s "Good choice."
                
                "No thanks.":
                    c "Sorry, I don't feel like listening to anything at the moment."
                    Ka normal "No problem."
                    $ renpy.music.set_pause(False, "music")

            Ka normal "Alright, here's the plan everyone."
            Ka "Remy, grab a scoop from that drawer there."
            Ry normal "Yes, sir!"
            Vr smsmile "Can I make it too?"
            Ka smile "Of course you can, Vara. Grab a scoop as well."
            Ka "[player_name], you take orders."
            Ka "And Adine... {w}Just make sure Amely doesn't cause too much chaos."
            Ad giggle b "Sounds good, Katsuharu."
            Ka "Quick tip, [player_name]. Customers don't always want the same thing. Try adapting to their interests."
            c "Seems simple enough."
            jump eval_katsu_help_init

        "[[Enjoy your ice cream alone]":
            $ adinestatus = "bad"
            $ remystatus = "bad"
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
            Vr smsad "..."
            show remy sad flip with dissolvemed
            show vara smsad flip with dissolvemed
            show amely smsad flip with dissolvemed
            hide remy with easeoutright
            hide vara with easeoutright
            hide amely with easeoutright
            m "With his head hung low, Remy walked away with Amely and Vara."
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
            play sound "fx/system3.wav"
            s "Wow, that was mean!"
            play sound "fx/system3.wav"
            s "How could you be so selfish?"
            $ evalFail = "Selfish"
            jump eval_fails

label eval_everyone_2:
    m "I looked out across the park. It seemed that every dragon had gotten their share of ice cream."
    c "I think we're done, guys!"
    stop music fadeout 2.0
    scene black with dissolveslow
    scene town7 with dissolveslow
    $ renpy.pause (1.0)
    show katsu normal flip at Position (xpos = 0.1)
    show vara smnormal at right
    show remy normal behind vara at right
    with dissolvemed
    play music "mx/jazzy2.ogg"
    Ka excited flip "Wonderful job, everyone!"
    Ka smile flip "Especially you, Vara. You really have a knack for scooping ice cream."
    Vr smnone "..."
    Ka normal flip "Is everything alright?"
    Ry smile "I think she's just excited. She loves this sort of stuff."
    Ka "Well, Vara, you can always come by whenever you want to help out."
    Ka smile flip "I could even teach you how to make the ice cream as well."
    m "Vara looked longingly at Remy."
    Vr smnormal "Can I come help again?"
    Ry normal "Of course you can, Vara!"
    show vara smsmile with dissolvemed
    c "You know, Katsuharu, Vara may be the perfect candidate for a successor to your business."
    Ka "You know what? You're right."
    Ka normal flip "She's a bit young, but I'm sure she would learn fast."
    Ry "Well, I'm sure she would be more than willing to learn from you. Right, Vara?"
    Vr "Yes!"
    if evalCustomerScore == 10:
        Ka smile flip "[player_name], you also did a wonderful job serving everyone. I don't think I saw a single unhappy customer!"
        c "Thanks, Katsuharu, but I couldn't have done it without you three as well."
    elif evalCustomerScore > 6:
        Ka normal flip "Great job serving everyone, [player_name]. I saw a lot of happy customers walking off."
        c "Thanks, Katsuharu."
    else:
        Ka normal flip "You did well serving everyone, [player_name]. There were a few happy customers I saw walking off."
        c "Thanks, Katsuharu."
    c "Wait a minute, where are Adine and Amely?"
    Ry normal "Look up."
    m "I looked up towards the sky. It took a second, but I found Adine flying in circles with Amely in her claws."
    Ry "Hold on, let me grab them."
    show remy normal flip with dissolvemed
    hide remy with easeoutright
    play sound "fx/takeoff.ogg"
    m "Remy took a few steps, then flew into the air."
    m "He caught up to Adine, and the two hovered in place for a moment before landing next to Katsuharu and I."
    show remy normal behind vara at right with easeinright
    show amely smnormal behind remy at Position (xpos = 0.6)
    show adine normal c behind amely at Position (xpos = 0.6)
    with easeinright
    Ad normal b "Hey guys! Did you have fun?"
    Vr "Yes!"
    Ry "I thought it was fun."
    c "It was a lot of work, but in a way, it was also nice talking to all the locals."
    Vr "And the big dragon wants me to make more ice cream!"
    Ad giggle b "His name is Katsuharu, Vara."
    Vr smnone "Sorry."
    Ka "No worries! A lot of people have trouble with my name."
    Vr smnormal "Katsuharu!"
    Ka smile flip "Well, you got it first try!"
    show vara smsmile with dissolvemed
    m "Vara nodded proudly."
    Ka normal flip "Although I must say, I think Adine had the hardest job here."
    Ad annoyed b "Ugh. It's impressive just how much chaos such a small little dragon can cause."
    show amely smnormal at left with move3
    Ad annoyed b "Amely, where do you think you're going?"
    Am "Hehe."
    hide amely with easeoutleft
    Ad frustrated b "I take my eyes off her for one second and she runs off."
    hide adine with easeoutleft
    Ry "And there they go again."
    Ka normal flip "Amely seems like quite the troublemaker."
    Ry look "She isn't normally this energetic and usually doesn't cause this much trouble."
    Ry normal "I think the idea of ice cream and being out with all of us has gotten her very excited."
    m "Adine returned with Amely's hand firmly grasped within her claw."
    show adine annoyed b flip behind remy at Position (xpos = 0.6) 
    show amely smnormal flip behind remy at Position (xpos = 0.6)
    with easeinleft
    show adine annoyed b behind amely at Position (xpos = 0.6) 
    show amely smnormal behind remy at Position (xpos = 0.6)
    with dissolvemed
    Ad "Sorry, I had to save Katsuharu's ice cream from this hungry little dragon."
    Am "Ice cream!"
    Ka smile flip "Well, how about I start serving you five your ice cream. You deserve it after all."
    Ry smile "I'm sure Adine could use a bit after chasing Amely around all day."
    Ad normal b "You say that sarcastically, but that's exactly what I need at the moment."
    Am "Ice cream!"
    Ad giggle b "And maybe a bit of sugar will calm this little dragon down."
    Ry normal "I doubt it."
    Ad normal b "So do I."
    Ka normal flip "Let's start with [player_name]."
    $ evalAdineTrick = False
    jump eval_ice_cream_choice

label eval_everyone_3:
    Ka "One scoop of [evalChosenFlavor] coming right up!"
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "The dragon walked behind his stand and started preparing the ice cream."
    m "Expecting the dragon to produce some sort of utensil, I was surprised when he suddenly thrust his hand into the vat and pulled out an almost perfectly spherical scoop of ice cream."
    c "(Damn, these dragons can fly, shoot fire, run extremely fast, and even make an amazing scoop of ice cream with their bare hands. This truly is the peak of evolution.)"
    Ka "Y'know, most ice cream vendors use some sort of scoop. But over the years, you learn that your bare hands are faster and more efficient than any of those stupid tools." #Might be a bit pointless to have this
    c "Don't you walk using your hands?" #Hands, claws, feet, I'm very confused at this point
    Ry look "You know, I never really thought of that."
    Ka "Well, I wash my hands before serving the ice cream, of course! I have a little station behind here and everything."
    c "(That's good to hear. I was worried for a moment.)"
    show remy normal behind vara with dissolvemed
    if evalChosenFlavor == "spaghettieis":
        m "With his other hand, Katsuharu grabbed a cup and ducked below his cart, tinkering with some sort of machine."
        c "(That must be the spaetzle, or whatever it was called.)"
        m "After a few moments, the dragon reappeared behind his cart, the cup full of what appeared to be ice cream in the shape of noodles."
        m "He reached under his cart once more, revealing a large bottle of an opaque, red syrup, and added a healthy portion to the cup."
        m "As a final touch, Katsuharu garnished the dessert with coconut shavings."
        m "He added a spoon and handed the cup over to me."
        show katsu smile flip at Position (xpos = 0.1) with easeinleft
        Ka "Here you are!"
    else:
        m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top."
        c "Interesting, those cones look exactly like the ones back in my world."
        show katsu excited flip at Position (xpos = 0.1) with easeinleft
        Ka "But I am sure they don't taste half as good as mine!"
        m "Katsuharu then handed me the cone, topped with the [evalChosenFlavor] ice cream."
        show katsu smile flip with dissolvemed

    if evalChosenFlavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color."
    elif evalChosenFlavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif evalChosenFlavor == "strawberry":
        m "The strawberry ice cream almost looked like a mix between the cherry and vanilla with its soft, pink color."
    elif evalChosenFlavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif evalChosenFlavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif evalChosenFlavor == "special":
        m "The special had a color uncomfortably close to the color of a mango."
        if mp.fish:
            c "(Why does fish translate to yellowish orange in ice cream form?)"
        else:
            c "(What kind of special menu item has this yellowish orange hue?)"

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

            m "Remy sighed."
            if persistent.adinegoodending and evalCurrentEnding < 3:
                Ry "First with Adine, now with me."
                c "Yep, you can't escape it."
            elif evalCurrentEnding > 2:
                Ry "I guess you could think about it like that."
                Ad giggle b "See, Remy? I'm not the only one who thinks that!"
                c "Am I missing something?"
                Ad normal b "When we used to get ice cream as kids, everyone would always call Remy the 'Vanilla Dragon'."
                Ry "Yes, a name I would like to leave in the past."
                Ad "Too late, Remy. [player_name] brought it back to light."
            else:
                Ry "I guess you could think about it like that."
        
        "Good choice.":
            c "Good choice."
            Ry normal "Thanks!"
            Ry "In my opinion, vanilla is the tried and true classic. You can't go wrong with it."

    Ka normal flip "Alright, Adine, I'll take your order as well."
    if evalChosenFlavor == "special":
        Ad normal b "I'm curious to try the 'special' with [player_name]."
        Ka "Good choice! I think you'll like it."
        Ad "I've served the dish enough times. I'm curious to see how it is as ice cream."
        Ka smile flip "Much better. I promise."
    elif evalAdineTrick:
        Ad "You know what? I made all that fuss, but I think I'll have the mango ice cream as well."
        c "Mango ice cream for a mang...{nw}"
        Ad frustrated b "Stop."
        c "Point taken."
        Ad normal b "Good."
    else:
        Ad normal b "I think I'll try the 'special'."
        Ka "Good choice! I think you'll like it."
        Ad"I've served the dish enough times. I'm curious to see how it is as ice cream."
        Ka smile flip "Much better. I promise."
    Ka "Just give me a moment to get you your scoops!"
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    show amely smnormal behind remy at Position (xpos = 0.6) with dissolvemed #Fix this it's ugly and broken
    m "I watched as Katsuharu repeated the process for Remy and Adine's cones."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    m "With some difficulty, Katsuharu managed to waddle back over to us on his back legs."
    Ka "Here you go."
    m "Adine and Remy graciously took their ice cream from Katsuharu."
    Ka "Years of experience have taught me how to stand on my hind legs to serve two scoops of ice cream."
    Ka smile flip "I'm not graceful, but at least I can do it at all."
    Ry smile "I don't know, Katsuharu, I doubt I could look as good as you doing that."
    Ka "Maybe so."
    Ka normal flip "Anyways, Amely, you're next. What would you like?"
    Am "I want..."
    Am "Ummm..."
    Am smsad "..."
    Ry smile "I think she may be a bit overwhelmed with all of the different flavor choices."
    Ry normal "How about we get her some chocolate?"
    Ka "I'm sure she will be quite happy with that choice, Remy."
    Ka smile flip "And last but not least my little assistant confectioner."
    Vr "I want the cherry, please."
    Ka normal flip "I think I could make that happen for you."
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "Katsuharu went back to his stand and made cones for Vara and Amely."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Here you go little ones."
    m "The two dragons grabbed their cones. Amely looked at her own in wonder, while Vara meticulously inspected hers from all angles."
    m "Cautiously, Amely tasted her chocolate ice cream."
    show amely smnormal at Position (xpos = 0.6) with dissolvemed
    m "The instant her tongue made contact with the chocolate, her eyes lit up in excitement and she took another bite."
    Ad giggle b "Well, I think someone likes ice cream."
    m "Amely was already attacking her cone from all angles."
    Ry normal "So, Amely, how's the ice cream?"
    Am "Ice cream... very good..."
    m "Her words were muffled as she continued devouring her cone."
    Ad normal b "I've never seen her eat something so fast!"
    m "Vara, done watching Amely enjoy her ice cream, took a small taste herself."
    m "She let the cold cream dissolve in her mouth, smacking her lips in the process."
    Vr "This is very good!"
    Ka smile flip "I'm glad you like it!"
    Vr "Are the cherries fresh?"
    Ka normal flip "Of course. Only the best for my customers."
    m "Vara took another small bite of her ice cream, while Amely was just about finished with hers."
    Ry "I just want to thank you again for everything, Katsuharu."
    Ka "In reality I should be the one thanking you five. Without you I doubt I could have served everyone in line today."
    Ad normal b "Even though I was busy corralling Amely the whole time?"
    c "If you weren't, I'm sure Amely would make a few of the customers unhappy."
    Ad giggle b "Good point."
    play sound "fx/bite.ogg"
    m "Looking down to Amely, I noticed that she had just taken the last bite of her cone."
    Ad normal b "Wait, is she done already?"
    Ry "Seems like it."
    Am "More?"
    Ad think b "We did promise to give her extra, didn't we?"
    Ry "I guess we did. Would you like another scoop of chocolate, Amely?"
    Am "Yes!"
    Ka normal flip "Another scoop of chocolate coming right up!"
    show katsu normal
    show adine normal b
    with dissolvemed
    hide katsu with easeoutleft
    $ renpy.pause (0.5)
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka smile flip "Here you go, Amely."
    Ad "What do we say, Amely?"
    Am "Thank you!"
    m "The little dragon attacked her cone with the same ferocity as the last."
    Ry "Vara, would you like another as well?"
    Vr "No thank you."
    Ka "Well, I best start closing up. Tonight I have to make a fresh batch of ice cream."
    Vr "Can I help?"
    Ry smile "Maybe another time, Vara. We should try to plan this out beforehand."
    Vr smsad "..."
    Ka "Don't worry, Vara. I make fresh ice cream quite often. Stop by in a few days, and you can help."
    Vr smnormal "Okay."
    if evalAdineTrick:
        Ad normal b "Oh! I think Amely left one of her toys by Katsuharu's cart when I grabbed her. I'll be right back."
        hide adine with easeoutleft
        c "(Wait, did Amely have a toy?)"
    Ry normal "Let's not hold Katsuharu up any longer. How about we find a nice place to sit?"
    if evalAdineTrick:
        c "I'll catch up with you in a moment. I don't want to leave Adine behind."
    else:
        c "I'll follow you."
    show remy normal flip
    show vara smnormal flip
    with dissolvemed
    hide remy
    hide vara
    with easeoutright
    if not evalAdineTrick:
        show adine normal b flip
    show amely smnormal flip
    with dissolvemed
    if not evalAdineTrick:
        hide adine
    hide amely
    with easeoutright
    if evalAdineTrick:
        show adine normal b flip at right with easeinleft
        show adine normal b
        Ad "By the way, [player_name]."
        c "Yes?"
        play sound "fx/slap1.wav"
        $ evalAdineSlaps += 1
        m "Giving me no time to react, I got another slap across the face."
        m "Taken aback, my cone fell from my grasp and onto the concrete."
        Ad giggle b "You're joke wasn't funny. I just wanted to catch you off guard."
        m "I rubbed my burning cheek."
        c "Ow! You made my drop my ice cream."
        Ka exhausted flip "You two really are something else. I can get you another scoop, [player_name]."
        show katsu exhausted with dissolvemed
        hide katsu with easeoutleft
        Ad normal b "I think you measured my patience incorrectly, it was at zero."
        Ad "Maybe next time don't annoy a wyvern with a mean slap."
        Ad giggle b "By the way, there's a bruise on your cheek that looks strangely like a banana."
        c "I hate you."
        Ad normal b "Love you too, [player_name]."
        show adine normal b flip with dissolvemed
        hide adine with easeoutright
        m "Adine made her way over to the rest of the group."
        show katsu normal flip at Position (xpos = 0.1) with easeinleft
        Ka "Here's a fresh scoop of mango ice cream, [player_name]."
        c "Sorry about dropping the first."
        Ka "No worries. Enjoy your ice cream, [player_name]."
        show katsu normal with dissolvemed
        hide katsu with easeoutleft
        m "With that, the dragon started packing up his cart."
        c "Do you need help with the cart again?"
        Ka "It's not stuck in a muddy hole this time, so I should manage."
        c "Well, I'm going to rejoin my group, have a nice day, Katsuharu."
        Ka "You too, [player_name]."
        scene black with dissolveslow
        m "Upon returning I found Adine, Remy, and Vara waiting with their ice cream while Amely was just finishing her own."
        scene evalpark1
        show adine normal b flip at left
        show amely smnormal flip at left
        show remy normal at right
        show vara smsmile at right
        with dissolveslow
        Ry "What happened back there, [player_name]?"
        c "Oh, I dropped my ice cream and Katsuharu had to get me another."
        Ry look "I guess that explains the bruise."
        Ad giggle b flip "I might have gotten a little bit of payback."
        Ry normal "I thought you liked [player_name]'s joke, Adine."
        Ad "I can be a master of deception if I want to be."
        if not adine1unheard:
            Ad "Like my voicemail to [player_name] when they first arrived."
            c "Oh yeah, you really got me with that. I totally thought it was my voicemail at first."
            Ad giggle b flip "Really?"
            c "No."
            Ad normal b flip "Damn."
        Ry "I'm glad you're back, though. I wanted to wait for you before I started, but I was starting to worry my ice cream would melt."
        Ad giggle b flip "Then let's eat before that inevitably happens."
        show adine normal b flip with dissolvemed
        Ry "You first, [player_name]. I want to see your reaction."
        m "Excited to finally try my ice cream, I saw Amely longingly look up at me."
        m "I paused for a moment and considered what to do."
        $ evalAdineTrickPassed=False
        menu:
            "[[Give Amely your ice cream]":
                c "Would you like some more ice cream, Amely?"
                Am "Yes!"
                Ry "That's a little too much ice cre-{w=0.5}{nw}"
                Ad sad b flip "No wait, don't give it t-{w=0.5}{nw}"
                m "I reached down to hand Amely my scoop of mango ice cream. She hungrily snatched it from my grasp and took a huge bite."
                Ad "Oh no..."
                $ renpy.pause (1.0)
                show amely smsad flip with dissolvemed
                Am "{size=+10}BLEAH!!!{/size}" with hpunch
                Am "Ice cream bad!"
                Am "{size=+10}Ice cream bad!{/size}"
                m "With as much force as she could muster, Amely threw the scoop of ice cream."
                show adine sad eval icecream flip with dissolvemed
                m "The scoop of mango landed directly on Adine, while the cone bounced and landed on the ground beside her."
                Ad annoyed eval icecream flip "Ack! Right on the muzzle!"
                Ad sad eval icecream flip "Oh, Amely! I am so sorry! I didn't mean for things to go this way."
                Ry look "What do you mean by that, Adine?"
                Ad annoyed eval icecream flip "Well, I tried to get back at [player_name] by switching the special and the mango in Katsuharu's cart."
                if mp.fish:
                    Ad "I knew that they didn't like it because they tried it at the diner a while ago, so I thought it would be a harmless joke."
                else:
                    Ad "Since the special is such an acquired taste, I assumed that they wouldn't enjoy it, so I thought it would be a harmless joke."
                c "Wait, so that wasn't mango ice cream?"
                Ad "No, it was the special."
                Ad sad eval icecream flip "I didn't expect you to give it to Amely, though, [player_name]."
                Ry "But wasn't the whole point of this to let [player_name] have some of Katsuharu's ice cream?"
                Ad think eval icecream flip "Of course. I was going to switch cones with them after they tried it. That's why I got the mango in the first place."
                Ad normal eval icecream flip "In hindsight, this probably wasn't one of my greatest plans. Here, [player_name], take my ice cream."
                m "Adine handed me her scoop of \"mango\" ice cream."
                c "Are you {i}sure{/i} that this ice cream is actually mango."
                Ad "I promise."
                Ry sad "What about Amely? She seems quite distraught after having the special."
                m "As if responding to Remy, Amely let out a small whimper."
                Ad sad eval icecream flip "I really don't know. I would ask Katsuharu for another scoop, but he's probably long gone."
                Vr "We share."
                show vara smsmile at Position (xpos = 0.7) with move
                Am "Ice cream bad."
                Vr "This one is good."
                Am "..."
                Am "Promise?"
                Vr "Promise."
                m "Amely tentatively tasted the cherry ice cream. As soon as she had a bite, her faith in ice cream seemed to be restored."
                Am smnormal flip "Good!"
                show remy normal
                show adine normal eval icecream flip
                with dissolvemed
                m "Amely took another big bite of the ice cream."
                Vr smshocked "I need some too!"
                Am "Sorry!"
                show vara smsmile with dissolvemed
                Ad giggle eval icecream flip "Vara! That's so nice of you."
                Ry normal "I'm glad everything seems to have sorted itself out for the most part."
                c "What about you, Adine?"
                Ad annoyed eval icecream flip "Well, I did get your scoop of ice cream, just not exactly how or where I wanted it."
                m "With a surprisingly long tongue, Adine started licking the ice cream off of her muzzle."
                Ry smile "That's one way to do it."
                Ad think eval icecream flip "You know what? Katsuharu was right. The special is somehow better in ice cream form."
                c "I beg to differ."
                Ad giggle eval icecream flip "I guess it's just an acquired taste you don't have."
                Ad normal eval icecream flip "But you two should really start to eat as well. Your ice cream is melting."
                m "Looking down, I noticed that the mango ice cream was dripping down the cone and pooling onto my hand."
                Ry normal "Good idea."
                m "In unison, Remy and I both took a bite of our respective scoops of ice cream."
                m "Still wary about which flavor I was really about to eat, I was pleasantly surprised when my tongue made contact with the cool, delicious flavor of mango ice cream."
                m "Any ice cream I had previously had could not compare with the smooth, creamy texture of Katsuharu's."
                $ evalAdineTrickPassed=True
            "[[Keep your ice cream]":
                c "Sorry, Amely. But I think you've had enough ice cream for today."
                Am smsad flip "Awwww..."
                Ry "Amely, you've already had two scoops."
                Am "Want more..."
                Ry "We'll make sure to come back here more often for you, alright?"
                Am smnormal flip "Alright."
                m "I took a bite of my ice cream as Adine and Remy watched."
                m "As soon as my tongue made contact with the mango ice cream, my face involuntarily contorted into disgust."
                c "This is the most disgusting mango flavor I have ever tasted."
                Ry look "I've had the mango before, it's really good."
                show adine giggle b flip with dissolvemed
                m "Adine burst out laughing."
                Ad "Sorry, [player_name], I guess Katsuharu might have given you the wrong flavor."
                c "What?"
                Ad normal b flip "I thought it would be obvious by now."
                m "After a moment of thought, I realized what had just happened."
                c "You switched out the flavors, didn't you?"
                Ad "Good going, detective!"
                c "I guess I should have seen this coming."
                Ry look "Adine, that's funny and all, but now [player_name] can't enjoy their ice cream."
                Ad giggle b flip "Don't be silly, why do you think I got the mango ice cream? Here, let's trade, [player_name]."
                m "I quickly swapped cones with Adine."
                Ry normal "That's quite clever, Adine."
                Ad normal b flip "Better than anything [player_name] could make up."
                m "I carefully inspected the scoop of \"mango\" Adine had just given me."
                c "Now, you promise that this isn't the special."
                Ad "Promise."
                m "I carefully took a taste of the ice cream."
                m "Preparing my taste buds for the worse, I was pleasantly surprised when my tongue made contact with the cool, delicious flavor of mango ice cream."
                m "Any ice cream I had previously had could not compare with the smooth, creamy texture of Katsuharu's."
                $ evalAdineTrickPassed=False
        c "Wow! This is amazing!"
        Ry smile "I'm glad you like it!"
        stop music fadeout 2.0
        scene black with dissolveslow
#        m "For the next while the five of us sat quietly as we enjoyed our ice cream. Adine had some difficulties with hers, but after a while she had completely cleaned off her muzzle."
        scene evalpark2
        show adine normal b flip at left #No more ice cream on her face. How sad.
        show amely smnormal flip at left
        show vara smnormal behind amely at right
        show remy normal behind vara at right
        with dissolveslow
        play music "mx/campfire.ogg" fadein 2.0
        $ renpy.pause (1.0)
        play sound "fx/bite.ogg"
        m "I took the final piece of my cone and bit down on it with a satisfying crunch."
        c "Well, I'm full."
        Ry smile "Same here."
        Am "Vara!"
        Vr "..."
        Am "Thanks!"
        show vara smnone with dissolvemed
        show amely smnormal flip at Position(xpos = 0.5) with move
        play sound "fx/hug.mp3"
        m "Amely wrapped her arms tightly around Vara's body."
        Vr smnormal "You're welcome."
        Ad giggle b flip "That's adorable."
        show amely smnormal
        show amely smnormal at left with move
        show amely smnormal flip
        Ad disappoint b flip "Now that I'm thinking about it, I may have been a bit too harsh on you, [player_name]. I'm sorry."
        
        menu:
            "It's alright.":
                c "Don't worry about it, Adine. In a way, I kind of deserved it."
                Ad giggle b flip "Probably not to this extent, but yes."
                label evalAdineTrickForgave:
                    pass
                Ad normal b flip "Just know that you're a wonderful friend, and even though it may not have seemed like it, I had fun."
                hide adine with dissolvemed
                play sound "fx/hug.mp3"
                if evalOrphanageScore == 2:
                    m "Adine walked up and gave me another big hug."
                else:
                    m "Adine walked up to me and gave me a hug."
                show adine normal b flip at left behind amely with dissolvemed
                Ad "Does that help make up for it?"
                if evalOrphanageScore == 2:
                    c "You're in quite the hugging mood today, Adine."
                    Ad giggle b flip "I guess so."
                else:
                    c "Yes it does."
                Ry look "Wow, when did it get this dark? We should probably start heading back."
                Ad think b flip "I guess I was just too busy focusing on getting all the ice cream off my muzzle."
                Ry "Let's get these two back to the orphanage, Adine. It would be faster if we each took one of them."
                Ad normal b flip "Sure, Remy. I guess this marks the end of our day out together."
                c "We're going to have to do this again sometime. That was delicious."
                Ry "I second that."
                Ad "And I don't think these two would mind either. Right?"
                Am "More?"
                Ad giggle b flip "Not right now, silly!"
                Ry "Would you mind helping Vara onto my back, [player_name]?"
                c "Sure."
                hide vara with dissolvemed
                m "I grabbed Vara and lifted her onto Remy's back."
                m "It was quite a sight seeing the small, pink dragon riding on Remy's back."
                Ry "You alright up there, Vara?"
                Vr "Yes."
                Ry "Alright then. See you soon, [player_name]."
                c "Goodbye, Remy."
                show remy normal flip with dissolvemed
                hide remy with easeoutright
                play sound "fx/takeoff.ogg"
                m "Remy, with Vara clutching onto his back, took off into the air."
                Ad "Come on, Amely, let's go as well."
                Am "Okay!"
                show adine normal b flip
                show amely smnormal flip
                with dissolvemed
                hide adine
                hide amely
                with easeoutright
                $ renpy.pause (1.0)
                play sound "fx/takeoff.ogg"
                m "With Amely tightly grasped within her claws, Adine soared into the night sky."
            "I forgive you, on one condition.":
                Ad sad b flip "what is it?"
                c "let's all agree to not pull pranks when the children are preset."
                Ad normal b flip "sure."
                if evalAdineTrickPassed:#if you gave Amely Adine's bad ice cream
                    c "that prank may have been funny if I kept my ice cream."
                    c "I probably would have deserved it."
                else:
                    c "I kind deserved it."
                    c "but I nearly gave Amely that ice cream."
                jump evalAdineTrickForgave
            "You went too far, Adine.":#shame on you MC, she already felt bad about that.
                $ adinestatus = "none"
                c "You should be sorry. That little joke of yours almost ruined our entire day out."
                Ad sad b flip "I... I know it was a bit rash, but I didn't know it was that bad."
                Ry look "It wasn't that bad, [player_name]. It's just ice cream."
                $ adinestatus = "abandoned"#good job [player_name], you made Adine feel like trash
                c "Yeah. That {i}I{/i} treated you to."
                Ad "..."
                Ad disappoint b flip "It's getting late. Let's go, Amely."
                Am "Okay!"
                show adine disappoint b flip behind amely
                show amely smnormal flip behind remy
                with dissolvemed
                hide adine
                hide amely
                with easeoutright
                Ry sad "Maybe you shouldn't have been so harsh on her. It was meant as a harmless joke."
                c "Her \"harmless\" joke almost ruined our day. Someone had to say something."
                Vr smgrowl "That was mean!"
                Ry look "I might have to agree with Vara here, [player_name]."
                Ry "The two of us should probably get going as well. It's getting close to Vara's bedtime."
                c "We should do this again sometime. Maybe without Adine, though."
                Ry "Maybe we could."
                Ry "Alright, Vara, climb aboard."
                hide vara with dissolvemed
                m "Remy got down on all fours as Vara clambered onto his back."
                Ry "Bye, [player_name]. See you around."
                c "Goodbye, Remy."
                show remy look flip with dissolvemed
                hide remy with easeoutright
                scene black with dissolveslow
                play sound "fx/system3.wav"
                s "Nice going [player_name]."
                play sound "fx/system3.wav"
                s "you made adine feel like trash."
                $ evalFail = "Taking Things too Seriously"
                jump eval_fails

    else:
        scene black with dissolveslow
        m "I followed the four dragons to a small clearing in the park."
        scene evalpark1
        show adine normal b flip at left
        show amely smnormal flip at left
        show remy normal at right
        show vara smnormal at right
        with dissolveslow
        Ry "This is as good of a spot as any."
        Ad "You should try yours first, [player_name]. I want to see how you like the [evalChosenFlavor]."
        m "Adine and Remy eagerly watched as I took a small bite of the [evalChosenFlavor] ice cream."
        if evalChosenFlavor == "special":
            m "As soon as I tasted the special, my face involuntarily contorted into a look of disgust."
            if mp.fish:
                c "Wow, this is just as disgusting as I remember it being."
                Ad giggle b flip "Well, I guess you didn't like it better in ice cream form after all."
            else:
                c "Wow, this is disgusting."
                Ad giggle b flip "Well, I guess you also won't like the special we serve at the diner as well."
            c "You actually enjoy this, Adine?"
            Ad normal b flip "Yeah! I think it's really good!"
            c "I find that very hard to believe."
            Ad "Well, I would be more than happy to take that off your hands."
            c "Be my guest."
            m "I handed the cone to Adine, who took it in her open claw."
            Ad "A bit of extra ice cream never hurt anyone."
            Ad annoyed b flip "Let's just hope my stomach doesn't say something to contradict that statement later."
            Ry look "Well, what are we going to do now? It's ironic that [player_name] brought us all out here to treat us to ice cream but isn't able to have any themself."
            Ka "Did I hear something about an unhappy customer?"
            hide adine
            hide amely
            with dissolvemed
            show amely smnormal at Position (xpos = 0.6) behind remy
            show adine normal b at Position (xpos = 0.6) behind amely
            show remy normal behind vara
            with dissolvemed
            show katsu normal flip at Position (xpos = 0.1) with easeinleft
            c "How did you know?"
            Ka smile flip "As a businessman, I have a sixth sense for customer satisfaction."
            m "Katsuharu quickly produced a fresh scoop of vanilla ice cream."
            Ka normal flip "You should like this much better."
            c "Wow! Thank you Katsuharu!"
            Am "More?"
            Ry "Sorry, Amely. We only promised two scoops of ice cream today."
            Am smsad "Awwwwwww."
            Ad "Don't worry, Amely. We'll come back another time."
            Am smnormal "Okay..."
            Ka "I'm going to get going for real this time. You five take care."
            Ry "Thank you, Katsuharu!"
            show katsu normal with dissolvemed
            hide katsu with easeoutleft
            Ry "Hopefully you'll like the vanilla."
            m "Cautiously, I took a small bite of the vanilla."
        else:
            m "I took a small bite of the [evalChosenFlavor] ice cream."
        m "As the cool ice cream dissolved on my tongue, my face lit up in excitement."
        Ad giggle b flip "Now that's the reaction I would expect from Katsuharu's ice cream."
        c "This is really good!"
        scene black with dissolveslow
        m "I quickly devoured the cone, rivaling Amely in speed."
        scene evalpark2
        show remy normal at right
        show vara smnormal at right
        show adine normal b flip at left
        show amely smnormal flip at left
        with dissolveslow
        Ry normal "Wow, I didn't even notice how late it was. We should probably start heading back."
        Ry "Let's get these two back to the orphanage, Adine. It would be faster if we each took one of them."
        Ad normal b flip "Sure, Remy. I guess this marks the end of our day out together."
        c "We're going to have to do this again sometime. That was delicious."
        Ry "I second that."
        Ad "And I don't think these two would mind either. Right?"
        Am "More?"
        Ad giggle b flip "Not right now, silly!"
        Ry "Would you mind helping Vara onto my back, [player_name]?"
        c "Sure."
        hide vara with dissolvemed
        m "I grabbed Vara and lifted her onto Remy's back."
        m "It was quite a sight seeing the small, pink dragon riding on Remy's back"
        Ry "You alright up there, Vara?"
        Vr "Yes."
        Ry "Alright then. See you soon, [player_name]."
        c "Goodbye, Remy."
        show remy normal flip with dissolvemed
        hide remy with easeoutright
        play sound "fx/takeoff.ogg"
        m "Remy, with Vara clutching onto his back, took off into the air."
        Ad "Come on, Amely, let's go as well."
        Am "Okay!"
        show adine normal b flip
        show amely smnormal flip
        with dissolvemed
        hide adine
        hide amely
        with easeoutright
        $ renpy.pause (1.0)
        play sound "fx/takeoff.ogg"
        m "With Amely tightly grasped within her claws, Adine soared into the night sky."
    
    m "With everyone else gone, I made my way back to my apartment."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene evalplayerapt1 with dissolveslow
    play music "mx/amb/night.ogg" fadein 2.0
    m "After a brisk walk, I arrived back at my apartment. I was surprised to see the interior lights seemed to be on."
    c "(I'm sure I turned them off before I left.)"
    stop music fadeout 2.0
    play sound "fx/door/doorchain.ogg"
    m "I used my key and walked inside."
    scene black with dissolveslow
    scene o2
    show remy smile
    with dissolveslow
    play music "mx/pier.mp3"
    Ry "Surprise!"
    c "What? A surprise?"
    Ry "Well, on our way back to the orphanage, Vara had the bright idea to come here and prepare you a surprise meal."
    Ry "So we made a quick stop there for ingredients and came right over."
    c "Really? That's so sweet."
    c "But how did you manage to get in?"
    Ry normal "When you first arrived in our world, I left a spare key hidden near the door."
    Ry look "Did you even read the letter I gave you?"
    c "I did, but I must have glanced over that part."
    Ry normal "Anyways, come into the kitchen. Vara should be finishing up shortly."
    scene black with dissolveslow
    scene evalplayerkitchen
    show remy normal at right
    with dissolveslow
    Ry "Hey, Vara. [player_name] is back."
    show vara smshocked at left with easeinright
    show vara smshocked flip at left with dissolvemed
    Vr "I'm not ready!"
    c "Don't worry about it, Vara. I've already been thoroughly surprised. Plus, I don't mind waiting and talking."
    Vr smnormal flip "Okay. Almost done."
    hide vara with easeoutright
    Ry smile "I would love to talk right here, but I'm more or less Vara's designated stool at the moment."
    c "What?"
    Ry normal "You'll see."
    show remy normal flip with dissolvemed
    hide remy with easeoutright
    m "Remy walked over to the edge of the countertop and stood parallel to it."
    m "Vara then hopped up onto his back and rested her front legs on the countertop."
    c "Now I see what you mean."
    Ry "I love assisting her while she cooks, but I still can't help looking forward to when Vara is tall enough to reach the countertop herself."
    m "I sat down at the table and watched Vara as she skillfully navigated her ingredients."
    m "I couldn't tell exactly what she was making, but it seemed to be some sort of meat similar to steak."
    m "I looked around the room, taking in the smaller details I had failed to notice earlier."
    c "(Damn, I cook so little I don't know where anything is in my own kitchen.)"
    show remy normal at right
    show vara smnormal at left
    with easeinright
    show vara smnormal flip with dissolvemed
    m "After a little bit longer, Vara and Remy returned to the table with three plates."
    c "Wow! This looks amazing!"
    Vr smsmile flip "It's Mouflon made with my own recipe."
    if not mp.vegetarian:
        c "Oh! I've had that before, but not so finely prepared. I'm excited to try it!"
    else:
        c "Can't say I've had Mouflon before, but it looks delicious."
    m "On the plate, a large chunk of the Mouflon rested in the middle of mashed potatoes lightly covered in an onion garnish."
    m "The meat was also covered in sauce that dripped down the edges and pooled where the meat and potatoes met."
    m "The meal and presentation looked like I was eating at a five star restaurant."
    show vara smnone flip with dissolvemed
    m "I carefully cut a small slice of the Mouflon. The meat was so tender it almost fell apart. As I was cutting, Vara looked at me nervously."
    m "I put the Mouflon into my mouth and started chewing. The mix of the juicy meat and Vara's sauce left me speechless."
    c "I am not kidding when I say that this is better than anything I ever had back in my world."
    Vr smshocked flip "Really?"
    c "I'm completely serious."
    Vr "..."
    Vr smsmile flip "Thank you!"
    m "Remy and Vara proceeded to eat their own portions as well."
    Ry smile "[player_name] isn't wrong, Vara. This is amazing."
    Vr "Could use less salt, but yes."
    c "Can I ask how you made it?"
    Vr "Nope! It's a secret."
    Ry look "Good luck trying to get any of Vara's recipes, [player_name]. Even I don't know them."
    Vr "They are my secret!"
    Vr "Maybe I will tell you later."
    Ry normal "It's not like either of us could cook them as well as you, anyways."
    m "It didn't take long for the three of us to clean our plates. Normally, I couldn't eat this much in one sitting, but this was an exception." #Possible to delete
    Ry "I'm impressed you were able to eat a course big enough for a dragon, [player_name]!"
    c "So am I. It was so good I just couldn't stop eating."
    m "Remy started taking our dishes and rinsing them off in the sink."
    c "Don't worry about the dishes, Remy. It's the least I can do to make up for this amazing meal."
    Ry smile "Personally I would never give up an offer for free dish washing, but suit yourself."
    scene black with dissolveslow
    stop music fadeout 2.0
    m "The three of us made our way into the main room."
    scene o2
    show remy normal at right
    show vara smsmile flip at left
    with dissolveslow
    if not evalDoingSecretEnding:
        Ry "Can we meet tomorrow, [player_name]."
        c "Of course we can. Goodnight you two."
        Ry "Goodnight, [player_name]."
        Vr "Goodnight!"
        hide remy
        hide vara
        with easeoutleft
        play sound "fx/door/doorchain.ogg"
        m "With that, the two dragons left through the door, leaving me alone in my apartment."
        m "I made my way over to the bedroom to get ready to sleep."
        c "(It's wonderful that Remy and Vara are a real family now.)"
        
        stop music fadeout 2.0
        scene black with dissolveslow
        $ persistent.evalEndingD = True
        jump eval_custom_credits#i think we need a different scene for if vara suvived due to another mod
    Ry "Well, Vara. Are you ready to go home?"
    Vr smnormal flip "The orphanage?"
    Ry shy "Well..."
    play sound "fx/envelope.wav"
    play music "mx/slow.ogg" fadein 4.0
    m "Remy lifted his wing, revealing a stack of paper that fell to the floor. He clumsily picked them up."
    Ry "I don't mean the orphanage, Vara. {w}I mean home."
    show vara smnone flip with dissolvemed
    m "Vara looked at Remy with a confused stare."
    Vr smnone flip "..."
    Vr smnone flip "..."
    Vr smshocked flip "..."
    Ry look "Vara are you alri-{w=0.3}{nw}"
    show vara smshocked flip behind remy at Position (xpos = 0.35) with move9
    show vara smsad flip behind remy
    show remy shy
    with dissolvemed
    m "The little dragon burst into tears and buried her face into Remy."
    Vr "H... {w}H..."
    m "She struggled to speak as tears continued to flow from her eyes."
    Vr "Home?"
    Ry "Yes, Vara. I signed the papers earlier today."
    Ry "You're my daughter."
    show vara smsad flip behind remy at Position (xpos = 0.4) with move
    m "Remy draped his wing around Vara and pulled her closer to him."
    hide remy
    hide vara
    with dissolvemed
    stop music fadeout 10.0
    m "It felt awkward to stand and watch the two dragons, so I rested on the nearby couch and idly skimmed through a book on the desk next to me."
    m "After a while, the crying subsided, and I heard Remy walk over to me."
    show remy normal
    show vara smnone
    with dissolvemed
    play music "mx/sleepingcity.ogg"
    Ry "{i}Draconic Desires{/i}? Really, [player_name]?"
    m "I hadn't even noticed that I had chosen that as my reading material."
    c "Oh! I didn't even notice, I was just idly skimming it."
    m "I closed the book and placed it back on the desk."
    c "It was such an emotional moment between the two of you. I felt awkward just standing and watching."
    Ry "I understand. I was going to tell Vara once we arrived at the orphanage, but when she had the idea to surprise you, I decided to announce it here instead."
    Ry "You mean a lot to the both of us, [player_name]. It felt only natural that you would be present when I broke the news to her."
    Ry shy "I know I may sound like a broken record at this point, but thank you for everything."
    Ry "This day out{w}, this wonderful little dragon that I can call my daughter{w}, and even my life. I owe it all to you."
    c "Remy, I don't know what to say."
    Ry "Then don't say anything. What you have done for us speaks louder than any words could."
    hide remy with dissolvemed
    if evalRemyRomance:
        m "Remy enveloped me in his wing and pulled me closer to him. His scales radiated with a soft warmth."
        m "Playfully, he gave my nose a lick."
    else:
        m "Remy gently enveloped me in his wing and pulled me closer. His scales radiated with a soft warmth."
    hide vara with dissolvemed
    m "Suddenly, I felt Vara hug me as well. Since she couldn't make it onto the couch, she resorted to squeezing my legs instead."
    m "While awkward, the little dragon's embrace was warm and comforting."
    m "We sat still for a few moments before Remy, with a relaxed sigh, released me from the clutches of his wing. Vara, however, stayed latched to my legs."
    show remy normal with dissolvemed
    Ry "You know, we should do this sort of thing more often."
    c "Well, now that I'm not chasing around murderers or in a coma, I should have a lot more free time."

    #Ry "You mean a lot to the both of us, you know."
    #Ry shy "I know I may sound like a broken record at this point, but thank you for everything, [player_name]."
    #Ry "This day out, this wonderful little dragon that I can call my daughter, and even my life. I owe it all to you."
    #c "Remy, I don't know what to say."
    #Ry "Then don't say anything."
    #hide remy
    #hide vara
    #with dissolvemed
    #if evalRemyRomance: #This if else is pretty meh. I can't write this crap.
    #    m "I was suddenly wrapped in Remy's warm embrace as he sat down and used his front legs to pull me into a big hug."
    #    m "Using his wings to cover up Vara, he pressed his lips against mine. I embraced him with my arms and pulled in closer."
    #    m "As we parted, he playfully flicked his tongue on my nose."
    #else:
    #    m "I was suddenly wrapped in Remy's warm embrace as he sat down and used his front legs to pull me into a big hug."
    #    m "There was no escaping his grasp, so I wrapped my arms around his neck and hugged him as well."
    #    m "Suddenly, I felt Vara embrace me as well. Since she was too short to hug my upper body, so she resorted to squeezing my legs instead."
    #    m "After a few tender moments, we parted."
    #show remy normal
    #show vara smnone
    #with dissolvemed
    #Ry smile "We should do this sort of thing more often."
    #c "Well, now that I'm not chasing around criminals or in a coma, I should have a lot more free time."
    #if evalRemyRomance:
    #    Ry smile "I meant the kiss."
    #    c "Who said more free time couldn't lead to that?"
    #    Ry normal "Point taken."
    #Ry shy "I just worry the time we have together is running thin."
    #c "How so?"
    #Ry look "Won't you be going back through the portal soon?"
    #c "I've been trying not to think about that, but I feel obligated to do everything in my power to save humanity."
    #Ry sad "It's going to be difficult when we have to part ways."
    #c "I'm not leaving. I'm just going back to the day I got here."
    #Ry "Still, I can't shake off the feeling that I won't ever see you again."
    #c "What do you mean?"
    #Ry "I know I said that I would see you again after you went through the portal, but in a way, I feel like when you enter that portal, you don't go back to my world, but a world exactly like mine with a dragon exactly like me."
    #c "I see."
    #m "Vara finally released her grip from my legs and returned to Remy's side."
    #show vara smnormal with dissolvemed
    #m "Remy looked down at Vara."
    #show vara smsmile with dissolvemed
    #m "Gently, he nuzzled her frills. As a result, a small smile formed at her lips."
    #Ry normal "But in the foreseeable future, you aren't going anywhere, and I am going to appreciate the time that we have together."
    #c "So will I."
    show vara smsmile with dissolvemed
    Ry "It's been fun, but I think that Vara and I should get going. We won't start moving her stuff in, but she still needs to settle in."
    Ry "Can we meet tomorrow, though? There's something I need to ask you."
    c "Of course we can. Goodnight you two."
    Ry "Goodnight, [player_name]."
    Vr "Goodnight!"
    hide remy
    hide vara
    with easeoutleft
    play sound "fx/door/doorchain.ogg"
    m "With that, the two dragons left through the door, leaving me alone in my apartment."
    m "I made my way over to the bedroom to get ready to sleep."
    c "(It's wonderful that Remy and Vara are a real family now.)"
    
    stop music fadeout 2.0
    scene black with dissolveslow
    #scene o2
    #play sound "fx/knocking1.ogg"
    #Another scrapped scene
    #m "Suddenly, there was a knock at the door."
    #c "(Remy and Vara must have forgotten something.)"
    #play sound "fx/door/doorchain.ogg"
    #m "I walked to the door and opened it."
    #play music "mx/cavern.mp3" fadein 3.0
    #show izumi normal 7 with dissolvemed
    #As "Hello, [player_name]."
    #c "Izumi? But I thought you died during the portal incident."
    #As "Did I? That must explain why I did not see myself when coming here."
    #As "Do you have what I am looking for?"
    #c "I don't think I understand."
    #As "Izumi revealed a small, pendant-like device identical to the previous Izumi had given me."
    #As "This."
    #c "I think so."
    #m "I dug into the pocket where I had kept the pendant. Luckily, it was still there."
    #m "I handed it to Izumi, who slid the cover up and inspected the light."
    #c "Can you explain what exactly these pendants do?"
    #As "In simple terms, they detect corrupted timelines."
    #c "Corrupted?"
    #As "Timelines influenced by others in ways they should not."
    #As "Over your many attempts going through the portal, certain continuities have been established between timelines."
    #As "While most of these are harmless to our cause to save both the dragon and human world, some have the potential to be catastrophic."
    #As "I do not know the explanation for these continuities, but this device informs me of their existence and their position."
    #m "Izumi took the two pendants and pressed the two pulsing red lights against each other."
    #play sound "fx/glassimpact2.ogg"
    #m "With a loud bang, the glass within the pendants shattered."
    #As "Good. I'm in the right place."
    #c "What does the shattered glass mean?"
    #As "It means that this timeline is corrupted and cannot interact with other timelines."
    #As "Do you know why this happened?"
    #c "The first Izumi said something about a fragment of events from alternate timelines."
    #As "I see. Events from other timelines have influenced your mind in this one."
    #As "While it is entirely possible that these fragments can be beneficial, this specific circumstance could spell disaster for our plans."
    #c "How so?"
    #As "With one fragment could come many more. Going back to the day you arrived could have irreversible consequences."
    #c "How could retaining knowledge of one timeline negatively impact another? Would that not better prepare me for the events that unfold and stop them in their tracks?"
    #As "There is a delicate balance between your interaction with the dragon world and saving humanity."
    #As "I cannot let you go through the portal with the possibility of my plans failing."
    #c "But what about my people? Are they destined to fall if I stay?"
    #As "There are others that will take your place to save humanity."
    #c "Others?"
    #As "Alternate versions of yourself, created in other timelines."
    #As "They will take your place."
    #c "So I have to stay here?"
    #As "You have no other choice."
    #c "But what about yourself?"
    #As "I do not belong here, nor do I need to be here any longer. I will leave and completely deactivate the portal."
    #m "I took a deep breath. It took a moment for Izumi's words to penetrate my mind."
    #c "I think I understand, Izumi."
    #As "Then my work here is done. Enjoy your life in the dragon world, [player_name]. It seems you've made some friends already."
    #show izumi normal 7 at left with move
    #c "Wait, Izumi."
    #show izumi normal 7 flip with dissolvemed
    #m "I looked at her one last time, taking in the sight of the last human I was ever going to see."
    #m "I took a deep breath."
    #c "Okay, you can go now."
    #As "Goodbye, [player_name]."
    #show izumi normal 7 with dissolvemed
    #hide izumi with easeoutleft
    #play sound "fx/door/doorchain.ogg"
    #m "With that, I was left alone with my thoughts."
    #m "I'll have to call Remy tomorrow and break the news to him."
    #stop music fadeout 2.0
    #scene black with dissolveslow

    #This dialogue kinda sucks rn - deleting until someone who can actually write this stuff looks over it
    #nvl clear
    #window show
    #
    #n "Laying in bed, I wrestled with the prospects of my future. I was stuck in the dragon world with no hope for escape or any human contacts."
    #n "Of course, I love the world and its people, but the idea of never seeing another human face was a pill that was hard to swallow."
    #n "There was nothing left back in my world. With the landscape in ruins and our power running low, the portal was our last ditch effort to save humanity."
    #n "But now I was no longer a part of that effort. It was now up to another version of myself from a different timeline."
    #
    #nvl clear
    #
    #n "But there was no use dwelling on these thoughts any longer. The portal was deactivated, and I needed to focus on my future in the dragon world."
    #n "I was unsure how much longer the dragon council would be willing to fund my stay in their world, or if I would keep my apartment at all. I would most likely have to get a job somewhere within the town."
    #n "However, deep down, I knew that I wouldn't have much to worry about. There were people here who cared for me, and I cared for them."
    #n "I knew that with their help and support, I could put the past behind me and move on. I was part of the dragon world now, and that was something I needed to accept."
    #n "After a few restless hours of sleep, I woke up and called Remy to tell him everything."
    #
    #nvl clear
    #window hide

    $ renpy.pause (1.5)
    scene o
    show remy normal
    with dissolveslow
    play music "mx/campfire.ogg"
    Ry "Hey, [player_name]. Long time no see."
    c "Remy, we just saw each other last night."
    Ry smile "I know."
    c "Well, was there any specific reason you wanted to come over and visit, or was it just to make that joke?"
    Ry normal "There is, but first, look what I brought."
    m "Remy revealed a bottle of wine."
    c "Oh boy, is this the {i}third{/i} cheapest wine this time? I feel spoiled."
    Ry smile "That would have been quite funny, but I decided that instead of getting the second cheapest wine, I would get us the second most expensive instead."
    c "Wow! How expensive was it?"
    Ry look "Let's just say that the cashier gave me a concerned look when I was checking out."
    Ry normal "But let's not worry about that and enjoy it."
    hide remy with easeoutleft
    m "Remy made his way into the kitchen and returned with two empty glasses."
    show remy normal flip with easeinleft
    show remy normal with dissolvemed
    play sound "fx/pouringwine.ogg"
    m "He carefully uncorked the bottle with his claw and poured us two glasses of the wine."
    m "Remy raised his glass."
    Ry smile "Cheers!"
    play sound "fx/clink.ogg"
    $ renpy.pause (1.0)
    show remy normal with dissolvemed
    m "I took a sip from my wine glass. Words couldn't describe just how much better this wine was compared to the last."
    Ry "Well, is the second most expensive wine any better than the second cheapest?"
    c "So much better. This is great."
    Ry "Well you better enjoy every last drop of it because there is no way I'm letting any of this go to waste."
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    m "The two of us quietly sipped at our wine glasses until Remy once again spoke."

    #Ry "You sounded serious on the phone, [player_name]. Is everything alright?"
    #c "I talked to Izumi again."
    #Ry "Wait, the human? Didn't she die back at the portal?"
    #c "It was another version of Izumi from a different timeline."
    #Ry sad "I don't think I'll ever be able to understand all of this time travel nonsense."
    #c "Well, you won't have to anymore, because I'm not going anywhere."
    #y "Wait. {w}What?"
    #c "Because I saved Vara, I get to stay here with you two."
    #Ry normal "Really? That's wonderful!"
    #Ry sad "But what about humanity? Aren't you their only hope?"
    #c "Izumi said that there were other versions of myself still working to save humanity. If I were to try and help now, I might mess everything up."
    #Ry look "I see. So you're staying here forever?"
    #c "Seems like it."
    #Ry smile "This is so exciting! I didn't even consider the possibility of you staying in our world."
    #c "It was a rough night thinking about my future here."
    #Ry look "I can see that. It must be so difficult having to accept the fact that you will never see another human again."
    #c "It is, trust me. But at least I have you guys to help me through it all."
    #Ry normal "Vara, Adine, Amely and I will always be there for you, [player_name]. I'm sure there's also a lot of other wonderful people you will meet as well."
    #c "Thanks, Remy."
    play music "mx/gravity.ogg" fadein 2.0
    Ry shy "[player_name], there's something I've been meaning to ask you."
    Ry "..."
    Ry "Would you be interested in a... {w}more meaningful relationship?"
    c "How so?"
    Ry "Well, what we have now is great, but I was looking for something... {w}deeper and more personal."
    Ry "I wasn't going to say any of this to you before because I thought you were going through the portal."
    c "Why not?"
    Ry sad "Because I couldn't take losing another person that close to me."
    Ry "Don't get me wrong, what we have is strong and special, but I was afraid to go any further because I didn't want to feel the pain like I did losing Amelia."
    Ry "It hurt me so badly, and I knew that if I developed a deeper relationship with you and you one day went through that portal, I would be crushed."
    Ry shy "But now that you're staying, I feel comfortable asking for more."
    Ry normal "What do you say, [player_name]? I'll be happy either way, I promise."

    menu:
        "[[Accept.]":
            c "I think we should give this a shot. We've been through so much together, and there is nobody I would rather spend my time with than you."
            c "Maybe we could even be our own little family."
            Ry shy "You do not understand how happy that makes me feel, [player_name]."
            Ry sad "For so long, I've had this hole in my heart that Amelia used to fill."
            Ry "I thought that all this time, everything I did was for her. To let her live on through my actions."
            Ry "I tried to fill that hole by isolating myself and remorsing over who had used to fill it."
            Ry shy "But with you, {w}I think I can finally be whole again."
            hide remy
            with dissolvemed
            m "Before I could react, I was wrapped within Remy's tight embrace as he sat down and used his front legs to pull me into a big hug."
            if evalRemyRomance:
                m "He pressed his lips against mine. I embraced him with my arms and pulled in closer."
            m "As we parted, he rested his head on top of my own. I felt a stream of tears form on my head and roll down my cheeks."
            m "It was possible that a few of those tears were mine as well."
            m "We embraced for what felt like hours. Time around us seemed to stop."
            m "At that moment, nothing else mattered. I buried my face deeper into his soft underbelly scales and closed my eyes."
            #m "Remy once again sat down and grabbed me with his front legs, pulling me into his soft, scaly underbelly."
            #m "I embraced him as well and pulled myself in as close as I could."
            #m "He rested the top of his head on my own, and I felt his tears form on my head and roll down my cheeks."
            #m "It was possible that a few of those tears were mine as well."
            #m "We embraced for what seemed like hours. Time around us stopped."
            #m "At that moment, nothing else mattered. I buried my face deeper into his scales and closed my eyes."
            stop music fadeout 2.0
            scene black with dissolveslow
            $ renpy.pause (2.0)
        "[[Reject]":
            c "Sorry, Remy, but I don't think I'm ready to take our relationship any further."
            c "You mean a lot to me, but I just can't say I'm ready."
            Ry "I understand. Maybe I was pushing you too hard. Would you be open to something in the future?"
            c "The most I can say is maybe. Please, don't take this as me not wanting to spend time with you, because that is not the case."
            Ry "Alright, I understand."
            Ry normal "I should probably run and get to work. Emera gets furious if I show up late."
            c "Is Vara coming with you?"
            Ry "I wasn't able to get a sitter on such short notice, so yes."
            c "Well, I'll see you later, Remy!"
            m "A single tear escaped Remy's eye."
            Ry "Goodbye, [player_name]! We need to plan some more things together."
            c "Absolutely."
            hide remy
            with easeoutleft
            $ renpy.pause (0.5)
            play sound "fx/door/door_chain.wav"
            $ renpy.pause (1.5)
            stop music fadeout 2.0
            scene black with dissolveslow
    $ renpy.pause (1.0)
    $ persistent.evalEndingD = True
    jump eval_custom_credits
    #With one fragment could come many more, leading to disatrous timelines.
    #There is a delicate balance between your interaction with the dragon world and saving humanity.
    #Add something about Remy wanting a real relationship now that you will be staying and he didn't want to bring it up before b/c he thought he would lose you like he lost amelia (didn't want to establish the same connection)

    #Jump to credits, then have message saying you have unlocked ability to play all scenes at any time

    #That's it... I'm done with this whole mod (probably not true). What an experience. <-- BOY WAS THIS WRONG LOL
