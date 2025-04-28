import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import random

# SOURCE_ID_REF_FOR_LOOKUP = "Order ID"
SOURCE_ID_REF_FOR_LOOKUP = "Tracking ID"
RANDOM_RUN_ID = "-1"
OUTPUT_FILE_KEYWORD_1 = "Veeqo"
MAIN_XITOR_LOOKUP_TYPE = "_Shipment_"


def getfunctionkey():

    return functionkey1


def getfunctionkey_processing():

    return functionkey_processing


sourcefilekey1 = {
    "Shipment_XITOR_KEY": [None, 1, -1, "Shipment_XITOR_KEY", "Shipment_XITOR_KEY", ""],
    "SHIP_HAS_DATA_ISSUE": [None, 2, 1, "SHIP_HAS_DATA_ISSUE", "SHIP_HAS_DATA_ISSUE", ""],
    "SHIP_DATA_ISSUE_NOTES": [None, 3, 1, "SHIP_DATA_ISSUE_NOTES", "SHIP_DATA_ISSUE_NOTES", ""],
    "SHIP_GEN_SERVICE": [None, 4, 1, "SHIP_GEN_SERVICE", "SHIP_GEN_SERVICE", ""],
    "SHIP_GEN_CREATE_DATE": [None, 5, 1, "SHIP_GEN_CREATE_DATE", "SHIP_GEN_CREATE_DATE", ""],
    "SHIP_GEN_CARRIER": [None, 6, 1, "SHIP_GEN_CARRIER", "SHIP_GEN_CARRIER", ""],
    "SHIP_GEN_CRR_SRV_DD": [None, 7, 1, "SHIP_GEN_CRR_SRV_DD", "SHIP_GEN_CRR_SRV_DD", ""],
    "SHIP_GEN_OWN_COMP": [None, 8, 1, "SHIP_GEN_OWN_COMP", "SHIP_GEN_OWN_COMP", ""],
    "SHIP_GEN_CHANNEL": [None, 9, 1, "SHIP_GEN_CHANNEL", "SHIP_GEN_CHANNEL", ""],
    "SHIP_RATE_SHIP_CHRG": [None, 10, 1, "SHIP_RATE_SHIP_CHRG", "SHIP_RATE_SHIP_CHRG", ""],
    "SHIP_RATESHIP_CHARGE__BASE": [None, 11, 1, "SHIP_RATESHIP_CHARGE__BASE", "SHIP_RATESHIP_CHARGE__BASE", ""],
    "SHIP_RATESHIP_CHARGE__ORIGINAL": [None, 12, 1, "SHIP_RATESHIP_CHARGE__ORIGINAL", "SHIP_RATESHIP_CHARGE__ORIGINAL",
                                       ""],
    "SHIP_PKG_FULL_DIMS": [None, 13, 1, "SHIP_PKG_FULL_DIMS", "SHIP_PKG_FULL_DIMS", ""],
    "SHIP_GEN_PKG_LENGTH": [None, 14, 1, "SHIP_GEN_PKG_LENGTH", "SHIP_GEN_PKG_LENGTH", ""],
    "SHIP_GEN_PKG_WIDTH": [None, 15, 1, "SHIP_GEN_PKG_WIDTH", "SHIP_GEN_PKG_WIDTH", ""],
    "SHIP_GEN_PKG_HEIGHT": [None, 16, 1, "SHIP_GEN_PKG_HEIGHT", "SHIP_GEN_PKG_HEIGHT", ""],
    "SHIP_GEN_PKG_WEIGHT": [None, 17, 1, "SHIP_GEN_PKG_WEIGHT", "SHIP_GEN_PKG_WEIGHT", ""],
    "SHIP_PKG_WEIGHT_OUNCES": [None, 18, 1, "SHIP_PKG_WEIGHT_OUNCES", "SHIP_PKG_WEIGHT_OUNCES", ""],
    "SHIP_PKG_WEIGHT_TEXT": [None, 19, 1, "SHIP_PKG_WEIGHT_TEXT", "SHIP_PKG_WEIGHT_TEXT", ""],
    "SHIP_GEN_ORDER_ID": [None, 20, 1, "SHIP_GEN_ORDER_ID", "SHIP_GEN_ORDER_ID", ""],
    "SHIP_GEN_ORDER_ID_2": [None, 21, 1, "SHIP_GEN_ORDER_ID_2", "SHIP_GEN_ORDER_ID_2", ""],
    "SHIP_GEN_TRACK_NUM": [None, 22, 1, "SHIP_GEN_TRACK_NUM", "SHIP_GEN_TRACK_NUM", ""],
    "SHIP_GEN_TO_STATE": [None, 23, 1, "SHIP_GEN_TO_STATE", "SHIP_GEN_TO_STATE", ""],
    "SHIP_GEN_FULL_NAME__SHIP_TO": [None, 24, 1, "SHIP_GEN_FULL_NAME__SHIP_TO", "SHIP_GEN_FULL_NAME__SHIP_TO", ""],
    "SHIP_INCOMINGOUTGOING": [None, 25, 1, "SHIP_INCOMINGOUTGOING", "SHIP_INCOMINGOUTGOING", ""],
    "SHIP_DELIVERY_STATUS": [None, 26, 1, "SHIP_DELIVERY_STATUS", "SHIP_DELIVERY_STATUS", ""],
    "SHIP_SECONDARY_TRACKING_NUMBER": [None, 27, 1, "SHIP_SECONDARY_TRACKING_NUMBER", "SHIP_SECONDARY_TRACKING_NUMBER",
                                       ""],
    "SHIP__IS_PHASE_2_RECORD": [None, 28, 1, "SHIP__IS_PHASE_2_RECORD", "SHIP__IS_PHASE_2_RECORD", ""],
    "SHIP_SYSTEM_CREATED_DATE": [None, 29, 1, "SHIP_SYSTEM_CREATED_DATE", "SHIP_SYSTEM_CREATED_DATE", ""],
    "SHIP_SYSTEM_UPDATED_DATE": [None, 30, 1, "SHIP_SYSTEM_UPDATED_DATE", "SHIP_SYSTEM_UPDATED_DATE", ""],
    "SHIP__COMBINED_SHIPMENT": [None, 31, 1, "SHIP__COMBINED_SHIPMENT", "SHIP__COMBINED_SHIPMENT", ""],
    "SHIP__DATA_SOURCE__VEEQO": [None, 32, 1, "SHIP__DATA_SOURCE__VEEQO", "SHIP__DATA_SOURCE__VEEQO", ""],
    "Shipped Date": [1, 33, 2, "Shipped Date", "ship_vq_ship_date", ""],
    "Store": [2, 34, 0, "Store", "ship_vq_store", ""],
    "Order ID": [3, 35, 0, "Order ID", "ship_vq_ord_id", "||"],
    "Carrier": [4, 36, 0, "Carrier", "ship_vq_carrier", ""],
    "Service": [5, 37, 0, "Service", "ship_vq_serv", ""],
    "Total Label Cost": [6, 38, 0, "Total Label Cost", "ship_vq_ttl_label_cost", ""],
    "Currency": [7, 39, 0, "Currency", "ship_vq_currency", ""],
    "Tracking ID": [8, 40, 0, "Tracking ID", "ship_vq_track_id", "||"],
    "Tracking Status": [9, 41, 0, "Tracking Status", "ship_vq_track_status", ""],
    "Length": [10, 42, 0, "Length", "ship_vq_length", ""],
    "Width": [11, 43, 0, "Width", "ship_vq_width", ""],
    "Height": [12, 44, 0, "Height", "ship_vq_height", ""],
    "Dimension Unit": [13, 45, 0, "Dimension Unit", "ship_vq_dim_unit", ""],
    "Weight": [14, 46, 0, "Weight", "ship_vq_weight", ""],
    "Weight Unit": [15, 47, 0, "Weight Unit", "ship_vq_weight_unit", ""],
    "Insurance Declared Value": [16, 48, 0, "Insurance Declared Value", "ship_vq_ins_decl_val", ""],
    "Charged By": [17, 49, 0, "Charged By", "ship_vq_charged_by", ""],
    "User": [18, 50, 0, "User", "ship_vq_user", ""],
    "Location": [19, 51, 0, "Location", "ship_vq_location", ""],
    "Ship From Country": [20, 52, 0, "Ship From Country", "ship_vq_ship_f_ctry", ""],
    "Ship From State": [21, 53, 0, "Ship From State", "ship_vq_ship_f_state", ""],
    "Ship From Zip": [22, 54, 0, "Ship From Zip", "ship_vq_ship_f_zip", ""],
    "Ship To Country": [23, 55, 0, "Ship To Country", "ship_vq_ship_t_ctry", ""],
    "Ship To Zip": [24, 56, 0, "Ship To Zip", "ship_vq_ship_t_zip", "||"],
    "Ship To State": [25, 57, 0, "Ship To State", "ship_vq_ship_t_state", ""],
    "Label URL": [26, 58, 0, "Label URL", "ship_vq_label_url", ""],

}

