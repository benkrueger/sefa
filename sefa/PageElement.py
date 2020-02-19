class PageElement:
    def __init__(self,args: dict) -> None:
        for k in args.keys():
            var = args[k]
            if(k == 'id' and type(var) is str):
                self.id = var
            elif(k == 'text' and type(var) is str):
                self.text = var
            elif(k == 'value' and type(var) is str):
                self.value = var
            elif(k == 'input' and type(var) is str):
                self.input = var
            elif(k == 'img' and type(var) is str):
                self.img = var
            else:
                raise TypeError("{} value {} is formatted incorrectly".format(k,var))
            
            assert self.id is not None and self.text is not None and self.value is not None