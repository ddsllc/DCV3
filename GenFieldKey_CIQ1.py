
# SOURCE_ID_REF_FOR_LOOKUP = "SHIP Tracking Number"
# SOURCE_ID_REF_FOR_LOOKUP = "SHIP ShipRush - Order Number"
SOURCE_ID_REF_FOR_LOOKUP_SHP = "SHIP Order ID - Secondary"  # backup column number to check for ID numbers
SOURCE_ID_REF_FOR_LOOKUP_STX = "SALETX Marketplace Transaction ID #2"  # backup column number to check for ID numbers
SOURCE_ID_REF_FOR_LOOKUP_SLN = "Sale Line: Item ID Tracking #"  # backup column number to check for ID numbers
# SOURCE_ID_REF_FOR_LOOKUP_LST = "LIST Listing ID"
SOURCE_ID_REF_FOR_LOOKUP_LST = "LST Listing ID"
SOURCE_ID_REF_FOR_LOOKUP_SFE = "SFE:Sale Financial Event ID"


LOOKUP_ORDER_ID1_NAME_SHIP = "SHIP_GEN_ORDER_ID"
LOOKUP_ORDER_ID2_NAME_SHIP = "SHIP_GEN_ORDER_ID_2"
LOOKUP_ORDER_ID1_NAME_STX = "STX_MARKETPLACE_TX_ID"
LOOKUP_ORDER_ID2_NAME_STX = "STX_MARKETPLACE_TX_ID"
LOOKUP_ORDER_ID1_NAME_SLN = "SALE_MARKETPLACE_TRANSACTION_ID"
LOOKUP_ORDER_ID2_NAME_SLN = "SALE_MARKETPLACE_TRANSACTION_ID"
LOOKUP_ORDER_ID1_NAME_LST = "LIST Listing ID"
LOOKUP_ORDER_ID2_NAME_LST = "LIST Listing ID"
LOOKUP_ORDER_ID1_NAME_SLN2LST = "ITEMDATA_GENERAL_CUSTOM_SKU"
LOOKUP_ORDER_ID2_NAME_SLN2LST = "SALE_MARKETPLACE_TRANSACTION_ID"
LOOKUP_ORDER_ID1_NAME_SLN2STX = "SALE__SELL_ID_NUM"
LOOKUP_ORDER_ID2_NAME_SLN2STX = "SALE__SELL_ID_NUM"
LOOKUP_ORDER_ID1_NAME_SFE = "SALE_FINANCIAL_EVENT_XITOR_KEY"
LOOKUP_ORDER_ID2_NAME_SFE = "SALE_FINANCIAL_EVENT_XITOR_KEY"

# lookupsourcefilekey1 = {
#     "SHIP Shipment CNE ID": [None, 1, None, "SHIP Shipment CNE ID", "SHIP Shipment CNE ID", ""],
#     "SHIP Order ID": [None, 2, None, "SHIP Order ID", "SHIP Order ID", ""],
#     "SHIP ShipRush - Order Internal Order ID": [None, 3, None, "SHIP ShipRush - Order Internal Order ID", "SHIP ShipRush - Order Internal Order ID", ""],
#     "SHIP ShipRush - Order External Order ID": [None, 4, None, "SHIP ShipRush - Order External Order ID", "SHIP ShipRush - Order External Order ID", ""],
#     "SHIP Veeqo - Order ID": [None, 5, None, "SHIP Veeqo - Order ID", "SHIP Veeqo - Order ID", ""],
#     # "SHIP Tracking Number": [None, 6, None, "Shipment Tracking Number", "SHIP Tracking Number", ""],
#     "SHIP Tracking Number": [None, 6, None, "SHIP Tracking Number", "SHIP Tracking Number", ""],
#     "SHIP ShipRush - Shipment Tracking Number": [None, 7, 1, "SHIP ShipRush - Shipment Tracking Number", "SHIP ShipRush - Shipment Tracking Number", ""],
#     "SHIP Veeqo - Tracking ID": [None, 8, None, "SHIP Veeqo - Tracking ID", "SHIP Veeqo - Tracking ID", ""]
# }

