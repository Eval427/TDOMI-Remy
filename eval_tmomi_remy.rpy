label eval_tmomi_remy:

    #So you're taking a peek at the code, eh? Well, enjoy all my comments, cause I'm not gonna delete anything

    #Current Issues:
        #Custom sounds and backgrounds arent working FIXED - NEVERMIND NOT FIXED - HAHA FIXED
        #I have no idea what to do for the orphanage
        #You can't pause or save during the mod? What? FIXED
        #Music stops when scrolling through previous text FIXED
        #Is it possible to change scenes without fading out characters?

    #TODO:
        #Add music - working on it!
        #Add skips
        #Add transitional pans to scenes
        #Adjust transitions to be smoother
        #Finish this lol

    #Plot issue of other kids in the orphanage:
        #After the incident at the portal, the children were put into emergency foster care outside of the town and still have not returned
        #Amely stayed because they couldn't find a place for her, but Remy and Adine agreed to take care of her

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
    Ry sad "Please tell me this isn't anything too serious. I don't think I could take much more at the moment."
    c "There is a dragon..."
    c "And that dragon..."
    $ renpy.pause (2.0)
    play music "mx/jazzy.ogg"
    c "Owes me ice cream."
    Ry look "Ice cream?"
    Ry normal "Oh, you mean Katsuharu. I haven't had anything from him in quite some time."
    c "Well, I was offered as much ice cream as I could eat, and still need to take him up on his offer."
    Ry "Can I ask why exactly he agreed to give you so much ice cream? I've seen your appetite, and it's quite impressive. Especially for such a small form."

    menu:
        "Are you calling me fat?":
            Ry shy "N... No of course not, I didn't mean it that way... I just meant..."
            c "I'm kidding, don't sweat it."
            Ry normal "Dragons don't sweat."
            c "Noted."
        
        "Thanks...":
            Ry shy "Hey! I didn't mean it that way!"
            c "Sure you didn't."

        "Hey, in my defense, that was some really good cooking.":
            Ry smile "Why thank you. I have been cooking for myself for a while, it's nice to know that my food still holds up strong with other people."
    
    show remy normal with dissolveslow
    c "Anyways, to make matters short, I gave him some advice about location, and it seemed to put him back on the radar."
    Ry "Where did you tell him to move?"
    c "Here. Tatsu Park."
    Ry "I find it strange that he didn't think to move to Tatsu Park earlier."
    c "When you've been doing something as long as Katsuharu and develop a routine, it's probably quite difficult to notice those things." #Gonna want to change this a bit
    Ry "I guess you're right."
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
            $ currentending = 1
            jump eval_solo_remy_1
        
        "We should bring Amely along with us.":
            c "Why don't we go together with Amely? She's a hatchling, so I'm sure she would love to go and get some ice cream with us. Especially from the renowned Katsuharu."
            Ry smile "Good idea. You know, I'm not even sure if she has ever had ice cream before. Usually, the young dragons at the orphanage don't get the opportunity to go out and enjoy even the most basic things like ice cream."
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
            $ currentending = 2
            jump eval_remy_amely_1

        "Why don't we invite Amely and Adine?" if persistent.adinegoodending:
            c "Why don't we take Adine and Amely as well? As a little hatchling, I'm sure that Amely would love to go and get some ice cream, and Adine has done so much for the both of us."
            Ry "It's been ages since I've had the opportunity to sit down and have a little get-together with everyone. Work, especially since Reza, has been particularly chaotic. It would be nice for the four of us to have a nice day out."
            c "Couldn't agree more. Being in a coma for the last few months, I feel like I've missed out on so much. It would be nice to talk over some nice ice cream."
            Ry look "Hmmm... We may have to wait a little bit, Adine is probably busy on her shift delivering food."
            c "Good point..."
            Ry normal "You know, we could make ourselves useful at the orphanage until she is off her shift. She usually comes down to check on things as soon as she's done, and it may be a nice surprise for her to find us there."

            menu:
                "Sure":
                    c "Sure. I've always been curious about the orphanage. I've heard a lot about it but I haven't gotten the opportunity to visit."
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
                        "Stop Remy":
                            c "Wait! Remy!"
                            play sound "fx/evalgrasswalk2"
                            m "Remy looked at me and walked back over."
                            $ renpy.pause (1.0) #This should fix it? No? Fixed. I'm an idiot
                            show remy look with dissolvemed #Wtf is happening here?
                            Ry "What?"
                            c "I'm sorry, you're right. It was extremely selfish of me to prioritize my own enjoyment over that of yours and the childrens'."
                            Ry normal "I'm glad to hear that. I was worried for a second that you really were just that unkind."
                            c "No, I think I just overreacted. Human children can be a complete nightmare sometimes."
                            Ry "Well, so can dragon children, but you just learn to accept that they haven't had as much time on the planet as us, and sometimes have difficulty expressing their emotions in other ways."
                            c "I guess..."
                            Ry smile "Plus, I think this experience will be a lot more fun than you think"
                            c "You're probably right."
                            Ry normal "Great, we can start making our way over there now!"
                            jump eval_trip_to_orphanage
                        
                        "Let him leave":
                            play sound "fx/takeoff.ogg"
                            m "I silently watched as Remy extended his wings and flew off to the orphanage."
                            "???" "You are an idiot"
                            c "What? Who are you?"
                            "???" "That doesn't matter. What does is how unbelievably selfish you are."
                            "!!!" "Yeah, idiot!"
                            c "What? There's two of you?"
                            "???" "Yeah, and what are you gonna do about it child hater?"
                            c "..."
                            $ renpy.pause (0.5)
                            scene black with dissolveslow
                            c "At a loss for words, I made my way back home, crawled into bed, and did nothing for the rest of the day."
                            m "Nice one."
                            $ persistent.evalremybad = "Worst Ending"
                            return

