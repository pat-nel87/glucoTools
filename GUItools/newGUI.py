from guiGraph import graphData
from guiGraph import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import PySimpleGUI as sg
matplotlib.use('TkAgg')

#figQuery = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2021,3])
#figQuery = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=[2020,3])
#fig = figQuery.getFig()
#dateIn = figQuery.getDate()
#readingList = figQuery.getList()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def make_win1():
    layout = [
              [sg.Text('Please enter a date to graph in fields below')],
              [sg.Button('View Graph'), sg.Button('Load Meter Data'), sg.Button('Exit')],

              [sg.Text("Year"), sg.Input(key='-YEAR-', enable_events=True)],
              [sg.Text("Month"), sg.Input(key='-MONTH-', enable_events=True)],
              [sg.Text("Day"), sg.Input(key='-DAY-', enable_events=True)]]              
  #  sg.theme('Dark Teal 7')
    return sg.Window('glucoTools', layout, location=(800,600), finalize=True)


def make_win2():
#    layout = [[sg.Text('The second window')],
#              [sg.Input(key='-IN-', enable_events=True)],
#              [sg.Text(size=(25,1), k='-OUTPUT-')],
#              [sg.Button('Erase'), sg.Button('Popup'), sg.Button('Exit')]]
#    return sg.Window('Second Window', layout, finalize=True)
    layout = [
          [sg.Text(dateIn)],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Table(readingList, headings=["Date     | Time "," mg/dl  "], justification='left')],
          [sg.Button('Ok')]]
    return sg.Window('glucoTools-GUI', layout, finalize=True, resizable=True, 
            element_justification='center', font='Monospace 10')

#fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

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

window1, window2 = make_win1(), None        # start off with 1 window open

#fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
sg.theme('Dark Teal 7')

while True:             # Event Loop
    
    window, event, values = sg.read_all_windows()
    sg.theme('Dark Teal 7')
    if event == sg.WIN_CLOSED or event == 'Exit' or event == 'Ok':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            #sg.theme('Dark Teal 7')
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Popup':
        sg.popup('This is a BLOCKING popup','all windows remain inactive while popup active')
    elif event == 'View Graph' and not window2:
        dateFilter = localFilter()
        figQuery = graphData(fileIn = "patreading.txt", fileGraph="clitest1", dateFilter=dateFilter)
        fig = figQuery.getFig()
        dateIn = figQuery.getDate()
        readingList = figQuery.getList()
        window2 = make_win2()
        fig_canvas_agg = draw_figure(window2['-CANVAS-'].TKCanvas, fig)
    
window.close()

