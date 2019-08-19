import requests
import sys

inputArgs = sys.argv
if len(inputArgs) < 2:
    print("Invalid input! Sample argument>Python MacAddressLookup.py 44:38:39:ff:ef:57 E8:FC:AF:B9:BE:A2 \nExiting....Try again!")
    sys.exit()
else:
    inputs = inputArgs[1:len(inputArgs)]  # Ignoring ScriptName
    inputLen = len(inputs)

print("\nInput Mac address(s): " + str(inputLen) + ' = ' + str(inputs) + '\n')
output = ""
success = 0
Failed = 0
for mac in inputs:
    response = requests.get(
        'https://api.macaddress.io/v1?apiKey=at_nbp0zMb8d6vchGU6zyPSOOPlogjm4&'
        'output=vendor&'
        'search=' + mac)
    output = output + mac + ' = ' + response.text + '\n'
    if response.status_code == 200:
        success = success + 1
    else:
        Failed = Failed + 1

print("### Result Start ###\n" + output + "### Result End ###")
print("Total Count=" + str(inputLen) + "; Success Count=" + str(success) + '; Failure Count=' + str(Failed))
print("* Completed *")
