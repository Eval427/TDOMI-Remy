label eval_tmomi_common:

    #Backgrounds
    image evalorphanage = "bg/evalorphanage.jpg"
    image evalwildlands = "bg/eckwildlands.jpg" #Tysm EvilChaosKnight
    image evalwildlands2 = "bg/eckwildlands.jpg" #Tysm again ECK
    image evalpark1 = "bg/evalpark1.jpg"
    image evalpark2 = "bg/evalpark2.jpg"
    image evalplayerapt1 = "bg/evalplayerapt1.jpg"

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

    if persistent.playedkatsu:
        jump eval_tmomi_remy