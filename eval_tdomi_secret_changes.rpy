#A list of everything required to get the secret ending:
    #Complete solo Remy and Remy + Amely endings
    #Complete Remy + Amely + Adine ending with perfect scores in both minigames and hugging Remy
    #Visit the hatchery to drop off the eggs
    #Save vara by following her out of the store


#Add 3P scene after the hatchery in which Remy convinces Adine not to fly due to her injurues
# (reference "what will the children do if you get hurt, or worse")

#Remy's 4th date, make it so that when Remy mentions Vara, he decides that the two of you should go grab
#her and ditch the fireworks

#maybe remy thinks that vara might open up more if she meets a human? maybe requires that you give the eggs to
#the hatchery? maybe she actually does open up more because she recognizes you when you found her
#with her dead mother?
label eval_c4_hatchery_init:
    
    if c4sectionsplayed==0:
        #call eval_tdomi_common from eval_tdomi_common_init
        $ eval_c4_hatchery_done=False
        $ eval_c4_hatchery_adinestatus=adinestatus
    else:
        #a hack to fix c4hatcheryplayed not being updated if the hatchery is your second pick
        if not c4hatcheryplayed and mcfirst and not c4hatcheryavailable:
            $ c4hatcheryplayed=True

        if c4hatcheryplayed and not renpy.python.store_dicts["store"].get("eval_c4_hatchery_done",True):#if you played the hatchery but haven't seen the extra scene
            if remystatus!="bad"and remystatus!="abandoned"and remygoodending or persistent.remygoodending:#if you have been doing at least OK with Remy
                $ eval_c4_hatchery_done=True
                stop music fadeout 2.0
                scene black with dissolveslow
                jump eval_hatchery_extension
    label eval_c4_hatchery_init_return:
        pass
label eval_hatchery_visited:
    if not renpy.python.store_dicts["store"].get("evalFixDoubleOrphanageLine", False) and varasaved:
        m "It wasn't until now that I noticed Vara looking at me with a curious expression."
        m "I wonder what that's about."
        $ evalFixDoubleOrphanageLine=True
    label eval_hatchery_visited_next:
        pass
#Extra stuff to explain why Adine doesn't die because why not
label eval_hatchery_extension:
    scene evalorphlight with dissolveslow
    show remy normal flip at left
    show vara smnormal flip at left
    if adinestatus=="bad":
        show adine annoyed b at right
    else:
        show adine normal b at right
    show amely smnormal at right
    with dissolvemed
    play music "mx/neptune.mp3" fadein 2.0

    if adinestatus=="bad":
        Ad "Ugh, I'm glad they're gone."
        Ry look flip "What's wrong with [player_name]?"
        if eval_c4_hatchery_adinestatus=="abandoned":#if adine's status is bad because you told here you do not want to see her again at the hatchery
            Ad disappoint b "They said that they didn't want to see me again."
            Ad sad b "I didn't know I was such bad company."
            Ry "You're not, Adine. [player_name] is going through a lot at the moment, and probably needs time alone to think."
        else:#if you were a jerk to her during a date
            Ad disappoint b "They acted like I was bad company."
            Ry "You're not, Adine. [player_name] is going through a lot at the moment."
        Ad disappoint b "You may be right, but it still hurts."
            
    elif adinestatus=="none":#"none" in code means neutral, "neutral" in code shows as good, and "good" means impressed
        Ad "They seem nice enough."
        Ry "I'm glad to hear that." #Bleah, change this.
        Ad disappoint b "Sorry, Remy, but I don't know how much I can help out today. Work has been getting to me lately."
        Ry look flip "That's not good."
    else:
        Ad giggle b "I'm glad [player_name] stopped by to visit. It's nice having their company."
        Ry smile flip "Agreed."
        Ad disappoint b "Sorry, Remy, but I don't know how much I can help out today. Work has been getting to me lately."
        Ry look flip "That's not good."
    Ry normal flip "Here, I think I know what will help."
    play sound "fx/hug.mp3"
    hide remy with dissolvemed
    $ renpy.pause (1.5)
    show remy normal flip behind vara at left
    show adine giggle b
    with dissolvemed
    Ad "I guess you were right, that did help."
    Ry smile flip "Glad I could be of assistance."
    Am "I want hug!"
    Ad normal b "Okay, Amely."
    play sound "fx/hug.mp3"
    hide adine with dissolvemed
    $ renpy.pause (1.5)
    show adine normal b at right behind amely with dissolvemed
    Am "Yay!"
    Ry "How about you, Vara?"
    Vr smnone flip "..."
    play sound "fx/hug.mp3"
    hide remy with dissolvemed
    $ renpy.pause (1.5)
    show remy normal flip behind vara at left
    show vara smnormal flip
    with dissolvemed
    Ad giggle b "Hugs all around."
    Ry smile flip "Indeed."
    Ry normal flip "Adine, there's something I would like to discuss with you quickly."
    Ad normal b "What is it, Remy?"
    Ry "I've noticed that your wing has been sagging recently. Is everything alright?"
    Ad "Yeah, I just strained it while practicing my routine for the upcoming flight competition."
    Ry look flip "Please tell me you aren't thinking of participating in the competition with your wing in the state it is."
    Ad giggle b "Don't worry about me, Remy. I'll be fine."
    Ry "Adine, I'm serious. I don't think you should enter the competition this year."
    Ad disappoint b "I... just have to try, you know?"
    Ry "What if something goes wrong, though? You don't want to be in that position."
    Ad "If I start making excuses now, maybe I'll never stop. I'll always be too nervous, or too injured, or didn't eat right the day before."
    Ad "I need to take this opportunity, Remy. Because if I don't now, maybe I never will."
    Ry sad flip "But Adine, think of the children here."
    Ad frustrated b "Don't you dare bring them into this! They have nothing to do with it."
    show amely smsad
    show vara smsad flip
    with dissolvemed
    Ry "If something happens to you, I don't know what any of us would do."
    Ry "I couldn't support the orphanage without you, and you would crush the hearts of Vara and Amely."
    Ad sad b "Remy, don't say that. I would never leave you three."
    Ad disappoint b "I just want to do more with my life. I want to be more than just a server and a delivery girl making minimum wage."
    Ad "Is this one opportunity to do something more with my life really too much to ask for?"
    Ry look flip "If you tell them you're injured, they might let you fly another year instead. You shouldn't taint your flying reputation by attempting tricks with an injured wing."
    Ad frustrated b "I don't want to wonder if I'll ever amount to anything more than a waitress. I want to be able to follow my dream, and I don't want to wait another year to find out."
    Ad "You mean a lot to me, Remy. But I won't let you get in the way of my-{w=0.5}{nw}"
    Am "I'm scared."
    Ad sad b "No, Amely, there's no reason to be scared. I'm just..."
    $ renpy.pause (2.0)
    Ad disappoint b "I need to give this some thought."
    Ad "I need to go now. I'll see you around."
    show adine disappoint b flip with dissolvemed
    Ry sad flip "Wait, Adine."
    Ad "What?"
    Ry "Just know that we care about you. I can't just watch you crash and burn without attempting to intervene."
    Ad "Thank you Remy. I just need time to think over all of this."
    hide adine with easeoutright
    play sound "fx/door/door_chain.ogg"
    Vr "..."
    Am "Adine leaving?"
    Ry look flip "Don't worry you two. I know that Adine will make the right decision when the time comes."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (0.5)
    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
    jump c4sections
