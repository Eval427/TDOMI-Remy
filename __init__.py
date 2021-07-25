import renpy
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

#varaSmallExpressions = ["smnormal", "smgrowl", "smnone", "smshocked", "smshocked_b", "smsad", "smnormal_ghost"]

#def load_ims():
#    for expression in varaSmallExpressions:
#        renpy.exports.image("vara %s"%expression.replace("_", " "), "cr/vara_%s"%expression)
#        renpy.exports.image("vara %s"%expression.replace("_", " "), im.Flip("cr/vara_%s"%expression, horizonal=True))

#def load_side_ims():
#    for expression in varaSmallExpressions:
#        renpy.exports.image("vara %s"%expression.replace("_", " "), "cr/vara_%s"%expression)
#        renpy.exports.image("vara %s"%expression.replace("_", " "), im.Flip("cr/vara_%s"%expression, horizonal=True))

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("This Man Owes me Ice Cream! Remy Edition", "v0.5.0", "Eval")

    def mod_load(self):
        #Remy's ending hook - Note I need to push this back earlier to change some prior dialogue
        endHookSource = modast.find_say("Besides, if you really end up going back in time, I'll see you again.")
        common_hook = modast.find_label("eval_tmomi_common")
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
        
        #Another hook to allow MC to stay in this current timeline?
        

    def mod_complete(self):
        pass