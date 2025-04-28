import os
# import switcher2
import csv
import SourceFileKey_ShipRush
import SourceFileKey_Veeqo
import GenFieldKey_CIQ1
import SourceFileKey_Ebay_Orders
import SourceFileKey_Ebay_Shipping
import SourceFileKey_AmazonAO_STX
import SourceFileKey_AmazonAO_SLN
import SourceFileKey_AmazonUTR_SFE
import SourceFileKey_Veeqo_Orders
from datetime import datetime


# [0] = function reference, [1] = n/a
def setbasesetglobalkeyfile():
    base_switcher_functionkey_processing = {

            "processfileheaderrow": [processfileheaderrow, 0],
            "translatefileheaderrow1": [translatefileheaderrow1],
            "translatefileheaderrow2": [translatefileheaderrow2],
            "processfilenextrow": [processfilenextrow],
            "processcalculatedrows": [processcalculatedrows],
            "processtranslatedrows": [processtranslatedrows],
            "getsecondarylookupvalues": [getsecondarylookupvalues],
            "getsecondaryagglookupvalues": [getsecondaryagglookupvalues],
            "getsecondaryagglookupvalues_UTR": [getsecondaryagglookupvalues_UTR],
            "finalerrorcheck": [finalerrorcheck],
            "pushfinalerrormessage": [pushfinalerrormessage],
            "ciqidlookupadd": [ciqidlookupadd],
            "ciqidlookupaddmulti": [ciqidlookupaddmulti],
            "ciqsearchlookupfile": [ciqsearchlookupfile, True],
            "buildcombinedshipmentslist": [buildcombinedshipmentslist],
            "markcombinedshipments": [markcombinedshipments],
            "general_post_processing": [general_post_processing],
            "write_row_list_to_files": [write_row_list_to_files],
            "filecleanup": [filecleanup]
        }
    return base_switcher_functionkey_processing


def setglobalkeyfile(sourcefiletype):
    bsfp = setbasesetglobalkeyfile()

    print(sourcefiletype)

    sourceglobkeyfile = None

    if sourcefiletype is None:
        return None

    match sourcefiletype:
        case "ShipRush":
            sourceglobkeyfile = SourceFileKey_ShipRush.getfunctionkey_processing()
        case "Veeqo":
            sourceglobkeyfile = SourceFileKey_Veeqo.getfunctionkey_processing()
        case "Ebay-Orders":
            sourceglobkeyfile = SourceFileKey_Ebay_Orders.getfunctionkey_processing()
        case "Ebay-Shipping":
            sourceglobkeyfile = SourceFileKey_Ebay_Shipping.getfunctionkey_processing()
        case "STX-Amazon-AO":
            sourceglobkeyfile = SourceFileKey_AmazonAO_STX.getfunctionkey_processing()
        case "SLN-Amazon-AO":
            sourceglobkeyfile = SourceFileKey_AmazonAO_SLN.getfunctionkey_processing()
        case "SFE-Amazon-UTR":
            sourceglobkeyfile = SourceFileKey_AmazonUTR_SFE.getfunctionkey_processing()
            print("sourceglobkeyfile:" + str(sourceglobkeyfile))
        case "Veeqo-Orders-STX":
            sourceglobkeyfile = SourceFileKey_Veeqo_Orders.getfunctionkey_processing()

    global switcher_functionkey_processing

    switcher_functionkey_processing = getfunctionkey_processing(sourcefiletype, bsfp)

    genglobkeyfile = switcher_functionkey_processing

    print("return:" + str(genglobkeyfile) + "|" + str(sourceglobkeyfile))
    return [genglobkeyfile, sourceglobkeyfile]


# returns [mainxitortypeprefix, mainxitorkeylength, mainxlookupposition, mainxlookupfinalpos]
def getinfofromxitortypekeyword(mainxitortypekeyword):

    mainxitortypeprefix = ""
    mainxitorkeylength = 0
    mainxlookupposition = "SHIP Order ID"  # for func "ciqidlookupadd"
    mainxlookupfinalpos = "SHIP Shipment CNE ID"  # for func "ciqidlookupadd"

    if isinstance(mainxitortypekeyword, list):
        match mainxitortypekeyword:
            case ["_Sale Line_", "_SalesListing_"]:
                mainxitortypeprefix = ["SLN-", "LST-"]
                mainxitorkeylength = [14, 14]
                mainxlookupposition = ["Sale Line: Marketplace Transaction ID (Sale)", "LIST Listing ID"]  #
                mainxlookupfinalpos = ["Sale Line: Sale Line ID", "LIST Listing ID"]  #
            case ["_Sale Line_", "_SalesListing Line_"]:
                mainxitortypeprefix = ["SLN-", "LST-"]
                mainxitorkeylength = [14, 14]
                mainxlookupposition = ["Sale Line: Marketplace Transaction ID (Sale)", "LST Channel SKU"]  #
                mainxlookupfinalpos = ["Sale Line: Sale Line ID", "LST Listing ID"]  #
            case ["_Sale Line_", "_SaleTx_"]:
                mainxitortypeprefix = ["SLN-", "STX-"]
                mainxitorkeylength = [14, 14]
                mainxlookupposition = ["Sale Line: Marketplace Transaction ID (Sale)", "SALETX Marketplace Transaction ID"]  #
                mainxlookupfinalpos = ["Sale Line: Sale Line ID", "SALETX CNE ID"]  #
            case ["_Sale Line_", "_Sale Line_"]:  # used to lookup xitor id's by column pair
                mainxitortypeprefix = ["SLN-", "SLN--"]
                mainxitorkeylength = [14, 14]
                mainxlookupposition = ["Sale Line: Item ID Tracking #",
                                       "Sale Line: Marketplace Transaction ID (Sale)"]  #
                mainxlookupfinalpos = ["Sale Line: Sale Line ID", "Sale Line: Sale Line ID"]  #
            # case "_Sale Line_":
            #     retkey = lookupsourcefilekey_SLN
            # case "_SalesListing_":
            #     retkey = lookupsourcefilekey_LISTING
            case _:
                retkey = None
    else:
        match mainxitortypekeyword:
            case "_Shipment_":
                mainxitortypeprefix = "SHP-"
                mainxitorkeylength = 14
                mainxlookupposition = "SHIP Order ID"  # for func "ciqidlookupadd"
                mainxlookupfinalpos = "SHIP Shipment CNE ID"  # for func "ciqidlookupadd"
            case "_SaleTx_":
                mainxitortypeprefix = "STX-"
                mainxitorkeylength = 14
                mainxlookupposition = "SALETX Marketplace Transaction ID"  # for func "ciqidlookupadd"
                mainxlookupfinalpos = "SALETX CNE ID"  # for func "ciqidlookupadd"
            case "_Sale Line_":
                mainxitortypeprefix = "SLN-"
                mainxitorkeylength = 14
                mainxlookupposition = "Sale Line: Marketplace Transaction ID (Sale)"  # for func "ciqidlookupadd"
                mainxlookupfinalpos = "Sale Line: Sale Line ID"  # for func "ciqidlookupadd"
            case "_SalesListing_":
                mainxitortypeprefix = "LST-"
                mainxitorkeylength = 0
                mainxlookupposition = "LIST Listing ID"  # for func "ciqidlookupadd"
                mainxlookupfinalpos = "LIST Listing ID"  # for func "ciqidlookupadd"
            case "_Sale Financial Event_":
                mainxitortypeprefix = "SFE-"
                mainxitorkeylength = 14
                mainxlookupposition = "SFE:Alias Field"  # for func "ciqidlookupadd"
                mainxlookupfinalpos = "SFE:Sale Financial Event ID"  # for func "ciqidlookupadd"
            case _:
                mainxitortypeprefix = None
                mainxitorkeylength = None
                print("\'mainxitortypekeyword\' not found: " + str(mainxitortypekeyword))

    return [mainxitortypeprefix, mainxitorkeylength, mainxlookupposition, mainxlookupfinalpos]

# get row's column location and possible values to identify which sales channel to search for listings
def getlistingchannelloc(curfilename):

    listchannelloc = ""
    listingchannelvalsdict = None

    match curfilename:
        case "STX-Amazon-AO" | "SLN-Amazon-AO":
            listchannelloc = "fulfillment-channel"
            listingchannelvalsdict = {
                # "{source report row value}": [{CIQ name for channel},{header name in CIQ lookup file to find CIQ channel name}]
                "TARGETFIELD": ["CHAN Sales Channel"],
                "Merchant": ["CNE Amazon FBM"],
                "Amazon": ["CNE Amazon FBA"]
            }
        # case "CNE Amazon FBA"
        case "AbesBargains Ebay":
            listchannelloc = ""
        case "Digicati Ebay":
            listchannelloc = ""
        case "ShopIncense.com":
            listchannelloc = ""
        case "ShopIncense.com":
            listchannelloc = ""
        case "Walmart.com":
            listchannelloc = ""
        case "WeIncense.com":
            listchannelloc = ""
        case "YourQuickStop.com":
            listchannelloc = ""
        case _:
            donothing = ""

    return [listchannelloc, listingchannelvalsdict]



# ------------------------
# FIND FILE NAME USING FILE NAME KEYWORD
# KEYWORD SHOULD BE A WILDCARD PHRASE WITHIN FILENAME
# ------------------------
def getfilenamebykeyword(keyword1):

    LOCAL_CONSOLE_OUTPUT1 = False

    curfolderfiles = os.listdir("_INPUT\\")
    # print(curfolderfiles)

    filenamekeyword = str(keyword1.replace("\'", ""))
    filenamekeyword = filenamekeyword.strip()
    # print(filenamekeyword)
    for filename in curfolderfiles:
        # print(filename)
        if str(filename).find(filenamekeyword) != -1 and (str(filename).find(".csv") != -1 or str(filename).find(".txt") != -1):
            if LOCAL_CONSOLE_OUTPUT1:
                print("Filename Located by Keyword | File Name: " + str(filename) + ", Keyword: " + keyword1)
            return "_INPUT\\" + str(filename)


    print("File Name Not Found -  by Keyword: " + keyword1 + "- Check file location and file extension.")
    return None


# ------------------------
# FIND CIQ LOOKUP FILE NAME USING FILE NAME KEYWORD
# KEYWORD SHOULD BE A WILDCARD PHRASE WITHIN FILENAME
# ------------------------
def getlookupfilenamebykeyword(keyword1):

    LOCAL_CONSOLE_OUTPUT1 = False

    curfolderfiles = os.listdir("_LOOKUP\\")
    # print(curfolderfiles)

    filenamekeyword = str(keyword1.replace("\'", ""))
    filenamekeyword = filenamekeyword.strip()
    # print(filenamekeyword)
    for filename in curfolderfiles:
        # print(filename)
        if str(filename).find(filenamekeyword) != -1 and str(filename).find(".csv") != -1:
            if LOCAL_CONSOLE_OUTPUT1:
                print("Filename Located by Keyword | File Name: " + str(filename) + ", Keyword: " + keyword1)
            return "_LOOKUP\\" + str(filename)
    print("File Name Not Found -  by Keyword: " + keyword1)
    return None


