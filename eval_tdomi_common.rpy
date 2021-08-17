init:

    #Backgrounds
    image evalwildlands = "bg/evalwildlands.jpg" #Tysm EvilChaosKnight
    image evalwildlands2 = "bg/evalwildlands2.jpg" #Tysm again ECK
    image evalpark1 = "bg/evalpark1.jpg"
    image evalpark2 = "bg/evalpark2.jpg"
    image evalplayerapt1 = "bg/evalplayerapt1.jpg"
    image evalplayerapt2 = "bg/evalplayerapt2.jpg"
    image evalkatsucart = "bg/evalkatsucart.jpg"
    image evalorphlight = "bg/evalorphlight.jpg"
    image evalorphevening = "bg/evalorphevening.jpg"
    image evalorphdark = "bg/evalorphdark.jpg"
    image evalplayerkitchen = "bg/evalplayerkitchen.jpg" #Tysm again again ECK

    #Characters

    #Amely brought to you by ECK
    image amely smnormal = "cr/amely_smnormal.png"
    image amely smnormal flip = "cr/amely_smnormal_flip.png"
    image amely sad = "cr/amely_sad.png"
    image amely sad flip = "cr/amely_sad_flip.png"
    image amely smsad = "cr/amely_smsad.png"
    image amely smsad flip = "cr/amely_smsad_flip.png"

    #Vara small
    image vara smnormal ghost = "cr/vara_smnormal_ghost.png"
    image vara smnormal ghost flip = im.Flip("cr/vara_smnormal_ghost.png", horizontal=True)
    image vara smnormal = "cr/vara_smnormal.png"
    image vara smnormal flip = im.Flip("cr/vara_smnormal.png", horizontal=True)
    image vara smsad = "cr/vara_smsad.png"
    image vara smsad flip = im.Flip("cr/vara_smsad.png", horizontal=True)
    image vara smnone = "cr/vara_smnone.png"
    image vara smnone flip = im.Flip("cr/vara_smnone.png", horizontal=True)
    image vara smgrowl = "cr/vara_smgrowl.png"
    image vara smgrowl flip = im.Flip("cr/vara_smgrowl.png", horizontal=True)
    image vara smshocked = "cr/vara_smshocked.png"
    image vara smshocked flip = im.Flip("cr/vara_smshocked.png", horizontal=True)
    image vara smshocked b = "cr/vara_smshocked_b.png"
    image vara smshocked b flip = im.Flip("cr/vara_smshocked_b.png", horizontal=True)

    #Remy wounded - Why a bullet on both sides? Well, I need him facing the right with the wound, and it felt weird to leave a non-flipped image in here as well
    image remy normal eval shot = "cr/remy_normal_eval_shot.png"
    image remy normal eval shot flip = im.Flip("cr/remy_normal_eval_shot.png", horizontal=True)
    image remy sad eval shot = "cr/remy_sad_e.png"
    image remy sad eval shot flip = im.Flip("cr/remy_sad_eval_shot.png", horizontal=True)
    image remy look eval shot = "cr/remy_look_e.png"
    image remy look eval shot flip = im.Flip("cr/remy_look_eval_shot.png", horizontal=True)
    image remy smile eval shot = "cr/remy_smile_e.png"
    image remy smile eval shot flip = im.Flip("cr/remy_smile_eval_shot.png", horizontal=True)
    image remy shy eval shot = "cr/remy_shy_e.png"
    image remy shy eval shot flip = im.Flip("cr/remy_shy_eval_shot.png", horizontal=True)
    image remy angry eval shot = "cr/remy_angry_e.png"
    image remy angry eval shot flip = im.Flip("cr/remy_angry_eval_shot.png", horizontal=True)

    #Adine ice cream face - Why doesn't this one make sense flipped either? I need the image flipped and can't be bothered to make a flipped sprite I won't use
    image adine normal eval icecream = "cr/adine_normal_eval_icecream.png"
    image adine normal eval icecream flip = im.Flip("cr/adine_normal_eval_icecream.png", horizontal=True)
    image adine annoyed eval icecream = "cr/adine_annoyed_eval_icecream.png"
    image adine annoyed eval icecream flip = im.Flip("cr/adine_annoyed_eval_icecream.png", horizontal=True)
    image adine disappoint eval icecream = "cr/adine_disappoint_eval_icecream.png"
    image adine disappoint eval icecream flip = im.Flip("cr/adine_disappoint_eval_icecream.png", horizontal=True)
    image adine frustrated eval icecream = "cr/adine_frustrated_eval_icecream.png"
    image adine frustrated eval icecream flip = im.Flip("cr/adine_frustrated_eval_icecream.png", horizontal=True)
    image adine giggle eval icecream = "cr/adine_giggle_eval_icecream.png"
    image adine giggle eval icecream flip = im.Flip("cr/adine_giggle_eval_icecream.png", horizontal=True)
    image adine sad eval icecream = "cr/adine_sad_eval_icecream.png"
    image adine sad eval icecream flip = im.Flip("cr/adine_sad_eval_icecream.png", horizontal=True)
    image adine think eval icecream = "cr/adine_think_eval_icecream.png"
    image adine think eval icecream flip = im.Flip("cr/adine_think_eval_icecream.png", horizontal=True)
