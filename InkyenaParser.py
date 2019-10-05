from Wes import Wes
from WesLis import weslis, weslisGreedy


syllasep = "-"
itemsep = " "

def parseFoil(foil):
    realfoil = foil.strip(syllasep)
    for letter in weslisGreedy: # match longest expression first
        if realfoil.startswith(letter.latinrep):
            car = letter
            cdrs = realfoil[len(letter.latinrep):]
            cdr = parseFoil(cdrs)
            if len(cdr) > 0 or len(cdrs) == 0:
                return [car] + cdr
            else:
                return []
    return []

def parseKyel(kyel):
    kyellist = kyel.split(itemsep, 2)
    while len(kyellist) < 3:
        kyellist += [""]
    return (kyellist[0], Foil(kyellist[1]), kyellist[2])

def parseFele(feleifden):
    with open(feleifden) as fele:
        parsedfele = []
        for kyel in fele:
            parsedfele += [parseKyel(kyel.strip())]
        return parsedfele

def gyiFeleParseNeSortNePrint(gyifele, felegyi):
    parsedfele = parseFele(gyifele)
    parsedfele.sort(key = lambda x: x[1])
    with open(felegyi, "w+") as fele:
        for kyel in parsedfele:
            fele.write(f"{kyel[1].latinrep} {kyel[0]} {kyel[2]}\n")


    