# ------------------------
# FIND FILE NAME USING FILE NAME KEYWORD
# KEYWORD SHOULD BE A WILDCARD PHRASE WITHIN FILENAME
# ------------------------
def checkoutputfilenameexists(name1):
    curfolderfiles = os.listdir("_RESULTS\\")
    # print(curfolderfiles)

    filename_new = str(name1.replace("\'", ""))
    filename_new = filename_new.strip()

    runididentifierstr = "_IMP-"

    if filename_new.find(runididentifierstr) != -1:
        filename_new = filename_new[:filename_new.index(runididentifierstr)]
        # print(filename_new)
    # print(filename_new)
    for filename in curfolderfiles:
        # print(filename + " | " + filename_new)
        if str(filename).find(str(filename_new)) != -1:
            # print("RETURN TRUE Output File  | File Name: " + str(filename) + ", Keyword: " + name1)
            return True
        # else:
            # print("Output File  | File Name: " + str(filename) + ", Keyword: " + name1)
            # print("No Match")

    # print("RETURN FALSE " + filename_new)

    return False


def createemptylist(listlength):
    newlist = []
    count = 0
    while count < listlength:
        newlist.insert(0, str(count))
        count += 1
    #print(newlist)
    return newlist


def processfileheaderrow(filerow, keyfile, keyfilelength):

    # print(filerow)

    newfilerow = createemptylist(keyfilelength)

    for temprow in filerow:
        temprow = temprow.replace("\"", "")
        for tempkey in keyfile:
            if temprow == tempkey:
                # print(temprow + tempkey)
                # print(int(keyfile[tempkey][1])-1)
                newfilerow.insert(int(keyfile[tempkey][1])-1, temprow)
                # print(int(keyfile[tempkey][1]))
                newfilerow.pop(int(keyfile[tempkey][1]))
            # else:
            #     print("No match:" + temprow)

    # print("newfilerow1: " + str(newfilerow))

    # newfilerow = translatefileheaderrow1(newfilerow, keyfile)
    # print("newfilerow1-post: " + str(newfilerow))
    return newfilerow

def translatefileheaderrow1(filerow, keyfile):

    newfilerow = filerow
    # print(filerow)

    for temprow in filerow:
        # print("--")
        temprow = temprow.replace("/", "")
        # print("-temprow-" + temprow)

        for tempkey in keyfile:
            # print("--" + tempkey)
            if temprow == tempkey:
                # print(keyfile[tempkey][3])
                # print(temprow + tempkey)
                # print(temprow)
                # print(int(keyfile[tempkey][1])-1)
                newval = keyfile[tempkey][4]

                newfilerow.insert(int(keyfile[tempkey][1])-1, newval)
                # print("-newval-" + newval)
                # print(int(keyfile[tempkey][1]))
                newfilerow.pop(int(keyfile[tempkey][1]))

    # print("newfilerow1: " + str(newfilerow))

    # newfilerow = translatefileheaderrow2(newfilerow, keyfile)

    return newfilerow


#for calc'd field headers
def translatefileheaderrow2(filerow, keyfile):

    count = 1
    newfilerow = filerow

    for tempkey in keyfile:
        # print(tempkey)
        if keyfile[tempkey][0] is None:
            # print(keyfile[tempkey][3])

            newval = keyfile[tempkey][4]

            newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval)
            # print(int(keyfile[tempkey][1]))
            newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    # print("---")
    # print("Header Row: " + str(newfilerow))

    return newfilerow


def processfilenextrow(filerow, keyfile, keyfilelength, curfile, filekey_proc):

    # print(filerow)
    newfilerow = createemptylist(keyfilelength)
    count = 1

    # print(keyfile)

    for temprow in filerow:
        temprow = str(temprow).replace(chr(9), "")
        temprow = str(temprow).replace(chr(10), "")
        # #change
        temprow = str(temprow).replace(",", "||")
        # if curfile == "Ebay-Orders":
        #     temprow = str(temprow).replace("\\'", "")
        #     # print("after: " + str(filerow))



        for tempkey in keyfile:
            if keyfile[tempkey][0] is not None:
                if count == int(keyfile[tempkey][0]):
                    # print(keyfile[tempkey][0])
                    # print(temprow + tempkey)
                    # print(str(count) + str(int(keyfile[tempkey][1]) - 1))
                    # temprow = temprow.replace(" ", "")
                    temprow = temprow.strip()
                    temprow = str(keyfile[tempkey][5]) + temprow
                    newfilerow.insert(int(keyfile[tempkey][1]) - 1, temprow)
                    # print(int(keyfile[tempkey][1]))
                    newfilerow.pop(int(keyfile[tempkey][1]))
        count += 1

    # newfilerow = processcalculatedrows(newfilerow, keyfile, keyfilelength, curfile, filekey_proc)
    # newfilerow = processtranslatedrows(newfilerow, keyfile, keyfilelength, curfile, filekey_proc)

    # print("newfilerow2: " + str(newfilerow))

    return newfilerow

# def processcalculatedrowsheader


# new values for import, derived from values in other columns
def processcalculatedrows(filerow, keyfile, keyfilelength, curfile, filekey_proc):
    count = 1
    newfilerow = filerow

    for tempkey in keyfile:
        if keyfile[tempkey][0] is None:
            # print(keyfile[tempkey][3])
            # print(keyfile)
            fieldname1 = keyfile[tempkey][3]
            # newval1 = switcher2.getcalcfieldvalues(fieldname1, newfilerow, curfile)
            newval1 = filekey_proc["getcalcfieldvalues"][0](fieldname1, newfilerow)
            # keyfile["getcalcfieldvalues"][0]()

            newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow


# keep the value from the source file but re-formatted for import
def processtranslatedrows(filerow, keyfile, keyfilelength, curfile, filekey_proc):

    count = 1
    newfilerow = filerow

    for tempkey in keyfile:
        if keyfile[tempkey][2] == 2:
            # print(keyfile[tempkey][3])

            fieldname1 = keyfile[tempkey][3]
            # newval1 = switcher2.gettranslatedfieldvalues(fieldname1, newfilerow, curfile)
            newval1 = filekey_proc["gettranslatedfieldvalues"][0](fieldname1, newfilerow)
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow


def getsecondarylookupvalues(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup):
    # print("filerow|" + str(filerow))

    count = 1
    newfilerow = ""
    # print("getsecondarylookupvalues: " + str(keyfile))
    for tempkey in keyfile:
        if keyfile[tempkey][2] == 3:
            # print(keyfile[tempkey][3])

            fieldname1 = keyfile[tempkey][3]
            # newval1 = switcher2.gettranslatedfieldvalues(fieldname1, newfilerow, curfile)
            newfilerow = filekey_proc["getsecondarylookupvalues"][0](fieldname1, filerow, keyfile, filekey_proc, filekey_lookup)
            # if newval1 != [[]]:
            #     newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            #     newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow


def secondarylookupvaluesfromfile(casefieldname, lookupfilenamekeyword, curfilerow, tempvalid, keyfile, filekey_proc, filekey_lookup):

    LOCAL_CONSOLE_OUTPUT1 = False

    newfilerow = curfilerow

    # print("filekey_lookup:" + str(filekey_lookup))

    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()
    if LOCAL_CONSOLE_OUTPUT1:
        print("mainxitortypekeyword:" + str(mainxitortypekeyword))

    lookupsource_filekey = getfilekey_lookup("CIQ", lookupfilenamekeyword)
    # print("lookupsource_filekey:" + str(lookupsource_filekey))

    tempinfoxitor_base = getinfofromxitortypekeyword(mainxitortypekeyword)
    xitorprefix = tempinfoxitor_base[0]
    mainxitortypekeylength = tempinfoxitor_base[1]
    mainxlookupposition = tempinfoxitor_base[2]
    mainxfinalposition = tempinfoxitor_base[3]
    if LOCAL_CONSOLE_OUTPUT1:
        print("tempinfoxitor_base:" + str(tempinfoxitor_base))

    tempinfoxitor_target = getinfofromxitortypekeyword(lookupfilenamekeyword)
    xitorprefix_target = tempinfoxitor_target[0]
    mainxitortypekeylength_target = tempinfoxitor_target[1]
    mainxlookupposition_target = tempinfoxitor_target[2]
    mainxfinalposition_target = tempinfoxitor_target[3]
    if LOCAL_CONSOLE_OUTPUT1:
        print("tempinfoxitor_target:" + str(tempinfoxitor_target))

    lookuporderidnames = filekey_lookup["getlookuporderidnames"][0](xitorprefix)
    if LOCAL_CONSOLE_OUTPUT1:
        print(lookuporderidnames)
    lookuporderid1name = lookuporderidnames[0]
    lookuporderid2name = lookuporderidnames[1]

    # lookupvalue = lookupvalue.replace("\"", "")

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword("cne.onevizion.com_Trackor Browser" + lookupfilenamekeyword)
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)



    matchingrowvalue = ""

    # lookupidresult = ciqsearchlookupfile(filerowvalue, filerowvalue2, lookupposition, lookupposition2,
    #                                      lookupfinalkeyposition, filekey_proc)

    # lookupvalue, lookupvalue2, poslookup, poslookup2, lookupkeyloc, filekey_proc
    filerowposition = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid1name)[1]) - 1
    lookupvalue = newfilerow[filerowposition]

    filerowposition2 = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid2name)[1]) - 1
    lookupvalue2 = newfilerow[filerowposition2]

    if LOCAL_CONSOLE_OUTPUT1:
        print([lookupfilenamekeyword, mainxlookupposition_target])

    poslookup = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeyword, mainxlookupposition_target)[1]) - 1

    secondarychecklookup = filekey_lookup["getsourceidrefforlookup"][0](lookupfilenamekeyword)
    lookuppositiontempkey = filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeyword,
                                                                               secondarychecklookup)
    poslookup2 = int(lookuppositiontempkey[1]) - 1

    lookupkeyloc = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeyword, mainxfinalposition_target)[1]) - 1

    if LOCAL_CONSOLE_OUTPUT1:
        print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(
            lookupkeyloc))

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for temprow in dcreader2:
            # print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(lookupkeyloc))
            # print(temprow)
            if temprow[poslookup] != "" and lookupvalue != "" and temprow[poslookup] == lookupvalue:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID found: " + lookupvalue + " | " + str(temprow))
            # else:
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            #     if temprow[poslookup] == (lookupvalue) or temprow[poslookup2] == (lookupvalue):
            #         matchingrowvalue = temprow[lookupkeyloc]
            #         matchingrowvalue = matchingrowvalue[0:14]  # CIQ Shipment IDs are 14 chars this trims trailing alias
            #         print("ID found: " + lookupvalue + " | " + str(temprow))
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            if temprow[poslookup2] != "" and lookupvalue2 != "" and temprow[poslookup2] == lookupvalue2:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID2 found: " + lookupvalue2 + " | " + str(temprow))
            if temprow[poslookup].find("MII-") != -1 and temprow[poslookup] != "" and lookupvalue != "" and \
                    temprow[poslookup].find(lookupvalue) != -1:
                matchingrowvalue = temprow[lookupkeyloc]
                # matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID3 found: " + lookupvalue + " | " + str(temprow))
            if matchingrowvalue != "":
                # return matchingrowvalue
                break
    if matchingrowvalue != "":
        for tempkey in keyfile:
            # print(keyfile[tempkey])
            if keyfile[tempkey][2] == 3 and keyfile[tempkey][3] == casefieldname:  # locate secondary lookup field
                # print("y1")
                newfilerow.insert(int(keyfile[tempkey][1]) - 1, matchingrowvalue)
                newfilerow.pop(int(keyfile[tempkey][1]))

    # print("newfilerow:" + str(newfilerow))
    return newfilerow


