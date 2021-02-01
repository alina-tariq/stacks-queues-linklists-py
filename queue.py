class Queue:
    # intializes queue
    def __init__(self):
        self.queue = []

    # inserts share quantity and price
    def enqueue(self, item):
        self.queue.insert(0, item)

    # removes shares using fifo principle
    def dequeue(self):
        self.queue.pop()

    # returns number of first block of shares
    def share(self):
        return self.queue[-1][0]

    # returns price of first block of shares
    def price(self):
        return self.queue[-1][1]

    # returns total shares owned
    def partial(self, item):
        self.queue[-1][0] = item


shares = Queue()
capital = 0
trans = [
    "buy 100 shares at $20 each",
    "buy 20 shares at $24 each",
    "sell 50 shares at $22 each",
    "buy 80 shares at $27 each",
    "sell 50 shares at $30 each",
    "sell 100 shares at $15 each",
]

for a in range(len(trans)):
    words = trans[a].split()
    # adds share numbers and prices to queue holding buying info
    if words[0] == "buy":
        buyprice = words[4]
        shares.enqueue([int(words[1]), float(buyprice[1:])])
    # sells off shares and calculates capital gain/loss
    elif words[0] == "sell":
        sellshares = int(words[1])
        sellprice = words[4]
        sellprice = float(sellprice[1:])
        while sellshares:
            # when partial blocks needs to be sold
            if sellshares < shares.share():
                capital += sellshares * (sellprice - shares.price())
                shares.partial(shares.share() - sellshares)
                sellshares = 0
            # when exactly one block needs to be sold
            elif sellshares == shares.share():
                capital += sellshares * (sellprice - shares.price())
                sellshares = 0
                shares.dequeue()
            # when more than one block needs to be sold
            else:
                capital += shares.share() * (sellprice - shares.price())
                sellshares = sellshares - shares.share()
                shares.dequeue()  # removes share block

if capital >= 0:
    print("Total capital gain: $%.2f" % capital)
else:
    print("Total capital loss: $%.2f" % abs(capital))