label eval_trip_to_orphanage:
    c "It's a bit far, is it not? The doctor said I shouldn't be walking too much."
    Ry normal "Well, you could always ride me instead of walking."
    c "Ummmm..."
    Ry shy "No... Not like that, I mean ride on my back. You're pretty small, plus I'm used to carrying around a bunch of books."
    c "I'll take being associated with a bunch of books as a compliment."
    Ry normal "Please do."

    menu:
        "Accept his offer":
            c "Sure, I'll make like a pile of books and hop on."
            hide remy with dissolvemed
            play sound "fx/bed.ogg" #Change Later
            m "Remy lay down on all fours, and making sure not to mess up his tie, I carefully hopped onto his back. He carefully folded his wings back to give me as much room as possible."
            Ry "Oof, maybe you're a bit heavier than the books I'm used to."
            c "Wait a minute..."
            Ry "Hey, books don't complain."
            m "After finding a relatively comfortable spot on his back, Remy lifted his body."
            Ry "How is it back there?"
            c "A bit bony. I think I need a saddle."
            Ry "Funnily enough, you can actually buy dragon saddles."
            c "That's... Interesting."
            Ry "They exist. I didn't say they were popular."
            scene black with dissolveslow
            play sound "fx/steps/rough_gravel.wav"
            m "Remy then slowly started walking forward, picking up speed surprisingly quickly."
            if rodebryce:
                m "It wasn't as uncomfortable as I had first imagined. In a way, it also felt strangely familiar, like I had done this before."
            else:
                m "It wasn't as uncomfortable as I had first imagined. It was almost like riding a horse, if the horse had scales, giant wings, and a tie."
            m "The experience was almost relaxing, with the light breeze and rhythmic thumping of Remy's feet on the grass and pavement."
            $ renpy.pause (0.5)
            m "It seemed as if it took no time at all to arrive at the orphanage."
            Ry "Ladies and gentledragons, this will be our final stop. Please make sure to grab all of your belongings and safely exit the vehicle."
            c "Very funny Remy."
            Ry "Thanks, I can tell that you sincerely mean that."
            play sound "fx/bed.ogg"
            m "I slid off of Remy's back and looked up at the orphanage."
            scene hatchery with dissolveslow #This background is temporary. Not sure if I like it BROKEN RN, IDK HOW TO FIX PLEASE HALP
            show remy normal with dissolve
            m "This content is currently under development! Redirecting to the beginning of the mod."
            jump eval_tmomi_remy
            #Welp, do orphanage stuff here or in another label, i have literally no clue what to do here
        "Take a scenic walk": #Add a skip here
            c "I think we should just walk and enjoy the scenery on our way there."
            Ry look "Are you sure [player_name]? It's quite a long walk to the orphanage."
            c "Don't worry about me, I feel just fine."
            Ry normal "Sounds good to me. Just let me know if you get tired so we can take a break. Can't have you hurting yourself."
            c "Don't worry, I know how to pace myself."
            scene black with dissolveslow
            hide remy with dissolvemed
            stop music fadeout 2.0
            m "With that, we started walking."
            m "However, it seemed as if I had greatly overestimated my physical strength. We continued on at a good pace for about ten minutes. However, I quickly fell victim to exhaustion and found myself struggling to keep up with Remy."
            scene forest1 with dissolveslow
            show remy normal with dissolve
            play music "mx/serene.ogg" #Look into changing this
            Ry look "Hey, are you alright? You look winded."
            c "I think I'm alright, just tired. I thought I could walk from one end of town to the other, but that coma really did a number on me."
            Ry "I can see that. Here, why don't we rest underneath that tree over there so you can regain your strength."
            scene black with dissolveslow
            hide remy with dissolvemed
            play sound "fx/evalgrasswalk1.ogg"
            m "The dragon made his way over to a peaceful little outcrop and lay down in a similar fashion to a dog. He beckoned me to follow."
            play sound "fx/evalgrasswalk2.ogg"
            scene evalwildlands with dissolveslow
            if mp.remyromance: #This part may be stupid, contemplating deleting this
                $ remypillow = True
                m "I collapsed on the ground next to the dragon, my face and his muzzle just inches apart."
                play sound "fx/kiss.wav"
                m "Unprompted, I was given a quick kiss by Remy. He smiled, and then raised his head."
                show remy shy with dissolvemed
                $ renpy.pause (0.5)
                c "What a nice surprise."
                Ry normal "Here, you can use me as a pillow. I don't mind."
                c "Oh boy, my very own full sized dragon pillow equipped with a built in heater!"
                Ry "I'm the latest model."
                m "I carefully propped myself up against Remy's side. I could feel his body rising and falling with each breath."
                Ry "Why don't you take a quick nap? I'll keep a lookout for unwanted visitors."
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
            
            $ renpy.pause (2.0)
            m "I felt a light tap on my shoulder. Slowly opening my eyes, I was met with Remy's face."
            scene evalwildlands2 with dissolveslow
            show remy smile with dissolvemed
            play music "mx/jazzy2.ogg"
            Ry "Hey there sleepy head. You slept for quite awhile."
            c "How long exactly."
            Ry normal "Well, you probably would have slept soundly for the next day or two, but I decided it was in our best interest if I were to wake you up before Adine's shift ends so we could meet her at the orphanage."
            c "Oh, did I really sleep for that long? I guess we won't be able to help at the orphanage today."
            Ry "It's alright, we can do it another time. Actually, all of the hatchlings aren't even there at the moment."
            c "Really? How come?"
            Ry "After the whole incident with Reza, they were put into emergency foster homes until everything cleared up. The council still hasn't given it the OK to let them back in the orphanage."
            c "What about Amely?"
            Ry look "Despite their best attempts, they couldn't find a place for Amely to stay, so Adine and I offered to take care of her instead. We both can't take her home because of our schedules, but young hatchlings are pretty self-sufficient."
            c "So what would we be doing exactly?"
            Ry normal "Well, there's always a lot to do, even if there aren't any children. Maintenance and such."
            #Its possible I want to add more here, lets see
            Ry "Anyways, we should get going. We don't want to miss Adine."
            scene black with dissolveslow
            hide remy with dissolvemed
            n "With renewed energy, Remy and I continued to the orphanage."
            #FX Here?
            $ renpy.pause (1.0)
            scene hatchery with dissolveslow
            show remy normal with dissolvemed
            Ry "Well, here we are. Now, all we have to do is wait for Adi..."
            play sound "fx/wooshes.ogg"
            hide remy with dissolvemed
            show remy normal at right with dissolvemed
            show adine normal c flip at left with dissolvemed
            Ad "Hey guys! What are you doing here?"
            Ry "Looking for you!"
            Ad giggle c flip "Well, I guess you found me, or rather, I found you. I expected to find you here Remy, but what is [player_name] doing here?"
            c "Ice cream."
            show remy look at right with dissolvemed
            Ad annoyed b flip "What?"
            c "Katsuharu owes me as much ice cream as I want, and I thought who better to bring than you two and Amely?"
            Ad think b flip "I have never heard of that dragon giving anyone free ice cream. You must have done something quite spectacular to get a deal like that."
            show remy normal at right with dissolvemed
            c "Just a little bit of business advice. I told him to move his stand down to Tatsu Park."
            Ad "You're telling me that you get an infinite supply of the world's best ice cream for free because you told him to move to Tatsu Park?"
            c "Well, not infinite. He said I could come by and get some ice cream when I felt like it."
            Ad normal b flip "So it's more of a one time deal. I get it. Count me in."
            Ry smile "Great! Lets grab Amely and we can go."
            Ad giggle b flip "Two dragons, a human with a big appetite, and a hatchling with unlimited access to delicious ice cream. I sure hope Katsuharu has enough stock."
            c "That old dragon owes me ice cream, and ice cream I, or we, shall receive!" #Cringy, should change
            scene black with dissolveslow
            hide adine with dissolvemed
            hide remy with dissolvemed
            m "This content is currently under development. Defaulting back to the beginning of the mod."
            jump eval_tmomi_remy


