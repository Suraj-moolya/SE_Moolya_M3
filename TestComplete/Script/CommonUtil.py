"""CommonUtil"""
import xml.etree.ElementTree as elementTree
import os
import datetime

def create_text_file():
    """create_text_file"""
    if not Project.Variables.VariableExists("textfile_path"):
        Project.Variables.AddVariable("textfile_path", "String")
    report_name= get_current_datetime()
    remove_char = [":","."," "]
    for char in remove_char:
        report_name=report_name.replace(char,"_")
    Project.Variables.textfile_path = os.path.abspath(os.path.join(os.getcwd(), report_name+"_report.txt"))

  
def get_version(softwareName):
    computerName="."
    wbemImpersonationLevelImpersonate = 3
    Locator = Sys.OleObject["WbemScripting.SWbemLocator"]
    Locator.Security_.ImpersonationLevel = wbemImpersonationLevelImpersonate
    services = Locator.ConnectServer (computerName, "root\cimv2")
    objectsList = services.InstancesOf("Win32_Product")
    for i in range (0, objectsList.Count - 1):
     if (objectsList.ItemIndex(i).Name == softwareName):
        return objectsList.ItemIndex(i).Version
  
def get_manufacturer():
    computerName="."
    wbemImpersonationLevelImpersonate = 3
    Locator = Sys.OleObject["WbemScripting.SWbemLocator"]
    Locator.Security_.ImpersonationLevel = wbemImpersonationLevelImpersonate
    services = Locator.ConnectServer (computerName, "root\cimv2")
    objectsList = services.InstancesOf("Win32_ComputerSystem")
    return objectsList.ItemIndex(0).Manufacturer

def get_model():
    computerName="."
    wbemImpersonationLevelImpersonate = 3
    Locator = Sys.OleObject["WbemScripting.SWbemLocator"]
    Locator.Security_.ImpersonationLevel = wbemImpersonationLevelImpersonate
    services = Locator.ConnectServer (computerName, "root\cimv2")
    objectsList = services.InstancesOf("Win32_ComputerSystem")
    return objectsList.ItemIndex(0).Model
  
def getRAM():
    computerName="."
    wbemImpersonationLevelImpersonate = 3
    Locator = Sys.OleObject["WbemScripting.SWbemLocator"]
    Locator.Security_.ImpersonationLevel = wbemImpersonationLevelImpersonate
    services = Locator.ConnectServer (computerName, "root\cimv2")
    objectsList = services.InstancesOf("Win32_OperatingSystem")
    ram = aqConvert.StrToInt(objectsList.ItemIndex(0).TotalVisibleMemorySize)
    return (str(ram/1048576) + " GB")

def getWIPversion():
    s = aqFile.ReadWholeTextFile("C:\\pms\\manual\\version.js", aqFile.ctANSI)
    str = aqString.Replace(s, "$", "")
    str = aqString.Replace(str, "\r\n"," ")
    return(str)

def get_system_info2():
  Log.Message("Location : Simulator")
  Log.Message("USS Version : ")
  Log.Message("Host Model : " + "HAWK 128")
  Log.Message("PHCT_ScannerVersion : ")
  Log.Message("WIP Version : ")

  Log.Message("Manufacturer : ")
  Log.Message("Model : ")
  Log.Message("System Type : " + str(Sys.OSInfo.FullName))
  Log.Message("DNS Hostname : " + str(Sys.HostName))
  Log.Message("Total Physical Memory (RAM) : " + str(Sys.MemUsage))
  
  Log.Message("Hard Drive Information:-")
  Log.Message("Drive C : " + str(aqFileSystem.GetDriveInfo("C").TotalSize))
  Log.Message("Drive D : " + str(aqFileSystem.GetDriveInfo("D").TotalSize))
  Log.Message("CPU data : " + str(Sys.CPU))
  Log.Message("CPU core : " + str(Sys.CPUCount))

def get_current_datetime():
    """get_current_datetime"""
    return str(datetime.datetime.now())

def write_text_file(text):
    """get_application_data"""
    pass
#    append_mode = open(Project.Variables.textfile_path, "a")
#    append_mode.writelines(text)
#    append_mode.close()

def get_application_data(xml_node):
    """get_application_data"""
    #Log.Message(os.getcwd())
    xmlpath = os.path.abspath(os.path.join(os.getcwd(), "ApplicationSettings.xml"))
    tree = elementTree.parse(xmlpath)
    root = tree.getroot()
    return str(root.find(xml_node).text)


def delete_files(folderpath):
    """delete files"""
    # folder = '/path/to/folder'
    for the_file in os.listdir(folderpath):
        file_path = os.path.join(folderpath, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as ex:
            raise Exception(ex) from ex

def rename_file(path, filename):
    """rename file"""
    try:
        newfilename = os.path.join(path,filename + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png",)
        os.rename(os.path.join(path, filename + ".png"), newfilename)
    except WindowsError:
        print("image not found to rename:" + newfilename)
