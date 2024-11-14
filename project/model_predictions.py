# model_predictions.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

def create_target(data):
    # Create a binary target where 1 = next hour’s close price is higher, 0 = lower
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
    data.dropna(inplace=True)  # Drop rows with NaN values from shifting
    return data

def train_model(data):
    # Create target variable
    data = create_target(data)

    # Define features and target
    features = ['SMA_20', 'RSI', 'MACD']
    X = data[features]
    y = data['Target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions and evaluate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Add predictions to the original data for use in backtesting
    data['Prediction'] = model.predict(X)

    return data, model
