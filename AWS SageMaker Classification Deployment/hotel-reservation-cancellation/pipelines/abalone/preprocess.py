# Importing the libraries nescessary
import argparse
import logging
import pathlib

import boto3
import numpy as np
import pandas as pd
import pickle
import os
import os
os.system('pip install sagemaker')

import sagemaker
import sagemaker.session
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

boto3.Session().region_name

if __name__ == "__main__":
    logger.debug("Starting preprocessing.")
    
# Change the bucket name    
    bucket = "sagemaker-us-east-1-160277102220"
    my_region = boto3.session.Session().region_name
    
    
    base_dir = "/opt/ml/processing"
    logger.debug("Reading data.")
    
# Check the key value
    s3_client = boto3.client("s3")
    df = pd.read_csv(s3_client.get_object(Bucket=bucket, Key='hotel_data_new.csv').get("Body"))
    

    #df = df.drop(["CustomerID"], axis=1)

    
    X, y = df.drop(['booking_status'], axis=1), df['booking_status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.4)
    
    obj_cols = X_train.select_dtypes(include=["object"]).columns
    num_cols = X_train.select_dtypes(exclude=["object"]).columns
    
    one_hot = OneHotEncoder()
    s_scaler = StandardScaler()
    
    one_hot = one_hot.fit(X_train[obj_cols])
    s_scaler = s_scaler.fit(X_train[num_cols])
    # Convert categorical variables into dummy/indicator variables.
    a = one_hot.transform(X_train[obj_cols]).toarray()
    b = s_scaler.transform(X_train[num_cols])
    X_train = np.c_[a, b]
    X_val = np.c_[one_hot.transform(X_val[obj_cols]).toarray(), s_scaler.transform(X_val[num_cols])]
    X_test = np.c_[one_hot.transform(X_test[obj_cols]).toarray(), s_scaler.transform(X_test[num_cols])]
    
    lb = LabelBinarizer().fit(y_train)
    y_train = lb.transform(y_train)
    y_val = lb.transform(y_val)
    y_test = lb.transform(y_test)
    # Store Transformations
    trans = {
        'One_Hot': one_hot,
        'scaler': s_scaler,
        'label': lb,
        'obj_cols': list(obj_cols),
        'num_cols': list(num_cols)
    }

    # Split the data
    pd.DataFrame(np.c_[y_train, X_train]).to_csv(f"{base_dir}/train/train.csv", header=False, index=False)
    pd.DataFrame(np.c_[y_val, X_val]).to_csv(f"{base_dir}/validation/validation.csv", header=False, index=False)
    pd.DataFrame(np.c_[y_test, X_test]).to_csv(f"{base_dir}/test/test.csv", header=False, index=False)