def secondarylookupvaluesfromfile2(casefieldname, lookupfilenamekeywordpair, curfilerow, tempvalid, keyfile, filekey_proc, filekey_lookup):

    newfilerow = curfilerow

    # print("filekey_lookup:" + str(filekey_lookup))

    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()
    print("mainxitortypekeyword:" + str(mainxitortypekeyword))

    # CUR
    lookupsource_filekey = getfilekey_lookup("CIQ", lookupfilenamekeywordpair)
    print("lookupsource_filekey:" + str(lookupsource_filekey))

    tempinfoxitor_base = getinfofromxitortypekeyword(lookupfilenamekeywordpair)
    xitorprefix = tempinfoxitor_base[0][0]
    mainxitortypekeylength = tempinfoxitor_base[1][0]
    mainxlookupposition = tempinfoxitor_base[2][0]
    mainxfinalposition = tempinfoxitor_base[3][0]
    print("tempinfoxitor_base:" + str(tempinfoxitor_base))

    # tempinfoxitor_target = getinfofromxitortypekeyword(lookupfilenamekeyword)
    tempinfoxitor_target = tempinfoxitor_base
    xitorprefix_target = tempinfoxitor_target[0][1]
    mainxitortypekeylength_target = tempinfoxitor_target[1][1]
    mainxlookupposition_target = tempinfoxitor_target[2][1]
    mainxfinalposition_target = tempinfoxitor_target[3][1]
    print("tempinfoxitor_target:" + str(tempinfoxitor_target))

    lookuporderidnames = filekey_lookup["getlookuporderidnames"][0](lookupfilenamekeywordpair)
    print(lookuporderidnames)
    lookuporderid1name = lookuporderidnames[0]
    lookuporderid2name = lookuporderidnames[1]

    # lookupvalue = lookupvalue.replace("\"", "")

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword("cne.onevizion.com_Trackor Browser" + lookupfilenamekeywordpair[1])
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)



    matchingrowvalue = ""

    # lookupidresult = ciqsearchlookupfile(filerowvalue, filerowvalue2, lookupposition, lookupposition2,
    #                                      lookupfinalkeyposition, filekey_proc)

    # lookupvalue, lookupvalue2, poslookup, poslookup2, lookupkeyloc, filekey_proc
    filerowposition = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid1name)[1]) - 1
    lookupvalue = newfilerow[filerowposition]

    filerowposition2 = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid2name)[1]) - 1
    lookupvalue2 = newfilerow[filerowposition2]

    print("lookuporderidnames:" + str(lookuporderid1name) + "|" + str(lookuporderid2name))
    print("filerowpositions:" + str(filerowposition) + "|" + str(filerowposition2))
    print("newfilerow:" + str(newfilerow))
    print("lookupvalues:" + str(lookupvalue) + "|" + str(lookupvalue2))

    print([lookupfilenamekeywordpair[0], mainxlookupposition_target])

    poslookup = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeywordpair[1], mainxlookupposition_target)[1]) - 1

    secondarychecklookup = filekey_lookup["getsourceidrefforlookup"][0](lookupfilenamekeywordpair[1])
    lookuppositiontempkey = filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeywordpair[1],
                                                                               secondarychecklookup)
    poslookup2 = int(lookuppositiontempkey[1]) - 1

    lookupkeyloc = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](lookupfilenamekeywordpair[1], mainxfinalposition_target)[1]) - 1

    print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(
        lookupkeyloc))

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for temprow in dcreader2:
            # print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(lookupkeyloc))
            # print(temprow)
            # print(len(temprow))
            if temprow == []:
                continue
            if len(temprow) > 0:
                if temprow[0].find("LSTLN-") == -1 and temprow[0].find("STX-") == -1:
                    continue
            if temprow[poslookup] != "" and lookupvalue != "" and temprow[poslookup] == lookupvalue:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                print("ID found: " + lookupvalue + " | " + str(temprow))
            # else:
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            #     if temprow[poslookup] == (lookupvalue) or temprow[poslookup2] == (lookupvalue):
            #         matchingrowvalue = temprow[lookupkeyloc]
            #         matchingrowvalue = matchingrowvalue[0:14]  # CIQ Shipment IDs are 14 chars this trims trailing alias
            #         print("ID found: " + lookupvalue + " | " + str(temprow))
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            if temprow[poslookup2] != "" and lookupvalue2 != "" and temprow[poslookup2] == lookupvalue2:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                print("ID2 found: " + lookupvalue2 + " | " + str(temprow))
            if temprow[poslookup].find("MII-") != -1 and temprow[poslookup] != "" and lookupvalue != "" and \
                    temprow[poslookup].find(lookupvalue) != -1:
                matchingrowvalue = temprow[lookupkeyloc]
                # matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                print("ID3 found: " + lookupvalue + " | " + str(temprow))
            if temprow[poslookup].find("(") != -1 and temprow[poslookup] != "" and lookupvalue != "" and \
                    temprow[poslookup].find(lookupvalue) != -1:
                matchingrowvalue = temprow[lookupkeyloc]
                # matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                print("ID4 found: " + lookupvalue + " | " + str(temprow))
            if matchingrowvalue != "":
                # return matchingrowvalue
                break
    if matchingrowvalue != "":
        for tempkey in keyfile:
            # print(keyfile[tempkey])
            if keyfile[tempkey][2] == 3 and keyfile[tempkey][3] == casefieldname:  # locate secondary lookup field
                # print("y1")
                newfilerow.insert(int(keyfile[tempkey][1]) - 1, matchingrowvalue)
                newfilerow.pop(int(keyfile[tempkey][1]))

    # print("newfilerow:" + str(newfilerow))
    return newfilerow


def getsecondaryagglookupvalues(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup, firstfile):
    # print("filerow|" + str(filerow))

    count = 1
    newfilerow = ""
    # print("getsecondarylookupvalues: " + str(keyfile))
    for tempkey in keyfile:
        if keyfile[tempkey][2] == 4:  # Identify fields with '4' = aggregate fields for lookup
            # print(keyfile[tempkey][3])

            fieldname1 = keyfile[tempkey][3]
            # newval1 = switcher2.gettranslatedfieldvalues(fieldname1, newfilerow, curfile)
            newfilerow = filekey_proc["getsecondaryagglookupvalues"][0](fieldname1, filerow, keyfile, filekey_proc, filekey_lookup, firstfile)
            # if newval1 != [[]]:
            #     newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            #     newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow

#  lookupfilenamekeywordpair = [lookup file type, [[SRC column for match, LU column to look for match, LU column to pull value, SRC column to insert result]]]
def secondaryagglookupvaluesfromfile(casefieldname, lookupfilenamekeywordpair, curfilerow, tempvalid, keyfile, filekey_proc, filekey_lookup):

    LOCAL_CONSOLE_OUTPUT1 = False

    newfilerow = curfilerow

    srcmatchnamelist = []
    lkupmatchnamelist = []
    lkuptargetnamelist = []
    srcdesttnamelist = []

    srcmatchloclist = []
    lkupmatchloclist = []
    lkuptargetloclist = []
    srcdesttloclist = []

    # print("filekey_lookup:" + str(filekey_lookup))

    mainxitortypestr = lookupfilenamekeywordpair[0]
    if LOCAL_CONSOLE_OUTPUT1:
        print("mainxitortypestr:" + str(mainxitortypestr))

    # [str, [["","","",""],["","","",""]]
    tempcount1 = 0
    for templkupsrcvals1 in lookupfilenamekeywordpair[1]:
        srcmatchnamelist.append(lookupfilenamekeywordpair[1][tempcount1][0])
        lkupmatchnamelist.append(lookupfilenamekeywordpair[1][tempcount1][1])
        lkuptargetnamelist.append(lookupfilenamekeywordpair[1][tempcount1][2])
        srcdesttnamelist.append(lookupfilenamekeywordpair[1][tempcount1][3])
        tempcount1 = tempcount1 + 1
    if LOCAL_CONSOLE_OUTPUT1:
        print("srcmatchnamelist:" + str(srcmatchnamelist))
        print("lkupmatchnamelist:" + str(lkupmatchnamelist))
        print("lkuptargetnamelist:" + str(lkuptargetnamelist))
        print("srcdesttnamelist:" + str(srcdesttnamelist))

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword("cne.onevizion.com_Trackor Browser" + mainxitortypestr)
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)

    matchingrowvalue = ""
    aggtotal = [0]
    aggcount = [0]

    tempcount2 = 0
    for templkupsrcvals2 in srcmatchnamelist:
        srcmatchloclist.append(int(filekey_proc["getsourcefilekeybyvalue"][0](srcmatchnamelist[tempcount2])[1] - 1))
        lkupmatchloclist.append(int(filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypestr, lkupmatchnamelist[tempcount2])[1] - 1))
        lkuptargetloclist.append(int(filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypestr, lkuptargetnamelist[tempcount2])[1] - 1))
        srcdesttloclist.append(int(filekey_proc["getsourcefilekeybyvalue"][0](srcdesttnamelist[tempcount2])[1] - 1))
        tempcount2 = tempcount2 + 1
    if LOCAL_CONSOLE_OUTPUT1:
        print("srcmatchloclist:" + str(srcmatchloclist))
        print("lkupmatchloclist:" + str(lkupmatchloclist))
        print("lkuptargetloclist:" + str(lkuptargetloclist))
        print("srcdesttloclist:" + str(srcdesttloclist))

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')

        targetfound = False

        for temprow in dcreader2:
            infolistcount = 0
            # print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(lookupkeyloc))
            # print(temprow)

            for templkupsrcvals3 in srcmatchloclist:
                tempsrcmatchval = newfilerow[srcmatchloclist[infolistcount]]
                templkupmatchval = temprow[lkupmatchloclist[infolistcount]]
                templkuptargetval = temprow[lkuptargetloclist[infolistcount]]
                tempsrcdestloc = srcdesttloclist[infolistcount]

                if tempsrcmatchval != "" and templkupmatchval != "" and tempsrcmatchval == templkupmatchval:
                    # matchingrowvalue = temprow[lookupkeyloc]
                    # matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                    if LOCAL_CONSOLE_OUTPUT1:
                        print("ID1 found - Shipping Cost: " + str(tempsrcmatchval) + " | " + str(templkuptargetval))
                    if templkuptargetval != "":
                        templkuptargetval = templkuptargetval.replace("$", "")
                        aggtotal[0] = aggtotal[0] + float(templkuptargetval)
                        aggcount[0] = aggcount[0] + 1
                        targetfound = True
                    if LOCAL_CONSOLE_OUTPUT1:
                        print("aggtotal|aggcount: " + str(aggtotal[0]) + " | " + str(aggcount[0]))

                infolistcount = infolistcount + 1

        if targetfound:

            for tempkey in keyfile:
                tempcount1 = 0
                # print(keyfile[tempkey])
                for templkupsrcvals4 in srcdesttloclist:
                    # print("templkupsrcvals4:" + str(templkupsrcvals4))
                    # print("keyfile[tempkey]:" + str(keyfile[tempkey]))
                    if keyfile[tempkey][2] == 4 and keyfile[tempkey][1] - 1 == templkupsrcvals4:
                        # print("y1")
                        # print("templkupsrcvals4:" + str(templkupsrcvals4))
                        # print("keyfile[tempkey]:" + str(keyfile[tempkey]))
                        newfilerow.insert(int(templkupsrcvals4), aggtotal[0])
                        newfilerow.pop(int(templkupsrcvals4) + 1)
                        match casefieldname:
                            case "STX_SHIPPING_COST":
                                newfilerow.insert(int(keyfile["STX_SHIPPING_COST_COUNT"][1]) - 1, aggcount[0])
                                newfilerow.pop(int(keyfile["STX_SHIPPING_COST_COUNT"][1]))
                    tempcount1 = tempcount1 + 1


    # print("newfilerow:" + str(newfilerow))
    return newfilerow


