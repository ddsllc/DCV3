import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import random

# SOURCE_ID_REF_FOR_LOOKUP = "Order ID"
SOURCE_ID_REF_FOR_LOOKUP = "LIST Listing ID"
RANDOM_RUN_ID = "-1"  # NO CHANGE NEEDED, this value is over-written by random number
RANDOM_RUN_ID_STR = "SFE_IMP-"  # Output file term
OUTPUT_FILE_KEYWORD_1 = "SFE-Amazon-UTR"
MAIN_XITOR_LOOKUP_TYPE = "_Sale Financial Event_"  # Keyword in CIQ export file for lookup


def getfunctionkey():

    return functionkey1


def getfunctionkey_processing():

    return functionkey_processing


sourcefilekey1 = {
    "SALE_FINANCIAL_EVENT_XITOR_KEY": [None, 1, -1, "SALE_FINANCIAL_EVENT_XITOR_KEY", "SALE_FINANCIAL_EVENT_XITOR_KEY",
                                       ""],
    "SFE_HAS_DATA_ISSUE": [None, 2, 1, "SFE_HAS_DATA_ISSUE", "SFE_HAS_DATA_ISSUE", ""],
    "SFE_DATA_ISSUE_NOTES": [None, 3, 1, "SFE_DATA_ISSUE_NOTES", "SFE_DATA_ISSUE_NOTES", ""],
    "SFE_AMOUNT": [None, 4, 1, "SFE_AMOUNT", "SFE_AMOUNT", ""],
    "SFE_FEES__BASE": [None, 5, 1, "SFE_FEES__BASE", "SFE_FEES__BASE", ""],
    "SFE_FEES__MISC": [None, 6, 1, "SFE_FEES__MISC", "SFE_FEES__MISC", ""],
    "SFE_ORDER_TOTAL": [None, 7, 1, "SFE_ORDER_TOTAL", "SFE_ORDER_TOTAL", ""],
    "SFE_SALES_CHANNEL": [None, 8, 1, "SFE_SALES_CHANNEL", "SFE_SALES_CHANNEL", ""],
    "SFE_INTERNAL_NOTES": [None, 9, 1, "SFE_INTERNAL_NOTES", "SFE_INTERNAL_NOTES", ""],
    "SFE_DESCRIPTION": [None, 10, 1, "SFE_DESCRIPTION", "SFE_DESCRIPTION", ""],
    "SFE_SKU": [None, 11, 1, "SFE_SKU", "SFE_SKU", ""],
    "SFE_ORDER_ID": [None, 12, 1, "SFE_ORDER_ID", "SFE_ORDER_ID", ""],
    "SFE_TYPE": [None, 13, 1, "SFE_TYPE", "SFE_TYPE", ""],
    "SFE_OPEN_DATE": [None, 14, 1, "SFE_OPEN_DATE", "SFE_OPEN_DATE", ""],
    "SFE_ALIAS_FIELD": [None, 15, 1, "SFE_ALIAS_FIELD", "SFE_ALIAS_FIELD", ""],
    "date/time": [1, 16, 0, "date/time", "date/time", ""],
    "settlement id": [2, 17, 0, "settlement id", "settlement id", ""],
    "type": [3, 18, 0, "type", "type", ""],
    "order id": [4, 19, 0, "order id", "order id", ""],
    "sku": [5, 20, 0, "sku", "sku", ""],
    "description": [6, 21, 0, "description", "description", ""],
    "quantity": [7, 22, 0, "quantity", "quantity", ""],
    "marketplace": [8, 23, 0, "marketplace", "marketplace", ""],
    "account type": [9, 24, 0, "account type", "account type", ""],
    "fulfillment": [10, 25, 0, "fulfillment", "fulfillment", ""],
    "order city": [11, 26, 0, "order city", "order city", ""],
    "order state": [12, 27, 0, "order state", "order state", ""],
    "order postal": [13, 28, 0, "order postal", "order postal", ""],
    "tax collection model": [14, 29, 0, "tax collection model", "tax collection model", ""],
    "product sales": [15, 30, 0, "product sales", "product sales", ""],
    "product sales tax": [16, 31, 0, "product sales tax", "product sales tax", ""],
    "shipping credits": [17, 32, 0, "shipping credits", "shipping credits", ""],
    "shipping credits tax": [18, 33, 0, "shipping credits tax", "shipping credits tax", ""],
    "gift wrap credits": [19, 34, 0, "gift wrap credits", "gift wrap credits", ""],
    "giftwrap credits tax": [20, 35, 0, "giftwrap credits tax", "giftwrap credits tax", ""],
    "Regulatory Fee": [21, 36, 0, "Regulatory Fee", "Regulatory Fee", ""],
    "Tax On Regulatory Fee": [22, 37, 0, "Tax On Regulatory Fee", "Tax On Regulatory Fee", ""],
    "promotional rebates": [23, 38, 0, "promotional rebates", "promotional rebates", ""],
    "promotional rebates tax": [24, 39, 0, "promotional rebates tax", "promotional rebates tax", ""],
    "marketplace withheld tax": [25, 40, 0, "marketplace withheld tax", "marketplace withheld tax", ""],
    "selling fees": [26, 41, 0, "selling fees", "selling fees", ""],
    "fba fees": [27, 42, 0, "fba fees", "fba fees", ""],
    "other transaction fees": [28, 43, 0, "other transaction fees", "other transaction fees", ""],
    "other": [29, 44, 0, "other", "other", ""],
    "total": [30, 45, 0, "total", "total", ""],

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
    retkey = sourcefilekey1["SaleTx_XITOR_KEY"][1]
    return retkey


def getcolplacement_tracknum():
    retkey = sourcefilekey1["Tracking ID"][1]
    return retkey


def getcolplacement_combinedflag():
    retkey = sourcefilekey1["SHIP__COMBINED_SHIPMENT"][1]
    return retkey


def getcalcfieldvalues(casefieldname, newfilerow):

    fieldnameresult = ""

    # print(newfilerow)

    #print(newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1])
    # checkval = newfilerow[getsourcefilekeybyvalue("Tracking ID")[1]-1]
    # checkval = newfilerow[getsourcefilekeybyvalue("Carrier")[1] - 1]
    # checkval = str(checkval).replace("$", "")
    # checkval = ((checkval).replace("\'", ""))
    # print(checkval)
    # checkvalexists = False
    checkvalexists = True
    # if isinstance(checkval, str) and len(checkval) > 0 and (checkval.find("Other") == -1 and checkval != "USPS"):
    # if isinstance(checkval, str) and len(checkval) > 0 and checkval.find("Buy Shipping") != -1:
    #     checkvalexists = True
    #     # print(checkval)

    match casefieldname:
        case "SALE_FINANCIAL_EVENT_XITOR_KEY":
            fieldnameresult = ""

        # case "LISTING":
        #     fieldnameresult = ""
        #
        # case "SALETX":
        #     fieldnameresult = ""

        case "SFE_HAS_DATA_ISSUE":
            fieldnameresult = ""

        case "SFE_DATA_ISSUE_NOTES":
            fieldnameresult = ""

        # case "SHIP_ACCOUNTING__ADDNL_DATA_VA":
        #     fieldnameresult = ""
        #
        # case "STX_NAME":
        #     if checkvalexists:
        #         tempval = newfilerow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
        #         fieldnameresult = tempval

        case "SFE_AMOUNT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("other")[1] - 1]
                fieldnameresult = tempval

        # case "SALE_LINE__SYSTEM_CREATED_DATE":
        #     current_date = datetime.now()
        #     date_string = current_date.strftime("%m/%d/%Y")
        #     fieldnameresult = date_string

        case "SFE_FEES__BASE":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("selling fees")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0.0
                tempval_fba = newfilerow[getsourcefilekeybyvalue("fba fees")[1] - 1]
                if tempval_fba == "":
                    tempval_fba = 0.0
                tempval = float(tempval_base) + float(tempval_fba)
                fieldnameresult = tempval

        case "SFE_FEES__MISC":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("other transaction fees")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0.0
                tempval = float(tempval_base)
                fieldnameresult = tempval

        case "SFE_ORDER_TOTAL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("product sales")[1] - 1]
                fieldnameresult = tempval

        case "SFE_OPEN_DATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("date/time")[1] - 1]
                # tempval = "Feb 1, 2025 6:09:01 AM US/Pacific"
                # tempval = str(tempval)[0:len(tempval)-3]
                tempval = tempval.replace("\'", "")
                tempval = tempval.replace("||", ",")
                tempval = tempval.replace(" PST", "")  # Time zone is throwing errors for unknown f'ing reason
                # print(str(datetime.now().strftime("%m/%d/%Y %Z")))

                # tempdate = datetime.strptime(tempval, "%b %d, %Y %I:%M:%S %p %Z")  # %b %d, %Y %I:%M:%S %p %Z
                tempdate = datetime.strptime(tempval, "%b %d, %Y %I:%M:%S %p")  # %b %d, %Y %I:%M:%S %p %Z
                fieldnameresult = tempdate.strftime("%m/%d/%Y %Z")
                # print(tempval)
        case "XITOR_CLASS_ID":
            fieldnameresult = "General Reselling"
        case "SALE_SALE_STATUS":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("item-status")[1] - 1]
                if tempval.find("Shipped") != -1:
                    tempval = "Sold - Open Warranty"
                elif tempval.find("Cancel") != -1:
                    tempval = "Canceled"
                else:
                    tempval = "Under Review - Internal"
                fieldnameresult = tempval
        case "SALE_FINANCIAL_FEES":
            if checkvalexists:
                fieldnameresult = 0
        case "SALE_SHIPPING_COST":
            fieldnameresult = ""
        case "SALE__SELL_ID_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
                fieldnameresult = tempval
        case "SALE_MARKETPLACE_TRANSACTION_ID":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("asin")[1] - 1]
                fieldnameresult = tempval
        case "SALE_LINE__TOTAL":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                tempval_ship = newfilerow[getsourcefilekeybyvalue("shipping-price")[1] - 1]
                tempval_misc = newfilerow[getsourcefilekeybyvalue("gift-wrap-price")[1] - 1]
                tempval_base_t = newfilerow[getsourcefilekeybyvalue("item-tax")[1] - 1]
                tempval_ship_t = newfilerow[getsourcefilekeybyvalue("shipping-tax")[1] - 1]
                tempval_misc_t = newfilerow[getsourcefilekeybyvalue("gift-wrap-tax")[1] - 1]

                tempvalarr = [tempval_base, tempval_ship, tempval_misc, tempval_base_t, tempval_ship_t, tempval_misc_t]

                tempval = 0
                for tval in tempvalarr:
                    if tval == "":
                        tval = 0
                    tempval += float(tval)

                # if tempval_base == "" or tempval_ship == "":
                #     if tempval_base != "":
                #         tempval = float(tempval_base)
                #     elif tempval_ship != "":
                #         tempval = float(tempval_ship)
                #     else:
                #         tempval = 0
                # else:
                #     tempval = float(tempval_base) + float(tempval_ship)
                fieldnameresult = tempval
        case "SALE_LINE__NET_ORDER_TOTAL":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                tempval_ship = newfilerow[getsourcefilekeybyvalue("shipping-price")[1] - 1]
                tempval_misc = newfilerow[getsourcefilekeybyvalue("gift-wrap-price")[1] - 1]

                tempvalarr = [tempval_base, tempval_ship, tempval_misc]

                tempval = 0
                for tval in tempvalarr:
                    if tval == "":
                        tval = 0
                    tempval += float(tval)

                fieldnameresult = tempval
        case "SALE_LINE__SUBTOTAL":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0
                fieldnameresult = tempval_base
        case "SALETX___OF_LINES":
            fieldnameresult = 1
        case "SALE_LINE__SHIPPING_CHARGES":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping-price")[1] - 1]
                if tempval == "":
                    tempval = 0
                fieldnameresult = tempval
        case "SALE_LINE__MISC_CHARGES":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("gift-wrap-price")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0
                fieldnameresult = tempval_base
        case "SALE_LINE__TAXES":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-tax")[1] - 1]
                # tempval_ship = newfilerow[getsourcefilekeybyvalue("shipping-tax")[1] - 1]
                tempval_ship = 0
                # print("item-tax:" + str(tempval_base) + "| shipping-tax:" + str(tempval_ship))
                if tempval_base == "" or tempval_ship == "":
                    if tempval_base != "":
                        tempval = float(tempval_base)
                    elif tempval_ship != "":
                        tempval = float(tempval_ship)
                    else:
                        tempval = ""
                else:
                    tempval = float(tempval_base) + float(tempval_ship)

                fieldnameresult = tempval
        case "SALE_LINE__SHIPPING_CHARGES__T":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping-tax")[1] - 1]
                if tempval == "":
                    tempval = 0
                fieldnameresult = tempval
        case "SALE_LINE__MISC_CHARGES__TAXES":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("gift-wrap-tax")[1] - 1]
                if tempval == "":
                    tempval = 0
                fieldnameresult = tempval
        case "SALE__ITEM_QUANTITY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("description")[1] - 1]
                fieldnameresult = tempval
        case "SFE_SALES_CHANNEL":
            if checkvalexists:
                fieldnameresult = "CN/Amazon-FBM"
        case "SFE_INTERNAL_NOTES":
            if checkvalexists:
                fieldnameresult = ""
        case "SFE_DESCRIPTION":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("description")[1] - 1]
                fieldnameresult = tempval
        case "SFE_ALIAS_FIELD":
            if checkvalexists:
                temptype = newfilerow[getsourcefilekeybyvalue("type")[1] - 1]
                if temptype == "Order":
                    tempvalsku = newfilerow[getsourcefilekeybyvalue("sku")[1] - 1]
                    tempvalorderid = newfilerow[getsourcefilekeybyvalue("order id")[1] - 1]
                    fieldnameresult = str(tempvalorderid) + "-" + str(tempvalsku)
                elif temptype == "Shipping Services":
                    tempvalorderid = newfilerow[getsourcefilekeybyvalue("order id")[1] - 1]
                    fieldnameresult = str(tempvalorderid)
                else:
                    tempvalorderid = newfilerow[getsourcefilekeybyvalue("order id")[1] - 1]
                    fieldnameresult = str(tempvalorderid)

        case "SFE_SKU":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("sku")[1] - 1]
                fieldnameresult = tempval
        case "SFE_ORDER_ID":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("order id")[1] - 1]
                fieldnameresult = tempval
        case "SFE_TYPE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("type")[1] - 1]
                fieldnameresult = tempval
        case "STX_GEN_BUYER_NOTES":
            fieldnameresult = ""
        case "STX_ID_TRACKING_SECONDARY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("sku")[1] - 1]
                fieldnameresult = tempval
        case "STX_FINANCIAL_TX_ID":
            fieldnameresult = ""
        case "STX_SHIPPING_NAME":
            fieldnameresult = ""
        case "STX_SHIPPING_ADDRESS1":
            fieldnameresult = ""
        case "STX_SHIPPING_ADDRESS2":
            fieldnameresult = ""
        case "STX_SHIPPING_CITY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("ship-city")[1] - 1]
                fieldnameresult = tempval
        case "STX_SHIPPING_PROVINCE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("ship-state")[1] - 1]
                fieldnameresult = tempval
        case "STX_SHIPPING_ZIP":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("ship-postal-code")[1] - 1]
                fieldnameresult = tempval
        case "STX_SHIPPING_COUNTRY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("ship-country")[1] - 1]
                fieldnameresult = tempval
            fieldnameresult = ""
        case "SALE_AMZ_ORDER_ID":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
                fieldnameresult = tempval
        case "SALE_AMZ_MERCH_ORDER_ID":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("merchant-order-id")[1] - 1]
                fieldnameresult = tempval
        case "SALE_AMZ_PURCH_DATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("purchase-date")[1] - 1]
                fieldnameresult = tempval
        case "ITEMDATA_AMAZON__LAST_UPDATED_":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("purchase-date")[1] - 1]
                fieldnameresult = tempval
        case "ITEMDATA_AMAZON__ORDER_STATUS":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("order-status")[1] - 1]
                fieldnameresult = tempval

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
        case "SALE_LINE__SYSTEM_CREATED_DATE":
            current_date = datetime.now()
            date_string = current_date.strftime("%m/%d/%Y")
            fieldnameresult = date_string
        case "SALE_LINE__SYSTEM_LAST_UPDATED":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__COMBINED_SHIPMENT":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__DATA_SOURCE__VEEQO":
            fieldnameresult = "Yes"
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


