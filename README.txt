MONGODB CLOUD NOTES APP

SETUP:
1. Create MongoDB Atlas free cluster (M0)
2. Create DB user
3. Allow network access: 0.0.0.0/0
4. Copy connection string
5. Replace USERNAME & PASSWORD in app.py

RUN:
pip install -r requirements.txt
python app.py

OPEN:
http://127.0.0.1:5000
