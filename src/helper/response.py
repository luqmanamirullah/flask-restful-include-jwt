from flask import jsonify
def response(data, status_code):
    return jsonify(data), status_code

def response_error(message, status_code):
  return response({"success": False, "message": message}, status_code)

def response_success(message, data, status_code):
  return response({"success": True, "message": message, "data": data}, status_code)