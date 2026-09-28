import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    classification_report
)


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
df = pd.read_csv("../data/diabetes_kaggle.csv")
df.columns = cols

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.03, random_state=42, stratify=y
)

clf = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(export_text(clf, feature_names=list(X.columns)))
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Precisão:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-Score:", f1_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
