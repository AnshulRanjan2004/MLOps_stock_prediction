from datetime import datetime, timedelta
import logging
import yfinance as yf
import pandas as pd
import os
import pandas as pd

def get_ticker_data(TICKER:str):

    with open(os.environ['GITHUB_OUTPUT'],'a') as f:
        print('filename=TICKER', f)
        
    data = pd.DataFrame({'Date':[1,2,3],'Close':[10,20,30]})

    data.to_csv('data_writeout.csv',index=False)

    # try:
        # start = str(datetime.today().date()-timedelta(days=366))
        # end = str(datetime.today().date()-timedelta(days=1))

        # tickerData=yf.download(TICKER,start=start, end=end, period='1d')
        # tickerData['Date']=[str(x)[:10] for x in tickerData.index]

        # if tickerData.shape[0]==0:
        #     raise ValueError("No data found via YFinance.")

        # tickerData['Ticker']=TICKER
        # tickerData = tickerData['Close']
        # logging.info(f"Length of ticker data: {len(tickerData.index)}")


        # with open(os.environ['GITHUB_OUTPUT'], 'w') as f:
            # json.dump(data, f)

        # print(tickerData['Close'])
    # except:
    #     logging.error("Problem with downloading data from YFinance.")

# def upload_data(ml_client, path, TICKER):

#     try:
#         ticker = TICKER[:TICKER.index('.')]
#         ticker_data = pd.read_csv(path)
#         ticker_data.index=ticker_data['Date']
#         ticker_data.drop(["Date"],axis=1,inplace=True)
#         data_to_upload=Data(
#             name=ticker,
#             version=re.sub('-','',str(datetime.today().date())),
#             description=f"Stock data for {TICKER} during {str(ticker_data.index[0][:10])}:{str(ticker_data.index[-1][:10])} in 1d interval.",
#             type='uri_file',
#             path=path,
#             tags={
#                 'Length':len(ticker_data),
#                 'Start':str(ticker_data.index[0][:10]),
#                 'End':str(ticker_data.index[-1][:10]),
#                 'Median':ticker_data.median(),
#                 'SD':ticker_data.std()}
#         )
#         ml_client.data.create_or_update(data_to_upload)

#         logging.info(f"Uploaded stock data for {TICKER} during {str(ticker_data.index[0][:10])}:{str(ticker_data.index[-1][:10])} in 1d interval.")
#     except:
#         logging.error("Problem with persisting data to Azure ML datastore.")

if __name__=="__main__":

    TICKER="LT.NS"
    path = get_ticker_data(TICKER=TICKER)

    # if path is not None:
    #     upload_data(ml_client,path, TICKER=TICKER)
