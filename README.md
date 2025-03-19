# NYC Taxi Fare Prediction API

## Project Overview
This project builds an **end-to-end machine learning pipeline** for taxi fare prediction using the **NYC Taxi Dataset**.  
It includes **data preprocessing, model training (XGBoost & Random Forest), and an API for real-time predictions**.

## Dataset
The dataset contains features such as:
- `passenger_count`
- `trip_distance`
- `ratecodeid`
- `payment_type`
- `extra`, `tip_amount`, `tolls_amount`
- `congestion_surcharge`, `tip_percent`
- `store_and_fwd_flag_encoded`

The **goal** is to build a model that accurately **predicts `fare_amount`** based on these features.

---
# To check the model prediction
# Clone the Repository
```bash
git clone https://github.com/DhanushSriniv/NYC_Taxi_Fare_Prediction.git
cd NYC_Taxi_Fare_Prediction

# Install Dependancies
pip install -r requirements.txt

# Run the training script to generate the model
python train_model.py

# Run the app file 
python app.py

# On running api will be available at:
http://127.0.0.1:5000

# Testing the Api
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d "{\"passenger_count\":2, \"trip_distance\":5.3, \"ratecodeid\":1, \"payment_type\":1, \"extra\":0.5, \"tip_amount\":2.75, \"tolls_amount\":0.0, \"congestion_surcharge\":2.5, \"tip_percent\":15.0, \"store_and_fwd_flag_encoded\":0}"