label eval_c4_adine4_change:
    if not renpy.python.store_dicts["store"].get("eval_c4_hatchery_done",False):
        label eval_c4_adine4_change_fail:
            pass
    show adine think b with dissolve
    Ad "This spot should be good."
    c "what made you reconsider?"
    Ad disappoint b "When I was inside and had a bit of time to think."
    Ad "about what you said, what Remy said, and then I spoke with some of the other competitors."
    Ad "they told me that stunt flying with an injured wing could easily lead to tragedy"
    Ad "someone even suggested that I stay grounded untill my wing fully heals"
    c "How do you feel now?"
    Ad "I know it was the right thing to do, but I can't help thinking that I just came so close. That I could've done it if I hadn't been injured."
    c "You'll get another chance, I promise."
    Ad "Don't make a promise you can't keep."
    c "..."
    label eval_c4_adine4_change_success:
        pass

label eval_remy_ch4_date_change: #This changes up the end of Remy's date to account for the secret ending
    if persistent.evalSecretEndingUnlocked and c4hatcheryplayed and varasaved:
        if persistent.evalSecretEndingCompleted:
            play sound "fx/system3.wav"
            s "It seems that you have already seen the true ending for This Dragon Owes me Ice Cream. Would you like to experience it again or the normal turn of events?"
            menu:
                "True ending path.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    $ renpy.pause (1.0)
                "Normal ending path.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    $ renpy.pause (1.0)
                    label eval_remy_ch4_date_change_fail:
                        pass

        Ry "You know, speaking of Vara, why don't we go grab her?"
        c "How come?"
        Ry "When you went and visited the hatchery earlier, she seemed very interested in you."
        Ry shy "You've done miracles to help me with my past, and I was thinking you could do the same for her as well."
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
        Vr smnone "..."
        show vara smnormal with dissolvemed
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
        c "Although, you aren't entirely wrong. People can have schooling to learn how to fly giant, mechanical machines."
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
        show vara smnone flip at left with dissolvemed
        Vr "..."
        Ry "Could you say [player_name]'s name, Vara?"
        Vr "..."
        c "It's okay. I'm shy around strangers myself."
        Ry "You seem to be doing quite alright in a world full of complete strangers."
        c "I guess you're right, but in a way it feels much easier talking to someone of a different species."
        Ry look "Strange, I feel the same way."
        c "Now, Remy. Did you want to clean out my bathroom cabinet while you're here?"
        Ry smile "That's a good one."
        Ry normal "This may surprise you, but no. I think I'll let you make the call on what dragon medications you should take."
        if renpy.python.store_dicts['store'].get('medunstaken', True):
            c "(I don't even want to imagine the terrible repercussions that could have.)"
        else:
            m "I recalled that I had attempted this earlier, and it wasn't a pretty result."
            c "(I probably shouldn't do that again.)"
        show vara smshocked b flip with dissolvemed
        m "Vara, with a distraught look, opened her mouth and pointed at it."
        Ry "Oh, I think Vara is a bit hungry. Would you mind if she had a quick snack?"
        c "Of course not! I still have plenty of food left, even after you raided my pantry."
        Ry look "If you ate any of the things I threw out, you would be in the hospital right now."
        c "I know, I'm kidding."
        Ry normal "I'm not."
        scene black with dissolveslow
        scene evalplayerkitchen with dissolveslow
        show remy normal at right
        show vara smnormal flip at left
        with dissolvemed
        Ry "Well, Vara, go ahead."
        Vr smsmile flip "..."
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
        show vara smnormal flip at Position (xpos=0.9)
        show remy normal flip behind vara at right
        with dissolvemed
        hide vara
        hide remy
        with easeoutright
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
        c "How did the fish not expire, Remy?"
        Ry "Our fish can last for months refrigerated."
        m "Vara proceeded to grab a thin, green sheet of a substance similar to seaweed and rested precooked rice evenly on top."
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
        $ evalVaraMood=1
        Ry smile "Impressive, isn't it?"

        menu:
            "Looks amazing.":
                $ evalVaraMood +=2
                c "I'll say! That looks wonderful."
                show vara smsmile flip with dissolvemed
            
            "It looks alright.":
                $ evalVaraMood +=1
                c "It looks good."
            
            "I could have done better.":
                $ evalVaraMood -=1
                c "I think I could have done better myself."
                Ry look "Is that so?"
                Vr smsad flip "..."
                show remy normal with dissolvemed
        
        play sound "fx/cuttingboard.mp3"
        m "Vara started carefully cutting the sushi roll. In the end, there were ten bite-sized pieces."
        $ renpy.pause (0.5)
        m "Once finished, she rested the knife down and popped a piece of the sushi in her mouth."
        m "Seemingly satisfied, she ate two more in rapid succession."
        $ renpy.pause (1.0)
        Ry normal "Could I have one, Vara?"
        m "Vara nodded."
        m "Remy grabbed a piece of sushi and put it in his mouth."
        Ry "Wow! It's really good!"
        m "Remy took another two pieces, and delicately rested them on his tongue."
        m "Vara pushed the cutting board in my direction."
        Ry "I think she wants you to try it, [player_name]."

        menu:
            "Sure!":
                $ evalVaraMood +=2
                c "I'd love to."
                m "I grabbed a piece of sushi and looked at it for a moment."
                show vara smnone flip with dissolvemed
                m "Vara looked at me nervously as I put the piece of sushi in my mouth."
                m "It was amazing. The buttery fish complemented the somewhat tangy taste of the algae and the crispness of the cucumber."
                c "Wow, Vara! This is really good!"
                if evalVaraMood >=4:
                    Vr "..."
                    Vr smnone flip "T... {w}T..."
                    Vr smsmile flip "Thanks."
                    c "You're welcome, Vara. I really mean it too."
                    Ry smile "You should be honored, [player_name]. Vara doesn't just speak to everyone."
                    c "After everything she's been through, I can't blame her."
                else:
                    Vr smnormal "..."
                m "I grabbed another piece and started eating."
                c "Would anyone else like more?"
                Vr "..."
                Ry normal "I think it's all yours."
                c "Not that I mind."
                m "I quickly finished off the remaining pieces of sushi."
                m "Remy then washed off the cutting board and put it back on the counter."
            
            "If I have to.":
                c "If I have to..."
                m "I tentatively grabbed a piece of sushi and looked at it for a moment."
                show vara smnone flip with dissolvemed
                m "Vara looked extremely nervous as I put the piece of sushi in my mouth."
                m "It was amazing. The buttery fish complemented the somewhat tangy taste of the algae and the crispness of the cucumber."
                c "Wow, Vara! This is really good!"
                show vara smnormal flip with dissolvemed
                if evalVaraMood >=4:
                    Vr smnone flip "T... Th..."
                    Vr smnormal flip "Thanks."
                    c "You're welcome, Vara. I really mean it too."
                    Ry smile "You should be honored, [player_name]. Vara doesn't just speak to everyone."
                    c "After everything she's been through, I can't blame her."
                else:
                    Vr smnormal flip "..."
                m "I grabbed another piece and started eating."
                c "Would anyone else like more?"
                Vr "..."
                Ry normal "I think it's all yours."
                c "Not that I mind."
                m "I quickly finished off the remaining pieces of sushi."
                m "Remy then washed off the cutting board and put it back on the counter."

            "No thank you.":
                $ evalVaraMood -=1
                c "I'm not hungry right now."
                Ry look "Oh, okay then."
                Vr smsad flip "..."
                m "Vara and Remy shared the remaining pieces of sushi and washed off the cutting board."

        
        scene black with dissolveslow
        scene o3 with dissolveslow
        show vara smnormal flip at left
        show remy normal at right behind vara
        with dissolvemed
        Ry "Well, it's getting to be Vara's bedtime, so we best get going."
        c "I understand."
        if evalVaraMood > 0:
            play sound "fx/fireworks2.ogg"
            $ renpy.pause (1.5)
            Vr smshocked flip "..."
            m "What must have been the finale for the day's firework show seemed to frighten Vara."
            show vara at right with move
            show vara smshocked with dissolvemed
            Ry "It's alright, Vara. It's just some fireworks."
            Vr "..."
            play sound "fx/hug.mp3"
            m "Remy embraced Vara with his wing and she seemed to settle down."
            show vara smnormal with dissolvemed
            m "I turned my gaze to face the two dragons."
            show remy normal behind vara at center
            show vara smnormal at center
            with move

            stop music fadeout 2.0
            $ renpy.pause (3.0)
            c "Wait a minute..."
            m "My vision started going blurry."
            Ry look "Are you alright, [player_name]?"
            c "I..."
            $ renpy.pause (2.0)
            show vara smnormal ghost with dissolvemed
            $ renpy.pause (4.0)
            show vara smnormal with dissolvemed
            scene black with dissolvemed
            play sound "fx/impact.wav"
            $ renpy.pause (2.0)
            m "The world around me went black as I fell to the floor, unconscious."
            m "I awoke when I felt a strange pressing sensation on my cheek."
            m "It was Vara, who looked down at me with a concerned expression."
            scene o3
            show remy look
            show vara smshocked
            with dissolvemed
            play music "mx/flashback.ogg"
            Vr "..."
            c "Ugh, how long was I out for?"
            Ry "Just a few minutes."
            Ry "[player_name], what was that?"
            c "I..."
            m "My mind was foggy. Faint memories flickered in my head."
            c "I think I'm remembering something. {w}Something important."
            Ry "What do you mean?"
            c "I'm not quite sure myself."
            Ry "Do you need to go to the hospital? Do you think it was the sushi?"
            Vr smsad "..."
            c "No, it wasn't the sushi."
            c "I saw something. I just need my mind to clear up."
            show vara smnone with dissolvemed
            c "Let me sleep on it."
            Ry "I refuse to leave you alone after what just happened."
            c "Remy, I'll be alright."
            Ry "No. We don't know what that was, and I can't risk leaving you alone and having something happen to you."
            c "Well, I guess you'll just have to sleep here for the night then."
            Ry normal "I guess I will."
            c "What about Vara?"
            Ry "Vara, would you like to stay here or go back to the orphanage?"
            Vr smnone "Here..."
            show vara smnormal with dissolvemed
            Ry "Alright, Vara. Let's get ready for bed, then."
            m "The two dragons started making their way over to the couch."
            if remystatus=="neutral":
                m "My mind still spinning, I made my way into the bedroom."
                play sound "fx/undress.ogg"
                m "I quickly undressed and, too tired to prepare any further, fell asleep."
                scene black with dissolveslow
            else:
                menu:
                    "Let them have the couch.":
                        play sound "fx/undress.ogg"
                        m "I watched as Vara hopped up onto the couch while Remy removed his tie and glasses."
                        hide vara with dissolvemed
                        m "While they were a bit cramped, the two dragons seemed rather comfortable snuggled close together."
                        c "Goodnight you two."
                        Ry smile "Goodnight, [player_name]."
                        m "My mind still spinning, I made my way into the bedroom."
                        play sound "fx/undress.ogg"
                        m "I quickly undressed and, too tired to prepare any further, fell asleep."
                        scene black with dissolvemed
                    "Share the bed.":
                        $ evalRemyDateBed=True
                        c "Hey, wait."
                        c "Why don't we share the bed? I don't want you both to have to share that tiny couch."
                        Ry smile "I could keep a closer eye on you as well. What do you say, Vara?"
                        m "Vara nodded."
                        Ry normal "I guess that decides it."
                        hide remy
                        hide vara
                        with dissolvemed
                        m "The three of us made our way into the bedroom."
                        m "Too tired to even take off my clothes, I laid down on the bed."
                        play sound "fx/undress.ogg"
                        m "I watched as Remy removed his tie and placed it on the nightstand next to the bed."
                        m "Remy climbed up onto the bed next to me."
                        m "Vara followed closely behind and wedged her way between Remy and I."
                        Vr smnormal "..."
                        m "Vara snuggled a bit closer to me, seemingly attracted to my body heat."
                        Ry smile "It seems that she's taken a liking to you, [player_name]."
                        m "I looked down at Vara, who was snuggled against my side."
                        c "It seems that way."
                        m "Remy let out a big yawn. As if contagious, I did as well."
                        Ry smile "Goodnight, [player_name]."
                        c "Goodnight, Remy."
                        c "And goodnight to you as well, Vara."
                        Vr smnormal "..."
                        scene black with dissolveslow
            stop music fadeout 2.0
            $ renpy.pause (4.0)
            jump eval_remy_ch4_date_change_2
        else:
            Ry "Goodbye, [player_name]. I'll see you around."
            c "Likewise."
            Ry "Can you say goodbye, Vara?"
            if evalVaraMood < 0:
                play sound "fx/growl.ogg"
                $ renpy.pause (2.0)
                Ry look "I guess not..."
            else:
                Vr smnone flip "..."
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
        jump eval_remy_ch4_date_change_fail

