from sefa import PageElement

class PageState:
    def __init__(args: dict) -> None:
        for k in args.keys():
            var = args[k]
            if k == 'id' and type(var) is str:
                self.id = var
            elif k == 'screenshot' and type(var) is str:
                self.screenshot = var
            elif k == 'alert' and type(var) is str:
                self.alert = var
            elif k == 'elements' and type(var) is list:
                self.elements = [PageElement(l) for l in var]
            elif k == 'src_str' and type(var) is list:
                self.src_str = [str(l) for l in var]
            else:
                raise TypeError("Invalid {} field in dict.")
        
        assert self.id is not None #only truly required string, all others can be none.
            
