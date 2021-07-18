import renpy
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("This Man Owes me Ice Cream! Remy Edition", "v0.5.0", "Eval")

    def mod_load(self):
        #Remy's ending hook - Note I need to push this back earlier to change some prior dialogue
        source = ml.search_peak_if(modast.find_say("Besides, if you really end up going back in time, I'll see you again."), ast.Scene, 100)
        common_hook = modast.find_label("eval_tmomi_common")
        hook = modast.hook_opcode(source, None)
        modast.call_hook(source, common_hook, None)
        hook.chain(modast.search_for_node_type(source, ast.Scene))

    def mod_complete(self):
        pass