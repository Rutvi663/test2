"""
 * ----------------------------------------------------------------------
 * Copyright (c) 2024, System Level Solutions (India) Pvt. Ltd.
 * ----------------------------------------------------------------------
 *      Purpose   : Verify Auth Logs module
 *      Package   : WISUN TestCases
 *      File name : TC002_Auth_Logs_Module_Start_Date_End_Date.py
 *      Project   : Wi-SUN Project
 * ----------------------------------------------------------------------
"""

import os
import sys
import time

from datetime import date
from datetime import datetime, timedelta

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

from Node_Test_Scripts.Main.main import (
    open_nms,
    close_driver,
    exception_handling,
    find_total_rows_columns,
    select_value_from_dropdown,
)

from Auth_Logs_Main.auth_logs_main import click_on_auth_logs, verify_in_both_pages, VALUE_FROM_DROPDOWN

# from Events_Main import main  # noqa
from Node_Test_Scripts.Main import main  # noqa

"""
The purpose of this file is to verify start/end date filter functionality.
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
This is Start and End Datetime Test Case.
Select valid start and end date from the filter in Auth logs Tab.
Verify whether all logs should be between start and end date time."""
    )
    status = open_nms()

    return status


def verify_datetime_in_logs(page_id):
    """
    This function is used to verify whether all logs should be displayed between
    selected start/end datetime.
    :param:
        page_id:str
    return:
        status:str
    """
    status = "FAIL"
    number_of_days = 7
    end_date_time = datetime.combine(date.today(), datetime.min.time())
    start_date_time = end_date_time - timedelta(number_of_days)
    try:
        if select_value_from_dropdown(page_id, VALUE_FROM_DROPDOWN) == "FAIL":
            return status
        print(
            "===================Check whether all the logs between Start/End date is present==================="
        )
        time.sleep(main.FIVE_SEC_WAIT)
        # Find total rows
        total_rows, _ = find_total_rows_columns("{}".format(page_id))
        if total_rows == main.ZERO_LENGTH:
            print("Total row length is zero.")
            close_driver()
            return status
        first_row = main.DRIVER.find_element(
            By.XPATH,
            "//div[@id='{}']//table[@role='presentation']/tbody/tr[1]/td[1]".format(
                page_id
            ),
        ).text

        if first_row == "No records available.":
            print(
                "No logs found between {} and {}".format(start_date_time, end_date_time)
            )
            close_driver()
            return status
        for row in range(1, total_rows + 1):
            # Get all data from fourth column and every rows
            date_time = main.DRIVER.find_element(
                By.XPATH,
                "//div[@id='{}']//table[@role='presentation']/tbody/tr[{}]/td[2]".format(
                    page_id, row
                ),
            ).text
            log_date_time = datetime.strptime(
                    date_time.split(" ")[main.START_INDEX], "%d/%m/%Y"
                )
            if start_date_time <= log_date_time <= end_date_time:
                print("{} is between {} and {}.".format(log_date_time, start_date_time, end_date_time))
            else:
                print(
                    f"{log_date_time} is not between {start_date_time} and {end_date_time}"
                )
                close_driver()
                return status
        else:
            print("Start and End Date time Filter is working properly.")
            status = "PASS"
    except Exception as err:
        print("Error in 'verify_datetime_in_logs'.")
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
    if verify_in_both_pages("verify_datetime_in_logs") == "FAIL":
        print("verify_in_both_pages : ", "FAIL")
        sys.exit(1)
    else:
        print("\n==================PASS==================\n")
