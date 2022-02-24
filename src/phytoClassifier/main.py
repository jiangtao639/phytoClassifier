from . import level4
from . import level3
from . import level2
from . import level1
from . import level0
from . import levelminus1


def getClassByName(name):

    level4C = level4.getClassByName(name)
    level3C = level3.getClassByName(name)
    level2C = level2.getClassByName(name)
    level1C = level1.getClassByName(name)
    level0C = level0.getClassByName(name)
    levelminus1C = levelminus1.getClassByName(name)

    if level4C != "None":
        return level4C
    elif level3C != "None":
        return level3C
    elif level2C != "None":
        return level2C
    elif level1C != "None":
        return level1C
    elif level0C != "None":
        return level0C
    elif levelminus1C != "None":
        return levelminus1C
    else:
        return "None"


def getClassByCid(cid):

    level4C = level4.getClassById(cid)
    level3C = level3.getClassById(cid)
    level2C = level2.getClassById(cid)
    level1C = level1.getClassById(cid)
    level0C = level0.getClassById(cid)
    levelminus1C = levelminus1.getClassById(cid)

    if level4C != "None":
        return level4C
    elif level3C != "None":
        return level3C
    elif level2C != "None":
        return level2C
    elif level1C != "None":
        return level1C
    elif level0C != "None":
        return level0C
    elif levelminus1C != "None":
        return levelminus1C
    else:
        return "None"


def getClassBySmiles(smiles):

    level4C = level4.getClassBySmiles(smiles)
    level3C = level3.getClassBySmiles(smiles)
    level2C = level2.getClassBySmiles(smiles)
    level1C = level1.getClassBySmiles(smiles)
    level0C = level0.getClassBySmiles(smiles)
    levelminus1C = levelminus1.getClassBySmiles(smiles)

    if level4C != "None":
        return level4C
    elif level3C != "None":
        return level3C
    elif level2C != "None":
        return level2C
    elif level1C != "None":
        return level1C
    elif level0C != "None":
        return level0C
    elif levelminus1C != "None":
        return levelminus1C
    else:
        return "None"


def getClassByInchi(inchi):

    level4C = level4.getClassByInChI(inchi)
    level3C = level3.getClassByInChI(inchi)
    level2C = level2.getClassByInChI(inchi)
    level1C = level1.getClassByInChI(inchi)
    level0C = level0.getClassByInChI(inchi)
    levelminus1C = levelminus1.getClassByInChI(inchi)

    if level4C != "None":
        return level4C
    elif level3C != "None":
        return level3C
    elif level2C != "None":
        return level2C
    elif level1C != "None":
        return level1C
    elif level0C != "None":
        return level0C
    elif levelminus1C != "None":
        return levelminus1C
    else:
        return "None"


def getClassByInChiKey(inchikey):

    level4C = level4.getClassByInChiKey(inchikey)
    level3C = level3.getClassByInChiKey(inchikey)
    level2C = level2.getClassByInChiKey(inchikey)
    level1C = level1.getClassByInChiKey(inchikey)
    level0C = level0.getClassByInChiKey(inchikey)
    levelminus1C = levelminus1.getClassByInChiKey(inchikey)

    if level4C != "None":
        return level4C
    elif level3C != "None":
        return level3C
    elif level2C != "None":
        return level2C
    elif level1C != "None":
        return level1C
    elif level0C != "None":
        return level0C
    elif levelminus1C != "None":
        return levelminus1C
    else:
        return "None"
