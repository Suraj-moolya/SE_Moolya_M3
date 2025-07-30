"""HOOKS"""
import Applicationutility
import CommonUtil
import Engineeringclientutility

#@beforefeature
#def before_feature(feature):#pylint: disable = unused-argument
#    """before_feature"""
#    if not Project.Variables.VariableExists("time_interval"):
#        Project.Variables.AddVariable("time_interval", "Integer")
#    Project.Variables.time_interval = CommonUtil.get_application_data("TimeIntervalInMilliSeconds")
#    
#    if not Project.Variables.VariableExists("username"):
#      Project.Variables.AddVariable("username", "String")
#    Project.Variables.username = "SE_Moolya_Test"
#      
#    if not Project.Variables.VariableExists("password"):
#      Project.Variables.AddVariable("password", "String")
#    Project.Variables.password = "P@ssw0rd1234"

      
#@beforescenario
#def before_scenario(scenario):
#    """before_scenario"""
#    try:
#        CommonUtil.write_text_file("\n**************** Scenario Start*************************\n")
#        start_time= CommonUtil.get_current_datetime()
#        CommonUtil.write_text_file("Start Time:"+start_time+"\n")
#        CommonUtil.write_text_file("Scenario outline:"+scenario.Name)
#        if Project.Variables.VariableExists("retry_count"):
#            Project.Variables.RemoveVariable("retry_count")
#        if Project.Variables.VariableExists("time_interval"):
#            Project.Variables.RemoveVariable("time_interval")
#        if not Project.Variables.VariableExists("time_interval"):
#            Project.Variables.AddVariable("time_interval", "Integer")
#        Project.Variables.time_interval = CommonUtil.get_application_data("TimeIntervalInMilliSeconds")
#        if not Project.Variables.VariableExists("retry_count"):
#            Project.Variables.AddVariable("retry_count", "Integer")
#        Project.Variables.retry_count = CommonUtil.get_application_data("RetryCount")
#        
#        if not Project.Variables.VariableExists("username"):
#          Project.Variables.AddVariable("username", "String")
#        Project.Variables.username = "SE_Moolya_Test"
#      
#        if not Project.Variables.VariableExists("password"):
#          Project.Variables.AddVariable("password", "String")
#        Project.Variables.password = "P@ssw0rd1234"
#
#        if '$$' in scenario.Name:
#          Engineeringclientutility.close_EC_ok_on_trial_pop_up()
#          Applicationutility.close_system_server()
#        else:
#          Applicationutility.launch_system_server_engineering_client()
#
#    except Exception as ex:
#        Log.Message(ex)
#
#@afterscenario
#def after_scenario(scenario):#pylint: disable = unused-argument
#    """after_scenario"""
#    try:
#        #Applicationutility.close_system_server_1()
#        CommonUtil.write_text_file("\n**************** Scenario End*************************\n")
#        end_time= CommonUtil.get_current_datetime()
#        CommonUtil.write_text_file("End Time:"+end_time+"\n")
#    except Exception as ex:
#        print(ex)
#
def on_log_message(sender, logparams):#pylint: disable = unused-argument
    """on_log_message"""
    pass
#    if "--" not in logparams.MessageText.upper() and "FILEPATH:" not in logparams.MessageText.upper():
#        CommonUtil.write_text_file("|| Log Message:"+logparams.MessageText)
#    elif "FILEPATH:" in logparams.MessageText.upper():
#        CommonUtil.write_text_file("|| Log Picture:"+logparams.MessageText)

def on_log_error(sender, logparams):#pylint: disable = unused-argument
    """on_log_error"""
    pass
#    CommonUtil.write_text_file("|| Log Error:"+logparams.MessageText)

def on_log_picture(sender, logparams, logfileparams):#pylint: disable = unused-argument
    """on_log_picture"""
    pass
#    if "Full Screenshot" in logparams.MessageText:
#        CommonUtil.write_text_file("|| Log Picture:"+logfileparams.DestFileName)

def on_start_test(sender):#pylint: disable = unused-argument
    """on_start_test"""
    pass
#    CommonUtil.create_text_file()

def on_log_checkpoint(sender, logparams):#pylint: disable = unused-argument
    """on_log_checkpoint"""
    pass
#    if "--" not in logparams.MessageText:
#        CommonUtil.write_text_file("|| Log Message:"+logparams.MessageText)
