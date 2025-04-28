import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import csv
import random

# SOURCE_ID_REF_FOR_LOOKUP = "Order ID"
SOURCE_ID_REF_FOR_LOOKUP = "Tracking ID"
RANDOM_RUN_ID = "-1"
OUTPUT_FILE_KEYWORD_1 = "Ebay-Shipping"
MAIN_XITOR_LOOKUP_TYPE = "_Shipment_"
global EBAY_SOURCE

def getfunctionkey():

    return functionkey1


def getfunctionkey_processing():

    return functionkey_processing


sourcefilekey1 = {
    "Shipment_XITOR_KEY": [None, 1, 1, "Shipment_XITOR_KEY", "Shipment_XITOR_KEY", ""],
    "SHIP_GEN_SERVICE": [None, 2, 1, "SHIP_GEN_SERVICE", "SHIP_GEN_SERVICE", ""],
    "SHIP_GEN_CREATE_DATE": [None, 3, 1, "SHIP_GEN_CREATE_DATE", "SHIP_GEN_CREATE_DATE", ""],
    "SHIP_GEN_CARRIER": [None, 4, 1, "SHIP_GEN_CARRIER", "SHIP_GEN_CARRIER", ""],
    "SHIP_GEN_CRR_SRV_DD": [None, 5, 1, "SHIP_GEN_CRR_SRV_DD", "SHIP_GEN_CRR_SRV_DD", ""],
    "SHIP_GEN_OWN_COMP": [None, 6, 1, "SHIP_GEN_OWN_COMP", "SHIP_GEN_OWN_COMP", ""],
    "SHIP_GEN_CHANNEL": [None, 7, 1, "SHIP_GEN_CHANNEL", "SHIP_GEN_CHANNEL", ""],
    "SHIP_RATE_SHIP_CHRG": [None, 8, 1, "SHIP_RATE_SHIP_CHRG", "SHIP_RATE_SHIP_CHRG", ""],
    "SHIP_RATESHIP_CHARGE__BASE": [None, 9, 1, "SHIP_RATESHIP_CHARGE__BASE", "SHIP_RATESHIP_CHARGE__BASE", ""],
    "SHIP_RATESHIP_CHARGE__ORIGINAL": [None, 10, 1, "SHIP_RATESHIP_CHARGE__ORIGINAL", "SHIP_RATESHIP_CHARGE__ORIGINAL",
                                       ""],
    "SHIP_GEN_ORDER_ID": [None, 11, 1, "SHIP_GEN_ORDER_ID", "SHIP_GEN_ORDER_ID", ""],
    "SHIP_GEN_ORDER_ID_2": [None, 12, 1, "SHIP_GEN_ORDER_ID_2", "SHIP_GEN_ORDER_ID_2", ""],
    "SHIP_GEN_TRACK_NUM": [None, 13, 1, "SHIP_GEN_TRACK_NUM", "SHIP_GEN_TRACK_NUM", ""],
    "SHIP_GEN_FULL_NAME__SHIP_TO": [None, 14, 1, "SHIP_GEN_FULL_NAME__SHIP_TO", "SHIP_GEN_FULL_NAME__SHIP_TO", ""],
    "SHIP_INCOMINGOUTGOING": [None, 15, 1, "SHIP_INCOMINGOUTGOING", "SHIP_INCOMINGOUTGOING", ""],
    "SHIP_DELIVERY_STATUS": [None, 16, 1, "SHIP_DELIVERY_STATUS", "SHIP_DELIVERY_STATUS", ""],
    "SHIP__EBAY_SHIPPING__SHIPPED_D": [None, 17, 1, "SHIP__EBAY_SHIPPING__SHIPPED_D", "SHIP__EBAY_SHIPPING__SHIPPED_D",
                                       ""],
    "SHIP__IS_PHASE_2_RECORD": [None, 18, 1, "SHIP__IS_PHASE_2_RECORD", "SHIP__IS_PHASE_2_RECORD", ""],
    "SHIP_SYSTEM_CREATED_DATE": [None, 19, 1, "SHIP_SYSTEM_CREATED_DATE", "SHIP_SYSTEM_CREATED_DATE", ""],
    "SHIP_SYSTEM_UPDATED_DATE": [None, 20, 1, "SHIP_SYSTEM_UPDATED_DATE", "SHIP_SYSTEM_UPDATED_DATE", ""],
    "SHIP__DATA_SOURCE__EBAYSHIPPIN": [None, 21, 1, "SHIP__DATA_SOURCE__EBAYSHIPPIN", "SHIP__DATA_SOURCE__EBAYSHIPPIN",
                                       ""],
    "Actions": [1, 22, 0, "Actions", "", ""],
    "Description": [2, 23, 0, "Description", "", ""],
    "Date Time": [3, 24, 0, "Date Time", "", ""],
    "Order Number": [4, 25, 0, "Order Number", "", ""],
    "Username": [5, 26, 0, "Username", "", ""],
    "Ship Service": [6, 27, 0, "Ship Service", "", ""],
    "Status": [7, 28, 0, "Status", "", ""],
    "blank1": [8, 29, 0, "blank1", "", ""],
    "blank2": [9, 30, 0, "blank2", "", ""],
    "blank3": [10, 31, 0, "blank3", "", ""],
    "blank4": [11, 32, 0, "blank4", "", ""],
    "Ship To Name": [12, 33, 0, "Ship To Name", "", ""],
    "Label Cost": [13, 34, 0, "Label Cost", "", ""],
    "Tracking Number": [14, 35, 0, "Tracking Number", "", "@@@"],

}

