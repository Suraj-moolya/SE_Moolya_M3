"""ApplicationExplorerTabWorkFlow"""
from ApplicationExplorerTabWorkFlow import ApplicationExplorerTabWorkFlow
import CommonUtil
import Applicationutility
import Applicationexplorertabutility

obj=ApplicationExplorerTabWorkFlow()

        
@when("I Expand template browser AE Templates browser Application in application explorer as {arg}")
def step_impl(templatesBrowserApplication1):
    """I Expand template browser AE Templates browser Application in application explorer as '<Templates browser Application1>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Templates browser Application in application explorer as \""+templatesBrowserApplication1+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(templatesBrowserApplication1)
  
@when("I Expand template browser AE Templates browser STAHL in application explorer as {arg}")
def step_impl(templatesBrowserStahl2):
    """I Expand template browser AE Templates browser STAHL in application explorer as '<Templates browser STAHL2>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Templates browser STAHL in application explorer as \""+templatesBrowserStahl2+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(templatesBrowserStahl2)
  
@then("verify composite template AE Templates browser in application explorer")
def step_impl():
    """verify composite template AE Templates browser in application explorer"""
    CommonUtil.write_text_file("\nThen verify composite template AE Templates browser in application explorer")
    obj.textboxtemplatesbrowserverifycompositetemplateae()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Collapse template browser AE STAHL in application explorer as {arg}")
def step_impl(stahl3):
    """I Collapse template browser AE STAHL in application explorer as '<STAHL3>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE STAHL in application explorer as \""+stahl3+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(stahl3)
  
@when("I Expand template browser AE Time Stamping in application explorer as {arg}")
def step_impl(timeStamping4):
    """I Expand template browser AE Time Stamping in application explorer as '<Time Stamping4>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Time Stamping in application explorer as \""+timeStamping4+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(timeStamping4)
  
