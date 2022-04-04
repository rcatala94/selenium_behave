import os, json, logging
from utils.driver_helper import *
from behave.log_capture import capture

@capture
def before_all(context):
    """ Executed before any test execution
    Initialize the device configuration from a json file
    """
    # Initialize logger
    context.logger = logging.getLogger("Selenium Behave testsuite")
    context.logger.setLevel(logging.DEBUG)

    # Load behave's userdata parameters
    config_file = context.config.userdata['browsers_capabilities_path']
    udid = context.config.userdata['udid']

    # Load devices configuration file
    if os.path.exists(config_file) :
        with open(config_file) as file:
            devices_configs = json.load(file)
    else:
        context.logger.info("Configuration file: {} not found ".format(config_file))
        raise RuntimeError("File not found")

    # Find the device specific configuration
    device = {}
    for config in devices_configs:
        if udid == config['udid']:
            device = config

    if device:
        context.logger.info("Configuration for device with udid: {} found".format(udid))
        # Store device config
        context.config.capabilities = device
    else:
        context.logger.info("Configuration for device with udid: {} not found in config file: {}".format(udid, config_file))
        raise RuntimeError("Configuration not found")

def before_feature(context, feature):
    """ Initialize feature with tags
    """
    context.logger.info("Feature execution: {}".format(feature.name))
    if 'MeliaSearch' in feature.tags:
         context.config.capabilities['url'] = 'https://www.melia.com'
    elif 'MeliaRooms' in feature.tags:
        context.config.capabilities['url'] = 'https://www.melia.com/es/hoteles/espana/madrid/melia-castilla/habitaciones.htm'
    else:
         context.config.capabilities['url'] = ''

def before_scenario(context, scenario):
    """ Initialize scenario
    """
    context.logger.info("Scenario execution: {}".format(scenario.name))
    driver_start(context, context.config.capabilities)

def after_scenario(context, scenario):
    """ Finalize scenario
    """
    context.logger.info("Scenario finished: {}".format(scenario.name))
    driver_stop(context, context.config.capabilities)

def after_feature(context, feature):
    """Finalize feature
    """
    context.logger.info("Feature finished: {}".format(feature.name))

def after_all(context):
    """Executed after the test execution
    """
    context.logger.info("Feature after_all: {}")