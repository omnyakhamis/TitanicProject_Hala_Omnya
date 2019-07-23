from API.model.run_pipeline import read_train
from API.model.prediction import make_prediction

test_data = [{'Age': 50, 'Pclass': 1, 'Fare': 71.2833, 'Sex': 'female'}]
print(make_prediction(test_data))