label eval_solo_remy_1: #Ending with only Remy
    $ currentending = 1
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
            c "Yeah, it's really been a while hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it. Hopefully it should all return back to the peaceful way it was. Everything has more or less resolved itself and the conflict is over." #Ew ugly
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
            Ka "*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka "I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
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
    if chosenflavor == "vanilla":
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
    c "I can tell. That is a seriously good looking scoop of ice cream."
    Ka "Thank you!"
    Ry "Even today it still surprises me. That's years of hard work and dedication."
    m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top, lightly pushing it down to make sure it didn't fall out."
    c "Interesting, those cones look exactly like the ones back in my world."
    show katsu excited flip at Position (xpos = 0.1) with easeinleft
    Ka "But I am sure that they don't taste half as good as mine!"
    m "Katsuharu then handed me the cone, topped with the [chosenflavor] ice cream."
    show katsu smile flip with dissolvemed
    
    if chosenflavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color." #Kinda bad, should change
    elif chosenflavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif chosenflavor == "strawberry":
        m "The strawberry ice cream looked different from what I was used to back in my world. Instead of a dark red, the scoop was tinted pinkish green, with small specks of what I assumed to be strawberry dotted within it."
    elif chosenflavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif chosenflavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif chosenflavor == "special":
        m "The Special was a disgusting mix of all the colors you don't want in your ice cream. It had a rather odd, dark gray color with pink dots speckled inside it, which I presumed was the fish."
    
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "I watched as Katsuharu went back to his stand and repeated the process for Remy's cone."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Here you are Remy."
    Ry smile "It's been so long since I've had ice cream."
    Ry "And there is nobody I would rather have ice cream with than you, [player_name]."
    c "Thanks Remy, that means a lot."
    Ka "Well, as promised, this one is on the house."
    c "Thank you Katsuharu."
    show remy normal at right with dissolvemed
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
    show katsu normal with dissolvemed #Why does katsu do a 360 flip here?
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
    scene black with dissolveslow
    hide remy with dissolvemed
    m "We made our way over to where Remy was looking and sat down side by side" #A little choppy, should fix this
    scene evalpark1 with dissolveslow
    show remy normal with dissolvemed
    Ry "We should make a toast."
    c "But we don't have any drinks."
    Ry "I guess our cones will have to suffice."
    c "You were the one who came up with the idea, so you go first."
    Ry smile "Alright then... To our health, both physically and mentally. Both of us have had a rough time in the past, but we have both stayed strong and supported each other."
    if chosenflavor == "vanilla":
        m "The two of us tapped our cones together, our scoops gently rubbing against each other."
        Ry look "Damn, our perfectly spherical scoops!"
    else:
        m "The two of us awkwardly tapped our cones together, careful as to not cross contaminate our different flavors."
    Ry normal "Seriously, though. I have so much to thank you for. Without you, I'm not sure I would be standing here at all today."
    c "Of course, Remy, I'll always be there fore you, even when I inevitably have to leave through the portal."
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
            c "To our love. You are the most gorgeous and kindhearted dragon I have ever seen."
            Ry shy "That definitely isn't what I expected to hear, but thank you. I can also confirm that you are the most beautiful human that I have ever seen."
            c "Not like I'm working with any real competition..."
            Ry normal "Hey, technically there were three humans here. I didn't have to say you were the most beautiful. I just sincerely mean it."
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
    m "I looked down, spotting trickles of the [chosenflavor] ice cream running down the cone and pooling on my hand."
    c "Good idea."
    if chosenflavor == "special":
        show remy smile with dissolvemed
        m "At the same time, Remy and I took a bite of our ice cream. Instantly, Remy's face lit up in excitement, and mine contorted into disgust."
        if mp.fish:
            c "Wow, this is just as disgusting as I remember it being."
        else:
            c "Wow, this is disgusting."
        Ry look "Are you not a big fan of the Special?"
        c "Not to offend anyone, but it's pretty gross."
        Ry normal "It isn't for everyone, but luckily it is for me. Would you like to switch?"

        menu:
            "Sure.":
                c "I mean, if you are okay with it."
                Ry smile "If you're happy, I'm happy."
                show remy normal with dissolvemed
                m "We quickly switched cones, and after a taste of the vanilla, I could see why Katsuharu was so well loved for his craft."
                m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."
                $ switchedcones = True
            
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
    show remy normal
    Ry smile "I would call this outing a complete success!"
    c "Agreed."
    Ry normal "It's getting a bit late, would you like me to walk you back to your place?"
    c "Sure!"
    scene black with dissolveslow
    hide remy with dissolvemed
    play sound "fx/steps/rough_gravel.wav"
    m "It didn't take us long to make our way back."
    scene evalplayerapt1 with dissolveslow
    show remy normal with dissolvemed
    Ry "Here we are, just like the night you first came here."

    menu:
        "Kiss him." if mp.remyromance:
            c "Sure. But on the first night would I do this?"
            play sound "fx/kiss.wav"
            m "I pulled Remy's muzzle to my lips and gave him a big kiss."
            Ry shy "I don't think you would then, but I'm glad you would now."

            if switchedcones:
                Ry normal "Your breath smells like vanilla."
                c "And yours of fish. I think I got the shorter end of the stick."
                Ry "I guess fish ice cream and kissing don't mix well together."
            elif chosenflavor == "special":
                c "Your breath smells like vanilla."
                Ry normal "And yours of fish. I think I got the shorter end of the stick."
                c "Yeah, I guess fish ice cream isn't the best for kissing."
            else:
                c "Your breath smells like vanilla."
                Ry normal "And yours of [chosenflavor]. Really adds to the kiss if you ask me."

            Ry shy "Hey... Uh, it's quite late, and my house is a bit far away, would you mind if I stayed at your place for the night?"
            c "Of course, the couch is always available."
            Ry "Well... I was thinking more along the lines of sharing the bed together."

            menu:
                "Sure.":
                    c "Well, Remy, sounds like a good time to me."
                    Ry normal "We'll see where things go, [player_name]." #Do I add more to this? Maybe I will in the final ending...
                    scene black with dissolveslow
                    stop music fadeout 2.0
                    play sound "mx/eveningmelody.ogg"
                    return
                
                "Sorry, but no.":
                    c "Sorry, but the bed is cramped enough for me as it is."
                    Ry sad "Oh, I understand, I guess the couch will be big enough for me."
                    scene black with dissolveslow
                    stop music fadeout 2.0
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
            return
    
    #And... scene!

