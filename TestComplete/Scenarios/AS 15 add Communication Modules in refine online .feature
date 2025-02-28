Feature: AS 15 add Communication Modules in refine online 

@TC_EPE_AS_0010
@test003
Scenario Outline: Add Communication Modules to PLC Bus in 6th Slot in refine online for the first time
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I select '<button>' in New Device PopUp Window
And I selected Dialog OK CE in dialog ce
And I select '<button1>' in New Device PopUp Window
And I select '<button>' in New Device PopUp Window
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 | button | button1 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$6 | Communication    | BME NOC 0301.4   | OK     | Yes     |
  
  
  

