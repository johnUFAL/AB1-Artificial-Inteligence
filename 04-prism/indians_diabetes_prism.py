import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


# Carregamento de dados

cols = [
    'Gravidez',
    'Glicose',
    'Pressao',
    'Pele',
    'Insulina',
    'IMC',
    'DiabetesPedigree',
    'Idade',
    'Outcome'
]
df = pd.read_csv("../data/diabetes_prism.csv")

df.columns = cols

# Discretização

for col in df.columns[:-1]:
    df[col] = pd.qcut(
        df[col],
        q=4,
        duplicates='drop'
    )


# Divisão entre treino e test

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

train = pd.concat([X_train, y_train], axis=1)


# Implementação do Prism

def prism(data, target_col, class_val):

    rules = []
    remaining = data.copy()

    while (remaining[target_col] == class_val).sum() > 0:

        data_sub = remaining.copy()
        rule = []

        used_columns = set()

        while True:

            best_prec = -1
            best_pair = None

            for col in data_sub.columns:

                if col == target_col or col in used_columns:
                    continue

                for val in data_sub[col].dropna().unique():

                    mask = data_sub[col] == val

                    subset = data_sub[mask]

                    if len(subset) == 0:
                        continue

                    p = (subset[target_col] == class_val).sum()
                    n = (subset[target_col] != class_val).sum()

                    if p == 0:
                        continue

                    prec = p / (p + n)

                    if prec > best_prec:
                        best_prec = prec
                        best_pair = (col, val)

            if best_pair is None:
                break

            rule.append(best_pair)

            col, val = best_pair

            data_sub = data_sub[data_sub[col] == val]

            used_columns.add(col)

            if (data_sub[target_col] == class_val).all():
                break

        if not rule:
            break

        rules.append((rule, class_val))

        rule_mask = pd.Series(True, index=remaining.index)

        for col, val in rule:
            rule_mask &= remaining[col] == val

        positive_mask = rule_mask & (
            remaining[target_col] == class_val
        )

        remaining = remaining[~positive_mask]

    return rules


# Treinamento

rules = prism(train, 'Outcome', 1)


# Visão das regras

print("\nREGRAS GERADAS:\n")

for rule, cls in rules:

    conditions = " E ".join(
        f"{col}={val}"
        for col, val in rule
    )

    print(f"SE {conditions} ENTÃO Outcome={cls}")


# Momento de predição

def predict_prism(row, rules):

    for rule, cls in rules:

        if all(row[col] == val for col, val in rule):
            return cls

    return 0


y_pred = X_test.apply(
    lambda row: predict_prism(row, rules),
    axis=1
)


# Métricas

print("\nMÉTRICAS:\n")

print("Acurácia:", accuracy_score(y_test, y_pred))
print("Precisão:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1:", f1_score(y_test, y_pred, zero_division=0))
