from flask import Flask, request, render_template
from model import Model
import pandas as pd

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)

        # inputs from user
        gender = int(form_input['gender'])
        age = int(form_input['age'])
        senior_citizen = int(form_input['senior_citizen'])
        married = int(form_input['married'])
        num_dependents = int(form_input['num_dependents'])
        num_referrals = int(form_input['num_referrals'])
        avg_gb_download_monthly = float(form_input['avg_gb_download_monthly'])
        total_monthly_fee = float(form_input['total_monthly_fee'])
        total_charges_quarter = float(form_input['total_charges_quarter'])

        # preparing inputs for model
        model_inputs = [[gender, age, senior_citizen, married, num_dependents, num_referrals, avg_gb_download_monthly,
                          total_monthly_fee, total_charges_quarter]]
        column = ['gender', 'age', 'senior_citizen', 'married', 'num_dependents', 'num_referrals', 'avg_gb_download_monthly',
                          'total_monthly_fee', 'total_charges_quarter']
        input = pd.DataFrame(model_inputs,columns=column)

        # make prediction
        prediction = Model().predict(input)
        print(prediction)
        return render_template('index.html', prediction=prediction) # Add parameter here
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)