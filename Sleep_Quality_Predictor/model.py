import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Load CSV
df = pd.read_csv("sleep_data.csv")  # <-- your file name

print("Columns in dataset:")
print(df.columns)

# 2️⃣ Handle missing values
df['CaffeineConsumption'] = df['CaffeineConsumption'].fillna(0)

# 3️⃣ Create Sleep Quality Label
def sleep_quality(eff):
    if eff >= 0.85:
        return "Good"
    elif eff >= 0.65:
        return "Average"
    else:
        return "Poor"

df['SleepQuality'] = df['SleepEfficiency'].apply(sleep_quality)

# 4️⃣ Encode Gender
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male/Female → 0/1

# 5️⃣ Select Features (MATCHING YOUR CSV)
X = df[
    [
        'SleepDuration',
        'Awakenings',
        'CaffeineConsumption',
        'ExerciseFrequency',
        'Age',
        'Gender'
    ]
]

y = df['SleepQuality']

# 6️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7️⃣ Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 8️⃣ Evaluate
y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 9️⃣ Test with new input
sample = [[7.5, 2, 50, 3, 25, 1]]  
# SleepDuration, Awakenings, Caffeine, ExerciseFreq, Age, Gender(1=Male)

prediction = model.predict(sample)
print("\nPredicted Sleep Quality:", prediction[0])
