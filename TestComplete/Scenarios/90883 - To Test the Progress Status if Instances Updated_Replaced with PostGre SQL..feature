Feature: 90883 - Verify Instance Progress Status when Templates are Updated or Replaced using PostgreSQL

@TC_EPE_AE_PGSQL_90883

@90883_1
Scenario Outline: Creating multiple instances by dragging and dropping template to folder and verifying progress status
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I selected Create Folder in context menu
  And I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
  And I drag Template from Template browser and drop to Application browser '<Count>' times with template as '<TemplateBrowser2>'
  Then Verify the progress status of instance in Application browser when opened as '<template>'

  @DragDrop_Instance_MotorGP_To_Folder_5_Times_90883
  Examples:
    | SlNo | ApplicationBrowserRoot | TemplatesBrowser1 | TemplateBrowser2           | Count | template         |
    | 1    | System                 | MotorGP           | MotorGP$$1.0.123$$Folder_1 | 5     | MotorGP_1$$0     |

@90883_2
Scenario Outline: Create New Template in Global Template
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar2>'
  And I Search text and select GTE global template search in global template explorer as '<TemplatesBrowser>'
  And I right click on the instance '<Identifier>' in device control window
  And I Select context menu item EC global template core in global template explorer as '<GlobalTemplateCore>'
  And I click the '<PrimaryButton>' button in the Composite Editor Workspace
  And I right click on the '<Instance1>' header with UC display type in composite editor workspace
  And I Select context menu item EC global template core in global template explorer as '<GlobalTemplateCore>'
  And I click the '<PrimaryButton>' button in the Composite Editor Workspace
  And I right click on the '<Instance2>' header with UC display type in composite editor workspace
  And I Select context menu item EC global template core in global template explorer as '<GlobalTemplateCore>'
  And I right click on the '<Instance3>' header with UC display type in composite editor workspace
  And I Select context menu item EC global template core in global template explorer as '<GlobalTemplateCore>'
  And I click the '<SecondaryButton>' button in the Composite Editor Workspace
  And I expand the instance '<ExpandInstance>' in the Global Template
  And I click the checkbox for instance '<CheckboxNames>' in the Global Template
  And I click the '<FinalButton>' button in the Composite Editor Workspace
  And I click the '<TertiaryButton>' button in the Composite Editor Workspace
  And I click the '<PrimaryButton>' button in the Composite Editor Workspace
  And I right click on the item '<instance_prop>' under the header '<header>'
  And I Select context menu item EC global template core in global template explorer as '<MenuItem>'
  And I right click on the item '<instance_prop1>' under the header '<header>'
  And I Select context menu item EC global template core in global template explorer as '<MenuItem>'
  And I right click on the item '<instance_prop2>' under the header '<header>'
  And I Select context menu item EC global template core in global template explorer as '<MenuItem>'
  And I right click on the item '<instance_prop3>' under the header '<header>'
  And I Select context menu item EC global template core in global template explorer as '<MenuItem>'
  And I click the '<Button>' button in the Composite Editor Workspace
  And I approve the new template by setting status to Approved and description to Test
  And I click on 'Save' button in Instance Save As window
  And I Close tab items EC main screen in engineering client as 'Test'
  And I Select button in the modal dialoge window as '<Button1>'
  And I Close tab items EC main screen in engineering client as '<Instance2>'
  And I click on Yes button in Message Box
  And I approve the new template by setting status to Approved and description to Test
  And I click on 'Save' button in Instance Save As window
  And I Select button in the modal dialoge window as '<Button1>'
  And I Close tab items EC main screen in engineering client as '<Instance1>'
  And I Select button in the modal dialoge window as '<Button1>'
  And I click on Yes button in Message Box
  And I approve the new template by setting status to Approved and description to Test
  And I click on 'Save' button in Instance Save As window
  And I Select button in the modal dialoge window as '<Button1>'
  And I Close tab items EC main screen in engineering client as 'MotorGP'
  And I Select button in the modal dialoge window as '<Button1>'
  And I click on Yes button in Message Box
  And I approve the new template by setting status to Approved and description to Test
  And I click on 'Save' button in Instance Save As window
  And I Close tab items EC main screen in engineering client as 'Global Templates'

  @Create_Global_Template
  Examples:
    | SlNo | MainToolBar2     | TemplatesBrowser          | Identifier        | GlobalTemplateCore | Instance1     | Instance2        | Instance3   | PrimaryButton   | SecondaryButton | ExpandInstance            | CheckboxNames                                                                   | FinalButton | TertiaryButton | instance_prop     | header      | MenuItem          | instance_prop1   | instance_prop2   | Button                                      | instance_prop3   | Button1 |
    | 1    | Global Templates | MotorGP$$MotorGP$$1.0.123 | $MotorGP$$1.0.123 | Edit               | MotorGP_UC    | MOTORCTRLGP_UC   | MOTORGP_UL  | Fit to content  | Templatizer     | MotorGP_ST$$STW$$CFGW     | $HMIVariable$$$STW.$InitValue$$$STW.$Comment$$$CFGW.$InitValue$$$CFGW.$Comment | Save        | Close          | $STW.$InitValue    | MotorGP_ST | Create Parameter  | $STW.$Comment     | $CFGW.$InitValue | Save the current template as a new template | $CFGW.$Comment  | Yes     |

