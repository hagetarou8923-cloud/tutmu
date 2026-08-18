import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Discord
    TOKEN = os.getenv("MTUzOTEzNTAxMDQ1NDUwNzU2MA.GUnXKh.BJOQHZboEYVB5tqqLPMG-KWOBNZo1wlTnr59IA")
    PREFIX = os.getenv("BOT_PREFIX", "!")
    ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
    
    # Database (MongoDB Atlas推奨)
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DB_NAME", "tsumtsum_bot")
    
    # Automation
    ADB_HOST = os.getenv("ADB_HOST", "localhost")
    ADB_PORT = int(os.getenv("ADB_PORT", "5037"))
    DEVICE_ID = os.getenv("DEVICE_ID", "emulator-5554")
    
    # MOD APK設定
    MOD_PACKAGE = os.getenv("MOD_PACKAGE", "com.linecorp.LGTMTM")
    MOD_ACTIVITY = os.getenv("MOD_ACTIVITY", ".TsumTsumActivity")
    MOD_VERSION = os.getenv("MOD_VERSION", "1.0.0")
    
    # コイン倍率設定
    COIN_MULTIPLIER = int(os.getenv("COIN_MULTIPLIER", "100000000"))  # 1億倍
    
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    
    # 料金設定
    PRICES = {
        "1hour": 500,
        "3hours": 1200,
        "6hours": 2000,
        "12hours": 3500,
        "24hours": 6000
    }
    
    # 自動化設定
    AUTO_SETTINGS = {
        "rounds_per_hour": 60,      # 1時間に60ラウンド
        "coin_per_round": 1000000,  # 1ラウンド100万コイン（MOD）
        "exp_per_round": 1000,
        "delay_between_rounds": 3,   # ラウンド間3秒
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = ProductionConfig() if os.getenv("ENV") == "production" else DevelopmentConfig()