import json
import pickle

import numpy as np
from flask import Flask, render_template, request, url_for, redirect, Response,jsonify,make_response

# from database import create_tabel
import requests
app = Flask(__name__)
# app = NoExtRef(app)
from encoding_input_data import enc_dict

# create_tabel()

np.random.seed(25)
'''['Age',
 'Ease and convenient',
 'Time saving',
 'More restaurant choices',
 'Easy Payment option',
 'More Offers and Discount',
 'Good Food quality',
 'Good Tracking system',
 'Unaffordable',
 'Maximum wait time']'''


# def jsonResponseFactory(data):
#     '''Return a callable in top of Response'''
#
#     def callable(response=None, *args, **kwargs):
#         '''Return a response with JSON data from factory context'''
#         return Response(json.dumps(data), 200, mimetype="application/json")
#
#     return callable


def encoding_data(enc_dict={}, dec_dict={}):
    list_enc = []
    convert_age = [20, 24, 22, 27, 23, 21, 28, 25, 32, 30, 31, 26, 18, 19, 33, 29]
    for i in dec_dict.keys():
        if (i == 'Age'):
            x = int(dec_dict[i])
            if x in convert_age:
                y = enc_dict[i][str(x)]
                list_enc.append(y)
            else:
                absolute_difference_function = lambda list_value: abs(list_value - x)
                closest_value = min(convert_age, key=absolute_difference_function)
                y = enc_dict[i][str(closest_value)]
                list_enc.append(y)

        else:
            y = enc_dict[i][dec_dict[i]]
            list_enc.append(y)

    return np.array(list_enc).reshape(1, -1)


def random():
    return np.random.randint(0, 235633)


def predction(pred_values):
    model = pickle.load(open('model.pkl', 'rb'))
    output = model.predict_proba(pred_values)
    print(output[0][1])
    return float(output[0][1])


@app.route('/', methods=['POST', 'GET'])
def form_submit():

    if request.method == 'POST':

        values = request.form.to_dict()

        pre_array = encoding_data(enc_dict, values)

        values['Output'] = round(predction(pre_array), 3)

        # from database import insert_values
        # x = insert_values(values.values())
        # y = random()
        # values['flag'] = f"{x},{y}"
        # k=values.copy()
        #
        #
        # values = json.dumps(values)
        # print("Hello",x+url_for("submission"))
        # ori="http://localhost:8078/submit_sucess"
        path=request.url_root+url_for("submission")

        r=requests.post(path, json=values)
        print("status",r.headers)



        return r.text
    else:
        return render_template('index.html')


@app.route('/submit_sucess', methods=['POST'])
def submission():
    # print(request)

    feedback=request.get_json()
    # print(feedback)
    # feedback=request.json()

    # print(feedback)
    # # feedback = feedback.replace("'", "\"")
    # feedback = json.loads(feedback)
    # flag = feedback['flag']
    # #
    # flag = flag.split(",")
    # results = list(map(float, flag))
    # del feedback['flag']
    #
    output = float(feedback['Output'])
    #
    del feedback['Output']
    # print(type(feedback))

    return render_template('submit_success.html', feedback=feedback, probability=round(output, 4))
    # return render_template('submit_success.html', feedback=feedback, probability=round(output, 4))
    # if (results[0] == 1):
    #     return render_template('submit_success.html', feedback=feedback, probability=round(output, 4))
    # else:
    #     # return render_template('unsuccessful.html')


@app.route('/about')
def about():
    return "<h2>hi im nikhil</h2>"

@app.route("/index_1")
def new_index():
    return  render_template("index.html")
# @app.route('/html_login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#
#         values = request.form.to_dict()
#         get_username = values['u']
#         get_password = values['p']
#
#         from database import get_admin_data
#         x = get_admin_data()
#         if x[0][0] == get_username and x[0][1] == get_password:
#             return redirect(url_for('fetch_data'))
#         else:
#             return render_template('invalid.html')
#     return render_template('html_login.html')
#

# @app.route("/admin/fetch_data")
# def fetch_data():
#     from database import get_data
#     field_names, data = get_data()
#     print(field_names, data)
#
#     return render_template('database_show.html', filed_names=field_names, data=data)


if __name__ == '__main__':
    app.run(debug=True)
