import time
import requests

for i in range(100):
    try:
        response = requests.post(
            "http://localhost:5000/human",
            json={"human_value": i},  # Send as JSON
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        print(f"Successfully sent data: {i}, Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {i}, Error: {e}")
    time.sleep(2)