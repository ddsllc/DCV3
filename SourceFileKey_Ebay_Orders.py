import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import csv
import random

SOURCE_ID_REF_FOR_LOOKUP = "SHIP_GEN_ORDER_ID"
# SOURCE_ID_REF_FOR_LOOKUP = "Tracking Number"
RANDOM_RUN_ID = "-1"
OUTPUT_FILE_KEYWORD_1 = "Ebay-Orders"
MAIN_XITOR_LOOKUP_TYPE = "_Shipment_"
global EBAY_SOURCE

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
    "SHIP__EBAY_ORDERS__SHIPPED_DAT": [None, 28, 1, "SHIP__EBAY_ORDERS__SHIPPED_DAT", "SHIP__EBAY_ORDERS__SHIPPED_DAT",
                                       ""],
    "SHIP__IS_PHASE_2_RECORD": [None, 29, 1, "SHIP__IS_PHASE_2_RECORD", "SHIP__IS_PHASE_2_RECORD", ""],
    "SHIP_SYSTEM_CREATED_DATE": [None, 30, 1, "SHIP_SYSTEM_CREATED_DATE", "SHIP_SYSTEM_CREATED_DATE", ""],
    "SHIP_SYSTEM_UPDATED_DATE": [None, 31, 1, "SHIP_SYSTEM_UPDATED_DATE", "SHIP_SYSTEM_UPDATED_DATE", ""],
    "SHIP__COMBINED_SHIPMENT": [None, 32, 1, "SHIP__COMBINED_SHIPMENT", "SHIP__COMBINED_SHIPMENT", ""],
    "SHIP__DATA_SOURCE__EBAYORDERS": [None, 33, 1, "SHIP__DATA_SOURCE__EBAYORDERS", "SHIP__DATA_SOURCE__EBAYORDERS",
                                      ""],
    "Sales Record Number": [1, 34, 0, "Sales Record Number", "", "||"],
    "Order Number": [2, 35, 0, "Order Number", "", ""],
    "Buyer Username": [3, 36, 0, "Buyer Username", "", ""],
    "Buyer Name": [4, 37, 0, "Buyer Name", "", ""],
    "Buyer Email": [5, 38, 0, "Buyer Email", "", ""],
    "Buyer Note": [6, 39, 0, "Buyer Note", "", ""],
    "Buyer Address 1": [7, 40, 0, "Buyer Address 1", "", ""],
    "Buyer Address 2": [8, 41, 0, "Buyer Address 2", "", ""],
    "Buyer City": [9, 42, 0, "Buyer City", "", ""],
    "Buyer State": [10, 43, 0, "Buyer State", "", ""],
    "Buyer Zip": [11, 44, 0, "Buyer Zip", "", "||"],
    "Buyer Country": [12, 45, 0, "Buyer Country", "", ""],
    "Buyer Tax Identifier Name": [13, 46, 0, "Buyer Tax Identifier Name", "", ""],
    "Buyer Tax Identifier Value": [14, 47, 0, "Buyer Tax Identifier Value", "", ""],
    "Ship To Name": [15, 48, 0, "Ship To Name", "", ""],
    "Ship To Phone": [16, 49, 0, "Ship To Phone", "", "||"],
    "Ship To Address 1": [17, 50, 0, "Ship To Address 1", "", ""],
    "Ship To Address 2": [18, 51, 0, "Ship To Address 2", "", ""],
    "Ship To City": [19, 52, 0, "Ship To City", "", ""],
    "Ship To State": [20, 53, 0, "Ship To State", "", ""],
    "Ship To Zip": [21, 54, 0, "Ship To Zip", "", "||"],
    "Ship To Country": [22, 55, 0, "Ship To Country", "", ""],
    "Item Number": [23, 56, 0, "Item Number", "", "||"],
    "Item Title": [24, 57, 0, "Item Title", "", ""],
    "Custom Label": [25, 58, 0, "Custom Label", "", ""],
    "Sold Via Promoted Listings": [26, 59, 0, "Sold Via Promoted Listings", "", ""],
    "Quantity": [27, 60, 0, "Quantity", "", ""],
    "Sold For": [28, 61, 0, "Sold For", "", ""],
    "Shipping And Handling": [29, 62, 0, "Shipping And Handling", "", ""],
    "Item Location": [30, 63, 0, "Item Location", "", ""],
    "Item Zip Code": [31, 64, 0, "Item Zip Code", "", "||"],
    "Item Country": [32, 65, 0, "Item Country", "", ""],
    "eBay Collect And Remit Tax Rate": [33, 66, 0, "eBay Collect And Remit Tax Rate", "", ""],
    "eBay Collect And Remit Tax Type": [34, 67, 0, "eBay Collect And Remit Tax Type", "", ""],
    "eBay Reference Name": [35, 68, 0, "eBay Reference Name", "", ""],
    "eBay Reference Value": [36, 69, 0, "eBay Reference Value", "", ""],
    "Tax Status": [37, 70, 0, "Tax Status", "", ""],
    "Seller Collected Tax": [38, 71, 0, "Seller Collected Tax", "", ""],
    "eBay Collected Tax": [39, 72, 0, "eBay Collected Tax", "", ""],
    "Electronic Waste Recycling Fee": [40, 73, 0, "Electronic Waste Recycling Fee", "", ""],
    "Mattress Recycling Fee": [41, 74, 0, "Mattress Recycling Fee", "", ""],
    "Battery Recycling Fee": [42, 75, 0, "Battery Recycling Fee", "", ""],
    "White Goods Disposal Tax": [43, 76, 0, "White Goods Disposal Tax", "", ""],
    "Tire Recycling Fee": [44, 77, 0, "Tire Recycling Fee", "", ""],
    "Additional Fee": [45, 78, 0, "Additional Fee", "", ""],
    "Lumber Fee": [46, 79, 0, "Lumber Fee", "", ""],
    "Prepaid Wireless Fee": [47, 80, 0, "Prepaid Wireless Fee", "", ""],
    "Road Improvement And Food Delivery Fee": [48, 81, 0, "Road Improvement And Food Delivery Fee", "", ""],
    "eBay Collected Charges": [49, 82, 0, "eBay Collected Charges", "", ""],
    "Total Price": [50, 83, 0, "Total Price", "", ""],
    "eBay Collected Tax and Fees Included in Total": [51, 84, 0, "eBay Collected Tax and Fees Included in Total", "",
                                                      ""],
    "Payment Method": [52, 85, 0, "Payment Method", "", ""],
    "Sale Date": [53, 86, 0, "Sale Date", "", ""],
    "Paid On Date": [54, 87, 0, "Paid On Date", "", ""],
    "Ship By Date": [55, 88, 0, "Ship By Date", "", ""],
    "Minimum Estimated Delivery Date": [56, 89, 0, "Minimum Estimated Delivery Date", "", ""],
    "Maximum Estimated Delivery Date": [57, 90, 0, "Maximum Estimated Delivery Date", "", ""],
    "Shipped On Date": [58, 91, 0, "Shipped On Date", "", ""],
    "Feedback Left": [59, 92, 0, "Feedback Left", "", ""],
    "Feedback Received": [60, 93, 0, "Feedback Received", "", ""],
    "My Item Note": [61, 94, 0, "My Item Note", "", ""],
    "PayPal Transaction ID": [62, 95, 0, "PayPal Transaction ID", "", ""],
    "Shipping Service": [63, 96, 0, "Shipping Service", "", ""],
    "Tracking Number": [64, 97, 0, "Tracking Number", "", ""],
    "Transaction ID": [65, 98, 0, "Transaction ID", "", ""],
    "Variation Details": [66, 99, 0, "Variation Details", "", ""],
    "Global Shipping Program": [67, 100, 0, "Global Shipping Program", "", ""],
    "Global Shipping Reference ID": [68, 101, 0, "Global Shipping Reference ID", "", ""],
    "Click And Collect": [69, 102, 0, "Click And Collect", "", ""],
    "Click And Collect Reference Number": [70, 103, 0, "Click And Collect Reference Number", "", ""],
    "eBay Plus": [71, 104, 0, "eBay Plus", "", ""],
    "Authenticity Verification Program": [72, 105, 0, "Authenticity Verification Program", "", ""],
    "Authenticity Verification Status": [73, 106, 0, "Authenticity Verification Status", "", ""],
    "Authenticity Verification Outcome Reason": [74, 107, 0, "Authenticity Verification Outcome Reason", "", ""],
    "PSA Vault Program": [75, 108, 0, "PSA Vault Program", "", ""],
    "Vault Fulfillment Type": [76, 109, 0, "Vault Fulfillment Type", "", ""],
    "eBay Fulfillment Program": [77, 110, 0, "eBay Fulfillment Program", "", ""],
    "Tax City": [78, 111, 0, "Tax City", "", ""],
    "Tax State": [79, 112, 0, "Tax State", "", ""],
    "Tax Zip": [80, 113, 0, "Tax Zip", "", ""],
    "Tax Country": [81, 114, 0, "Tax Country", "", ""],
    "eBay International Shipping": [82, 115, 0, "eBay International Shipping", "", ""],

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
            tempcount += 1

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