def getsourcefilekey():
    return sourcefilekey1


def getsourcefilekeylength():
    return len(sourcefilekey1)


#length of key base report rows only, no calculated rows
def getsourcefilekeybaselength():

    tempcount = 0
    for temprow in sourcefilekey1:
        # print(sourcefilekey1[temprow][2])
        if sourcefilekey1[temprow][2] == 1:
            tempcount += tempcount

    return tempcount


def getsourcefilekeybyvalue(val1):
    retkey = sourcefilekey1[val1]
    return retkey


def getcolplacement_xitor():
    retkey = sourcefilekey1["Shipment_XITOR_KEY"][1]
    return retkey


def getcolplacement_tracknum():
    retkey = sourcefilekey1["Tracking ID"][1]
    return retkey


def getcolplacement_combinedflag():
    retkey = sourcefilekey1["SHIP__COMBINED_SHIPMENT"][1]
    return retkey


def getcalcfieldvalues(casefieldname, newfilerow):

    fieldnameresult = ""

    #print(newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1])
    # checkval = newfilerow[getsourcefilekeybyvalue("Tracking ID")[1]-1]
    checkval = newfilerow[getsourcefilekeybyvalue("Carrier")[1] - 1]
    checkval = str(checkval).replace("$", "")
    checkval = ((checkval).replace("\'", ""))
    # print(checkval)
    checkvalexists = False
    # if isinstance(checkval, str) and len(checkval) > 0 and (checkval.find("Other") == -1 and checkval != "USPS"):
    if isinstance(checkval, str) and len(checkval) > 0 and checkval.find("Buy Shipping") != -1:
        checkvalexists = True
        # print(checkval)

    match casefieldname:
        case "Shipment_XITOR_KEY":
            fieldnameresult = ""

        case "SHIP_HAS_DATA_ISSUE":
            fieldnameresult = ""

        case "SHIP_DATA_ISSUE_NOTES":
            fieldnameresult = ""

        case "SHIP_ACCOUNTING__ADDNL_DATA_VA":
            fieldnameresult = ""

        case "SHIP_WATCH_LIST":
            fieldnameresult = ""

        case "SHIP_GEN_SERVICE":
            if checkvalexists:
                fieldnameresult = "Veeqo"

        case "SHIP_GEN_CREATE_DATE":
            if checkvalexists:
                # print("0: " + str(newfilerow))
                tempval = newfilerow[getsourcefilekeybyvalue("Shipped Date")[1] - 1]
                tempval = ((tempval).replace("\'", ""))
                tempval = ((tempval).replace("[", ""))
                # print("1: " + str(tempval))
                tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
                fieldnameresult = tempdate.strftime("%m/%d/%Y")
                # print(str(fieldnameresult))

        case "SHIP_GEN_CARRIER":
            if checkvalexists:

                tempval = newfilerow[getsourcefilekeybyvalue("Carrier")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier(tempval)

        case "SHIP_GEN_CRR_SRV_DD":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier_dd(tempval)

        case "SHIP_GEN_OWN_COMP":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Store")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
                # print(tempval)
        case "SHIP_GEN_CHANNEL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Store")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_channel(tempval)
        case "SHIP_RATE_SHIP_CHRG":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Total Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__BASE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Total Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__ORIGINAL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Total Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_PKG_FULL_DIMS":
            if checkvalexists:
                tempval_length = newfilerow[getsourcefilekeybyvalue("Length")[1] - 1]
                tempval_width = newfilerow[getsourcefilekeybyvalue("Width")[1] - 1]
                tempval_height = newfilerow[getsourcefilekeybyvalue("Height")[1] - 1]
                tempval_length = round(float(tempval_length.replace("\'", "")), 0)
                tempval_width = round(float(tempval_width.replace("\'", "")), 0)
                tempval_height = round(float(tempval_height.replace("\'", "")), 0)
                tempval_final = str(int(round(tempval_length, 0))) + "x" + str(int(round(tempval_width, 0))) + "x" + \
                    str(int(round(tempval_height, 0)))
                fieldnameresult = tempval_final
                # print(fieldnameresult)
        case "SHIP_GEN_PKG_LENGTH":
            if checkvalexists:
                tempval_length = newfilerow[getsourcefilekeybyvalue("Length")[1] - 1]
                fieldnameresult = tempval_length
        case "SHIP_GEN_PKG_WIDTH":
            if checkvalexists:
                tempval_width = newfilerow[getsourcefilekeybyvalue("Width")[1] - 1]
                fieldnameresult = tempval_width
        case "SHIP_GEN_PKG_HEIGHT":
            if checkvalexists:
                tempval_height = newfilerow[getsourcefilekeybyvalue("Height")[1] - 1]
                fieldnameresult = tempval_height
        case "SHIP_GEN_PKG_WEIGHT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]
                tempval = float(tempval.replace("\'", ""))
                fieldnameresult = str(round(float(tempval), 4))
        case "SHIP_PKG_WEIGHT_OUNCES":
            # Veeqo package weight is given in ounces
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]

                tempval = ((tempval).replace("\'", ""))
                if len(tempval) > 0:
                    tempval = float(tempval.replace("\'", ""))
                    fieldnameresult = str(round(float(tempval), 4))
                else:
                    fieldnameresult = ""
        case "SHIP_PKG_WEIGHT_TEXT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]
                tempval = float((tempval).replace("\'", ""))
                tempvalstr = ""
                if float(tempval) > 16:
                    tempvalstr = str(math.floor(float(tempval)/16)) + " lbs " + str(
                        round(math.floor(float(tempval % 16)))) + " oz"
                else:
                    tempvalstr = str(round(float(tempval), 4)) + " oz"
                # print(tempvalstr)
                fieldnameresult = tempvalstr
        case "SHIP_GEN_ORDER_ID":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue("Order ID")[1] - 1]
            tempsrcstore = newfilerow[getsourcefilekeybyvalue("Store")[1] - 1]

            # Veeqo pulls in Sales Record for Ebay orders, skip main Order ID for these (goes in Secondary ID)
            if tempsrcstore.find("Abes") != -1 or tempsrcstore.find("Ebay") != -1:
                fieldnameresult = ""
            else:
                fieldnameresult = str(getsourcefilekeybyvalue("Order ID")[5]) + tempval
            # print("Store:" + fieldnameresult)
        case "SHIP_GEN_ORDER_ID_2":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue("Order ID")[1] - 1]
            tempsrcstore = newfilerow[getsourcefilekeybyvalue("Store")[1] - 1]

            # Veeqo pulls in Sales Record for Ebay orders, skip main Order ID for these (goes in Secondary ID)
            if tempsrcstore.find("Abes") != -1 or tempsrcstore.find("Ebay") != -1:
                fieldnameresult = str(getsourcefilekeybyvalue("Order ID")[5]) + tempval
            else:
                fieldnameresult = ""
        case "SHIP_GEN_TRACK_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Tracking ID")[1] - 1]
                fieldnameresult = str(getsourcefilekeybyvalue("Order ID")[5]) + tempval
        case "SHIP_GEN_TO_STATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Ship To State")[1] - 1]
                tempval = (tempval).replace("\'", "")
                fieldnameresult = GenFieldKey_CIQ1.get_to_state(tempval)
        case "SHIP_GEN_FULL_NAME__SHIP_TO":
            if checkvalexists:
                # tempval_firstname = newfilerow[getsourcefilekeybyvalue("Ship To FirstName")[1] - 1]
                # tempval_lastname = newfilerow[getsourcefilekeybyvalue("Ship To LastName")[1] - 1]
                # fieldnameresult = tempval_firstname + " " + tempval_lastname
                fieldnameresult = ""
        case "SHIP_INCOMINGOUTGOING":
            if checkvalexists:
                fieldnameresult = "Outgoing"
        case "SHIP_DELIVERY_STATUS":
            if checkvalexists:
                fieldnameresult = "New"
        case "SHIP_SECONDARY_TRACKING_NUMBER":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP_SYSTEM_CREATED_DATE":
            current_date = datetime.now()
            date_string = current_date.strftime("%m/%d/%Y")
            fieldnameresult = date_string
        case "SHIP_SYSTEM_UPDATED_DATE":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__COMBINED_SHIPMENT":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__DATA_SOURCE__VEEQO":
            fieldnameresult = "Yes"
        case "SHIP__IS_PHASE_2_RECORD":
            fieldnameresult = "YES"
        case _:
            print("Calc'd field not found for Switch statement: " + str(casefieldname))



    return fieldnameresult


