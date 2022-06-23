import yfinance as yf

if __name__ == "__main__":
    novo_nordisk = yf.Ticker("NVO")

    history = novo_nordisk.history()

    print(history)
