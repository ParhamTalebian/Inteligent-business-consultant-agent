from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")  # مسیر دقیق فایل env خودت
print("TOGETHER_API_KEY =", os.getenv("TOGETHER_API_KEY"))
