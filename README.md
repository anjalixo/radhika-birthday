# Radhika Birthday Website

A simple pink birthday page built with Python and Streamlit, using six personal photos.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the website:

   ```bash
   streamlit run app.py
   ```

## Deploy on Render

1. Upload this project folder to a GitHub repository.
2. In Render, create **New + → Web Service** and connect the repository.
3. Set:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT`
4. Click **Create Web Service**.

Keep the `photos` folder in the GitHub repository so the images appear on the deployed page.
