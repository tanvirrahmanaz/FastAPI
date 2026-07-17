from fastapi import FastAPI, HTTPException, status
import json

app = FastAPI()

bugs = {
    "BUG-001": {
        "title": "Login button not working",
        "description": "User clicks login button but nothing happens",
        "severity": "High",
        "priority": "P1",
        "status": "Open",
        "project": "Maison PMS",
        "assigned_to": "developer_1",
        "reported_by": "qa_1"
    },
    "BUG-002": {
        "title": "Reservation export missing",
        "description": "Export CSV button is not visible on reservation page",
        "severity": "Medium",
        "priority": "P2",
        "status": "In Progress",
        "project": "Maison PMS",
        "assigned_to": "developer_2",
        "reported_by": "qa_1"
    },
    "BUG-003": {
        "title": "Candidate score not updating",
        "description": "Interview score remains old after refresh",
        "severity": "High",
        "priority": "P1",
        "status": "Open",
        "project": "HireFlow",
        "assigned_to": "developer_3",
        "reported_by": "qa_2"
    }
}

def filter_bugs_by_status(bugs_data:dict,status:str) -> dict:
    result = {}

    for bug_id, bug in bugs_data.items():
        if bug["status"].lower() == status.lower():
            result[bug_id] = bug
    return result

def filter_bugs_by_severity(
        bugs_data: dict,
        severity: str
) -> dict:
    result = {}
    for bug_id, bug in bugs_data.items():
        if bug[severity].lower() == severity.lower():
            result[bug_id] = bug
        
    return result

def filter_bugs_by_project(
        bugs_data: dict,
        project: str
) -> dict :
    result = {}

    for bug_id, bug in bugs_data.item():
        if bug["project"].lower() == project.lower():
            result[bug_id]= bug
    return result

def paginate_bugs(
        bugs_data: dict,
        limit: int,
        offset:int
) -> dict:
    bug_items = list(bugs_data.items())
    paginated_items = bug_items[offset: offset+limit]

    return dict(paginated_items)



@app.get("/")
def home():
    return {
        "message" : "BugOps API is running"
    }

@app.get("/bugs")
def get_bugs(
    status: str | None = None,
    severity: str | None = None,
    project: str | None = None,
    keyword: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    result = bugs.copy