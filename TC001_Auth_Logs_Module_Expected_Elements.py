"""
 * ----------------------------------------------------------------------
 * Copyright (c) 2024, System Level Solutions (India) Pvt. Ltd.
 * ----------------------------------------------------------------------
 *      Purpose   : Verify Auth Logs module
 *      Package   : WISUN TestCases
 *      File name : TC001_Auth_Logs_Module_Expected_Elements.py
 *      Project   : Wi-SUN Project
 * ----------------------------------------------------------------------
"""

import os
import sys
import time

from selenium.webdriver.common.by import By

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

from Node_Test_Scripts.Main.main import open_nms, close_driver, exception_handling

from Auth_Logs_Main.auth_logs_main import click_on_auth_logs, verify_in_both_pages

# from Events_Main import main  # noqa
from Node_Test_Scripts.Main import main

"""
The purpose of this file is to verify whether all expected elements are present in Auth Logs tab of NMS portal.
"""


def Initialization():
    """
    This function is used to open NMS web page
    return:
        status:str
    """
    print(
        """
Test Description:
Test Type : Positive
This is Auth Logs page info test case..
Check whether all the expected buttons and information are present 
after clicking on Auth Logs."""
    )
    status = open_nms()

    return status


def check_auth_logs_expected_elements(page_id):
    """
    This function is used to check all the present elements of Auth logs tab of NMS Home page.
    return:
        status:str
    """
    status = "FAIL"
    try:
        locator_dict = {
            "Start Date Time": "//div[@id='{}']//input[@placeholder='Start Date Time']".format(page_id),
            "End Date Time": "//div[@id='{}']//input[@placeholder='End Date Time']".format(page_id),
            "UTC checkbox": "//div[@id='{}']//input[@type='checkbox']".format(page_id),
            "Table first column": "//div[@id='{}']//th[@role='columnheader'][normalize-space()='Mac']".format(page_id),
            "Table second column": "//div[@id='{}']//th[@role='columnheader'][normalize-space()='Auth Date']".format(page_id),
            "Report Button": "//div[@id='{}']//button[@class='btn bg-theme text-white'][normalize-space()='Report']".format(page_id),
            "Go to first page": "//div[@id='{}']//a[@title='Go to the first page']".format(page_id),
            "Go to previous page": "//div[@id='{}']//a[@title='Go to the previous page']".format(page_id),
            "Go to next page": "//div[@id='{}']//a[@title='Go to the next page']".format(page_id),
            "Go to last page": "//div[@id='{}']//a[@title='Go to the last page']".format(page_id),
            "items per page ": "//div[@id='{}']//select[@aria-label='items per page']".format(page_id)
        }
        for module_name, locater_path in locator_dict.items():
            print("checking if {} is present.....".format(module_name))
            main.DRIVER.find_element(By.XPATH, "{}".format(locater_path))
        else:
            print(
                "\n===================All the above elements are present in {}===================".format(page_id)
            )
            status = "PASS"
    except Exception as err:
        print("Error in 'check_auth_logs_expected_elements'.")
        exception_handling(err)
        close_driver()

    return status


if __name__ == "__main__":
    if Initialization() == "FAIL":
        print("NMS portal open successfully : ", "FAIL")
        sys.exit(1)
    if click_on_auth_logs() == "FAIL":
        print("click_on_auth_logs : ", "FAIL")
        sys.exit(1)
    if verify_in_both_pages("check_auth_logs_expected_elements") == "FAIL":
        print("verify_in_both_pages : ", "FAIL")
        sys.exit(1)
    else:
        print("\n==================PASS==================\n")
