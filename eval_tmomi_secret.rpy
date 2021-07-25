#A list of everything required to get the secret ending:
    #Complete solo Remy and Remy + Amely endings
    #Complete Remy + Amely + Adine ending with perfect scores in both minigames and hugging Remy
    #Visit the hatchery to drop off the eggs
    #Save vara by following her out of the store

#Remy's 4th date, make it so that when Remy mentions Vara, he decides that the two of you should go grab
#her and ditch the fireworks

#maybe remy thinks that vara might open up more if she meets a human? maybe requires that you give the eggs to
#the hatchery? maybe she actually does open up more because she recognizes you when you found her
#with her dead mother?

label eval_hatchery_visited: #This is only to incorporate the declaration of a variable
    m "It wasn't until now that I noticed Vara looking at me curiously."
    $ evalHatcheryVisited = True
    return

label eval_remy_ch4_date_change: #This changes up the end of Remy's date to account for the secret ending
    if persistent.evalSecretEndingUnlocked and evalHatcheryVisited and varasaved:
        if persistent.evalSecretEndingCompleted:
            play sound "fx/system3.wav"
            s "It seems that you have already seen the true ending for TDOMI. Would you like to experience it again or the normal turn of events?"

            menu:
                "True ending path.":
                    pass
                
                "Normal ending path.":
                    return

        $ renpy.pop_call()
        Ry "Speaking of Vara, why don't we go grab her?"
        c "How come?"
        Ry "When you went and visited the hatchery earlier, Vara seemed very interested in you."
        Ry shy "You've done miracles to help me move on from my past, and I was thinking you could do the same for her as well."
        c "I did notice her looking at me earlier. I would love to try and help if I could."
        c "But what about the festival?"
        Ry normal "Well, if you still want to go, we could watch the big fireworks show together in a few days."
        c "That's an idea."
        Ry smile "Alright, let's grab Vara."
        show remy normal with dissolvemed
        m "I watched Remy as he got up, stretching himself in a way that reminded me of a cat before we prepared to leave."

        scene town7 with dissolveslow
        $ renpy.pause (0.5)
        show remy normal at right with easeinright
        show zhong normal c flip at left with easeinleft
        c "Oh, you're still here. How's business?"
        Fv "As expected. People always get hungry at these events eventually."
        Fv "Can I offer you some more meat balls?"
        Ry "No, thanks. I'm quite full from my earlier helping."
        Fv "How about you, [player_name]?"
        c "A tempting offer, but we're just about to call it a day."
        Fv "I see. Are you going to watch the big fireworks at the end of the festival?"
        c "That's the plan."
        Fv "Be sure not to miss it. You haven’t seen anything until you see the fireworks!"
        c "That's what everyone keeps telling me."
        Ry smile "Because it's true."
        show remy normal with dissolve
        c "Anyway, we should probably get going."
        Fv "Have a good day, then."
        c "You too."
        show zhong normal c at left with dissolvemed
        hide zhong with easeoutleft
        Ry "I think it'll be faster if I fly down to the hatchery to grab Vara and meet you at your place."
        c "Sounds like a plan."
        show remy normal flip at right with dissolvemed
        hide remy with easeoutright
        $ renpy.pause (1.0)
        play sound "fx/takeoff.ogg"
        m "With a running start, Remy took off into the air."
        scene black with dissolvemed
        m "It didn't take long to make it back to my apartment."
        m "I was surprised to find that Remy was already there with Vara."

        scene evalplayerapt2 with dissolveslow
        show remy normal with dissolvemed
        show vara smnormal with dissolvemed
        c "Hello, Vara."
        Vr "..."
        Ry "Took you long enough to get here."
        c "Hey! In my defense, I don't have wings."
        Ry "And in my defense I had to carry Vara on my back. You can really feel every pound of extra weight in the air."
        c "Can she not fly on her own?"
        Ry smile "She's learning, but still a bit too young."
        Ry normal "She'll be ready to go to flight school in a year or so."
        c "Flight school?"
        Ry "It's a three month training course where young dragons learn how to safely fly. They even learn to perform some maneuvers and tricks."
        Ry look "Do you not have that back home?"
        c "Remy, look at me. Does it look like humans would need flight school?"
        Ry smile "You do make a good point."
        c "Although, you aren't entirely wrong. People could take schooling to learn how to fly giant, mechanical machines."
        Ry normal "I think I read about those in your PDAs."
        c "They're a hassle. I would much rather have wings like you."
        Ry "I think I'll stick with my wings as well."
        c "Here, why don't we go inside instead of standing out here all day."
        Ry smile "Sure. Come on, Vara."
        Vr "..."
        scene black with dissolveslow
        play sound "fx/door/doorchain.ogg"
        scene o4 with dissolveslow
        show vara smnormal flip at left with dissolvemed
        show remy normal at right with dissolvemed
        c "I'm sorry, Vara. I don't think I ever properly introduced myself. I'm [player_name]."
        Vr "..."
        Ry "Could you say [player_name]'s name, Vara?"
        Vr "..."
        c "It's okay. I'm shy around strangers myself."
        Ry "You seem to be doing quite alright in a world full of complete strangers."
        c "You guys are so much nicer than most humans. Plus, it feels much easier talking to a different species."
        Ry look "Strange, I feel the same way."
        c "Now, Remy. Did you want to clean out my bathroom cabinent as well or something?"
        Ry smile "That's a good one."
        show remy normal with dissolvemed
        Ry "This may surprise you, but no. I think I'll let you make the call on what dragon medications you should take."
        c "(I don't even want to imagine the terrible repercussions that could have.)"
        Ry "You know, maybe I should have just brought Vara to the park and had her watch the fireworks with us instead of coming back here."
        c "Don't say that. We're still going to see the fireworks together."
        c "We can bring Vara as well, I think it would be fun!"
        Ry smile "That's true."
        Ry normal "You know, I'm very curious to see what your reaction to that will be. It's quite a sight to behold."
        c "People just keep saying that."
        Ry "Maybe you will, too."
        c "We'll see."
        show vara smshocked b flip with dissolvemed
        m "Vara, with a distraught look, opened her mouth and pointed at it."
        Ry "Oh, I think Vara is a bit hungry. Would you mind if she had a quick snack?"
        c "Of course not! I still have plenty of food left, even after you raided my pantry."
        Ry look "If you ate any of the things I threw out, you would be in the hospital right now."
        c "I know, I'm kidding."
        Ry normal "I'm not."
        scene black with dissolveslow
        m "We made our way into the kitchen."

        scene evalplayerkitchen with dissolveslow
        show remy normal at right with dissolvemed
        show vara smnormal flip at left with dissolvemed
        Ry "Well, Vara, go ahead."
        hide vara with easeoutright
        play sound "fx/fridge.mp3"
        m "Vara made her way over to the fridge and grabbed a few ingredients."
        Ry "I don't think I ever mentioned this, but Vara loves to prepare her own food."
        Ry smile "She's her own little chef! Sometimes she even makes things for the other orphans."
        c "That's so sweet."
        Ry normal "She's quite good, too."
        show vara smnormal at Position (xpos=0.9) with easeinright
        m "Vara walked up to Remy and poked his side."
        Ry "I think she needs some help to reach the cabinents and the countertop."
        show vara smnormal flip at Position (xpos=0.9) with dissolvemed
        show remy normal flip behind vara at right with dissolvemed
        hide vara with easeoutright
        hide remy with easeoutright
        m "Remy walked over to the countertop near the cutting board. Then, Vara climbed up on his back."
        c "You make a great stepping stool, Remy."
        Ry look "Thanks?"
        m "Vara laid her ingredients out on the countertop and grabbed a knife."
        c "(Oh my goodness, the little dragon has a knife.)"
        c "You really trust her with a knife like that?"
        Ry normal "She's been doing this for a long time now. I trust her."
        c "If you say so."
        m "Vara set the knife on the cutting board."
        m "From her ingredients, she chose what looked to be a cucumber."
        play sound "fx/cuttingboard.mp3"
        m "Grabbing the knife in her muzzle, Vara dexterously cut it lengthwise and put it to the side."
        m "Then, without letting go of the knife, Vara grabbed some sort of fish out of a bag and cut it into thin slices."
        c "How was the fish not expired, Remy?"
        Ry "Our fish can last for months refrigerated."
        m "Vara proceeded to grab a long, thin green sheet of a substance similar to seaweed and rested rice evenly on top."
        c "Is that seaweed?"
        Ry look "What's seaweed?"
        c "An underwater plant that looks exactly like that."
        Ry normal "Well, this is algae. It's popular among water dragons."
        c "I see."
        m "Vara carefully distributed the cucumber and fish into the middle of the sheet."
        m "She rolled it so the algae formed a barrier around the other ingredients."
        c "Oh! It's sushi! I can't believe I didn't notice that earlier!"
        m "Vara hopped off of Remy's back with the knife still in her mouth."
        m "Remy grabbed the cutting board with the sushi and brought it over to the table."
        show remy normal at right with easeinright
        show vara smnormal at left with easeinright
        show vara smnormal flip at left with dissolvemed
        $ evalVaraMood = 2
        Ry smile "Impressive, isn't it?"

        menu:
            "Looks amazing.":
                $ evalVaraMood += 2
                c "I'll say! That looks wonderful."
                m "I saw the corners of Vara's mouth form a small smile."
            
            "It looks alright.":
                $ evalVaraMood += 1
                c "It looks good."
            
            "I could have done better.":
                $ evalVaraMood -= 1
                c "I think I could have done better myself."
                Ry look "Is that so?"
                Vr smsad flip "..."
                show remy normal with dissolvemed
        
        play sound "fx/cuttingboard.mp3"
        m "Vara started carefully cutting the sushi roll. In the end, there were ten bite-sized pieces."
        $ renpy.pause (0.5)
        m "Once finished, she rested the knife down and popped a piece of the sushi in her mouth."
        show vara smnormal flip with dissolvemed
        m "Seemingly satisfied, she ate two more in rapid succession."
        $ renpy.pause (1.0)
        Ry normal "Could I have one, Vara?"
        m "Vara nodded. Remy grabbed a piece of sushi and put it in his mouth."
        Ry "Wow! It's really good Vara!"
        m "Remy took another two pieces, and Vara suddenly pushed the cutting board in my direction."
        Ry "I think she wants you to try it, [player_name]."

        menu:
            "Sure!":
                $ evalVaraMood += 2
                c "I'd love to."
                m "I grabbed a piece of sushi and looked at it for a moment."
                show vara smnone flip with dissolvemed
                m "Vara looked extremely nervous as I put the piece of sushi in my mouth."
                m "It was amazing. The buttery fish complemented the somewhat tangy taste of the algae and the crispness of the cucumber."
                c "Wow, Vara! This is really good!"
                show vara smnormal flip with dissolvemed
                if evalVaraMood > 4:
                    Vr smnone flip "T... T..."
                    Vr smnormal flip "Thanks."
                    c "You're welcome, Vara. I really mean it too."
                    Ry smile "You should be honored, [player_name]. Vara doesn't just speak to everyone."
                    c "After everything she's been through, I can't blame her."
                else:
                    Vr smnormal "..."
                m "I grabbed another piece and started eating."
                c "Would anyone else like any more?"
                Vr "..."
                Ry normal "I think it's all yours."
                c "Not that I mind."
                m "I quickly finished off the remaining pieces of sushi."
                m "Remy then washed off the cutting board and put it back on the counter."
            
            "If I have to.":
                c "If I have to..."
                m "I tenatively grabbed a piece of sushi and looked at it for a moment."
                show vara smnone flip with dissolvemed
                m "Vara looked extremely nervous as I put the piece of sushi in my mouth."
                m "It was amazing. The buttery fish complemented the somewhat tangy taste of the algae and the crispness of the cucumber."
                c "Wow, Vara! This is really good!"
                show vara smnormal flip with dissolvemed
                if evalVaraMood > 4:
                    Vr smnone flip "T... Th..."
                    Vr smnormal flip "Thanks."
                    c "You're welcome, Vara. I really mean it too."
                    Ry smile "You should be honored, [player_name]. Vara doesn't just speak to everyone."
                    c "After everything she's been through, I can't blame her."
                else:
                    Vr smnormal "..."
                m "I grabbed another piece and started eating."
                c "Would anyone else like any more?"
                Vr "..."
                Ry normal "I think it's all yours."
                c "Not that I mind."
                m "I quickly finished off the remaining pieces of sushi."
                m "Remy then washed off the cutting board and put it back on the counter."

            "No thank you.":
                $ evalVaraMood -= 1
                c "I'm not hungry right now."
                Ry look "Oh, okay then."
                Vr smsad flip "..."
                m "Vara and Remy shared the remaining pieces of sushi and washed off the cutting board."

        
        m "We made our way back to the main room."
        scene o3 with dissolveslow
        show vara smnormal flip at left with dissolvemed
        show remy normal at right behind vara with dissolvemed
        Ry "Well, it's getting to be Vara's bedtime, so we best get going."
        c "I understand."
        if evalVaraMood > 4:
            play sound "fx/fireworks2.ogg"
            Vr smshocked flip "..."
            m "What must have been the finale fireworks for the day's show seemed to frighten Vara."
            hide vara with dissolvemed
            show vara smshocked at right with dissolvemed
            Ry "It's alright, Vara. It's just some fireworks."
            Vr "..."
            play sound "fx/hug.mp3"
            m "Remy hugged Vara with his wings, and she seemed to settle down."
            show vara smnormal with dissolvemed
            m "I turned my gaze to face the two dragons."
            hide remy
            hide vara
            with dissolvemed
            show remy normal behind vara
            show vara smnormal
            with dissolvemed

            stop music fadeout 2.0
            $ renpy.pause (2.0)
            c "Wait a minute..."
            m "My vision started going blurry."
            Ry look "Are you alright, [player_name]?"
            c "I..."
            show vara smnormal ghost with dissolvemed
            $ renpy.pause (4.0)
            show vara smnormal with dissolvemed
            scene black with dissolvemed
            play sound "fx/impact.wav"
            $ renpy.pause (2.0)
            m "I feel to the floor unconscious."
            $ renpy.pause (1.0)
            m "I awoke when I felt a strange pressing senastion on my cheek."
            m "It was Vara, who looked down at me with a concerened expression."
            scene o3 with dissolveslow
            show remy look with dissolvemed
            show vara smshocked with dissolvemed
            play music "mx/flashback.ogg"
            Vr "..."
            c "Ugh, how long was I out for?"
            Ry "Just a few minutes."
            Ry "[player_name], what was that?"
            c "I..."
            m "My mind was foggy. Faint memories of something were rolling around inside my head."
            c "I think I'm remembering something. Something important."
            Ry "What do you mean?"
            c "I'm not quite sure myself."
            Ry "Do you need to go to the hospital? Do you think it was the sushi?"
            Vr smsad "..."
            c "No, it wasn't the sushi."
            show vara smnone with dissolvemed
            c "I saw something. I just need my mind to clear up."
            c "Let me sleep on it."
            Ry "Well, I refuse to leave you alone after that incident."
            c "Well, I guess you'll just have to sleep here for the night then."
            Ry normal "I guess I will."
            c "What about Vara?"
            Ry "Vara, would you like to stay here or go back to the orphanage."
            Vr smnone "Here..."
            show vara smnormal with dissolvemed
            Ry "Alright, Vara. Let's get ready for bed, then."
            m "The two dragons started making their way over to the couch."
            if remystatus == "neutral":
                m "My mind still spinning, I made my way into the bedroom."
                play sound "fx/undress.ogg"
                m "I quickly undressed, and too tired to prepare any further, fell asleep."
                scene black with dissolveslow
            else:
                menu:
                    "Let them have the couch.":
                        m "My mind still spinning, I made my way into the bedroom."
                        play sound "fx/undress.ogg"
                        m "I quickly undressed, and too tired to prepare any further, fell asleep."
                        scene black with dissolvemed
                    
                    "Share the bed.":
                        c "Hey, wait."
                        c "Why don't we share the bed? I don't want you both to have to share that tiny couch."
                        Ry smile "I could even keep a closer eye on you as well. What do you say, Vara?"
                        m "Vara nodded."
                        Ry normal "I guess that decides it."
                        hide remy with dissolvemed
                        hide vara with dissolvemed
                        m "The three of us made our way into the bedroom."
                        m "Too tired to even take off my clothes, I lay down on the bed."
                        m "Remy removed his tie and rested it on the nightstand."
                        show remy normal b with dissolvemed
                        Ry "Can't have this on while I sleep."
                        c "It doesn't look like the most comfortable sleeping attire."
                        hide remy with dissolvemed
                        m "Remy climbed up onto the bed next to me."
                        m "Vara followed closely behind and wedged her way between Remy and I."
                        Vr "Warm..."
                        m "She snuggled a bit closer to me."
                        Ry "Look's like you're Vara's personal pillow with a built in heater."
                        c "I don't mind."
                        Ry "It seems that she's taken a liking to you, [player_name]."
                        c "I'm glad."
                        Ry "Goodnight, [player_name]."
                        c "Goodnight, Remy."
                        c "And goodnight to you as well, Vara."
                        Vr "..."
                        scene black with dissolveslow
            stop music fadeout 2.0
            jump eval_remy_ch4_date_change_2
        else:
            Ry "Goodbye, [player_name]. I'll see you around."
            c "Likewise."
            Ry "Can you say goodbye, Vara?"
            if evalVaraMood == 0:
                Vr smgrowl "{i}grrrrrrr{/i}"
                Ry look "I guess not..."
            else:
                Vr smnone "..."
                Ry look "I guess not..."

            show vara smnormal with dissolvemed
            hide vara with easeoutright
            hide remy with easeoutright
            play sound "fx/door/doorchain.ogg"
            $ renpy.pause (3.0)
            play sound "fx/takeoff.ogg"
            m "With that, Remy and Vara left."
            jump eval_post_date_change

    else:
        return

