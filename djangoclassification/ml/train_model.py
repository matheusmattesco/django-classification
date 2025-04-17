import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import sqlite3

df = pd.read_csv("./ml/Lung Cancer Dataset.csv")

# Connect to SQLite database
conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()


# Insert data into the LungCancer table
df.to_sql('LungCancer', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

df['GENDER'] = df['GENDER'].map({'M': 1, 'F': 0})
X = df.drop('PULMONARY_DISEASE', axis=1)
y = df['PULMONARY_DISEASE'].map({'YES': 1, 'NO': 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print(f"Model accuracy: {model.score(X_test, y_test)}")
# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)