lookupsourcefilekey_SHP = {
    "SHIP Shipment CNE ID": [None, 1, 1, "SHIP Shipment CNE ID", "SHIP Shipment CNE ID", ""],
    "SHIP Order ID": [None, 2, 1, "SHIP Order ID", "SHIP Order ID", ""],
    "SHIP Order ID - Secondary": [None, 3, 1, "SHIP Order ID - Secondary", "SHIP Order ID - Secondary", ""],
    "SHIP ShipRush - Order Number": [None, 4, 1, "SHIP ShipRush - Order Number", "SHIP ShipRush - Order Number", ""],
    "SHIP ShipRush - Order Internal Order ID": [None, 5, 1, "SHIP ShipRush - Order Internal Order ID",
                                                "SHIP ShipRush - Order Internal Order ID", ""],
    "SHIP ShipRush - Order External Order ID": [None, 6, 1, "SHIP ShipRush - Order External Order ID",
                                                "SHIP ShipRush - Order External Order ID", ""],
    "SHIP Veeqo - Order ID": [None, 7, 1, "SHIP Veeqo - Order ID", "SHIP Veeqo - Order ID", ""],
    "SHIP Tracking Number": [None, 8, 1, "SHIP Tracking Number", "SHIP Tracking Number", ""],
    "SHIP ShipRush - Shipment Tracking Number": [None, 9, 1, "SHIP ShipRush - Shipment Tracking Number",
                                                 "SHIP ShipRush - Shipment Tracking Number", ""],
    "SHIP Veeqo - Tracking ID": [None, 10, 1, "SHIP Veeqo - Tracking ID", "SHIP Veeqo - Tracking ID", ""],
    "SHIP Rate/Ship Charge - Base": [None, 11, 1, "SHIP Rate/Ship Charge - Base", "SHIP Rate/Ship Charge - Base", ""],
    "SHIP Rate/Ship Charge - Original Base": [None, 12, 1, "SHIP Rate/Ship Charge - Original Base",
                                              "SHIP Rate/Ship Charge - Original Base", ""],
    "SHIP Rate/Ship Charge - Ttl": [None, 13, 1, "SHIP Rate/Ship Charge - Ttl", "SHIP Rate/Ship Charge - Ttl", ""],
    "SHIP Rate/Ship Charge - Adjustment": [None, 14, 1, "SHIP Rate/Ship Charge - Adjustment",
                                           "SHIP Rate/Ship Charge - Adjustment", ""],
    "SHIP Rate/Ship Charge - Adjustment Date": [None, 15, 1, "SHIP Rate/Ship Charge - Adjustment Date",
                                                "SHIP Rate/Ship Charge - Adjustment Date", ""],
    "SHIP Rate/Ship Charge - Adjustment Notes": [None, 16, 1, "SHIP Rate/Ship Charge - Adjustment Notes",
                                                 "SHIP Rate/Ship Charge - Adjustment Notes", ""],
    "SHIP Rate/Ship Charge - Adjustment Reason": [None, 17, 1, "SHIP Rate/Ship Charge - Adjustment Reason",
                                                  "SHIP Rate/Ship Charge - Adjustment Reason", ""],
    "SHIP System Created Date": [None, 18, 1, "SHIP System Created Date", "SHIP System Created Date", ""],
    "SHIP System Last Updated Date": [None, 19, 1, "SHIP System Last Updated Date", "SHIP System Last Updated Date",
                                      ""],

}

lookupsourcefilekey_STX = {
    "SALETX CNE ID": [None, 1, 1, "SALETX CNE ID", "SALETX CNE ID", ""],
    "SALETX Marketplace Transaction ID": [None, 2, 1, "SALETX Marketplace Transaction ID", "SALETX Marketplace Transaction ID", ""],
    "SALETX Marketplace Transaction ID #2": [None, 3, 1, "SALETX Marketplace Transaction ID #2", "SALETX Marketplace Transaction ID #2", ""],


}

lookupsourcefilekey_SLN_STX = {
    "SALETX CNE ID": [None, 1, 1, "SALETX CNE ID", "SALETX CNE ID", ""],
    "SALETX Marketplace Transaction ID": [None, 2, 1, "SALETX Marketplace Transaction ID", "SALETX Marketplace Transaction ID", ""],
    "SALETX Marketplace Transaction ID #2": [None, 3, 1, "SALETX Marketplace Transaction ID #2", "SALETX Marketplace Transaction ID #2", ""],


}