def gettranslatedfieldvalues(casefieldname, newfilerow):
    # print("run")
    fieldnameresult = ""

    match casefieldname:
        case "Shipped Date":
            tempval = newfilerow[getsourcefilekeybyvalue("Shipped Date")[1] - 1]
            tempval = ((tempval).replace("\'", ""))
            tempval = ((tempval).replace("[", ""))
            # print(str(tempval))
            tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # print(str(fieldnameresult))
        case _:
            print("Transl'd field not found for Switch statement: " + str(casefieldname))

    return fieldnameresult


def setrandomrunid():

    runid = random.randint(0, 99999999)
    runidstr = "SHP_IMP-" + str(runid)
    global RANDOM_RUN_ID
    RANDOM_RUN_ID = runidstr
    print(RANDOM_RUN_ID)


def getrandomrunid():

    return RANDOM_RUN_ID


def getoutputfile_add():
    runidstr = RANDOM_RUN_ID
    print(runidstr)
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-ADD-" + date_string + "--" + str(1) + "--" + runidstr +\
                  ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-ADD-" + date_string + "--" + str(counter1) + \
                              "--" + runidstr + ".csv"
                #print(output_file)
            else:
                getnextfilename = False
            counter1 = counter1 + 1
    script_dir = os.path.dirname(__file__)
    reloutputfile = "_RESULTS\\" + output_file
    outputfile = os.path.join(script_dir, reloutputfile)
    return outputfile


