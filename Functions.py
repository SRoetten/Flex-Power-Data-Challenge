import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import seaborn as sns
from datetime import datetime, timedelta

from IPython.display import display, HTML

pd.options.display.float_format = '{:,.2f}'.format

def display_side_by_side(dfs:list, captions:list, tablespacing=10):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table caption
    """
    output = ""
    for (caption, df) in zip(captions, dfs):
        output += df.style.hide().set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += tablespacing * "\xa0"
    display(HTML(output))

def Price_prod_graph(df, ASSETS, color, header, SIZE):
    fig, ax1 = plt.subplots(figsize=SIZE)
    palette = color

    f1 = sns.barplot(data = df, y='production_kwh', x='delivery_start', hue = 'mp' ,alpha=0.8, palette = palette)
    f1.set_xticklabels(f1.get_xticklabels(),rotation=40, ha="right");
    f1.set_title(header, fontsize=16)
    
    ax2 = ax1.twinx()
    
    f2 = sns.lineplot(data = df, x='delivery_start', y='market_index_price', marker='o',markers=True, lw=1, color = 'black', sort = False, label = 'Market_Index_price')

    f3 = sns.lineplot(data = df, x='delivery_start', y='price_fcst_eur_per_mwh', marker='o',markers=True, lw=1, color = 'blue', sort = False, label = 'FCST_Price')

    f4 = sns.lineplot(data = df, x='delivery_start', y=ASSETS.price__eur_per_mwh.mean(), marker='o',markers=True, lw=1, color = 'red', sort = False, label = 'Fixed_Price')
    ax2.legend(loc=2)
    
    ax2.set(ylabel='Prices (Market_Index, Forecasted & Fixed')
    ax2.set_ylim(ymin=0) # let bars touch the bottom of the plot
            
    return 