lookupsourcefilekey_SLN = {
    "Sale Line: Sale Line ID": [None, 1, 1, "Sale Line: Sale Line ID", "Sale Line: Sale Line ID", ""],
    "SALETX CNE ID": [None, 2, 1, "SALETX CNE ID", "SALETX CNE ID", ""],
    "Sale Line: Item ID Tracking #": [None, 3, 1, "Sale Line: Item ID Tracking #", "Sale Line: Item ID Tracking #", ""],
    "Sale Line: Marketplace Transaction ID (Sale)": [None, 4, 1, "Sale Line: Marketplace Transaction ID (Sale)", "Sale Line: Marketplace Transaction ID (Sale)", ""],
    "CHAN Sales Channel": [None, 5, 1, "CHAN Sales Channel", "CHAN Sales Channel", ""],

}


# lookupsourcefilekey_LISTING = {
#     "LIST Listing ID": [None, 1, 1, "LIST Listing ID", "LIST Listing ID", ""],
#
# }
lookupsourcefilekey_LISTING = {
    "LSTN SalesListing Line ID": [None, 1, 1, "LSTN SalesListing Line ID", "LSTN SalesListing Line ID", ""],
    "LSTN Internal SKU": [None, 2, 1, "LSTN Internal SKU", "LSTN Internal SKU", ""],
    "LSTN Number of Items": [None, 3, 1, "LSTN Number of Items", "LSTN Number of Items", ""],
    "CHAN Sales Channel": [None, 4, 1, "CHAN Sales Channel", "CHAN Sales Channel", ""],
    "LST Listing ID": [None, 5, 1, "LST Listing ID", "LST Listing ID", ""],
    "LST Listing Title": [None, 6, 1, "LST Listing Title", "LST Listing Title", ""],
    "LST Channel SKU": [None, 7, 1, "LST Channel SKU", "LST Channel SKU", ""],
    "MII Inventory Master Item": [None, 8, 1, "MII Inventory Master Item", "MII Inventory Master Item", ""],
    "MII Description": [None, 9, 1, "MII Description", "MII Description", ""],
    "MCC Master Cost Category": [None, 10, 1, "MCC Master Cost Category", "MCC Master Cost Category", ""],
    "MCC Master Cost - Current, for Cost/COGS": [None, 11, 1, "MCC Master Cost - Current, for Cost/COGS",
                                                 "MCC Master Cost - Current, for Cost/COGS", ""],
    "MCC Master Cost - Cur for COGS - Since Date": [None, 12, 1, "MCC Master Cost - Cur for COGS - Since Date",
                                                    "MCC Master Cost - Cur for COGS - Since Date", ""],

}

# lookupsourcefilekey_SLN_LST = {
#     "LIST Listing ID": [None, 1, 1, "LIST Listing ID", "LIST Listing ID", ""],
#
# }
lookupsourcefilekey_SLN_LST = {
    "LSTN SalesListing Line ID": [None, 1, 1, "LSTN SalesListing Line ID", "LSTN SalesListing Line ID", ""],
    "LSTN Internal SKU": [None, 2, 1, "LSTN Internal SKU", "LSTN Internal SKU", ""],
    "LSTN Number of Items": [None, 3, 1, "LSTN Number of Items", "LSTN Number of Items", ""],
    "CHAN Sales Channel": [None, 4, 1, "CHAN Sales Channel", "CHAN Sales Channel", ""],
    "LST Listing ID": [None, 5, 1, "LST Listing ID", "LST Listing ID", ""],
    "LST Listing Title": [None, 6, 1, "LST Listing Title", "LST Listing Title", ""],
    "LST Channel SKU": [None, 7, 1, "LST Channel SKU", "LST Channel SKU", ""],
    "MII Inventory Master Item": [None, 8, 1, "MII Inventory Master Item", "MII Inventory Master Item", ""],
    "MII Description": [None, 9, 1, "MII Description", "MII Description", ""],
    "MCC Master Cost Category": [None, 10, 1, "MCC Master Cost Category", "MCC Master Cost Category", ""],
    "MCC Master Cost - Current, for Cost/COGS": [None, 11, 1, "MCC Master Cost - Current, for Cost/COGS",
                                                 "MCC Master Cost - Current, for Cost/COGS", ""],
    "MCC Master Cost - Cur for COGS - Since Date": [None, 12, 1, "MCC Master Cost - Cur for COGS - Since Date",
                                                    "MCC Master Cost - Cur for COGS - Since Date", ""],

}