sourcefilekey_shipping = {
    "Shipment_XITOR_KEY": [None, 1, 1, "Shipment_XITOR_KEY", "Shipment_XITOR_KEY", ""],
    "SHIP_GEN_SERVICE": [None, 2, 1, "SHIP_GEN_SERVICE", "SHIP_GEN_SERVICE", ""],
    "SHIP_GEN_CREATE_DATE": [None, 3, 1, "SHIP_GEN_CREATE_DATE", "SHIP_GEN_CREATE_DATE", ""],
    "SHIP_GEN_CARRIER": [None, 4, 1, "SHIP_GEN_CARRIER", "SHIP_GEN_CARRIER", ""],
    "SHIP_GEN_CRR_SRV_DD": [None, 5, 1, "SHIP_GEN_CRR_SRV_DD", "SHIP_GEN_CRR_SRV_DD", ""],
    "SHIP_GEN_OWN_COMP": [None, 6, 1, "SHIP_GEN_OWN_COMP", "SHIP_GEN_OWN_COMP", ""],
    "SHIP_GEN_CHANNEL": [None, 7, 1, "SHIP_GEN_CHANNEL", "SHIP_GEN_CHANNEL", ""],
    "SHIP_RATE_SHIP_CHRG": [None, 8, 1, "SHIP_RATE_SHIP_CHRG", "SHIP_RATE_SHIP_CHRG", ""],
    "SHIP_RATESHIP_CHARGE__BASE": [None, 9, 1, "SHIP_RATESHIP_CHARGE__BASE", "SHIP_RATESHIP_CHARGE__BASE", ""],
    "SHIP_RATESHIP_CHARGE__ORIGINAL": [None, 10, 1, "SHIP_RATESHIP_CHARGE__ORIGINAL", "SHIP_RATESHIP_CHARGE__ORIGINAL",
                                       ""],
    "SHIP_GEN_ORDER_ID": [None, 11, 1, "SHIP_GEN_ORDER_ID", "SHIP_GEN_ORDER_ID", ""],
    "SHIP_GEN_ORDER_ID_2": [None, 12, 1, "SHIP_GEN_ORDER_ID_2", "SHIP_GEN_ORDER_ID_2", ""],
    "SHIP_GEN_TRACK_NUM": [None, 13, 1, "SHIP_GEN_TRACK_NUM", "SHIP_GEN_TRACK_NUM", ""],
    "SHIP_GEN_FULL_NAME__SHIP_TO": [None, 14, 1, "SHIP_GEN_FULL_NAME__SHIP_TO", "SHIP_GEN_FULL_NAME__SHIP_TO", ""],
    "SHIP_INCOMINGOUTGOING": [None, 15, 1, "SHIP_INCOMINGOUTGOING", "SHIP_INCOMINGOUTGOING", ""],
    "SHIP_DELIVERY_STATUS": [None, 16, 1, "SHIP_DELIVERY_STATUS", "SHIP_DELIVERY_STATUS", ""],
    "SHIP__EBAY_SHIPPING__SHIPPED_D": [None, 17, 1, "SHIP__EBAY_SHIPPING__SHIPPED_D", "SHIP__EBAY_SHIPPING__SHIPPED_D",
                                       ""],
    "SHIP__IS_PHASE_2_RECORD": [None, 18, 1, "SHIP__IS_PHASE_2_RECORD", "SHIP__IS_PHASE_2_RECORD", ""],
    "SHIP_SYSTEM_CREATED_DATE": [None, 19, 1, "SHIP_SYSTEM_CREATED_DATE", "SHIP_SYSTEM_CREATED_DATE", ""],
    "SHIP_SYSTEM_UPDATED_DATE": [None, 20, 1, "SHIP_SYSTEM_UPDATED_DATE", "SHIP_SYSTEM_UPDATED_DATE", ""],
    "SHIP__DATA_SOURCE__EBAYSHIPPIN": [None, 21, 1, "SHIP__DATA_SOURCE__EBAYSHIPPIN", "SHIP__DATA_SOURCE__EBAYSHIPPIN",
                                       ""],
    "Actions": [1, 22, 0, "Actions", "", ""],
    "Description": [2, 23, 0, "Description", "", ""],
    "Date Time": [3, 24, 0, "Date Time", "", ""],
    "Order Number": [4, 25, 0, "Order Number", "", ""],
    "Username": [5, 26, 0, "Username", "", ""],
    "Ship Service": [6, 27, 0, "Ship Service", "", ""],
    "Status": [7, 28, 0, "Status", "", ""],
    "blank1": [8, 29, 0, "blank1", "", ""],
    "blank2": [9, 30, 0, "blank2", "", ""],
    "blank3": [10, 31, 0, "blank3", "", ""],
    "blank4": [11, 32, 0, "blank4", "", ""],
    "Ship To Name": [12, 33, 0, "Ship To Name", "", ""],
    "Label Cost": [13, 34, 0, "Label Cost", "", ""],
    "Tracking Number": [14, 35, 0, "Tracking Number", "", "@@@"],

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
    retkey = sourcefilekey1["Tracking Number"][1]
    return retkey


def getcolplacement_combinedflag():
    retkey = sourcefilekey1["SHIP__COMBINED_SHIPMENT"][1]
    return retkey


def getcalcfieldvalues_shipping(casefieldname, newfilerow):

    fieldnameresult = ""

    #print(newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1])
    # checkval = newfilerow[getsourcefilekeybyvalue("Tracking ID")[1]-1]
    # checkval = newfilerow[getsourcefilekeybyvalue_shipping("Carrier")[1] - 1]
    # checkval = str(checkval).replace("$", "")
    # checkval = ((checkval).replace("\'", ""))
    # print(checkval)
    checkvalexists = True
    # if isinstance(checkval, str) and len(checkval) > 0 and checkval.find("Other") == -1:
    #     checkvalexists = True
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
                fieldnameresult = "Ebay"

        case "SHIP_GEN_CREATE_DATE":
            if checkvalexists:
                # print("0: " + str(newfilerow))
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Date Time")[1] - 1]
                tempval = ((tempval).replace("\'", ""))
                tempval = ((tempval).replace("[", ""))
                # print("1: " + str(tempval))
                tempdate = datetime.strptime(tempval, "%b %d|| %Y %I:%M%p")
                fieldnameresult = tempdate.strftime("%m/%d/%Y")
                # print(str(fieldnameresult))
        case "SHIP__EBAY_SHIPPING__SHIPPED_D":
            if checkvalexists:
                # print("0: " + str(newfilerow))
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Date Time")[1] - 1]
                tempval = ((tempval).replace("\'", ""))
                tempval = ((tempval).replace("[", ""))
                # print("1: " + str(tempval))
                tempdate = datetime.strptime(tempval, "%b %d|| %Y %I:%M%p")
                fieldnameresult = tempdate.strftime("%m/%d/%Y")
                # print(str(fieldnameresult))
        case "SHIP_GEN_CARRIER":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Ship Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier(tempval)

        case "SHIP_GEN_CRR_SRV_DD":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Ship Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier_dd(tempval)

        case "SHIP_GEN_OWN_COMP":
            if checkvalexists:
                if EBAY_SOURCE == "ABES":
                    tempval = "AbesBargains"
                    fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
                elif EBAY_SOURCE == "DDS":
                    tempval = "Digicati"
                    fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
                else:
                    fieldnameresult = ""
                # fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
        case "SHIP_GEN_CHANNEL":
            if checkvalexists:
                if EBAY_SOURCE == "ABES":
                    tempval = "AbesBargains"
                    fieldnameresult = GenFieldKey_CIQ1.get_gen_channel(tempval)
                elif EBAY_SOURCE == "DDS":
                    tempval = "Digicati"
                    fieldnameresult = GenFieldKey_CIQ1.get_gen_channel(tempval)
                else:
                    fieldnameresult = ""
        case "SHIP_RATE_SHIP_CHRG":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__BASE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__ORIGINAL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Label Cost")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_PKG_FULL_DIMS":
            if checkvalexists:
                tempval_length = newfilerow[getsourcefilekeybyvalue("Length")[1] - 1]
                tempval_width = newfilerow[getsourcefilekeybyvalue("Width")[1] - 1]
                tempval_height = newfilerow[getsourcefilekeybyvalue("Height")[1] - 1]
                tempval_final = str(tempval_length) + "x" + str(tempval_width) + "x" + str(tempval_height)
                fieldnameresult = tempval_final
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
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]

                tempval = ((tempval).replace("\'", ""))
                if len(tempval) > 0:
                    tempval = float(tempval.replace("\'", ""))
                    fieldnameresult = str(round(float(tempval) * 16, 4))
                else:
                    fieldnameresult = ""
        case "SHIP_PKG_WEIGHT_TEXT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]
                tempval = float((tempval).replace("\'", ""))
                tempvalstr = ""
                if float(tempval) > 1:
                    tempvalstr = str(math.floor(float(tempval))) + " lbs " + str(
                        round((float(tempval) - math.floor(float(tempval))) * 16, 4)) + " oz"
                else:
                    tempvalstr = str(round(float(tempval) * 16, 4)) + " oz"
                fieldnameresult = tempvalstr
        case "SHIP_GEN_ORDER_ID":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue_shipping("Order Number")[1] - 1]
            fieldnameresult = str(getsourcefilekeybyvalue_shipping("Order Number")[5]) + tempval
        case "SHIP_GEN_TRACK_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Tracking Number")[1] - 1]
                # fieldnameresult = str(getsourcefilekeybyvalue_shipping("Tracking Number")[5]) + tempval
                fieldnameresult = tempval
        case "SHIP_GEN_TO_STATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Ship To State")[1] - 1]
                tempval = (tempval).replace("\'", "")
                fieldnameresult = GenFieldKey_CIQ1.get_to_state(tempval)
        case "SHIP_GEN_FULL_NAME__SHIP_TO":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue_shipping("Ship To Name")[1] - 1]
                # tempval_firstname = newfilerow[getsourcefilekeybyvalue("Ship To FirstName")[1] - 1]
                # tempval_lastname = newfilerow[getsourcefilekeybyvalue("Ship To LastName")[1] - 1]
                # fieldnameresult = tempval_firstname + " " + tempval_lastname
                fieldnameresult = tempval.capitalize()
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
        case "SHIP__COMBINED_SHIPMENT":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__DATA_SOURCE__EBAYSHIPPIN":
            fieldnameresult = "YES"
        case "SHIP__IS_PHASE_2_RECORD":
            fieldnameresult = "YES"
        case _:
            print("Calc'd field not found for Switch statement: " + str(casefieldname))



    return fieldnameresult


