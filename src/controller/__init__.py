from flask import request, jsonify, Response, abort, make_response, redirect, url_for, send_from_directory, send_file, current_app
from flask_api import status
import os
import datetime
import json
from ..helper.response import response_success, response_error

class Controller(object):
  def __init__(self):
    self.request = request
    self.os = os
    self.datetime = datetime
    self.json = json
    self.jsonify = jsonify
    self.Response = Response
    self.abort = abort
    self.status = status
    self.make_response = make_response
    self.redirect = redirect
    self.url_for = url_for
    self.send_from_directory = send_from_directory
    self.send_file = send_file
    self.current_app = current_app
    self.response_success = response_success
    self.response_error = response_error
  
  
  