Feature: AS3 Map the port to the new tag container and map the device in the communication mapping

  
@TC_EPE_PE_AS3a
@test003
Scenario Outline: Map the port to the new tag container
#When I Edit IO Device Properties project browser in project explorer as '<project browser8>'
When I Close tab items EC main screen in engineering client as 'IODevices'

Examples:
  | SlNo. | project browser8 |
  | 1     | Ports$$Prot_1    |

  
@TC_EPE_PE_AS3b
@test003
Scenario Outline:Navigate to communication mapping Tab
When I Click '<tabname>' on service mapping edittor window

Examples:
  | SlNo. | tabname               |
  | 1     | Communication Mapping |

  
@TC_EPE_PE_AS3
@test003
Scenario Outline: Map the device in the communication mapping
When I Map IO Devices in PE project browser in project explorer as '<project browser1>'

Examples:
  | SlNo. | project browser1             |
  | 1     | IODevice_1$$2$$Workstation_1 |
  | 2     | IODevice_2$$2$$Workstation_1 |
  | 3     | IODevice_1$$3$$NIC_1         |
  | 4     | IODevice_2$$3$$NIC_1         |
  
  
@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign Instance to Containers in Supervision Prject
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | controller  | section          |
  | 1     | Sample_Test | Supervision_Test |
   


  



  