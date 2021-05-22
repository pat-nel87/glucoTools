import os
from guiGraph import graphData
from guiGraph import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import PySimpleGUI as sg
matplotlib.use('TkAgg')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def make_win1():
    sg.theme('Dark Teal 7')
    layout = [
              [sg.Text('Please enter a date to graph in fields below')],
              [sg.Button('View Graph'), sg.Button('Load Meter Data'), sg.Button('Exit')],

              [sg.Text("Year"), sg.Input(key='-YEAR-', size=(10, 1), enable_events=True),
               sg.Text("Month"), sg.Input(key='-MONTH-', size=(10,1), enable_events=True),
               sg.Text("Day"), sg.Input(key='-DAY-', size=(10,1), enable_events=True)]]              
    return sg.Window('glucoTools', layout, location=(800,200), element_justification='center', finalize=True)


def make_win2():
    layout = [
          [sg.Text(dateIn)],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Table(readingList, headings=["Date     | Time "," mg/dl  "], justification='left')],
          [sg.Button('Ok')]]
    return sg.Window('glucoTools-GUI', layout, location=(800, 200),  finalize=True, resizable=True, 
            element_justification='center', font='Monospace 10')

def localFilter():
   temp = []
        
   if values["-DAY-"]:
        temp.append(values["-YEAR-"])
        temp.append(values["-MONTH-"])        
        temp.append(values["-DAY-"])
        return temp    
   elif values["-MONTH-"]:
       temp.append(values["-YEAR-"])
       temp.append(values["-MONTH-"])
       return temp    
   elif values["-YEAR-"]:
       temp.append(values["-YEAR-"])
       return temp

def loadMeter():
    os.system('python loadMeter.py')

window1, window2 = make_win1(), None        # start off with 1 window open


while True:             # Event Loop
    
    window, event, values = sg.read_all_windows()
    sg.theme('Dark Teal 7')
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Ok':
        if window != None:
            window.close()
        if window == window2:       # if closing win 2, mark as closed
            window = make_win1()
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Load Meter Data':
        loadMeter() 
    elif event == 'View Graph' and not window2:
        window.close()
        try:
         dateFilter = localFilter()
         figQuery = graphData(fileIn = "fsNeoReading.txt", fileGraph="latestGraph", dateFilter=dateFilter)
         fig = figQuery.getFig()
         dateIn = figQuery.getDate()
         readingList = figQuery.getList()
         window2 = make_win2()
         fig_canvas_agg = draw_figure(window2['-CANVAS-'].TKCanvas, fig)
        except KeyError:
            window1 = make_win1() 
#window.close()

