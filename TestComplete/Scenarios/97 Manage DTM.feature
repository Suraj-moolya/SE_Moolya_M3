Feature: 97 Manage DTM

@TC_EPE_DTM_0001
Scenario Outline: Manage DTM
When I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window
And I select '<protocol>' and '<device>' in DTM Browser Add device window
And I Double Click on '<property>' in channel Window
And I select '<button>' in DTM Browser property device window
And I double click on the installed '<prm1>' on DTM Browser
And I selected '<property1>' from the dropdown in the Reference Filtering tab
And I selected '<slot>' and '<module>' in the Options Modules tab
And I clicked '<button>' in the DTM channel window
Then I verify the Device Name and Reference in the DTM Channel window

Examples:
  | SlNo. | prm             | option | protocol    | device | property    | button | prm1   | property1   | slot         | module                  |
  | 1     | BMEP58_ECPU_EXT | Add... | EtherNet IP | ATV6xx | EtherNet IP | OK     | ATV6xx | ATV630U07M3 | OptionBoard1 | EtherNet/IP - ModbusTCP |