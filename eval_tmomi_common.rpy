label eval_tmomi_common:

    #Backgrounds
    image evalorphanage = "bg/evalorphanage.jpg"
    image evalwildlands = "bg/eckwildlands.jpg" #Tysm EvilChaosKnight
    image evalwildlands2 = "bg/eckwildlands.jpg" #Tysm again ECK
    image evalpark1 = "bg/evalpark1.jpg"
    image evalpark2 = "bg/evalpark2.jpg"
    image evalplayerapt1 = "bg/evalplayerapt1.jpg"
    image evalkatsucart = "bg/evalkatsucart.jpg"
    image evalorphlight = "bg/evalorphlight.jpg"
    image evalorphevening = "bg/evalorphevening.jpg"
    image evalorphdark = "bg/evalorphdark.jpg"

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
    $ evalRodeBryce = False #This is NOT weird I promise
    if persistent.eckbryceendingseena and persistent.eckbryceendingseena == "A":
        $ evalRodeBryce = True
    
    #Flavor you choose
    $ evalChosenFlavor = ""

    #Shows/hides the menu option for the special flavor
    $ evalShowSpecialFlavor = True

    #Tracks current ending (1 = solo remy, 2 = remy + amely, 3 = remy + amely + adine)
    $ evalCurrentEnding = 0

    #Whether you decide to switch cones with Remy
    $ evalSwitchedCones = False

    #Whether you sleep on Remy
    $ evalRemyPillow = False

    #Whether Amely pisses off everyone in line
    $ evalAmelyAnnoysLine = False

    #Whether you rode Remy or not <-- THIS IS NOT WEIRD AGAIN I PROMISE
    $ evalRodeRemy = False

    #Whether you asked if Remy called you fat in the first choice
    $ evalAskifFat = False

    #Whether you manage to help out at the orphanage
    $ evalHelpOrphanage = False

    #How many times Adine has slapped you lol
    $ evalAdineSlaps = 0

    #How well the player did on the orphanage minigame. 0-2 - 0 bad - 1 good - 2 perfect
    $ evalOrphanageScore = 0
    
    #Whether you agree to help Xith with his report
    $ evalHelpXith = False

    #Whether you played Katsu's game
    $ evalPlayedKatsuGame = False



    #A bunch of variables for the orphanage minigame

    #Variable that toggles certain dialogue for increased continuity
    $ evalJumpFromMain = False

    #Variable to account if Remy was gone while you turned on the lights
    $ evalLightsOnWithoutRemy = False

    #Whether you have fixed the lights based on progress. Completes at 2
    $ evalReplaceBulbs = False
    $ evalResetBreaker = False
    $ evalReplaceSwitch = False

    #Whether you have fixed the desk based on progress. Completes at 2
    $ evalApplyDWD = False
    $ evalFixLeg = False
    $ evalFixSeat = False

    #Whether you have organized the books based on progress. Completes at 3
    $ evalPickUpBooks = False
    $ evalUncrumpleProgress = 0
    $ evalUncrumplePages = False
    $ evalSortBooks = False

    #Whether you sorted through the papers based on progress. Completes at 3
    $ evalHatchlingArt = False
    $ evalPaperwork = False
    $ evalFoldNewspaper = False
    $ evalAmelyPicture = False #Make sure to reference this later

    #Whether you cleaned everything based on progress. Completes at 3
    $ evalCleanWalls = False
    $ evalCleanDesks = False
    $ evalCleanWhiteboard = False

    #How many actions Remy will be gone for and handling his return
    $ evalMinutesRemyIsGone = 0
    $ evalRemyOnMission = False
    $ evalRemyItem = ""

    #How many minutes you get before your time is up. Base 15? 20? 25? I'll balance it once I finish
    $ evalRemainingMinutes = 250

    #How many tasks have been completed. Completes at 5
    $ evalTasksComplete = 0

    #What text to display when the user asks what to do next in the menu
    $ evalWhatNextText = ""

    #Lists of items the player has
    $ evalGatheredItems = []

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
    
    #Stuff for orphanage minigame display. Thanks EvilChaosKnight :)
    $ evalDisplayVar1name = ""
    $ evalDisplayVar1 = 0
    $ evalDisplayVar1unit = ""
    $ evalDisplayVar1sec = 0

    $ evalDisplayVar2name = ""
    $ evalDisplayVar2 = 0
    $ evalDisplayVar2unit = ""
    $ evalDisplayVar3name = ""
    $ evalDisplayVar3 = 0
    $ evalDisplayVar3unit = ""
    $ evalDisplayVar4name = ""
    $ evalDisplayVar4 = 0
    $ evalDisplayVar4unit = ""
    $ evalDisplayVar5name = ""
    $ evalDisplayVar5 = 0
    $ evalDisplayVar5unit = ""
    $ evalDisplayVar6name = ""
    $ evalDisplayVar6 = 0
    $ evalDisplayVar6unit = ""
    $ evalDisplayVar7name = ""
    $ evalDisplayVar7 = 0
    $ evalDisplayVar7unit = ""
    $ evalDisplayVar8name = ""
    $ evalDisplayVar8 = 0
    $ evalDisplayVar8unit = ""

    #Updated to require the player to meet with katsu every playthrough they want the ending
    if chap3picka == "katsu" or chap3pickb == "katsu":
        jump eval_tmomi_remy