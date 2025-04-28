import GenFieldKey_CIQ1
import math
import os
from datetime import datetime
import Helpers1
import random

# [pos in input file,pos in output file,2=transl'd field|1=cal'dfield|0=inputfilefield,header/field name,output header/field name]
# sourcefilekey1 = {
#         "Shipment_XITOR_KEY": [None, 1, 1, "Shipment_XITOR_KEY"],
#         "SHIP_GEN_SERVICE": [None, 2, 2, "SHIP_GEN_SERVICE"],
#         "Shipment Type": [1, 3, 0],
#         "Shipment Service": [4, 4, 0],
#         "Shipment Shipping Account": [3, 5, 0],
#         "Shipment Carrier Charges": [13, 6, 0],
#         "Shipment Carrier": [2, 7, 0],
#         "Shipment_XITOR_KEY2": [None, 8, 1, "Shipment_XITOR_KEY2"]
#     }

# SOURCE_ID_REF_FOR_LOOKUP = "SHIP_GEN_TRACK_NUM"
SOURCE_ID_REF_FOR_LOOKUP = "Shipment Tracking Number"
RANDOM_RUN_ID = "-1"
OUTPUT_FILE_KEYWORD_1 = "ShipRush"
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
    "SHIP__DATA_SOURCE__SHIPRUSH": [None, 32, 1, "SHIP__DATA_SOURCE__SHIPRUSH", "SHIP__DATA_SOURCE__SHIPRUSH", ""],
    "Shipment Type": [1, 33, 0, "Shipment Type", "ship_sr_type", ""],
    "Shipment Carrier": [2, 34, 0, "Shipment Carrier", "ship_sr_carrier", ""],
    "Shipment Shipping Account": [3, 35, 0, "Shipment Shipping Account", "ship_sr_acct", ""],
    "Shipment Service": [4, 36, 0, "Shipment Service", "ship_sr_service", ""],
    "Shipment Date": [5, 37, 0, "Shipment Date", "SHIP_SR_DATE2", ""],
    "Shipment Tracking Number": [6, 38, 0, "Shipment Tracking Number", "ship_sr_track_num", "||"],
    "Shipment Alt. Tracking Number": [7, 39, 0, "Shipment Alt. Tracking Number", "ship_sr_alt_track_num", ""],
    "Shipment Shipping Charges": [8, 40, 0, "Shipment Shipping Charges", "ship_sr_chrg", ""],
    "Shipment Surcharges": [9, 41, 0, "Shipment Surcharges", "ship_sr_surchrg", ""],
    "Shipment Declared Value Rate": [10, 42, 0, "Shipment Declared Value Rate", "ship_sr_decl_val_rate", ""],
    "Shipment Declared Value Charges": [11, 43, 0, "Shipment Declared Value Charges", "ship_sr_decl_val_chrg", ""],
    "Shipment ClearPath Charges": [12, 44, 0, "Shipment ClearPath Charges", "ship_sr_clearpath_chrg", ""],
    "Shipment Carrier Charges": [13, 45, 0, "Shipment Carrier Charges", "ship_sr_carrier_chrg", ""],
    "Shipment Frieght Charges": [14, 46, 0, "Shipment Frieght Charges", "ship_sr_frieght_chrg", ""],
    "Shipment Return Type": [15, 47, 0, "Shipment Return Type", "ship_sr_return_type", ""],
    "Package Weight": [16, 48, 0, "Package Weight", "ship_sr_pkg_wt", ""],
    "Package Reference": [17, 49, 0, "Package Reference", "ship_sr_pkg_ref", ""],
    "Package Reference 2": [18, 50, 0, "Package Reference 2", "ship_sr_pkg_ref_2", ""],
    "Package Reference 3": [19, 51, 0, "Package Reference 3", "ship_sr_pkg_ref_3", ""],
    "Package Reference 4": [20, 52, 0, "Package Reference 4", "ship_sr_pkg_ref_4", ""],
    "Package Reference 5": [21, 53, 0, "Package Reference 5", "SHIP_SR_PKG_REF_5", ""],
    "Package DeliveryConfirmation": [22, 54, 0, "Package DeliveryConfirmation", "ship_sr_pkg_delconf", ""],
    "Package COD Type": [23, 55, 0, "Package COD Type", "ship_sr_pkg_cod_type", ""],
    "Package COD Funds": [24, 56, 0, "Package COD Funds", "ship_sr_pkg_cod_funds", ""],
    "Package COD Amount": [25, 57, 0, "Package COD Amount", "ship_sr_pkg_cod_amt", ""],
    "Package Declared Value Amount": [26, 58, 0, "Package Declared Value Amount", "ship_sr_pkg_decval_amt", ""],
    "Package Declared Value Currency": [27, 59, 0, "Package Declared Value Currency", "ship_sr_pkg_decval_cur", ""],
    "Package Size Length": [28, 60, 0, "Package Size Length", "ship_sr_pkg_size_l", ""],
    "Package Size Width": [29, 61, 0, "Package Size Width", "ship_sr_pkg_size_w", ""],
    "Package Size Height": [30, 62, 0, "Package Size Height", "ship_sr_pkg_size_h", ""],
    "Package Packaging Type": [31, 63, 0, "Package Packaging Type", "ship_sr_pkg_pkg_type", ""],
    "Package Additional Handling": [32, 64, 0, "Package Additional Handling", "ship_sr_pkg_addnl_hndl", ""],
    "Package NonStandard Container": [33, 65, 0, "Package NonStandard Container", "ship_sr_pkg_nst_cntnr", ""],
    "Package Alcohol": [34, 66, 0, "Package Alcohol", "ship_sr_pkg_alcohol", ""],
    "Package Dangerous Goods": [35, 67, 0, "Package Dangerous Goods", "ship_sr_pkg_dngrs_good", ""],
    "Order Date": [36, 68, 0, "Order Date", "ship_sr_ord_date", ""],
    "Order Number": [37, 69, 0, "Order Number", "ship_sr_ord_num", "||"],
    "Order Internal Order ID": [38, 70, 0, "Order Internal Order ID", "ship_sr_ord_int_ord_id", ""],
    "Order External Order ID": [39, 71, 0, "Order External Order ID", "ship_sr_ord_ext_ord_id", ""],
    "Order Subtotal": [40, 72, 0, "Order Subtotal", "ship_sr_ord_subtotal", ""],
    "Order Tax": [41, 73, 0, "Order Tax", "ship_sr_ord_tax", ""],
    "Order Shipping Paid": [42, 74, 0, "Order Shipping Paid", "ship_sr_ord_paid", ""],
    "Order Total": [43, 75, 0, "Order Total", "ship_sr_ord_total", ""],
    "Order Comments": [44, 76, 0, "Order Comments", "ship_sr_ord_comments", ""],
    "Order Webstore Name": [45, 77, 0, "Order Webstore Name", "ship_sr_ord_store_name", ""],
    "Order Tags": [46, 78, 0, "Order Tags", "ship_sr_ord_tags", ""],
    "Ship To Company": [47, 79, 0, "Ship To Company", "ship_sr_to_company", ""],
    "Ship To FirstName": [48, 80, 0, "Ship To FirstName", "ship_sr_to_firstname", ""],
    "Ship To LastName": [49, 81, 0, "Ship To LastName", "ship_sr_to_lastname", ""],
    "Ship To Address1": [50, 82, 0, "Ship To Address1", "ship_sr_to_address1", ""],
    "Ship To Address2": [51, 83, 0, "Ship To Address2", "ship_sr_to_address2", ""],
    "Ship To City": [52, 84, 0, "Ship To City", "ship_sr_to_city", ""],
    "Ship To State": [53, 85, 0, "Ship To State", "ship_sr_to_state", ""],
    "Ship To PostalCode": [54, 86, 0, "Ship To PostalCode", "ship_sr_to_postalcode", "||"],
    "Ship To Phone": [55, 87, 0, "Ship To Phone", "ship_sr_to_phone", "||"],
    "Ship To EMail": [56, 88, 0, "Ship To EMail", "ship_sr_to_email", ""],
    "Ship From Company": [57, 89, 0, "Ship From Company", "ship_sr_from_company", ""],
    "Ship From FirstName": [58, 90, 0, "Ship From FirstName", "ship_sr_from_firstname", ""],
    "Ship From LastName": [59, 91, 0, "Ship From LastName", "ship_sr_from_lastname", ""],
    "Ship From Address1": [60, 92, 0, "Ship From Address1", "ship_sr_from_address1", ""],
    "Ship From Address2": [61, 93, 0, "Ship From Address2", "ship_sr_from_address2", ""],
    "Ship From City": [62, 94, 0, "Ship From City", "ship_sr_from_city", ""],
    "Ship From State": [63, 95, 0, "Ship From State", "ship_sr_from_state", ""],
    "Ship From PostalCode": [64, 96, 0, "Ship From PostalCode", "ship_sr_from_pstlcode", "||"],
    "Ship To Country": [65, 97, 0, "Ship To Country", "ship_sr_to_country", ""],
    "Ship From Phone": [66, 98, 0, "Ship From Phone", "ship_sr_from_phone", "||"],
    "Ship From EMail": [67, 99, 0, "Ship From EMail", "ship_sr_from_email", ""],
    "Shipper Account Used": [68, 100, 0, "Shipper Account Used", "ship_sr_ship_acct_used", ""],

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
    retkey = sourcefilekey1["Shipment Tracking Number"][1]
    return retkey


