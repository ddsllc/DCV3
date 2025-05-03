import Helpers1
import csv
import os
import switcher2
import re
import GenFieldKey_CIQ1
import SourceFileKey_Ebay_Shipping

# read in outputfileformat


RUN_MODE = 1  # 0= write each line and display combined's, 1= store lines, write all at once with integrated combined's
CONSOLE_OUTPUT_SECTIONS_0 = False
CONSOLE_OUTPUT_0 = False
CONSOLE_OUTPUT_1 = True
CONSOLE_OUTPUT_2 = False
TESTING_RUN_LIMIT = -1  # Limit the number of loops for testing/review, -1=unlimited


def processfile(t_mode, filesforprocessing, globkeyfile, sourceglobkeyfile, outputfiletype):
    TEST_MODE = t_mode

    print("---OUTPUT FILE TYPE---")
    print(outputfiletype)
    print("---")
    # print(globkeyfile["processfileheaderrow"])

    print("---GLOBAL KEY FILE---")
    print(globkeyfile)
    print("---")
    # print(globkeyfile["processfileheaderrow"])

    print("---SOURCE GLOBAL KEY FILE---")
    print(sourceglobkeyfile)
    print("---")
    # print(globkeyfile["processfileheaderrow"])


    firstfile = filesforprocessing[0]
    print("---FIRST FILE SOURCE KEYWORD---")
    print(firstfile)
    print("---")
    outputfile_add, outputfile_update, outputfile_err, outputfile_test1 = None, None, None, None


    # get dictionary of all functions for the target source file
    filekey_1 = Helpers1.getfunctionkey(firstfile)
    print("---FILE SOURCE KEYFILE---")
    if filekey_1 == "":
        print("***ERROR*** File Source Keyfile (filekey_1) not found - File Source Keyword may be incorrect or "
              "File Source Keyfile is set up incorrectly")
        print("filekey_1:" + str(filekey_1))
    else:
        print("filekey_1:" + str(filekey_1))
    print("---")

    print("---MAIN_XITOR_TYPE_KEYWORD from FILE SOURCE KEYFILE---")
    mainxitortypekeyword = filekey_1["getmainxitorlookuptype"][0]()
    print(str(mainxitortypekeyword))
    print("---")

    # get dictionary of all functions for the target lookup file (probably from CIQ)
    filekey_lookup = Helpers1.getfunctionkey_lookup("CIQ", mainxitortypekeyword)
    print("---LOOKUP FILE KEYFILE---")
    print(filekey_lookup)
    print("---")

    if TEST_MODE:
        print("---OUTPUT FILES CREATED---")
        filekey_1["setrandomrunid"][0]()  # Creates and sets unique import ID to append to output filenames

        outputfile_add = filekey_1["getoutputfile_add"][0]()
        print("Output File Add: " + outputfile_add)
        outputfile_update = filekey_1["getoutputfile_update"][0]()
        print("Output File Update: " + outputfile_update)
        outputfile_err = filekey_1["getoutputfile_err"][0]()
        print("Output File Error: " + outputfile_err)
        outputfile_test1 = filekey_1["getoutputfile_test1"][0]()
        print("Output File test1: " + outputfile_test1)
        print("---")
    else:
        outputfileformat = ""
        outputfile = ""

    # outputfileformatlength = len(outputfileformat)

    # read in primary source file

    # ------------------------
    # READ IN AND STORE CURRENT STATE OF  FILE
    # *no longer needed?
    # ------------------------
    inputFileList = []
    with open(outputfile_add, "w", newline='') as csvfileOutput:
        # dcreaderoutput = csv.reader(csvfileOutput, delimiter=',', quotechar='|')
        dcreaderoutput = csv.reader(csvfileOutput, delimiter=',', quoting=csv.QUOTE_NONE)
        # for tempRow in dcreaderoutput:
        #     inputFileList.append(tempRow)
        #     print(inputFileList)

    curfilename = Helpers1.getfilenamebykeyword(str(firstfile))

    if curfilename is not None and len(curfilename) > 0:
        dataFileContents = [""]
        ttlDataFileRows = 0
        curfilename = str(curfilename.strip())
        curfilename = curfilename.replace("\'", "")
        print("---")
        print("Processing File: " + str(curfilename))
    else:
        print("filename not found")

    f_add = open(outputfile_add, "w")
    f_update = open(outputfile_update, "w")
    f_err = open(outputfile_err, "w")
    f_test1 = open(outputfile_test1, "w")

    fullinputrowlist = [[]]
    fullinputrowlistheader = [[]]

    # ------------------------
    # OPEN THE FIRST FILE & READ IN HEADER ROW
    #  #ADD-NEW-1
    # ------------------------
    # with open(curfilename, newline='') as csvfile:
    errors1 = ''
    match firstfile:
        # cp1252

        case "ShipRush":
            encoding1 = "latin-1"
            newline1 = '\r\n'
            errors1 = 'backslashreplace'
        case "Ebay-Orders":
            encoding1 = "utf-8-sig"
            newline1 = ''
        case "Ebay-Shipping":
            encoding1 = "mbcs"
            newline1 = ''
        case "SLN-Amazon-AO":
            encoding1 = "utf-8"
            newline1 = ''
        case "STX-Amazon-AO":
            encoding1 = "utf-8"
            newline1 = ''
        case "STX-Amazon-AO":
            encoding1 = "utf-8"
            newline1 = ''
        case "SFE-Amazon-UTR":
            encoding1 = "utf-8"
            newline1 = ''
        case "Veeqo-Orders-STX":
            encoding1 = "utf-8"
            newline1 = ''
        case _:
            encoding1 = "utf-8"
            newline1 = ''

    print("Args: " + encoding1 + " | " + newline1)
    # with open(curfilename, encoding="utf-8-sig") as csvfile:
    # with open(curfilename, mode='rt', encoding=encoding1, newline=newline1, errors=errors1) as csvfile:
    #  #ADD-NEW-2
    # with open(curfilename, mode='rt', encoding=encoding1, newline=newline1, errors=errors1) as csvfile:
    with open(curfilename, mode='r', encoding=encoding1, newline=newline1, errors=errors1) as csvfile:

        if firstfile == "Ebay-Orders" or firstfile == "Ebay-Shipping":
            dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        elif firstfile == "ShipRush":
            dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"', lineterminator='\r')
        elif firstfile.find("Amazon-AO") != -1:
            dcreader2 = csv.reader(csvfile, delimiter='\t')
            print("reader: Amazon-AO")
        elif firstfile == "Veeqo-Orders-STX":
            dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"', lineterminator='\r')
        else:
            dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"')

        # # dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='|')
        # dcreader2 = csv.reader(csvfile, delimiter=',', quotechar='"', lineterminator='\r')

        # print(curHeader)

        curheader = []
        #skip reading header row if there are specialfunctions1
        if "specialfunctions1" not in sourceglobkeyfile:
            curheader = next(dcreader2)
            print("skipped")

        print("curheader1: " + str(curheader))

        curheader = str(curheader).replace("\'", "")
        curheader = str(curheader).replace("[", "")
        curheader = str(curheader).replace("]", "")
        # outputheaderlist = str(curheader).split(",")
        print("curheader: " + str(curheader))
        startIndex = 0




        # test1 = switcher2.getsourcefilekeybyvalue("Shipment Service")
        # print(test1)
        curkeyfile = filekey_1["getsourcefilekey"][0]()
        # print(curkeyfile)

        new_output_row_str = ""

        curheaderlist = str(curheader).split(", ")
        print("curheaderlist:" + str(curheaderlist))
        new_output_row_list = []

        keylength = filekey_1["getsourcefilekeylength"][0]()
        basekeylength = filekey_1["getsourcefilekeybaselength"][0]()

        # check for blank first row
        print("check blanks: " + curheaderlist[0])
        # while curheaderlist is None or len(curheaderlist) == 0 or curheaderlist[0] == ""
        while curheaderlist is None or len(curheaderlist) == 0 or curheaderlist[0] == "" or len(curheaderlist) < basekeylength:
            curheader = next(dcreader2)
            curheader = str(curheader).replace("\'", "")
            curheader = str(curheader).replace("[", "")
            curheader = str(curheader).replace("]", "")
            curheaderlist = str(curheader).split(", ")
            if CONSOLE_OUTPUT_0:
                print("len(curheaderlist): " + str(len(curheaderlist)))
                print("basekeylength: " + str(basekeylength))
                print("curheaderlist: " + str(curheaderlist))



        if "processfileheaderrow" in globkeyfile:
            print("---FUNCTION \"processfileheaderrow\" EXECUTED---")
            # new_output_row_list = Helpers1.processfileheaderrow(curheaderlist, curkeyfile, keylength)
            new_output_row_list = globkeyfile["processfileheaderrow"][0](curheaderlist, curkeyfile, keylength)
            print(new_output_row_list)
            print("---")

            # fullinputrowlistheader.append(new_output_row_list)
            # fullinputrowlistheader.pop(0)



        if "translatefileheaderrow1" in globkeyfile:
            print("---FUNCTION \"translatefileheaderrow1\" EXECUTED---")
            # new_output_row_list = Helpers1.processfileheaderrow(curheaderlist, curkeyfile, keylength)
            new_output_row_list = globkeyfile["translatefileheaderrow1"][0](new_output_row_list, curkeyfile)
            print(new_output_row_list)
            print("---")

            # fullinputrowlistheader.append(new_output_row_list)
            # fullinputrowlistheader.pop(0)




        if "translatefileheaderrow2" in globkeyfile:
            print("---FUNCTION \"translatefileheaderrow2\" EXECUTED---")
            # new_output_row_list = Helpers1.processfileheaderrow(curheaderlist, curkeyfile, keylength)
            new_output_row_list = globkeyfile["translatefileheaderrow2"][0](new_output_row_list, curkeyfile)
            print(new_output_row_list)
            print("---")



        fullinputrowlistheader.append(new_output_row_list)
        fullinputrowlistheader.pop(0)

        # translatefileheaderrow1
        # translatefileheaderrow2

        # print("fullinputrowlistheader: " + str(fullinputrowlistheader))

        new_output_row_list = str(new_output_row_list).replace("\'", "")
        new_output_row_list = str(new_output_row_list).replace("[", "")
        new_output_row_list = str(new_output_row_list).replace("]", "")
        new_output_row_list = str(new_output_row_list).replace(", ", ",")

        print("---FINAL HEADER ROW---")
        print(str(new_output_row_list))
        print("---")



        if RUN_MODE == 0:
            f_add.write(str(new_output_row_list) + "\n")
            f_update.write(str(new_output_row_list) + "\n")

            count = 0
            for temprow in dcreader2:
                # print("---")
                # print("temprow: " + str(temprow))

                temprowlist = str(temprow).split(", ")
                initlength = len(temprowlist)
                # print(str(initlength))
                new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                new_output_row_list = Helpers1.finalerrorcheck(new_output_row_list, curkeyfile, keylength, firstfile,
                                                               initlength)
                new_output_row_list = Helpers1.ciqidlookupadd(new_output_row_list, curkeyfile, keylength, firstfile)

                fullinputrowlist.append(new_output_row_list)

                new_output_row_list = str(new_output_row_list).replace("\'", "")
                new_output_row_list = str(new_output_row_list).replace("[", "")
                new_output_row_list = str(new_output_row_list).replace("]", "")
                new_output_row_list = str(new_output_row_list).replace("\"", "")
                # new_output_row_list = str(new_output_row_list).replace("||", "\'")
                # new_output_row_list = str(new_output_row_list).replace("\'\'", "\'")
                new_output_row_list = str(new_output_row_list).replace("||", "")
                new_output_row_list = str(new_output_row_list).replace(", ", ",")
                new_output_row_list = str(new_output_row_list).replace("$", "")
                # print("new_output_row_list: " + str(new_output_row_list))
                new_output_row_list = new_output_row_list.strip()
                # print("---")

                print("Final Processed Row: [" + str(new_output_row_list) + "]")
                # print("Final Processed Row: [" + str(new_output_row_list[0:4]) + "]")

                if new_output_row_list.find("CNE-DC Errors found") != -1:
                    print("Error")
                    f_err.write(str(new_output_row_list) + "\n")
                elif new_output_row_list[0:4] == "SHP-":
                    # print("Update")
                    f_update.write(str(new_output_row_list) + "\n")
                else:
                    # print("Add")
                    f_add.write(str(new_output_row_list) + "\n")
                count += 1
            print("-----------------------------------")
            print("Total Rows Processed: " + str(count))
            print("-----------------------------------")

        elif RUN_MODE == 1:
            count = 0
            # print("fullinputrowlist-f: " + str(fullinputrowlist))
            print("-----------------------------------")
            print("PROCESS ROWS: ")
            print("-----------------------------------")

            if "specialfunctions1" in sourceglobkeyfile:
                print("---FUNCTION \"specialfunctions1\" EXECUTED---")
                # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                filekey_1["specialfunctions1"][0](curfilename, encoding1, newline1)
                # print(new_output_row_list)
                # if new_output_row_list is None:
                #     print("Invalid Row--Skipped:" + str(temprowlist))
                #     continue
                print("---")

            run_count = 1  # used with TESTING_RUN_LIMIT to limit loops for testing

            for temprow in dcreader2:

                if TESTING_RUN_LIMIT != -1 and run_count >= TESTING_RUN_LIMIT:
                    print("-----------------------------------")
                    print("***PROGRAM ENDED VIA TESTING_RUN_LIMIT***: " + str(TESTING_RUN_LIMIT))
                    print("-----------------------------------")
                    break

                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("-----------------------------------")
                print("--- Processing complete, row: " + str(count) + " ---")
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("-----------------------------------")
                # print("---")
                if CONSOLE_OUTPUT_1:
                    print("temprow: " + str(temprow))

                #  ADD-NEW-2
                if firstfile == "Ebay-Orders" or firstfile == "Ebay-Shipping":
                    temprowstr = str(temprow).replace("Alpharetta\', ", "Alpharetta|| ")
                    # temprowlist = str(temprowstr).split(", ")

                    # regex desc: using positive lookahead, split around a comma only if no double quotes or
                    # #  if is an even number of double quotes ahead
                    temprowlist = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", str(temprowstr))
                    # print(csv.list_dialects())
                    # print(temprowlist)
                elif firstfile == "ShipRush":
                    # temprowstr = str(temprow).replace("Alpharetta\', ", "Alpharetta|| ")
                    # temprowlist = str(temprowstr).split(", ")

                    # regex desc: using positive lookahead, split around a comma only if no double quotes or
                    # #  if is an even number of double quotes ahead
                    # temprowlist = re.split(",(?=(?:[^\']*\'[^\']*\')*[^\']*$)", str(temprow))

                    # print("temprowlist[0]:" + str(temprow))
                    # print(str(temprow).find("\'"))
                    # temprow = str(temprow).replace("\'", "")
                    # print("temprow1:" + str(temprow))
                    # temprowtest = re.sub(r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", "|", str(temprow), flags=re.IGNORECASE)
                    # print("temprowtest:" + str(str(temprow).count("\'")))
                    # temprowlist = re.split(", (?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", str(temprow))
                    temprowlist = temprow
                    count1 = 0
                    # print(len(temprow))
                    # for char1 in temprow:
                    #     # print(temprow)
                    #     if char1 == "'":
                    #         count1 += 1
                    #         print(char1)
                    # print("loopcount:" + str(count1))


                    # temprowlist = re.split(",(?=(?:[^\']*\'[^\']*\')*[^\']*$)", str(temprow))
                    # print(csv.list_dialects())
                    # print("temprowlist[0]:" + str(temprowlist))
                elif firstfile.find("-Amazon-") != -1:
                    temprowlist = temprow
                    count1 = 0
                    # print(len(temprow))
                    # print("loopcount:" + str(count1))
                elif firstfile == "Veeqo-Orders-STX":
                    temprowlist = temprow
                    count1 = 0
                else:
                    temprowlist = str(temprow).split(", ")
                initlength = len(temprowlist)
                # print(str(initlength))
                # print(firstfile)
                # print(switcher2.getsourcefilekeybaselength(firstfile))
                # print(temprowlist)



                if "preprocessfilerow" in sourceglobkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"preprocessfilerow\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = filekey_1["preprocessfilerow"][0](temprowlist)
                    # print(new_output_row_list)
                    if new_output_row_list is None:
                        print("Invalid Row--Skipped:" + str(temprowlist))
                        continue
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")
                # print(new_output_row_list)



                if "processfilenextrow" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"processfilenextrow\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["processfilenextrow"][0](temprowlist, curkeyfile, keylength,
                                                                               firstfile, filekey_1)
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")
                if CONSOLE_OUTPUT_1:
                    print("post-processfilenextrow|new_output_row_list: " + str(new_output_row_list))
                    print("---")



                if "processcalculatedrows" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"processcalculatedrows\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["processcalculatedrows"][0](new_output_row_list, curkeyfile,
                                                                                  keylength, firstfile, filekey_1)
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")



                if "processtranslatedrows" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"processtranslatedrows\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["processtranslatedrows"][0](new_output_row_list, curkeyfile,
                                                                                  keylength, firstfile, filekey_1)
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")


                if "getsecondarylookupvalues" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"getsecondarylookupvalues\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["getsecondarylookupvalues"][0](new_output_row_list, curkeyfile,
                                                                                  keylength, firstfile, filekey_1, filekey_lookup)
                    if CONSOLE_OUTPUT_0:
                        print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

                if "getsecondaryagglookupvalues" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"getsecondaryagglookupvalues\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["getsecondaryagglookupvalues"][0](new_output_row_list, curkeyfile,
                                                                                  keylength, firstfile, filekey_1,
                                                                                        filekey_lookup, firstfile)
                    if CONSOLE_OUTPUT_0:
                        print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

                if "getsecondaryagglookupvalues_UTR" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"getsecondaryagglookupvalues_UTR\" EXECUTED---")
                    # new_output_row_list = Helpers1.processfilenextrow(temprowlist, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["getsecondaryagglookupvalues_UTR"][0](new_output_row_list, curkeyfile,
                                                                                  keylength, firstfile, filekey_1, filekey_lookup)
                    if CONSOLE_OUTPUT_0:
                        print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

                error_results = [None, False, ""]
                if "finalerrorcheck" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"finalerrorcheck\" EXECUTED---")
                    # new_output_row_list = Helpers1.finalerrorcheck(new_output_row_list, curkeyfile, keylength,
                    # firstfile, initlength)
                    error_results = globkeyfile["finalerrorcheck"][0](new_output_row_list, curkeyfile, keylength,
                                                                            firstfile, initlength, filekey_1)
                    new_output_row_list = error_results[0]
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

                if "pushfinalerrormessage" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"pushfinalerrormessage\" EXECUTED---")
                    if error_results[1]:
                        # new_output_row_list = Helpers1.ciqidlookupadd(new_output_row_list, curkeyfile, keylength, firstfile)
                        new_output_row_list = globkeyfile["pushfinalerrormessage"][0](new_output_row_list, curkeyfile,
                                                                                      error_results[2])
                        # print(new_output_row_list)
                    else:
                        if CONSOLE_OUTPUT_SECTIONS_0:
                            print("No Errors Detected, No Change")
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")


                # for same-type xitor key lookups
                if "ciqidlookupadd" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"ciqidlookupadd\" EXECUTED---")
                    # new_output_row_list = Helpers1.ciqidlookupadd(new_output_row_list, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["ciqidlookupadd"][0](new_output_row_list, curkeyfile, keylength,
                                                                           firstfile, filekey_1, filekey_lookup)
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

                # for same-type xitor key lookup w multi-column lookup value (example: [Order ID]--[SKU] for SaleLine
                if "ciqidlookupaddmulti" in globkeyfile:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"ciqidlookupaddmulti\" EXECUTED---")
                    # new_output_row_list = Helpers1.ciqidlookupadd(new_output_row_list, curkeyfile, keylength, firstfile)
                    new_output_row_list = globkeyfile["ciqidlookupaddmulti"][0](new_output_row_list, curkeyfile,
                                                                           keylength,
                                                                           firstfile, filekey_1, filekey_lookup)
                    # print(new_output_row_list)
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")


                fullinputrowlist.append(new_output_row_list)
                # print("new_output_row_list: " + str(new_output_row_list[40]))

                if CONSOLE_OUTPUT_1:
                    print("new_output_row_list: " + str(new_output_row_list))
                    print("---")



                # print("Final Processed Row2: [" + str(new_output_row_list[63]) + "]")
                new_output_row_list = str(new_output_row_list).replace("\'", "")
                new_output_row_list = str(new_output_row_list).replace("[", "")
                new_output_row_list = str(new_output_row_list).replace("]", "")
                new_output_row_list = str(new_output_row_list).replace("\"", "")
                # new_output_row_list = str(new_output_row_list).replace("||", "\'")
                # new_output_row_list = str(new_output_row_list).replace("\'\'", "\'")
                new_output_row_list = str(new_output_row_list).replace("||", "")
                new_output_row_list = str(new_output_row_list).replace(", ", ",")
                new_output_row_list = str(new_output_row_list).replace("$", "")

                new_output_row_list = new_output_row_list.strip()

                # print("new_output_row_list: " + str(new_output_row_list))
                # fullinputrowlist.append(new_output_row_list)
                # print("---")
                count += 1

                run_count = run_count + 1
            # ---END READING ROWS OF FILE LINES---

            if CONSOLE_OUTPUT_2:
                print("post loop: " + str(new_output_row_list))

                # print("Final Processed Row: [" + str(new_output_row_list[0:4]) + "]")
            # print("fullinputrowlist-f: " + str(fullinputrowlist[0]))
            print("-----------------------------------")
            print("Total Rows Processed: " + str(count))
            print("-----------------------------------")

            # Look for Combined Shipments
            print("-----------------------------------")
            print("COMBINED SHIPMENTS: ")
            print("-----------------------------------")
            combinedshipmentslist = [[]]
            if "buildcombinedshipmentslist" in globkeyfile or "markcombinedshipments" in globkeyfile:

                colplacement_xitor = filekey_1["getcolplacement_xitor"][0]() - 1
                # print(colplacement_xitor)
                colplacement_track = filekey_1["getcolplacement_tracknum"][0]() - 1
                # print(colplacement_track)

            if "buildcombinedshipmentslist" in globkeyfile:
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---FUNCTION \"buildcombinedshipmentslist\" EXECUTED---")
                bcslresults = globkeyfile["buildcombinedshipmentslist"][0](fullinputrowlist, colplacement_xitor,
                                                                                   colplacement_track,
                                                                                   combinedshipmentslist)
                combinedshipmentslist = bcslresults[0]
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---")

            if CONSOLE_OUTPUT_SECTIONS_0:
                print("Matches List Length: " + str(len(combinedshipmentslist)))
                print("Matches List: " + str(combinedshipmentslist))
            # print("fullinputrowlist-f: " + str(fullinputrowlist[0]))



            if "markcombinedshipments" in globkeyfile:
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---FUNCTION \"markcombinedshipments\" EXECUTED---")
                mcsresults = globkeyfile["markcombinedshipments"][0](fullinputrowlist, colplacement_xitor,
                                                                      colplacement_track, combinedshipmentslist,
                                                                      filekey_1)
                fullinputrowlist = mcsresults[0]
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---")

            if "sourcefilekey_processing" in sourceglobkeyfile:
                if sourceglobkeyfile["sourcefilekey_processing"]:
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---FUNCTION \"sourcefilekey_processing\" EXECUTED---")
                    # print(sourceglobkeyfile)
                    sfkpresults = filekey_1["sourcefilekey_processing"][0](fullinputrowlist)
                    fullinputrowlist = sfkpresults[0]
                    if CONSOLE_OUTPUT_SECTIONS_0:
                        print("---")

            if "general_post_processing" in globkeyfile:
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---FUNCTION \"general_post_processing\" EXECUTED---")
                gppresults = globkeyfile["general_post_processing"][0](fullinputrowlist, filekey_1, outputfiletype)
                fullinputrowlist = gppresults[0]
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---")

            if CONSOLE_OUTPUT_2:
                print("post general_post_processing: " + str(fullinputrowlist))

            fullinputrowlistheaderstr = str(fullinputrowlistheader)
            fullinputrowlistheaderstr = str(fullinputrowlistheaderstr).replace("\'", "")
            fullinputrowlistheaderstr = str(fullinputrowlistheaderstr).replace("[", "")
            fullinputrowlistheaderstr = str(fullinputrowlistheaderstr).replace("]", "")
            fullinputrowlistheaderstr = str(fullinputrowlistheaderstr).replace(" ", "")
            # print(fullinputrowlistheaderstr)
            f_err.write(fullinputrowlistheaderstr + "\n")
            f_update.write(fullinputrowlistheaderstr + "\n")
            f_add.write(fullinputrowlistheaderstr + "\n")

            count = "ERROR"

            if "write_row_list_to_files" in globkeyfile:
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---FUNCTION \"write_row_list_to_files\" EXECUTED---")
                wrlfresults = globkeyfile["write_row_list_to_files"][0](fullinputrowlist, firstfile, filekey_1,
                                                                        f_err, f_update, f_add)
                fullinputrowlist = wrlfresults[1]
                count = wrlfresults[2]
                if wrlfresults[0]:
                    print("FILE WRITING COMPLETE")
                if CONSOLE_OUTPUT_SECTIONS_0:
                    print("---")

            print("-----------------------------------")
            print("Total Rows Processed: " + str(count))
            print("-----------------------------------")
        else:
            print("RUN_MODE UNKNOWN")

    if "filecleanup" in globkeyfile:
        print("---FUNCTION \"filecleanup\" EXECUTED---")
        fcresults = globkeyfile["filecleanup"][0](curfilename)
        if fcresults[0]:
            print("FILE CLOSING COMPLETE")
        print("---")



    return False
