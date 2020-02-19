import json
from selenium import webdriver
from sefa import PageState
from sefa import PageAction

class NoDriverException(Exception):
    def __init__(self,message: str) -> None:
        self.message = message
class InvalidStateException(Exception):
    def __init__(self,message: str) -> None:
        self.message = message

class SeleniumFiniteAutomata:
    def __init__(self,**kwargs) -> None:
        if kwargs['driver'] is not None:
            self.driver = kwargs['driver']
        else:
            raise NoDriverException("No driver given for SeFA...")
        
        if type(kwargs['timeout']) is float or type(kwargs['timeout']) is int:
            self.timeout = kwargs['timeout']
        else:
            raise TypeError("Must give number for timeout")
        
        if type(kwargs['save_ss']) is bool:
            self.save_ss = kwargs['save_ss']
        else:
            raise TypeError("Must give bool to save screenshot.")
        
        if type(kwargs['start_url']) is str:
            self.start_url = kwargs['start_url']
        else:
            raise TypeError("Must give string for start url..")

        if type(kwargs['spec']) is dict:
            spec_d = kwargs['spec']
            for k in spec_d.keys():
                var = spec_d[k]
                if(k == 'states' and type(var) is list):
                    self.states = [PageState(l) for l in var]
                elif(k == 'timeout' and (type(var) is int or type(var) is float)):
                    if self.timeout is None:
                        self.timeout = var
                elif(k == 'start_url' and type(var) is str and self.start_url is None):
                    self.start_url = var
                elif(k == 'transitions' and type(var) is dict):
                    self.transitions = var
                elif(k == 'actions' and type(var) is list):
                    self.actions = [PageAction(l) for l in var]
                elif (k == 'accept_states' and type(var) is list):
                    self.accept_states = [str(l) for l in var]
                else:
                    raise TypeError("{} value {} is not correct value".format(k,var))
                
        else:
            raise TypeError("Spec must be a dict")
        assert self.driver is not None and self.start_url is not None and self.accept_states is not None and self.transitions is not None
    def execute(self):
        pass
    def verify_state(self):
        pass
    def is_accepting_state(self):
        pass