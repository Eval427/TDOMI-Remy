import renpy
import renpy.ast as ast
import renpy.display.im as im

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

#Adding side images for small Vara
varaSmallExpressions = ["smnormal", "smgrowl", "smnone", "smshocked", "smshocked_b", "smsad", "smnormal_ghost"]

def load_side_ims():
    def clip_vara_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (0, 150, 350, 400)), 250, 300), horizontal=True)
    
    for expression in varaSmallExpressions:
        renpy.exports.image("side vara %s"%expression.replace("_", " "), clip_vara_side_image("cr/vara_%s.png"%expression))

#Function by Joey to simplify connecting hooks
def connect(node, next):
    hook = modast.hook_opcode(node, None)
    hook.chain(next)

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("This Man Owes me Ice Cream! Remy Edition", "v0.7.0", "Eval")

    def mod_load(self):
        #Variable init hook. I'm lazy, so I just decided to define all my variables early instead of having a dedicated label to call whenever I needed to confirm vars
        varInitHook = modast.find_say("I'll leave the stuff for you here, and I'll take care of the rest once I get back, alright?")# modast.find_say("Getting ready, I noticed something lying on the table. It was the note Remy had left for me in case I needed anything. Along with his own home phone and work number, there were also some numbers for delivery of food and other necessities, as well as emergency and even janitorial services. He had certainly thought of everything, even though I now had to wonder what a dragon plumber might look like.")
        modast.call_hook(varInitHook, modast.find_label("eval_tdomi_common"))
        
        #Remy's ending hook - Note I need to push this back earlier to change some prior dialogue
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
        
        #Hook to remove any mentions of sweat from the game so my jokes make canotical sense
        handleSweat = modast.find_say("After holding it for a few seconds, he breathed a sigh of relief as he relaxed and the flapping motion stopped again.")
        modast.call_hook(handleSweat, modast.find_label("eval_change_sweat_reference"), None, modast.search_for_node_type(handleSweat, ast.Menu))
        

    def mod_complete(self):
        if "Side Images" in modinfo.get_mods():
            load_side_ims()