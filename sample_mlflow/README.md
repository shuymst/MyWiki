# mlflow
実験のパラメータやメトリクスの記録を簡単に行うことができる

```Python
mlflow.set_experiment("experiment_name")
with mlflow.start_run():                         # 1回のRunを記録
    mlflow.log_param("lr", 0.01)                 # パラメータ
    mlflow.log_metric("loss", 0.23)              # メトリクス
    mlflow.pytorch.log_model(model, "model")     # モデル保存
```

以下のコマンドをシェルで実行し, http://localhost:5000にアクセスすることでUIにアクセスできる
```bash
mlflow ui
```