lookupsourcefilekey_SFE = {
    "SFE:Sale Financial Event ID": [None, 1, -1, "SFE:Sale Financial Event ID", "SFE:Sale Financial Event ID", ""],
    "SFE:Alias Field": [None, 2, 1, "SFE:Alias Field", "SFE:Alias Field", ""],
    "SFE:Order ID": [None, 3, 1, "SFE:Order ID", "SFE:Order ID", ""],
    "SFE:SKU": [None, 4, 1, "SFE:SKU", "SFE:SKU", ""],
    "SFE:Open Date": [None, 5, 1, "SFE:Open Date", "SFE:Open Date", ""],
    "SFE:Type": [None, 6, 1, "SFE:Type", "SFE:Type", ""],
    "SFE:Amount": [None, 7, 1, "SFE:Amount", "SFE:Amount", ""],
    "SFE:Fees - Base": [None, 8, 1, "SFE:Fees - Base", "SFE:Fees - Base", ""],
    "SFE:Fees - Misc": [None, 9, 1, "SFE:Fees - Misc", "SFE:Fees - Misc", ""],
    "SFE:Order Total": [None, 10, 1, "SFE:Order Total", "SFE:Order Total", ""],

}

lookupsourcefilekey_MII_MCC = {
    "LSTN SalesListing Line ID": [None, 1, 1, "LSTN SalesListing Line ID", "LSTN SalesListing Line ID", ""],
    "LSTN Internal SKU": [None, 2, 1, "LSTN Internal SKU", "LSTN Internal SKU", ""],
    "LSTN Number of Items": [None, 3, 1, "LSTN Number of Items", "LSTN Number of Items", ""],
    "CHAN Sales Channel": [None, 4, 1, "CHAN Sales Channel", "CHAN Sales Channel", ""],
    "LST Listing ID": [None, 5, 1, "LST Listing ID", "LST Listing ID", ""],
    "LST Listing Title": [None, 6, 1, "LST Listing Title", "LST Listing Title", ""],
    "LST Channel SKU": [None, 7, 1, "LST Channel SKU", "LST Channel SKU", ""],
    "MII Inventory Master Item": [None, 8, 1, "MII Inventory Master Item", "MII Inventory Master Item", ""],
    "MII Description": [None, 9, 1, "MII Description", "MII Description", ""],
    "MCC Master Cost Category": [None, 10, 1, "MCC Master Cost Category", "MCC Master Cost Category", ""],
    "MCC Master Cost - Current, for Cost/COGS": [None, 11, 1, "MCC Master Cost - Current, for Cost/COGS",
                                                 "MCC Master Cost - Current, for Cost/COGS", ""],
    "MCC Master Cost - Cur for COGS - Since Date": [None, 12, 1, "MCC Master Cost - Cur for COGS - Since Date",
                                                    "MCC Master Cost - Cur for COGS - Since Date", ""],

}

lookupsourcefilekey_UTR = {
    "date/time": [None, 1, 1, "date/time", "date/time", ""],
    "settlement id": [None, 2, 1, "settlement id", "settlement id", ""],
    "type": [None, 3, 1, "type", "type", ""],
    "order id": [None, 4, 1, "order id", "order id", ""],
    "sku": [None, 5, 1, "sku", "sku", ""],
    "description": [None, 6, 1, "description", "description", ""],
    "quantity": [None, 7, 1, "quantity", "quantity", ""],
    "marketplace": [None, 8, 1, "marketplace", "marketplace", ""],
    "account type": [None, 9, 1, "account type", "account type", ""],
    "fulfillment": [None, 10, 1, "fulfillment", "fulfillment", ""],
    "order city": [None, 11, 1, "order city", "order city", ""],
    "order state": [None, 12, 1, "order state", "order state", ""],
    "order postal": [None, 13, 1, "order postal", "order postal", ""],
    "tax collection model": [None, 14, 1, "tax collection model", "tax collection model", ""],
    "product sales": [None, 15, 1, "product sales", "product sales", ""],
    "product sales tax": [None, 16, 1, "product sales tax", "product sales tax", ""],
    "shipping credits": [None, 17, 1, "shipping credits", "shipping credits", ""],
    "shipping credits tax": [None, 18, 1, "shipping credits tax", "shipping credits tax", ""],
    "gift wrap credits": [None, 19, 1, "gift wrap credits", "gift wrap credits", ""],
    "giftwrap credits tax": [None, 20, 1, "giftwrap credits tax", "giftwrap credits tax", ""],
    "Regulatory Fee": [None, 21, 1, "Regulatory Fee", "Regulatory Fee", ""],
    "Tax On Regulatory Fee": [None, 22, 1, "Tax On Regulatory Fee", "Tax On Regulatory Fee", ""],
    "promotional rebates": [None, 23, 1, "promotional rebates", "promotional rebates", ""],
    "promotional rebates tax": [None, 24, 1, "promotional rebates tax", "promotional rebates tax", ""],
    "marketplace withheld tax": [None, 25, 1, "marketplace withheld tax", "marketplace withheld tax", ""],
    "selling fees": [None, 26, 1, "selling fees", "selling fees", ""],
    "fba fees": [None, 27, 1, "fba fees", "fba fees", ""],
    "other transaction fees": [None, 28, 1, "other transaction fees", "other transaction fees", ""],
    "other": [None, 29, 1, "other", "other", ""],
    "total": [None, 30, 1, "total", "total", ""],

}


