def normalize_commits_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "name": r["name"],
            "message": r["metadata"].get("message"),
            "author_name": r["metadata"].get("author"),
            "created_date": r["created_at"],
            "updated_date": r["updated_at"]
        })

    return normalized

def normalize_prs_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "title": r["name"],
            "state": r["status"],
            "author_name": r["metadata"].get("author"),
            "created_date": r["created_at"],
            "updated_date": r["updated_at"]
        })

    return normalized

def normalize_issues_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "title": r["name"],
            "state": r["status"],
            "author_name": r["metadata"].get("author"),
            "created_date": r["created_at"],
            "updated_date": r["updated_at"]
        })

    return normalized

def normalize_workflow_runs_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "name": r["name"],
            "status": r["status"],
            "conclusion": r["metadata"].get("conclusion"),
            "url": r["metadata"].get("url"),
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    return normalized

def normalize_deployments_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "name": r["type"],
            "status": r["status"],
            "environment": r["environment"],
            "url": r["url"],
            "sha": r["metadata"].get("sha"),
            "ref": r["metadata"].get("ref"),
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    return normalized

def normalize_projects_data_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "title": r["name"],
            "status": r["status"],
            "number": r["metadata"].get("number"),
            "labels": r["metadata"].get("labels"),
            "project_fields": r["metadata"].get("project_fields"),
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    # print("Normalized data from the normalize.py: \n", normalized)
    return normalized

def normalize_bq_data_to_devlake(data):
    records = data["data"]

    normalized = []

    for r in records:
        normalized.append({
            "id": r["id"],
            "service_name": r["name"],
            "transaction_type": r["status"],
            "platform": r["metadata"].get("platform"),
            "cost": r["metadata"].get("cost"),
            "sku_name": r["metadata"].get("sku_name"),
            "location": r["metadata"].get("location"),
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    return normalized