# [SRC|Listing ID, SRC|Quantity, LKUP|Listing ID, LKUP|Cost, SRC|Destination Field]
def secondaryagglookupvaluesfromfile_product(casefieldname, fieldslist, curfilerow, tempvalid, keyfile, filekey_proc,
                                             filekey_lookup, firstfile):

    LOCAL_CONSOLE_OUTPUT1 = False
    LOCAL_CONSOLE_OUTPUT2 = False

    curfile = firstfile
    newfilerow = curfilerow

    # tempchannellist returns... [listchannelloc, listingchannelvalsdict]
    # [0] listchannelloc = "fulfillment-channel"
    # [1] example dict entries... "TARGETFIELD": ["CHAN Sales Channel"],
    #                              "Merchant": ["CNE Amazon FBM"],
    tempchannellist = getlistingchannelloc(curfile)
    listingchannellocfieldname = tempchannellist[0]
    listingchannelloc = int(filekey_proc["getsourcefilekeybyvalue"][0](listingchannellocfieldname)[1]) - 1
    listingchannelsrcvalue = curfilerow[listingchannelloc]
    listingchannelvalsdict = tempchannellist[1]
    lookupfilechannelnameloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("MII-MCC", listingchannelvalsdict["TARGETFIELD"][0])[1] - 1)
    if LOCAL_CONSOLE_OUTPUT1:
        print("listingchannelloc:" + str(listingchannelloc))
        print("listingchannelsrcvalue:" + str(listingchannelsrcvalue))
        print("listingchannelvalsdict:" + str(listingchannelvalsdict))
        print("lookupfilechannelnameloc:" + str(lookupfilechannelnameloc))

    srclistingidname = fieldslist[0]
    srcquantityname = fieldslist[1]
    lkuplistingidname = fieldslist[2]
    lkupcostname = fieldslist[3]
    lkupunitquantityname = fieldslist[4]
    srcdestinationfieldname = fieldslist[5]

    srclistingidloc = int(filekey_proc["getsourcefilekeybyvalue"][0](srclistingidname)[1] - 1)
    srcquantityloc = int(filekey_proc["getsourcefilekeybyvalue"][0](srcquantityname)[1] - 1)
    lkuplistingidloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("MII-MCC", lkuplistingidname)[1] - 1)
    lkupcostloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("MII-MCC", lkupcostname)[1] - 1)
    lkupunitquantityloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("MII-MCC", lkupunitquantityname)[1] - 1)
    srcdestinationfieldloc = int(filekey_proc["getsourcefilekeybyvalue"][0](srcdestinationfieldname)[1] - 1)
    if LOCAL_CONSOLE_OUTPUT1:
        print("srclistingidloc:" + str(srclistingidloc))
        print("srcquantityloc:" + str(srcquantityloc))
        print("lkuplistingidloc:" + str(lkuplistingidloc))
        print("lkupcostloc:" + str(lkupcostloc))
        print("lkupunitquantityloc:" + str(lkupunitquantityloc))
        print("srcdestinationfieldloc:" + str(srcdestinationfieldloc))

    srcprodcostcountloc = int(filekey_proc["getsourcefilekeybyvalue"][0]("STX_INITIAL_COST_COUNT")[1] - 1)

    srclistingidval = newfilerow[srclistingidloc]
    srcquantityval = newfilerow[srcquantityloc]

    curfilename = getlookupfilenamebykeyword("_Trackor Browser_SalesListing Line_")
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)

    # print("listingchannelloc:" + str(listingchannelloc))
    # print("listingchannelsrcvalue:" + str(listingchannelsrcvalue))
    # print("listingchannelvalsdict:" + str(listingchannelvalsdict))
    # print("lookupfilechannelnameloc:" + str(lookupfilechannelnameloc))

    with open(lookupfile) as csvfile:
        # dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"', lineterminator='\r')
        targetfound = False

        aggcost = 0
        aggcount = 0

        for temprow in dcreader2:
            infolistcount = 0
            if temprow[lookupfilechannelnameloc] != listingchannelvalsdict[listingchannelsrcvalue][0]:
                if LOCAL_CONSOLE_OUTPUT2:
                    print("Channel Listing skipped: " + str(listingchannelvalsdict[listingchannelsrcvalue][0]) + "|" +
                          str(temprow[lookupfilechannelnameloc]))
                continue
            templkuplistingidval1 = temprow[lkuplistingidloc]
            # print(temprow[lkuplistingidloc])
            if templkuplistingidval1 != "" and srclistingidval != "" and templkuplistingidval1 == srclistingidval:
                targetfound = True
                templkupcostval1 = temprow[lkupcostloc]
                templkupcostval1 = templkupcostval1.replace("$", "")
                if templkupcostval1 == "":
                    templkupcostval1 = 0
                templkupquantityval1 = temprow[lkupunitquantityloc]
                if templkupquantityval1 == "":
                    templkupquantityval1 = 0
                aggcost = aggcost + (float(templkupcostval1) * float(templkupquantityval1))
                aggcount = aggcount + 1
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID1 found - Product Cost: " + str(aggcost) + " | " + str(aggcount))

    if targetfound:
        if srcquantityval != "":
            srcquantityval = int(srcquantityval)
        aggcost = aggcost * srcquantityval
        newfilerow.insert(srcdestinationfieldloc, aggcost)
        newfilerow.pop(srcdestinationfieldloc + 1)

        newfilerow.insert(srcprodcostcountloc, aggcount)
        newfilerow.pop(srcprodcostcountloc + 1)

    return newfilerow


def getsecondaryagglookupvalues_UTR(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup):
    # print("filerow|" + str(filerow))

    firstfile = curfile

    count = 1
    # newfilerow = ""
    newfilerow = filerow
    # print("getsecondarylookupvalues: " + str(keyfile))
    for tempkey in keyfile:
        # print("tempkey|" + str(keyfile[tempkey]))
        if keyfile[tempkey][2] == 4 and keyfile[tempkey][3] == "STX_COMMISSION_FEES":  # Identify fields with '4' = aggregate fields for lookup
            # print(keyfile[tempkey][3])

            fieldname1 = keyfile[tempkey][3]
            # newval1 = switcher2.gettranslatedfieldvalues(fieldname1, newfilerow, curfile)
            newfilerow = filekey_proc["getsecondaryagglookupvalues"][0](fieldname1, filerow, keyfile, filekey_proc, filekey_lookup, firstfile)
            # if newval1 != [[]]:
            #     newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            #     newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow


# secondaryagglookupvaluesfromfile_UTR(casefieldname, ["SFE-Amazon-UTR", ["STX_NAME", "order id", "selling fees",
    # "fba fees", "other transaction fees", "total", "STX_SHIPPING_COST"]], curfilerow,
    # tempvalid, keyfile, filekey_proc, filekey_lookup)