def gettranslatedfieldvalues(casefieldname, newfilerow):

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


def getoutputfile_shipping():
    runidstr = RANDOM_RUN_ID
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-Ebay-Shipping-" + OUTPUT_FILE_KEYWORD_1 + "-" + date_string + "--" + str(1) + "--" + \
                  runidstr + ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-Ebay-Shipping-" + OUTPUT_FILE_KEYWORD_1 + "-" + date_string + "--" + \
                              str(counter1) + "--" + runidstr + ".csv"
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


def getsourcefilekey_shipping():
    return sourcefilekey_shipping


def getsourcefilekeylength_shipping():
    return len(sourcefilekey_shipping)


#length of key base report rows only, no calculated rows
def getsourcefilekeybaselength_shipping():

    tempcount = 0
    for temprow in sourcefilekey_shipping:
        # print(sourcefilekey1[temprow][2])
        if sourcefilekey_shipping[temprow][2] == 1:
            tempcount += tempcount

    return tempcount


def getsourcefilekeybyvalue_shipping(val1):
    retkey = sourcefilekey_shipping[val1]
    return retkey

def process_ebay_shipping_file(filenamestr):

    script_dir = os.path.dirname(__file__)
    reloutputfile = "_INPUT\\" + filenamestr
    inputfile = os.path.join(script_dir, reloutputfile)

    fullinputrowlist = [[]]

    with open(inputfile) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='\"')

        for temprow in dcreader2:
            # print(temprow)
            # fullinputrowlist.append(temprow)

            mainrow = temprow
            subrow = next(dcreader2)

            for tempsubitem in subrow:
                mainrow.append(tempsubitem)
            fullinputrowlist.append(mainrow)

    outputfile_shipping = getoutputfile_shipping()
    f_ship = open(outputfile_shipping, "w")


    filerow = []
    newheaderrow = translatefileheaderrow1(filerow, sourcefilekey_shipping)
    print(newheaderrow)
    write_file_row(newheaderrow, f_ship)

    fullinputrowlist.pop(0)
    for outputrow in fullinputrowlist:
        newoutputrow = processfilenextrow(outputrow, sourcefilekey_shipping, getsourcefilekeylength_shipping(), "")
        print(newoutputrow)
        print("---")
        write_file_row(newoutputrow, f_ship)


