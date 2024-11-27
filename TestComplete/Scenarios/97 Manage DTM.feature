Feature: 97 Manage DTM

@TC_EPE_DTM_0001
Scenario Outline: Manage DTM
When I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window

Examples:
  | SlNo. | prm             | option |
  | 1     | BMEP58_ECPU_EXT | Add... |