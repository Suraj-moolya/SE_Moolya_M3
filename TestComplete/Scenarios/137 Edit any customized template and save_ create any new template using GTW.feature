Feature: 137 Edit any customized template and save_ create any new template using GTW

@TC_EPE_GT_0005
Scenario Outline: Edit any customized template and save
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I Select '<tab>' in global template explorer
And I Drag and Drop '<source>' from toolbox to the edit page in global template explorer
And I selected save as composite editor in composite editor
And I click on '<btn>' in the Save As window
And I change the template name to '<name>' and version to '<version>' in the Save As window
And I enter the description in the Save As window as '<desc>'
And I Click on old State Selector in global template explorer
And I Click on Approved combo item in global template explorer
And I Click on State Selector in global template explorer
And I Click on Approved combo item in global template explorer
And I selected Save in save as windowo
And I Close tab items EC main screen in engineering client as 'Sample'
And I Close tab items EC main screen in engineering client as 'Global'

@Edit_MotorGP_template_and_save_as_Sample_Test
Examples:
  | SlNo. | Templates browser1        | global template core5 | tab     | source | btn   | name        | version | desc               |
  | 1     | Motorgp$$MotorGP$$1.0.123 | Edit                  | Toolbox | Add    | Other | Sample_Test | 1.0.126 | Sample Description |

@Edit_MotorGP_template_1.0.127_and_save_as_Sample_Test
Examples:
  | SlNo. | Templates browser1        | global template core5 | tab     | source | btn   | name        | version | desc               |
  | 1     | Motorgp$$MotorGP$$1.0.127 | Edit                  | Toolbox | Add    | Other | Sample_Test | 1.0.126 | Sample Description |
  
@TC_EPE_GT_0005A
Scenario Outline: Edit Sample Test customized template and save
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I Select '<tab>' in global template explorer
And I Drag and Drop '<source>' from toolbox to the edit page in global template explorer
And I selected save as composite editor in composite editor
And I click on '<btn>' in the Save As window
And I Click on State Selector in global template explorer
And I Click on Approved combo item in global template explorer
And I change the template name to '<name>' and version to '<version>' in the Save As window
And I enter the description in the Save As window as '<desc>'
And I selected Save in save as windowo
When I Close tab items EC main screen in engineering client as 'Sample'
And I Close tab items EC main screen in engineering client as 'Global'

@Edit_Sample_Test_template_and_save_as_Sample_Test_to_update
Examples:
  | SlNo. | Templates browser1                | global template core5 | tab     | source | btn       | name        | version | desc                       |
  | 1     | Sample_Test$$Sample_Test$$1.0.126 | Edit                  | Toolbox | And    | New Build | Sample_Test | 1.0.130 | Updated Sample Description |
      
  
@TC_EPE_GT_0005
Scenario Outline: Create any new template using GTW
When I Right Click on nodes System Explorer Node in system explorer as 'Global Templates'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I click on the '<button>' button in the Template Creation Wizard
And I click on the Browse button in the Template Creation Wizard
And I Enter FileLocation and FileName to be Imported Import in import dialog as 'Test_M580'
And I click on the '<button>' button in the Template Creation Wizard
And I click on the '<button>' button in the Template Creation Wizard
And I click on the '<elem>' Add button in the Template Creation Wizard
And I select '<tag>' in Select Tag Window
And I Select button in the modal dialoge window as '<Button name>'
And I click on the '<elem1>' Add button in the Template Creation Wizard
And I select '<tag1>' in Select Tag Window
And I Select button in the modal dialoge window as '<Button name>'
And I click on the '<button>' button in the Template Creation Wizard
And I click on the '<button>' button in the Template Creation Wizard
And I Exapnd the '<lib>' in Template Creation Wizard
And I click on the '<lib1>' in Template Creation Wizard
And I Drag and Drop '<prop>' from Genie to Genie Facet in Template Creation Wizard
And I click on the '<button>' button in the Template Creation Wizard
And I click on the '<button>' button in the Template Creation Wizard
And I click on the '<button1>' button in the Template Creation Wizard
And I Select button in the modal dialoge window as '<button name1>'
And I right click on the created template in global template explorer as '<temp>'
And I Select context menu item EC global template core in global template explorer as '<menu>'
And I Close tab items EC main screen in engineering client as '<temp>'

Examples:
  | SlNo. | global template core5    | Import4 | tag          | Button name | elem1         | elem          | tag1           | lib                   | prop      | lib1      | button | button1         | button name1 | temp       | menu |
  | 1     | Template Creation Wizard | Open    | Variable Tag | OK          | VariableTag_1 | Template_1_CD | Advanced Alarm | GeneralPurposeLibrary | shelved_m | gpl_alarm | Next   | Create Template | Yes          | Template_1 | Edit |