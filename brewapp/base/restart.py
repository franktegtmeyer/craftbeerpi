from flask import Blueprint, render_template, jsonify,redirect, url_for, request
import json
from brewapp import app, socketio
from thread import start_new_thread
import logging
import time
from views import base

## Restart Endpoint
@app.route('/restart')
def restart():
    app.logger.info("--> RESTART TRIGGERED")
    ## Do in other thread
    start_new_thread(doRestart,())
    return base.send_static_file("restart.html")

## Execute Restart
def doRestart():
    time.sleep(5)
    from subprocess import call
    app.logger.info("--> RESTART EXECUTE")
    call(["/etc/init.d/craftbeerpiboot", "restart"])

## Shutdown Endpoint
@app.route('/halt')
def halt():
    app.logger.info("--> HALT TRIGGERED")
    ## Do in other thread
    start_new_thread(doHalt,())
    return base.send_static_file("halt.html")

## Execute Restart
def doHalt():
    time.sleep(5)
    from subprocess import call
    app.logger.info("--> HALT EXECUTE")
    call("halt")
