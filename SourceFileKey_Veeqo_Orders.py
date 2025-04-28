import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import random

# File Name: SourceFileKey_Veeqo_Orders

# SOURCE_ID_REF_FOR_LOOKUP = "Order ID"
SOURCE_ID_REF_FOR_LOOKUP = "SaleTx_XITOR_KEY"
RANDOM_RUN_ID = "-1"
RANDOM_RUN_ID_STR = "STX_IMP-"
OUTPUT_FILE_KEYWORD_1 = "Veeqo-Orders-STX"
MAIN_XITOR_LOOKUP_TYPE = "_SaleTx_"  # Keyword in CIQ export file for lookup


def getfunctionkey():

    return functionkey1


def getfunctionkey_processing():

    return functionkey_processing


sourcefilekey1 = {
    "SaleTx_XITOR_KEY": [None, 1, -1, "SaleTx_XITOR_KEY", "SaleTx_XITOR_KEY", ""],
    "STX_HAS_DATA_ISSUE": [None, 2, 1, "STX_HAS_DATA_ISSUE", "STX_HAS_DATA_ISSUE", ""],
    "STX_DATA_ISSUE_NOTES": [None, 3, 1, "STX_DATA_ISSUE_NOTES", "STX_DATA_ISSUE_NOTES", ""],
    "x:id": [None, 4, 1, "x:id", "x:id", ""],
    "x:number": [None, 5, 1, "x:number", "x:number", ""],
    "x:total_price": [None, 6, 1, "x:total_price", "x:total_price", ""],
    "x:subtotal_price": [None, 7, 1, "x:subtotal_price", "x:subtotal_price", ""],
    "x:delivery_cost": [None, 8, 1, "x:delivery_cost", "x:delivery_cost", ""],
    "x:created_at": [None, 9, 1, "x:created_at", "x:created_at", ""],
    "x:channel": [None, 10, 1, "x:channel", "x:channel", ""],
    "x:billing_address_first_name": [None, 11, 1, "x:billing_address_first_name", "x:billing_address_first_name", ""],
    "x:billing_address_last_name": [None, 12, 1, "x:billing_address_last_name", "x:billing_address_last_name", ""],
    "x:shipping_address_first_name": [None, 13, 1, "x:shipping_address_first_name", "x:shipping_address_first_name",
                                      ""],
    "x:shipping_address_last_name": [None, 14, 1, "x:shipping_address_last_name", "x:shipping_address_last_name", ""],
    "x:shipping_address_city": [None, 15, 1, "x:shipping_address_city", "x:shipping_address_city", ""],
    "x:shipping_address_state": [None, 16, 1, "x:shipping_address_state", "x:shipping_address_state", ""],
    "x:shipping_address_zip": [None, 17, 1, "x:shipping_address_zip", "x:shipping_address_zip", ""],
    "x:sku": [None, 18, 1, "x:sku", "x:sku", ""],
    "x:quantity": [None, 19, 1, "x:quantity", "x:quantity", ""],
    "x:price_per_unit": [None, 20, 1, "x:price_per_unit", "x:price_per_unit", ""],
    "x:product_title": [None, 21, 1, "x:product_title", "x:product_title", ""],
    "STX_INITIAL_COST": [None, 22, 4, "STX_INITIAL_COST", "STX_INITIAL_COST", ""],
    "STX_INITIAL_COST_COUNT": [None, 23, 1, "STX_INITIAL_COST_COUNT", "STX_INITIAL_COST_COUNT", ""],
    "STX_CREATED_AT": [None, 24, 1, "STX_CREATED_AT", "STX_CREATED_AT", ""],
    "STX_UPDATED_AT": [None, 25, 1, "STX_UPDATED_AT", "STX_UPDATED_AT", ""],
    "id": [1, 26, 0, "id", "id", ""],
    "number": [2, 27, 0, "number", "number", ""],
    "receipt_printed": [3, 28, 0, "receipt_printed", "receipt_printed", ""],
    "status": [4, 29, 0, "status", "status", ""],
    "total_price": [5, 30, 0, "total_price", "total_price", ""],
    "marketplace_fees": [6, 31, 0, "marketplace_fees", "marketplace_fees", ""],
    "gross_profit_value": [7, 32, 0, "gross_profit_value", "gross_profit_value", ""],
    "gross_profit_percent": [8, 33, 0, "gross_profit_percent", "gross_profit_percent", ""],
    "cost_price": [9, 34, 0, "cost_price", "cost_price", ""],
    "cost_of_goods": [10, 35, 0, "cost_of_goods", "cost_of_goods", ""],
    "subtotal_price": [11, 36, 0, "subtotal_price", "subtotal_price", ""],
    "total_tax": [12, 37, 0, "total_tax", "total_tax", ""],
    "delivery_cost": [13, 38, 0, "delivery_cost", "delivery_cost", ""],
    "total_discounts": [14, 39, 0, "total_discounts", "total_discounts", ""],
    "total_discounts_legacy": [15, 40, 0, "total_discounts_legacy", "total_discounts_legacy", ""],
    "shipping_discount": [16, 41, 0, "shipping_discount", "shipping_discount", ""],
    "additional_order_level_taxless_discount": [17, 42, 0, "additional_order_level_taxless_discount",
                                                "additional_order_level_taxless_discount", ""],
    "taxless_discount_per_unit": [18, 43, 0, "taxless_discount_per_unit", "taxless_discount_per_unit", ""],
    "created_at": [19, 44, 0, "created_at", "created_at", ""],
    "delivery_method": [20, 45, 0, "delivery_method", "delivery_method", ""],
    "payment_type": [21, 46, 0, "payment_type", "payment_type", ""],
    "payment_created_at": [22, 47, 0, "payment_created_at", "payment_created_at", ""],
    "shipped_at": [23, 48, 0, "shipped_at", "shipped_at", ""],
    "cancelled_at": [24, 49, 0, "cancelled_at", "cancelled_at", ""],
    "cancel_reason": [25, 50, 0, "cancel_reason", "cancel_reason", ""],
    "notes": [26, 51, 0, "notes", "notes", ""],
    "customer_note": [27, 52, 0, "customer_note", "customer_note", ""],
    "channel_type": [28, 53, 0, "channel_type", "channel_type", ""],
    "channel": [29, 54, 0, "channel", "channel", ""],
    "channel_id": [30, 55, 0, "channel_id", "channel_id", ""],
    "customer_email": [31, 56, 0, "customer_email", "customer_email", ""],
    "customer_phone": [32, 57, 0, "customer_phone", "customer_phone", ""],
    "customer_mobile": [33, 58, 0, "customer_mobile", "customer_mobile", ""],
    "customer_remote_id": [34, 59, 0, "customer_remote_id", "customer_remote_id", ""],
    "billing_address_first_name": [35, 60, 0, "billing_address_first_name", "billing_address_first_name", ""],
    "billing_address_last_name": [36, 61, 0, "billing_address_last_name", "billing_address_last_name", ""],
    "billing_address_company": [37, 62, 0, "billing_address_company", "billing_address_company", ""],
    "billing_address_address1": [38, 63, 0, "billing_address_address1", "billing_address_address1", ""],
    "billing_address_address2": [39, 64, 0, "billing_address_address2", "billing_address_address2", ""],
    "billing_address_city": [40, 65, 0, "billing_address_city", "billing_address_city", ""],
    "billing_address_country": [41, 66, 0, "billing_address_country", "billing_address_country", ""],
    "billing_address_state": [42, 67, 0, "billing_address_state", "billing_address_state", ""],
    "billing_address_zip": [43, 68, 0, "billing_address_zip", "billing_address_zip", ""],
    "billing_address_phone": [44, 69, 0, "billing_address_phone", "billing_address_phone", ""],
    "shipping_address_first_name": [45, 70, 0, "shipping_address_first_name", "shipping_address_first_name", ""],
    "shipping_address_last_name": [46, 71, 0, "shipping_address_last_name", "shipping_address_last_name", ""],
    "shipping_address_company": [47, 72, 0, "shipping_address_company", "shipping_address_company", ""],
    "shipping_address_address1": [48, 73, 0, "shipping_address_address1", "shipping_address_address1", ""],
    "shipping_address_address2": [49, 74, 0, "shipping_address_address2", "shipping_address_address2", ""],
    "shipping_address_city": [50, 75, 0, "shipping_address_city", "shipping_address_city", ""],
    "shipping_address_country": [51, 76, 0, "shipping_address_country", "shipping_address_country", ""],
    "shipping_address_state": [52, 77, 0, "shipping_address_state", "shipping_address_state", ""],
    "shipping_address_zip": [53, 78, 0, "shipping_address_zip", "shipping_address_zip", ""],
    "number_of_lines": [54, 79, 0, "number_of_lines", "number_of_lines", ""],
    "sku": [55, 80, 0, "sku", "sku", ""],
    "upc": [56, 81, 0, "upc", "upc", ""],
    "quantity": [57, 82, 0, "quantity", "quantity", ""],
    "quantity_shipped": [58, 83, 0, "quantity_shipped", "quantity_shipped", ""],
    "price_per_unit": [59, 84, 0, "price_per_unit", "price_per_unit", ""],
    "price_per_unit_including_tax": [60, 85, 0, "price_per_unit_including_tax", "price_per_unit_including_tax", ""],
    "product_title": [61, 86, 0, "product_title", "product_title", ""],
    "variant_title": [62, 87, 0, "variant_title", "variant_title", ""],
    "order_remote_id": [63, 88, 0, "order_remote_id", "order_remote_id", ""],
    "additional_options": [64, 89, 0, "additional_options", "additional_options", ""],
    "variant_weight": [65, 90, 0, "variant_weight", "variant_weight", ""],
    "tracking_number": [66, 91, 0, "tracking_number", "tracking_number", ""],
    "due_date": [67, 92, 0, "due_date", "due_date", ""],
    "tags": [68, 93, 0, "tags", "tags", ""],
    "hazmat": [69, 94, 0, "hazmat", "hazmat", ""],

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
        case "x:id":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("id")[1] - 1]
                fieldnameresult = tempval
        case "x:number":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("number")[1] - 1]
                fieldnameresult = tempval
        case "x:total_price":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("total_price")[1] - 1]
                fieldnameresult = tempval
        case "x:subtotal_price":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("subtotal_price")[1] - 1]
                fieldnameresult = tempval
        case "x:delivery_cost":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("delivery_cost")[1] - 1]
                fieldnameresult = tempval
        case "x:created_at":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("created_at")[1] - 1]
                fieldnameresult = tempval
        case "x:channel":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("channel")[1] - 1]
                fieldnameresult = tempval
        case "x:billing_address_first_name":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("billing_address_first_name")[1] - 1]
                fieldnameresult = tempval
        case "x:billing_address_last_name":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("billing_address_last_name")[1] - 1]
                fieldnameresult = tempval
        case "x:shipping_address_first_name":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping_address_first_name")[1] - 1]
                fieldnameresult = tempval
        case "x:shipping_address_last_name":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping_address_last_name")[1] - 1]
                fieldnameresult = tempval
        case "x:shipping_address_city":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping_address_city")[1] - 1]
                fieldnameresult = tempval
        case "x:shipping_address_state":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping_address_state")[1] - 1]
                fieldnameresult = tempval
        case "x:shipping_address_zip":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("shipping_address_zip")[1] - 1]
                fieldnameresult = tempval
        case "x:sku":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("sku")[1] - 1]
                fieldnameresult = tempval
        case "x:quantity":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("quantity")[1] - 1]
                fieldnameresult = tempval
        case "x:price_per_unit":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("price_per_unit")[1] - 1]
                fieldnameresult = tempval
        case "x:product_title":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("product_title")[1] - 1]
                fieldnameresult = tempval

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
                if tempval_base == "" or tempval_ship == "":
                    if tempval_base != "":
                        tempval = float(tempval_base)
                    elif tempval_ship != "":
                        tempval = float(tempval_ship)
                    else:
                        tempval = 0
                else:
                    tempval = float(tempval_base) + float(tempval_ship)
                fieldnameresult = tempval
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
        case "STX_TAXES":
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

                tempval = "\"$" + tempvalttl + " FBM Purchase to " + tempvalcity + " | " + tempvalstate + "\""

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
        # case "SHIP_SYSTEM_UPDATED_DATE":
        #     if checkvalexists:
        #         fieldnameresult = ""
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
            # print("curfilerow|" + str(curfilerow))
            newfilerow = Helpers1.secondarylookupvaluesfromfile(casefieldname, "_Shipment_", curfilerow, tempvalid,
                                                                keyfile, filekey_proc, filekey_lookup)
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
        cumval_quantity_loc = getsourcefilekeybyvalue("quantity")[1] - 1  # quantity
        cumval_numlines_loc = 0  # [count number of tx lines]
        cumval_tax1_loc = getsourcefilekeybyvalue("item-tax")[1] - 1  # item-tax
        cumval_shippingpaid_loc = getsourcefilekeybyvalue("shipping-price")[1] - 1  # shipping-price
        cumval_shippingtax_loc = getsourcefilekeybyvalue("shipping-tax")[1] - 1  # shipping-price
        cumval_prodcost_loc = getsourcefilekeybyvalue("STX_INITIAL_COST")[1] - 1
        cumval_prodcostcount_loc = getsourcefilekeybyvalue("STX_INITIAL_COST_COUNT")[1] - 1

        cumval_price_loc2 = getsourcefilekeybyvalue("STX_TOTAL")[1] - 1  # item-price
        cumval_subtotal_loc2 = getsourcefilekeybyvalue("SALETX_SUBTOTAL2")[1] - 1  #
        cumval_quantity_loc2 = getsourcefilekeybyvalue("STX_ITEM_QUANTITY")[1] - 1  # quantity
        cumval_numlines_loc2 = getsourcefilekeybyvalue("SALETX___OF_LINES")[1] - 1  # [count number of tx lines]
        cumval_tax1_loc2 = getsourcefilekeybyvalue("STX_TAXES")[1] - 1  # item-tax
        cumval_shippingpaid_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES")[1] - 1  # shipping-price
        cumval_shippingtax_loc2 = getsourcefilekeybyvalue("SALETX__SHIPPING_CHARGES__TAXE")[1] - 1  # shipping-price
        cumval_prodcost_loc2 = getsourcefilekeybyvalue("STX_INITIAL_COST")[1] - 1
        cumval_prodcostcount_loc2 = getsourcefilekeybyvalue("STX_INITIAL_COST_COUNT")[1] - 1

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
            temprow2[cumval_price_loc2] = cumval_price
            temprow2[cumval_subtotal_loc2] = cumval_subtotal
            temprow2[cumval_quantity_loc2] = cumval_quantity
            temprow2[cumval_tax1_loc2] = cumval_tax1
            temprow2[cumval_shippingpaid_loc2] = cumval_shippingpaid
            temprow2[cumval_shippingtax_loc2] = cumval_shippingtax
            temprow2[cumval_prodcost_loc2] = cumval_prodcost
            temprow2[cumval_prodcostcount_loc2] = cumval_prodcostcount
        # print("sourcefilekey_processing2:" + str(temprow2))
        # end for1


    return [newfilerows]


def sourcestringprocessing(tempstring):

    newstring = tempstring

    # newstring = str(newstring).replace("\\", "")
    # newstring = str(newstring).replace("\'", "")
    # newstring = str(newstring).replace("\"", "")

    return newstring


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


def getsecondaryagglookupvalues(casefieldname, curfilerow, keyfile, filekey_proc, filekey_lookup):

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
                                                                           keyfile, filekey_proc, filekey_lookup)
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
                                                                       tempvalid, keyfile, filekey_proc, filekey_lookup)
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
    "sourcefilekey_processing_string": [sourcefilekey_processing_string],
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
    "processtranslatedrows": True,
    "getsecondarylookupvalues": False,
    "getsecondaryagglookupvalues": True,
    "getsecondaryagglookupvalues_UTR": False,
    "finalerrorcheck": True,
    "pushfinalerrormessage": True,
    "ciqidlookupadd": False,
    "ciqsearchlookupfile": False,
    "buildcombinedshipmentslist": False,
    "markcombinedshipments": False,
    "sourcefilekey_processing": False,
    "general_post_processing": False,
    "write_row_list_to_files": True,
    "filecleanup": True,



}