label eval_remy_ch4_date_change_2:
    $ renpy.pause (3.0)
    scene o with dissolveslow
    play music "mx/basicguitar.ogg"
    if evalRemyDateBed:
        m "I woke up to find that I was alone in the bed."
        c "(How long did I sleep?)"
    else:
        m "I woke up with the sun shining brightly through the blinds."
        c "(How long did I sleep?)"
    m "I got up and walked out into the main room. Remy was sitting on the couch."
    show remy smile with dissolvemed
    Ry "Hi there, sleepy head!"
    c "Good morning. Where's Vara?"
    Ry normal "I think you mean good afternoon. I brought her back to the orphanage."
    m "Remy let out a long sigh."
    Ry look "You know, maybe I shouldn't have mentioned Vara at all yesterday. I feel partially responsible for everything that happened."
    Ry "I feel bad for forcing you to miss out on the show."
    c "Don't say that. How were you supposed to know that I was going to pass out? Plus, we're still going to see the fireworks together."
    c "We can bring Vara as well, I think it would be fun!"
    Ry look "That's true, but you know how I feel. I guess I just wanted to make the most of our outing yesterday."
    if remystatus == "good": #Obligatory inclusion of the kiss scene. Can't be the fourth date without it, really
        c "Speaking of which, I've never actually seen you without your tie."
        Ry normal "Well, actually..."
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
                $ remystatus="neutral"
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
                $ mp.remyromance=True
                $ evalRemyRomance = True
                $ mp.save()
                hide remyrom
                hide remy
                with fade
                $ renpy.pause (0.3)
                m "We met, and my arms enveloped his neck as our lips touched. For a few seconds, we were closer than ever before. During the kiss, he used a lot more tongue than I was expecting."
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
                $ remystatus="good"
                show remy normal with dissolvemed
                $ renpy.pause (1.0)

    stop music fadeout 2.0
    Ry look "But now that you're rested. What happened last night?"
    c "I'm still not sure..."
    c "I think I saw Vara, but she was a ghost."
    Ry "A ghost?"
    c "Yes, when she stood beside you it looked exactly like when..."
    $ renpy.pause (2.0)
    m "Suddenly, it hit me."
    play music "mx/judgement.ogg"
    c "The big fireworks show, Remy. {w}Vara dies."
    Ry "What?"
    show remy angry with dissolvemed
    Ry "HOW?" with hpunch
    c "I... I can't recall. But we need to protect her."
    Ry sad "How would we do that?"
    c "I don't think I can tell the police. I doubt they would believe me."
    Ry "Maybe we should just have Adine take care of her."
    c "I don't think she'll believe me either."
    Ry "Really?"
    c "I don't think so."
    Ry "But what made you so certain that I would believe you?"
    c "I don't know, but I had a feeling that you would."
    Ry "Well, I do. I've been having strange dreams about Vara as well."
    c "Really?"
    Ry "Yes. However, all I can recall is a feeling of loneliness."
    c "Well, that lines up with her death."
    Ry "So it's up to us to save her?"
    c "I guess it is."
    Ry sad "I don't know if you or I can protect her."
    c "I don't know. I think our best bet would be to bring her with us when we see the fireworks that day."
    Ry look "We're still going to do that?"
    c "Something tells me that we need to. I can't explain it, but I know that it must be done."
    Ry sad "But what if she dies because she goes with us? What then?"
    c "What are our other options?"
    Ry "We could lock her up somewhere in the orphanage."
    c "Do you trust that she couldn't escape?"
    Ry "No."
    Ry "She seems to be quite afraid of the fireworks, so recently I've been sleeping at the orphanage with her."
    Ry look "Something tells me she would somehow escape and come looking for me if we left her alone that night."
    Ry sad "And that cannot be good."
    c "She can escape through a locked door?"
    Ry look "She's a water dragon. She can spit acid to melt the door lock to the point where she can open it."
    c "Has she done this before?"
    Ry "Not to that extent."
    Ry "When a dragon first starts experimenting with their fire or acid breath, there can be a few... accidents."
    Ry "We have more fire extinguishers and anti-burn kits on hand at the orphanage than they do at the hospital."
    c "But what makes you think she can suddenly learn to spit acid on command?"
    Ry "Most of us learn how to control that ability under high amounts of stress or pressure."
    c "I see..."
    Ry sad "I'm scared, [player_name]. I don't want to lose Vara."
    c "We won't. I promise."
    m "Remy took a deep breath and wiped away a few tears."
    Ry look "Maybe you're right."
    Ry "I know I couldn't do this alone, but with you? I think we have a chance."
    c "Glad to hear that, Remy. You're a lot braver than you make yourself out to be."
    Ry "Well, you're making me work double-time here. Before you, I didn't have to worry about all of this nonsense."
    Ry normal "But you know what? I wouldn't have it any other way."
    if remystatus=="good":
        m "Remy gave me a playful lick on the cheek."
    Ry "I'm still stressed beyond belief, but let's not let this impact us too heavily."
    Ry "We have to be ready to protect Vara."
    Ry look "From an unknown force, nevertheless."
    c "I agree."
    Ry normal "I better get going. I told Emera I was going to be a bit late, but I didn't expect our conversation to take this long."
    c "I understand. Stay strong, Remy."
    Ry "You too, [player_name]. I'll be ready."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ evalPathToSecretComplete=True
    jump eval_post_date_change

