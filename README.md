# 🚀 GCP VM Scheduler (Cloud Function)

This project allows you to **start or stop Compute Engine VM instances** across multiple availability zones using a **Google Cloud Function** triggered by an HTTP request.

---

## ✅ Features

- Control specific VM instances via simple HTTP GET request
- Supports multiple zones (e.g. `asia-south1-c`, `asia-south2-c`)
- Returns clear JSON response with results or errors
- Easily deployable using `gcloud` CLI

---

## 🧰 Prerequisites

- GCP Project (e.g. `jaatbreak-dev-env`)
- Cloud Functions & Compute Engine APIs enabled
- Permissions: Cloud Functions Developer, Compute Admin
- Installed:
  - [Google Cloud SDK](https://cloud.google.com/sdk)
  - Python 3.11+

---

## 📁 Files

- `main.py` — Cloud Function source code
- `requirements.txt` — Python dependencies

---

## 🚀 Deploying the Function

From the root project folder (with `main.py` and `requirements.txt`):

```bash
gcloud functions deploy manage-vms \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --region=asia-south1

🌐 Usage (HTTP Requests)
curl "https://REGION-PROJECT_ID.cloudfunctions.net/manage-vms?action=start"
curl "https://REGION-PROJECT_ID.cloudfunctions.net/manage-vms?action=stop"

📦 Example Response
json
Copy
Edit
{
  "action": "stop",
  "results": {
    "apache-server-production": "stop initiated in asia-south1-c",
    "gke-prod-cluster": "stop initiated in asia-south2-c"
  }
}
💡 Customization
To add more VM instances or update zones, modify the instances dictionary in main.py:

python
Copy
Edit
instances = {
  "apache-server-production": "asia-south1-c",
  "gke-prod-cluster": "asia-south2-c",
  "another-instance": "asia-south1-a"
}
🗓️ Optional Automation
You can set up a Cloud Scheduler job to hit this endpoint automatically at specific times (e.g., stop VMs every night).
