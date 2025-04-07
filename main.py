from googleapiclient import discovery
from google.auth import default
from flask import jsonify  # If you're using this in a Flask-based Cloud Function

def manage_vms(request):
    request_args = request.args
    action = request_args.get('action') if request_args else None

    if action not in ("start", "stop"):
        return jsonify({"error": "Invalid or missing 'action' parameter. Use 'start' or 'stop'."}), 400

    project = "jaatbreak-dev-env"
    zone = "asia-south1-c"
    instances = ["apache-server-production", "gke-prod-cluster"]

    credentials, _ = default()
    service = discovery.build('compute', 'v1', credentials=credentials)

    results = {}
    for instance in instances:
        try:
            if action == "start":
                service.instances().start(project=project, zone=zone, instance=instance).execute()
            elif action == "stop":
                service.instances().stop(project=project, zone=zone, instance=instance).execute()
            results[instance] = f"{action} initiated"
        except Exception as e:
            results[instance] = f"error: {str(e)}"

    return jsonify({"action": action, "results": results})
from googleapiclient import discovery
from google.auth import default
from flask import jsonify

def manage_vms(request):
    request_args = request.args
    action = request_args.get('action') if request_args else None

    project = "jaatbreak-dev-env"

    # Map instance names to their actual zones
    instances = {
        "apache-server-production": "asia-south1-c",
        "gke-prod-cluster": "asia-south2-c"
    }

    credentials, _ = default()
    service = discovery.build('compute', 'v1', credentials=credentials)

    results = {}

    for instance, zone in instances.items():
        try:
            if action == "start":
                service.instances().start(project=project, zone=zone, instance=instance).execute()
                results[instance] = f"start initiated in {zone}"
            elif action == "stop":
                service.instances().stop(project=project, zone=zone, instance=instance).execute()
                results[instance] = f"stop initiated in {zone}"
            else:
                results[instance] = f"invalid action '{action}'"
        except Exception as e:
            results[instance] = f"error: {str(e)}"

    return jsonify({"action": action, "results": results})
