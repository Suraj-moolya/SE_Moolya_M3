Feature: AS22 Unlink between instances in Asset work space and save

@TC_EPE_AE_0058
@test001
@TC_EPE_AE_0058
Scenario Outline: Link/Unlink between instances in Asset Workspace
When I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'
Then Verify Link Status Node Instance in application explorer
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | ContextMenu5     | Asset workspace6 | Asset workspace7 | Assert Workspace Editor8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | AssetWorkspace element12 | Assert Workspace Editor13 |
  | 1     | Create Workspace | AssetWorkspace_1 | Edit Workspace   | AnalogOutputGP_1         | AnalogOutputGP_1         | AnalogInputGP_1           | AnalogInputGP_1           | Interlock                | AnalogInputGP_1           |


#Total No. of Test Cases : 1

@TC_EPE_AE_0059
@test002
@TC_EPE_AE_0059
Scenario Outline: Link/Unlink between instances in Asset Workspace (Linking from Enabling new Properties)
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu14>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor15>'
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist16>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist17>'
And I selected Instance editor save in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close18>'
And I double click on asset workspace elements AssetWorkspace element in application explorer as '<AssetWorkspace element19>'
And I double click on asset workspace elements AssetWorkspace element in application explorer as '<AssetWorkspace element20>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor21>'
When I Link from range node to range node AE Node Instance in application explorer as 'Running$$OpenPOS'
And I Link from range node to range node AE Node Instance in application explorer as 'Stopped$$ValveOP'
Then Verify Link Status Node Instance in application explorer
And Verify link two instances asset workspace Node Instance in application explorer as 'ValveOP'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Templates browser3 | Templates browser4 | Asset workspace5 | Asset workspace6 | Asset workspace7 | Asset workspace8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | Assert Workspace Editor12 | Identifier MotorGP_113 | ContextMenu14 | Instance Editor15 | Instance editor checklist16 | Instance editor checklist17 | Instance editor close18 | AssetWorkspace element19 | AssetWorkspace element20 | Assert Workspace Editor21 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | ValveGP            | ValveGP$$1.0.100   | System1          | Create Workspace | AssetWorkspace   | Edit Workspace   | MotorGP_1                | MotorGP_1                 | ValveGP_1                 | ValveGP_1                 | MotorGP_1$$1.0.123     | Properties    | MotorGP_1         | Running$$1                  | Stopped$$1                  | MotorGP_1               | Running                  | Stopped                  | MotorGP_1                 |


#Total No. of Test Cases : 2

@TC_EPE_AE_0060
@test003
@TC_EPE_AE_0060
Scenario Outline: Link/Unlink between instances in Asset Workspace (Linking from Enabling new Properties and not saving)
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu14>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor15>'
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist16>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist17>'
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close18>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox19>'
When I selected Save changes dialogbox no in application explorer
And I double click on template Identifier in application browser as '<Identifier20>'
And I take evidence Instance Editor in application explorer
And I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Templates browser3 | Templates browser4 | Asset workspace5 | ContextMenu6     | Asset workspace7 | Asset workspace8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | Assert Workspace Editor12 | Identifier MotorGP_113 | ContextMenu14 | Instance Editor15 | Instance editor checklist16 | Instance editor checklist17 | Instance editor close18 | Save changes dialogbox19   | Identifier20 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | ValveGP            | ValveGP$$1.0.100   | System1          | Create Workspace | AssetWorkspace   | Edit Workspace   | MotorGP_1                | MotorGP_1                 | ValveGP_1                 | ValveGP_1                 | MotorGP_1$$1.0.123     | Properties    | MotorGP_1         | Running$$1                  | Stopped$$1                  | MotorGP_1               | MotorGP_1: Save Changes(s) | MotorGP_1    |


#Total No. of Test Cases : 3

