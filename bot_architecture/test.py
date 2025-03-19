from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract
import threading
import time

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    
    # Callback for real-time bar updates
    def realtimeBar(self, reqId, time, open, high, low, close, volume, wap, count):
        bot.on_bar_update(reqId, time, open, high, low, close, volume, wap, count)

class Bot:
    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7497, 1)
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()
        time.sleep(1)
        
        symbol = input("Enter the symbol for trading: ")
        # Create contract
        contract = Contract()
        contract.symbol = symbol.upper()
        contract.secType = "STK"
        contract.exchange = "SMART"  # Options: AUTO, SMART, NYSE, etc.
        contract.currency = "USD"
        
        # Request real-time bar data
        self.ib.reqRealTimeBars(0, contract, 5, "TRADES", 1, [])

    def run_loop(self):
        self.ib.run()

    # Real-time bar update callback handler
    def on_bar_update(self, reqId, time, open, high, low, close, volume, wap, count):
        print("Bar Update. ReqID:", reqId, "Time:", time)

bot = Bot()

#Need to enable IBKR Subscription for US Stock Data in Account Management