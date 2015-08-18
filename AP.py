#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Aug 17, 2015 10:10:51 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import AP_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('AP_PPT')
    geom = "601x447+259+271"
    root.geometry(geom)
    AP_support.set_Tk_var()
    w = AP_PPT (root)
    AP_support.init(root, w)
    root.after(10,  lambda: AP_support.EventLoop())
    root.mainloop()

w = None
def create_AP_PPT(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('AP_PPT')
    geom = "601x447+259+271"
    w.geometry(geom)
    AP_support.set_Tk_var()
    w_win = AP_PPT (w)
    AP_support.init(w, w_win, param)
    return w_win

def destroy_AP_PPT():
    global w
    w.destroy()
    w = None


class AP_PPT:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(highlightcolor="black")


        self.Text1 = Text(master)
        self.S = Scrollbar(self.Text1)
        self.S.pack(side=RIGHT, fill=Y)
        self.Text1.place(relx=0.02, rely=0.76, relheight=0.23, relwidth=0.97)
        self.Text1.configure(background="#c0c0c0")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(relief=RIDGE)
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=584)
        self.Text1.configure(wrap=WORD)
        self.S.configure(command=self.Text1.yview)
        self.Text1.configure(yscrollcommand=self.S.set)

        self.Label1 = Label(master)
        self.Label1.place(relx=0.02, rely=0.72, height=21, width=52)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Console:''')

        self.Canvas1 = Canvas(master)
        self.Canvas1.place(relx=0.02, rely=0.02, relheight=0.63, relwidth=0.64)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(width=386)

        self.StartTest = Button(master)
        self.StartTest.place(relx=0.68, rely=0.03, height=134, width=177)
        self.StartTest.configure(activebackground="#d9d9d9")
        self.StartTest.configure(pady="0")
        self.StartTest.configure(command=AP_support.StartTest)
        self.StartTest.configure(text='''Start Test''')

        self.StopTest = Button(master)
        self.StopTest.place(relx=0.68, rely=0.34, height=134, width=177)
        self.StopTest.configure(activebackground="#d9d9d9")
        self.StopTest.configure(pady="0")
        self.StopTest.configure(state=ACTIVE)
        self.StopTest.configure(command=AP_support.StopTest)
        self.StopTest.configure(text='''Stop Test''')

        self.PrintOption = Checkbutton(master)
        self.PrintOption.place(relx=0.77, rely=0.67, relheight=0.06
                , relwidth=0.22)
        self.PrintOption.configure(activebackground="#d9d9d9")
        self.PrintOption.configure(justify=LEFT)
        self.PrintOption.configure(text='''Print Test Receipt''')
        self.PrintOption.configure(variable=AP_support.che49)

        self.TProgressbar1 = ttk.Progressbar(master)
        self.TProgressbar1.place(relx=0.12, rely=0.67, relwidth=0.65
                , relheight=0.0, height=22)

        self.Label5 = Label(master)
        self.Label5.place(relx=0.02, rely=0.66, height=21, width=54)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Progress:''')

    @staticmethod
    def popup1(event):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {DejaVu Sans} -size 4 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(font=font12)
        Popupmenu1.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



