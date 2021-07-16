import backtrader as bt


class Signal_Intraday_Trading_Long(bt.Strategy):
    lines = ('signal',)
    params = (('period', 15),)

    def __init__(self):
        # if current volumne >= 5 * volumne(SMA_15), then buy!
        self.lines.signal = (0, 1)[self.data.volume / bt.indicators.Average(self.data.volume, period=self.p.period) >= 5]
        print('ssssssssssss')


class Signal_Intraday_Trading_Short(bt.Indicator):
    lines = ('signal',)
    params = (('period', 5),)

    def __init__(self):
        # when now close price - SMA_5 < 0, then sell
        # signal will be trigger once value "self.lines.signal" > 0
        self.lines.signal = bt.indicators.SMA(period=self.p.period) - self.data.close
