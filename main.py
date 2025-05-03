import CNE_DataCompiler_CreateOutput2
import SourceFileKey_Ebay_Shipping
import Helpers1


filesToProcess = []
# filesToProcess.append("STX-Amazon-AO")
# outputfiletype = "STX"
# filesToProcess.append("SLN-Amazon-AO")
# outputfiletype = "SLN"
# filesToProcess.append("Veeqo-Orders-STX")
# outputfiletype = "STX"
filesToProcess.append("SFE-Amazon-UTR")
outputfiletype = "SFE"


# filesToProcess.append("ShipRush")  #ShipRush Shipments Report
# outputfiletype = "SHP"
# filesToProcess.append("Ebay-Shipping")  #
# outputfiletype = "SHP"
# filesToProcess.append("Ebay-Orders")  #
# outputfiletype = "SHP"
# filesToProcess.append("Veeqo")  #
# outputfiletype = "SHP"

globkeyfileresults = Helpers1.setglobalkeyfile(filesToProcess[0])
genglobkeyfile = globkeyfileresults[0]
sourceglobkeyfile = globkeyfileresults[1]
if genglobkeyfile is None:
    print("***ERROR***: globkeyfile is None")
else:
    CNE_DataCompiler_CreateOutput2.processfile(True, filesToProcess, genglobkeyfile, sourceglobkeyfile, outputfiletype)
