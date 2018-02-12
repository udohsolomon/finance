import pandas as pd


def same_timeseries(ts1, ts2):
    """
    return True if timeseries ts1 == timeseries ts2.

    :param ts1: pandas Dataframe object
    :param ts2: pandas Dataframe object
    :return: True if ts1 and ts2 are at least identical (Allowed Difference - 0.00001).
    """
    if len(ts1) == len(ts2):
        return (sum(ts1.values - ts2.values) < 10**-5).all()
    else:
        return False


def find_differences(bbg_df, quandl_df, csv_file_path=None):
    """
    prints or saves to csv the differences between two timeseries files.

    :param bbg_df: pandas Dataframe object
    :param quandl_df: pandas Dataframe object
    :param csv_file_path: path to save the output csv file (default=None)
    If csv_file_path is not None, will save the output to a csv file.
    :return: None.

    for each ticker find the start date of data from both sources,
    and prints True/False if prices series match since the common start date.

    Compare (BBG 'price' to quandl 'close price')

    CSV output example:
    
        Ticker, Quantle Start Date, BBG Start Date, Match since common start date?
        DOC US Equity ,2000-01-01, 1990-01-01, True
        ABO US Equity ,1999-01-01, 1990-01-01, False
        ...
        ...
        ...
        ABO US Equity ,1999-01-01, 1990-01-01, False
    
    """
    
    # write your code here.
    result = ""
    
    # save csv if file path was specified:
    if csv_file_path:
        csv_file = open(csv_file_path, 'w')
        csv_file.write(result)
        csv_file.close()
    
    print result

if __name__=="__main__":
    bbg_df = pd.read_csv("bbg_data2.csv", header=[0,1], index_col=0)
    quandl_df = pd.read_csv("quantl_data2.csv", header=[0,1], index_col=0)
    find_differences(bbg_df, quandl_df, "output.csv")