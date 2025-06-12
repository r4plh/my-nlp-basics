from fastapi import FastAPI , HTTPException , Query
import json

app = FastAPI()

def load_data():
    with open('data.json','r') as f:
        data = json.load(f)

    return data    


@app.get("/")
def hello():
    return {'message': 'An App to track pateints'}

@app.get("/about")
def about():
    return {'message': "To help doctors track the medical records of their pateints"}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {"message":"pateint could not be found"}

@app.get("/sort")
def sort_and_arrange(sort_by:str = Query(...,description="could be either on the basis of weight, height or bmi"), order:str = Query("asc",description = "could be asc or dsc")):

    valid_fields = ['height','weight','bmi']

    if sort_by in valid_fields:
        data = load_data()
    else:
        raise HTTPException(status_code=400,detail="bad request from user , no such field exists")

    if order not in ['asc','dsc']:
        raise HTTPException(status_code=400,detail="bad request from user , no such field exists")        

    data = load_data()

    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse = sort_order)
    return sorted_data
