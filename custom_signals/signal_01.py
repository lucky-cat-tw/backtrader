import backtrader as bt


class Signal_Swing_Trading_Long(bt.Indicator):
    lines = ('signal',)
    params = (('period', 20),)

    def __init__(self):
        # when now close price - SMA_20 >= 0, then buy
        self.lines.signal = self.data - bt.indicators.SMA(period=self.p.period)


class Signal_Swing_Trading_Short(bt.Indicator):
    lines = ('signal',)
    params = (('period', 5),)

    def __init__(self):
        # when now close price - SMA_5 < 0, then sell
        # signal will be trigger once value "self.lines.signal" > 0
        self.lines.signal = bt.indicators.SMA(period=self.p.period) - self.data