def getfunctionkey(outputxitortype):

    newkey = None

    match outputxitortype:
        case "_Shipment_":
            newkey = functionkey1
        case "_SaleTx_":
            newkey = functionkey1
        case "_Sale Line_":
            newkey = functionkey1
        case "_Sale Financial Event_":
            newkey = functionkey1
        case _:
            newkey = functionkey1

    return functionkey1


def getlookupsourcefilekey(outputxitortype):

    retkey = None

    if isinstance(outputxitortype, list):
        match outputxitortype:
            case ["_Sale Line_", "_SalesListing_"]:
                retkey = lookupsourcefilekey_SLN_LST
            case ["_Sale Line_", "_SalesListing Line_"]:
                retkey = lookupsourcefilekey_SLN_LST
            case ["_Sale Line_", "_SaleTx_"]:
                retkey = lookupsourcefilekey_SLN_STX
            # case "_Sale Line_":
            #     retkey = lookupsourcefilekey_SLN
            # case "_SalesListing_":
            #     retkey = lookupsourcefilekey_LISTING
            case _:
                retkey = None
    else:
        match outputxitortype:
            case "_Shipment_":
                retkey = lookupsourcefilekey_SHP
            case "_SaleTx_":
                retkey = lookupsourcefilekey_STX
            case "_Sale Line_":
                retkey = lookupsourcefilekey_SLN
            case "_SalesListing_":
                retkey = lookupsourcefilekey_LISTING
            case "_Sale Financial Event_":
                retkey = lookupsourcefilekey_SFE
            case _:
                retkey = None

    # retkey = lookupsourcefilekey1[val1]
    return retkey


def getlookupsourcefilekeylength():
    return len(lookupsourcefilekey_SHP)


def getlookupsourcefilekeylength_multi(outputxitortype):

    match outputxitortype:
        case "SFE-Amazon-UTR":
            retkey = len(lookupsourcefilekey_UTR)
        case _:
            print("getlookupsourcefilekeylength_multi|retkey not found:" + str(outputxitortype))
            retkey = None

    return retkey



def getlookupsourcefilekeybyvalue(outputxitortype, val1):

    # print("val1:" + str(val1))

    retkey = None

    match outputxitortype:
        case "_Shipment_":
            retkey = lookupsourcefilekey_SHP[val1]
        case "_SaleTx_":
            retkey = lookupsourcefilekey_STX[val1]
        case "_Sale Line_":
            retkey = lookupsourcefilekey_SLN[val1]
        case "_SalesListing_":
            retkey = lookupsourcefilekey_LISTING[val1]
        case "_SalesListing Line_":
            retkey = lookupsourcefilekey_LISTING[val1]
        case "_Sale Financial Event_":
            retkey = lookupsourcefilekey_SFE[val1]
        case "MII-MCC":
            retkey = lookupsourcefilekey_MII_MCC[val1]
        case "UTR":
            retkey = lookupsourcefilekey_UTR[val1]
        case _:
            retkey = None

    # retkey = lookupsourcefilekey1[val1]
    return retkey

def getsourceidrefforlookup(outputxitortype):

    match outputxitortype:
        case "_Shipment_":
            return SOURCE_ID_REF_FOR_LOOKUP_SHP
        case "_SaleTx_":
            return SOURCE_ID_REF_FOR_LOOKUP_STX
        case "_Sale Line_":
            return SOURCE_ID_REF_FOR_LOOKUP_SLN
        case "_SalesListing_":
            return SOURCE_ID_REF_FOR_LOOKUP_LST
        case "_SalesListing Line_":
            return SOURCE_ID_REF_FOR_LOOKUP_LST
        case "_Sale Financial Event_":
            return SOURCE_ID_REF_FOR_LOOKUP_SFE
        case _:
            return None