# ["SFE-Amazon-UTR", [["STX_NAME", "order id", "selling fees", "fba fees", "other transaction fees", "total", "STX_COMMISSION_FEES"]]]
def secondaryagglookupvaluesfromfile_UTR(casefieldname, lookupfilenamekeywordpair, curfilerow, tempvalid, keyfile,
                                         filekey_proc, filekey_lookup, firstfile):
    SALVFF_UTR_DEBUG = False

    newfilerow = curfilerow

    if SALVFF_UTR_DEBUG:
        print("lookupfilenamekeywordpair:" + str(lookupfilenamekeywordpair))

    srcmatchname = lookupfilenamekeywordpair[1][0]
    lkupmatchname = lookupfilenamekeywordpair[1][1]
    lkuptargetname_sellfees = lookupfilenamekeywordpair[1][2]
    lkuptargetname_fbafees = lookupfilenamekeywordpair[1][3]
    lkuptargetname_otherfees = lookupfilenamekeywordpair[1][4]
    lkuptargetname_total = lookupfilenamekeywordpair[1][5]
    srcdestname = lookupfilenamekeywordpair[1][6]
    if SALVFF_UTR_DEBUG:
        print("srcmatchname:" + str(srcmatchname))
        print("lkupmatchname:" + str(lkupmatchname))
        print("lkuptargetname_sellfees:" + str(lkuptargetname_sellfees))
        print("lkuptargetname_fbafees:" + str(lkuptargetname_fbafees))
        print("lkuptargetname_otherfees:" + str(lkuptargetname_otherfees))
        print("lkuptargetname_total:" + str(lkuptargetname_total))
        print("srcdestname:" + str(srcdestname))

    mainxitortypestr = lookupfilenamekeywordpair[0]
    if SALVFF_UTR_DEBUG:
        print("mainxitortypestr:" + str(mainxitortypestr))

    srcmatchloc = int(filekey_proc["getsourcefilekeybyvalue"][0](srcmatchname)[1] - 1)
    lkupmatchloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", lkupmatchname)[1] - 1)
    lkuptargetloc_sellfees = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", lkuptargetname_sellfees)[1] - 1)
    lkuptargetloc_fbafees = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", lkuptargetname_fbafees)[1] - 1)
    lkuptargetloc_otherfees = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", lkuptargetname_otherfees)[1] - 1)
    lkuptargetloc_total = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", lkuptargetname_total)[1] - 1)
    srcdestloc = int(filekey_proc["getsourcefilekeybyvalue"][0](srcdestname)[1] - 1)
    if SALVFF_UTR_DEBUG:
        print("srcmatchloc:" + str(srcmatchloc))
        print("lkupmatchloc:" + str(lkupmatchloc))
        print("lkuptargetloc_sellfees:" + str(lkuptargetloc_sellfees))
        print("lkuptargetloc_fbafees:" + str(lkuptargetloc_fbafees))
        print("lkuptargetloc_otherfees:" + str(lkuptargetloc_otherfees))
        print("lkuptargetloc_total:" + str(lkuptargetloc_total))
        print("srcdestloc:" + str(srcdestloc))

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword(mainxitortypestr)
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"')

        targetfound = False

        srcmatchval = curfilerow[srcmatchloc]

        linetypeloc = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0]("UTR", "type")[1] - 1)
        templinetypeval = ""

        aggfees = 0.0
        aggtotals = 0.0
        aggfeecount = 0
        donothing = 0  # does nothing, placeholder


        for temprow in dcreader2:
            # print("secondaryagglookupvaluesfromfile_UTR|temprow:" + str(temprow))

            if len(temprow) != filekey_lookup["getlookupsourcefilekeylength_multi"][0](mainxitortypestr):
                if SALVFF_UTR_DEBUG:
                    print("*lookupfile line skipped - line length mismatch:" + str(len(temprow)) + "|"
                          + str(filekey_lookup["getlookupsourcefilekeylength_multi"][0](mainxitortypestr)))
                continue

            templkupmatchval = temprow[lkupmatchloc]
            templinetypeval = temprow[linetypeloc]

            # print("Searching: " + str(srcmatchval) + " | " + str(templkupmatchval))

            match templinetypeval:
                case "Order":

                    if srcmatchval != "" and templkupmatchval != "" and srcmatchval == templkupmatchval:
                        targetfound = True

                        if SALVFF_UTR_DEBUG:
                            print("ID1 found - UTR Costs by ID: " + str(srcmatchval) + " | " + str(templkupmatchval))

                        lkuptargetval_sellfees = temprow[lkuptargetloc_sellfees]
                        if lkuptargetval_sellfees == "":
                            lkuptargetval_sellfees = 0.0
                        lkuptargetval_fbafees = temprow[lkuptargetloc_fbafees]
                        if lkuptargetval_fbafees == "":
                            lkuptargetval_fbafees = 0.0
                        lkuptargetval_otherfees = temprow[lkuptargetloc_otherfees]
                        if lkuptargetval_otherfees == "":
                            lkuptargetval_otherfees = 0.0
                        lkuptargetval_total = temprow[lkuptargetloc_total]
                        if lkuptargetval_total == "":
                            lkuptargetval_total = 0.0

                        aggfees = aggfees + float(lkuptargetval_sellfees) + float(lkuptargetval_fbafees) + float(lkuptargetval_otherfees)
                        aggfeecount = aggfeecount + 1
                        aggtotals = aggtotals + float(lkuptargetval_total)
                        if SALVFF_UTR_DEBUG:
                            print("aggfees:" + str(aggfees))
                            print("aggfeecount:" + str(aggfeecount))
                            print("aggtotals:" + str(aggtotals))
                case _:
                    donothing = donothing
                    # print("UTR Line Type Unknown:" + str(templinetypeval))

        if targetfound:

            newfilerow.insert(keyfile["STX_COMMISSION_FEES"][1] - 1, aggfees)
            newfilerow.pop(keyfile["STX_COMMISSION_FEES"][1])

            newfilerow.insert(keyfile["STX_COMMISSION_FEES_COUNT"][1] - 1, aggfeecount)
            newfilerow.pop(keyfile["STX_COMMISSION_FEES_COUNT"][1])

            newfilerow.insert(keyfile["STX_PAY_FROM_MRKT"][1] - 1, aggtotals)
            newfilerow.pop(keyfile["STX_PAY_FROM_MRKT"][1])

            # for tempkey in keyfile:
            #     tempcount1 = 0
            #     # print(keyfile[tempkey])
            #     if keyfile[tempkey][1] - 1 == templkupsrcvals4:
            #         # print("y1")
            #         # print("templkupsrcvals4:" + str(templkupsrcvals4))
            #         # print("keyfile[tempkey]:" + str(keyfile[tempkey]))
            #         newfilerow.insert(int(templkupsrcvals4), aggtotal[0])
            #         newfilerow.pop(int(templkupsrcvals4) + 1)
            #         match casefieldname:
            #             case "STX_SHIPPING_COST":
            #                 newfilerow.insert(int(keyfile["STX_SHIPPING_COST_COUNT"][1]) - 1, aggcount[0])
            #                 newfilerow.pop(int(keyfile["STX_SHIPPING_COST_COUNT"][1]))
            #     tempcount1 = tempcount1 + 1

    if SALVFF_UTR_DEBUG:
        print("secondaryagglookupvaluesfromfile_UTR|newfilerow:" + str(newfilerow))

    return newfilerow




def finalerrorcheck(filerow, keyfile, keyfilelength, curfile, initlength, filekey_proc):

    newfilerow = filerow
    # keyfilebaselength = switcher2.getsourcefilekeybaselength(curfile)
    keyfilebaselength = filekey_proc["getsourcefilekeybaselength"][0]()
    errorstr = ""
    errorflag = False

    if str(newfilerow).find("ERROR") != -1:

        for temprow in newfilerow:
            # print(temprow)
            if str(temprow).find("ERROR") != -1:
                errorflag = True
                # print("{CNE-DC Errors found: " + str(temprow) + " | " + str(keyfilebaselength))
                errorstr = errorstr + "CNE-DC Errors found: " + str(temprow) + "}"

    if initlength + keyfilebaselength > keyfilelength:
        errorflag = True
        errorstr = errorstr + "{CNE-DC Errors found: Row length different than expected - possible unexpected data " \
            "parsing error: " + str(initlength) + " | " + str(keyfilebaselength) + " | " + str(keyfilelength) + "}"

    if errorflag:
        print(errorstr)
        newfilerow = pushfinalerrormessage(newfilerow, keyfile, errorstr)

    return [newfilerow, errorflag, errorstr]


def pushfinalerrormessage(filerow, keyfile, errorstr):

    newfilerow = filerow

    for tempkey in keyfile:
        # print(keyfile[tempkey])
        if keyfile[tempkey][3] == "SHIP_HAS_DATA_ISSUE":
            # print("y1")
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, "Yes")
            newfilerow.pop(int(keyfile[tempkey][1]))

        if keyfile[tempkey][3] == "SHIP_DATA_ISSUE_NOTES":
            # print("y2")
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, errorstr)
            newfilerow.pop(int(keyfile[tempkey][1]))

    return newfilerow


# find matching orders from CIQ - primary xitor key
def ciqidlookupadd(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup):

    LOCAL_CONSOLE_OUTPUT1 = False

    # filekey_lookup_value =

    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()
    if LOCAL_CONSOLE_OUTPUT1:
        print(mainxitortypekeyword)

    # print("filekey_lookup:" + str(filekey_lookup))

    tempinfoxitor = getinfofromxitortypekeyword(mainxitortypekeyword)
    xitorprefix = tempinfoxitor[0]
    mainxlookupposition = tempinfoxitor[2]
    mainxfinalposition = tempinfoxitor[3]
    if LOCAL_CONSOLE_OUTPUT1:
        print(tempinfoxitor)


    lookuporderidnames = filekey_lookup["getlookuporderidnames"][0](xitorprefix)
    if LOCAL_CONSOLE_OUTPUT1:
        print(lookuporderidnames)
    lookuporderid1name = lookuporderidnames[0]
    lookuporderid2name = lookuporderidnames[1]

    newfilerow = filerow
    # print("lookupadd:" + str(newfilerow))

    # lookupkey = switcher2.getlookupsourcefilekey("CIQ")

    # lookup file - col position of comparison value - find position of column to lookup within lookup file
    # lookupposition = int(switcher2.getlookupsourcefilekeybyvalue("CIQ", "SHIP Order ID")[1])-1
    # lookupposition = int(switcher2.getlookupsourcefilekeybyvalue("CIQ", "SHIP Order ID")[1]) - 1
    # print(type(filekey_lookup))
    # print(filekey_lookup["getlookupsourcefilekeybyvalue"][0])
    lookupposition = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxlookupposition)[1]) - 1
    # filekey_proc["getlookupsourcefilekeybyvalue"][0]()
    # print(lookupposition)

    # lookup file - col position of target value to retrieve - find placement of final ID value (Xitor) within lookup file row
    # lookupfinalkeyposition = int(switcher2.getlookupsourcefilekeybyvalue("CIQ", "SHIP Shipment CNE ID")[1]) - 1
    lookupfinalkeyposition = int(filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxfinalposition)[1]) - 1
    # filekey_proc["getlookupsourcefilekeybyvalue"][0]

    # lookup file - col position of backup comparison value
    # secondarychecklookup = switcher2.getsourceidrefforlookup("CIQ")
    secondarychecklookup = filekey_lookup["getsourceidrefforlookup"][0](mainxitortypekeyword)
    if LOCAL_CONSOLE_OUTPUT1:
        print("secondarychecklookup:" + str(secondarychecklookup))
    # filekey_proc["getsourceidrefforlookup"][0]
    # lookuppositiontempkey = switcher2.getlookupsourcefilekeybyvalue("CIQ", secondarychecklookup)
    lookuppositiontempkey = filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, secondarychecklookup)
    # filekey_proc["getlookupsourcefilekeybyvalue"][0]
    lookupposition2 = int(lookuppositiontempkey[1]) - 1

    # current file - col position of comparison value - find id value to match within current row to search for within lookup file
    # filerowposition = int(switcher2.getsourcefilekeybyvalue(curfile, "SHIP_GEN_ORDER_ID")[1]) - 1
    filerowposition = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid1name)[1]) - 1
    # filekey_proc["getsourcefilekeybyvalue"][0]
    # print(filerowposition)

    # current file - col position of backup comparison value - find id value to match within current row to search for within lookup file
    # filerowposition2 = int(switcher2.getsourcefilekeybyvalue(curfile, "SHIP_GEN_ORDER_ID_2")[1]) - 1
    filerowposition2 = int(filekey_proc["getsourcefilekeybyvalue"][0](lookuporderid2name)[1]) - 1
    # filekey_proc["getsourcefilekeybyvalue"][0]
    # print(filerowposition)

    # lookupidresult = ciqsearchlookupfile(filerowvalue, filerowvalue2, lookupposition, lookupposition2,
    #                                      lookupfinalkeyposition, filekey_proc)



    filerowvalue = newfilerow[filerowposition]
    filerowvalue = str(filerowvalue).replace("\'", "")
    filerowvalue = str(filerowvalue).replace("||", "")
    filerowvalue = str(filerowvalue).replace(" ", "")
    # print(":" + str(filerowvalue))
    # lookupposition2 = ""

    filerowvalue2 = newfilerow[filerowposition2]
    filerowvalue2 = str(filerowvalue2).replace("\'", "")
    filerowvalue2 = str(filerowvalue2).replace("||", "")
    filerowvalue2 = str(filerowvalue2).replace(" ", "")

    if LOCAL_CONSOLE_OUTPUT1:
        print(str(filerowvalue) + "/" + str(filerowvalue2) + "---" + str(lookupposition) + "---" + str(
            lookupposition2) + "---" + str(
            lookupfinalkeyposition))

    #secondary check if first value doesnt work
    # if filerowvalue == '':
    #
    #     # secondarycheck = switcher2.getsourceidrefforlookup("CIQ")
    #     # lookuppositiontempkey = switcher2.getlookupsourcefilekeybyvalue("CIQ", secondarycheck)
    #     # lookupposition2 = int(lookuppositiontempkey[1]) - 1
    #     # filerowposition = int(switcher2.getsourcefilekeybyvalue(curfile, lookuppositiontempkey[3])[1])-1
    #     # secondarychecklookup = switcher2.getsourceidrefforlookup("CIQ")
    #     # # print(secondarychecklookup)
    #     # lookuppositiontempkey = switcher2.getlookupsourcefilekeybyvalue("CIQ", secondarychecklookup)
    #     # print(lookuppositiontempkey)
    #     # lookupposition2 = int(lookuppositiontempkey[1]) - 1
    #     # print("lookupposition2: " + str(lookupposition2))
    #     # secondarychecksource = switcher2.getsourceidrefforlookup(curfile)
    #     # # print(secondarychecksource)
    #     # filerowposition = int(switcher2.getsourcefilekeybyvalue(curfile, secondarychecksource)[1]) - 1
    #     # filerowvalue = newfilerow[filerowposition]
    #     # filerowvalue = str(filerowvalue).replace("\'", "")
    #     # filerowvalue = str(filerowvalue).replace("||", "")
    #     # # print("secondary: " + str(filerowvalue))
    #     # if filerowvalue == '':
    #     print("No lookup ID found - End Lookup")
    #     return newfilerow


    # print("filerowvalue1: " + str(filerowvalue))

    lookupidresult = ciqsearchlookupfile(filerowvalue, filerowvalue2, lookupposition, lookupposition2,
                                         lookupfinalkeyposition, filekey_proc)

    for tempkey in keyfile:
        # print(keyfile[tempkey])
        if keyfile[tempkey][2] == -1:  # locate primary xitor key by value==-1, should only be one option
            # print("y1")
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, lookupidresult)
            newfilerow.pop(int(keyfile[tempkey][1]))

    # for temprow in newfilerow:
    #     # print(temprow)
    #     if temprow.find("ERROR") != -1:
    #         errorflag = True
    #         print("{CNE-DC Errors found: " + str(temprow) + " | " + str(keyfilebaselength))
    #         errorstr = errorstr + "CNE-DC Errors found: " + str(temprow) + "}"

    return newfilerow



