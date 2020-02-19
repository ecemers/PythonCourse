#INTL550 - Homework 1#
#Ecem ERSÖZLÜ

stock_prices = dict({})
mut_fund = dict({})
stocks = dict({})

class Stock(object):

    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
        stock_prices[symbol] = {price}

class MutualFund(object):

    def __init__(self, symb):
        self.symb = symb

class Portfolio(object):

    def __init__(self, cash=0, stocks={}, mut_fund={}):
        self.cash = cash
        self.stocks = stocks
        self.mut_fund = mut_fund
        self.db = {}

    def addCash(self, amount):
        self.cash += amount
        print(f"\n ${amount} added to balance.")

    def withdrawCash(self, amount):
        if  self.cash >= amount:
            self.cash -= amount
            print(f"\n ${amount} withdrawn from balance.")
        else:
            print("\n Unable to complete request due to insufficient funds.")

    def __str__(self):
        return "%s\n%s\n%s" %(f"Cash: ${self.cash}", f"Stock: {self.stocks}", f"Mutual Funds: {mut_fund}")

    def buyStock(self, share, symbol):
        self.share = share
        self.symbol = symbol
        sp = stock_prices.get(symbol, )
        if self.cash >= sp:
            self.stocks[symbol] = {share}
            Portfolio.withdrawCash(sp * share)
            print("Transaction complete!")
        else: print("\n Unable to complete request due to insufficient funds.")

    def sellStock(self, symbol, share):
        self.share = share
        self.symbol = symbol
        if symbol in self.stocks:
            del self.stocks[symbol]
            self.cash += float(self.sp) * self.random.uniform(0.5,1.5)
            print("Transaction complete!")
        else: print("You do not own a share of this stock.")

    def buyMutualFund(self, mfshare, symb):
        self.mfshare = mfshare
        self.symb = symb
        if self.cash >= mfshare:
           mut_fund[self.symb] = {self.mfshare}
           self.cash -= float(self.mfshare)
           print("Transaction complete!")
        else: print("\n Unable to complete transaction due to insufficient funds.")

    def sellMutualFund(self, symb, mfshare):
        self.mfshare = mfshare
        self.symb = symb
        try:
            del self.mut_fund[symb]
            self.cash += float(self.mfshare) * self.random.uniform(0.9,1.2)
            print("Transaction complete!")
        except KeyError:
            print("You do not own a share of this mutual fund.")

    def history():
        pass