def getsecondarylookupvalues(casefieldname, curfilerow, keyfile, filekey_proc, filekey_lookup):

    newfilerow = ""
    fieldnameresult = ""

    match casefieldname:
        case "SHIPMENT":
            tempvalid = curfilerow[getsourcefilekeybyvalue("STX_MARKETPLACE_TX_ID")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            print("getsecondarylookupvalues run|" + casefieldname)
            print(tempvalid)
            print("curfilerow|" + str(curfilerow))
            newfilerow = Helpers1.secondarylookupvaluesfromfile(casefieldname, "_Shipment_", curfilerow, tempvalid,
                                                                keyfile, filekey_proc, filekey_lookup)
        case "LISTING":
            # tempvalid = curfilerow[getsourcefilekeybyvalue("ITEMDATA_GENERAL_CUSTOM_SKU")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            # fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            print("getsecondarylookupvalues run|" + casefieldname)
            # print(tempvalid)
            print("curfilerow|" + str(curfilerow))
            newfilerow = Helpers1.secondarylookupvaluesfromfile2(casefieldname, ["_Sale Line_", "_SalesListing_"],
                                                                 curfilerow, "", keyfile, filekey_proc,
                                                                 filekey_lookup)
        case "SALETX":
            # tempvalid = curfilerow[getsourcefilekeybyvalue("ITEMDATA_GENERAL_CUSTOM_SKU")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            # fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            print("getsecondarylookupvalues run|" + casefieldname)
            # print(tempvalid)
            print("curfilerow|" + str(curfilerow))
            newfilerow = Helpers1.secondarylookupvaluesfromfile2(casefieldname, ["_Sale Line_", "_SaleTx_"],
                                                                 curfilerow, "", keyfile, filekey_proc,
                                                                 filekey_lookup)
        case _:
            print("Secondary Lookup Value field not found for Switch statement: " + str(casefieldname))
            return curfilerow



    return newfilerow


def setrandomrunid():

    runid = random.randint(0, 99999999)
    runidstr = RANDOM_RUN_ID_STR + str(runid)
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


#takes in entire list of filerows
def specialfunctions1(curfilename, encoding1, newline1):

    process_AmazonAO_stx(curfilename, encoding1, newline1)


def process_AmazonAO_stx(curfilename, encoding1, newline1):



    return None


def getsourceidrefforlookup():

    return SOURCE_ID_REF_FOR_LOOKUP


def getmainxitorlookuptype():

    return MAIN_XITOR_LOOKUP_TYPE



def sourcefilekey_processing(filerow):

    # count = 0
    #
    # # ONE: Remove duplicate rows to create list of unique STX's
    # newfilerows = [[]]
    # lastorderid = ""
    #
    # for temprow in filerow:
    #     if temprow != []:
    #
    #         tempval = temprow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
    #         tempval = sourcestringprocessing(tempval)
    #         if tempval != lastorderid:
    #             newfilerows.append(temprow)
    #         # else:
    #         #     # print("Row Omitted, {" + str(tempval) + "} duplicate row: " + str(filerow[count]))
    #         #     print("Row Omitted, {" + str(tempval) + "} duplicate row")
    #         lastorderid = tempval
    #     count += 1
    #
    # # TWO: Traverse original list to calculate aggregate fields (i.e. transaction total, quantity, numlines, tax, shipp)
    # #take in new list
    # #for each row in new list, traverse old list
    #     #for each row in old list, check id match, if match then += cum value
    #     #when done, put cum value into new list field destination
    #
    # for temprow2 in newfilerows:
    #     # get id in temprow2
    #
    #     # print("sourcefilekey_processing1:" + str(temprow2))
    #
    #     if temprow2 == []:
    #         continue
    #     lookupid1 = temprow2[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
    #
    #     # setup cum values
    #     cumval_price = 0  # item-price + [ship charges]
    #     cumval_subtotal = 0  # item-price
    #     cumval_quantity = 0  # quantity
    #     cumval_numlines = 0  # [count number of tx lines]
    #     cumval_tax1 = 0  # item-tax
    #     cumval_shippingpaid = 0  # shipping-price
    #     cumval_shippingtax = 0  # shipping-tax
    #
    #     # cumval_price_loc = getsourcefilekeybyvalue("item-price")[1] - 1  # item-price
    #     # cumval_quantity_loc = getsourcefilekeybyvalue("quantity")[1] - 1  # quantity
    #     # cumval_numlines_loc = 0  # [count number of tx lines]
    #     # cumval_tax1_loc = getsourcefilekeybyvalue("item-tax")[1] - 1  # item-tax
    #     # cumval_shippingpaid_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
    #     # cumval_shippingtax_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
    #
    #     cumval_price_loc = getsourcefilekeybyvalue("item-price")[1] - 1  # item-price
    #     cumval_quantity_loc = getsourcefilekeybyvalue("quantity")[1] - 1  # quantity
    #     cumval_numlines_loc = 0  # [count number of tx lines]
    #     cumval_tax1_loc = getsourcefilekeybyvalue("item-tax")[1] - 1  # item-tax
    #     cumval_shippingpaid_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
    #     cumval_shippingtax_loc = getsourcefilekeybyvalue("shipping-tax")[1] - 1  # shipping-price
    #
    #     cumval_price_loc2 = getsourcefilekeybyvalue("STX_TOTAL")[1] - 1  # item-price
    #     cumval_subtotal_loc2 = getsourcefilekeybyvalue("SALETX_SUBTOTAL2")[1] - 1  #
    #     cumval_quantity_loc2 = getsourcefilekeybyvalue("STX_ITEM_QUANTITY")[1] - 1  # quantity
    #     cumval_numlines_loc2 = getsourcefilekeybyvalue("SALETX___OF_LINES")[1] - 1  # [count number of tx lines]
    #     cumval_tax1_loc2 = getsourcefilekeybyvalue("STX_TAXES")[1] - 1  # item-tax
    #     cumval_shippingpaid_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES")[1] - 1  # shipping-price
    #     cumval_shippingtax_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES__TAXE")[1] - 1  # shipping-price
    #
    #     for oldtemprow in filerow:
    #         # check id match to temprow2
    #         if oldtemprow == []:
    #             continue
    #         lookupid2 = oldtemprow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
    #
    #         if lookupid1 == lookupid2:
    #             cumval_numlines += 1
    #
    #             # cumval_shippingpaid
    #             tempval_shippingpaid = oldtemprow[cumval_shippingpaid_loc]
    #             if tempval_shippingpaid != "":
    #                 cumval_shippingpaid = cumval_shippingpaid + float(oldtemprow[cumval_shippingpaid_loc])
    #
    #             # cumval_subtotal
    #             tempval_subtotal = oldtemprow[cumval_price_loc]
    #             if tempval_subtotal != "":
    #                 cumval_subtotal = cumval_subtotal + float(oldtemprow[cumval_price_loc])
    #
    #             # cumval_price
    #             if tempval_subtotal == "" or tempval_shippingpaid == "":
    #                 if tempval_subtotal != "":
    #                     cumval_price = cumval_price + float(tempval_subtotal)
    #                 elif tempval_shippingpaid != "":
    #                     cumval_price = cumval_price + float(tempval_shippingpaid)
    #                 else:
    #                     cumval_price = cumval_price + 0
    #             else:
    #                 cumval_price = cumval_price + float(tempval_subtotal) + float(tempval_shippingpaid)
    #
    #             # cumval_quantity
    #             tempval_quantity = oldtemprow[cumval_quantity_loc]
    #             if tempval_quantity != "":
    #                 cumval_quantity = cumval_quantity + float(oldtemprow[cumval_quantity_loc])
    #
    #             tempval_tax1 = oldtemprow[cumval_tax1_loc]
    #             if tempval_tax1 != "":
    #                 cumval_tax1 = cumval_tax1 + float(oldtemprow[cumval_tax1_loc])
    #
    #             tempval_shippingtax = oldtemprow[cumval_shippingtax_loc]
    #             if tempval_shippingtax != "":
    #                 cumval_shippingtax = cumval_shippingtax + float(oldtemprow[cumval_shippingtax_loc])
    #         # end for2
    #     if cumval_numlines > 1:
    #         # print("Match:" + str(lookupid1) + "|" + str(cumval_numlines) + "|" + str(cumval_price))
    #         temprow2[cumval_numlines_loc2] = cumval_numlines
    #         temprow2[cumval_price_loc2] = cumval_price
    #         temprow2[cumval_subtotal_loc2] = cumval_subtotal
    #         temprow2[cumval_quantity_loc2] = cumval_quantity
    #         temprow2[cumval_tax1_loc2] = cumval_tax1
    #         temprow2[cumval_shippingpaid_loc2] = cumval_shippingpaid
    #         temprow2[cumval_shippingtax_loc2] = cumval_shippingtax
    #     # print("sourcefilekey_processing2:" + str(temprow2))
    #     # end for1


    return [filerow]


def sourcestringprocessing(tempstring):

    newstring = tempstring

    # newstring = str(newstring).replace("\\", "")
    # newstring = str(newstring).replace("\'", "")
    # newstring = str(newstring).replace("\"", "")

    return newstring


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
    "getsecondarylookupvalues": [getsecondarylookupvalues],
    "getoutputfile_add": [getoutputfile_add],
    "getoutputfile_update": [getoutputfile_update],
    "getoutputfile_err": [getoutputfile_err],
    "getoutputfile_test1": [getoutputfile_test1],
    "getsourceidrefforlookup": [getsourceidrefforlookup],
    "sourcefilekey_processing": [sourcefilekey_processing],
    "setrandomrunid": [setrandomrunid],
    "specialfunctions1": [specialfunctions1],
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
    "specialfunctions1": False,
    "processfilenextrow": True,
    "processcalculatedrows": True,
    "processtranslatedrows": False,
    "getsecondarylookupvalues": False,
    "finalerrorcheck": True,
    "pushfinalerrormessage": True,
    "ciqidlookupadd": True,
    "ciqsearchlookupfile": False,
    "buildcombinedshipmentslist": False,
    "markcombinedshipments": False,
    "sourcefilekey_processing": False,
    "general_post_processing": False,
    "write_row_list_to_files": True,
    "filecleanup": True,



}
