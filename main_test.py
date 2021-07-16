from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt

# from relvolbybar import RelativeVolumeByBar
from custom_signals import signal_01, signal_02


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    # datapath = os.path.join(modpath, '.\\custom_datas\\finmind_tw_2330.csv')
    datapath = os.path.join(modpath, '.\\custom_datas\\finmind_price_tick_1504_20210621.csv')

    # Create a Data Feed
    # for custom csv format, please refer: https://www.backtrader.com/docu/datafeed/#genericcsvdata
    # data = bt.feeds.GenericCSVData(
    #     dataname=datapath,
    #     fromdate=datetime.datetime(2018, 1, 1),
    #     todate=datetime.datetime(2021, 12, 31),
    #     nullvalue=0.0,
    #     dtformat=('%Y-%m-%d'),
    #     datetime=1,
    #     high=6,
    #     low=7,
    #     open=5,
    #     close=8,
    #     volume=3
    # )

    # for intraday timeframes (finmind intraday dataset)
    # please refer: https://community.backtrader.com/topic/244/backtesting-1-minute-data
    data = bt.feeds.GenericCSVData(
        dataname=datapath,
        sessionstart=datetime.time(9, 0),
        sessionend=datetime.time(13, 30),
        timeframe=bt.TimeFrame.Seconds,
        compression=1,
        dtformat=('%H:%M:%S.%f'),
        datetime=5,
        high=3,
        low=3,
        open=3,
        close=3,
        volume=4
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Add a strategy
    # cerebro.addstrategy(test_strategy.TestStrategy)
    # Or, just add a signal
    cerebro.add_signal(bt.SIGNAL_LONG, signal_01.Signal_Swing_Trading_Long)
    cerebro.add_signal(bt.SIGNAL_SHORT, signal_01.Signal_Swing_Trading_Short)
    # cerebro.add_signal(bt.SIGNAL_LONG, signal_02.Signal_Intraday_Trading_Long)
    # cerebro.add_signal(bt.SIGNAL_SHORT, signal_02.Signal_Intraday_Trading_Short)

    # Set our desired cash start
    cerebro.broker.setcash(1000.0)

    # Add a FixedSize sizer according to the stake
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    # Set the commission
    cerebro.broker.setcommission(commission=0.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Plot the result
    cerebro.plot()