label eval_remy_amely_1:
    m "I decided to sit on a nearby park bench while I waited for Remy to return with Amely."
    m "Glancing around the area, I saw what looked like the end of a long line of dragons, assumingly for Katsuharu's ice cream."
    c "Oh boy, I hope that line doesn't take too long."
    $ renpy.pause (2.0)
    m "Looking to my left, I saw that a dragon had been silently sitting on the bench with me."
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
        Dr "Dramavian..."
        hide dramavian with dissolvemed
        c "I guess his name is Dramavian..."
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
    show amely smnormal at right with dissolvemed
    show remy normal at right behind amely with dissolvemed
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
    show amely smnormal at right with dissolvemed
    show remy normal at right behind amely with dissolvemed
    Ry "Wow, this is quite an impressive line."
    c "It seems that my advice has paid off for him after all."
    Ry smile "Indeed."
    Ry normal "Wait, are we planning on waiting in line with everyone else? It seems like that might take a while."

    menu:
        "It would be rude to skip everyone.":
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
    Ka "Well, if it isn't the business saving human, [player_name]. Have you come to take up my offer?"

    menu:
        "Hey! Long time no see.":
            c "Yeah, it's really been a while hasn't it. A lot has gone on since we last saw each other."
            Ka exhausted flip "Quite a lot it seems. You have caused quite the chaos since you arrived."
            c "I guess I just have a knack for it. Hopefully it should all return back to the peaceful way it was. Everything has more or less resolved itself and the conflict is over."
            Ka smile flip "Glad to hear that."
            c "Is it alright that I brought Remy and Amely along as well?"
            Ka normal flip "Perfectly fine! Although Remy is going to have to pay for the both of them."
            Ry look "Umm... [player_name]? I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'm happy to accomodate the two of you as well."
            Ry normal "Why thank you Katsuharu, that's very generous of you."
            Ka "But enough chit-chat, we have to get to the more important matters."
            c "Like?"
            jump eval_ice_cream_choice
        "No time for chatting.":
            c "No time for chatting, we are here for important ice cream related matters."
            show remy look at right with dissolvemed
            Ka "*chuckles* Well, I guess I can't blame you for the enthusiasm."
            Ka "I actually remember Remy's first time getting ice cream from me, back when he was just a young little dragon."
            Ry shy "You do?"
            Ka smile flip "Yep, you were just as enthusiastic. Your eyes were practically bulging out of your head looking at all of the different flavors."
            Ry "I... guess I do remember being quite excited that day."
            c "Speaking of Remy, is it alright that I brought him along as well?"
            Ka normal flip "Perfectly fine! Although he is going to have to pay."
            Ry look "Umm... [player_name] I didn't bring any money."
            Ka smile flip "I'm just messing with you. I'm happy to accomodate Remy as well."
            Ry normal "Why thank you Katsuharu, that's very generous of you."
            Ka normal "Well, enough about embarrassing childhood memories, like you said, [player_name], we have to get to the more important matters."
            jump eval_ice_cream_choice

