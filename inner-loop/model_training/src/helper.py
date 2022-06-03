import lightgbm as lgb
import time
from sklearn.metrics import log_loss, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split



# データ前処理 (データ型変更、特徴量と目的変数の作成、データ分割)
def preprocess_data(df, categorical_cols, float_cols):

    df[categorical_cols] = df[categorical_cols].astype('category')
    df[float_cols] = df[float_cols].astype('float')

    X = df.drop(["Survived", "PassengerId"], axis=1)
    y = df["Survived"]

    enc = LabelEncoder()
    y = enc.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, enc, categorical_cols


# モデル学習
def train_model(params, num_boost_round, X_train, X_test, y_train, y_test, categorical_cols):
    t1 = time.time()
    train_data = lgb.Dataset(X_train, label=y_train, categorical_feature=categorical_cols)
    test_data = lgb.Dataset(X_test, label=y_test, categorical_feature=categorical_cols)
    model = lgb.train(
        params,
        train_data,
        num_boost_round=num_boost_round,
        valid_sets=[test_data],
        valid_names=["test"],
    )
    t2 = time.time()

    return model, t2 - t1


# モデル評価
def evaluate_model(model, X_test, y_test):
    y_proba = model.predict(X_test)
    y_pred = y_proba.argmax(axis=1)
    loss = log_loss(y_test, y_proba)
    acc = accuracy_score(y_test, y_pred)

    return loss, acc