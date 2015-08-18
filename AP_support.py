#! /usr/bin/env python
#
# Support module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Aug 17, 2015 10:09:43 PM


import sys, time

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

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global che49
    che49 = StringVar()


def init(top, gui, arg=None):
    global w, top_level, root, currentState, waitCounter
    global STATE_WAITING
    global STATE_TESTING_POWER
    global STATE_WAIT_FOR_POWER_UP
    global STATE_START_PROGRAMMING
    global STATE_WAIT_FOR_PROGRAMMING
    global STATE_TESTING_FAILED
    global STATE_TESTING_SUCCESS
    global STATE_TESTING_COMPLETE
    global STATE_TESTING_CANCELLED
    global STATE_PRINT_AND_OR_ADVISE
    global INIT

    STATE_WAITING = 0
    STATE_TESTING_POWER = 1
    STATE_WAIT_FOR_POWER_UP = 2
    STATE_START_PROGRAMMING = 3
    STATE_WAIT_FOR_PROGRAMMING = 4
    STATE_TESTING_FAILED = 5
    STATE_TESTING_SUCCESS = 6
    STATE_TESTING_COMPLETE = 7
    STATE_TESTING_CANCELLED = 8
    STATE_PRINT_AND_OR_ADVISE = 9
    INIT = 10

    currentState = INIT
    w = gui
    top_level = top
    root = top
    waitCounter = 0

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def EventLoop():
    global currentState, waitCounter

    state = currentState #Latching currentState
    if state == INIT:
        #Do all the init stuff
        w.Canvas1.delete(ALL)
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="STANDING BY")
        w.Canvas1.config(background="#ecf0f1")
        currentState = STATE_WAITING

    if state == STATE_WAITING:
        pass
 
    elif state == STATE_TESTING_POWER:
        #Start any ADC stuff that's needed and connect power to the board.
        #This is going to block and check current on start-up with an external shunt
        #just to be safe and not blow things up.  (thumbs up)
        w.Canvas1.delete(ALL)
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="POWER TEST")
        w.Canvas1.config(background="#1abc9c")
        currentState = STATE_WAIT_FOR_POWER_UP

    elif state == STATE_WAIT_FOR_POWER_UP:
        waitCounter += 1
        # Each count is equivalent to ~10 mS
        if waitCounter >=500:
            waitCounter = 0
            #Process ADC Data and change states accordingly
            #Assume for now that it all passed properly.
            currentState = STATE_START_PROGRAMMING

    elif state == STATE_START_PROGRAMMING:
        #Start programming with the pickit.
        currentState = STATE_WAIT_FOR_PROGRAMMING
        w.Canvas1.delete(ALL)	
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="IC TEST")

    elif state == STATE_WAIT_FOR_PROGRAMMING:
        waitCounter += 1
        #Each count is equivalent to ~10 mS
        if waitCounter >= 500:
            waitCounter = 0
            #Process the test data from the pic and change states accordingly.
            #Here we assume that everything turned out okay and go to the testing complete phase
            currentState = STATE_TESTING_SUCCESS

    elif state == STATE_TESTING_FAILED:
        #Turn off power.
        #Update the canvas with information about the test status.
        #Anything else that needs to be handled before going to the test complete phase.
        w.Canvas1.delete(ALL)	
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="PASS")
        w.Canvas1.config(background="#e74c3c")
        w.Text1.insert(END, "Test Failed, click start test to proceed.'")
        w.Text1.see(END)
        currentState = STATE_TESTING_COMPLETE

    elif state == STATE_TESTING_SUCCESS:
        #Turn off the power
        #Update the canvas with information about the test status.
        #Anything else that needs to be handled before going to the test complete phase.
        w.Canvas1.delete(ALL)	
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="PASS")
        w.Canvas1.config(background="#2ecc71")
        currentState = STATE_TESTING_COMPLETE

    elif state == STATE_TESTING_COMPLETE:
        #update the canvas with pertinent information
        #Parse any flags that may hae beem set 
        #Any other code cleanup, this state may not be needed, so we can get rid of it probably.
        currentState = STATE_PRINT_AND_OR_ADVISE

    elif state == STATE_PRINT_AND_OR_ADVISE:
        #Advise to the user what to check in the system, if anything
        #print report here
	# Clean up any flags for a new test.
        pass

    elif state == STATE_TESTING_CANCELLED:
        #Tunr off power
        #Clean up anything for a new test.
        w.Canvas1.delete(ALL)	
        w.Canvas1.create_text(185, 140, anchor=CENTER, font=("Purisa", 40), text="CANCELLED")
        w.Canvas1.config(background="#f1c40f")

    root.after(10, lambda: EventLoop())

def StartTest():
    global startTime, currentState
    startTime = time.time()
    currentState = STATE_TESTING_POWER
    w.Text1.insert(END, 'Starting Test at ' + str(startTime) + '.\n')
    w.Text1.see(END)

def StopTest():
    global startTime, currentState
    endTime = time.time()
    currentState = STATE_TESTING_CANCELLED
    w.Text1.insert(END, 'Stopping Test!  Test took ' + str(endTime - startTime) + ' seconds.\n')
    w.Text1.see(END)

