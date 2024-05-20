# * ----------------------------------------------------------------------
# * Copyright (c) 2024, System Level Solutions (India) Pvt. Ltd.
# * ----------------------------------------------------------------------
# *      Purpose   : Verify Events module
# *      Package   : WISUN TestCases
# *      File name : TC001_Auth_Logs_Module_Expected_Elements.robot
# *      Project   : Wi-SUN Project
# * ----------------------------------------------------------------------

| *** Settings *** |

| Documentation  | Testlogs_Auth_Logs_Elements. |
| Library        | TC001_Auth_Logs_Module_Expected_Elements.py |

| *** Variables *** |
| ${FUNCTION_NAME}       | check_auth_logs_expected_elements  |

| *** Test Cases *** |
| Testlogs_Auth_Logs_Elements |
|    | [Tags] | Testlogs_Auth_Logs_Elements |
|    | ${output} =     | TC001_Initialization |
|    | Run Keyword If  | '${output}' != 'PASS'  | FAIL |
|    | ${output} =     | TC001_Click_On_Auth_Logs |
|    | Run Keyword If  | '${output}' != 'PASS'  | FAIL |
|    | ${output} =     | TC001_Verify_Expected_Elements |
|    | Run Keyword If  | '${output}' != 'PASS'  | FAIL |


| *** Keywords *** |

| TC001_Initialization |
|    | ${status} = | TC001_Auth_Logs_Module_Expected_Elements.Initialization |
|    | [Return]    |  ${status} |

| TC001_Click_On_Auth_Logs |
|    | ${status} = | TC001_Auth_Logs_Module_Expected_Elements.click_on_auth_logs |
|    | [Return]    |  ${status} |

| TC001_Verify_Expected_Elements |
|    | ${status} = | TC001_Auth_Logs_Module_Expected_Elements.verify_in_both_pages | ${FUNCTION_NAME} |
|    | [Return]    |  ${status} |
