Feature: 56 Configure HART modules and map the communication(Distributed IO's)

@TC_EPE_TE_0002
@test002
Scenario Outline: Configure HART modules and map the communication(Distributed IO's)
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I select '<button>' in PLC window
And I select "<rack number_0>" rack in PLC bus Window
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<device>'
And I select '<button1>' in New Device PopUp Window
And I select "<rack number_1>" rack in PLC bus Window
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<device1>'
And I select '<button1>' in New Device PopUp Window

And I select "<rack number>" rack in PLC bus Window
And I selected the checkbox for channel '<num>' in the HART configuration
And I click Validate button on control configuration window
And I selected Save PRM Configuration in Configuration Window
#And I Select button in the modal dialoge window as '<button1>'
#And I selected '<button2>' Button in BME window
And I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window  
And I select '<protocol>' and '<device>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window 
And I select '<protocol>' and '<device1>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I click '<menu1>' in Tool Bar
And I click '<menu_item1>' in Tool Bar popup window
#And I select '<button3>' in New Device PopUp Window
And I wait for the Build Project window to disappear
And I selected Save PRM Configuration in Configuration Window
And I selected Close Configuration window in Topology Explorer

Examples:
  | SlNo. | node_name    | action    | Project Browser RO1        | Dialog Panel CE3 | button   | button1 | button2 | menu  | prm             | option | protocol    | device       | device1      | menu_item   | menu_item1          | menu1 | num | button3 | rack number | rack number_1 | rack number_0 |
  | 1     | Controller_2 | Configure | Configuration$$0 : PLC bus | Analog           | Maximize | OK      | Close   | Tools | BMEP58_ECPU_EXT | Add... | EtherNet IP | BME AHI 0812 | BME AHO 0412 | DTM Browser | Rebuild All Project | Build | 0   | Yes     | 2           | 3             | 2             |
  
  
@TC_EPE_TE_0002
@test002
Scenario Outline: Configure HART modules
When I select "<rack number>" rack in PLC bus Window
And I selected the checkbox for channel '<num>' in the HART configuration
And I click Validate button on control configuration window
And I selected Save PRM Configuration in Configuration Window
And I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window  
And I select '<protocol>' and '<device>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window 
And I select '<protocol>' and '<device1>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I click '<menu1>' in Tool Bar
And I click '<menu_item1>' in Tool Bar popup window
And I wait for the Build Project window to disappear

@BME_AHI_0812_slot_4__BME_AHO_0412_slot_5__Configure_Hart_modules
Examples:
  | SlNo. | button1 | menu  | prm             | option | protocol    | menu_item   | menu_item1          | menu1 | num | rack number | device       | device1      |
  | 1     | OK      | Tools | BMEP58_ECPU_EXT | Add... | EtherNet IP | DTM Browser | Rebuild All Project | Build | 0   | 4           | BME AHI 0812 | BME AHO 0412 |