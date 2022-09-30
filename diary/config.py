import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일을 읽어서 환경변수에 넣어줌

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["DIARY_DATABASE_NAME"],
        "USER": os.environ["DIARY_DATABASE_USER"],
        "PASSWORD": os.environ["DIARY_DATABASE_PASSWORD"],
        "HOST": os.environ["DIARY_DATABASE_HOST"],
        "PORT": int(os.environ.get("DIARY_DATABASE_PORT", "3306")),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

SECRET_KEY = os.environ["DIARY_SECRET_KEY"]

API_KEY = os.environ["DIARY_API_KEY"]