# ciqsearchlookupfile(filerowvalue, lookupposition, lookupposition2, lookupfinalkeyposition)
def ciqsearchlookupfile(lookupvalue, lookupvalue2, poslookup, poslookup2, lookupkeyloc, filekey_proc):

    LOCAL_CONSOLE_OUTPUT1 = False

    matchingrowvalue = ""
    # print(matchingrowvalue)

    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()

    tempinfoxitor = getinfofromxitortypekeyword(mainxitortypekeyword)
    mainxitortypeprefix = tempinfoxitor[0]
    mainxitortypekeylength = tempinfoxitor[1]

    lookupvalue = lookupvalue.replace("\"", "")

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword("cne.onevizion.com_Trackor Browser" + mainxitortypekeyword)
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for temprow in dcreader2:
            # print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(lookupkeyloc))
            # print(str(lookupvalue))
            # print(temprow)
            if temprow[poslookup] != "" and lookupvalue != "" and temprow[poslookup] == lookupvalue:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID found: " + lookupvalue + " | " + str(temprow))
            # else:
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            #     if temprow[poslookup] == (lookupvalue) or temprow[poslookup2] == (lookupvalue):
            #         matchingrowvalue = temprow[lookupkeyloc]
            #         matchingrowvalue = matchingrowvalue[0:14]  # CIQ Shipment IDs are 14 chars this trims trailing alias
            #         print("ID found: " + lookupvalue + " | " + str(temprow))
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            if temprow[poslookup2] != "" and lookupvalue2 != "" and temprow[poslookup2] == lookupvalue2:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                if LOCAL_CONSOLE_OUTPUT1:
                    print("ID2 found: " + lookupvalue2 + " | " + str(temprow))
            if matchingrowvalue != "":
                return matchingrowvalue

    return matchingrowvalue


# find matching orders from CIQ - primary xitor key
def ciqidlookupaddmulti(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup):

    # filekey_lookup_value =
    ciqlookupaddmultivals = filekey_proc["getciqidlookupaddmulti"][0]()
    print("ciqlookupaddmultivals:" + str(ciqlookupaddmultivals))


    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()
    print(mainxitortypekeyword)

    print("filekey_lookup:" + str(filekey_lookup))

    #  return [mainxitortypeprefix, mainxitorkeylength, mainxlookupposition, mainxlookupfinalpos]
    tempinfoxitor = getinfofromxitortypekeyword([mainxitortypekeyword, mainxitortypekeyword])
    xitorprefix = tempinfoxitor[0]
    mainxlookuppositionlist = tempinfoxitor[2]
    mainxfinalpositionlist = tempinfoxitor[3]
    print(tempinfoxitor)

    # lookuppositionlist = mainxlookuppositionlist  # field names to concat and lookup in lookup file
    # lookupfinalkeyposition = mainxfinalpositionlist  # field names to return from lookup file after match
    # filerowpositionlist = ciqlookupaddmultivals  # field names to concat and lookup in source file


    lookuporderidnames = filekey_lookup["getlookuporderidnames"][0](xitorprefix)
    print(lookuporderidnames)
    lookuporderid1name = lookuporderidnames[0]
    lookuporderid2name = lookuporderidnames[1]

    newfilerow = filerow
    print("lookupadd:" + str(newfilerow))

    # lookupkey = switcher2.getlookupsourcefilekey("CIQ")

    # lookup file - col position of comparison value - find position of column to lookup within lookup file
    lookuppositionpart1 = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxlookuppositionlist[0])[1]) - 1
    lookuppositionpart2 = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxlookuppositionlist[1])[1]) - 1
    print("lookuppositionpart1|lookuppositionpart2:" + str(lookuppositionpart1) + "|" + str(lookuppositionpart2))

    # lookup file - col position of target value to retrieve - find placement of final ID value (Xitor) within lookup file row
    lookupfinalkeyposition = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxfinalpositionlist[0])[1]) - 1
    print("lookupfinalkeyposition:" + str(lookupfinalkeyposition))

    # current file - col position of comparison value - find id value to match within current row to search for within lookup file
    filerowpositionpart1 = int(filekey_proc["getsourcefilekeybyvalue"][0](ciqlookupaddmultivals[0])[1]) - 1
    # print(filerowposition)
    # current file - col position of backup comparison value - find id value to match within current row to search for within lookup file
    filerowpositionpart2 = int(filekey_proc["getsourcefilekeybyvalue"][0](ciqlookupaddmultivals[1])[1]) - 1
    # print(filerowposition)
    print("filerowpositionpart1|filerowpositionpart2:" + str(filerowpositionpart1) + "|" + str(filerowpositionpart2))

    lookuppositionlist = [lookuppositionpart1, lookuppositionpart2]  # field names to concat and lookup in lookup file
    lookupfinalkeyposition = [lookupfinalkeyposition]  # field names to return from lookup file after match
    filerowpositionlist = [filerowpositionpart1, filerowpositionpart2]  # field names to concat and lookup in source file
    filerowvallist = [newfilerow[filerowpositionpart1], newfilerow[filerowpositionpart2]]

    # filerowvalue = newfilerow[filerowposition]
    # filerowvalue = str(filerowvalue).replace("\'", "")
    # filerowvalue = str(filerowvalue).replace("||", "")
    # filerowvalue = str(filerowvalue).replace(" ", "")
    # # print(":" + str(filerowvalue))
    # # lookupposition2 = ""
    #
    # filerowvalue2 = newfilerow[filerowposition2]
    # filerowvalue2 = str(filerowvalue2).replace("\'", "")
    # filerowvalue2 = str(filerowvalue2).replace("||", "")
    # filerowvalue2 = str(filerowvalue2).replace(" ", "")

    # print(str(lookuppositionlist) + "/" + str(filerowvalue2) + "---" + str(lookupposition) + "---" + str(
    #     lookupposition2) + "---" + str(
    #     lookupfinalkeyposition))

    lookupidresult = ciqsearchlookupfilemulti(
        filerowpositionlist, filerowvallist, lookuppositionlist, lookupfinalkeyposition, filekey_proc)

    for tempkey in keyfile:
        # print(keyfile[tempkey])
        if keyfile[tempkey][2] == -1:  # locate primary xitor key by value==-1, should only be one option
            # print("y1")
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, lookupidresult)
            newfilerow.pop(int(keyfile[tempkey][1]))

    # for temprow in newfilerow:
    #     # print(temprow)
    #     if temprow.find("ERROR") != -1:
    #         errorflag = True
    #         print("{CNE-DC Errors found: " + str(temprow) + " | " + str(keyfilebaselength))
    #         errorstr = errorstr + "CNE-DC Errors found: " + str(temprow) + "}"

    return newfilerow