@TC_EPE_AE_0061
@test004
@TC_EPE_AE_0061
Scenario Outline: Link/Unlink between instances in Asset Workspace (Linking from Enabling new Properties_1)
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu14>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor15>'
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist16>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist17>'
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close18>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox19>'
When I selected Save changes dialogbox yes in application explorer
And I double click on asset workspace elements AssetWorkspace element in application explorer as '<AssetWorkspace element20>'
And I double click on asset workspace elements AssetWorkspace element in application explorer as '<AssetWorkspace element21>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor22>'
When I Link from range node to range node AE Node Instance in application explorer as 'Running$$OpenPOS'
And I Link from range node to range node AE Node Instance in application explorer as 'Stopped$$ValveOP'
Then Verify link two instances asset workspace Node Instance in application explorer as 'OpenPOS'
And Verify Link Status Node Instance in application explorer
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Templates browser3 | Templates browser4 | Asset workspace5 | ContextMenu6     | Asset workspace7 | Asset workspace8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | Assert Workspace Editor12 | Identifier MotorGP_113 | ContextMenu14 | Instance Editor15 | Instance editor checklist16 | Instance editor checklist17 | Instance editor close18 | Save changes dialogbox19   | AssetWorkspace element20 | AssetWorkspace element21 | Assert Workspace Editor22 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | ValveGP            | ValveGP$$1.0.100   | System1          | Create Workspace | AssetWorkspace   | Edit Workspace   | MotorGP_1                | MotorGP_1                 | ValveGP_1                 | ValveGP_1                 | MotorGP_1$$1.0.123     | Properties    | MotorGP_1         | Running$$1                  | Stopped$$1                  | MotorGP_1               | MotorGP_1: Save Changes(s) | Running                  | Stopped                  | MotorGP_1                 |


#Total No. of Test Cases : 4

@TC_EPE_AE_0062
@test005
@TC_EPE_AE_0062
Scenario Outline: Link/Unlink between instances in Asset Workspace (Linking from Enabling new Properties and not saving_1)
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu14>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor15>'
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist16>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist17>'
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close18>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox19>'
When I selected Save changes dialogbox cancel in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close20>'
And I selected Save changes dialogbox no in application explorer
And I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Templates browser3 | Templates browser4 | Asset workspace5 | ContextMenu6     | Asset workspace7 | Asset workspace8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | Assert Workspace Editor12 | Identifier MotorGP_113 | ContextMenu14 | Instance Editor15 | Instance editor checklist16 | Instance editor checklist17 | Instance editor close18 | Save changes dialogbox19   | Instance editor close20 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | ValveGP            | ValveGP$$1.0.100   | System1          | Create Workspace | AssetWorkspace   | Edit Workspace   | MotorGP_1                | MotorGP_1                 | ValveGP_1                 | ValveGP_1                 | MotorGP_1$$1.0.123     | Properties    | MotorGP_1         | Running$$1                  | Stopped$$1                  | MotorGP_1               | MotorGP_1: Save Changes(s) | MotorGP_1               |


#Total No. of Test Cases : 5

@TC_EPE_AE_0063
@test006
@TC_EPE_AE_0063
Scenario Outline: Link/Unlink between instances in Asset Workspace (Enabling properties directly from Drag and Dropped Instance)
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu13>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor14>'
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist15>'
And I selected Instance editor save in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close16>'
And I double click on asset workspace elements AssetWorkspace element in application explorer as '<AssetWorkspace element17>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor18>'
When I Link from range node to range node AE Node Instance in application explorer as 'ExternallyControlled$$MotorLOP'
Then Verify link two instances asset workspace Node Instance in application explorer as 'MotorLOP'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Templates browser3 | Templates browser4 | Asset workspace5 | Asset workspace6 | Asset workspace7 | Asset workspace8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 | Assert Workspace Editor12 | ContextMenu13 | Instance Editor14 | Instance editor checklist15 | Instance editor close16 | AssetWorkspace element17 | Assert Workspace Editor18 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | ValveGP            | ValveGP$$1.0.100   | System1          | Create Workspace | AssetWorkspace   | Edit Workspace   | MotorGP_1                | MotorGP_1                 | ValveGP_1                 | ValveGP_1                 | Properties    | ValveGP_1         | ExternalControl$$1          | ValveGP_1               | ExternalControl          | ValveGP_1                 |


#Total No. of Test Cases : 6

