# Crop Recommendation and Price Prediction Platform

## About
This project is a cloud-based web application to assist farmers in Karnataka. It provides:
1. **Crop Price Prediction:** Predict future market prices of selected crops.
2. **Crop Recommendation:** Suggest the best crops to grow based on input parameters.

## Features
- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Flask (Python)
- **Machine Learning:** scikit-learn
- **Deployment:** Render Cloud Platform

## Deployment on Render
### Steps:
1. Fork this repository to your account.
2. Ensure `requirements.txt` and `Procfile` are present.
3. Go to [Render](https://render.com/) and create a new Web Service.
4. Connect the repo and set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click "Deploy."

Your app will automatically start and be accessible via the Render-provided URL.