import datetime
import json
import os
import socket
import urllib.request


##########################################
#       Created By Cod3Br3ak3r           #
#       github.com/codebreaker444        #
##########################################
class cb_colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[0;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    COLOR_OFF = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class cb_api_merger(object):
    def cb_merger_initializing(self):  ##  Initializes the time,checks internet availability
        cm_t = datetime.datetime.now()
        global cm_for_t
        cm_for_t = cm_t.strftime("%Y-%m-%d-%H.%M")
        REMOTE_SERVER = "www.google.com"
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            print(cb_colors.GREEN + "Internet Connection Present" + cb_colors.COLOR_OFF)
            return True
        except:
            pass
            print("Connection Error!!", end='')
            return False

    def cb_merger_inputs(self):  ##  Takes Input from the USER
        global cb_f_name, cmi_url, cmi_page_start, cmi_page_end
        cb_f_name = cm_for_t + "_CB_API_MERGER.txt"
        # print(cb_f_name)
        print(cb_colors.RED + "Note:Enter Without the Page or Form Number...\nEg:http://localhost/api?page=0 --> http://localhost/api?page=  " + cb_colors.COLOR_OFF)
        cmi_url = str(input(cb_colors.BLUE + "Enter Url:" + cb_colors.COLOR_OFF))
        cmi_page_start = int(input(cb_colors.BLUE + "Enter Starting Page:" + cb_colors.COLOR_OFF))
        cmi_page_end = int(input(cb_colors.BLUE + "Enter Ending Page:" + cb_colors.COLOR_OFF))
        return True

    def cb_merger_collect(self):  ##  Collects and Stored the JSON data from given URL
        error = ""
        if os.path.exists(cb_f_name):
            os.remove(cb_f_name)
            print(cb_colors.RED + "Removed existing File.." + cb_colors.COLOR_OFF)
            print("Creating File as : " + cb_f_name)
        else:
            print("Creating File as : " + cb_f_name)
        for i in range(cmi_page_start, cmi_page_end + 1):
            url1 = cmi_url
            url1 += str(i)
            print(url1)
            try:
                print(cb_colors.BLUE + "Loading URL..." + cb_colors.COLOR_OFF)
                urllib.request.urlopen(url1)
            except:
                error = "True"
            if error != "True":
                try:
                    with urllib.request.urlopen(url1) as url:
                        data = json.loads(url.read().decode())
                        print(cb_colors.BLUE + "URL:", url1, " --Loaded" + cb_colors.COLOR_OFF)
                        with open(cb_f_name, 'a') as outfile:
                            json.dump(data, outfile, indent=1)
                            print(cb_colors.GREEN + "///Data SuccessFully Dumped" + cb_colors.COLOR_OFF)
                except ValueError as e:
                    print(cb_colors.RED + "Not Valid JSON URL...Exiting!" + cb_colors.COLOR_OFF)
                    return False
            else:
                print(cb_colors.RED + "URL Error!Please check the URL by opening in Browser.." + cb_colors.COLOR_OFF)
                return False
        if i == cmi_page_end:
            return True

    def cb_merger_correction(
            self):  ## Corrects the JSON Data if different pages has their own array and combines them into single array
        global j
        j = 0
        with open(cb_f_name, 'r+') as f:
            print("Correcting Data....")
            data = f.read()
            f.seek(0)
            data = data.replace('[', '')
            data = data.replace(']', '')
            data = data.replace('\n\n', '\n')
            data = data.replace('},', '}')
            data = data.replace('}', '},')
        with open(cb_f_name, 'w') as f:
            f.write(data)
        with open(cb_f_name, 'r') as f:
            lines = f.readlines()
            f.seek(0)
        with open(cb_f_name, 'w') as f:
            f.write("[")
        with open(cb_f_name, 'a') as f:
            for line in lines[:-1]:
                j += 1
                f.write(line)
        with open(cb_f_name, 'a') as outfile:
            outfile.write("}]")
            print(cb_colors.GREEN + "Data Corrected..." + cb_colors.COLOR_OFF)
            return True

    def cb_merger_validation(self):  ## Validates the Final JSON Data...(Post isuues if it fails.)
        print("Validating JSON Data..")
        with open(cb_f_name, 'r') as outfile:
            try:
                json.load(outfile)
                print(cb_colors.GREEN + "JSON Data Successfully Validated" + cb_colors.COLOR_OFF)
                return True
            except ValueError as e:
                print(
                    cb_colors.RED + "Cannot Validate Data..!Post an issue in github with console log.." + cb_colors.COLOR_OFF,
                    e)
                return False


if cb_api_merger().cb_merger_initializing():
    if cb_api_merger().cb_merger_inputs():
        if cb_api_merger().cb_merger_collect():
            if cb_api_merger().cb_merger_correction():
                if cb_api_merger().cb_merger_validation():
                    print(
                        cb_colors.BOLD + cb_colors.GREEN + "Thank_You For Using CB API MERGER.." + cb_colors.COLOR_OFF)
                else:
                    print("Error At Validation")
            else:
                print("Error at Correction")
        else:
            print("Error at Collection")
    else:
        print("Error at Inputs")
else:
    print("Error at Initialization")


    ##      FEEl FREE TO CHANGE THE CODE AND HAVE FUN....Cheers Cod3Br3ak3r
