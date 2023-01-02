def returnDecision(inputMessage="", forceValidInput=False, defaultValue=False):
    userInput = input(inputMessage).lower().replace(" ", "")
    if userInput in ['y','yes','true','yep', 'allright','alright','verywell','ofcourse','byallmeans','sure','certainly','absolutely','indeed','affirmative','agreed','roger','aye','ayeaye','yeah','yah','yep','yup','uh-huh','okay','ok','okey-dokey','okey-doke','achcha','righto','righty-ho','surely']:
        return True
    elif userInput in ['n','no','nope', 'false','not','noindeed','absolutelynot','mostcertainlynot','ofcoursenot','undernocircumstances','bynomeans','notatall','negative','never','notreally','nothanks','nae','nope','nah','notonyourlife','noway','nofear','notonyournelly','nosiree','naw']:
        return False
    elif forceValidInput:
        return returnDecision(inputMessage, True)
    else:
        return defaultValue

def RD(inputMessage="", forceValidInput=False, defaultValue=False):
    userInput = input(inputMessage).lower().replace(" ", "")
    if userInput in ['y','yes','1','true','yep', 'allright','alright','verywell','ofcourse','byallmeans','sure','certainly','absolutely','indeed','affirmative','agreed','roger','aye','ayeaye','yeah','yah','yep','yup','uh-huh','okay','ok','okey-dokey','okey-doke','achcha','righto','righty-ho','surely']:
        return True
    elif userInput in ['n','no','0','nope', 'false','not','noindeed','absolutelynot','mostcertainlynot','ofcoursenot','undernocircumstances','bynomeans','notatall','negative','never','notreally','nothanks','nae','nope','nah','notonyourlife','noway','nofear','notonyournelly','nosiree','naw']:
        return False
    elif forceValidInput:
        return returnDecision(inputMessage, True)
    else:
        return defaultValue