label eval_post_date_change: #Skips back to character select after the changed ch4 Remy date
    $ renpy.pause (2.0)
    $ remyscenesfinished=4
    if chapter4unplayed==False:
        jump chapter4chars
    elif chapter3unplayed==False:
        jump chapter3chars
    elif chapter2unplayed==False:
        jump chapter2chars
    else:
        jump chapter1chars

label eval_remy_good_ending_change: #And so the contruction of a completely new ending for Remy begins...
    if not evalPathToSecretComplete:
        label eval_remy_good_ending_change_fail:
            pass
    show black with dissolvemed
    $ renpy.pause (0.5)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

    $ save_name=(_("Chapter 5 - Remy"))

    play sound "fx/door/doorbell.wav"
    $ renpy.pause(1.0)

    c "(That must be them.)"
    stop sound fadeout 0.5
    $ renpy.pause(0.4)
    play sound "fx/door/handle.wav"
    $ renpy.pause(1.0)

    show remy look
    show vara smnormal
    with dissolvemed
    Ry "I'm nervous, [player_name]."
    c "I am too, but I'm ready."
    c "Does Vara know?"
    m "Remy stared intently at me."
    Ry "That we're going to see the fireworks tonight? She does."
    show vara smnone with dissolvemed
    m "I understood what he meant."
    c "Don't worry, Vara. We'll be there for you to comfort you during the show."
    show vara smnormal with dissolvemed
    m "She looked a little less concerned after I said that."
    Ry normal "Alright, let's get going."
    scene black with dissolveslow
    $ renpy.pause (0.5)
    scene viewingspot with dissolvemed
    play music "mx/amb/night.ogg" fadein 5.0
    m "After a few minutes of walking, we arrived at a rather empty looking area near the edge of town."
    c "Looks deserted to me. I thought everyone was watching the fireworks."
    show remy normal
    show vara smnormal
    with dissolvemed
    Ry "They are, but they're doing it somewhere else. I don't really like crowds, and it just feels much safer out here."
    c "Better safe than sorry, at any rate."
    Ry look "That's what I'm thinking."
    Ry normal "Oh, I think it's starting. Now, watch!"
    play soundloop "fx/fireworks3.ogg"
    m "We were quiet as we waited and the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."
    m "More rockets followed, their thunderous noise echoing throughout the land."
    show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
    $ renpy.pause (6.0)
    stop music fadeout 2.0
    hide fireworks with dissolveslow
    m "Suddenly, a terrible realization hit me."
    stop soundloop fadeout 1.0
    play music "mx/judgement.ogg" fadein 0.5
    m "Considering how public of an event this was and how I was told multiple times that everyone would be watching the fireworks, now would be the best time for Reza to do anything he planned to do."
    m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."
    m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."
    c "Remy, I think we need to go. Now."
    m "Remy instinctively got in a defensive position around Vara."
    show vara smshocked
    show remy angry
    with dissolvemed
    Ry "What? Where?"
    c "What we were talking about earlier. I know how it happens."
    Ry "Why didn't you say anything before?"
    c "Because I didn't figure it out until now."
    c "I know where Reza is. We need to stop him."
    Vr smshocked b "..."
    Ry look "Reza? Are you sure?"
    c "The fireworks are the perfect cover for gunshots and his passage through the portal."
    Ry "You have a good point."
    Ry shy "But I'm not sure if I could fight him."
    c "Me neither. If I bring you there, he probably won't hesitate to shoot."
    Ry sad "Maybe you can hold him off and I'll try to get some help."
    c "But I can't think of anyone who would believe us."
    Ry look "I can."
    c "Alright, you go do that. I'll hold him off as long as I can."
    Ry sad "Good luck, [player_name]."
    Vr smsad "Scared..."
    m "Vara escaped from Remy's protective grasp and ran over to me."
    hide vara with dissolvemed
    m "She pressed her head into my idly open hand. I could feel tears forming in her eyes."
    c "It'll be alright, Vara. I promise everything will be okay."
    m "I gently rubbed her head."
    Ry "Come on, Vara. Let's go help [player_name]."
    show vara smsad with dissolvemed
    m "Vara returned to Remy, and the two dragons rushed off in the other direction."
    show vara smsad flip
    show remy sad flip
    with dissolvemed
    hide remy
    hide vara
    with easeoutright
    scene black with dissolveslow
    stop music fadeout 2.0
    $ renpy.pause (3.0)

    #Add a POV that isn't from the MC's POV. Oooo, fancy! - Maverick shouldn't be wearing his badge. Have something where Remy goes looking for Maverick and catches him snooping at the PD
    play music "mx/prayer.ogg" fadein 2.0
    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
    $ renpy.pause(2.0)
    show remy look at right
    show vara smsad at right
    with easeinright
    Ry "Hello?"
    show maverick normal b flip at Position (xpos = 0.1) with easeinleft
    Mv nice b flip "What are you doing here, Remy? Why aren't you two seeing the fireworks?"
    Ry "Reza is at the portal as we speak."
    Mv normal flip "What?"
    Mv "How do you know this?"
    Ry "[player_name] told me."
    Mv angry b flip "What?"
    Mv "How do they know, then?"
    Ry "When we were watching the fireworks, [player_name] noticed that the noise was a perfect opportunity for Reza to escape."
    Mv "And where is [player_name] now?"
    Ry "At the portal to distract Reza."
    Mv "And you really believe them?"
    Ry sad "What do you mean?"
    Mv angry b flip "Remy, can you not see that [player_name] is in on all of this as well?"
    Mv rage b flip "He played you! He used you to escape with Reza and the generators!"
    Ry "Maverick, that's not tr-{w=0.5}{nw}"#a "-" implies they were cut off
    Mv "Isn't it so convenient that [player_name]'s little plan involves both himself and Reza alone near the portal?"
    show remy angry with dissolvemed
    Ry "{size=+20}STOP!{/size}" with hpunch
    show maverick angry b flip with dissolvemed
    Ry "You do not understand {size=+20}ANYTHING{/size} about [player_name], Maverick."
    Ry "Without them, I wouldn't be here."
    Ry "Without them, I would be hanging limp from my ceiling."
    Mv scared b flip "What do you mean, Remy?"
    Ry "I've gone through hell and back, and you know very well why."
    Ry "I was close to the edge, Maverick. Close to ending it once and for all."
    Ry "But you know what? [player_name] saved my life."
    Ry "They helped me reunite with old friends, move on from the past, and find this lovely little dragon next to me."
    Mv "I... I didn't know it was that bad, Remy. I'm so sorry."
    Ry "Feel bad for me later, Maverick. We have to help [player_name]."
    Mv normal flip "I can't say I fully trust [player_name], Remy, but I'll still help you."
    Vr "I help?"
    Ry sad "Vara, you should stay here where you'll be safe."
    Vr "..."
    Ry "I promise, Vara. We will come back when it's safe."
    Vr "..."
    Ry "Come on, Maverick. Let's go."
    Mv normal b flip "Okay, Remy. I'm with you."
    hide remy
    hide maverick
    with easeoutright
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    Vr smgrowl "I help."
    show vara smgrowl flip with dissolvemed
    hide vara with easeoutright
    scene black with dissolveslow

    #Back to MC POV
    $ renpy.pause (0.5)
    scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    $ renpy.pause (3.5)
    call endingjustafewminuteslater from _call_endingjustafewminuteslater_eval
    m "He was right."
    m "What could I do to stop him? I had stalled for as long as I could, but Remy still hadn't returned."
    m "He had a gun, and I had nothing."
    c "(Remy, you need to hurry up.)"
    c "I don't think I can do anything, can I?"
    play sound "fx/rev.ogg"
    Rz gunself "You can. Take those generators and walk to the portal. No sudden movements or I shoot."
    m "I carefully walked over and picked up the generators."
    show izumi normal behind reza at Position(xpos=1.25, xanchor='center')
    show reza at Position(xpos=0.45, xanchor='center') with ease
    m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."
    show izumi normal at right with ease
    As "Stop, Reza."
    play sound "fx/rev.ogg"
    show reza gunpoint flip with dissolvemed
    m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."
    Rz "Who the fuck are you? Freeze! I said freeze!"
    show izumi at Position(xpos=0.8, xanchor='center') with ease
    $ persistent.izumiseen = True
    As "Want to waste your bullets on me? Feel free."
    Rz gunpoint flip "If you say so."
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)
    play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact3.ogg"
    hide izumi with easeoutbottom
    m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."
    $ persistent.izumiseen=True
    show izumiinjured4 at Pan((300, 0), (600, 608), 7.0) with fade
    $ renpy.pause (5.0)
    hide izumiinjured4
    show reza gunself
    with dissolveslow
    Rz "Enough with your tricks, [player_name]. Let's go."
    m "Reza escorted me outside, his gun barrel trained on my skull."
    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene np1r flip at Pan((400, 0), (100, 100), 6.0) with dissolvemed
    stop music fadeout 2.0
    play music "mx/amb/night.ogg" fadein 5.0
    $ renpy.pause (5.0)
    show reza gunself with dissolvemed
    Rz "Move."
    m "I picked up my pace to the portal."
    $ renpy.pause (2.0)
    play sound "fx/bush.mp3"
    m "I suddenly heard a soft movement in the nearby brush."
    m "Reza must have as well."
    stop music fadeout 2.0
    show reza gunpoint flip with dissolvemed
    show reza gunpoint with dissolvemed
    show reza gunpoint with dissolvemed
    play music "mx/termination.ogg" fadein 2.0
    Rz "What the hell?"
    Rz gunself "You brought them to me, didn't you?"
    Rz "{size=+10}Traitor!{/size}" with hpunch
    play sound "fx/gunshot2.wav"
    m "A searing pain shot through my back. I recoiled and fell to the ground."
    $ renpy.pause (0.5)
    play sound "fx/impact3.ogg"
    $ renpy.pause (1.0)
    show reza gunpoint at Position(xpos=0.8) with move6
    $ renpy.pause (2.0)
    play sound "fx/gunshot2.wav"
    $ renpy.pause (1.0)
    play sound "fx/impact3.ogg"
    m "He pulled the trigger a second time, and I heard a dull thud come from the bushes."
    m "Suddenly, a flurry of gray rushed at Reza."
    show maverick angry b flip at Position(xpos=0.65, xanchor='center') with easeinleft
    play sound "fx/impact3.ogg"
    show maverick rage b at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top")
    show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top")
    with move9
    queue sound "fx/bite.ogg"
    m "Maverick pounced, snarling, and knocked Reza to the ground before embedding his teeth into the body before him."
    m "Despite his thrashing and screaming, Reza held tightly onto the gun and aimed at Maverick."
    m "I crawled over to the fight, desperate in my attempts to disarm Reza."
    m "I wasn't going to make it. Reza's gun was aimed at Maverick's forehead."
    play sound "fx/acid.mp3" fadein 0.5
    m "From a different direction, a ball of liquid flew at Reza's gun hand."
    m "Upon contact, Reza's skin started to boil."
    m "Reza expressed no signs of pain, and I noticed a strange metallic sheen and sparks flying from his hand."
    # m "Maverick wrenched the gun out of his grasp with his teeth and tossed it to the side."
    m "Maverick sunk his teeth into Reza and attempted to wrench the weapon out of his. However, Reza held an iron grip on the gun."
    m "Some of the acid must have made contact with Maverick's maw as well."
    play sound "fx/dragonpain.wav"
    m "Maverick released his grip and held onto his muzzle in pain."
    m "Within an instant, Reza made a break for the portal."
    play sound "fx/acid.mp3" fadein 0.5
    m "Another ball of acid flew at Reza, hitting his foreleg."
    play sound "fx/impact3.ogg"
    m "This time, Reza screamed in pain and dropped to the ground."
    play sound "fx/gunshot2.wav"
    m "On impact, a single shot was fired off in front of him."
    play sound "fx/portalhit.mp3"
    m "Sparks flew from the portal's terminal as the bullet pierced the metal frame and lodged itself within its inner mechanisms."
    c "(That can't be good.)"
    m "He clutched his burning leg in agony, the acid melting away at his skin and muscle."
    m "Weakly, he crawled towards the portal, but his movements soon grew sluggish as he slumped to the ground, motionless."
    show maverick rage d at Position(xpos = 0.9, xanchor = "center") with easeinright
    stop music fadeout 2.0
    $ renpy.pause (3.0)
    play music "mx/infinite.mp3" fadein 1.0
    Mv "Damn! That hurts!"
    Mv "What the hell burned my mouth so badly?"
    #play sound "fx/bite.ogg" This was a previous rendition where Reza didn't escape and was killed. This is too close to the true ending, so he had to escape
    #m "In another swift motion, Maverick's jaws clamped down on Reza's neck."
    #m "Reza fell limp on the ground."
    show vara smshocked b with easeinright
    Vr "Remy!"
    hide vara with easeoutleft
    m "Vara rushed over to the bushes Maverick had emerged from. She returned with Remy, who was limping and bloody."
    show remy sad eval shot flip at Position(xpos=0.1) with easeinleft
    show vara smshocked flip behind remy at left with easeinleft
    Mv scared c "Oh, Remy!"
    c "You're injured."
    Ry look eval shot flip "So are you."
    c "We need to stop the bleeding."
    m "I put some pressure on his wound, momentarily halting the blood that was trickling down his body."
    c "Can you do this?"
    Ry "Let me try."
    m "He felt around his side, trying to get the right grip before he applied pressure on his own. I let go, and after a bit of adjustment, Remy could stop the bleeding on his own for now."
    play sound "fx/undress.ogg"
    m "I took off my shirt and briefly considered whether I would be able to use it to dress Remy's wound, but I soon realized it was not long enough to wrap around him properly."
    m "Instead, I used the shirt to curb my own bleeding, folding it and wrapping it around my abdomen tightly."
    Ry sad eval shot flip "We did it, [player_name]."
    c "Yes we did, Remy."
    Mv "Are you two alright?"
    Ry look eval shot flip "I've been better."
    Ry "How about you? I heard you scream in pain."
    Mv normal c "I think a bit of Vara's acid got onto my face. It hurts like hell, but I'll live. Let me get the EMTs."
    Ry "Thank you, Maverick."
    show maverick normal d flip with dissolvemed
    hide maverick with easeoutright
    Vr "..."
    Ry sad eval shot flip "Vara, you silly girl. Why did you follow us?"
    Vr smsad flip "I... help."
    Ry "You could have gotten hurt! Or worse..."
    c "Remy. She saved Maverick's life."
    Ry look eval shot flip "Really?"
    c "Yes. She hit Reza's gun with her acid."
    c "If she weren't there, Maverick would have been shot."
    m "I pointed to Reza's body."
    c "She also managed to stop Reza from escaping through the portal."
    c "Without her, all of this would have been a complete failure."
    Ry sad eval shot flip "Wow, Vara. That was very brave of you."
    Vr "..."
    Ry "I'm proud of you."
    m "With effort, he bent down and gave the little dragon a kiss on the cheek."
    show vara smsad flip behind remy at Position(xpos=-0.1) with move
    m "Vara snuggled closer to Remy and buried her face in his side."
    m "Suddenly, the Administrator appeared next to me."
    if persistent.remybadending:#if you have seen remy's bad ending, you know the administrator's real name
        define As=Character(_("Izumi"), color="#d2d9ff", image="izumi")
    if persistent.annabadending==True:
        show izumi normal 4 d at Position(xpos=0.9) with easeinright
    else:
        show izumi normal 4 c at Position(xpos=0.9) with easeinright
    As "This is not right."
    c "What do you mean?"
    show vara smgrowl flip at Position(xpos=-0.1) with dissolvemed
    play sound "fx/growl.ogg"
    show vara smgrowl flip at left with move
    $ renpy.pause (1.5)
    c "Vara, It's okay. She's a friend."
    show vara smnone flip at left with dissolvemed
    Ry look eval shot flip "Who are you?"
    As "That does not matter at the moment."
    As "Vara should be dead."
    show remy sad eval shot flip with dissolvemed
    $ renpy.pause (0.5)
    As "How did this happen?"
    c "I knew that she would die."
    As "What?"
    c "When I saw Remy and Vara together in my apartment. I guess it reminded me of something."
    As "Something, as in a ghostly image?"
    c "Yes, I saw Vara resembling a ghost."
    As "Hmm... you must have experienced fragments of this timeline in a previous one."
    As "That was no ghost you saw, but it was Vara in this timeline."
    c "But why would the fragmentation of this time appear as a ghost as well?"
    As "It did not, but rather your mind referenced the fragment from a previous timeline in this current one."
    As "That ghost you saw was actually a memory from a previous timeline."
    As "Sometimes, these fragments will make their way through displaced wormholes and manifest in the form of visions or thoughts."
    if loremscenesfinished > 1:
        c "Ipsum discussed these wormholes with me earlier. I think I understand."
        Ry "I think I'm missing something here."
        c "I'll explain it to you later, Remy."
    else:
        c "Wormholes?"
        As "There's someone here who could do a much better job explaining this than I could."
    m "Her voice wavered, and her legs started shaking."
    c "Are you okay?"
    As "My time here is limited. I will not be alive for much longer."
    As "There are emergency coordinates in the portal."
    As "They are tied to your biometric data, and will send you back to the day you arrived in this world."
    $ renpy.pause (1.5)
    hide izumi with easeoutbottom
    play sound "fx/impact3.ogg"
    m "The Administrator suddenly fell to the ground."
    show vara smshocked flip with dissolvemed
    if persistent.annabadending == True:
        As normal 4 d "You will know what to do, [player_name]."
    else:
        As normal 4 c "You will know what to do, [player_name]."
        c "But-{w=0.5}{nw}"
    m "With that, she closed her eyes and her body went limp."

    stop music fadeout 3.0
    $ renpy.pause (0.5)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    nvl clear
    window show
    n "Soon, more help arrived. Remy and I got all the medical attention we needed while Vara was sent to Adine to be taken care of."
    n "Maverick had only sustained minor burn injuries and abrasions. However, Reza and Izumi were both dead."
    n "I warned the dragons about the comet, telling them to check the PDAs I had given them for verification of my claims."
    n "A few minutes later, EMTs arrived and I was put into a medically induced coma due to my injuries."
    n "In the weeks I was out, a number of things happened."
    n "Out of respect, Reza's body was given a proper funeral in a remote location. His weapon and remaining ammunition were to be left in my care."
    n "After attempts were made to make contact with the human world, it was discovered that the portal was no longer operational."
    window hide
    nvl clear
    window show
    n "Upon this discovery, the dragons sent their brightest engineers in attempts to establish a connection with the human world."
    n "However, after weeks of unsuccessful attempts, the operation was deemed to be a failure."
    n "Ultimately, the dragons decided to leave the portal standing in its current state."
    n "Fortunately, my claims were taken seriously, and there was already a plan in place to divert the comet."
    n "Using the lab's generators, the dragons were successfully able to redirect the comet's path away from Earth."
    window hide
    nvl clear
    window show
    n "After I awoke from my coma, I had to consider what my future held."
    n "With my limited knowledge of the portal, there was very little possibility of fixing it without the expertise of the dead Administrator.."
    n "Any possibilities of my return to the human world had vanished with the destruction of the portal."
    n "I met with Remy as soon as I could, who told me about what I had missed."
    window hide
    nvl clear
    $ renpy.pause (2.0)
    $ evalDoingSecretEnding=True

    jump eval_post_secret_remy_meeting

