Feature: 152 Open any section and check network variable window

@TC_EPE_PE_CP_0033
@test001
Scenario Outline: Open Refine of one Control Project and add Elementary Variables with Custom name P2P - Add Constant and Custom columns
When I RClick on filter Refine Offline MDI Window in refine offline
And I selected Customize Columns in refine offline
And I Select Column Configuration Customize Columns in refine offline as 'Constant'
And I Select Column Configuration Customize Columns in refine offline as 'Custom'

Examples:
  | SlNo. | 
  | 1     | 

#Total No. of Test Cases : 1

@TC_EPE_PE_CP_0033a
@test002
Scenario Outline: Open Refine of one Control Project and add Elementary Variables with Custom name P2P 
When I Add variable name in name column MDI Window in refine offline as '<MDI Window1>'
And I click on ellipsis MDI Window in refine offline
And I selected Type column ellipsis in refine offline
And I select variable type Dialog popup CE Type column ellipsis in refine offline
And I select Constant check box Type column ellipsis in refine offline
And I Enter P2P in Custom box MDI Window in refine offline
And I Add variable name in name column MDI Window in refine offline as '<MDI Window2>'
And I select variable type MDI Window in refine offline as '<MDI Window>'
And I select Constant check box Type column ellipsis in refine offline
And I Enter P2P in Custom box MDI Window in refine offline


Examples:
  | SlNo. | MDI Window1 | MDI Window2 | MDI Window  | 
  | 1     | V1          | V2          | REF_TO BOOL |


#Total No. of Test Cases : 2

@TC_EPE_PE_CP_0034
@test003
Scenario Outline: Open Refine of the other Control Project and add Elementary Variables
When I Add variable name in name column MDI Window in refine offline as '<MDI Window1>'
And I click on ellipsis MDI Window in refine offline
And I selected Type column ellipsis in refine offline
And I select variable type Dialog popup CE Type column ellipsis in refine offline
And I select Constant check box Type column ellipsis in refine offline
And I Add variable name in name column MDI Window in refine offline as '<MDI Window2>'
And I select variable type MDI Window in refine offline as '<MDI Window>'
And I select Constant check box Type column ellipsis in refine offline


Examples:
  | SlNo. | MDI Window1 | MDI Window2 | MDI Window  | 
  | 1     | V1          | V2          | REF_TO BOOL | 


#Total No. of Test Cases : 3

@TC_EPE_PE_CP_0035
@test004
Scenario Outline: Map the Control Projects in Communication Mapping Editor
When I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as '<Communication Peer to Peer Pannel1>'
And I edit P2P Properties Communication Channels Pannel in communication mapping as '<Communication Channels Pannel2>'
And I edit P2P Properties Communication Channels Pannel in communication mapping as '<Communication Channels Pannel3>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'

Examples:
  | SlNo. | Communication Peer to Peer Pannel1 | Communication Channels Pannel2 | Communication Channels Pannel3 |
  | 1     | ControlExecutable                  | Read Description$$Test123      | Read size (0-125 words)$$100   | 


#Total No. of Test Cases : 4

@TC_EPE_PE_CP_0036
@test005
Scenario Outline: Click on Manage Network Variables button in Refine Offline
When I selected Manage Network Variables in refine offline


Examples:
  | SlNo. | 
  | 1     | 

#Total No. of Test Cases : 5

@TC_EPE_PE_CP_0036a
@test006
Scenario Outline: Open any section and check network variable window - Remove Variables
When I Right click on variable Manage Network Variables in message box as '<Manage Network Variables1>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'

Examples:
  | SlNo. | Manage Network Variables1 | 
  | 1     | V2                        |      

#Total No. of Test Cases : 6

@TC_EPE_PE_CP_0036b
@test007
Scenario Outline: Open any section and check network variable window - Verify Variable is Removed
Then Verify variable is removed Refine Offline MDI Window in refine offline as '<MDI Window1>'


Examples:
  | SlNo. | MDI Window1 | 
  | 1     | V2          | 

#Total No. of Test Cases : 7