# find matching orders from CIQ - primary xitor key
def ciqidlookupaddmulti(filerow, keyfile, keyfilelength, curfile, filekey_proc, filekey_lookup):

    # filekey_lookup_value =
    ciqlookupaddmultivals = filekey_proc["getciqidlookupaddmulti"][0]()
    print("ciqlookupaddmultivals:" + str(ciqlookupaddmultivals))


    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()
    print(mainxitortypekeyword)

    print("filekey_lookup:" + str(filekey_lookup))

    #  return [mainxitortypeprefix, mainxitorkeylength, mainxlookupposition, mainxlookupfinalpos]
    tempinfoxitor = getinfofromxitortypekeyword([mainxitortypekeyword, mainxitortypekeyword])
    xitorprefix = tempinfoxitor[0]
    mainxlookuppositionlist = tempinfoxitor[2]
    mainxfinalpositionlist = tempinfoxitor[3]
    print(tempinfoxitor)

    # lookuppositionlist = mainxlookuppositionlist  # field names to concat and lookup in lookup file
    # lookupfinalkeyposition = mainxfinalpositionlist  # field names to return from lookup file after match
    # filerowpositionlist = ciqlookupaddmultivals  # field names to concat and lookup in source file


    lookuporderidnames = filekey_lookup["getlookuporderidnames"][0](xitorprefix)
    print(lookuporderidnames)
    lookuporderid1name = lookuporderidnames[0]
    lookuporderid2name = lookuporderidnames[1]

    newfilerow = filerow
    print("lookupadd:" + str(newfilerow))

    # lookupkey = switcher2.getlookupsourcefilekey("CIQ")

    # lookup file - col position of comparison value - find position of column to lookup within lookup file
    lookuppositionpart1 = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxlookuppositionlist[0])[1]) - 1
    lookuppositionpart2 = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxlookuppositionlist[1])[1]) - 1
    print("lookuppositionpart1|lookuppositionpart2:" + str(lookuppositionpart1) + "|" + str(lookuppositionpart2))

    # lookup file - col position of target value to retrieve - find placement of final ID value (Xitor) within lookup file row
    lookupfinalkeyposition = int(
        filekey_lookup["getlookupsourcefilekeybyvalue"][0](mainxitortypekeyword, mainxfinalpositionlist[0])[1]) - 1
    print("lookupfinalkeyposition:" + str(lookupfinalkeyposition))

    # current file - col position of comparison value - find id value to match within current row to search for within lookup file
    filerowpositionpart1 = int(filekey_proc["getsourcefilekeybyvalue"][0](ciqlookupaddmultivals[0])[1]) - 1
    # print(filerowposition)
    # current file - col position of backup comparison value - find id value to match within current row to search for within lookup file
    filerowpositionpart2 = int(filekey_proc["getsourcefilekeybyvalue"][0](ciqlookupaddmultivals[1])[1]) - 1
    # print(filerowposition)
    print("filerowpositionpart1|filerowpositionpart2:" + str(filerowpositionpart1) + "|" + str(filerowpositionpart2))

    lookuppositionlist = [lookuppositionpart1, lookuppositionpart2]  # field names to concat and lookup in lookup file
    lookupfinalkeyposition = [lookupfinalkeyposition]  # field names to return from lookup file after match
    filerowpositionlist = [filerowpositionpart1, filerowpositionpart2]  # field names to concat and lookup in source file
    filerowvallist = [newfilerow[filerowpositionpart1], newfilerow[filerowpositionpart2]]

    # filerowvalue = newfilerow[filerowposition]
    # filerowvalue = str(filerowvalue).replace("\'", "")
    # filerowvalue = str(filerowvalue).replace("||", "")
    # filerowvalue = str(filerowvalue).replace(" ", "")
    # # print(":" + str(filerowvalue))
    # # lookupposition2 = ""
    #
    # filerowvalue2 = newfilerow[filerowposition2]
    # filerowvalue2 = str(filerowvalue2).replace("\'", "")
    # filerowvalue2 = str(filerowvalue2).replace("||", "")
    # filerowvalue2 = str(filerowvalue2).replace(" ", "")

    # print(str(lookuppositionlist) + "/" + str(filerowvalue2) + "---" + str(lookupposition) + "---" + str(
    #     lookupposition2) + "---" + str(
    #     lookupfinalkeyposition))

    lookupidresult = ciqsearchlookupfilemulti(
        filerowpositionlist, filerowvallist, lookuppositionlist, lookupfinalkeyposition, filekey_proc)

    for tempkey in keyfile:
        # print(keyfile[tempkey])
        if keyfile[tempkey][2] == -1:  # locate primary xitor key by value==-1, should only be one option
            # print("y1")
            newfilerow.insert(int(keyfile[tempkey][1]) - 1, lookupidresult)
            newfilerow.pop(int(keyfile[tempkey][1]))

    # for temprow in newfilerow:
    #     # print(temprow)
    #     if temprow.find("ERROR") != -1:
    #         errorflag = True
    #         print("{CNE-DC Errors found: " + str(temprow) + " | " + str(keyfilebaselength))
    #         errorstr = errorstr + "CNE-DC Errors found: " + str(temprow) + "}"

    return newfilerow


