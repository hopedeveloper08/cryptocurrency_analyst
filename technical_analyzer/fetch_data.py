import yfinance as yf
from datetime import timedelta, datetime


def calculate_start_time(interval):
    if interval == '1m':
        time_delta = timedelta(minutes=1000)
    elif interval == '5m':
        time_delta = timedelta(minutes=1500)
    elif interval == '15m':
        time_delta = timedelta(hours=80)
    elif interval == '30m':
        time_delta = timedelta(hours=150)
    elif interval == '1h':
        time_delta = timedelta(hours=300)
    elif interval == '1d':
        time_delta = timedelta(days=300)
    elif interval == '1wk':
        time_delta = timedelta(weeks=250)
    start_time = datetime.now() - time_delta
    return start_time


def fetch_data(symbol, interval):
    start_time = calculate_start_time(interval)
    df = yf.download(
        f'{symbol}-usd',
        start=start_time,
        interval=interval,
        multi_level_index=False,
        auto_adjust=True,
    )
    return df