def getoutputfile_update():
    runidstr = RANDOM_RUN_ID
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-UPDATE-" + date_string + "--" + str(1) + "--" + runidstr + \
                  ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-UPDATE-" + date_string + "--" + \
                              str(counter1) + "--" + runidstr + ".csv"
                #print(output_file)
            else:
                getnextfilename = False
            counter1 = counter1 + 1
    script_dir = os.path.dirname(__file__)
    reloutputfile = "_RESULTS\\" + output_file
    outputfile = os.path.join(script_dir, reloutputfile)
    return outputfile


def getoutputfile_err():
    runidstr = RANDOM_RUN_ID
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-ERRORS-" + date_string + "--" + str(1) + "--" + \
                  runidstr + ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-ERRORS-" + date_string + "--" + \
                              str(counter1) + "--" + runidstr + ".csv"
                #print(output_file)
            else:
                getnextfilename = False
            counter1 = counter1 + 1
    script_dir = os.path.dirname(__file__)
    reloutputfile = "_RESULTS\\" + output_file
    outputfile = os.path.join(script_dir, reloutputfile)
    return outputfile


def getoutputfile_test1():
    runidstr = RANDOM_RUN_ID
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-TEST1-" + date_string + "--" + str(1) + "--" + runidstr \
                  + ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-" + OUTPUT_FILE_KEYWORD_1 + "-TEST1-" + date_string + "--" + str(counter1) \
                              + "--" + runidstr + ".csv"
                #print(output_file)
            else:
                getnextfilename = False
            counter1 = counter1 + 1
    script_dir = os.path.dirname(__file__)
    reloutputfile = "_RESULTS\\" + output_file
    outputfile = os.path.join(script_dir, reloutputfile)
    return outputfile


