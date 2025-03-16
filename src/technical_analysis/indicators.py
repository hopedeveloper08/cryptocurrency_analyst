import pandas_ta as ta


def trend_checker(price, short_sma, long_sma):
    if price > short_sma and price > long_sma:
        return 'صعودی'
    elif price < short_sma and price < long_sma:
        return 'نزولی'
    else:
        return 'رنج'


def sma_trend(df):
    price = df.iloc[-1]['close']

    sma_10 = df.ta.sma(length=10).iloc[-1]
    sma_20 = df.ta.sma(length=20).iloc[-1]
    short_trend = trend_checker(price, sma_10, sma_20)

    sma_50 = df.ta.sma(length=50).iloc[-1]
    sma_100 = df.ta.sma(length=100).iloc[-1]
    mid_trend = trend_checker(price, sma_50, sma_100)

    sma_200 = df.ta.sma(length=200).iloc[-1]
    long_trend = trend_checker(price, sma_200, sma_200)
        
    report = f"وضعیت روندها\nروند کوتاه مدت: {short_trend}\nروند میان مدت: {mid_trend}\nروند بلند مدت: {long_trend}"
    return report


def sr_level_ema(df):    
    l1 = df.ta.ema(length=9).iloc[-1]
    l2 = df.ta.ema(length=21).iloc[-1]
    l3 = df.ta.ema(length=50).iloc[-1]
    l4 = df.ta.ema(length=100).iloc[-1]
    l5 = df.ta.ema(length=200).iloc[-1]
    report = f"سطوح مهم\nقیمت: {l1}\nقیمت: {l2}\nقیمت: {l3}\nقیمت: {l4}\nقیمت: {l5}"
    return report


def ema_signal(df):
    ema_50 = df.ta.ema(length=50)
    past = ema_50.iloc[-2]
    now = ema_50.iloc[-1]
    ema_200 = df.ta.ema(length=200).iloc[-1]
    ema_200_past = df.ta.ema(length=200).iloc[-2]
    if now > ema_200 and past < ema_200_past:
        signal = 'خرید'
    elif now < ema_200 and past > ema_200_past:
        signal = 'فروش'
    else:
        signal = 'هنوز سیگنالی صادر نشده'
    report = f"{signal} :EMA"
    return report


def macd_trend_signal(df):
    macd = df.ta.macd()
    macd_line = macd.iloc[-1, 0]
    signal_line = macd.iloc[-1, 2]
    if macd_line > signal_line:
        trend = 'صعودی'
    else:
        trend = 'نزولی'
    past = macd.iloc[-2, 0]
    signal_past = macd.iloc[-2, 2]
    if macd_line > signal_line and past < signal_past:
        signal = 'خرید'
    elif macd_line < signal_line and past > signal_past:
        signal = 'فروش'
    else:
        signal = 'هنوز سیگنالی صادر نشده'
    report = f"روند مکدی: {trend}\nسیگنال مکدی: {signal}"
    return report


def rsi_signal(df):
    rsi = round(df.ta.rsi().iloc[-1])
    if rsi > 70:
        status = 'اشباع خرید'
    elif rsi < 30:
        status = 'اشباع فروش'
    else:
        status = 'عادی'
    report = f"{status} :RSI وضعیت"
    return report


def cci_signal(df):
    cci = round(df.ta.cci().iloc[-1])
    if cci > 100:
        status = 'اشباع خرید'
    elif cci < -100:
        status = 'اشباع فروش'
    else:
        status = 'عادی'
    if cci > 0:
        trend = 'صعودی'
    else:
        trend = 'نزولی'
    report = f"{trend} :CCI روند\n{status} :CCI وضعیت"
    return report


def stoch_signal(df):
    k, d = df.ta.stoch().iloc[-1].values
    if k < 20 or d < 20:
        signal = 'خرید'
    elif k > 80 or d > 80:
        signal = 'فروش'
    else:
        signal = 'هنوز سیگنالی صادر نشده'
    report = f"استوکاستیک: {signal}"
    return report


def adx_signal(df):
    adx, p, n = df.ta.adx().iloc[-1].values
    if adx > 25 and p > n:
        signal = 'خرید'
    elif adx > 25 and p < n:
        signal = 'فروش'
    else:
        signal = 'هنوز سیگنالی صادر نشده'
    report = f"{signal} :ADX"
    return report


def bband_signal(df):
    price = df.iloc[-1]['close']
    price_past = df.iloc[-2]['close']
    bband = df.ta.bbands()
    now = bband.iloc[-1]
    past = bband.iloc[-2]
    if price_past < past.iloc[0] and price > now.iloc[0]:
        signal = 'خرید'
    elif price_past > past.iloc[2] and price < now.iloc[2]:
        signal = 'فروش'
    else:
        if price > now.iloc[1] and price_past < past.iloc[1]:
            signal = 'خرید'
        elif price < now.iloc[1] and price_past > past.iloc[1]:
            signal = 'فروش'
        else:
            signal = 'هنوز سیگنالی صادر نشده'
    report = f"سیگنال بولینگربند: {signal}"
    return report


def ichimoku_trend(df):
    ichi = df.ta.ichimoku(offset=False)[0]
    tenkan_sen = ichi.iloc[:, 2]
    kijun_sen = ichi.iloc[:, 3]
    senkou_span_a = ichi.iloc[:, 0]
    senkou_span_b = ichi.iloc[:, 1]
    chikou_span = ichi.iloc[:, 4]
    price = df.iloc[-1]['close']

    if price > senkou_span_a.iloc[-1] and price > senkou_span_b.iloc[-1]:
        trend = 'صعودی'
    elif price < senkou_span_a.iloc[-1] and price < senkou_span_b.iloc[-1]:
        trend = 'نزولی'
    else:
        trend = 'رنج'

    if tenkan_sen.iloc[-1] > kijun_sen.iloc[-1] and tenkan_sen.iloc[-2] < kijun_sen.iloc[-2]:
        tk_kj_signal = 'سیگنال خرید'
    elif tenkan_sen.iloc[-1] < kijun_sen.iloc[-1] and tenkan_sen.iloc[-2] > kijun_sen.iloc[-2]:
        tk_kj_signal = 'سیگنال فروش'
    else:
        tk_kj_signal = 'هنوز سیگنالی صادر نشده'

    if chikou_span.iloc[-26] > senkou_span_a.iloc[-26] and chikou_span.iloc[-26] > senkou_span_b.iloc[-26]:
        ck_span_signal = 'سیگنال خرید'
    elif chikou_span.iloc[-26] < senkou_span_a.iloc[-26] and chikou_span.iloc[-26] < senkou_span_b.iloc[-26]:
        ck_span_signal = 'سیگنال فروش'
    else:
        ck_span_signal = 'هنوز سیگنالی صادر نشده'

    report = f"روند ایچیموکو: {trend}\nکراس تنکان و کیجون: {tk_kj_signal}\nکراس چیکو و ابر: {ck_span_signal}"
    return report


def generate_indicators_report(df):
    report = ""
    report += sma_trend(df) + "\n\n"
    report += sr_level_ema(df) + "\n\n"
    report += ema_signal(df) + "\n\n"
    report += macd_trend_signal(df) + "\n\n"
    report += rsi_signal(df) + "\n\n"
    report += cci_signal(df) + "\n\n"
    report += stoch_signal(df) + "\n\n"
    report += adx_signal(df) + "\n\n"
    report += bband_signal(df) + "\n\n"
    report += ichimoku_trend(df) + "\n\n"
    return report
