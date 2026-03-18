from flask import Flask, jsonify
from fhir_service import get_multiple_encounters
from analysis import analyze_all

app = Flask(__name__)

@app.route("/batch-analysis")
def batch_analysis():
    patient_ids = ["example", "example2", "example3"]  # 模擬多病人

    all_data = get_multiple_encounters(patient_ids)
    result = analyze_all(all_data)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
