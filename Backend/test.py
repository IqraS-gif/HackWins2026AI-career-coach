import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Print current directory so we know where we are
print(f"📂 Current Working Directory: {os.getcwd()}")

# 2. Try to load .env
loaded = load_dotenv()
print(f"📄 .env file loaded? {'Yes' if loaded else 'No'}")

# 3. Get the Key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("\n❌ CRITICAL ERROR: Python cannot find 'GEMINI_API_KEY'.")
    print("---------------------------------------------------")
    print("CHECK THESE 3 THINGS:")
    print("1. Do you have a file named exactly '.env' in the 'Backend' folder?")
    print("2. Does it contain the line: GEMINI_API_KEY=AIzaSy...")
    print("3. Did you save the file?")
    exit()

print(f"\n🔑 Key Found: {api_key[:5]}... (length: {len(api_key)})")

# 4. Test the Key
genai.configure(api_key=api_key)
try:
    print("📡 Testing Connection to Google...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Are you working?")
    print(f"✅ SUCCESS! Response: {response.text}")
except Exception as e:
    print(f"❌ CONNECTION FAILED: {e}")