import os

token = os.getenv("GITHUB_TOKEN")

if token:
    print("✅ GITHUB_TOKEN is set!")
else:
    print("❌ GITHUB_TOKEN is NOT set!")
