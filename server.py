from flask import Flask, request, jsonify, render_template
import csv, time, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    data['timestamp'] = timestamp

    file_exists = os.path.exists("imu_data.csv")
    with open("imu_data.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    return jsonify({"status": "ok", "received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