def getlookuporderidnames(xitortype):

    field1 = ""
    field2 = ""

    if isinstance(xitortype, list):
        match xitortype:
            case ["_Sale Line_", "_SalesListing_"]:
                field1 = LOOKUP_ORDER_ID1_NAME_SLN2LST
                field2 = LOOKUP_ORDER_ID2_NAME_SLN2LST
            case ["_Sale Line_", "_SalesListing Line_"]:
                field1 = LOOKUP_ORDER_ID1_NAME_SLN2LST
                field2 = LOOKUP_ORDER_ID2_NAME_SLN2LST
            case ["_Sale Line_", "_SaleTx_"]:
                field1 = LOOKUP_ORDER_ID1_NAME_SLN2STX
                field2 = LOOKUP_ORDER_ID2_NAME_SLN2STX
            # case "_Sale Line_":
            #     retkey = lookupsourcefilekey_SLN
            # case "_SalesListing_":
            #     retkey = lookupsourcefilekey_LISTING
    else:
        match xitortype:
            case "SHP-":
                field1 = LOOKUP_ORDER_ID1_NAME_SHIP
                field2 = LOOKUP_ORDER_ID2_NAME_SHIP
            case "STX-":
                field1 = LOOKUP_ORDER_ID1_NAME_STX
                field2 = LOOKUP_ORDER_ID2_NAME_STX
            case "SLN-":
                field1 = LOOKUP_ORDER_ID1_NAME_SLN
                field2 = LOOKUP_ORDER_ID2_NAME_SLN
            case "LST-":
                field1 = LOOKUP_ORDER_ID1_NAME_LST
                field2 = LOOKUP_ORDER_ID2_NAME_LST
            case "SFE-":
                field1 = LOOKUP_ORDER_ID1_NAME_SFE
                field2 = LOOKUP_ORDER_ID2_NAME_SFE

    return [field1, field2]


# SHIP_GEN_CARRIER / "Carrier"
def get_gen_carrier(field_ship_sr_service):

    if field_ship_sr_service.find("USPS") != -1:
        return "USPS"
    elif field_ship_sr_service.find("UPS") != -1:
        return "UPS"
    elif field_ship_sr_service.find("FedEx") != -1:
        return "FedEx"
    elif field_ship_sr_service.find("DHL") != -1:
        return "DHL"
    elif field_ship_sr_service.find("Amazon") != -1:
        return "Amazon"
    elif field_ship_sr_service.find("Sendle") != -1:
        return "Sendle"
    elif field_ship_sr_service.find("Other") != -1:
        return "Other"
    else:
        print("CARRIER U: " + field_ship_sr_service)
        return "ERROR CARRIER UNKNOWN"

# SHIP_GEN_CRR_SRV_DD / "Carrier Service DD"
def get_gen_carrier_dd(field_ship_sr_service):

    if field_ship_sr_service == '' or field_ship_sr_service == '\'\'':
        return ""

    if field_ship_sr_service.find("USPS First Class") != -1 or field_ship_sr_service.find("FirstClass") != -1:
        return "First Class"
    elif field_ship_sr_service.find("Media Mail") != -1 or field_ship_sr_service.find("MediaMail") != -1:
        return "Media Mail"
    elif field_ship_sr_service.find("Express") != -1:
        return "Express"
    elif field_ship_sr_service.find("Parcel Select") != -1 or field_ship_sr_service.find("ParcelSelect") != -1:
        return "Parcel Select"
    elif field_ship_sr_service.find("USPS Priority") != -1 or field_ship_sr_service.find("USPSPriority") != -1:
        return "Priority Mail"
    elif (field_ship_sr_service.find("UPS") != -1 and field_ship_sr_service.find("Ground") != -1) or \
            field_ship_sr_service.find("UPSGround") != -1:
        return "UPS Ground"
    elif field_ship_sr_service.find("UPS 2nd Day Air") != -1:
        return "UPS Ground"
    elif field_ship_sr_service.find("UPS 3 Day Select") != -1:
        return "UPS Ground"
    elif field_ship_sr_service.find("FedEx Ground") != -1:
        return "FedEx Ground"
    elif field_ship_sr_service.find("FedEx Home Delivery") != -1:
        return "FedEx Home Delivery"
    elif field_ship_sr_service.find("USPS Intl First Class") != -1:
        return "USPS Intl First Class"
    elif field_ship_sr_service.find("USPS Ground Advantage") != -1 or field_ship_sr_service.find("GroundAdvantage") \
            != -1:
        return "USPS Ground Advantage"
    elif field_ship_sr_service.find("Sendle Standard") != -1:
        return "Sendle Standard"
    elif field_ship_sr_service.find("Sendle Saver") != -1:
        return "Sendle Saver"
    elif field_ship_sr_service.find("Sendle Preferred") != -1:
        return "Sendle Preferred"
    elif field_ship_sr_service.find("Sendle First Class Mail Plus") != -1:
        return "Sendle First Class Mail Plus"
    elif field_ship_sr_service.find("Sendle Parcel Select Ground Plus") != -1:
        return "Sendle Parcel Select Ground Plus"
    elif field_ship_sr_service.find("Sendle Priority Mail Plus") != -1:
        return "Sendle Priority Mail Plus"
    else:
        print("CARRIER SERV U: " + field_ship_sr_service)
        return "ERROR CARRIER SERVICE UNKNOWN"

