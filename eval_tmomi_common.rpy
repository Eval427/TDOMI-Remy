label eval_tmomi_common:

    #Backgrounds
    image evalorphanage = "bg/evalorphanage.jpg"
    image evalwildlands = "bg/eckwildlands.jpg" #Tysm EvilChaosKnight
    image evalwildlands2 = "bg/eckwildlands.jpg" #Tysm again ECK
    image evalpark1 = "bg/evalpark1.jpg"
    image evalpark2 = "bg/evalpark2.jpg"
    image evalplayerapt1 = "bg/evalplayerapt1.jpg"
    image evalkatsucart = "bg/evalkatsucart.jpg"

    #Characters

    #Brought to you by ECK
    image amely smnormal = "cr/amely_smnormal.png"
    image amely smnormal flip = "cr/amely_smnormal_flip.png"
    image amely sad = "cr/amely_sad.png"
    image amely sad flip = "cr/amely_sad_flip.png"
    image amely smsad = "cr/amely_smsad.png"
    image amely smsad flip = "cr/amely_smsad_flip.png"

    #Fixes a ton of issues
    $ _game_menu_screen = "navigation"

    #Check if player has ridden Bryce in ECK's Savior Mod. Not even sure if this is a good enough check, I'll check back later
    $ rodebryce = False #This is NOT weird I promise
    if persistent.eckbryceendingseena and persistent.eckbryceendingseena == "A":
        $ rodebryce = True
    
    #Flavor you choose
    $ chosenflavor = ""

    #Shows/hides the menu option for the special flavor
    $ showspecialflavor = True

    #Tracks current ending (1 = solo remy, 2 = remy + amely, 3 = remy + amely + adine)
    $ currentending = 0

    #Whether you decide to switch cones with Remy
    $ switchedcones = False

    #Whether you sleep on Remy
    $ remypillow = False

    #Whether Amely pisses off everyone in line
    $ amelyannoysline = False

    #Whether you rode Remy or not <-- THIS IS NOT WEIRD AGAIN I PROMISE
    $ roderemy = False

    #Whether you asked if Remy called you fat in the first choice
    $ askiffat = False

    #Whether you manage to help out at the orphanage
    $ helporphanage = False

    #How many times Adine has slapped you lol
    $ adineslaps = 0

    #Whether the player is able to access the Remy + Amely + Adine ending
    #This is actually impossible to get, since you would need 3 dates to get it. Lucky you, all you have to do is get Adine's good ending at least once
    $ showadineending = False
    if persistent.adinegoodending:
        $ showadineending = True
    
    #Whether you agree to help Xith with his report
    $ helpxith = False

    #Stuff for endings that I might just scrap
    python:
        if not persistent.evalremybad:
            persistent.evalremybad = "???"
        if not persistent.evalremysologood:
            persistent.evalremysologood = "???"
        if not persistent.evalremysolobad:
            persistent.evalremysolobad = "???"
        if not persistent.evalremyamelygood:
            persistent.evalremyamelygood = "???"
        if not persistent.evalremyamelybad:
            persistent.evalremyamelybad = "???"
        if not persistent.evalremyamelybad:
            persistent.evalremyamelyadinegood = "???"
        if not persistent.evalremyamelybad:
            persistent.evalremyamelyadinebad = "???"
        if not persistent.seendramavian:
            persistent.seendramavian = False

    #Updated to require the player to meet with katsu every playthrough they want the ending
    if chap3picka == "katsu" or chap3pickb == "katsu":
        jump eval_tmomi_remy