def getsourceidrefforlookup():

    return SOURCE_ID_REF_FOR_LOOKUP


def getmainxitorlookuptype():

    return MAIN_XITOR_LOOKUP_TYPE


def sourcefilekey_processing(filerow):

    return [filerow]


# dictionary of all functions in this file, to pass to main files for use
functionkey1 = {
    "getsourcefilekey": [getsourcefilekey],
    "getsourcefilekeylength": [getsourcefilekeylength],
    "getsourcefilekeybaselength": [getsourcefilekeybaselength],
    "getsourcefilekeybyvalue": [getsourcefilekeybyvalue],
    "getcolplacement_xitor": [getcolplacement_xitor],
    "getcolplacement_tracknum": [getcolplacement_tracknum],
    "getcolplacement_combinedflag": [getcolplacement_combinedflag],
    "getcalcfieldvalues": [getcalcfieldvalues],
    "gettranslatedfieldvalues": [gettranslatedfieldvalues],
    "getoutputfile_add": [getoutputfile_add],
    "getoutputfile_update": [getoutputfile_update],
    "getoutputfile_err": [getoutputfile_err],
    "getoutputfile_test1": [getoutputfile_test1],
    "getsourceidrefforlookup": [getsourceidrefforlookup],
    "sourcefilekey_processing": [sourcefilekey_processing],
    "setrandomrunid": [setrandomrunid],
    "getmainxitorlookuptype": [getmainxitorlookuptype]


}

