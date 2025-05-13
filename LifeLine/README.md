# LifeLine
A machine learning project created for the effective distribution of ambulances within the Nairobi region. It implements Natural Language Processing (NLP) to perform classification of injuries based on a description of an emergency.

The model also performs clustering based on the location and time of accidents that have occurred within the Nairobi region in the year 2019. This information is utilised for the optimal placement of emergency vehicles every 3 hours to ensure the shortest distance to the site of emergency therefore ensuring the shortest response time possible.

Our proposed solution is an innovative digital aggregator platform that will connect patients in need of emergency transportation to hospitals with app-listed drivers and ambulance companies. It aims to address two primary causes of delay in emergency care: delays in identifying the required care and delays in reaching definitive care.

The model is deployed using [FastAPI](https://fastapi.tiangolo.com) to allow for ease in the deployment and access of the output of the Machine Learning Algorithm

## How to Install and Run the Project
To run the project **locally**, download the GitHub repository and open it in your preferred IDE or text editor.
### 1. Ambulance Distribution

Install the required python packages by running the command `pip install -r requirements.txt`. This will install the listed packages into your virtual environment.

To run the local web server for accessing the project, run the command `uvicorn main:app --reload`. This starts up a web server on your localhost. To access the API endpoints, one can use either [Postman](https://www.postman.com) or your web browser.

### API Endpoints
An in depth documentation of the API endpoints can be accessed via your browser by accessing the url `127.0.0.1:8000/docs`.


### 2. Accident Classification
Open the file labelled `natural_language_processing_feature.ipynb`.

Run all the cells in the notebook to generate the model and save it in the `models` folder.

## The Team
Adriana Helga: [GitHub](https://github.com/AdrianaHelga)

Colette Muiruri: [GitHub](https://github.com/muiruric)

Dan Wanjohi: [GitHub](https://github.com/DanYT2)
