"""
 * ----------------------------------------------------------------------
 * Copyright (c) 2024, System Level Solutions (India) Pvt. Ltd.
 * ----------------------------------------------------------------------
 *      Purpose   : Verify Auth Logs module
 *      Package   : WISUN TestCases
 *      File name : TC006_Auth_Logs_Go_To_Next_page.py
 *      Project   : Wi-SUN Project
 * ----------------------------------------------------------------------
"""

import os
import sys

# To get parent path of current file
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# To get grand parent path of current file
grand_parent_path = os.path.dirname(parent_path)
# To get grand parent path
great_grand_parent_path = os.path.dirname(grand_parent_path)
# To access Events_Main folder
sys.path.append(grand_parent_path)
# To access Node Test Scripts folder
sys.path.append(great_grand_parent_path)

from Auth_Logs_Main.auth_logs_main import (
    click_on_auth_logs,
    verify_in_both_pages
)

from Events_Test_Scripts.TestCases.Events.TC008_Events_Go_To_Next_page import Initialization

"""
The purpose of this file is to verify go to next page functionality in Auth Logs Tab.
"""

if __name__ == "__main__":
    if Initialization() == "FAIL":
        print("NMS portal open successfully : ", "FAIL")
        sys.exit(1)
    if click_on_auth_logs() == "FAIL":
        print("click_on_auth_logs : ", "FAIL")
        sys.exit(1)
    if verify_in_both_pages("click_on_go_to_next_page") == "FAIL":
        print("verify_in_both_pages : ", "FAIL")
        sys.exit(1)
    else:
        print("\n==================PASS==================\n")
