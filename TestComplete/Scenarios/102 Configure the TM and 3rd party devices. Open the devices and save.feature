Feature: 102 Configure the TM and 3rd party devices. Open the devices and save

@TC_EPE_DTM_0001
Scenario Outline: Configure a Third Party DTM Device, open and save
When I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window
And I select '<protocol>' and '<device>' in DTM Browser Add device window
And I select '<button>' in DTM Browser property device window
And I double click on the installed '<prm1>' on DTM Browser
And I import the required module '<module>' to configured modules
And I click '<button1>' and close the DTM Window

Examples:
  | SlNo. | prm             | option | protocol    | device                           | button | prm1                           | module                   | button1 |
  | 1     | BMEP58_ECPU_EXT | Add... | EtherNet IP | EtherNet/IP Messaging (from EDS) | OK     | EtherNet_IP_Messaging_from_EDS | 1756-Lx/Em Revision 10.1 | Apply   |
  

@TC_EPE_DTM_0002
Scenario Outline: Set IP to the DTMs
When I double click on the installed '<prm>' on DTM Browser
And I click on required '<channel>' on DTM Browser
And I select '<tab>' in FDT Configuration Window
And I update the '<ip_address>' in FDT Configuration Window

Examples:
  | SlNo. | prm             | channel                        | tab             | ip_address     |
  | 1     | BMEP58_ECPU_EXT | EtherNet_IP_Messaging_from_EDS | Address Setting | 182.179.244.99 |