def getcolplacement_combinedflag():
    retkey = sourcefilekey1["SHIP__COMBINED_SHIPMENT"][1]
    return retkey


def getcalcfieldvalues(casefieldname, newfilerow):

    fieldnameresult = ""

    #print(newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1])
    checkval = newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1]-1]
    checkval = str(checkval).replace("$", "")
    checkval = float((checkval).replace("\'", ""))
    # print(checkval)
    checkvalexists = False
    if isinstance(checkval, float) and checkval != 0:
        checkvalexists = True

    match casefieldname:
        case "Shipment_XITOR_KEY":
            fieldnameresult = ""

        case "SHIP_HAS_DATA_ISSUE":
            fieldnameresult = ""

        case "SHIP_DATA_ISSUE_NOTES":
            fieldnameresult = ""

        case "SHIP_GEN_SERVICE":
            if checkvalexists:
                fieldnameresult = "ShipRush"

        case "SHIP_GEN_CREATE_DATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Date")[1]-1]
                fieldnameresult = tempval

        case "SHIP_GEN_CARRIER":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier(tempval)

        case "SHIP_GEN_CRR_SRV_DD":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Service")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_carrier_dd(tempval)

        case "SHIP_GEN_OWN_COMP":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Order Webstore Name")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_own_comp(tempval)
        case "SHIP_GEN_CHANNEL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Order Webstore Name")[1] - 1]
                fieldnameresult = GenFieldKey_CIQ1.get_gen_channel(tempval)
        case "SHIP_RATE_SHIP_CHRG":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__BASE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_RATESHIP_CHARGE__ORIGINAL":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Carrier Charges")[1] - 1]
                fieldnameresult = tempval
        case "SHIP_PKG_FULL_DIMS":
            if checkvalexists:
                tempval_length = newfilerow[getsourcefilekeybyvalue("Package Size Length")[1] - 1]
                tempval_width = newfilerow[getsourcefilekeybyvalue("Package Size Width")[1] - 1]
                tempval_height = newfilerow[getsourcefilekeybyvalue("Package Size Height")[1] - 1]
                tempval_final = str(tempval_length) + "x" + str(tempval_width) + "x" + str(tempval_height)
                fieldnameresult = tempval_final

        case "SHIP_GEN_PKG_LENGTH":
            if checkvalexists:
                tempval_length = newfilerow[getsourcefilekeybyvalue("Package Size Length")[1] - 1]
                fieldnameresult = tempval_length
        case "SHIP_GEN_PKG_WIDTH":
            if checkvalexists:
                tempval_width = newfilerow[getsourcefilekeybyvalue("Package Size Width")[1] - 1]
                fieldnameresult = tempval_width
        case "SHIP_GEN_PKG_HEIGHT":
            if checkvalexists:
                tempval_height = newfilerow[getsourcefilekeybyvalue("Package Size Height")[1] - 1]
                fieldnameresult = tempval_height
        case "SHIP_GEN_PKG_WEIGHT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Package Weight")[1] - 1]
                tempval = float(tempval.replace("\'", ""))
                fieldnameresult = str(round(float(tempval), 4))
        case "SHIP_PKG_WEIGHT_OUNCES":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Package Weight")[1] - 1]
                tempval = float(tempval.replace("\'", ""))
                fieldnameresult = str(round(float(tempval) * 16, 4))
        case "SHIP_PKG_WEIGHT_TEXT":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Package Weight")[1] - 1]
                tempval = float((tempval).replace("\'", ""))
                tempvalstr = ""
                if float(tempval) > 1:
                    tempvalstr = str(math.floor(float(tempval))) + " lbs " + str(round((float(tempval) - math.floor(float(tempval)))*16, 4)) + " oz"
                else:
                    tempvalstr = str(round(float(tempval) * 16, 4)) + " oz"
                fieldnameresult = tempvalstr
        case "SHIP_GEN_ORDER_ID":
            # if checkvalexists:
            tempval = newfilerow[getsourcefilekeybyvalue("Order Number")[1] - 1]
            fieldnameresult = str(getsourcefilekeybyvalue("Order Number")[5]) + tempval
        case "SHIP_GEN_ORDER_ID_2":
            fieldnameresult = ""
        case "SHIP_GEN_TRACK_NUM":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Shipment Tracking Number")[1] - 1]
                fieldnameresult = str(getsourcefilekeybyvalue("Order Number")[5]) + tempval
        case "SHIP_GEN_TO_STATE":
            if checkvalexists:
                tempval = newfilerow[getsourcefilekeybyvalue("Ship To State")[1] - 1]
                tempval = (tempval).replace("\'", "")
                fieldnameresult = GenFieldKey_CIQ1.get_to_state(tempval)
        case "SHIP_GEN_FULL_NAME__SHIP_TO":
            if checkvalexists:
                tempval_firstname = newfilerow[getsourcefilekeybyvalue("Ship To FirstName")[1] - 1]
                tempval_lastname = newfilerow[getsourcefilekeybyvalue("Ship To LastName")[1] - 1]
                fieldnameresult = tempval_firstname + " " + tempval_lastname
        case "SHIP_INCOMINGOUTGOING":
            if checkvalexists:
                fieldnameresult = "Outgoing"
        case "SHIP_DELIVERY_STATUS":
            if checkvalexists:
                fieldnameresult = "New"
        case "SHIP_SECONDARY_TRACKING_NUMBER":
            if checkvalexists:
                fieldnameresult = ""
        case "SHIP__IS_PHASE_2_RECORD":
            fieldnameresult = "YES"
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
        case "SHIP__DATA_SOURCE__SHIPRUSH":
            fieldnameresult = "YES"
        case _:
            print("Calc'd field not found for Switch statement: " + str(casefieldname))



    return fieldnameresult


def gettranslatedfieldvalues(casefieldname, newfilerow):
    print("run")
    fieldnameresult = ""

    match casefieldname:
        # case "Shipped Date":
        #     tempval = newfilerow[getsourcefilekeybyvalue("Shipped Date")[1] - 1]
        #     tempval = ((tempval).replace("\'", ""))
        #     tempval = ((tempval).replace("[", ""))
        #     # print(str(tempval))
        #     tempdate = datetime.strptime(tempval, "%Y-%m-%d %H:%M:%S")
        #     fieldnameresult = tempdate.strftime("%m/%d/%Y")
        #     print(str(fieldnameresult))
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


#takes in one row string - final processing before writing to file
def sourcefilekey_processing_string(filerowstr):

    # filerowstr = str(filerowstr).replace("\\", "")

    return filerowstr


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
    "sourcefilekey_processing_string": [sourcefilekey_processing_string],
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
