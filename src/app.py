from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)

        # # Modified code
        # age = int(form_input['age'])
        # sex = form_input['sex']
        # bmi = float(form_input['bmi'])
        # children = int(form_input['children'])
        # smoker = form_input['smoker']
        # #region = form_input['region']

        # model_inputs = [age, sex, bmi, children, smoker, region]
        # prediction = Model().predict(model_inputs)

        #return render_template('index.html', prediction=prediction) # Add parameter here
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)