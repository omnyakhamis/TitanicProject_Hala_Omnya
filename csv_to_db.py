import pandas as pd
from sqlalchemy import create_engine
import os

train_file = os.path.dirname(os.path.realpath(__file__)) + '/API/model/dataset/train.csv'
train = pd.read_csv(train_file)
url = "postgres://xeumkbpo:oVQND5ep22edECWjXRx-zUEGsV09C3KT@raja.db.elephantsql.com:5432/xeumkbpo"

engine = create_engine(url)
train.to_sql("passengers", con=engine)
