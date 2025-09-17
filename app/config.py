from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
ML_MODEL_PATH = os.getenv("ML_MODEL_PATH")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")
