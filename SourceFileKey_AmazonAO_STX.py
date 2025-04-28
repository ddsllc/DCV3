import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import random

# SOURCE_ID_REF_FOR_LOOKUP = "Order ID"
SOURCE_ID_REF_FOR_LOOKUP = "SaleTx_XITOR_KEY"
RANDOM_RUN_ID = "-1"
RANDOM_RUN_ID_STR = "STX_IMP-"
OUTPUT_FILE_KEYWORD_1 = "Amazon-AO-STX"
MAIN_XITOR_LOOKUP_TYPE = "_SaleTx_"  # Keyword in CIQ export file for lookup


def getfunctionkey():

    return functionkey1


def getfunctionkey_processing():

    return functionkey_processing


sourcefilekey1 = {
    "SaleTx_XITOR_KEY": [None, 1, -1, "SaleTx_XITOR_KEY", "SaleTx_XITOR_KEY", ""],
    "CONTACT": [None, 2, 3, "CONTACT", "CONTACT", ""],
    "SHIPMENT": [None, 3, 3, "SHIPMENT", "SHIPMENT", ""],
    "STX_NAME": [None, 4, 1, "STX_NAME", "STX_NAME", ""],
    "STX_GENERAL_CUSTOM_SKU": [None, 5, 1, "STX_GENERAL_CUSTOM_SKU", "STX_GENERAL_CUSTOM_SKU", ""],
    "STX_CREATED_AT": [None, 6, 1, "STX_CREATED_AT", "STX_CREATED_AT", ""],
    "STX_UPDATED_AT": [None, 7, 1, "STX_UPDATED_AT", "STX_UPDATED_AT", ""],
    "STX_WARRANTY_END_DATE": [None, 8, 1, "STX_WARRANTY_END_DATE", "STX_WARRANTY_END_DATE", ""],
    "STX_CURRENCY": [None, 9, 1, "STX_CURRENCY", "STX_CURRENCY", ""],
    "STX_DATE": [None, 10, 1, "STX_DATE", "STX_DATE", ""],
    "XITOR_CLASS_ID": [None, 11, 1, "XITOR_CLASS_ID", "XITOR_CLASS_ID", ""],
    "STX_STATUS": [None, 12, 1, "STX_STATUS", "STX_STATUS", ""],
    "STX_FINANCIAL_FEES": [None, 13, 1, "STX_FINANCIAL_FEES", "STX_FINANCIAL_FEES", ""],
    "STX_SHIPPING_COST": [None, 14, 4, "STX_SHIPPING_COST", "STX_SHIPPING_COST", ""],
    "STX_SHIPPING_COST_COUNT": [None, 15, 1, "STX_SHIPPING_COST_COUNT", "STX_SHIPPING_COST_COUNT", ""],
    "STX_INITIAL_COST": [None, 16, 4, "STX_INITIAL_COST", "STX_INITIAL_COST", ""],
    "STX_INITIAL_COST_COUNT": [None, 17, 1, "STX_INITIAL_COST_COUNT", "STX_INITIAL_COST_COUNT", ""],
    "STX_MARKETPLACE_TX_ID": [None, 18, 1, "STX_MARKETPLACE_TX_ID", "STX_MARKETPLACE_TX_ID", ""],
    "STX_SELL_ID_NUM": [None, 19, 1, "STX_SELL_ID_NUM", "STX_SELL_ID_NUM", ""],
    "STX_TOTAL": [None, 20, 1, "STX_TOTAL", "STX_TOTAL", ""],
    "SALETX_SUBTOTAL2": [None, 21, 1, "SALETX_SUBTOTAL2", "SALETX_SUBTOTAL2", ""],
    "SALETX___OF_LINES": [None, 22, 1, "SALETX___OF_LINES", "SALETX___OF_LINES", ""],
    "SALETX__SHIPPING_CHARGES": [None, 23, 1, "SALETX__SHIPPING_CHARGES", "SALETX__SHIPPING_CHARGES", ""],
    "SALETX__MISC_CHARGES": [None, 24, 1, "SALETX__MISC_CHARGES", "SALETX__MISC_CHARGES", ""],
    "STX_TAXES2": [None, 25, 1, "STX_TAXES2", "STX_TAXES2", ""],
    "SALETX__SHIPPING_CHARGES__TAXE": [None, 26, 1, "SALETX__SHIPPING_CHARGES__TAXE", "SALETX__SHIPPING_CHARGES__TAXE",
                                       ""],
    "SALETX__MISC_CHARGES__TAXES": [None, 27, 1, "SALETX__MISC_CHARGES__TAXES", "SALETX__MISC_CHARGES__TAXES", ""],
    "STX_ITEM_QUANTITY": [None, 28, 1, "STX_ITEM_QUANTITY", "STX_ITEM_QUANTITY", ""],
    "STX_SELL_ACCT_CHAN": [None, 29, 1, "STX_SELL_ACCT_CHAN", "STX_SELL_ACCT_CHAN", ""],
    "STX_SELLING_ACCOUNT": [None, 30, 1, "STX_SELLING_ACCOUNT", "STX_SELLING_ACCOUNT", ""],
    "STX_PAY_ACCOUNT": [None, 31, 1, "STX_PAY_ACCOUNT", "STX_PAY_ACCOUNT", ""],
    "STX_DESC": [None, 32, 1, "STX_DESC", "STX_DESC", ""],
    "STX_COMMISSION_FEES": [None, 33, 4, "STX_COMMISSION_FEES", "STX_COMMISSION_FEES", ""],
    "STX_COMMISSION_FEES_COUNT": [None, 34, 1, "STX_COMMISSION_FEES_COUNT", "STX_COMMISSION_FEES_COUNT", ""],
    "STX_ADPROMO_COSTS": [None, 35, 1, "STX_ADPROMO_COSTS", "STX_ADPROMO_COSTS", ""],
    "STX_IMPORT_ID": [None, 36, 1, "STX_IMPORT_ID", "STX_IMPORT_ID", ""],
    "STX_GEN_BUYER_NOTES": [None, 37, 1, "STX_GEN_BUYER_NOTES", "STX_GEN_BUYER_NOTES", ""],
    "STX_ID_TRACKING_SECONDARY": [None, 38, 1, "STX_ID_TRACKING_SECONDARY", "STX_ID_TRACKING_SECONDARY", ""],
    "STX_FINANCIAL_TX_ID": [None, 39, 1, "STX_FINANCIAL_TX_ID", "STX_FINANCIAL_TX_ID", ""],
    "STX_SHIPPING_NAME": [None, 40, 1, "STX_SHIPPING_NAME", "STX_SHIPPING_NAME", ""],
    "STX_SHIPPING_ADDRESS1": [None, 41, 1, "STX_SHIPPING_ADDRESS1", "STX_SHIPPING_ADDRESS1", ""],
    "STX_SHIPPING_ADDRESS2": [None, 42, 1, "STX_SHIPPING_ADDRESS2", "STX_SHIPPING_ADDRESS2", ""],
    "STX_SHIPPING_CITY": [None, 43, 1, "STX_SHIPPING_CITY", "STX_SHIPPING_CITY", ""],
    "STX_SHIPPING_PROVINCE": [None, 44, 1, "STX_SHIPPING_PROVINCE", "STX_SHIPPING_PROVINCE", ""],
    "STX_SHIPPING_ZIP": [None, 45, 1, "STX_SHIPPING_ZIP", "STX_SHIPPING_ZIP", ""],
    "STX_SHIPPING_COUNTRY": [None, 46, 1, "STX_SHIPPING_COUNTRY", "STX_SHIPPING_COUNTRY", ""],
    "STX_SHIPPING_PHONE": [None, 47, 1, "STX_SHIPPING_PHONE", "STX_SHIPPING_PHONE", ""],
    "STX_EMAIL": [None, 48, 1, "STX_EMAIL", "STX_EMAIL", ""],
    "STX_PAY_FROM_MRKT": [None, 49, 1, "STX_PAY_FROM_MRKT", "STX_PAY_FROM_MRKT", ""],
    "STX_PERC_WITHHELD": [None, 50, 1, "STX_PERC_WITHHELD", "STX_PERC_WITHHELD", ""],
    "STX_SELL_RECOVERY": [None, 51, 1, "STX_SELL_RECOVERY", "STX_SELL_RECOVERY", ""],
    "STX_CALC_ITEM_PROFIT": [None, 52, 1, "STX_CALC_ITEM_PROFIT", "STX_CALC_ITEM_PROFIT", ""],
    "SALETX__NET_MARGIN_2": [None, 53, 1, "SALETX__NET_MARGIN_2", "SALETX__NET_MARGIN_2", ""],
    "STX_LINE_ITEM_ROI": [None, 54, 1, "STX_LINE_ITEM_ROI", "STX_LINE_ITEM_ROI", ""],
    "temp sell recovery": [None, 55, 1, "temp sell recovery", "temp sell recovery", ""],
    "amazon-order-id": [1, 56, 0, "amazon-order-id", "STX_AMZ_ORDER_ID", ""],
    "merchant-order-id": [2, 57, 0, "merchant-order-id", "STX_AMZ_MERCH_ORDER_ID", ""],
    "purchase-date": [3, 58, 0, "purchase-date", "STX_AMZ_PURCH_DATE", ""],
    "last-updated-date": [4, 59, 0, "last-updated-date", "STX_AMZ_LAST_UPDATED_", ""],
    "order-status": [5, 60, 0, "order-status", "STX_AMZ_ORDER_STATUS", ""],
    "fulfillment-channel": [6, 61, 0, "fulfillment-channel", "STX_AMZ_FULF_CHANNEL", ""],
    "sales-channel": [7, 62, 0, "sales-channel", "STX_AMZ_SALES_CHANNEL", ""],
    "order-channel": [8, 63, 0, "order-channel", "", ""],
    "url": [9, 64, 0, "url", "", ""],
    "ship-service-level": [10, 65, 0, "ship-service-level", "STX_AMZ_SHIP_SERV_LVL", ""],
    "product-name": [11, 66, 0, "product-name", "STX_AMZ_PRODUCT_NAME", ""],
    "sku": [12, 67, 0, "sku", "STX_AMZ_SKU", ""],
    "asin": [13, 68, 0, "asin", "STX_AMZ_ASIN", ""],
    "number-of-items": [14, 69, 0, "number-of-items", "SALETX_AMAZON__NUMBER_OF_ITEMS", ""],
    "item-status": [15, 70, 0, "item-status", "", ""],
    "quantity": [16, 71, 0, "quantity", "STX_AMZ_QUANT", ""],
    "currency": [17, 72, 0, "currency", "STX_AMZ_CURRENCY", ""],
    "item-price": [18, 73, 0, "item-price", "STX_AMZ_ITEM_PRICE", ""],
    "item-tax": [19, 74, 0, "item-tax", "STX_AMZ_ITEM_TAX", ""],
    "shipping-price": [20, 75, 0, "shipping-price", "STX_AMZ_SHIP_PRICE", ""],
    "shipping-tax": [21, 76, 0, "shipping-tax", "STX_AMZ_SHIP_TAX", ""],
    "gift-wrap-price": [22, 77, 0, "gift-wrap-price", "STX_AMZ_GIFTWRAP_PRICE", ""],
    "gift-wrap-tax": [23, 78, 0, "gift-wrap-tax", "STX_AMZ_GIFTWRAP_TAX", ""],
    "item-promotion-discount": [24, 79, 0, "item-promotion-discount", "STX_AMZ_ITEM_PROMO_DISC", ""],
    "ship-promotion-discount": [25, 80, 0, "ship-promotion-discount", "", ""],
    "address-type": [26, 81, 0, "address-type", "SALETX_AMAZON__ADDRESS_TYPE", ""],
    "ship-city": [27, 82, 0, "ship-city", "STX_AMZ_SHIP_ADDR_CITY", ""],
    "ship-state": [28, 83, 0, "ship-state", "STX_AMZ_SHIP_ADDR_STATE", ""],
    "ship-postal-code": [29, 84, 0, "ship-postal-code", "STX_AMZ_SHIP_ADDR_ZIP", ""],
    "ship-country": [30, 85, 0, "ship-country", "STX_AMZ_SHIP_ADDR_COUNTRY", ""],
    "promotion-ids": [31, 86, 0, "promotion-ids", "", ""],
    "cpf": [32, 87, 0, "cpf", "", ""],
    "is-business-order": [33, 88, 0, "is-business-order", "SALETX_AMAZON__IS_BUSINESS_ORD", ""],
    "purchase-order-number": [34, 89, 0, "purchase-order-number", "", ""],
    "price-designation": [35, 90, 0, "price-designation", "", ""],
    "is-transparency": [36, 91, 0, "is-transparency", "SALETX_AMAZON__IS_TRANSPARENCY", ""],
    "signature-confirmation-recommended ": [37, 92, 0, "signature-confirmation-recommended ", "", ""],

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

    LOCAL_CONSOLE_OUTPUT1 = False

    fieldnameresult = ""

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
        case "SaleTx_XITOR_KEY":
            fieldnameresult = ""

        case "CONTACT":
            fieldnameresult = ""

        case "SHIPMENT":
            fieldnameresult = ""

        case "SHIP_HAS_DATA_ISSUE":
            fieldnameresult = ""

        case "SHIP_DATA_ISSUE_NOTES":
            fieldnameresult = ""

        case "SHIP_ACCOUNTING__ADDNL_DATA_VA":
            fieldnameresult = ""

        case "STX_NAME":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
                fieldnameresult = tempval

        case "STX_GENERAL_CUSTOM_SKU":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("sku")[1] - 1]
                fieldnameresult = tempval

        case "STX_CREATED_AT":
            current_date = datetime.now()
            date_string = current_date.strftime("%m/%d/%Y")
            fieldnameresult = date_string

        case "STX_CREATED_AT":
            fieldnameresult = ""

        case "STX_WARRANTY_END_DATE":
            fieldnameresult = ""

        case "STX_CURRENCY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("currency")[1] - 1]
                fieldnameresult = tempval

        case "STX_DATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("purchase-date")[1] - 1]
                # tempval = str(tempval)[0:len(tempval)-3]
                # tempval = tempval.replace("00:00", "0000")
                # print(str(tempval))
                tempdate = datetime.strptime(tempval, "%Y-%m-%dT%H:%M:%S%z")
                fieldnameresult = tempdate.strftime("%m/%d/%Y")
                # print(tempval)
        case "XITOR_CLASS_ID":
            fieldnameresult = ""
        case "STX_STATUS":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("order-status")[1] - 1]
                if tempval.find("Shipped") != -1:
                    tempval = "Sold - Open Warranty"
                elif tempval.find("Cancel") != -1:
                    tempval = "Canceled"
                else:
                    tempval = "Under Review - Internal"
                fieldnameresult = tempval
        case "STX_FINANCIAL_FEES":
            if checkvalexists:
                fieldnameresult = 0
        case "STX_SHIPPING_COST":
            fieldnameresult = ""
        case "STX_MARKETPLACE_TX_ID":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
                fieldnameresult = tempval
        case "STX_SELL_ID_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("asin")[1] - 1]
                fieldnameresult = tempval
        case "STX_TOTAL":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                tempval_ship = newfilerow[getsourcefilekeybyvalue("shipping-price")[1] - 1]
                tempval_base_tax = newfilerow[getsourcefilekeybyvalue("item-tax")[1] - 1]
                tempval_ship_tax = newfilerow[getsourcefilekeybyvalue("shipping-tax")[1] - 1]

                templist = [tempval_base, tempval_ship, tempval_base_tax, tempval_ship_tax]

                tempval_temptotal = 0
                for templistitem in templist:
                    if templistitem != "":
                        tempval_temptotal = tempval_temptotal + float(templistitem)
                # if tempval_base == "" or tempval_ship == "":
                #     if tempval_base != "":
                #         tempval = float(tempval_base)
                #     elif tempval_ship != "":
                #         tempval = float(tempval_ship)
                #     else:
                #         tempval = 0
                # else:
                #     tempval = float(tempval_base) + float(tempval_ship)
                fieldnameresult = tempval_temptotal
        case "SALETX_SUBTOTAL2":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0
                fieldnameresult = tempval_base
        case "SALETX___OF_LINES":
            fieldnameresult = 1
        case "SALETX__SHIPPING_CHARGES":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping-price")[1] - 1]
                if tempval == "":
                    tempval = 0
                fieldnameresult = tempval
        case "SALETX__MISC_CHARGES":
            if checkvalexists:
                tempval_base = newfilerow[getsourcefilekeybyvalue("gift-wrap-price")[1] - 1]
                if tempval_base == "":
                    tempval_base = 0
                fieldnameresult = tempval_base
        case "STX_TAXES2":
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
                    tempval = (float(tempval_base) + float(tempval_ship))

                fieldnameresult = tempval
        case "SALETX__SHIPPING_CHARGES__TAXE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping-tax")[1] - 1]
                if tempval == "":
                    tempval = 0
                fieldnameresult = tempval
        case "STX_ITEM_QUANTITY":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("quantity")[1] - 1]
                fieldnameresult = tempval
        case "STX_SELL_ACCT_CHAN":
            if checkvalexists:
                fieldnameresult = "Amazon"
        case "STX_SELLING_ACCOUNT":
            if checkvalexists:
                fieldnameresult = "CN/Amazon-FBM"
        case "STX_PAY_ACCOUNT":
            if checkvalexists:
                fieldnameresult = "CN Checking"
        case "STX_DESC":
            if checkvalexists:
                tempvalttl = newfilerow[getsourcefilekeybyvalue("item-price")[1] - 1]
                tempvalcity = newfilerow[getsourcefilekeybyvalue("ship-city")[1] - 1]
                tempvalstate = newfilerow[getsourcefilekeybyvalue("ship-state")[1] - 1]

                # tempval = "\"$" + tempvalttl + " FBM Purchase to " + tempvalcity + " | " + tempvalstate + "\""
                # order total will be aggregated and included later
                tempval = "\"$$$ FBM Purchase to " + tempvalcity + " | " + tempvalstate + "\""

                fieldnameresult = tempval
        case "STX_COMMISSION_FEES":
            fieldnameresult = ""
        case "STX_ADPROMO_COSTS":
            fieldnameresult = ""
        case "STX_IMPORT_ID":
            fieldnameresult = ""
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
                tempval = GenFieldKey_CIQ1.get_to_state(tempval)
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
        case "STX_SHIPPING_PHONE":
            fieldnameresult = ""
        case "STX_EMAIL":
            fieldnameresult = ""
        case "STX_PAY_FROM_MRKT":
            fieldnameresult = ""
        case "STX_PERC_WITHHELD":
            fieldnameresult = ""
        case "STX_SELL_RECOVERY":
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
        case "c":
            fieldnameresult = ""
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
        case "SHIP__COMBINED_SHIPMENT":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__DATA_SOURCE__VEEQO":
            fieldnameresult = "Yes"
        case _:
            if LOCAL_CONSOLE_OUTPUT1:
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

    LOCAL_CONSOLE_OUTPUT1 = False

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
            if LOCAL_CONSOLE_OUTPUT1:
                print("getsecondarylookupvalues run|" + casefieldname)
                print(tempvalid)
            # print("curfilerow|" + str(curfilerow))
            newfilerow = Helpers1.secondarylookupvaluesfromfile(casefieldname, "_Shipment_", curfilerow, tempvalid,
                                                                keyfile, filekey_proc, filekey_lookup)
        case "CONTACT":
            donothing = True
        case _:
            print("Secondary Lookup Value field not found for Switch statement: " + str(casefieldname))

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

    LOCAL_CONSOLE_OUTPUT1 = True

    count = 0

    # ONE: Remove duplicate rows to create list of unique STX's
    newfilerows = [[]]
    lastorderid = ""

    for temprow in filerow:
        if temprow != []:

            tempval = temprow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]
            tempval = sourcestringprocessing(tempval)
            if tempval != lastorderid:
                newfilerows.append(temprow)
            # else:
            #     # print("Row Omitted, {" + str(tempval) + "} duplicate row: " + str(filerow[count]))
            #     print("Row Omitted, {" + str(tempval) + "} duplicate row")
            lastorderid = tempval
        count += 1

    # TWO: Traverse original list to calculate aggregate fields (i.e. transaction total, quantity, numlines, tax, shipp)
    #take in new list
    #for each row in new list, traverse old list
        #for each row in old list, check id match, if match then += cum value
        #when done, put cum value into new list field destination

    for temprow2 in newfilerows:
        # get id in temprow2

        # print("sourcefilekey_processing1:" + str(temprow2))

        if temprow2 == []:
            continue
        lookupid1 = temprow2[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]

        # setup cum values
        cumval_price = 0  # item-price + [ship charges]
        cumval_nettotal = 0  # net order total (sell recovery)
        cumval_subtotal = 0  # item-price
        cumval_quantity = 0  # quantity
        cumval_numlines = 0  # [count number of tx lines]
        cumval_tax1 = 0  # item-tax
        cumval_shippingpaid = 0  # shipping-price
        cumval_shippingtax = 0  # shipping-tax
        cumval_prodcost = 0
        cumval_prodcostcount = 0

        # cumval_price_loc = getsourcefilekeybyvalue("item-price")[1] - 1  # item-price
        # cumval_quantity_loc = getsourcefilekeybyvalue("quantity")[1] - 1  # quantity
        # cumval_numlines_loc = 0  # [count number of tx lines]
        # cumval_tax1_loc = getsourcefilekeybyvalue("item-tax")[1] - 1  # item-tax
        # cumval_shippingpaid_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
        # cumval_shippingtax_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price

        cumval_price_loc = getsourcefilekeybyvalue("item-price")[1] - 1  # item-price
        # cumval_nettotal_loc =
        cumval_quantity_loc = getsourcefilekeybyvalue("quantity")[1] - 1  # quantity
        cumval_numlines_loc = 0  # [count number of tx lines]
        cumval_tax1_loc = getsourcefilekeybyvalue("item-tax")[1] - 1  # item-tax
        cumval_shippingpaid_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
        cumval_shippingtax_loc = getsourcefilekeybyvalue("shipping-tax")[1] - 1  # shipping-price
        cumval_prodcost_loc = getsourcefilekeybyvalue("STX_INITIAL_COST")[1] - 1
        cumval_prodcostcount_loc = getsourcefilekeybyvalue("STX_INITIAL_COST_COUNT")[1] - 1

        cumval_price_txdesc_loc = getsourcefilekeybyvalue("STX_DESC")[1] - 1  # to put order total in description

        cumval_price_loc2 = getsourcefilekeybyvalue("STX_TOTAL")[1] - 1  # item-price
        cumval_subtotal_loc2 = getsourcefilekeybyvalue("SALETX_SUBTOTAL2")[1] - 1  #
        cumval_quantity_loc2 = getsourcefilekeybyvalue("STX_ITEM_QUANTITY")[1] - 1  # quantity
        cumval_numlines_loc2 = getsourcefilekeybyvalue("SALETX___OF_LINES")[1] - 1  # [count number of tx lines]
        cumval_tax1_loc2 = getsourcefilekeybyvalue("STX_TAXES2")[1] - 1  # item-tax
        cumval_shippingpaid_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES")[1] - 1  # shipping-price
        cumval_shippingtax_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES__TAXE")[1] - 1  # shipping-price
        cumval_prodcost_loc2 = getsourcefilekeybyvalue("STX_INITIAL_COST")[1] - 1
        cumval_prodcostcount_loc2 = getsourcefilekeybyvalue("STX_INITIAL_COST_COUNT")[1] - 1

        cumval_nettotal_loc2 = getsourcefilekeybyvalue("STX_SELL_RECOVERY")[1] - 1

        cumval_price_txdesc_loc2 = getsourcefilekeybyvalue("STX_DESC")[1] - 1  # to put order total in description

        for oldtemprow in filerow:
            # check id match to temprow2
            if oldtemprow == []:
                continue
            lookupid2 = oldtemprow[getsourcefilekeybyvalue("amazon-order-id")[1] - 1]

            if lookupid1 == lookupid2:
                cumval_numlines += 1

                # cumval_shippingpaid
                tempval_shippingpaid = oldtemprow[cumval_shippingpaid_loc]
                if tempval_shippingpaid != "":
                    cumval_shippingpaid = cumval_shippingpaid + float(oldtemprow[cumval_shippingpaid_loc])

                # cumval_subtotal
                tempval_subtotal = oldtemprow[cumval_price_loc]
                if tempval_subtotal != "":
                    cumval_subtotal = cumval_subtotal + float(oldtemprow[cumval_price_loc])

                # cumval_price
                if tempval_subtotal == "" or tempval_shippingpaid == "":
                    if tempval_subtotal != "":
                        cumval_price = cumval_price + float(tempval_subtotal)
                    elif tempval_shippingpaid != "":
                        cumval_price = cumval_price + float(tempval_shippingpaid)
                    else:
                        cumval_price = cumval_price + 0
                else:
                    cumval_price = cumval_price + float(tempval_subtotal) + float(tempval_shippingpaid)

                # cumval_quantity
                tempval_quantity = oldtemprow[cumval_quantity_loc]
                if tempval_quantity != "":
                    cumval_quantity = cumval_quantity + float(oldtemprow[cumval_quantity_loc])

                tempval_tax1 = oldtemprow[cumval_tax1_loc]
                if tempval_tax1 != "":
                    cumval_tax1 = cumval_tax1 + float(oldtemprow[cumval_tax1_loc])

                tempval_shippingtax = oldtemprow[cumval_shippingtax_loc]
                if tempval_shippingtax != "":
                    cumval_shippingtax = cumval_shippingtax + float(oldtemprow[cumval_shippingtax_loc])

                tempval_prodcost = oldtemprow[cumval_prodcost_loc]
                if tempval_prodcost != "":
                    cumval_prodcost = cumval_prodcost + float(oldtemprow[cumval_prodcost_loc])

                tempval_prodcostcount = oldtemprow[cumval_prodcostcount_loc]
                if tempval_prodcostcount != "":
                    cumval_prodcostcount = cumval_prodcostcount + float(oldtemprow[cumval_prodcostcount_loc])


            # end for2
        if cumval_numlines > 1:
            # print("Match:" + str(lookupid1) + "|" + str(cumval_numlines) + "|" + str(cumval_price))
            temprow2[cumval_numlines_loc2] = cumval_numlines
            temprow2[cumval_price_loc2] = cumval_price + cumval_tax1 + cumval_shippingtax
            temprow2[cumval_subtotal_loc2] = cumval_subtotal
            temprow2[cumval_quantity_loc2] = cumval_quantity
            temprow2[cumval_tax1_loc2] = cumval_tax1
            temprow2[cumval_shippingpaid_loc2] = cumval_shippingpaid
            temprow2[cumval_shippingtax_loc2] = cumval_shippingtax
            temprow2[cumval_prodcost_loc2] = cumval_prodcost
            temprow2[cumval_prodcostcount_loc2] = cumval_prodcostcount

            cumval_nettotal = cumval_price
            temprow2[cumval_nettotal_loc2] = cumval_nettotal

            tempdesc = temprow2[cumval_price_txdesc_loc2]
            tempdesc = tempdesc.replace("$$$", str("$" + str(round(cumval_price, 2))))
            temprow2[cumval_price_txdesc_loc2] = tempdesc
        else:
            tempdesc = temprow2[cumval_price_txdesc_loc2]
            tempdesc = tempdesc.replace("$$$", str("$" + str(round(cumval_price, 2))))
            temprow2[cumval_price_txdesc_loc2] = tempdesc
        # print("sourcefilekey_processing2:" + str(temprow2))
        # end for1

    netprofit2name = "STX_CALC_ITEM_PROFIT"
    netmargin2name = "SALETX__NET_MARGIN_2"
    roi2name = "STX_LINE_ITEM_ROI"

    netorderttlname = "STX_SELL_RECOVERY"
    numlinesname = "SALETX___OF_LINES"
    itemqname = "STX_ITEM_QUANTITY"
    comfeesname = "STX_COMMISSION_FEES"
    commfescountname = "STX_COMMISSION_FEES_COUNT"
    prodcostname = "STX_INITIAL_COST"
    prodcostcountname = "STX_INITIAL_COST_COUNT"
    shippingcostname = "STX_SHIPPING_COST"
    shippingcostcountname = "STX_SHIPPING_COST_COUNT"

    netprofit1loc = getsourcefilekeybyvalue(netprofit2name)[1] - 1
    netmargin2loc = getsourcefilekeybyvalue(netmargin2name)[1] - 1
    roi2loc = getsourcefilekeybyvalue(roi2name)[1] - 1

    netorderttlloc = getsourcefilekeybyvalue(netorderttlname)[1] - 1
    numlinesloc = getsourcefilekeybyvalue(numlinesname)[1] - 1
    itemqloc = getsourcefilekeybyvalue(itemqname)[1] - 1
    comfeesloc = getsourcefilekeybyvalue(comfeesname)[1] - 1
    commfescountloc = getsourcefilekeybyvalue(commfescountname)[1] - 1
    prodcostloc = getsourcefilekeybyvalue(prodcostname)[1] - 1
    prodcostcountloc = getsourcefilekeybyvalue(prodcostcountname)[1] - 1
    shippingcostloc = getsourcefilekeybyvalue(shippingcostname)[1] - 1
    shippingcostcountloc = getsourcefilekeybyvalue(shippingcostcountname)[1] - 1

    checkfornotempty = [netorderttlloc, comfeesloc, prodcostloc, shippingcostloc]

    tempprofit = 0.0
    tempmargin = 0.0
    temproi = 0.0

    for temprow3 in newfilerows:
        if not temprow3:  # is empty list
            continue

        isemptyvals = False
        for tempval in checkfornotempty:
            if temprow3[tempval] == 0 or temprow3[tempval] == "":
                isemptyvals = True
                break
        if isemptyvals:
            continue