label eval_remy_amely_2:
    Ka normal flip "How about you, Remy?"
    if chosenflavor == "vanilla":
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
            Ry normal "Thanks! In my opinion, vanilla is the tried and true classic. You can't go wrong with it."
    
    show remy normal with dissolvemed
    Ka smile flip "And what about you, little... Amely, is it?"
    Am smsad "..."
    Ry smile "I think she may be a bit overwhelmed with all of the different flavor choices. How about we just get here some chocolate?"
    Ka normal flip "I'm sure she will be quite happy with that choice Remy. Just give me a second to get you your scoops!"
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    show amely smnormal at right with dissolvemed
    m "The dragon walked behind his stand and started preparing the ice cream."
    m "Expecting the dragon to produce some sort of utensil, I was surprised when he suddenly thrust his hand into the vat and pulled out an almost perfectly spherical scoop of ice cream."
    c "(Damn, these dragons can fly, shoot fire, run extremely fast, and even make an amazing scoop of ice cream with their bare hands. This truly is the peak of evolution.)"
    Ka "Y'know, most ice cream vendors use some sort of scoop. But over the years, you learn that your bare hands are faster and more efficient than any of those stupid tools." #Might be a bit pointless to have this
    c "I can tell. That is a seriously good looking scoop of ice cream."
    Ka "Thank you!"
    Ry normal "Even today it still surprises me. That's years of hard work and dedication."
    m "In another brisk motion, the dragon revealed a standard waffle cone and carefully rested the scoop on top, ligtly pushing it down to make sure it didn't fall out."
    c "Interesting, those cones look exactly like the ones back in my world."
    show katsu excited flip at Position (xpos = 0.1) with easeinleft
    Ka "But I am sure that they don't taste half as good as mine!"
    m "Katsuharu then handed me the cone, topped with the [chosenflavor] ice cream."
    show katsu smile flip with dissolvemed

    if chosenflavor == "vanilla":
        m "The vanilla ice cream itself was quite normal looking. It was a smooth and simple white color." #Kinda bad, should change
    elif chosenflavor == "chocolate":
        m "The chocolate ice cream looked almost exactly like it had at home. Dark, cocoa brown with the nice addition of what seemed to be tiny chocolate chips sprinkled within."
    elif chosenflavor == "strawberry":
        m "The strawberry ice cream looked different from what I was used to back in my world. Instead of a dark red, the scoop was tinted pinkish green, with small specks of what I assumed to be strawberry dotted within it."
    elif chosenflavor == "mango":
        m "The mango ice cream looked very similar to that of my own world. However, upon further inspection, I found that there were chunks of mango within the scoop as well."
        if persistent.adinegoodending:
            m "It also resembled the color of a very familiar dragon."
    elif chosenflavor == "cherry":
        m "Cherry ice cream in itself was a very unique concept to me. The scoop looked like the strawberry ice cream back in my world, but with a slightly darker shade of red."
    elif chosenflavor == "special":
        m "The Special was a disgusting mix of all the colors you don't want in your ice cream. It had a rather odd, dark gray color with pink dots speckled inside it, which I presumed was the fish."
    
    show katsu normal with dissolvemed
    hide katsu with easeoutleft
    m "I watched as Katsuharu went back to his stand and repeated the process for Remy and Amely's cones."
    show katsu normal flip at Position (xpos = 0.1) with easeinleft
    Ka "Here you go guys!"
    m "Remy and Amely took their cones from Katsuharu. Amely looked at it for a moment in wonder."
    show amely smnormal at right with dissolvemed
    m "The instant her tongue made contact with the chocolate, her eyes lit up in excitement and she took another bite."
    Ry smile "It's been so long since I've had ice cream."
    m "Amely was already attacking her cone from all angles."
    Ry normal "So, Amely, how is the ice cream?"
    Am "Ice cream... very good..."
    m "Her words were muffled as she continued devouring her cone."
    Ka "Well, as promised, this one is on the house."
    c "Thank you Katsuharu."
    Ka smile flip "I should be thanking you. Without you, I wouldn't even have a business."
    c "This ice cream is more than enough to show your gratitude."
    play sound "fx/bite.ogg"
    m "Amely had already finished the scoop of ice cream and had just started working on the cone."
    Ry "Wow, she's eating that impressively fast"
    Ka "Go ahead and stop by anytime you wish. I'll always have plenty of ice cream."
    c "Free of charge?"
    Ka exhausted flip "Well... We'll see. Amely could probably eat my entire stock and still have room for a full meal."
    Ry smile "I don't doubt that."
    Ka normal flip "Anyways, I should probably get back to my stand before the people in line start getting too angry. Amely seems to have upset them enough as it is."
    Ry look "Yeah, sorry about that. Thank you though, Katsuharu."
    Ka "No problem. Any time."
    show katsu normal with dissolvemed
    show remy normal with dissolvemed
    $ renpy.pause (0.2)
    hide katsu with easeoutleft
    c "Do you want to walk for a while?"
    Ry normal "As much as I would love to, it's a bit difficult as a quadruped"
    m "I looked down to see Remy carefully walking on 3 legs while balancing the cone with his fourth"
    c "Of course, let's find a good place to rest."
    Ry "That area looks nice and peaceful."
    scene black with dissolveslow
    hide remy with dissolvemed
    hide amely with dissolvemed
    stop music fadeout 2.0
    m "We made our way over to where Remy was looking and sat down side by side."
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
    if chosenflavor == "vanilla":
        m "The two of us tapped our cones together, our scoops gently rubbing against each other."
        Ry look "Damn, our perfectly spherical scoops!"
    else:
        m "The two of us awkwardly tapped our cones together, careful as to not cross contaminate our different flavors."
    Ry normal "Seriously, though. I have so much to thank you for. Without you, I'm not sure I would be standing here at all today."
    c "Of course, Remy, I'll always be there fore you, even when I inevitably have to leave through the portal."
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
            c "To our love. You are the most gorgeous and kindhearted dragon I have ever seen."
            Ry shy "That definitely isn't what I expected to hear, but thank you. I can also confirm that you are the most beautiful human that I have ever seen."
            c "Not like I'm working with any real competition..."
            Ry normal "Hey, technically there were three humans here. I didn't have to say you were the most beautiful. I just sincerely mean it." #Meh, change this
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
    m "I looked down, spotting trickles of the [chosenflavor] ice cream running down the cone and pooling on my hand."
    c "Good idea."
    show amely smnormal with dissolvemed
    m "I noticed that Amely had returned and her focus seemed to have drifted to the ice cream in my hand."

    menu:
        "Let Amely have your ice cream.":
            c "Here, Amely, you can have mine."
            Ry look "Are you sure that's such a good idea? That's a lot of sugar for a small dragon like her."
            c "It should be alright. It's her first time anyways, she deserves a bit extra."
            Ry normal "I guess."
            m "Amely eagerly grabbed the cone from my hands and took a giant bite of the [chosenflavor] ice cream."
            if chosenflavor == "special":
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
                            Ry smile "It is quite impressive, is it not?"
                            m "The two of us made short work of the scoop. Muzzle and face mere centimeters apart."
                            m "Suddenly, I felt Remy's tongue through the scoop. It seemed as if we had made it to the center"

                            menu:
                                "Sneak in a kiss.":
                                    m "Awkwardly, I pushed my lips onto his."
                                    m "Remy seemed to have caught the memo, pressing his lips onto mine in response and slipping in his tongue."
                                    play sound "fx/kiss.wav"
                                    Ry smile "That was the best bite yet!"
                                    c "I could say the same myself."
                                
                                "Pretend it didn't happen.":
                                    pass
                            
                        "Don't worry about it.":
                            c "Don't worry about it Remy, enjoy your ice cream."
                            Ry smile "Whatever you say. I won't give up an opportunity for more ice cream."
                            scene black with dissolveslow
                            stop music fadeout 2.0
                            m "You missed the entire point of this mod. The goal was ice cream, and every chance you had you threw it away!"
                            return #for now
                    m "With our combined ice cream eating power, we were able to make quick work of the cone."

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
            if chosenflavor == "special":
                show remy smile with dissolvemed
                m "At the same time, Remy and I took a bite of our ice cream. Instantly, Remy's face lit up in excitement, and mine contorted into disgust."
                if mp.fish:
                    c "Wow, this is just as disgusting as I remember it being."
                else:
                    c "Wow, this is disgusting."
                Ry look "Are you not a big fan of the Special?"
                c "Not to offend anyone, but it's pretty gross."
                Ry normal "It isn't for everyone, but luckily it is for me. Would you like to switch?"

                menu:
                    "Sure.":
                        c "I mean, if you are okay with it."
                        Ry smile "If you're happy, I'm happy."
                        show remy normal with dissolvemed
                        m "We quickly switched cones, and after a taste of the vanilla, I could see why Katsuharu was so well loved for his craft."
                        m "Our cones did not last long. Soon, the only remnants of our ice cream lay in our stomachs or dried on our hands."
                        $ switchedcones = True
                    
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

    #Wow that was a long and confusing series of events to program, hopefully it isn't all messed up
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
    c "It sure was. We should do this sort of thing more often. Especially if it involves ice cream"
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
            return