def process_ebay_shipping_file2(curfilename, encoding1, newline1):

    fullinputrowlist = [[]]

    # fullinputrowlist = filerowlist
    global EBAY_SOURCE

    if str(curfilename).find("DDS") != -1:

        EBAY_SOURCE = "DDS"
    elif str(curfilename).find("ABES") != -1:
        # global EBAY_SOURCE
        EBAY_SOURCE = "ABES"
    else:
        # global EBAY_SOURCE
        EBAY_SOURCE = "UNKNOWN"

    with open(curfilename, encoding=encoding1, newline=newline1) as csvfile:
        dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='\"')

        for temprow in dcreader2:
            # print(temprow)
            # fullinputrowlist.append(temprow)

            mainrow = temprow
            subrow = next(dcreader2)

            for tempsubitem in subrow:
                mainrow.append(tempsubitem)
            fullinputrowlist.append(mainrow)

    outputfile_shipping = getoutputfile_shipping()
    print("---")
    print("Output File Shipping: " + outputfile_shipping)
    print("---")
    f_ship = open(outputfile_shipping, "w")


    filerow = []
    newheaderrow = translatefileheaderrow1(filerow, sourcefilekey_shipping)
    print("Final Header Row:" + str(newheaderrow))
    write_file_row(newheaderrow, f_ship)

    fullinputrowlist.pop(0)
    # print("fullinputrowlist:" + str(fullinputrowlist))
    for outputrow in fullinputrowlist:
        newoutputrow = processfilenextrow(outputrow, sourcefilekey_shipping, getsourcefilekeylength_shipping(), "")
        print("Final Filerow:" + str(newoutputrow))
        print("---")
        write_file_row(newoutputrow, f_ship)



