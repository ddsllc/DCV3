import os
import SourceFileKey_ShipRush
import SourceFileKey_Veeqo
import GenFieldKey_CIQ1
import SourceFileKey_Ebay_Orders
# import Helpers1

# switcher_functionkey_processing = {
#
#     "processfileheaderrow": [Helpers1.processfileheaderrow],
#     "translatefileheaderrow1": [Helpers1.translatefileheaderrow1],
#     "translatefileheaderrow2": [Helpers1.translatefileheaderrow2],
#     "processfilenextrow": [Helpers1.processfilenextrow],
#     "processcalculatedrows": [Helpers1.processcalculatedrows],
#     "processtranslatedrows": [Helpers1.processtranslatedrows],
#     "finalerrorcheck": [Helpers1.finalerrorcheck],
#     "pushfinalerrormessage": [Helpers1.pushfinalerrormessage],
#     "ciqidlookupadd": [Helpers1.ciqidlookupadd],
#     "ciqsearchlookupfile": [Helpers1.ciqsearchlookupfile],
#     # "buildcombinedshipmentslist": [buildcombinedshipmentslist],
#     # "markcombinedshipments": [markcombinedshipments],
#     # "sourcefilekey_processing": [sourcefilekey_processing],
#     # "general_post_processing": [general_post_processing]
# }
#
# def setglobalkeyfile(sourcefiletype):
#
#     if sourcefiletype is None:
#         return None
#
#     global globalsourcekey = None
#
#     match sourcefiletype:
#         case "ShipRush":
#             outputfile = SourceFileKey_ShipRush.getfunctionkey()
#         case "Veeqo":
#             outputfile = SourceFileKey_Veeqo.getfunctionkey_processing()
#         case "Ebay-Orders":
#             outputfile = SourceFileKey_Ebay_Orders.getfunctionkey()
#
#     return outputfile

def getfunctionkey(sourcefiletype):

    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getfunctionkey()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getfunctionkey_processing()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getfunctionkey()

    return outputfile


def getfunctionkey_processing(sourcefiletype):

    if sourcefiletype is None:
        return None

    outputkey_basekey = ""
    outputkey = [[]]
    count = 0

    match sourcefiletype:
        # case "ShipRush":
        #     outputfile = SourceFileKey_ShipRush.getfunctionkey()
        case "Veeqo":
            outputkey_basekey = SourceFileKey_Veeqo.getfunctionkey_processing()
        # case "Ebay-Orders":
        #     outputfile = SourceFileKey_Ebay_Orders.getfunctionkey()

    for keyrow in outputkey_basekey:
        if keyrow[0]:
            for switcher_keyrow in switcher_functionkey_processing:
                if switcher_keyrow == keyrow:
                    outputkey.append(keyrow)

    outputkey.pop(0)

    return outputkey


