import renpy
import renpy.ast as ast
import renpy.display.im as im
import renpy.parser as parser

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

#Adding side images for unique character expressions
varaSmallExpressions = ["smnormal", "smgrowl", "smnone", "smshocked", "smshocked_b", "smsad", "smnormal_ghost", "smsmile"]
adineIceCreamExpressions = ["annoyed_eval_icecream", "disappoint_eval_icecream", "frustrated_eval_icecream", "giggle_eval_icecream", "normal_eval_icecream", "sad_eval_icecream", "think_eval_icecream"]
remyShotExpressions = ["angry_eval_shot", "look_eval_shot", "normal_eval_shot", "sad_eval_shot", "shy_eval_shot", "smile_eval_shot"]
adineGoggleExpressions = ["annoyed", "disappoint", "frustrated", "giggle", "normal", "sad", "think"]

def load_side_ims():
    def clip_vara_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (0, 150, 350, 400)), 250, 300), horizontal=True)

    def clip_adine_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (50, 0, 500, 600)), 250, 300), horizontal=True)
    
    def clip_remy_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (5, 30, 500, 600)), 250, 300), horizontal=True)
    
    for expression in varaSmallExpressions:
        renpy.exports.image("side vara %s"%expression.replace("_", " "), clip_vara_side_image("cr/vara_%s.png"%expression))
    
    for expression in adineIceCreamExpressions:
        renpy.exports.image("side adine %s"%expression.replace("_", " "), clip_adine_side_image("cr/adine_%s.png"%expression))
    
    for expression in remyShotExpressions:
        renpy.exports.image("side remy %s"%expression.replace("_", " "), clip_remy_side_image("cr/remy_%s.png"%expression))
    
    #For most of Adine's goggle expressions
    for expression in adineGoggleExpressions:
        if expression in ["giggle", "think"]:
            for letter in ["a", "b", "c", "d"]:
                renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
        else:
            for letter in ["a", "b", "c", "d", "e"]:
                renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
    
    #For Adine's sad shot expressions that had to be differently formatted
    for letter in ["a", "b", "c", "d", "e"]:
        renpy.exports.image("side adine sad goggles shot %s"%letter, clip_adine_side_image("cr/adine_sad_goggles_%s.png"%letter))
            

#Function by Joey to simplify connecting hooks
def connect(node, next):
    hook = modast.hook_opcode(node, None)
    hook.chain(next)

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("This Dragon Owes me Ice Cream!", "v0.9.0", "Eval")

    def mod_load(self):
        #Variable init hook. I'm lazy, so I just decided to define all my variables early instead of having a dedicated label to call whenever I needed to confirm vars
        varInitHook = modast.find_say("I'll leave the stuff for you here, and I'll take care of the rest once I get back, alright?")# modast.find_say("Getting ready, I noticed something lying on the table. It was the note Remy had left for me in case I needed anything. Along with his own home phone and work number, there were also some numbers for delivery of food and other necessities, as well as emergency and even janitorial services. He had certainly thought of everything, even though I now had to wonder what a dragon plumber might look like.")
        modast.call_hook(varInitHook, modast.find_label("eval_tdomi_common"))
        
        #Early variable init hook. This is similar to the one above, but initializes variables at the very start of the game. Trust me, it helps with conflicts
        earlyVarInitHook = modast.find_say("I awoke from uneasy dreams looking at an unfamiliar ceiling. Just for a moment, I wondered where I was before the events of last night all came back to me.")
        modast.call_hook(earlyVarInitHook, modast.find_label("eval_tdomi_early"))
        
        #Remy's ending hook
        endHookSource = modast.find_say("Besides, if you really end up going back in time, I'll see you again.")
        common_hook = modast.find_label("eval_extended_ending")
        hook = modast.hook_opcode(endHookSource, None)
        modast.call_hook(endHookSource, common_hook, None)
        hook.chain(modast.search_for_node_type(endHookSource, ast.Scene))
        
        #Hook to add variable to determine whether MC visited the hatchery to drop off the eggs
        for node in renpy.game.script.all_stmts:
            if isinstance(node, ast.Say) and node.what == "Well, see you some other time, [player_name].":
                modast.call_hook(node, modast.find_label("eval_hatchery_visited"))

        #Hook for changed chapter 4 Remy date
        changeCh4Date = modast.find_say("You know about her, then? It's such a sad story.")
        #postChangeCh4Date = modast.find_label("eval_post_date_change")
        #changeCh4Date.next = postChangeCh4Date
        modast.call_hook(changeCh4Date, modast.find_label("eval_remy_ch4_date_change"))
        
        #Hook for changed Remy ending
        changeRemyGoodEnding = modast.find_label("remy5")
        modast.call_hook(changeRemyGoodEnding, modast.find_label("eval_remy_good_ending_change"))
        
        #Hook to remove any mentions of sweat from the game so my jokes make canonical sense
        handleSweat = modast.find_say("After holding it for a few seconds, he breathed a sigh of relief as he relaxed and the flapping motion stopped again.")
        modast.call_hook(handleSweat, modast.find_label("eval_change_sweat_reference"), None, modast.search_for_node_type(handleSweat, ast.Menu))
        
        #Hook to add a variable as to whether you have met Lucius in the current playthrough.
        metLucius = modast.find_say("Just as I entered the southern part of the park, I found myself tumbling to the ground when someone suddenly bumped into me.")
        modast.call_hook(metLucius, modast.find_label("eval_met_lucius"), None, modast.find_say("Sorry about that. Are you alright?"))
        
        #Hook to add a variable as to whether you have met Kalinth in the current playthrough.
        metKalinth = modast.find_say("You're in luck, [player_name]! Bryce compiled all the case files a while ago. Ever since you came to our world, he seems to be a lot more interested in these human mysteries. I wonder if it has something to do with you?")
        modast.call_hook(metKalinth, modast.find_label("eval_met_kalinth"), None, modast.find_say("Anyway, you can find all the files here. I'll leave the rest to you."))
        
        #Hook to add a variable as to whether you have met Dramavian in the current playthrough.
        metDram = modast.find_say("(Well, maybe it {i}is{/i} a statue. Or I just turned invisible.)")
        modast.call_hook(metDram, modast.find_label("eval_met_dram"), None, modast.find_say("(I hope it's not the latter.)"))
        
        #Adding stuff to the main menu screen. Code by ECK
        tocompile = """
        screen dummy:
            if persistent.evalEndingA:
                add "image/ui/title/vanillaEnding.png"
            
            if persistent.evalEndingB:
                add "image/ui/title/strawberryEnding.png"
            
            if persistent.evalEndingC:
                add "image/ui/title/mangoEnding.png"
            
            if persistent.evalEndingD:
                add "image/ui/title/cherryEnding.png"
            
            if persistent.evalGogglesScene:
                add "image/ui/title/chocolateEnding.png"
        """
        compiled = parser.parse("FNDummy", tocompile)
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    modast.get_slscreen("main_menu").children.append(child)

    def mod_complete(self):
        if "Side Images" in modinfo.get_mods():
            load_side_ims()