x
        if LOCAL_CONSOLE_OUTPUT1:
            print("temprow3[netorderttlloc]:" + str(temprow3[netorderttlloc]))
            print("temprow3[comfeesloc]:" + str(temprow3[comfeesloc]))
            print("temprow3[prodcostloc]:" + str(temprow3[prodcostloc]))
            print("temprxow3[shippingcostloc]:" + str(temprow3[shippingcostloc]))

        tempprofit = float(temprow3[netorderttlloc]) - abs(float(temprow3[comfeesloc])) - \
            abs(float(temprow3[prodcostloc])) - abs(float(temprow3[shippingcostloc]))
        tempmargin = tempprofit / temprow3[netorderttlloc]
        temproi = (tempprofit + abs(float(temprow3[prodcostloc]))) / abs(float(temprow3[prodcostloc]))
        tempprofit = round(tempprofit, 2)
        tempmargin = round(tempmargin, 4)
        temproi = round(temproi, 4)

        if LOCAL_CONSOLE_OUTPUT1:
            print("tempprofit:" + str(tempprofit))
            print("tempmargin:" + str(tempmargin))
            print("temproi:" + str(temproi))

        if tempprofit > 0.0:
            temprow3[netprofit1loc] = tempprofit
        if tempmargin > 0.0:
            temprow3[netmargin2loc] = tempmargin
        if temproi > 0.0:
            temprow3[roi2loc] = temproi

    return [newfilerows]


