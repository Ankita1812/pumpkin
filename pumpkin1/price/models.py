from django.db import models
import uuid
from django.contrib.auth.models import User
''''import mysql.connector
# Create your models here.
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="abc"
)

# data = pd.read_csv("atlanta.csv")
cityc = [
    (Atlanta, 'ATLANTA'),
    (Baltimore, 'BALTIMORE'),
    (Boston, 'BOSTON'),
    (Chicago, 'CHICAGO'),
    (Columbia, 'COLUMBIA'),
    (Dallas, 'DALLAS'),
    (Detroit, 'DETROIT'),
    (Los_Angeles, 'LOS ANGELES'),
    (Miami, 'MIAMI'),
    (New_York, 'NEW YORK'),
    (Philadelphia, 'PHILADELPHIA'),
    (San_Fransisco, 'SAN FRANSISCO'),
    (St_Louis, 'ST. LOUIS'),
]
'''

class Pumpkin:
    date = models.DateField()
    city = models.CharField(max_length=100,)# choices=cityc)
    lowp = models.DecimalField()
    highp = models.DecimalField()
