from datetime import date

import yfinance as yf


def get_change_between_dates(
    tickers: list[str],
    start: date = None,
    end: date = date.today(),
) -> float:
    if start is None:
        start = date.today()
        start.month = start.month - 3
    days_between_dates = (end - start).days
    interval = int(days_between_dates / 90)
    if interval >= 1:
        interval = "3mo"
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        interval=interval,
    )
    changes = {}
    data = data["Open"]
    for ticker in tickers:
        ticker_data = data[ticker]
        index = ticker_data.index
        first_value = ticker_data[index[0]]
        last_value = ticker_data[index[-1]]
        changes[ticker] = (last_value / first_value - 1) * 100
    return changes


if __name__ == "__main__":
    start = date(2017, 11, 1)
    end = date.today()
    data = get_change_between_dates(tickers=["NVO", "DANSKE.CO"], start=start, end=end)

    print(data)
