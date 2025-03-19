from flask import Flask, request, jsonify
import pickle
import pandas as pd

# ✅ Correctly Load the Trained Model
try:
    model_path = model_path = "C:\\Users\\Administrator\\OneDrive\\Desktop\\EAI6020\\Module 3\\xgb_model.pkl"
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)  # ✅ Ensure model loads correctly
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", e)
    model = None  # Set model to None if loading fails

# ✅ Initialize Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Taxi Fare Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Ensure Model is Loaded
        if model is None:
            return jsonify({"error": "Model is not loaded properly. Ensure 'best_model.pkl' exists."})

        # ✅ Get JSON Input
        data = request.get_json(force=True)  # ✅ Ensures JSON is correctly parsed

        # ✅ Convert JSON to DataFrame (Handles Both Single & Multiple Requests)
        if isinstance(data, dict):  # If single request, wrap it in a list
            input_df = pd.DataFrame([data])
        elif isinstance(data, list):
            input_df = pd.DataFrame(data)
        else:
            return jsonify({"error": "Invalid input format. Expecting JSON object or list."})

        # ✅ Ensure All Required Features Are Present
        expected_features = ['passenger_count', 'trip_distance', 'ratecodeid', 'payment_type',
                             'extra', 'tip_amount', 'tolls_amount', 'congestion_surcharge',
                             'tip_percent', 'store_and_fwd_flag_encoded']
        
        missing_cols = [col for col in expected_features if col not in input_df.columns]
        if missing_cols:
            return jsonify({"error": f"Missing required input features: {missing_cols}"})

        # ✅ Make Predictions
        prediction = model.predict(input_df)

        # ✅ Return Results as JSON
        return jsonify({"predicted_fare_amount": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
