class PageAction:
    def __init__(self,args: dict) -> None:
        for k,v in args.items():
            if(k == 'id' and type(v) is str):
                self.id = v
            elif(k == 'target' and type(v) is str):
                self.target = v
            elif(k == 'type' and type(v) is str):
                self.type = v
            elif(k == 'input' and type(v) is str):
                self.input = v
            else:
                raise TypeError("{} value {} is not correct value".format(k,v))
        
        assert self.id is not None and self.target is not None and self.type is not None
