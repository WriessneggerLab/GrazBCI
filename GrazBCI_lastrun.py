#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 03, 2022, at 18:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet

# Setup the LSL stream
info = StreamInfo(name='PsychoPy', type='Markers', channel_count=1,
                  channel_format='int32', source_id='PsychopyMarkersID321654')
# Initialize the LSL stream.
outlet = StreamOutlet(info)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'para'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Alberto\\code\\GrazBCI\\GrazBCI_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "intro"
introClock = core.Clock()
text_intro = visual.TextStim(win=win, name='text_intro',
    text='Wellcome!',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
text_cross = visual.TextStim(win=win, name='text_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=4.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pre"
preClock = core.Clock()
text_pre_condition = visual.TextStim(win=win, name='text_pre_condition',
    text='',
    font='Open Sans',
    pos=(0, 4), height=4.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_pre_fix = visual.TextStim(win=win, name='text_pre_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=4.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_condition = visual.TextStim(win=win, name='text_condition',
    text='',
    font='Open Sans',
    pos=(0, 0), height=4.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "nothing"
nothingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='End!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
introComponents = [text_intro]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_intro* updates
    if text_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_intro.frameNStart = frameN  # exact frame index
        text_intro.tStart = t  # local t and not account for scr refresh
        text_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_intro, 'tStartRefresh')  # time at next scr refresh
        text_intro.setAutoDraw(True)
    if text_intro.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_intro.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_intro.tStop = t  # not accounting for scr refresh
            text_intro.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_intro, 'tStopRefresh')  # time at next scr refresh
            text_intro.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_intro.started', text_intro.tStartRefresh)
thisExp.addData('text_intro.stopped', text_intro.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=60.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('lists/llist.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [text_cross]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_cross* updates
        if text_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_cross.frameNStart = frameN  # exact frame index
            text_cross.tStart = t  # local t and not account for scr refresh
            text_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_cross, 'tStartRefresh')  # time at next scr refresh
            text_cross.setAutoDraw(True)
        if text_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_cross.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_cross.tStop = t  # not accounting for scr refresh
                text_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_cross, 'tStopRefresh')  # time at next scr refresh
                text_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_cross.started', text_cross.tStartRefresh)
    trials.addData('text_cross.stopped', text_cross.tStopRefresh)
    
    # ------Prepare to start Routine "pre"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    text_pre_condition.setText(condition)
    # keep track of which components have finished
    preComponents = [text_pre_condition, text_pre_fix]
    for thisComponent in preComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pre"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = preClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=preClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_pre_condition* updates
        if text_pre_condition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_pre_condition.frameNStart = frameN  # exact frame index
            text_pre_condition.tStart = t  # local t and not account for scr refresh
            text_pre_condition.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_pre_condition, 'tStartRefresh')  # time at next scr refresh
            text_pre_condition.setAutoDraw(True)
        if text_pre_condition.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_pre_condition.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_pre_condition.tStop = t  # not accounting for scr refresh
                text_pre_condition.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_pre_condition, 'tStopRefresh')  # time at next scr refresh
                text_pre_condition.setAutoDraw(False)
        
        # *text_pre_fix* updates
        if text_pre_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_pre_fix.frameNStart = frameN  # exact frame index
            text_pre_fix.tStart = t  # local t and not account for scr refresh
            text_pre_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_pre_fix, 'tStartRefresh')  # time at next scr refresh
            text_pre_fix.setAutoDraw(True)
        if text_pre_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_pre_fix.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_pre_fix.tStop = t  # not accounting for scr refresh
                text_pre_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_pre_fix, 'tStopRefresh')  # time at next scr refresh
                text_pre_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in preComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre"-------
    for thisComponent in preComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_pre_condition.started', text_pre_condition.tStartRefresh)
    trials.addData('text_pre_condition.stopped', text_pre_condition.tStopRefresh)
    trials.addData('text_pre_fix.started', text_pre_fix.tStartRefresh)
    trials.addData('text_pre_fix.stopped', text_pre_fix.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_condition.setText(condition)
    if condition == "feet":
         outlet.push_sample([1])
    elif condition == "hand":
         outlet.push_sample([2])
        
    # keep track of which components have finished
    trialComponents = [text_condition]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_condition* updates
        if text_condition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_condition.frameNStart = frameN  # exact frame index
            text_condition.tStart = t  # local t and not account for scr refresh
            text_condition.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_condition, 'tStartRefresh')  # time at next scr refresh
            text_condition.setAutoDraw(True)
        if text_condition.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_condition.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_condition.tStop = t  # not accounting for scr refresh
                text_condition.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_condition, 'tStopRefresh')  # time at next scr refresh
                text_condition.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_condition.started', text_condition.tStartRefresh)
    trials.addData('text_condition.stopped', text_condition.tStopRefresh)
    
    # ------Prepare to start Routine "nothing"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    nothingComponents = [text]
    for thisComponent in nothingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nothingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nothing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = nothingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nothingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nothingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nothing"-------
    for thisComponent in nothingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 60.0 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
