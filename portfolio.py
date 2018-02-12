import sys
import pandas as pd
import matplotlib.pyplot as plt
 

def plot_dr_ratio(portfolio_index, dr):
    """
	:param portfolio_index: pandas Dataframe object of the portfolio index
	:param dr: pandas Dataframe object of the DR ratio
	"""
	
	# do your magic here
    plt.show()


def rolling_dr_ratio(df, rolling_window_size=200):
    """
	calculates and plots the dr ratio.
	
    :param df: the dataframe contains the daily total return price change, the weights and the portfolio index.
    :param rolling_window_size: default to 200 days.
    :return: None.
    """
    # some tests

    # calculate the rolling DR ratio
    # dr = ...

    # plot index and the rolling dr
    plot_dr_ratio(df["Portfolio_Index"], dr)


if __name__=="__main__":
    df = pd.read_csv("dr.csv", index_col=0, header=[0,1], parse_dates=0)
	rolling_dr_ratio(df)