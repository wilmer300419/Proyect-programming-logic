"""
Ejercicios
1. Crear una función que calcule la edad de una persona
"""
from datetime import datetime

def your_age(birthdate):
    now_date = datetime.now()
    birthdate_date = datetime.strptime(birthdate, "%d-%m-%Y")
    
    age = now_date.year - birthdate_date.year
    if (now_date.month, now_date.day) < (birthdate_date.month, birthdate_date.day):
        age -= 1
    
    print("Fecha actual:", now_date.date())
    return age

print(your_age("30-04-2005"))