def getcalcfieldvalues(casefieldname, newfilerow):

    fieldnameresult = ""

    # print(newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1])
    # checkval = newfilerow[getsourcefilekeybyvalue("Tracking ID")[1]-1]
    checkval = newfilerow[getsourcefilekeybyvalue("Ship To Name")[1] - 1]
    checkval = str(checkval).replace("$", "")
    checkval = ((checkval).replace("\'", ""))
    # print(checkval)
    # print(newfilerow)
    checkvalexists = False
    if isinstance(checkval, str) and len(checkval) > 0:
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
                fieldnameresult = ""

        case "SHIP_GEN_CREATE_DATE":
            if checkvalexists:
                # print("0: " + str(newfilerow))
                tempval = newfilerow[getsourcefilekeybyvalue("Shipped On Date")[1] - 1]
                tempval = ((tempval).replace("\'", ""))
                tempval = ((tempval).replace("[", ""))
                tempval = ((tempval).replace("\"", ""))
                if tempval == "":
                    fieldnameresult = tempval
                else:
                    # print("1: " + str(tempval))
                    tempdate = datetime.strptime(tempval, "%b-%d-%y")
                    fieldnameresult = tempdate.strftime("%m/%d/%Y")
                    # print(str(fieldnameresult))
        case "SHIP__EBAY_ORDERS__SHIPPED_DAT":
            if checkvalexists:
                # print("0: " + str(newfilerow))
                tempval = newfilerow[getsourcefilekeybyvalue("Shipped On Date")[1] - 1]
                tempval = ((tempval).replace("\'", ""))
                tempval = ((tempval).replace("[", ""))
                tempval = ((tempval).replace("\"", ""))
                if tempval == "":
                    fieldnameresult = tempval
                else:
                    # print("1: " + str(tempval))
                    tempdate = datetime.strptime(tempval, "%b-%d-%y")
                    fieldnameresult = tempdate.strftime("%m/%d/%Y")
                    # print(str(fieldnameresult))
        case "SHIP_GEN_CARRIER":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipping Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier(tempval)

        case "SHIP_GEN_CRR_SRV_DD":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipping Service")[1] - 1]
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
            # if checkvalexists:
            #     tempval = "AbesBargains"
            #     fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
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
            # if checkvalexists:
            #     tempval = "AbesBargains"
            #     fieldnameresult = GenFieldKey_CIQ1.get_gen_channel(tempval)
        case "SHIP_RATE_SHIP_CHRG":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Label Cost")[1] - 1]
                tempval = ""
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__BASE":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Label Cost")[1] - 1]
                tempval = ""
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__ORIGINAL":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Label Cost")[1] - 1]
                tempval = ""
                fieldnameresult = tempval
        case "SHIP_PKG_FULL_DIMS":
            if checkvalexists:
                # tempval_length = newfilerow[getsourcefilekeybyvalue("Length")[1] - 1]
                # tempval_width = newfilerow[getsourcefilekeybyvalue("Width")[1] - 1]
                # tempval_height = newfilerow[getsourcefilekeybyvalue("Height")[1] - 1]
                # tempval_final = str(tempval_length) + "x" + str(tempval_width) + "x" + str(tempval_height)
                tempval_final = ""
                fieldnameresult = tempval_final
        case "SHIP_GEN_PKG_LENGTH":
            if checkvalexists:
                # tempval_length = newfilerow[getsourcefilekeybyvalue("Length")[1] - 1]
                tempval_length = ""
                fieldnameresult = tempval_length
        case "SHIP_GEN_PKG_WIDTH":
            if checkvalexists:
                # tempval_width = newfilerow[getsourcefilekeybyvalue("Width")[1] - 1]
                tempval_width = ""
                fieldnameresult = tempval_width
        case "SHIP_GEN_PKG_HEIGHT":
            if checkvalexists:
                # tempval_height = newfilerow[getsourcefilekeybyvalue("Height")[1] - 1]
                tempval_height = ""
                fieldnameresult = tempval_height
        case "SHIP_GEN_PKG_WEIGHT":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]
                # tempval = float(tempval.replace("\'", ""))
                tempval = ""
                #fieldnameresult = str(round(float(tempval), 4))
                fieldnameresult = tempval
        case "SHIP_PKG_WEIGHT_OUNCES":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]

                # tempval = ((tempval).replace("\'", ""))
                # if len(tempval) > 0:
                #     tempval = float(tempval.replace("\'", ""))
                #     fieldnameresult = str(round(float(tempval) * 16, 4))
                # else:
                #     fieldnameresult = ""
                tempval = ""
                fieldnameresult = tempval

        case "SHIP_PKG_WEIGHT_TEXT":
            if checkvalexists:
                # tempval = newfilerow[getsourcefilekeybyvalue("Weight")[1] - 1]
                # tempval = float((tempval).replace("\'", ""))
                # tempvalstr = ""
                # if float(tempval) > 1:
                #     tempvalstr = str(math.floor(float(tempval))) + " lbs " + str(
                #         round((float(tempval) - math.floor(float(tempval))) * 16, 4)) + " oz"
                # else:
                #     tempvalstr = str(round(float(tempval) * 16, 4)) + " oz"
                # fieldnameresult = tempvalstr
                tempval = ""
                fieldnameresult = tempval
        case "SHIP_GEN_ORDER_ID":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue("Order Number")[1] - 1]
            fieldnameresult = str(getsourcefilekeybyvalue("Order Number")[5]) + tempval
        case "SHIP_GEN_ORDER_ID_2":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue("Sales Record Number")[1] - 1]
            fieldnameresult = str(getsourcefilekeybyvalue("Sales Record Number")[5]) + tempval
        case "SHIP_GEN_TRACK_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Tracking Number")[1] - 1]
                fieldnameresult = str(getsourcefilekeybyvalue("Tracking Number")[5]) + tempval
        case "SHIP_GEN_TO_STATE":
            # print("state:" + str(newfilerow[getsourcefilekeybyvalue("Ship To State")[1] - 1]))
            if checkvalexists:
                tempcountry = newfilerow[getsourcefilekeybyvalue("Ship To Country")[1] - 1]
                tempcountry = (tempcountry).replace("\'", "")
                tempcountry = (tempcountry).replace("\"", "")
                # print("tempcountry:" + str(tempcountry))
                if tempcountry.find("United States") != -1 or tempcountry.find("Virgin Islands") != -1:
                    tempval = newfilerow[getsourcefilekeybyvalue("Ship To State")[1] - 1]
                    tempval = (tempval).replace("\'", "")
                    tempval = (tempval).replace("\"", "")
                    fieldnameresult = GenFieldKey_CIQ1.get_to_state(tempval)
                    # print("tempstate:" + str(tempval))
                elif tempcountry.find("Puerto Rico") != -1:
                    fieldnameresult = GenFieldKey_CIQ1.get_to_state(tempcountry)
                    # print("tempcountry:" + str(tempcountry))
                else:
                    fieldnameresult = "ERROR UNKNOWN SHIP TO STATE"

        case "SHIP_GEN_FULL_NAME__SHIP_TO":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Ship To Name")[1] - 1]
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
        case "SHIP_SYSTEM_UPDATED_DATE":
            fieldnameresult = ""
        case "SHIP__COMBINED_SHIPMENT":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__DATA_SOURCE__EBAYORDERS":
            fieldnameresult = "Yes"
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
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    output_file = "DCv3Processed-Ebay-Shipping-" + date_string + "--" + str(1) + ".csv"
    counter1 = 2
    getnextfilename = True
    if Helpers1.checkoutputfilenameexists(output_file):
        while getnextfilename or counter1 < 10:
            if Helpers1.checkoutputfilenameexists(output_file):
                output_file = "DCv3Processed-Ebay-Shipping-" + date_string + "--" + str(counter1) + ".csv"
                #print(output_file)
            else:
                getnextfilename = False
            counter1 = counter1 + 1
    script_dir = os.path.dirname(__file__)
    reloutputfile = "_RESULTS\\" + output_file
    outputfile = os.path.join(script_dir, reloutputfile)
    return outputfile