def processfilenextrow(filerow, keyfile, keyfilelength, curfile):

    # print("filerow:" + str(filerow))
    # print("keyfile:" + str(keyfile))
    newfilerow = createemptylist(keyfilelength)
    count = 1

    for temprow in filerow:
        temprow = str(temprow).replace(chr(9), "")
        temprow = str(temprow).replace(chr(10), "")
        temprow = str(temprow).replace(",", "||")

        for tempkey in keyfile:
            # print(keyfile[tempkey])
            if keyfile[tempkey][0] is not None:
                if count == int(keyfile[tempkey][0]):
                    temprow = temprow.strip()
                    temprow = str(keyfile[tempkey][5]) + temprow
                    newfilerow.insert(int(keyfile[tempkey][1]) - 1, temprow)
                    newfilerow.pop(int(keyfile[tempkey][1]))
        count += 1

    newfilerow = processcalculatedrows(newfilerow, keyfile, keyfilelength, curfile)
    # newfilerow = processtranslatedrows(newfilerow, keyfile, keyfilelength, curfile)

    # print("newfilerow2: " + str(newfilerow))

    return newfilerow


# new values for import, derived from values in other columns
def processcalculatedrows(filerow, keyfile, keyfilelength, curfile):
    count = 1
    newfilerow = filerow
    # print(filerow)

    for tempkey in keyfile:
        if keyfile[tempkey][0] is None:
            # print("keyfile[tempkey][3]:" + str(keyfile[tempkey][3]))

            fieldname1 = keyfile[tempkey][3]
            newval1 = getcalcfieldvalues_shipping(fieldname1, newfilerow)

            newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval1)
            newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    return newfilerow