# ciqsearchlookupfile(filerowpositionlist, lookuppositionlist, lookupfinalkeyposition, filekey_proc)
# OLD: ciqsearchlookupfile(lookupvalue, lookupvalue2, poslookup, poslookup2, lookupkeyloc, filekey_proc):
def ciqsearchlookupfilemulti(filerowpositionlist, filerowvallist, lookuppositionlist, lookupfinalkeyposition, filekey_proc):
    matchingrowvalue = ""
    # print(matchingrowvalue)

    filerowval1 = filerowvallist[0]
    filerowval2 = filerowvallist[1]

    filerowvalstr = str(filerowval1) + str(filerowval2)

    lookupposition1 = lookuppositionlist[0]
    lookupposition2 = lookuppositionlist[1]

    lookupkeyloc = lookupfinalkeyposition[0]


    mainxitortypekeyword = filekey_proc["getmainxitorlookuptype"][0]()

    tempinfoxitor = getinfofromxitortypekeyword(mainxitortypekeyword)
    mainxitortypeprefix = tempinfoxitor[0]
    mainxitortypekeylength = tempinfoxitor[1]

    # lookupvalue = lookupvalue.replace("\"", "")

    # curfilename = "cne.onevizion.com_Trackor Browser_Shipment_02162025174347.csv"
    curfilename = getlookupfilenamebykeyword("cne.onevizion.com_Trackor Browser" + mainxitortypekeyword)
    script_dir = os.path.dirname(__file__)
    reloutputfile = curfilename
    if reloutputfile is None:
        print("***ERROR***: CIQ Lookup file not found - check file is in correct place and is .csv")
    lookupfile = os.path.join(script_dir, reloutputfile)

    with open(lookupfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        for temprow in dcreader2:
            # print(str(lookupvalue) + "/" + str(lookupvalue2) + "---" + str(poslookup) + "---" + str(poslookup2) + "---" + str(lookupkeyloc))
            # print(str(lookupvalue))
            # print(temprow)
            tempfilerowlookupval = str(temprow[lookupposition1]) + str(temprow[lookupposition2])

            if str(temprow[lookupposition1]) != "" and str(temprow[lookupposition2]) != "" and tempfilerowlookupval == filerowvalstr:
                matchingrowvalue = temprow[lookupkeyloc]
                matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
                print("ID pair found: " + filerowvalstr + " | " + str(temprow))
            # else:
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            #     if temprow[poslookup] == (lookupvalue) or temprow[poslookup2] == (lookupvalue):
            #         matchingrowvalue = temprow[lookupkeyloc]
            #         matchingrowvalue = matchingrowvalue[0:14]  # CIQ Shipment IDs are 14 chars this trims trailing alias
            #         print("ID found: " + lookupvalue + " | " + str(temprow))
            #     # if temprow[poslookup].find(lookupvalue) != -1 or temprow[poslookup2].find(lookupvalue) != -1:
            # if temprow[poslookup2] != "" and lookupvalue2 != "" and temprow[poslookup2] == lookupvalue2:
            #     matchingrowvalue = temprow[lookupkeyloc]
            #     matchingrowvalue = matchingrowvalue[0:mainxitortypekeylength]  # CIQ Shipment IDs are 14 chars this trims trailing alias
            #     print("ID2 found: " + lookupvalue2 + " | " + str(temprow))
            if matchingrowvalue != "":
                return matchingrowvalue

    return matchingrowvalue


# SWITCHER

switcher_functionkey_processing = {

    "processfileheaderrow": [processfileheaderrow],
    "translatefileheaderrow1": [translatefileheaderrow1],
    "translatefileheaderrow2": [translatefileheaderrow2],
    "processfilenextrow": [processfilenextrow],
    "processcalculatedrows": [processcalculatedrows],
    "processtranslatedrows": [processtranslatedrows],
    "finalerrorcheck": [finalerrorcheck],
    "pushfinalerrormessage": [pushfinalerrormessage],
    "ciqidlookupadd": [ciqidlookupadd],
    "ciqsearchlookupfile": [ciqsearchlookupfile],
    # "buildcombinedshipmentslist": [buildcombinedshipmentslist],
    # "markcombinedshipments": [markcombinedshipments],
    # "sourcefilekey_processing": [sourcefilekey_processing],
    # "general_post_processing": [general_post_processing]
}

def getfunctionkey(sourcefiletype):

    if sourcefiletype is None:
        return None

    outputfile = ""

    match sourcefiletype:
        case "ShipRush":
            outputfile = SourceFileKey_ShipRush.getfunctionkey()
        case "Veeqo":
            outputfile = SourceFileKey_Veeqo.getfunctionkey()
        case "Ebay-Orders":
            outputfile = SourceFileKey_Ebay_Orders.getfunctionkey()
        case "Ebay-Shipping":
            outputfile = SourceFileKey_Ebay_Shipping.getfunctionkey()
        case "STX-Amazon-AO":
            outputfile = SourceFileKey_AmazonAO_STX.getfunctionkey()
        case "SLN-Amazon-AO":
            outputfile = SourceFileKey_AmazonAO_SLN.getfunctionkey()
        case "SFE-Amazon-UTR":
            outputfile = SourceFileKey_AmazonUTR_SFE.getfunctionkey()
        case "Veeqo-Orders-STX":
            outputfile = SourceFileKey_Veeqo_Orders.getfunctionkey()


    return outputfile


def getfunctionkey_lookup(placeholder, outputxitortype):

    if outputxitortype is None:
        return None

    outputfile = ""

    match placeholder:
        case "CIQ":
            outputfile = GenFieldKey_CIQ1.getfunctionkey(outputxitortype)


    return outputfile


def getfilekey_lookup(placeholder, outputxitortype):

    if outputxitortype is None:
        return None

    outputfile = ""

    match placeholder:
        case "CIQ":
            outputfile = GenFieldKey_CIQ1.getlookupsourcefilekey(outputxitortype)


    return outputfile


def getfunctionkey_processing(sourcefiletype, bsfp):

    if sourcefiletype is None:
        return None

    outputkey_basekey = ""
    outputkey = {}
    count = 0



    match sourcefiletype:
        case "ShipRush":
            outputkey_basekey = SourceFileKey_ShipRush.getfunctionkey_processing()
        case "Veeqo":
            outputkey_basekey = SourceFileKey_Veeqo.getfunctionkey_processing()
        case "Ebay-Orders":
            outputkey_basekey = SourceFileKey_Ebay_Orders.getfunctionkey_processing()
        case "Ebay-Shipping":
            outputkey_basekey = SourceFileKey_Ebay_Shipping.getfunctionkey_processing()
        case "STX-Amazon-AO":
            outputkey_basekey = SourceFileKey_AmazonAO_STX.getfunctionkey_processing()
        case "SLN-Amazon-AO":
            outputkey_basekey = SourceFileKey_AmazonAO_SLN.getfunctionkey_processing()
        case "SFE-Amazon-UTR":
            outputkey_basekey = SourceFileKey_AmazonUTR_SFE.getfunctionkey_processing()
        case "Veeqo-Orders-STX":
            outputkey_basekey = SourceFileKey_Veeqo_Orders.getfunctionkey_processing()


    # print("bsfp:" + str(bsfp))
    # print("outputkey_basekey:" + str(outputkey_basekey))

    for keyrow in outputkey_basekey:
        if outputkey_basekey[keyrow]:
            for switcher_keyrow in bsfp:
                # print(switcher_keyrow)
                # print(outputkey[keyrow])
                if switcher_keyrow == keyrow:
                    # print(switcher_keyrow)
                    outputkey[keyrow] = bsfp[switcher_keyrow]
                    # print(outputkey[keyrow])

    # outputkey.pop(0)

    print("Ebay:" + str(outputkey))

    return outputkey

def buildcombinedshipmentslist(fullinputrowlist, colplacement_xitor, colplacement_track, combinedshipmentslist):

    for temprow in fullinputrowlist:
        # if len(temprow) > 0:
        # print("temprow: " + str(temprow[0]))
        tempcount = 0
        tempmatch = False
        for temprow2 in fullinputrowlist:
            # if temprow != [] and temprow2 != []:
            #     print(temprow)
            #     print(temprow[40])
            #     print(temprow2)
            #     print(temprow2[40])

            # If Xitor IDs match, mark as combined
            if temprow != [] and temprow2 != [] and len(temprow[colplacement_xitor]) > 0 and len(
                    temprow2[colplacement_xitor]) > 0:
                # print("temprow/2[colplacement_xitor]: " + temprow[colplacement_xitor] + "---" + temprow2[
                #     colplacement_xitor])
                if temprow[colplacement_xitor] == temprow2[colplacement_xitor]:  # compare xitor's
                    tempmatch = True

            # If tracking IDs match, mark as combined
            if temprow != [] and temprow2 != [] and len(temprow[colplacement_track]) > 0 and len(
                    temprow2[colplacement_track]) > 0:
                temprowstr = str(temprow[colplacement_track])
                temprowstr = temprowstr.replace("||", "")
                temprowstr = temprowstr.replace("\'", "")
                temprowstr = temprowstr.replace(" ", "")
                temprowstr2 = str(temprow2[colplacement_track])
                temprowstr2 = temprowstr2.replace("||", "")
                temprowstr2 = temprowstr2.replace("\'", "")
                temprowstr2 = temprowstr2.replace(" ", "")
                # print(colplacement_track)
                # print("temprow[colplacement_track]: " + temprowstr + "---" + temprowstr2)
                if temprowstr == temprowstr2 and len(temprowstr) > 1 and len(
                        temprowstr2) > 1:  # compare tracking numbers
                    tempmatch = True
                    # print("temprow[32]: " + temprowstr + "---" + temprowstr2)
            if tempmatch:
                tempcount += 1
                tempmatch = False
        if tempcount > 1:
            # print(str(tempcount) + " MATCHES: " + str(temprow[colplacement_xitor]) + " --- " + str(temprow[colplacement_xitor]))
            # print(temprow)
            # print("---")
            # combinedshipmentslist.append([str(temprow[colplacement_xitor]), str(temprow[colplacement_xitor])])
            combinedshipmentslist.append([str(temprow[colplacement_xitor]), str(temprow[colplacement_track])])

        return [combinedshipmentslist, tempcount]


def markcombinedshipments(fullinputrowlist, colplacement_xitor, colplacement_track, combinedshipmentslist, filekey_1):
    for temprowcomb in combinedshipmentslist:
        count = 0
        for temprowfull in fullinputrowlist:

            if temprowcomb != [] and temprowfull != []:
                temprowcombstr1 = temprowcomb[0]
                temprowcombstr1 = temprowcombstr1.replace("||", "")
                temprowcombstr1 = temprowcombstr1.replace("\'", "")
                temprowcombstr2 = temprowcomb[1]
                temprowcombstr2 = temprowcombstr2.replace("||", "")
                temprowcombstr2 = temprowcombstr2.replace("\'", "")
                temprowfullstr1 = temprowfull[colplacement_xitor]
                temprowfullstr1 = temprowfullstr1.replace("||", "")
                temprowfullstr1 = temprowfullstr1.replace("\'", "")
                temprowfullstr2 = temprowfull[colplacement_track]
                temprowfullstr2 = temprowfullstr2.replace("||", "")
                temprowfullstr2 = temprowfullstr2.replace("\'", "")

                # colplacement_combinedflag = switcher2.getcolplacement_combinedflag(firstfile) - 1
                colplacement_combinedflag = filekey_1["getcolplacement_combinedflag"][0]() - 1
                # print(colplacement_combinedflag)

                if temprowfullstr1 != '':
                    if temprowcombstr1 == temprowfullstr1:
                        # print(temprowcombstr1 + "---" + temprowcombstr2 + "---" + temprowfullstr1 + "---" + temprowfullstr2)
                        # if len(temprowfull) <= 96:
                        temprowfull.insert(colplacement_combinedflag, "Yes")
                        temprowfull.pop(colplacement_combinedflag + 1)

                        fullinputrowlist.insert(count, temprowfull)
                        fullinputrowlist.pop(count + 1)
                        # print(str(temprowfull))
                        # print("temprowfull: " + str(temprowfull))
                elif temprowfullstr2 != '':
                    if temprowcombstr2 == temprowfullstr2:
                        # print(temprowcombstr1 + "---" + temprowcombstr2 + "---" + temprowfullstr1 + "---" + temprowfullstr2)
                        temprowfull.insert(colplacement_combinedflag, "Yes")
                        temprowfull.pop(colplacement_combinedflag + 1)

                        fullinputrowlist.insert(count, temprowfull)
                        fullinputrowlist.pop(count + 1)
                        # print(str(temprowfull))
                        # print("temprowfull: " + str(temprowfull))
            count += 1

    return [fullinputrowlist]


def general_post_processing(fullinputrowlist, filekey_1, outputfiletype):

    # Add or modify SYSTEM CREATED DATE and SYSTEM LAST UPDATED DATE depending on ADD/UPDATE status
    fullinputrowlist = addcreatedorupdateddates(fullinputrowlist, filekey_1, outputfiletype)

    return [fullinputrowlist]


def write_row_list_to_files(fullinputrowlist, firstfile, filekey_1, f_err, f_update, f_add):

    LOCAL_CONSOLE_OUTPUT1 = False

    mainxitortypekeyword = filekey_1["getmainxitorlookuptype"][0]()

    tempinfoxitor = getinfofromxitortypekeyword(mainxitortypekeyword)
    mainxitortypeprefix = tempinfoxitor[0]
    mainxitortypekeylength = tempinfoxitor[1]

    count = 0
    for temprow in fullinputrowlist:
        if temprow != []:
            temprowstr = str(temprow)
            if LOCAL_CONSOLE_OUTPUT1:
                print(temprowstr)
                print(firstfile)
            temprowstr = str(temprowstr).replace("\'", "")
            temprowstr = str(temprowstr).replace("||", "")
            temprowstr = str(temprowstr).replace("\"", "")
            temprowstr = str(temprowstr).replace("[", "")
            temprowstr = str(temprowstr).replace("]", "")
            if firstfile.find("STX-Amazon-AO") == -1:
                temprowstr = str(temprowstr).replace("$", "")
            temprowstr = str(temprowstr).replace(", ", ",")
            if "sourcefilekey_processing_string" in filekey_1:
                temprowstr = filekey_1["sourcefilekey_processing_string"][0](temprowstr)
                # print("after2: " + str(temprowstr))
            # if firstfile == "Ebay-Orders":
            #     # temprowstr = str(temprowstr).replace("\\", "")
            #     print("after2: " + str(temprowstr))
            temprowstr = str(temprowstr).strip()
            # print(temprowstr)
            # print("---" + str(count) + "---")
            if temprowstr.find("CNE-DC Errors found") != -1:
                # print("Error")
                f_err.write(temprowstr + "\n")
            elif temprowstr[0:4] == mainxitortypeprefix:
                # print("Update")
                f_update.write(temprowstr + "\n")
            else:
                # print("Add")
                f_add.write(temprowstr + "\n")
            count += 1

    return [True, fullinputrowlist, count]


def filecleanup(curfilename):
    closecurfilename = curfilename.replace("_INPUT\\", "")
    os.rename(curfilename, "_INPUT\\PROCESSED\\" + closecurfilename)

    return [True]


def addcreatedorupdateddates(fullinputrowlist, filekey_1, outputfiletype):

    LOCAL_CONSOLE_OUTPUT1 = False

    if LOCAL_CONSOLE_OUTPUT1:
        print("outputfiletype:" + str(outputfiletype))

    match outputfiletype:
        case "SHP":
            xitorfieldname = "Shipment_XITOR_KEY"
            createdatename = "SHIP_SYSTEM_CREATED_DATE"
            updatename = "SHIP_SYSTEM_UPDATED_DATE"
        case "STX":
            xitorfieldname = "SaleTx_XITOR_KEY"
            createdatename = "STX_CREATED_AT"
            updatename = "STX_UPDATED_AT"
        case "SLN":
            xitorfieldname = "SALEBETA_XITOR_KEY"
            createdatename = "SALE_LINE__SYSTEM_CREATED_DATE"
            updatename = "SALE_LINE__SYSTEM_LAST_UPDATED"
        case _:
            xitorfieldname = ""
            createdatename = ""
            updatename = ""

    # tempxitorloc = (filekey_1["getsourcefilekeybyvalue"][0]("Shipment_XITOR_KEY")[1]) - 1
    tempxitorloc = (filekey_1["getsourcefilekeybyvalue"][0](xitorfieldname)[1]) - 1
    tempcreatedateloc = (filekey_1["getsourcefilekeybyvalue"][0](createdatename)[1]) - 1
    tempupdateloc = (filekey_1["getsourcefilekeybyvalue"][0](updatename)[1]) - 1
    current_date = datetime.now()
    tempdate = current_date.strftime("%m/%d/%Y")

    for temprow in fullinputrowlist:
        if LOCAL_CONSOLE_OUTPUT1:
            print("|" + str(temprow))
        if temprow != []:

            if temprow[tempxitorloc] != "":
                # print(temprow[tempxitorloc])
                temprow[tempcreatedateloc] = ""
                temprow[tempupdateloc] = tempdate
            else:
                temprow[tempcreatedateloc] = tempdate
            # print("|" + str(temprow))

    return fullinputrowlist