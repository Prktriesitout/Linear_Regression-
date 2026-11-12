from sklearn.model_selection import train_test_split 
import pandas as pd 
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 



model = LinearRegression()
print("\n--- Model Initialized ---")
print(model)

california = fetch_california_housing()
california_df = pd.DataFrame(california.data, columns=california.feature_names)
california_df['MedHouseVal'] = california.target

X = california_df.drop('MedHouseVal', axis=1)
y = california_df["MedHouseVal"]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model.fit(X_train, y_train)
print("\n--- Model Trained ---")
print("Intercept:", model.intercept_)

print("\n--- Data Split ---")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

predictions = model.predict(X_test)
print("\n--- Predictions ---")
print(predictions[:5])

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5, color='blue', edgecolors='black')

plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
'r--', linewidth=2, label='Perfect Prediction')

plt.xlabel('Actual House Prices ($100,000)')
plt.ylabel('Predicted House Prices ($100,000)')
plt.title('Linear Regression: Actual vs Predicted House Prices')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('housing_predictions.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n--- Visualizion Complete ---")
print("Plot saved to housing_predictions.png")