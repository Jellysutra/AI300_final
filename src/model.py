import joblib
import pandas as pd

class Model:
    def __init__(self):
        self.model = joblib.load('model/xgboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)
    
# feature = {
#     'gender' : 0,
#     'age' : 38,
#     'senior_citizen' : 0,
#     'married' : 0,
#     'num_dependents' : 1,
#     'num_referrals' : 1,
#     'avg_gb_download_monthly' : 12,
#     'total_monthly_fee' : 50.2,
#     'total_charges_quarter' : 300.2
# }

# model_inputs = pd.DataFrame([feature])

# print(model_inputs)
# print(Model().predict(model_inputs))