label eval_ice_cream_choice: #mp.fish <-- variable for whether player has had the special
    Ka "What flavor would you like?"

    menu:
        "Vanilla":
            $ chosenflavor = "vanilla"
            c "I'll take vanilla please."
            Ka smile flip "Ah, a simple flavor for a refined palette, good choice."
        
        "Chocolate":
            $ chosenflavor = "chocolate"
            c "I'll take chocolate please."
            Ka smile flip "Chocolate, perfect on its own, but even better in ice cream."
        
        "Strawberry":
            $ chosenflavor = "strawberry"
            c "I'll take strawberry please."
            Ka smile flip "You can never go wrong with a bit of berries in your ice cream."
        
        "Mango":
            $ chosenflavor = "mango"
            c "I'll take mango please."
            Ka smile flip "A bit tropical, I like your choice."
            if persistent.adinegoodending:
                Ry smile "Adine would slap you if she were here."
                c "I know."
            
        "Cherry":
            $ chosenflavor = "cherry"
            c "I'll take cherry please."
            Ka smile flip "You know, cherries are my favorite fruit. If you can get around the pit, they are delicious."
        
        'The "Special"' if showspecialflavor: #Oh no...
            $ chosenflavor = "special"
            c "I'll take the special, whatever that means."
            Ka smile flip "Ah, probably my most unique flavor."
            c "How so?"
            Ka normal flip "Have you been to our local diner?"
            c "Yes."
            Ka "Have you had the fish special?"

            if mp.fish:
                c "Oh please, don't remind me."
                Ka exhausted flip "What? Did you not like it?"
                c "Lets just say that it... Well, I guess all I can say is that it was awful."
                Ka normal flip "Well, with the power of a blender and some ice cream magic, you can now have that wonderful flavor in ice cream form!"
                c "Yay?"
                Ry look "That is a little bit... Interesting. I don't remember that being on your menu before."
                Ka "It's a recent addition."
                Ka "Well, what do you say?"
            else:
                c "Can't say I have."
                Ka smile flip "Well, they serve this wonderful fish dish that I loved so much, I decided to blend up and turn into an ice cream flavor!"
                c "Sounds a bit gross."
                Ry look "I would have to agree."
                Ka normal flip "It's better than it sounds. I promise. So, what do you say?"
            
            menu:
                "Maybe it's better as ice cream." if mp.fish:
                    c "You know what? Maybe it's actually better in ice cream form."
                    Ka smile flip "That's the spirit!"

                "I'm feeling adventurous." if not mp.fish:
                    c "You know what? I'm feeling adventurous today, I'll try it!"
                    Ka smile flip "That's the spirit!"

                "Maybe I should rethink my choice.":
                    $ showspecialflavor = False
                    show remy normal with dissolvemed
                    jump eval_ice_cream_choice

    if currentending == 1:
        jump eval_solo_remy_2
    elif currentending == 2:
        jump eval_remy_amely_2
    elif currentending == 3: #Update later
        pass