def sourcestringprocessing(tempstring):

    newstring = tempstring

    newstring = str(newstring).replace("\\", "")
    newstring = str(newstring).replace("\'", "")
    newstring = str(newstring).replace("\"", "")

    return newstring

def getsourceidrefforlookup():

    return SOURCE_ID_REF_FOR_LOOKUP


#takes in entire list of filerows
def specialfunctions1(curfilename, encoding1, newline1):
    # determine which Ebay channel the file is for
    global EBAY_SOURCE

    if str(curfilename).find("DDS") != -1:

        EBAY_SOURCE = "DDS"
    elif str(curfilename).find("ABES") != -1:
        # global EBAY_SOURCE
        EBAY_SOURCE = "ABES"
    else:
        # global EBAY_SOURCE
        EBAY_SOURCE = "UNKNOWN"


def getmainxitorlookuptype():

    return MAIN_XITOR_LOOKUP_TYPE



#takes in entire list of filerows
def sourcefilekey_processing(filerow):
    count = 0

    # ONE: Remove duplicate rows for mult-line orders
    newfilerow = [[]]

    for temprow in filerow:
        if temprow != []:

            tempval = temprow[getsourcefilekeybyvalue("Buyer Name")[1] - 1]
            tempval = sourcestringprocessing(tempval)
            if tempval != "":
                newfilerow.append(temprow)
            else:
                print("Row Omitted, {" + str(tempval) + "} not found: " + str(filerow[count]))

        count += 1


    # TWO: Remove any backslashes
    newfilerow2 = [[]]

    for temprow2 in newfilerow:
        newtemprow = []
        for tempcol in temprow2:
            # print(tempcol)
            tempcol = str(tempcol).replace("\\", "")
            newtemprow.append(tempcol)
        newfilerow2.append(temprow2)

    return [newfilerow2]

