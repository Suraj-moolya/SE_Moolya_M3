Feature: 138 Check Control and supervision participants are opening in GT

@TC_EPE_GT_0001
Scenario Outline: Check Control Participants are opening in GT
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<global template core>'



Examples:
  | SlNo. | Templates browser         | global template core |
  | 1     | Motorgp$$MotorGP$$1.0.123 | Edit                 |