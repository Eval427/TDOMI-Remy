import renpy
import renpy.parser as parser
import renpy.ast as ast
import renpy.display.im as im

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

#Adding side images for unique character expressions
varaSmallExpressions = ["smnormal", "smgrowl", "smnone", "smshocked", "smshocked_b", "smsad", "smnormal_ghost", "smsmile"]
adineIceCreamExpressions = ["annoyed_eval_icecream", "disappoint_eval_icecream", "frustrated_eval_icecream", "giggle_eval_icecream", "normal_eval_icecream", "sad_eval_icecream", "think_eval_icecream"]
remyShotExpressions = ["angry_eval_shot", "look_eval_shot", "normal_eval_shot", "sad_eval_shot", "shy_eval_shot", "smile_eval_shot"]
adineGoggleExpressions = ["annoyed", "disappoint", "frustrated", "giggle", "normal", "sad", "think"]
remyGoggleExpressions = ["look", "normal", "sad", "shy", "smile"]
varaGoggleExpressions = ["smnone", "smnormal", "smsmile"]
amelyGoggleExpressions = ["smnormal", "smsad"]

def load_side_ims():
    def clip_vara_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (0, 150, 350, 400)), 250, 300), horizontal=True)

    def clip_adine_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (50, 0, 500, 600)), 250, 300), horizontal=True)
    
    def clip_remy_side_image(imagefile):
        return im.Flip(im.Scale(im.Crop(imagefile, (5, 30, 500, 600)), 250, 300), horizontal=True)

    def clip_amely_side_image(imagefile):
        return im.Scale(im.Crop(imagefile, (180, 114, 500, 500)), 250, 250)
    
    for expression in varaSmallExpressions:
        renpy.exports.image("side vara %s"%expression.replace("_", " "), clip_vara_side_image("cr/vara_%s.png"%expression))
    
    for expression in adineIceCreamExpressions:
        renpy.exports.image("side adine %s"%expression.replace("_", " "), clip_adine_side_image("cr/adine_%s.png"%expression))
    
    for expression in remyShotExpressions:
        renpy.exports.image("side remy %s"%expression.replace("_", " "), clip_remy_side_image("cr/remy_%s.png"%expression))
    
    for expression in remyGoggleExpressions:
        renpy.exports.image("side remy %s goggles"%expression, clip_remy_side_image("cr/remy_%s_goggles.png"%expression))
    
    for expression in varaGoggleExpressions:
        renpy.exports.image("side vara %s goggles"%expression, clip_vara_side_image("cr/vara_%s_goggles.png"%expression))
    
    for expression in amelyGoggleExpressions:
        renpy.exports.image("side amely %s goggles"%expression, clip_amely_side_image("cr/amely_%s_goggles.png"%expression))
        renpy.exports.image("side amely %s goggles flip"%expression, clip_amely_side_image("cr/amely_%s_goggles_flip.png"%expression))
    
    #For most of Adine's goggle expressions
    for expression in adineGoggleExpressions:
        if expression in ["giggle", "think"]:
            for letter in ["a", "b", "c", "d"]:
                if letter == "a":
                    renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
                else:
                    renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
        else:
            for letter in ["a", "b", "c", "d", "e"]:
                if letter == "a":
                    renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
                else:
                    renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
    
    #For Adine's sad shot expressions that had to be differently formatted
    for letter in ["a", "b", "c", "d", "e"]:
        if letter == "a":
            renpy.exports.image("side adine %s goggles"%expression, clip_adine_side_image("cr/adine_%s_goggles.png"%expression))
        else:
            renpy.exports.image("side adine %s goggles %s"%(expression, letter), clip_adine_side_image("cr/adine_%s_goggles_%s.png"%(expression, letter)))
            

#Function by Joey to simplify connecting hooks
def connect(node, next):
    hook = modast.hook_opcode(node, None)
    hook.chain(next)

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("This Dragon Owes me Ice Cream!", "v1.0.1", "Eval")
    def mod_load(self):
        #Variable init hook. I'm lazy, so I just decided to define all my variables early instead of having a dedicated label to call whenever I needed to confirm vars
        varInitHook = modast.find_say("I'll leave the stuff for you here, and I'll take care of the rest once I get back, alright?")# modast.find_say("Getting ready, I noticed something lying on the table. It was the note Remy had left for me in case I needed anything. Along with his own home phone and work number, there were also some numbers for delivery of food and other necessities, as well as emergency and even janitorial services. He had certainly thought of everything, even though I now had to wonder what a dragon plumber might look like.")
        modast.call_hook(varInitHook, modast.find_label("eval_tdomi_common"))
        common_hook = modast.find_label("eval_extended_ending")
        for node in renpy.game.script.all_stmts:
            if isinstance(node, ast.Say) and node.what == "Besides, if you really end up going back in time, I'll see you again.":
                connect(node,common_hook)

        #Hook to add line of dialog when our MC dropps off the eggs at the hatchery
        for node in renpy.game.script.all_stmts:
            if isinstance(node, ast.Say) and node.what == "Well, see you some other time, [player_name].":
                next=node.next
                connect(modast.find_label("eval_hatchery_visited_next"),next)
                connect(node,modast.find_label("eval_hatchery_visited"))
        #hatchery post scene
        """
        c4sections=modast.find_label("c4sections")
        c4sections_next=c4sections.next
        connect(c4sections,modast.find_label("eval_c4_hatchery_init"))
        connect(modast.find_label("eval_c4_hatchery_init_return"),c4sections_next)
        """
        #changes some dialog from adine's 4th date
        """
        eval_c4_adine4_change=modast.find_say("We walked away from the festival and sat down under a tree in the outskirts of town. As the competition was already nearly over, the darkness had already set in.")
        eval_c4_adine4_change_fail=eval_c4_adine4_change.next
        eval_c4_adine4_change_success=modast.find_say("Hey, [player_name]. Look at the sky. Can you see that light? The one that looks a bit brighter than all the others?")
        connect(eval_c4_adine4_change,modast.find_label("eval_c4_adine4_change"))
        connect(modast.find_label("eval_c4_adine4_change_fail"),eval_c4_adine4_change_fail)
        connect(modast.find_label("eval_c4_adine4_change_success"),eval_c4_adine4_change_success)
        """
        #Hook for changed chapter 4 Remy date
        changeCh4Date = modast.find_say("You know about her, then? It's such a sad story.")
        changeCh4Date_next=changeCh4Date.next
        #postChangeCh4Date = modast.find_label("eval_post_date_change")
        #changeCh4Date.next = postChangeCh4Date
        connect(changeCh4Date, modast.find_label("eval_remy_ch4_date_change"))
        connect(modast.find_label("eval_remy_ch4_date_change_fail"),changeCh4Date_next)
        #Hook for changed Remy ending
        remy5=modast.find_label("remy5")
        remy5_next=remy5.next
        connect(remy5,modast.find_label("eval_remy_good_ending_change"))
        connect(modast.find_label("eval_remy_good_ending_change_fail"),remy5_next)
        #Hook to remove any mentions of sweat from the game so my jokes make canonotical sense
        handleSweat = modast.find_say("After holding it for a few seconds, he breathed a sigh of relief as he relaxed and the flapping motion stopped again.")
        modast.call_hook(handleSweat, modast.find_label("eval_change_sweat_reference"), None, modast.search_for_node_type(handleSweat, ast.Menu))
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