@when("I scroll down template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser5):
    """I scroll down template browser AE Templates browser in application explorer as '<Templates browser5>'"""
    CommonUtil.write_text_file("\nWhen I scroll down template browser AE Templates browser in application explorer as \""+templatesBrowser5+"\"")
    obj.textboxtemplatesbrowserscrolldowntemplatebrowserae(templatesBrowser5)
  
@when("I Collapse template browser AE Time Stamping in application explorer as {arg}")
def step_impl(timeStamping6):
    """I Collapse template browser AE Time Stamping in application explorer as '<Time Stamping6>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Time Stamping in application explorer as \""+timeStamping6+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(timeStamping6)
  
@when("I Expand template browser AE Unity Array Variables in application explorer as {arg}")
def step_impl(unityArrayVariables7):
    """I Expand template browser AE Unity Array Variables in application explorer as '<Unity Array Variables7>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Unity Array Variables in application explorer as \""+unityArrayVariables7+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(unityArrayVariables7)
  
@when("I Collapse template browser AE Unity Array Variables in application explorer as {arg}")
def step_impl(unityArrayVariables8):
    """I Collapse template browser AE Unity Array Variables in application explorer as '<Unity Array Variables8>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Unity Array Variables in application explorer as \""+unityArrayVariables8+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(unityArrayVariables8)
  
@when("I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as {arg}")
def step_impl(unityElementaryTimeStampedVariables9):
    """I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables9>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as \""+unityElementaryTimeStampedVariables9+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(unityElementaryTimeStampedVariables9)
  
@when("I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as {arg}")
def step_impl(unityElementaryTimeStampedVariables11):
    """I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables11>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as \""+unityElementaryTimeStampedVariables11+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(unityElementaryTimeStampedVariables11)
  
@when("I Expand template browser AE Owner_Consumer Templates in application explorer as {arg}")
def step_impl(ownerconsumerTemplates12):
    """I Expand template browser AE Owner_Consumer Templates in application explorer as '<Owner_Consumer Templates12>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Owner_Consumer Templates in application explorer as \""+ownerconsumerTemplates12+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(ownerconsumerTemplates12)
  
@when("I Collapse template browser AE Unity Peer to Peer in application explorer as {arg}")
def step_impl(unityPeerToPeer13):
    """I Collapse template browser AE Unity Peer to Peer in application explorer as '<Unity Peer to Peer13>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Unity Peer to Peer in application explorer as \""+unityPeerToPeer13+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(unityPeerToPeer13)
  
@when("I Expand template browser AE Advantys in application explorer as {arg}")
def step_impl(advantys14):
    """I Expand template browser AE Advantys in application explorer as '<Advantys14>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Advantys in application explorer as \""+advantys14+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(advantys14)
  
@when("I Collapse template browser AE Advantys in application explorer as {arg}")
def step_impl(advantys15):
    """I Collapse template browser AE Advantys in application explorer as '<Advantys15>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Advantys in application explorer as \""+advantys15+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(advantys15)
  
@when("I Expand template browser AE M340 in application explorer as {arg}")
def step_impl(m34016):
    """I Expand template browser AE M340 in application explorer as '<M34016>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE M340 in application explorer as \""+m34016+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(m34016)
  
@when("I Collapse template browser AE M340 in application explorer as {arg}")
def step_impl(m34017):
    """I Collapse template browser AE M340 in application explorer as '<M34017>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE M340 in application explorer as \""+m34017+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(m34017)
  
@when("I Expand template browser AE M580 in application explorer as {arg}")
def step_impl(m58018):
    """I Expand template browser AE M580 in application explorer as '<M58018>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE M580 in application explorer as \""+m58018+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(m58018)
  
@when("I Collapse template browser AE M580 in application explorer as {arg}")
def step_impl(m58019):
    """I Collapse template browser AE M580 in application explorer as '<M58019>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE M580 in application explorer as \""+m58019+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(m58019)
  
@when("I Expand template browser AE Quantum in application explorer as {arg}")
def step_impl(quantum20):
    """I Expand template browser AE Quantum in application explorer as '<Quantum20>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE Quantum in application explorer as \""+quantum20+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(quantum20)
  
@when("I Collapse template browser AE Foundation Library in application explorer as {arg}")
def step_impl(foundationLibrary21):
    """I Collapse template browser AE Foundation Library in application explorer as '<Foundation Library21>'"""
    CommonUtil.write_text_file("\nWhen I Collapse template browser AE Foundation Library in application explorer as \""+foundationLibrary21+"\"")
    obj.textboxstahlcollapsetemplatebrowserae(foundationLibrary21)
  
@when("I Expand template browser AE General Purpose Library in application explorer as {arg}")
def step_impl(generalPurposeLibrary22):
    """I Expand template browser AE General Purpose Library in application explorer as '<General Purpose Library22>'"""
    CommonUtil.write_text_file("\nWhen I Expand template browser AE General Purpose Library in application explorer as \""+generalPurposeLibrary22+"\"")
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(generalPurposeLibrary22)
  
@then("verify template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser):
    """verify template browser AE Templates browser in application explorer as '<Templates browser>'"""
    CommonUtil.write_text_file("\nThen verify template browser AE Templates browser in application explorer as \""+templatesBrowser+"\"")
    obj.textboxtemplatesbrowserverifytemplatebrowserae()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I close all tabs except system explorer EC Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser23):
    """I close all tabs except system explorer EC Templates browser in application explorer as '<Templates browser23>'"""
    CommonUtil.write_text_file("\nWhen I close all tabs except system explorer EC Templates browser in application explorer as \""+templatesBrowser23+"\"")
    obj.textboxtemplatesbrowserclosealltabsexceptsystemexplorerec()
  
@when("I search text template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser1):
    """I search text template browser AE Templates browser in application explorer as '<Templates browser1>'"""
    CommonUtil.write_text_file("\nWhen I search text template browser AE Templates browser in application explorer as \""+templatesBrowser1+"\"")
    obj.textboxtemplatesbrowsersearchtexttemplatebrowserae(templatesBrowser1)
  
@when("I drag composite template drop application browser system1 AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser2):
    """I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'"""
    CommonUtil.write_text_file("\nWhen I drag composite template drop application browser system1 AE Templates browser in application explorer as \""+templatesBrowser2+"\"")
    obj.textboxtemplatesbrowserdragcompositetemplatedropapplicationbrowsersystem1ae(templatesBrowser2)
 
@when("I rclick asset workspace folder AE Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace4):
    """I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'"""
    CommonUtil.write_text_file("\nWhen I rclick asset workspace folder AE Asset workspace in application explorer as \""+assetWorkspace4+"\"")
    obj.textboxassetworkspacerclickassetworkspacefolderae(assetWorkspace4)
  
@when("I Select context menu item EC Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace5):
    """I Select context menu item EC Asset workspace in application explorer as '<Asset workspace5>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC Asset workspace in application explorer as \""+assetWorkspace5+"\"")
    obj.textboxassetworkspaceselectcontextmenuitemec(assetWorkspace5)
  
@when("I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as {arg}")
def step_impl(assertWorkspaceEditor8):
    """I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor8>'"""
    CommonUtil.write_text_file("\nWhen I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as \""+assertWorkspaceEditor8+"\"")
    obj.textboxassertworkspaceeditordragtemplateinapplicationbrowserdropassetworkspaceeditorae(assertWorkspaceEditor8)
  
@then("Verify Template AE Assert Workspace Editor in application explorer as {arg}")
def step_impl(assertWorkspaceEditor9):
    """Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'"""
    CommonUtil.write_text_file("\nThen Verify Template AE Assert Workspace Editor in application explorer as \""+assertWorkspaceEditor9+"\"")
    obj.textboxassertworkspaceeditorverifytemplateae(assertWorkspaceEditor9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Link from range node to range node AE Node Instance in application explorer as {arg}")
def step_impl(rsprangedpvranged):
    """I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'"""
    CommonUtil.write_text_file("\nWhen I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'")
    obj.buttonnodeinstancelinkfromrangenodetorangenodeae(rsprangedpvranged)
  
@then("Verify Link Status Node Instance in application explorer")
def step_impl():
    """Verify Link Status Node Instance in application explorer"""
    CommonUtil.write_text_file("\nThen Verify Link Status Node Instance in application explorer")
    obj.buttonnodeinstanceverifylinkstatus()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I rclick application browser folder AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser3):
    """I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'"""
    CommonUtil.write_text_file("\nWhen I rclick application browser folder AE Application browser in application explorer as \""+applicationBrowser3+"\"")
    obj.textboxapplicationbrowserrclickapplicationbrowserfolderae(applicationBrowser3)
  
@when("I rclick application browser template AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser4):
    """I rclick application browser template AE Application browser in application explorer as '<Application browser4>'"""
    CommonUtil.write_text_file("\nWhen I rclick application browser template AE Application browser in application explorer as \""+applicationBrowser4+"\"")
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(applicationBrowser4)
  
@when("I Select context menu item EC Application browser in application explorer as {arg}")
def step_impl(applicationBrowser5):
    """I Select context menu item EC Application browser in application explorer as '<Application browser5>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC Application browser in application explorer as \""+applicationBrowser5+"\"")
    obj.textboxapplicationbrowserselectcontextmenuitemec(applicationBrowser5)
    Applicationutility.wait_in_seconds(2000, 'Wait')
    
@when("I Rename the Insatnce to the requirement {arg}")
def step_impl(Name1):
    """I Rename the Insatnce to the requirement '<Name1>'"""
    CommonUtil.write_text_file("\nI Rename the Insatnce to the requirement \""+Name1+"\"")
    obj.textboxRenameInsatnce(Name1)
  
@then("verify inspect instance window open Inspect instance tree in inspect instance as {arg}")
def step_impl(inspectInstanceTree6):
    """verify inspect instance window open Inspect instance tree in inspect instance as '<Inspect instance tree6>'"""
    CommonUtil.write_text_file("\nThen verify inspect instance window open Inspect instance tree in inspect instance as \""+inspectInstanceTree6+"\"")
    obj.textboxinspectinstancetreeverifyinspectinstancewindowopen(inspectInstanceTree6)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Inspect instance ok in inspect instance")
def step_impl():
    """I selected Inspect instance ok in inspect instance"""
    CommonUtil.write_text_file("\nWhen I selected Inspect instance ok in inspect instance")
    obj.buttoninspectinstanceokselected()
  
@when("I Close inspect instance window AE Inspect instance window in inspect instance")
def step_impl():
    """I Close inspect instance window AE Inspect instance window in inspect instance as '<Inspect instance window>'"""
    obj.textboxinspectinstancewindowcloseinspectinstancewindowae()
  
@when("I Esc keyboard action Inspect instance window in inspect instance")
def step_impl():
    """I Esc keyboard action Inspect instance window in inspect instance as '<Inspect instance window>'"""
    obj.textboxinspectinstancewindowesckeyboardaction()

@when("I Create system and create instance Create Multiple instance in application explorer")
def step_impl():
    """I Create system and create instance Create Multiple instance in application explorer"""
    CommonUtil.write_text_file("\nWhen I Create system and create instance Create Multiple instance in application explorer")
    obj.buttoncreatemultipleinstancecreatesystemandcreateinstance()
  
@then("Verify folder created Identifier in application browser as {arg}")
def step_impl(identifier1):
    """Verify folder created Identifier in application browser as '<Identifier1>'"""
    CommonUtil.write_text_file("\nThen Verify folder created Identifier in application browser as \""+identifier1+"\"")
    obj.textboxidentifierverifyfoldercreated(identifier1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify template created Identifier MotorGP_1 in application browser as {arg}")
def step_impl(identifierMotorgp13):
    """Verify template created Identifier MotorGP_1 in application browser as '<Identifier MotorGP_13>'"""
    CommonUtil.write_text_file("\nThen Verify template created Identifier MotorGP_1 in application browser as \""+identifierMotorgp13+"\"")
    obj.textboxidentifiermotorgp1verifytemplatecreated(identifierMotorgp13)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify template created Identifier ValveGP_1 in application browser as {arg}")
def step_impl(identifierValvegp14):
    """Verify template created Identifier ValveGP_1 in application browser as '<Identifier ValveGP_14>'"""
    CommonUtil.write_text_file("\nThen Verify template created Identifier ValveGP_1 in application browser as \""+identifierValvegp14+"\"")
    obj.textboxidentifiermotorgp1verifytemplatecreated(identifierValvegp14)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I double click on template Identifier in application browser as {arg}")
def step_impl(identifier5):
    """I double click on template Identifier in application browser as '<Identifier5>'"""
    CommonUtil.write_text_file("\nWhen I double click on template Identifier in application browser as \""+identifier5+"\"")
    obj.textboxidentifierdoubleclickontemplate(identifier5)
  
@then("Verify template instance editor Instance Editor in application explorer as {arg}")
def step_impl(instanceEditor6):
    """Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'"""
    CommonUtil.write_text_file("\nThen Verify template instance editor Instance Editor in application explorer as \""+instanceEditor6+"\"")
    obj.textboxinstanceeditorverifytemplateinstanceeditor(instanceEditor6)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I take evidence Instance Editor in application explorer")
def step_impl():
    """I take evidence Instance Editor in application explorer"""
    CommonUtil.write_text_file("\nWhen I take evidence Instance Editor in application explorer")
    obj.textboxinstanceeditortakeevidence()
  
@when("I Check instance editor Instance editor checklist in application explorer as {arg}")
def step_impl(instanceEditorChecklist7):
    """I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist7>'"""
    CommonUtil.write_text_file("\nWhen I Check instance editor Instance editor checklist in application explorer as \""+instanceEditorChecklist7+"\"")
    obj.textboxinstanceeditorchecklistcheckinstanceeditor(instanceEditorChecklist7)
  
@when("I Enter description AE Instance description in application explorer")
def step_impl():
    """I Enter description AE Instance description in application explorer"""
    CommonUtil.write_text_file("\nWhen I Enter description AE Instance description in application explorer")
    obj.buttoninstancedescriptionenterdescriptionae()
  
@when("I selected Instance editor save in application explorer")
def step_impl():
    """I selected Instance editor save in application explorer"""
    CommonUtil.write_text_file("\nWhen I selected Instance editor save in application explorer")
    obj.buttoninstanceeditorsaveselected()
  
@when("I Close instance editor tab Instance editor close in application explorer as {arg}")
def step_impl(instanceEditorClose8):
    """I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'"""
    CommonUtil.write_text_file("\nWhen I Close instance editor tab Instance editor close in application explorer as \""+instanceEditorClose8+"\"")
    obj.textboxinstanceeditorclosecloseinstanceeditortab(instanceEditorClose8)
  
@then("verify popup AE Save changes dialogbox in application explorer as {arg}")
def step_impl(saveChangesDialogbox9):
    """verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'"""
    CommonUtil.write_text_file("\nThen verify popup AE Save changes dialogbox in application explorer as \""+saveChangesDialogbox9+"\"")
    obj.textboxsavechangesdialogboxverifypopupae(saveChangesDialogbox9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Save changes dialogbox yes in application explorer")
def step_impl():
    """I selected Save changes dialogbox yes in application explorer"""
    CommonUtil.write_text_file("\nWhen I selected Save changes dialogbox yes in application explorer")
    obj.buttonsavechangesdialogboxyesselected()
  
@when("I selected Save changes dialogbox no in application explorer")
def step_impl():
    """I selected Save changes dialogbox no in application explorer"""
    CommonUtil.write_text_file("\nWhen I selected Save changes dialogbox no in application explorer")
    obj.buttonsavechangesdialogboxnoselected()
  
@when("I selected Save changes dialogbox cancel in application explorer")
def step_impl():
    """I selected Save changes dialogbox cancel in application explorer"""
    CommonUtil.write_text_file("\nWhen I selected Save changes dialogbox cancel in application explorer")
    obj.buttonsavechangesdialogboxcancelselected()
  
@when("I rclick application browser template AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate5):
    """I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template5>'"""
    CommonUtil.write_text_file("\nWhen I rclick application browser template AE MotorGP template in application explorer as \""+motorgpTemplate5+"\"")
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(motorgpTemplate5)
  
@then("verify context menu items ContextMenu in application explorer")
def step_impl():
    """verify context menu items ContextMenu in application explorer"""
    CommonUtil.write_text_file("\nThen verify context menu items ContextMenu in application explorer")
    obj.textboxcontextmenuverifycontextmenuitems()
    Applicationutility.take_screenshot("Full Screenshot")
    
@then("verify the status of the instance")
def step_impl():
    obj.textboxverifyinstancevalidity()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Select context menu item EC ContextMenu in application explorer as {arg}")
def step_impl(contextmenu6):
    """I Select context menu item EC ContextMenu in application explorer as '<ContextMenu6>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC ContextMenu in application explorer as \""+contextmenu6+"\"")
    obj.textboxassetworkspaceselectcontextmenuitemec(contextmenu6)
  
@when("I rclick application browser folder AE Folder_2 in application explorer as {arg}")
def step_impl(folder27):
    """I rclick application browser folder AE Folder_2 in application explorer as '<Folder_27>'"""
    CommonUtil.write_text_file("\nWhen I rclick application browser folder AE Folder_2 in application explorer as \""+folder27+"\"")
    obj.textboxapplicationbrowserrclickapplicationbrowserfolderae(folder27)
  
@then("Verify template created Application browser template in application explorer as {arg}")
def step_impl(applicationBrowserTemplate9):
    """Verify template created Application browser template in application explorer as '<Application browser template9>'"""
    CommonUtil.write_text_file("\nThen Verify template created Application browser template in application explorer as \""+applicationBrowserTemplate9+"\"")
    obj.textboxidentifiermotorgp1verifytemplatecreated(applicationBrowserTemplate9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I double click on template Identifier ValveGP_1 in application browser as {arg}")
def step_impl(identifierValvegp15):
    """I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'"""
    CommonUtil.write_text_file("\nWhen I double click on template Identifier ValveGP_1 in application browser as \""+identifierValvegp15+"\"")
    obj.textboxidentifierdoubleclickontemplate(identifierValvegp15)
  
@then("Verify instance lock popup Warning popup window in application explorer as {arg}")
def step_impl(warningPopupWindow11):
    """Verify instance lock popup Warning popup window in application explorer as '<Warning popup window11>'"""
    CommonUtil.write_text_file("\nThen Verify instance lock popup Warning popup window in application explorer as \""+warningPopupWindow11+"\"")
    obj.textboxwarningpopupwindowverifyinstancelockpopup(warningPopupWindow11)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected AE warning popup ok in application explorer")
def step_impl():
    """I selected AE warning popup ok in application explorer"""
    CommonUtil.write_text_file("\nWhen I selected AE warning popup ok in application explorer")
    obj.buttonaewarningpopupokselected()
  
@when("I Create multiple folders and instances AE Create Multiple instance in application explorer")
def step_impl():
    """I Create multiple folders and instances AE Create Multiple instance in application explorer"""
    CommonUtil.write_text_file("\nWhen I Create multiple folders and instances AE Create Multiple instance in application explorer")
    obj.buttoncreatemultipleinstancecreatemultiplefoldersandinstancesae()
  
@when("I rclick application browser template AE Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace3):
    """I rclick application browser template AE Asset workspace in application explorer as '<Asset workspace3>'"""
    CommonUtil.write_text_file("\nWhen I rclick application browser template AE Asset workspace in application explorer as \""+assetWorkspace3+"\"")
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(assetWorkspace3)

  
@when("I uncheck all filters temp browser AE Templates browser in application explorer")
def step_impl():
    """I uncheck all filters temp browser AE Templates browser in application explorer"""
    CommonUtil.write_text_file("\nWhen I uncheck all filters temp browser AE Templates browser in application explorer")
    obj.textboxtemplatesbrowseruncheckallfilterstempbrowserae()
  
@when("I entered Application browser in application explorer")
def step_impl():
    """I entered Application browser in application explorer"""
    obj.textboxapplicationbrowserentered()

@then("Verify version in application explorer as {arg}")
def step_impl(applicationBrowser):
    """I entered Application browser in application explorer as '<Application browser>'"""
    CommonUtil.write_text_file("\nWhen I entered Application browser in application explorer as \""+applicationBrowser+"\"")
    obj.verifyaeapplicationbrowsertemplate(applicationBrowser)

@when("I Enter FileLocation and FileName to be Imported Import in import dialog as {arg}")
def step_impl(import3):
    """I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'"""
    CommonUtil.write_text_file("\nWhen I Enter FileLocation and FileName to be Imported Import in import dialog as \""+import3+"\"")
    obj.textboximportenterfilelocationandfilenametobeimported(import3)
  
@when("I Click on Buttons in Import System1 Popup_AE Import in import dialog as {arg}")
def step_impl(import4):
    """I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'"""
    CommonUtil.write_text_file("\nWhen I Click on Buttons in Import System1 Popup_AE Import in import dialog as \""+import4+"\"")
    obj.textboximportclickonbuttonsinimportsystem1popupae(import4)
  
@when("I Wait for Import popup Import in import dialog")
def step_impl():
    """I Wait for Import popup Import in import dialog"""
    CommonUtil.write_text_file("\nWhen I Wait for Import popup Import in import dialog")
    obj.textboximportwaitforimportpopup()
  
@when("I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as {arg}")
def step_impl(ok):
    """I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'"""
    CommonUtil.write_text_file("\nWhen I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'")
    obj.buttonimportdialogclickonbuttonsinimportdialogpopupae(ok)
  
@then("I Delete the folders created in order")
def step_impl():
    Applicationexplorertabutility.delete_all_folder_system_ord_EC()   

    
@then("I Close the message window")
def step_impl():
    Applicationexplorertabutility.close_Message_Window()
    
    
@when("I Wait for Import Conflict Dialog Box Import Conflict Dialog in import dialog as {arg}")
def step_impl(importConflictDialog):
    """I Wait for Import Conflict Dialog Box Import Conflict Dialog in import dialog as '<Import Conflict Dialog>'"""
    CommonUtil.write_text_file("\nWhen I Wait for Import Conflict Dialog Box Import Conflict Dialog in import dialog as \""+importConflictDialog+"\"")
    obj.textboximportconflictdialogwaitforimportconflictdialogbox(importConflictDialog)


@when("I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as {arg}")
def step_impl(importConflictDialog7):
    """I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'"""
    CommonUtil.write_text_file("\nWhen I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as \""+importConflictDialog7+"\"")
    obj.textboximportconflictdialogclickonbuttonsinconflictdialogpopup(importConflictDialog7)
  
@then("Verify template added in Application browser AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser9):
    """Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'"""
    CommonUtil.write_text_file("\nThen Verify template added in Application browser AE Application browser in application explorer as \""+applicationBrowser9+"\"")
    obj.textboxapplicationbrowserverifytemplateaddedinapplicationbrowserae(applicationBrowser9)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@then("Verify instance lock popup Application browser in application explorer as {arg}")
def step_impl(applicationBrowser5):
    """Verify instance lock popup Application browser in application explorer as '<Application browser5>'"""
    CommonUtil.write_text_file("\nThen Verify instance lock popup Application browser in application explorer as \""+applicationBrowser5+"\"")
    obj.textboxapplicationbrowserverifyinstancelockpopup(applicationBrowser5)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Click on Buttons in Import Dialog popup AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser6):
    """I Click on Buttons in Import Dialog popup AE Application browser in application explorer as '<Application browser6>'"""
    CommonUtil.write_text_file("\nWhen I Click on Buttons in Import Dialog popup AE Application browser in application explorer as \""+applicationBrowser6+"\"")
    obj.buttonimportdialogclickonbuttonsinimportdialogpopupae(applicationBrowser6)
    
    
@when("I selected Relative Radio in import dialog")
def step_impl():
    """I selected Relative Radio in import dialog"""
    CommonUtil.write_text_file("\nWhen I selected Relative Radio in import dialog")
    obj.buttonrelativeradioselected()
    
@when("I Click on buttons in popup window Application browser in application explorer as {arg}")
def step_impl(applicationBrowser6):
    """I Click on buttons in popup window Application browser in application explorer as '<Application browser6>'"""
    CommonUtil.write_text_file("\nWhen I Click on buttons in popup window Application browser in application explorer as \""+applicationBrowser6+"\"")
    obj.textboxapplicationbrowserclickonbuttonsinpopupwindow(applicationBrowser6)

  
@when("I close all tabs except system explorer in Engineering Client")
def step_impl():
    """I close all tabs except system explorer EC Templates browser in application explorer as '<Templates browser23>'"""
    obj.textboxtemplatesbrowserclosealltabsexceptsystemexplorerec()

    
@when("I Copy and paste using shortcut keys Specific template in application browser")
def step_impl():
    """I Copy and paste using shortcut keys Specific template in application browser"""
    CommonUtil.write_text_file("\nWhen I Copy and paste using shortcut keys Specific template in application browser")
    obj.buttonspecifictemplatecopyandpasteusingshortcutkeys()    
    
    
@then("Verify delete window AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate3):
    """Verify delete window AE MotorGP template in application explorer as '<MotorGP template3>'"""
    CommonUtil.write_text_file("\nThen Verify delete window AE MotorGP template in application explorer as \""+motorgpTemplate3+"\"")
    obj.textboxmotorgptemplateverifydeletewindowae(motorgpTemplate3)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I take evidence Identifier MotorGP_1 in application browser")
def step_impl():
    """I take evidence Identifier MotorGP_1 in application browser"""
    CommonUtil.write_text_file("\nWhen I take evidence Identifier MotorGP_1 in application browser")
    obj.textboxinstanceeditortakeevidence()
    
    
@when("I Click template AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate1):
    """I Click template AE MotorGP template in application explorer as '<MotorGP template1>'"""
    CommonUtil.write_text_file("\nWhen I Click template AE MotorGP template in application explorer as \""+motorgpTemplate1+"\"")
    obj.textboxmotorgptemplateclicktemplateae(motorgpTemplate1)
    
    
@when("I Press short keys MotorGP template in application explorer")
def step_impl():
    """I Press short keys MotorGP template in application explorer"""
    CommonUtil.write_text_file("\nWhen I Press short keys MotorGP template in application explorer")
    obj.textboxmotorgptemplatepressshortkeys()
    
    
@when("I double click on template Identifier MotorGP_1 in application browser as {arg}")
def step_impl(identifierMotorgp11):
    """I double click on template Identifier MotorGP_1 in application browser as '<Identifier MotorGP_11>'"""
    CommonUtil.write_text_file("\nWhen I double click on template Identifier MotorGP_1 in application browser as \""+identifierMotorgp11+"\"")
    obj.textboxidentifierdoubleclickontemplate(identifierMotorgp11)
    

@when("I Click on buttons in popup window Warning popup window in application explorer as {arg}")
def step_impl(warningPopupWindow7):
    """I Click on buttons in popup window Warning popup window in application explorer as '<Warning popup window7>'"""
    CommonUtil.write_text_file("\nWhen I Click on buttons in popup window Warning popup window in application explorer as \""+warningPopupWindow7+"\"")
    obj.textboxwarningpopupwindowclickonbuttonsinpopupwindow(warningPopupWindow7)
    
    
@when("I Warning popup close Warning popup window in application explorer")
def step_impl():
    """I Warning popup close Warning popup window in application explorer"""
    CommonUtil.write_text_file("\nWhen I Warning popup close Warning popup window in application explorer")
    obj.textboxwarningpopupwindowwarningpopupclose()
    
    
@then("Verify Message from notification panel AE Delete popup in message box as {arg}")
def step_impl(deleteInstance):
    """Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'"""
    CommonUtil.write_text_file("\nThen Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'")
    obj.buttondeletepopupverifymessagefromnotificationpanelae(deleteInstance)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I Copy and paste using shortcut keys value template in application browser")
def step_impl():
    """I Copy and paste using shortcut keys Specific template in application browser"""
    CommonUtil.write_text_file("\nWhen I Copy and paste using shortcut keys Specific template in application browser")
    obj.buttonspecifictemplatecopyandpasteusingshortcutkeys_1()
    
@then("I verify the file existance")##
def step_impl():
    Applicationexplorertabutility.Verify_file_existance()
    

@then("Verify the template is present in Application browser as {arg}")
def step_impl(Templatesbrowser1):
    """Verify the template is present in Application browser"""
    CommonUtil.write_text_file("\nThen Verify the template is present in Application browser")
    Applicationexplorertabutility.verify_instance_application_browser(Templatesbrowser1)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Expand System and Folder in Application browser")
def step_impl():
    """When I Expand System and Folder in Application browser"""
    CommonUtil.write_text_file("\nWhen I Expand System and Folder in Application browser")
    obj.expandfoldersystem()
    
@then("I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message")
def step_impl():
    """I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message"""
    CommonUtil.write_text_file("\nthen I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message")
    obj.verifySameNameErrorboxapplicationbrowser()
    
@when("I Click on buttons as {arg}")
def step_impl(button_1):
    obj.renameinstancepopupbutton(button_1)
    
@when("I Close Lockup pop up window")
def step_impl():
    """I Close Lockup pop up window"""
    CommonUtil.write_text_file("\nwhen I Close Lockup pop up window")
    obj.modaldialogwindowclose()
    
@then("Verify application browser folder AE")
def step_impl(applicationBrowser3):
    """Verify application browser folder AE"""
    Applicationexplorertabutility.verify_instance_application_browser()  
    
@then("verify window open as {arg}")
def step_impl(Window):
    """I Rename the Insatnce to the requirement '<Name1>'"""
    CommonUtil.write_text_file("\nI Rename the Insatnce to the requirement \""+Window+"\"")
    Applicationutility.wait_in_seconds(2000, 'Wait')
    obj.verifyobject(Window)

@when("I select the template to replace in replace template as {arg}")
def step_impl(Replace_Template):    
    obj.replacetemplatecomb(Replace_Template)
    
@then("I wait for Import Dialogue Window to appear")
def step_impl():    
    obj.replacetemplatecomb(ReplaceTemplate)


@when("I Select button in the modal dialoge window as {arg}")
def step_impl(Buttonname):    
    """I Select button in the modal dialoge window as '<Buttonname>'"""
    obj.modaldiawindow(Buttonname)
    Applicationutility.wait_in_seconds(5000, 'Wait')

@when("I Close modal dialog window")
def step_impl():
    """I Close Lockup pop up window"""
    CommonUtil.write_text_file("\nwhen I Close Lockup pop up window")
    obj.modaldialogwindowclose()
    
@then("verify template and version in application browser as {arg}")
def step_impl(Template):
    """verify template and version in application browser"""
    Applicationutility.wait_in_seconds(3000, 'Wait')
    obj.verifytemplatebrowserinae(Template)
    Applicationutility.take_screenshot('Full screenshot !!')

    
@when("I Select context menu item as {arg}")
def step_impl(action):
    obj.textboxassetworkspaceselectcontextmenuitemec(action)
  
@when("I click modal dialog window Instance editor save in application explorer as {arg}")
def step_impl(yes):
    """I click modal dialog window Instance editor save in application explorer as 'Yes'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window Instance editor save in application explorer as 'Yes'")
    obj.buttoninstanceeditorsaveclickmodaldialogwindow(yes)
    
@when("I drag template in application browser Link Editor as {arg}")
def step_impl(assertWorkspaceEditor8):
    """I drag template in application browser Link Editor as '<Assert Workspace Editor8>'"""
    CommonUtil.write_text_file("\nWhen I drag template in application browser Link Editor as \""+assertWorkspaceEditor8+"\"")
    obj.dragtemplatefromapplicationbrowsertolinkeditor(assertWorkspaceEditor8)

@when("I Remove PVRanged link AE Assert Workspace Editor in application explorer")
def step_impl():
    """I Remove PVRanged link AE Assert Workspace Editor in application explorer"""
    CommonUtil.write_text_file("\nWhen I Remove PVRanged link AE Assert Workspace Editor in application explorer")
    obj.textboxassertworkspaceeditorremovepvrangedlinkae()
  
@then("Verify link two instances asset workspace Assert Workspace Editor in application explorer")
def step_impl():
    """Verify link two instances asset workspace Assert Workspace Editor in application explorer"""
    CommonUtil.write_text_file("\nThen Verify link two instances asset workspace Assert Workspace Editor in application explorer")
    obj.textboxassertworkspaceeditorverifylinktwoinstancesassetworkspace()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Enter FileLocation and FileName in empty pages import dialog as {arg}")
def step_impl(importfile):
    """I Enter FileLocation and FileName in empty pages import dialog as '<Import3>'"""
    CommonUtil.write_text_file("\nI Enter FileLocation and FileName in empty pages import dialog as \""+importfile+"\"")
    obj.textboximportemptypagesenterfilelocationandfilenametobeimported(importfile)

@when("I drag Template from Template browser and drop to the Folders in Application browser with folder name as {arg}")
def step_impl(templatesBrowser2):
    """I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<Templates browser2>'"""
    CommonUtil.write_text_file("\nWhen I drag Template from Template browser and drop to the Folders in Application browser with folder name as \""+templatesBrowser2+"\"")
    Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE(templatesBrowser2)