#takes in one row string - final processing before writing to file
def sourcefilekey_processing_string(filerowstr):

    filerowstr = str(filerowstr).replace("\\", "")

    # replace stupid emojis
    replacechar1 = u"\U0001f642"
    filerowstr = str(filerowstr).replace(replacechar1, "[special character removed--U0001f642]")
    # object replacement character ???
    replacechar1 = u"\ufffc"
    filerowstr = str(filerowstr).replace(replacechar1, "[special character removed--ufffc]")
    # replace stupid emojis
    replacechar1 = u"\U0001f60a"
    filerowstr = str(filerowstr).replace(replacechar1, "[special character removed--U0001f60a]")


    return filerowstr


# takes in one list of a single row's elements
# returns None if row should be skipped
def preprocessfilerow(filerowlist):

    newfilerowlist = filerowlist

    # print("filerowlist:" + str(newfilerowlist))

    # if row is blank
    if newfilerowlist == ['[]']:
        newfilerowlist = None
        return newfilerowlist

    # if row is bullshit text notes from report source
    if len(newfilerowlist) > 1 and newfilerowlist[1].find("record(s) downloaded") != -1:
        newfilerowlist = None
        return newfilerowlist
    if len(newfilerowlist) > 0 and newfilerowlist[0].find("Seller ID") != -1:
        newfilerowlist = None
        return newfilerowlist

    return newfilerowlist


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
    "specialfunctions1": [specialfunctions1],
    "sourcefilekey_processing_string": [sourcefilekey_processing_string],
    "preprocessfilerow": [preprocessfilerow],
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
    "specialfunctions1": True,
    "preprocessfilerow": True,
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