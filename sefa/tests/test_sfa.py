from sefa import SeleniumFiniteAutomata
from selenium import webdriver

def test_init():
    wd = "asdf"
    my_fa = SeleniumFiniteAutomata.SeleniumFiniteAutomata(driver=wd,spec='./tests/test_spec.json')

def test_execute():
    pass
def test_is_accepting_state():
    pass