def getoutputfile_add(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getoutputfile_add()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getoutputfile_add()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getoutputfile_add()

    return outputfile


def getoutputfile_update(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getoutputfile_update()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getoutputfile_update()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getoutputfile_update()

    return outputfile


def getoutputfile_err(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getoutputfile_err()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getoutputfile_err()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getoutputfile_err()

    return outputfile


def getoutputfile_test1(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getoutputfile_test1()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getoutputfile_test1()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getoutputfile_test1()

    return outputfile


def getsourcefilekeybyvalue(sourcefiletype, value):
    if sourcefiletype is None:
        return None

    outputvalue = ""

    match sourcefiletype:
        case "ShipRush":
            outputvalue = SourceFileKey_ShipRush.getsourcefilekeybyvalue(value)
        case "Veeqo":
            outputvalue = SourceFileKey_Veeqo.getsourcefilekeybyvalue(value)
        case "Ebay-Orders":
            outputvalue = SourceFileKey_Ebay_Orders.getsourcefilekeybyvalue(value)


    return outputvalue


def getsourcefilekey(sourcefiletype):
    if sourcefiletype is None:
        return None

    filekey = ""

    match sourcefiletype:
        case "ShipRush":
            filekey = SourceFileKey_ShipRush.getsourcefilekey()
        case "Veeqo":
            filekey = SourceFileKey_Veeqo.getsourcefilekey()
        case "Ebay-Orders":
            filekey = SourceFileKey_Ebay_Orders.getsourcefilekey()

    return filekey


def getsourcefilekeylength(sourcefiletype):
    if sourcefiletype is None:
        return None

    filekeylength = 0

    match sourcefiletype:
        case "ShipRush":
            filekeylength = SourceFileKey_ShipRush.getsourcefilekeylength()
        case "Veeqo":
            filekeylength = SourceFileKey_Veeqo.getsourcefilekeylength()
        case "Ebay-Orders":
            filekeylength = SourceFileKey_Ebay_Orders.getsourcefilekeylength()

    return filekeylength


def getsourcefilekeybaselength(sourcefiletype):
    if sourcefiletype is None:
        return None

    filekeylength = 0

    match sourcefiletype:
        case "ShipRush":
            filekeylength = SourceFileKey_ShipRush.getsourcefilekeybaselength()
        case "Veeqo":
            filekeylength = SourceFileKey_Veeqo.getsourcefilekeybaselength()
        case "Ebay-Orders":
            filekeylength = SourceFileKey_Ebay_Orders.getsourcefilekeybaselength()

    return filekeylength


def getcalcfieldvalues(fieldname1, newfilerow, curfile):
    if curfile is None:
        return None

    procfilerow = ""

    match curfile:
        case "ShipRush":
            procfilerow = SourceFileKey_ShipRush.getcalcfieldvalues(fieldname1, newfilerow)
        case "Veeqo":
            procfilerow = SourceFileKey_Veeqo.getcalcfieldvalues(fieldname1, newfilerow)
        case "Ebay-Orders":
            procfilerow = SourceFileKey_Ebay_Orders.getcalcfieldvalues(fieldname1, newfilerow)

    return procfilerow


def gettranslatedfieldvalues(fieldname1, newfilerow, curfile):
    if curfile is None:
        return None

    procfilerow = ""

    match curfile:
        # case "ShipRush":
            # procfilerow = SourceFileKey_ShipRush.gettranslatedieldvalues(fieldname1, newfilerow)
        case "Veeqo":
            procfilerow = SourceFileKey_Veeqo.gettranslatedfieldvalues(fieldname1, newfilerow)
        case "Ebay-Orders":
            procfilerow = SourceFileKey_Ebay_Orders.gettranslatedfieldvalues(fieldname1, newfilerow)

    return procfilerow


def getsourceidrefforlookup(curfile):
    if curfile is None:
        return None

    outputvalue = ""

    match curfile:
        case "ShipRush":
            outputvalue = SourceFileKey_ShipRush.getsourceidrefforlookup()
        case "Veeqo":
            outputvalue = SourceFileKey_Veeqo.getsourceidrefforlookup()
        case "CIQ":
            outputvalue = GenFieldKey_CIQ1.getsourceidrefforlookup()
        case "Ebay-Orders":
            outputvalue = SourceFileKey_Ebay_Orders.getsourceidrefforlookup()

    return outputvalue


def getlookupourcefilekey(sourcefiletype):
    if sourcefiletype is None:
        return None

    filekey = ""

    match sourcefiletype:
        case "CIQ":
            filekey = GenFieldKey_CIQ1.getlookupsourcefilekey()

    return filekey


def getlookupsourcefilekeybyvalue(sourcefiletype, value):
    if sourcefiletype is None:
        return None

    outputvalue = ""

    match sourcefiletype:
        case "CIQ":
            outputvalue = GenFieldKey_CIQ1.getlookupsourcefilekeybyvalue(value)


    return outputvalue


def getcolplacement_xitor(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputvalue = ""

    match sourcefiletype:
        case "ShipRush":
            outputvalue = SourceFileKey_ShipRush.getcolplacement_xitor()
        case "Veeqo":
            outputvalue = SourceFileKey_Veeqo.getcolplacement_xitor()
            # print(outputvalue)
        # case "CIQ":
        #     outputvalue = GenFieldKey_CIQ1.getcolplacement_xitor()
        case "Ebay-Orders":
            outputvalue = SourceFileKey_Ebay_Orders.getcolplacement_xitor()

    return outputvalue


def getcolplacement_tracknum(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputvalue = ""

    match sourcefiletype:
        case "ShipRush":
            outputvalue = SourceFileKey_ShipRush.getcolplacement_tracknum()
        case "Veeqo":
            outputvalue = SourceFileKey_Veeqo.getcolplacement_tracknum()
        case "Ebay-Orders":
            outputvalue = SourceFileKey_Ebay_Orders.getcolplacement_tracknum()
        # case "CIQ":
        #     outputvalue = GenFieldKey_CIQ1.getcolplacement_tracknum()

    return outputvalue


def getcolplacement_combinedflag(sourcefiletype):
    if sourcefiletype is None:
        return None

    outputvalue = ""

    match sourcefiletype:
        case "ShipRush":
            outputvalue = SourceFileKey_ShipRush.getcolplacement_combinedflag()
        case "Veeqo":
            outputvalue = SourceFileKey_Veeqo.getcolplacement_tracknum()
        case "Ebay-Orders":
            outputvalue = SourceFileKey_Ebay_Orders.getcolplacement_tracknum()
        # case "CIQ":
        #     outputvalue = GenFieldKey_CIQ1.getcolplacement_tracknum()

    return outputvalue

