from datetime import date

import yfinance as yf


def get_change_between_dates(
    tickers: list[str],
    start: date = None,
    end: date = None,
) -> float:
    days_between_dates = (end - start).days
    interval =
    print(type(time_difference))
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
    )
    return data


if __name__ == "__main__":
    start = date(2017, 11, 1)
    end = date.today()
    data = get_change_between_dates(tickers=["NVO", "DANSKE.CO"], start=start, end=end)

    print(data.info)
