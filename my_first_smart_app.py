from fhirclient import client
from fhirclient.models.patient import Patient

# 設定連線到公開 Sandbox（無需登入）
settings = {
    'app_id': 'my_web_app',           # 你可以改成自己的 App 名稱
    'api_base': 'https://r4.smarthealthit.org'  # 官方測試伺服器
}

smart = client.FHIRClient(settings=settings)

# 讀取單一病人資料（Patient ID 可在 Sandbox 查）
patient = Patient.read('2cda5aad-e409-4070-9a15-e1c35c46ed5a', smart.server)

print("出生日期：", patient.birthDate.isostring)          # 輸出：1992-07-03
print("姓名：", smart.human_name(patient.name[0]))       # 輸出：Mr. Geoffrey Abbott