@90883_3
@Creating_ControlProject_And_Assigning_All_Instances
@covered_in_90882
Scenario Outline: Creating Control Project and Assigning All Instances to Control Project
# Steps are reused from 90882.feature

@90883_4
@Creating_SupervisionProject_And_Assigning_All_Instances
@covered_in_90882
Scenario Outline: Creating Supervsion Project and Assigning All Instances to Control Project
# Steps are reused from 90882.feature

@90883_4
@Generate_Instances_In_Projects
Scenario Outline: Genarate Instances in Control & Supervision Project
  When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
  Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'

  @Generate_general_M580_Standalone
  Examples:
    | SlNo | container dock1           | container dock3 |
    | 1    | M580_Standalone$$Generate | Generate        |

  @Generate_general_Supervision_test
  Examples:
    | SlNo | container dock1            | container dock3 |
    | 1    | Supervision_Test$$Generate | Generate        |

@90883_5
@Verify_progress_status_after_Generate
@covered_in_90882
Scenario Outline: Verify Progress Status Of Instances After Generate
# Steps are reused from 90882.feature

@90883_6
Scenario Outline: Update template in AE and Verifying status progress
  When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
  And I Select context menu item EC Application browser in application explorer as '<Menu Item>'
  And I click modal dialog window Modal dialog window in message box as '<Button>'
  Then Verify Action message in notification pannel project browser in project explorer as '<Message>'
  Then Verify the progress status of instance in Application browser when opened as '<instance>'

  @Update_Template_And_Verify_Progress
  Examples:
    | SlNo | Application browser  | Menu Item       | Message                              | Button | instance        |
    | 1    | MotorGP_1$$1.0.123   | Update Template | Update Instance Template (Completed) | OK     | MotorGP_1$$100  |

@90883_7
@Replace_Template_And_Verify_Progress
Scenario Outline: Replace template - Select template to replace template from Application browser and Verifying status progress
  When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
  And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
  And I select the template to replace in replace template as '<Replace_Template>'
  And I Select button in the modal dialoge window as '<Button name>'
  Then verify template and version in application browser as '<Replace_Template>'
  Then Verify the progress status of instance in Application browser when opened as '<instance>'

  @Replace_Template_And_Verify_Progress
  Examples:
    | SlNo | Application browser | Application browser1 | Window           | Replace_Template    | Button name | instance      |
    | 1    | MotorGP_1$$1.0.123  | Replace Template     | Replace Template | AAlarmGP_UC$$1.0.11 | OK          | MotorGP_1$$25 |