init python:
    if not persistent.evalSeenDramavian: #Detects whether you have seen Dramavian a second time in this mod
        persistent.evalSeenDramavian = False
    if not persistent.evalSecretEndingUnlocked: #[REDACTED]
        persistent.evalSecretEndingUnlocked = False
    
    #Endings
    if not persistent.evalEndingA: #Unlike ECK, endings aren't named and "A" isn't the best
        persistent.evalEndingA = False #Just Remy - Vanilla
    if not persistent.evalEndingB:
        persistent.evalEndingB = False #Remy and Amely - Strawberry
    if not persistent.evalEndingC:
        persistent.evalEndingC = False #Remy, Amely, and Adine - Mango
    if not persistent.evalEndingD:
        persistent.evalEndingD = False #Everyone - Cherry
    
    #Fails
    if not persistent.evalUniqueFails:
        persistent.evalUniqueFails = []
    
    #Skips

    #General Skips
    if not persistent.evalOrphanageTripSkip:
        persistent.evalOrphanageTripSkip = False
    if not persistent.evalOrphanageSleepSkip:
        persistent.evalOrphanageSleepSkip = False

    #Ending A
    if not persistent.evalA1Skip:
        persistent.evalA1Skip = False
    if not persistent.evalA2Skip:
        persistent.evalA2Skip = False
    
    #Ending B
    if not persistent.evalB1Skip:
        persistent.evalB1Skip = False

    #Ending C
    if not persistent.evalC1Skip:
        persistent.evalC1Skip = False
    if not persistent.evalC2Skip:
        persistent.evalC2Skip = False

    #Ending D
    if not persistent.evalD1Skip:
        persistent.evalD1Skip = False
label eval_tdomi_common:
    #Whether you will actually get the secret ending or not
    $ evalPathToSecretComplete = False
    #Whether you have experienced the secret ending and currently in that timeline
    $ evalDoingSecretEnding = False
    #Whether you share the bed in the changed Ch4 Remy date
    $ evalRemyDateBed = False
    #Whether you visit the hatchery in chapter 4
    $ evalHatcheryVisited = False
    #Vara's mood during the chapter 4 Remy date change\
    $ evalVaraMood = 2
    return
screen main_menu_eval_icecream:
    if persistent.evalEndingA:
        add "image/ui/title/vanillaEnding.png"
    if persistent.evalEndingB:
        add "image/ui/title/strawberryEnding.png"
    if persistent.evalEndingC:
        add "image/ui/title/mangoEnding.png"
    if persistent.evalEndingD:
        add "image/ui/title/cherryEnding.png"
    if persistent.evalEndingA and persistent.evalEndingB and persistent.evalEndingC and persistent.evalEndingD:
        add "image/ui/title/chocolateEnding.png"
label eval_extended_ending:
    #Fixes a ton of issues
    $ _game_menu_screen = "navigation"

    #Check if player has ridden Bryce in ECK's Savior Mod.
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
    $ evalAskIfFat = False

    #Whether you manage to help out at the orphanage
    $ evalHelpOrphanage = False

    #How many times Adine has slapped you lol
    $ evalAdineSlaps = 0

    #How well the player did on the orphanage minigame. 0-2 - 0 bad - 1 good - 2 perfect
    $ evalOrphanageScore = 0

    #Whether you played Katsu's game
    $ evalPlayedKatsuGame = False

    #Whether you experienced my comedic genius
    $ evalSweatJoke = False

    #Whether you share the bed with Remy in the third ending
    $ evalRemyShareBed3 = False

    #Whether you have the tape measure for a very bad joke
    $ evalTapeMeasure = False

    #Whether Adine tricks you
    $ evalAdineTrick = False

    #Whether you walk with Remy. Does some logic to account for sleeping
    $ evalScenicWalk = False

    #Whether you listen to Katsu's music
    $ evalKatsuMusic = False



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

    #Variables for when Vara leaves in the orphanage minigame
    $ evalVaraGone = False
    $ evalRemyAsksAboutVara = False
    $ evalVaraSnack = False
    $ evalRemyGoneWhileSnack = False
    $ evalCrackersConsumed = 0
    $ evalJustAteCracker = False
        
    #Unique fails/quick endings
    $ evalFail = ""
    $ evalTotalFails = 0
    
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
        if renpy.python.store_dicts["store"].get("evalDoingSecretEnding",None)==None:
            play sound "fx/system3.wav"
            s "uh oh, it seems like you loaded a \"broken\" save, let me see if i can fix it"
            call eval_tdomi_common from eval_tdomi_common_init_late
            play sound "fx/system3.wav"
            s "Ok I think I fixed it"
            play sound "fx/system3.wav"
            s "you may want to play from very start to eliminate the remaining errors"
        jump eval_tdomi_remy
    elif evalPathToSecretComplete:
        play sound "fx/system3.wav"
        s "You saved Vara, but there is still more to her story..."
        stop music fadeout 2.0
        scene black with dissolveslow
        return