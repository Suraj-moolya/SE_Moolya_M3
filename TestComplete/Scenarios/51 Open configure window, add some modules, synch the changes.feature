Feature: Description of the new feature1

@TC_EPE_TE_CS_0015
Scenario Outline: Unlock Safety Protection for adding Safety modules
When I selected Unlock Safety Protection CE in control expert
And I Add new text modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window2>'

Examples:
  | SlNo. | Modal dialog window1 | Modal dialog window2 | content |
  | 1     | password             | OK                   | NA      |


@TC_EPE_TE_CS_0014A
Scenario Outline: Open configure window, add Analog modules
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'
And I selected Dialog OK CE in dialog ce
 
@Add_Analog_Module__BMX_AMO_0410_slot6
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$6 | Analog           | BMX AMO 0410     |
@Add_Analog_Module__BMX_AMI_0810_Slot4
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$4 | Analog           | BMX AMI 0810     |
@Add_Analog_Module__BMX_AMI_0812_Slot4_HART
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$4 | Analog           | BME AHI 0812     | 
@Add_Analog_Module__BME_AHO_0412_Slot5_HART
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$5 | Analog           | BME AHO 0412     |
  
@Add_Communication_Module__BME_AHO_0412_Slot5_HART
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$5 | Analog           | BME AHO 0412     |
  
@TC_EPE_TE_CS_0014B
Scenario Outline: Open configure window, add Discrete modules
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'
And I selected Dialog OK CE in dialog ce
 
@Add_Discrete_Module__BMX_DDI_1602_slot2
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Discrete         | BMX DDI 1602     |
  
@Add_Discrete_Module__BMX_DDO_1602_slot3
Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$3 | Discrete         | BMX DDO 1602     |
 
  
