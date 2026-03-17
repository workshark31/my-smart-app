import jwt
import time
import requests

# =============================
# Step 4 - 建立 JWT
# =============================

client_id = "my-backend-service"
token_url = "https://r4.smarthealthit.org/auth/token"
fhir_base = "https://r4.smarthealthit.org"

# 讀取 private key
with open("private_key.pem", "r") as f:
    private_key = f.read()

now = int(time.time())

payload = {
    "iss": client_id,
    "sub": client_id,
    "aud": token_url,
    "exp": now + 300,
    "iat": now
}

jwt_token = jwt.encode(
    payload,
    private_key,
    algorithm="RS384"
)

print("✅ JWT 建立成功")

# =============================
# Step 5 - 換 Access Token
# =============================

response = requests.post(
    token_url,
    data={
        "grant_type": "client_credentials",
        "client_assertion_type":
        "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": jwt_token,
        "scope": "system/*.read"
    }
)

print("Token Status:", response.status_code)
print("Token Response:", response.text)

if response.status_code != 200:
    print("❌ 取得 Token 失敗")
    exit()

access_token = response.json().get("access_token")
print("✅ Access Token 取得成功")

# =============================
# Step 6 - 呼叫 FHIR API
# =============================

headers = {
    "Authorization": f"Bearer {access_token}"
}

res = requests.get(f"{fhir_base}/Patient", headers=headers)

print("FHIR Status:", res.status_code)
print("FHIR Response:")
print(res.json())