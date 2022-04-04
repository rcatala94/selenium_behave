# -*- coding: utf-8 -*-
u"""

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time, os

def driver_start(context, device_config):
    """ Connect with a remote Selenium server

    Driver is stored in context.driver variable

    :param context: Behave session context
    :param device_config: Dictionary with device configuration parameters
    """
    print("\nStarting the selenium webdriver")

    if 'chrome' in device_config['browser_name']:
        browser_options = ChromeOptions()
        browser_options.add_argument(device_config['windowSize'])
        browser_options.add_argument('log-level=3')
    else:
        raise RuntimeError(f"Configuration not found for the {device_config['browser_name']} browser") 

    try:
        context.driver = webdriver.Chrome(executable_path = device_config['browser_path'], options = browser_options)
        context.driver.maximize_window()
    except Exception:
        raise

    if device_config['url']:
        context.driver.get(device_config['url'])

    return context.driver

def driver_stop(context, device_config):
    """ Stop the selenium driver
    """
    if device_config['screenshot']:
        timestr = time.strftime
        path = f'{os.getcwd()}\\Screenshot_selenium\\{timestr("%Y")}\\{timestr("%m")}\\{timestr("%d")}'
        file = f'Screenshot_appium{timestr("%H%M%S")}.png'
        logfile = f'{path}\\{file}'

        if not os.path.exists(path):
            # Create a new directory because it does not exist 
            os.makedirs(path)

        #print(f'Path the Screenshot -> {logfile}\n')
        context.driver.get_screenshot_as_file(logfile)
    context.driver.close()
    context.driver.quit()