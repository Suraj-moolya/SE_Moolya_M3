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

Examples:
  | SlNo. | Project Browser RO1                             | Project Browser RO2                             | Dialog Panel CE3 | Dialog Panel CE4 | Dialog List box CE5 | content |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Analog           | BMX AMO 0802     | DDT                 | NA      |



@TC_EPE_TE_CS_0014B
Scenario Outline: Open configure window, add Discrete modules
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'
And I selected Dialog OK CE in dialog ce

Examples:
  | SlNo. | Project Browser RO1                             | Project Browser RO2                             | Dialog Panel CE3 | Dialog Panel CE4 | Dialog List box CE5 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$3 | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Discrete         | BMX DAI 0805     | DDT                 |


@TC_EPE_TE_CS_0014B
Scenario Outline: Open configure window, add Communication modules
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce
And I selected Dialog OK CE in dialog ce

Examples:
  | SlNo. | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$4 | Communication    | BME NOC 0301.2   |