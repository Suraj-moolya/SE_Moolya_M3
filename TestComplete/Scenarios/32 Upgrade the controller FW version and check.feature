Feature: 32 Upgrade the controller FW version and check

@TC_EPE_TE_0025
Scenario Outline: Upgrade the controller FW version
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I selected select PLC bus combobox item CE in refine offline as '<Cpu_version>'


Examples:
  | SlNo. | Project Browser RO1        | Cpu_version          |
  | 1     | Configuration$$0 : PLC bus | BME P58 6040   04.40 |