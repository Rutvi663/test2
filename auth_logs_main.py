"""
 * ----------------------------------------------------------------------
 * Copyright (c) 2024, System Level Solutions (India) Pvt. Ltd.
 * ----------------------------------------------------------------------
 *      Purpose   : Define All Common Functions for Auth Logs Tab
 *      Package   : WISUN Auth Logs Main File
 *      File name : auth_logs_main.py
 *      Project   : Wi-SUN Project
 * ----------------------------------------------------------------------
"""

import os
import sys
import time

from selenium.webdriver.common.by import By

"""
The purpose of this file is defining all the common functions to verify Auth logs tab which will be used
in Regression Testing.
"""

VALUE_FROM_DROPDOWN = 100

# To get parent directory path
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_path)
# To get great grand parent path
grand_parent_path = os.path.dirname(parent_path)
# To access Node Test Script folder
sys.path.append(grand_parent_path)
# To import all the functions
from Node_Test_Scripts.Main.main import exception_handling,close_driver

from Node_Test_Scripts.Main import main

def click_on_auth_logs():
    """
    This function is used to click on "Auth Logs" tab located on the left panel of NMS Home page.
    return:
        status:str
    """
    status = "FAIL"
    try:
        print("===================Go to Auth Logs.===================")
        time.sleep(main.FIVE_SEC_WAIT)
        main.DRIVER.find_element(
            By.XPATH, "//a[@routerlink='/auth-logs']"
        ).click()
        time.sleep(main.FIVE_SEC_WAIT)
        status = "PASS"
    except Exception as err:
        print("Error in 'click_on_auth_logs'.")
        exception_handling(err)
        close_driver()

    return status


def verify_in_both_pages(function_name):
    """
    This function is used to check all the functionality in Success and Failure Pages.
    param:
        function_name:str
    return:
        status:str
    """
    from TestCases.Auth_Logs.TC001_Auth_Logs_Module_Expected_Elements import check_auth_logs_expected_elements
    from TestCases.Auth_Logs.TC002_Auth_Logs_Module_Start_Date_End_Date import verify_datetime_in_logs
    from TestCases.Auth_Logs.TC003_Auth_Logs_Module_Invalid_Datetime import enter_invalid_start_end_datetime
    from TestCases.Auth_Logs.TC005_Auth_Logs_Module_UTC_Checkbox import verify_utc_time
    from Events_Test_Scripts.TestCases.Events.TC008_Events_Go_To_Next_page import click_on_go_to_next_page
    from Events_Test_Scripts.TestCases.Events.TC009_Events_Go_To_Last_page import click_on_go_to_last_page
    from Events_Test_Scripts.TestCases.Events.TC010_Events_Go_To_Previous_page import click_on_go_to_previous_page
    from Events_Test_Scripts.TestCases.Events.TC011_Events_Go_To_First_page import click_on_go_to_first_page
    from Events_Test_Scripts.TestCases.Events.TC012_Events_items_per_page import verify_dropdown
    status = "FAIL"
    func_dict = {"check_auth_logs_expected_elements": check_auth_logs_expected_elements,
                 "verify_datetime_in_logs" : verify_datetime_in_logs,
                 "enter_invalid_start_end_datetime" : enter_invalid_start_end_datetime,
                 "verify_utc_time" : verify_utc_time,
                 "click_on_go_to_next_page": click_on_go_to_next_page,
                 "click_on_go_to_last_page" :click_on_go_to_last_page, 
                 "click_on_go_to_previous_page": click_on_go_to_previous_page,
                 "click_on_go_to_first_page" : click_on_go_to_first_page, 
                 "verify_dropdown" : verify_dropdown}
    for page_id in ["success", "failure"]:
        if page_id == "failure":
            print("\n=================Checking in Failure Page.=====================")
            main.DRIVER.find_element(By.XPATH, "//span[normalize-space()='Failure']").click()
            time.sleep(main.THREE_SEC_WAIT)
        else:
            print("\n=================Checking in Success Page.=====================")
        for str_name in func_dict.keys():
            # Convert string name to function name
            if str_name == function_name:
                if func_dict[str_name](page_id) == "FAIL":
                    return status
                break
        else:
            print("Function name is not defined.")
            return status
    else:
        status = close_driver()
        
    return status


if __name__ != "__main__":
    pass
else:
    print("This file is used for defining common functions for Auth Logs Tab.")
    sys.exit()
