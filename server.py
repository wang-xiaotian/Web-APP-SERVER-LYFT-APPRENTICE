# Web Application - Xiaotian Wang - 07.25.2020
# listening on localhost:5000

from flask import Flask
from flask import render_template as rt
from flask import jsonify
from flask import request
import json as jn
import math

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Xiaotian Wang Web Applicaiton!'

# response to POST request
# accept one string argument with key 'string_to_cut'
#   parse string and only retain every third letter from input argument
# return string with key 'return_string'
@app.route('/test', methods=['POST'])
def lyft_test():
    return_string = "Unexpected Error: \n (Windows Users): Please execute command line \n curl -X POST HTTP://127.0.0.1:5000/test --header \"Content-Type: application/json\" --data {\\\"string_to_cut\\\":\\\"STRING\\\"}"
    try:
        data = request.get_json()
        # verify input argument 'string_to_cut'
        # ONLY execute cut_string_Alphanumeric
        # WHEN key = 'string_to_cut'
        string_to_cut = None
        if 'string_to_cut' in data:
            string_to_cut = data['string_to_cut']
            return_string = cut_string_Alphanumeric(string_to_cut)
        else:
            return_string = "Oops! KEY 'string_to_cut' DOES NOT EXIST IN YOUR ARGUMENT! PLEASE TYPE AGAIN."
    except:
        print(return_string)

    return return_string

# function that extract every third letter from input string
# e.g. cut_string_everyThirdLetter("abcedfg") returns "cf"
# special cases:
#   1. empty string
#   2. length of string may cause overflow, veryfy before access to string[index]
#   3. input string can only retain alphabatical letters
#   4. what if input string has backslash -- WORKING ON IT
#   5. isspace() = True -- WORKING ON IT
def cut_string_Alphanumeric(input_string):
    return_string = ""
    index = 0
    count = 1
    while (index < len(input_string)):
        if input_string[index].isalnum():
            if (count%3 == 0):
                return_string += input_string[index]
            count+=1
        index+=1

    return jn.dumps({'return_string':return_string}, indent = 4)

# function that extract every third letter from input string
# e.g. cut_string_everyThirdLetter("abcedfg") returns "cf"
# special cases:
#   1. empty string
#   2. length of string may cause overflow, veryfy before access to string[index]
#   3. input string can contains any letters but not \
def cut_string(input_string):
    return_string = ""
    num_letters = math.floor(len(input_string)/3)
    for n in range(num_letters):
        index = (n+1)*3
        if (index <= len(input_string)):
            return_string += input_string[index-1]

    return jn.dumps({'return_string':return_string}, indent = 4)

# run app in debug mode if using python server.py
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=1, port=5000)
