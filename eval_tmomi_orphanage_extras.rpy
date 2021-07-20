#PLEASE I WANT EVERYONE TO KNOW THAT THIS IS NOT MY CODE!!!!!!!!!
#This is all done by EvilChaosKnight. I take zero credit for anything that is written here or any of the files associated with it.
#If you like this mod, and for some strange reason you haven't already completed the ECK trilogy. Do it. It's even better than this.










#NOTE: The ONLY reason I changed variable names was to ensure that this mod had no conflicts with ECK's stuff (Not even sure it would if I kept them the same
#but I don't want to find out)










#Ugh this must have been a complete nightmare to make
screen evalextrainfo:
    
    if evalextradisplay == 1:
        add "image/ui/evalextras2.png" at zoom_fade_in
        
    elif evalextradisplay == 2:
        add "image/ui/evalextras2.png" at zoom_fade_in
    
    elif evalextradisplay == 3:
        add "image/ui/evalextras3.png" at zoom_fade_in
        
    elif evalextradisplay == 4:
        add "image/ui/evalextras4.png" at zoom_fade_in
    
    elif evalextradisplay == 5:
        add "image/ui/evalextras5.png" at zoom_fade_in
        
    elif evalextradisplay == 6:
        add "image/ui/evalextras6.png" at zoom_fade_in
        
    elif evalextradisplay == 7:
        add "image/ui/evalextras7.png" at zoom_fade_in
        
    elif evalextradisplay == 8:
        add "image/ui/evalextras8.png" at zoom_fade_in
        
    elif evalextradisplay == 11:
        add "image/ui/evalextras5.png" at zoom_fade_in
        
    else:
        pass

    hbox at zoom_fade_in:
        xalign 0.03
        yalign 0.0

        if evalextradisplay == 1:
#           add "image/ui/evalextras2.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]") style "status_text"
            
        elif evalextradisplay == 2:
#           add "image/ui/evalextras2.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]") style "status_text"
        
        elif evalextradisplay == 3:
#           add "image/ui/evalextras3.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]") style "status_text"
            
        elif evalextradisplay == 4:
#           add "image/ui/evalextras4.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]") style "status_text"
        
        elif evalextradisplay == 5:
#           add "image/ui/evalextras5.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]\n[evalDisplayVar5name] {b}[evalDisplayVar5]{/b}[evalDisplayVar5unit]") style "status_text"
            
        elif evalextradisplay == 6:
#           add "image/ui/evalextras6.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]\n[evalDisplayVar5name] {b}[evalDisplayVar5]{/b}[evalDisplayVar5unit]\n[evalDisplayVar6name] {b}[evalDisplayVar6]{/b}[evalDisplayVar6unit]") style "status_text"
            
        elif evalextradisplay == 7:
#           add "image/ui/evalextras7.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]\n[evalDisplayVar5name] {b}[evalDisplayVar5]{/b}[evalDisplayVar5unit]\n[evalDisplayVar6name] {b}[evalDisplayVar6]{/b}[evalDisplayVar6unit]\n[evalDisplayVar7name] {b}[evalDisplayVar7]{/b}[evalDisplayVar7unit]") style "status_text"
            
        elif evalextradisplay == 8:
#           add "image/ui/evalextras8.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1]{/b}[evalDisplayVar1unit]\n[evalDisplayVar2name] {b}[evalDisplayVar2]{/b}[evalDisplayVar2unit]\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]\n[evalDisplayVar5name] {b}[evalDisplayVar5]{/b}[evalDisplayVar5unit]\n[evalDisplayVar6name] {b}[evalDisplayVar6]{/b}[evalDisplayVar6unit]\n[evalDisplayVar7name] {b}[evalDisplayVar7]{/b}[evalDisplayVar7unit]\n[evalDisplayVar8name] {b}[evalDisplayVar8]{/b}[evalDisplayVar8unit]") style "status_text"
            
        if evalextradisplay == 11:
#           add "image/ui/evalextras5.png"
            text _("[evalDisplayVar1name]{b} [evalDisplayVar1][evalDisplayVar1unit][evalDisplayVar1sec]{/b}\n[evalDisplayVar2name] {b}[evalDisplayVar2][evalDisplayVar2unit]{/b}\n[evalDisplayVar3name] {b}[evalDisplayVar3]{/b}[evalDisplayVar3unit]\n[evalDisplayVar4name] {b}[evalDisplayVar4]{/b}[evalDisplayVar4unit]") style "status_text"
            
        else:
            pass

#Thank you ECK...