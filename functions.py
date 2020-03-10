# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:14:06 2019

@author: Antoine
"""

import pandas as pd
from bokeh.plotting import figure, show, output_file, output_notebook, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.layouts import row

def results_test(data, gs_model, test_index, pred, y_test):
    model_predict = pd.Series(pred, index=test_index)
    perf_model = pd.concat([y_test,model_predict], axis=1)
    perf_model.columns = ['real', 'prediction']
    perf_model['%_error'] = (perf_model['prediction'] - perf_model['real']) / perf_model['real'] * 100
    tempo = data.loc[test_index, ['LargestPropertyUseType', 'LargestPropertyUseTypeGFA',
                             'SecondLargestPropertyUseType', 'SecondLargestPropertyUseTypeGFA',
                             'ThirdLargestPropertyUseType', 'ThirdLargestPropertyUseTypeGFA']]
    perf_model_concat = pd.concat([perf_model, tempo], axis=1, join='inner')
    return(perf_model_concat)

def show_pred_vs_real_test(results_df_test):
	source = ColumnDataSource(results_df_test)
	p = figure(title = "Prediction vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')])
	p.xaxis.axis_label = 'Real'
	p.yaxis.axis_label = 'Prediction'
	p.circle("real", "prediction", source=source)
	p.line("real", "real", color='orange', source=source)
	output_notebook()
	show(p)

def show_error_vs_real_test(results_df_test):
	source = ColumnDataSource(results_df_test)
	p = figure(title = "Error vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')])
	p.xaxis.axis_label = 'Real'
	p.yaxis.axis_label = '% Error'
	p.circle("real", '%_error', source=source)
	output_notebook()
	show(p)
    
def results_train(data, gs_model, train_index, pred, y_train):
    model_predict = pd.Series(pred, index=train_index)
    perf_model = pd.concat([y_train,model_predict], axis=1)
    perf_model.columns = ['real', 'prediction']
    perf_model['%_error'] = (perf_model['prediction'] - perf_model['real']) / perf_model['real'] * 100
    tempo = data.loc[train_index, ['LargestPropertyUseType', 'LargestPropertyUseTypeGFA',
                             'SecondLargestPropertyUseType', 'SecondLargestPropertyUseTypeGFA',
                             'ThirdLargestPropertyUseType', 'ThirdLargestPropertyUseTypeGFA','PropertyGFATotal']]
    perf_model_concat = pd.concat([perf_model, tempo], axis=1, join='inner')
    return(perf_model_concat)

def show_pred_vs_real_train(results_df_train):
	source = ColumnDataSource(results_df_train)
	p = figure(title = "Prediction vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
			('Building surface', '@PropertyGFATotal{0,0}'),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')])
	p.xaxis.axis_label = 'Real'
	p.yaxis.axis_label = 'Prediction'
	p.circle("real", "prediction", source=source)
	p.line("real", "real", color='orange', source=source)
	output_notebook()
	show(p)

def show_error_vs_real_train(results_df_train):
	source = ColumnDataSource(results_df_train)
	p = figure(title = "Error vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
			('Building surface', '@PropertyGFATotal{0,0}'),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')])
	p.xaxis.axis_label = 'Real'
	p.yaxis.axis_label = '% Error'
	p.circle("real", '%_error', source=source)
	output_notebook()
	show(p)

def show_perf(results_df_train):

	source = ColumnDataSource(results_df_train)

	p1 = figure(title = "Prediction vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
			('Building surface', '@PropertyGFATotal{0,0}'),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')],
			plot_width=500, plot_height=500)
	p1.xaxis.axis_label = 'Real'
	p1.yaxis.axis_label = 'Prediction'
	p1.circle("real", "prediction", source=source)
	p1.line("real", "real", color='orange', source=source)

	p2 = figure(title = "Error vs real", tools='pan, box_zoom, undo, reset, hover', 
           	tooltips =[("index", "@index"),
                      	("prediction", "@prediction{0,0}"),
                      	("real", "@real{0,0}"),
			('Building surface', '@PropertyGFATotal{0,0}'),
                      	('Primary usage', '@LargestPropertyUseType, @LargestPropertyUseTypeGFA{0,0}'),
                      	('Second usage', '@SecondLargestPropertyUseType, @SecondLargestPropertyUseTypeGFA{0,0}'),
                      	('Third usage', '@ThirdLargestPropertyUseType, @ThirdLargestPropertyUseTypeGFA{0,0}')],
			plot_width=500, plot_height=500)
	p2.xaxis.axis_label = 'Real'
	p2.yaxis.axis_label = '% Error'
	p2.circle("real", '%_error', source=source)

	output_notebook()
	show(row(p1,p2))


