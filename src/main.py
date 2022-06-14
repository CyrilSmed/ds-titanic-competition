import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

import data_analysis
import data_processing
import models

def predict_and_save(model, file_name, is_neural_net=False) -> None:
    test_df = pd.read_csv(r"../datasets/test.csv", sep=",", header="infer", names=None, encoding="utf-8")
    ids, test_df = data_processing.normalize_for_prediction(test_df)

    pred_df = pd.DataFrame(ids)
    y_pred = model.predict(X_test)

    if is_neural_net:
        y_pred = (y_pred > 0.5).astype("int32")
        y_pred = list(map(lambda x: x[0], y_pred))

    pred_df["Survived"] = pd.Series(y_pred)
    pred_df.to_csv(r"../datasets/{0}.csv".format(file_name), index=False)

def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

if __name__ == "__main__":
    df = pd.read_csv(r"../datasets/train.csv", sep=",", header="infer", names=None, encoding="utf-8")
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    df = data_processing.clean_training_dataset(df)

    models.model_selection(df)

    # predict_and_save(neural_network, file_name="neural_net_submission", is_neural_net=True)