# SHIP_GEN_OWN_COMP / "Owning Company"
def get_gen_own_comp(field_ship_sr_ord_store_name):

    if field_ship_sr_ord_store_name.find("CNE LLC") != -1 or field_ship_sr_ord_store_name.find("CNELLC") != -1:
        return "CNE LLC"
    elif field_ship_sr_ord_store_name.find("Digicati") != -1 or field_ship_sr_ord_store_name.find("digicati") != -1:
        return "Digicati"
    elif field_ship_sr_ord_store_name.find("eIncense") != -1 or field_ship_sr_ord_store_name.find("eincense") != -1:
        return "Digicati"
    elif field_ship_sr_ord_store_name.find("ShopIncense") != -1 or field_ship_sr_ord_store_name.find("Shop Incense") != -1:
        return "Digicati"
    elif field_ship_sr_ord_store_name.find("ebliquidators") != -1:
        return "CNE LLC"
    elif field_ship_sr_ord_store_name.find("ourQuickStop") != -1 or field_ship_sr_ord_store_name.find("ourquickstop")\
            != -1:
        return "Digicati"
    elif field_ship_sr_ord_store_name.find("Abes Bargains") != -1 or field_ship_sr_ord_store_name.find("AbesBargains")\
            != -1:
        return "CNE LLC"
    elif field_ship_sr_ord_store_name.find("almart") != -1:
        return "CNE LLC"
    elif field_ship_sr_ord_store_name.find("CSV Orders") != -1:
        return ""
    elif field_ship_sr_ord_store_name.find("Manual Store") != -1:
        return ""
    elif field_ship_sr_ord_store_name == "":
        return ""
    else:
        print("OWNING CO U: " + field_ship_sr_ord_store_name)
        return "ERROR OWNING CO UNKNOWN"

# SHIP_GEN_CHANNEL / "Sales Channel"
def get_gen_channel(field_ship_sr_ord_store_name):

    # if field_ship_sr_ord_store_name.find("CNE LLC") != -1 or field_ship_sr_ord_store_name.find("CNELLC") != -1:
    #     return "CN/Ebay"
    if field_ship_sr_ord_store_name.find("Digicati") != -1 or field_ship_sr_ord_store_name.find("digicati") != -1:
        return "DDS/Ebay"
    elif field_ship_sr_ord_store_name.find("eIncense") != -1 or field_ship_sr_ord_store_name.find("eincense") != -1:
        return "WeIncense"
    elif field_ship_sr_ord_store_name.find("ShopIncense") != -1 or field_ship_sr_ord_store_name.find("Shop Incense") != -1:
        return "ShopIncense"
    elif field_ship_sr_ord_store_name.find("ebliquidators") != -1 or field_ship_sr_ord_store_name.find("Amazon") != -1 \
            or field_ship_sr_ord_store_name.find("AMZ") != -1:
        return "CN/Amazon-FBM"
    elif field_ship_sr_ord_store_name.find("ourQuickStop") != -1 or field_ship_sr_ord_store_name.find("ourquickstop")\
            != -1:
        return "YourQuickStop"
    elif field_ship_sr_ord_store_name.find("Abes Bargains") != -1 or field_ship_sr_ord_store_name.find("AbesBargains")\
            != -1:
        return "CN/Ebay"
    elif field_ship_sr_ord_store_name.find("almart") != -1:
        return "CN/Walmart"
    elif field_ship_sr_ord_store_name == "":
        return ""
    else:
        print("SALES CHANNEL UNKNOWN: " + str(field_ship_sr_ord_store_name))
        return "SALES CHANNEL UNKNOWN"