# dictionary of all functions to perform on file rows, to pass to main files/Helpers for use
functionkey_processing = {
    # "processfileheaderrow": [processfileheaderrow],
    # "translatefileheaderrow1": [translatefileheaderrow1],
    # "translatefileheaderrow2": [translatefileheaderrow2],
    # "processfilenextrow": [processfilenextrow],
    # "processcalculatedrows": [processcalculatedrows],
    # "processtranslatedrows": [processtranslatedrows],
    # "finalerrorcheck": [finalerrorcheck],
    # "pushfinalerrormessage": [pushfinalerrormessage],
    # "ciqidlookupadd": [ciqidlookupadd],
    # "ciqsearchlookupfile": [ciqsearchlookupfile],
    # "buildcombinedshipmentslist": [buildcombinedshipmentslist],
    # "markcombinedshipments": [markcombinedshipments],
    # "sourcefilekey_processing": [sourcefilekey_processing],
    # "general_post_processing": [general_post_processing]
    "processfileheaderrow": True,
    "translatefileheaderrow1": True,
    "translatefileheaderrow2": True,
    "processfilenextrow": True,
    "processcalculatedrows": True,
    "processtranslatedrows": True,
    "finalerrorcheck": True,
    "pushfinalerrormessage": True,
    "ciqidlookupadd": True,
    "ciqsearchlookupfile": True,
    "buildcombinedshipmentslist": True,
    "markcombinedshipments": True,
    "sourcefilekey_processing": True,
    "general_post_processing": True,
    "write_row_list_to_files": True,
    "filecleanup": True


}
