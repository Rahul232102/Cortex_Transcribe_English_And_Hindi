from dotenv import load_dotenv
import os

load_dotenv()

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

if not SARVAM_API_KEY:
    print("❌ API key not found")
else:
    print("✅ API key loaded")