def translatefileheaderrow1(filerow, keyfile):

    newfilerow = filerow

    for tempkey in keyfile:

        newval = keyfile[tempkey][4]
        newfilerow.append(newval)

    # print("newfilerow1: " + str(newfilerow))

    # newfilerow = translatefileheaderrow2(newfilerow, keyfile)

    return newfilerow


#for calc'd field headers
def translatefileheaderrow2(filerow, keyfile):

    count = 1
    newfilerow = filerow

    for tempkey in keyfile:
        if keyfile[tempkey][0] is None:
            # print(keyfile[tempkey][3])

            newval = keyfile[tempkey][4]

            newfilerow.insert(int(keyfile[tempkey][1]) - 1, newval)
            # print(int(keyfile[tempkey][1]))
            newfilerow.pop(int(keyfile[tempkey][1]))

        count += 1

    # print("newfilerow2: " + str(newfilerow))

    return newfilerow

def write_file_row(filerow, fwriter):
    temprowstr = str(filerow)
    # print(temprowstr)
    temprowstr = str(temprowstr).replace("\'", "")
    temprowstr = str(temprowstr).replace("||", "")
    temprowstr = str(temprowstr).replace("\"", "")
    temprowstr = str(temprowstr).replace("[", "")
    temprowstr = str(temprowstr).replace("]", "")
    temprowstr = str(temprowstr).replace("$", "")
    temprowstr = str(temprowstr).replace(", ", ",")
    temprowstr = str(temprowstr).strip()

    fwriter.write(str(temprowstr) + "\n")

    return True


#takes in entire list of filerows
def sourcefilekey_processing(filerowlist):

    process_ebay_shipping_file2(filerowlist)


#takes in entire list of filerows
def specialfunctions1(curfilename, encoding1, newline1):

    process_ebay_shipping_file2(curfilename, encoding1, newline1)


def getmainxitorlookuptype():

    return MAIN_XITOR_LOOKUP_TYPE


def createemptylist(listlength):
    newlist = []
    count = 0
    while count < listlength:
        newlist.insert(0, str(count))
        count += 1
    #print(newlist)
    return newlist


# dictionary of all functions in this file, to pass to main files for use
functionkey1 = {
    "getsourcefilekey": [getsourcefilekey],
    "getsourcefilekeylength": [getsourcefilekeylength],
    "getsourcefilekeybaselength": [getsourcefilekeybaselength],
    "getsourcefilekeybyvalue": [getsourcefilekeybyvalue],
    "getcolplacement_xitor": [getcolplacement_xitor],
    "getcolplacement_tracknum": [getcolplacement_tracknum],
    "getcolplacement_combinedflag": [getcolplacement_combinedflag],
    # "getcalcfieldvalues": [getcalcfieldvalues],
    "gettranslatedfieldvalues": [gettranslatedfieldvalues],
    "getoutputfile_add": [getoutputfile_add],
    "getoutputfile_update": [getoutputfile_update],
    "getoutputfile_err": [getoutputfile_err],
    "getoutputfile_test1": [getoutputfile_test1],
    "getsourceidrefforlookup": [getsourceidrefforlookup],
    "sourcefilekey_processing": [sourcefilekey_processing],
    "setrandomrunid": [setrandomrunid],
    "specialfunctions1": [specialfunctions1],
    "getmainxitorlookuptype": [getmainxitorlookuptype]
    # "sourcefilekey_processing_string": [sourcefilekey_processing_string],
    # "preprocessfilerow": [preprocessfilerow]
}


# dictionary of all functions to perform on file rows, to pass to main files/Helpers for use
functionkey_processing = {

    "specialfunctions1": True,
    "sourcefilekey_processing": False,

}
