Feature: Description of the new feature3

@TC_EPE_TE_CS_0018
@test006
Scenario Outline: Add drops to EIO Bus
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I Rclick Drops EIO add new device CE FBD SectionWindow in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<Dialog List box CE4>'
And I selected Dialog OK CE in dialog ce

Examples:
  | SlNo. | Project Browser RO1        | Dialog Panel CE2 | Dialog Panel CE3 | Dialog List box CE4 | content |
  | 1     | Configuration$$2 : EIO Bus | .X80 remote drop | BMX XBP 1200     | BME CRA 313 10      | NA      |


@TC_EPE_TE_CS_0019
@test007
Scenario Outline: Add Communication Modules to EIO bus
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce

Examples:
  | SlNo. | Project Browser RO1                                                   | Project Browser RO2                             | Dialog Panel CE3 | Dialog Panel CE4 | content |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BMX XBP 1200$$1 | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Communication    | BMX NOM 0200.4   | NA      |


@TC_EPE_TE_CS_0017
@test003
Scenario Outline: Add Communication Modules to PLC Bus
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce
And I selected Properties of device OK CE in control expert

Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$4 | Communication    | BME NOC 0301.4   |
  
  
@TC_EPE_TE_CS_0017
@test003
Scenario Outline: Add Communication Modules to PLC Bus in 6th Slot
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce
And I selected Properties of device OK CE in control expert

Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$6 | Communication    | BME NOC 0301.4   |
  
@TC_EPE_TE_CS_0014A
Scenario Outline: Open configure window, add Communication modules modules
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce 
And I selected Dialog OK CE in dialog ce 
And I selected List of modified Yes button CE in dialog ce
And I selected Dialog OK CE in dialog ce 
And I selected Dialog OK CE in dialog ce 
And I selected Dialog OK CE in dialog ce 
@Add_Communication_Module__BME_NOC_0301_Slot2_HART
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Communication    | BME NOC 0301.2   |

  

