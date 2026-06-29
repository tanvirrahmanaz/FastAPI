from fastapi import FastAPI,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return {'message':"FastaAPI is running"}

@app.get("/patients")
def get_patients():
    return {'message':"Patients Routs working"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patients/{patient_id}')
def view_patient(patient_id:str):
    #load all the patient data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404,detail="patient Not found")


@app.get('/sort')
def sort_patients(sort_by : str= Query(...,description='sort on the basis of height, weight or bmi'), order:str =Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"invalid field select from {valid_fields}")
