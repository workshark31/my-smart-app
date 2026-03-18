def analyze_all(all_data):
    result = {}

    for item in all_data:
        pid = item["patient_id"]
        bundle = item["data"]

        encounters = bundle.get("entry", [])
        total = len(encounters)

        result[pid] = {
            "total_encounters": total
        }

    return result