# SHIP_GEN_TO_STATE / "Ship To State"
def get_to_state(gen_to_state):

    state_lower = gen_to_state.lower()

    match state_lower:
        case "alabama" | "al":
            return "AL"
        case "arizona" | "az":
            return "AZ"
        case "arkansas" | "ar":
            return "AR"
        case "california" | "ca":
            return "CA"
        case "colorado" | "co":
            return "CO"
        case "connecticut" | "ct":
            return "CT"
        case "delaware" | "de":
            return "DE"
        case "dist. of columbia" | "dc" | "d.c." | "district of columbia":
            return "DC"
        case "florida" | "fl":
            return "FL"
        case "georgia" | "ga":
            return "GA"
        case "hawaii" | "hi":
            return "HI"
        case "illinois" | "il":
            return "IL"
        case "indiana" | "in":
            return "IN"
        case "iowa" | "ia":
            return "IA"
        case "kansas" | "ks":
            return "KS"
        case "kentucky" | "ky":
            return "KY"
        case "louisiana" | "la":
            return "LA"
        case "maine" | "me":
            return "ME"
        case "maryland" | "md":
            return "MD"
        case "massachusetts" | "ma":
            return "MA"
        case "michigan" | "mi":
            return "MI"
        case "minnesota" | "mn":
            return "MN"
        case "mississippi" | "ms":
            return "MS"
        case "missouri" | "mo":
            return "MO"
        case "montana" | "mt":
            return "MT"
        case "nebraska" | "ne":
            return "NE"
        case "nevada" | "nv":
            return "NV"
        case "new hampshire" | "nh":
            return "NH"
        case "new jersey" | "nj":
            return "NJ"
        case "new mexico" | "nm":
            return "NM"
        case "new york" | "ny":
            return "NY"
        case "north carolina" | "nc":
            return "NC"
        case "ohio" | "oh":
            return "OH"
        case "oklahoma" | "ok":
            return "OK"
        case "oregon" | "or":
            return "OR"
        case "pennsylvania" | "pa":
            return "PA"
        case "rhode island" | "ri":
            return "RI"
        case "south carolina" | "sc":
            return "SC"
        case "south dakota" | "sd":
            return "SD"
        case "tennessee" | "tn":
            return "TN"
        case "alaska" | "ak":
            return "AK"
        case "texas" | "tx":
            return "TX"
        case "vermont" | "vt":
            return "VT"
        case "virginia" | "va":
            return "VA"
        case "washington" | "wa":
            return "WA"
        case "west virginia" | "wv":
            return "WV"
        case "wisconsin" | "wi":
            return "WI"
        case "wyoming" | "wy":
            return "WY"
        case "north dakota" | "nd":
            return "ND"
        case "idaho" | "id":
            return "ID"
        case "utah" | "ut":
            return "UT"
        case "puerto rico" | "pr":
            return "PR"
        case "virgin islands" | "vi":
            return "VI"
        case "guam" | "gu":
            return "GU"
        case "armed forces americas" | "APO/FPO":
            return "APO/FPO"
        case "armed forces europe" | "APO/FPO" | "ae":
            return "APO/FPO"
        case "Northern Mariana Islands" | "Northern Mariana Islands":
            return "Northern Mariana Islands"
        case "British Columbia" | "BC":
            return "BC"
        case "Quebec" | "QC":
            return "QC"
        case "Ontario" | "ON":
            return "ON"
        case "anonymized by amazon":
            return "REMOVED"
        case _:
            print("STATE U: " + state_lower)
            return "ERROR UNKNOWN SHIP TO STATE"

# dictionary of all functions in this file, to pass to main files for use
functionkey1 = {
    "getlookupsourcefilekey": [getlookupsourcefilekey],
    "getlookupsourcefilekeylength": [getlookupsourcefilekeylength],
    "getlookupsourcefilekeylength_multi": [getlookupsourcefilekeylength_multi],
    "getlookupsourcefilekeybyvalue": [getlookupsourcefilekeybyvalue],
    "getsourceidrefforlookup": [getsourceidrefforlookup],
    "get_gen_carrier": [get_gen_carrier],
    "get_gen_carrier_dd": [get_gen_carrier_dd],
    "get_gen_own_comp": [get_gen_own_comp],
    "get_gen_channel": [get_gen_channel],
    "get_to_state": [get_to_state],
    "getlookuporderidnames": [getlookuporderidnames]



}
