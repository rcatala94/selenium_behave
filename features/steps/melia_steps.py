# -*- coding: utf-8 -*-
u"""
"""

from behave import given, when, then
from features.pageobjects.melia_pageobjects import MeliaPageObject

'''

Section: Web Melia Management

'''

@given(u'Open the Navigator')
def step_impl(context):
    context.current_page = MeliaPageObject(context.driver)

@when(u'Select destination "{destinations}"')
def step_impl(context, destinations):
    context.logger.info("Step - {}".format(destinations))
    context.current_page.goto_search_and_write(destinations)

@when(u'Select date "{dates}"')
def step_impl(context, dates):
    context.logger.info("Step - {}".format(dates))
    context.current_page.goto_dates_and_select(dates)

@when(u'Select persons and search')
def step_impl(context):
    context.current_page.select_persons_and_search()

@then(u'Message Hotels appears')
def step_impl(context):
    assert (context.current_page.loaded() is True)

@then(u'Get All Rooms')
def step_impl(context):
    hotels = context.current_page.get_all_rooms()
    print(hotels)