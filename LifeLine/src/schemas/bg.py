from pydantic import BaseModel
from datetime import datetime

class Prediction(BaseModel):
    uid: int
    datetime: str
    latitude: float
    longitude: float
    
    def to_input_array(self):
        dt = datetime.strptime(self.datetime, '%Y-%m-%d %H:%M:%S')
        return [[self.uid, self.latitude, self.longitude, dt]]

