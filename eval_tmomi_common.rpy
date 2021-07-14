label eval_tmomi_common:

    image evalorphanage = "bg/evalorphanage.jpg"
    image evalwildlands = "bg/eckwildlands.jpg" #Tysm EvilChaosKnight
    image evalwildlands2 = "bg/eckwildlands.jpg" #Tysm again ECK
    image evalpark1 = "bg/evalpark1.jpg"
    image evalpark2 = "bg/evalpark2.jpg"
    image evalplayerapt1 = "bg/evalplayerapt1.jpg"

    #Fixes a ton of issues
    $ _game_menu_screen = "navigation"

    #Check if player has ridden Bryce in ECK's Savior Mod. Not even sure if this is a good enough check, I'll check back later
    $ rodebryce = False #This is NOT weird I promise
    if persistent.eckbryceendingseena and persistent.eckbryceendingseena == "A":
        $ rodebryce = True
    
    #Other variables
    $ chosenflavor = ""
    $ showspecialflavor = True
    $ currentending = 0
    $ switchedcones = False
    $ remypillow = False

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