import yfinance as yf


def get_data(ticks):
    data = yf.Ticker(ticks)
    print(data.info["currentPrice"])



if __name__ == "__main__":

    us_stocks = open("us_stocks_track.config", "r")
    for ticks in us_stocks:
        print(ticks)
        get_data(ticks)