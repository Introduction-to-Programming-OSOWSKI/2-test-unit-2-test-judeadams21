def waterState(f):
    if f < 33:
        return "solid"
    elif 212 > f > 32:
        return "liquid"
    else:
        return "gas"

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

def toGerman(x):
    if x == "yes":
        return "ja"
    else:
        return "nein"

def stopLight(c):
    if c == "green":
        return "go"
    elif c == "yellow":
        return "slow"
    else:
        return "stop"