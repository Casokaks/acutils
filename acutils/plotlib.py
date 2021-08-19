"""
acutils plotlib
==================================
Library to plot charts.

Created on Fri Oct 25 15:07:11 2019
Author: Andrea Casati, andrea1.casati@gmail.com

"""


from sys import exit
import pandas as pd
import numpy as np
from math import ceil
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .list_utils import get_shape


def __update_layout(fig, title_label=None, x_label=None, y_label=None, x_log=False, y_log=False, font=None,
                    height=None, width=None, xaxis_rangeslider_visible=False):
    """
    Return the input figure customised with the input layout.
    """
    title = go.layout.Title(text=title_label, font=font)
    xaxis = go.layout.XAxis(title=go.layout.xaxis.Title(text=x_label, font=font))
    yaxis = go.layout.YAxis(title=go.layout.yaxis.Title(text=y_label, font=font))
    fig.update_layout(title=title, xaxis=xaxis, yaxis=yaxis, height=height, width=width,
                      xaxis_rangeslider_visible=xaxis_rangeslider_visible)
    if x_log:
        fig.update_xaxes(type="log")
    if y_log:
        fig.update_yaxes(type="log")
    return fig


def __make_subplots(graphs_list, rows, cols, column_widths=None, row_heights=None,
                    shared_xaxes=True, vertical_spacing=0.02):
    """
    Return plotly figure with subplots.
    graphs_list is a last list of plotly.graph_objects objects, eg:
    [go.Scatter(x=[0, 1, 2], y=[10, 11, 12]), go.Scatter(x=[2, 3, 4], y=[100, 110, 120])].
    column_widths, row_heights can be None to split columns and rows in equal size,
    or they con be specified as list, eg: column_widths=[0.7, 0.3].
    """
    # reshape input plotly.graph_objects list
    length = len(graphs_list)
    tot = rows * cols
    if tot < length:
        plots_list = graphs_list[:tot]
    elif tot > length:
        rows = ceil(length / cols)
        tot = rows * cols
        add = tot - length
        plots_list = graphs_list + [None] * add
    else:
        plots_list = graphs_list
    plots_list = np.reshape(a=plots_list, newshape=(rows, cols))
    # make figure
    fig = make_subplots(rows=rows, cols=cols, shared_xaxes=shared_xaxes,
                        column_widths=column_widths, row_heights=row_heights, vertical_spacing=vertical_spacing)
    for r, row in enumerate(plots_list):
        for c, chart in enumerate(row):
            if chart is not None:
                fig.add_trace(trace=chart, row=r+1, col=c+1)
    return fig


def plot_series(series_df, title_label=None, x_label=None, y_label=None, x_log=False, y_log=False, font=None,
                show_legend=True, x_slider=False):
    """
    Plot all series in the data frame using plotly.
    Customize fonts passing a dictionary like:
    font = dict(family="Courier New, monospace", size=18, color="#7f7f7f")
    """
    fig = go.Figure()
    if isinstance(series_df, pd.DataFrame):
        df = series_df
    else:
        df = pd.DataFrame(series_df)
    df.apply(lambda series:
             fig.add_trace(go.Scatter(x=series.index, y=series, name=series.name, showlegend=show_legend)),
             axis=0)
    fig = __update_layout(fig=fig, title_label=title_label, x_label=x_label, y_label=y_label,
                          x_log=x_log, y_log=y_log, font=font, xaxis_rangeslider_visible=x_slider)
    fig.show()


def plot_series_stack(series_df_list, height=None, width=None, row_heights=None, column_widths=None,
                      y_type=None, x_type=None, showlegend=True, y_showgrid=True, x_showgrid=True,
                      shared_xaxes=False, shared_x_label=None, shared_yaxes=False, shared_y_label=None,
                      title_label=None, subplot_titles=None, subplot_x_labels=None, subplot_y_labels=None):
    """
    Plot all dataframes in input list in subsequent stacked sub-plots.
    series_df_list is a list of lists of dataframes. Each df contains the series to plot in each graph.
    the shape of series_df_list will give the shape to the whole figure. e.g. :
    [[df1, df2],[df3, df4]] will result in a 2 rows x 2 columns subplot figure.
    [[df1, df2, df3, df4]] will result in a 1 row x 4 columns subplot figure.
    subplot_titles=("First Subplot","Second Subplot", "Third Subplot"). Do not make it it nested.
    subplot_x_labels (for y the same) will need to replicate series_df_list structure.
    y_type = "log" for log scale. same for x_axes if needed.
    """
    # check input shape
    shape = get_shape(lst=series_df_list)
    # make figure
    if not shared_xaxes:
        shared_x_label = None
    if not shared_yaxes:
        shared_y_label = None
    fig = make_subplots(rows=shape[0], cols=shape[1],
                        row_heights=row_heights, column_widths=column_widths,
                        shared_xaxes=shared_xaxes, x_title=shared_x_label,
                        shared_yaxes=shared_yaxes, y_title=shared_y_label,
                        subplot_titles=subplot_titles)
    # make plots
    for r, row in enumerate(series_df_list):
        for c, df in enumerate(row):
            # chart
            df.apply(lambda series:
                     fig.add_trace(go.Scatter(x=series.index, y=series, name=series.name, showlegend=showlegend),
                                   row=r + 1, col=c + 1),
                     axis=0)
            # layout
            fig.update_xaxes(row=r + 1, col=c + 1, showgrid=x_showgrid, type=x_type)
            if subplot_x_labels is not None:
                fig.update_xaxes(row=r + 1, col=c + 1, title_text=subplot_x_labels[r][c])
            fig.update_yaxes(row=r + 1, col=c + 1, showgrid=y_showgrid, type=y_type)
            if subplot_y_labels is not None:
                fig.update_yaxes(row=r + 1, col=c + 1, title_text=subplot_y_labels[r][c])
    # customize figure
    fig.update_layout(title_text=title_label, height=height, width=width, xaxis_rangeslider_visible=False)
    fig.show()


def plot_ohcl(date_series, open_series, high_series, close_series, low_series, x_log=False, y_log=False,
              chart_type='candlestick', title_label=None, x_label=None, y_label=None, font=None, x_slider=False):
    """
    Plot OHCL chart of input series using plotly.
    Customize fonts passing a dictionary like:
    type: {'candlestick', 'ohcl'}
    font = dict(family="Courier New, monospace", size=18, color="#7f7f7f")
    """
    if chart_type == 'candlestick':
        chart = go.Candlestick(x=date_series, open=open_series, high=high_series, low=low_series, close=close_series)
    elif chart_type == 'ohcl':
        chart = go.Ohlc(x=date_series, open=open_series, high=high_series, low=low_series, close=close_series)
    else:
        print('ERROR - chart_type not recognized')
        exit(-1)
    fig = go.Figure(data=[chart])
    fig = __update_layout(fig=fig, title_label=title_label, x_label=x_label, y_label=y_label,
                          x_log=x_log, y_log=y_log, font=font, xaxis_rangeslider_visible=x_slider)
    fig.show()
