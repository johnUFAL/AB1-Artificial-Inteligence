import pandas as pd
from chefboost import Chefboost as chef

df = pd.read_csv("../data/credito_ampliado.csv")

df = df.drop(columns=["Ex"])
df = df.rename(columns={"Risco": "Decision"})

for col in df.columns:
    df[col] = df[col].astype(object)

for algo in ["ID3", "C4.5", "CART"]:
    config = {
        "algorithm": algo,
        "enableParallelism": False
    }

    print(f"\n==== {algo} ====")

    model = chef.fit(df.copy(), config=config)
