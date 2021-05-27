from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae
import lightgbm
import optuna.integration.lightgbm as lgb


def train(df):
    
    df_train, df_val = train_test_split(df, test_size=0.2)

    col = "取引価格（総額）_log"
    train_y = df_train[col]
    train_x = df_train.drop(col, axis=1)

    val_y = df_val[col]
    val_x = df_val.drop(col, axis=1)

    trains = lgb.Dataset(train_x, train_y)
    valids = lgb.Dataset(val_x, val_y)
    
    params = {
        "objective": "regression",
        "metrics": "mae", 
        "lambda_l1": 8.442195346804022,
        "lambda_l2": 5.708301125509865e-05,
        "num_leaves": 143,
        "feature_fraction": 0.484,
        "bagging_fraction": 1.0,
        "bagging_freq": 0,
        "min_child_samples": 50
    }

    model = lgb.train(params, trains, valid_sets=valids, num_boost_round=1000, early_stopping_rounds=100, verbose_eval=200)
    
    vals = model.predict(val_x)
    print("val_mae:", mae(vals, val_y))
    
    return model