def sourcestringprocessing(tempstring):

    newstring = tempstring

    # newstring = str(newstring).replace("\\", "")
    # newstring = str(newstring).replace("\'", "")
    # newstring = str(newstring).replace("\"", "")

    return newstring


def getsecondaryagglookupvalues(casefieldname, curfilerow, keyfile, filekey_proc, filekey_lookup, firstfile):

    LOCAL_CONSOLE_OUTPUT1 = False

    newfilerow = ""
    fieldnameresult = ""

    match casefieldname:
        case "STX_SHIPPING_COST":
            tempvalid = curfilerow[getsourcefilekeybyvalue("STX_SHIPPING_COST")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            if LOCAL_CONSOLE_OUTPUT1:
                print("getsecondarylookupvalues run|" + casefieldname)
                print(tempvalid)
            # print("curfilerow|" + str(curfilerow))

            # secondaryagglookupvaluesfromfile(casefieldname, lookupfilenamekeywordpair, curfilerow, tempvalid, keyfile, filekey_proc, filekey_lookup):
            #  lookupfilenamekeywordpair = [lookup file type, [[SRC column for match, LU column to look for match, LU column to pull value, SRC column to insert result]]]
            newfilerow = Helpers1.secondaryagglookupvaluesfromfile(casefieldname,
                                                                   ["_Shipment_",
                                                                    [["amazon-order-id", "SHIP Order ID",
                                                                      "SHIP Rate/Ship Charge - Base",
                                                                     "STX_SHIPPING_COST"]]], curfilerow, tempvalid,
                                                                   keyfile, filekey_proc, filekey_lookup)
            tempshipcostloc = sourcefilekey1["STX_SHIPPING_COST"][1] - 1
            if newfilerow[tempshipcostloc] != "":
                newfilerow[tempshipcostloc] = -1 * float(newfilerow[tempshipcostloc])
        case "STX_INITIAL_COST":
            tempvalid = curfilerow[getsourcefilekeybyvalue("STX_INITIAL_COST")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            if LOCAL_CONSOLE_OUTPUT1:
                print("getsecondarylookupvalues run|" + casefieldname)
                print(tempvalid)
            # print("curfilerow|" + str(curfilerow))
            # newfilerow = Helpers1.secondaryagglookupvaluesfromfile_product(casefieldname,
            #                                                        ["MII-MCC",
            #                                                         [["sku", "MII Inventory Master Item",
            #                                                           "Ops Mgt Cost",
            #                                                           "STX_INITIAL_COST"]]], curfilerow, tempvalid,
            #                                                        keyfile, filekey_proc, filekey_lookup)
            # [SRC|Listing ID, SRC|Quantity, LKUP|Listing ID, LKUP|Cost, SRC|Destination Field]
            newfilerow = Helpers1.secondaryagglookupvaluesfromfile_product(casefieldname,
                                                                            ["sku", "quantity",
                                                                              "LST Channel SKU", "MCC Master Cost - Current, for Cost/COGS",
                                                                             "LSTN Number of Items",
                                                                              "STX_INITIAL_COST"], curfilerow,
                                                                           tempvalid,
                                                                           keyfile, filekey_proc, filekey_lookup, firstfile)
            tempproductcostloc = sourcefilekey1["STX_INITIAL_COST"][1] - 1
            if newfilerow[tempproductcostloc] != "":
                newfilerow[tempproductcostloc] = -1 * float(newfilerow[tempproductcostloc])
        case "STX_COMMISSION_FEES":
            tempvalid = curfilerow[getsourcefilekeybyvalue("STX_COMMISSION_FEES")[1] - 1]
            # tempvalloc = getsourcefilekeybyvalue("SHIPMENT")[1] - 1
            fieldnameresult = 1
            # tempval = ((tempval).replace("\'", ""))
            # tempval = ((tempval).replace("[", ""))
            # # print(str(tempval))
            # tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
            # fieldnameresult = tempdate.strftime("%m/%d/%Y")
            # # print(str(fieldnameresult))
            if LOCAL_CONSOLE_OUTPUT1:
                print("getsecondarylookupvalues run|" + casefieldname)
                print(tempvalid)
            # print("curfilerow|" + str(curfilerow))

            # secondaryagglookupvaluesfromfile(casefieldname, lookupfilenamekeywordpair, curfilerow, tempvalid, keyfile, filekey_proc, filekey_lookup):
            #  lookupfilenamekeywordpair = [lookup file type, [[SRC column for match, LU column to look for match, LU column to pull value, SRC column to insert result]]]
            newfilerow = Helpers1.secondaryagglookupvaluesfromfile_UTR(casefieldname,
                                                                       ["SFE-Amazon-UTR",
                                                                        ["STX_NAME", "order id",
                                                                          "selling fees", "fba fees",
                                                                          "other transaction fees",
                                                                          "total", "STX_COMMISSION_FEES"]], curfilerow,
                                                                       tempvalid, keyfile, filekey_proc, filekey_lookup,
                                                                       firstfile)
        case _:
            print("Secondary Lookup Value field not found for Switch statement: " + str(casefieldname))
            return curfilerow



    return newfilerow



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
    "getsecondaryagglookupvalues": [getsecondaryagglookupvalues],
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
    # "specialfunctions1": False,
    "processfilenextrow": True,
    "processcalculatedrows": True,
    "processtranslatedrows": True,
    "getsecondarylookupvalues": True,
    "getsecondaryagglookupvalues": True,
    "getsecondaryagglookupvalues_UTR": True,
    "finalerrorcheck": True,
    "pushfinalerrormessage": True,
    "ciqidlookupadd": True,
    "ciqsearchlookupfile": False,
    "buildcombinedshipmentslist": False,
    "markcombinedshipments": False,
    "sourcefilekey_processing": True,
    "general_post_processing": True,
    "write_row_list_to_files": True,
    "filecleanup": True,



}