label eval_post_secret_remy_meeting:
    $ persistent.evalSecretEndingCompleted=True
    scene park2 with dissolveslow
    show remy normal with dissolvemed
    play music "mx/library.ogg" fadein 2.0
    c "So, the comet has been diverted. I guess I must've been out for a long time."
    Ry look "Yes you were. A lot has happened since then."
    Ry normal "By the way, I talked with Maverick a few days ago."
    c "Oh, what did he have to say?"
    Ry "I think it would be better if he explained himself."
    show remy normal at right with move
    show maverick normal b flip at Position (xpos=0.1) with easeinleft
    Mv "Hello, [player_name]."
    c "Hello, Maverick."
    Mv "Listen, [player_name]. I think I owe you an apology."
    Mv "This whole time I thought you were putting on an act."
    Mv "Trying to impress everyone and get on their good side."
    Mv "I never stopped to think that maybe you were just a nice person."
    Mv "Remy had some things to say about you."
    Mv scared b flip "Some things I'll never forget."
    Mv normal b flip "And I want to give you my sincerest apologies."
    c "I forgive you, Maverick. I can understand how you felt." #Possible to add a choice here to just deny him
    c "With all of the uncertainty and confusion surrounding that time, distrust was inevitable."
    c "I'm just glad we can put this all behind us and move on."
    Mv nice b flip "Me too, [player_name]."
    Mv normal b flip "I'd love to stick around and chat, but Bryce needs me back at the station."
    Ry smile "I'm glad you two were able to settle your differences."
    c "Me too. See you around, Maverick."
    show maverick normal b with dissolvemed
    hide maverick with easeoutleft
    show remy smile at center with move
    Ry normal "What will you do now, [player_name]?"
    c "I don't know. As you probably have heard, the portal is no longer operational."
    Ry sad "I know, and I'm sorry. I can't imagine how terrible it must feel knowing that you have no way to save humanity."
    m "I can't give up hope now. Maybe they just missed an emergency failsafe only intended for myself to discover."
    c "Do you think we could look at the portal?"
    Ry look "Of course. Although I doubt we're going to fix anything a team of our most talented engineers couldn't."
    scene black with dissolveslow
    scene np1x
    show remy look
    with dissolveslow
    Ry "Here we are. What were you interested in looking at?"
    c "Let me get a closer look."
    hide remy with dissolvemed
    play sound "fx/evalgrasswalk2.ogg"
    m "I made my way over to the portal while Remy made himself comfortable in the grass."
    scene black with dissolve
    scene evalportalb at Pan ((0, 0), (600, 380), 4.0) with dissolveslow
    $ renpy.pause (4.0)
    m "Aside from a few meager attempts to put the portal's terminal back together, the components still lay in tatters."
    m "I attempted to interact with the terminal. However, I received no response."
    m "Looking down again, I noticed a small bullet hole near the base of the terminal's housing."
    c "(So that's where Reza's final bullet landed.)"
    m "The damage it had caused wasn't pretty. It had managed to pierce through the metal frame and much of the hardware."
    m "In one last desperate attempt, I tried the terminal screen again."
    m "There was no response."
    m "With a sigh of defeat, I made my way back over to Remy."
    scene black with dissolveslow
    play sound "fx/evalgrasswalk2.ogg"
    $ renpy.pause (1.0)
    scene np1x
    show remy normal
    with dissolveslow
    Ry "So, any luck?"
    c "No, I don't think there's any way to fix the portal and travel back to the day I came here without the help of the dead Administrator."
    Ry "Wait, go back to the day you got here? Doesn't that imply time travel?"
    c "Yes. The portal can be used to manipulate time."
    Ry "I guess that makes sense. In most circumstances, the probability for an alien life form to be able to live in the conditions of another planet would be astronomically low."
    Ry "However, if you instead came from another time period on Earth, then it would make sense why you are accustomed to our environment."
    Ry look "You know, if you were supposed to go back to the day you came here, does that mean that you have done this before?"
    c "Yes. I mean, I think so. The memories are vague."
    Ry "Did things happen the same way they did here?"
    c "I really can't remember. The only thing I can say for sure is that at some point, Vara was dead."
    Ry "Then that must mean that alternate timelines exist."
    Ry "And in that case, if you've experienced something as significant as Vara dying, what's to say that other factors couldn't change in those timelines as well?"
    c "What do you mean by that?"
    Ry normal "Well, it's quite possible that in one of those timelines, you save humanity as well."
    m "I pondered what Remy had just said. It seemed crazy, yet it also made too much sense."
    c "Huh. Guess you're right."
    Ry "You don't have to go back and attempt to fix everything, especially if it's no longer possible."
    Ry "You've done everything you could, and you managed to save all of dragonkind in the process."
    Ry smile "Besides, I would be more than happy to have you stay here with us."
    scene black with dissolveslow

    # More scrapped stuff
    #c "That is true, but I can't help thinking that there could have been a solution that saved both worlds."
    #Ry "Whatever you want to do now, you can be sure that you'll have the council's support."
    #Ry "You could just stay here if you wanted to."
    #c "I bet you and Vara wouldn't mind that, would you?"
    #Ry smile "You know how I am. Humans just fascinate me."
    #Ry "And you are the only person, other than myself and Adine, that Vara seems to have taken a liking to."
    #Ry normal "This isn't just about us, though. Of course we would love it if you stayed with us, but I know there are many other factors at play here, and that it won't be an easy decision for you to make."
    #Ry "Don't let us stop you from going back if that's what you want to do, though. We'll be fine."
    #c "Are you sure about that?"
    #Ry "Yes. After all, I have Vara to keep me company."
    #Ry "Also, while you were busy these last few weeks, I spent a lot of time with Adine, and we rekindled our lost friendship."
    #Ry smile "Besides, if you really go back in time, I'll see you again."
    jump eval_tdomi_remy
#Thus marks the end of the changes required to actually get Vara's extended ending
