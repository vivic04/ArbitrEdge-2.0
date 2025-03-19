from ibapi.wrapper import EWrapper
from ibapi.client import EClient

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
       

class Bot:
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7496, 1)
        self.ib.run()


bot = Bot()