label eval_remy_ch4_date_change_2:
    $ renpy.pause (3.0)
    scene o with dissolveslow
    play music "mx/basicguitar.ogg"
    m "I woke up to find that I was alone in the bed."
    c "(How long did I sleep?)"
    m "I got up and walked out into the main room. Remy was sitting on the couch."
    show remy normal with dissolvemed
    Ry "You sleep like a brick."
    c "I was tired, okay?"
    Ry smile "I tried pushing you and talking to you, but nothing would make you budge."
    c "I get it. Where's Vara?"
    Ry normal "I brought her back to the orphanage."
    if remystatus != "neutral": #Obligatory inclusion of the kiss scene. Can't be the fourth date without it, really
        c "You know, Remy. You looked good without your tie."
        Ry "Well, actually..."
        hide remy with dissolvemed
        play sound "fx/undress.ogg"
        $ renpy.pause (2.0)
        show remy smile b with dissolvemed
        Ry "How about now?"
        c "You are pretty cute, you know that?"
        Ry normal b "Is that just a term of endearment, or are you actually serious?"
        c "I am serious."
        m "He looked at me, hesitating. Then, he took a step forward, his head slowly moving closer to my own."
        show remyrom at Pan ((580, 326), (350, 0), 8.0) with fade
        $ renpy.pause (6.0)

        menu:
            "Look away.":
                hide remyrom
                hide remy
                with fade
                $ renpy.pause (0.3)
                m "When I made the motion to dodge his advance, he stopped in his tracks immediately."
                show remy shy b with dissolvemed
                Ry "I'm sorry, I just thought..."
                c "Don't worry about it. I'm just not sure if I can do this."
                Ry normal b "I understand."
                hide remy with dissolvemed
                play sound "fx/undress.ogg"
                m "Remy put his tie back on."
                show remy normal with dissolvemed
                $ renpy.pause (1.0)
            
            "Kiss him.":
                hide remyrom
                hide remy
                with fade
                $ renpy.pause (0.3)
                m "We met, and my arms enveloped his nack as our lips touched. For a few seconds, we were closer than ever before. During the kiss, he used a lot more tongue than I was expecting."
                m "Just after we parted, he finished by giving me a small lick on the cheek."
                show remy smile b with dissolvemed
                Ry "How was that?"
                c "Unique, that's for sure."
                Ry normal b "Maybe I shouldn't wear the tie anymore if this is what happens when I take it off."
                c "Actually, I think you should keep it."
                Ry "Really?"
                c "Yeah. It looks good on you."
                Ry smile b "Well, if you say so."
                hide remy with dissolvemed
                play sound "fx/undress.ogg"
                m "Remy put his tie back on."
                $ remystatus = "good"
                show remy normal with dissolvemed
                $ renpy.pause (1.0)

    Ry look "But now that you're rested. What happened last night?"
    c "I'm still not sure..."
    c "I think I saw Vara, but she was a ghost."
    Ry "A ghost?"
    c "Yes, when she stood beside you it looked exactly like when..."
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    m "Suddenly, it hit me."
    play music "mx/judgement.ogg"
    c "The big fireworks show, Remy."
    c "Vara dies."
    Ry "What?"
    Ry angry "How?" with Shake ((0, 0, 0, 0), 2, dist=10)
    c "I... I can't recall. But it's our highest priority to keep her safe."
    Ry look "How should we do that?"
    c "I don't think I can tell the police. I doubt they would believe me."
    Ry "So it's up to us."
    c "I guess it is."
    Ry sad "I don't know if you or I can protect her."
    Ry "Maybe we should just have Adine take care of her."
    c "We are the only ones who know about what will happen, so we should be the only ones who take care of her."
    Ry "Why don't you just tell Adine?"
    c "I don't think she'll believe me."
    c "But I know that deep down, you believe me."
    Ry "I do. I've been having strange dreams about Vara as well."
    c "Really?"
    Ry "Yes. However, all I can recall is a feeling of loneliness."
    c "Well, with this insight let's hope that those dreams don't become a reality."
    Ry look "But how are we supposed to save Vara?"
    c "I don't know. I think our best bet would be to bring her with us when we see the fireworks that day."
    Ry "We're still going to do that?"
    c "Something tells me that we need to. I can't explain it, but I know we need to."
    Ry "But what if she dies because she goes with us? What then?"
    c "What are our other options?"
    Ry "We could lock her up somewhere in the orphanage."
    c "Do you trust that she couldn't escape?"
    Ry sad "No."
    Ry "She seems to be quite afraid of the fireworks, so recently she's been sleeping with me."
    Ry look "Something tells me she would somehow escape and come looking for me if we left her alone that night."
    Ry sad "And that cannot be good."
    c "She can escape through a locked door?"
    Ry look "She's a water dragon. She can spit acid to melt the door lock to the point where she can open it."
    c "Has she done this before?"
    Ry "Not to that extent. When a dragon first starts experimenting with their fire or acid breath, there can be a few... accidents."
    Ry "We have more fire extinguishers and anti-burn kits on hand at the orphanage than they do at the hospital."
    c "But what makes you think she can suddenly learn to spit acid on command?"
    Ry "Most of us learn how to control that ability under high amounts of stress or pressure."
    c "I see..."
    Ry sad "I'm scared, [player_name]. I don't want to lose Vara."
    c "You won't. I promise."
    m "Remy took a deep breath and wiped away a few tears."
    Ry look "Maybe you're right."
    Ry "I know I couldn't do this alone. But with you? I think we have a chance."
    c "Glad to hear that, Remy. You're a lot braver than you make youself out to be."
    Ry normal "Well, you're making me work double-time here. Before you, I didn't have to worry about all of this nonsense."
    Ry "But you know what? I wouldn't have it any other way."
    if remystatus != "neutral":
        m "Remy gave me a playful lick on the cheek."
    Ry "I'm still stressed beyond belief, but let's not let this impact us too heavily."
    Ry "We have to stay strong to protect Vara."
    c "I agree."
    Ry "I better get going. I told Emera I was going to be a bit late, but I didn't expect our conversation to take this long."
    c "I understand. Stay strong, Remy."
    Ry "You too, [player_name]. I'll be ready."
    stop music fadeout 2.0
    scene black with dissolvemed
    $ evalPathToSecretComplete = True
    jump eval_post_date_change

label eval_post_date_change: #Skips back to character select after the changed ch4 Remy date
    $ renpy.pause (2.0)

    $ remyscenesfinished = 4

    if chapter4unplayed == False:

        jump chapter4chars

    elif chapter3unplayed == False:

        jump chapter3chars

    elif chapter2unplayed == False:

        jump chapter2chars

    else:
        jump chapter1chars

label eval_secret_ending_extra_day: #Scrapping this most likely
    m "Hey! Eval here. Sorry to rip you out of my amazing AWSW extended universe like this, but I'm thinking of scrapping the extra thing with Adine and Xith all together."
    m "It just doesn't really have a place in the story any more."
    m "I don't know, though. Please let me know if you would like to see it after you play the true ending as well."
    m "Btw to get the true ending right now, replay Remy's fourth date."
    m "I'm currently working on this content. Check back in 3-5 business days."
    m "As cliche as that sounds, It'll probably be even less time :)"
    return