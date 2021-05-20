#!/usr/bin/env python


# Using PySimpleGUI/matplotlib
# to create a GUI interface
# for glucoTools
from guiGraph import graphData
from guiGraph import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
matplotlib.use('TkAgg')

 



# figQuery = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2021,3,25])
figQuery = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2021,3])
fig = figQuery.getFig()
dateIn = figQuery.getDate()
readingList = figQuery.getList()

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------
sg.theme('Dark Teal 7')
# define the window layout
layout = [
          [sg.Text(dateIn)],                                  
          [sg.Canvas(key='-CANVAS-')],
          [sg.Table(readingList, headings=["Date     | Time "," mg/dl  "], justification='left')],
          [sg.Button('Ok')],
         ]

# create the form and show it without the plot
window = sg.Window('glucoTools-GUI', layout, finalize=True, resizable=True, element_justification='center', font='Monospace 10')

# add the plot to the window
fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()
