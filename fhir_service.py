import requests

FHIR_BASE = "https://r4.smarthealthit.org"

def get_encounters(patient_id):
    url = f"{FHIR_BASE}/Encounter?subject={patient_id}"
    res = requests.get(url)
    return res.json()

def get_multiple_encounters(patient_ids):
    all_data = []

    for pid in patient_ids:
        data = get_encounters(pid)
        all_data.append({
            "patient_id": pid,
            "data": data
        })

    return all_data
