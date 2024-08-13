import numpy 
import json

with open("count.json","r") as c:
    count = c["count":]

jung = 60
alt = 3
erwachsen = 3 


def c_alt():
    alt = erwachsen/3
    return alt
def c_jung():
    jung = erwachsen*4+alt*2
    return jung
def c_erwachsen():
    erwachsen=jung/2
    return erwachsen

def neue_gen():
    
    global count
    data = {
        "generation": count,
        "jung": {"gruppe": "jung", "anzahl": c_jung()},
        "erwachsen": {"gruppe": "erwachsen", "anzahl": c_erwachsen()},
        "alt": {"gruppe": "alt", "anzahl": c_alt()}
    }
    c.close()
    
    with open("count.json","w") as c:
        count = count+1
        data = {"count": count}
        json.dump(data,c,indent=4)
    with open("save.json","w") as save:
        json.dump(data, save, indent=4)
    

neue_gen()