#IMPORTAR LIBRERÍAS Y DEMÁS
import random
import pandas as pd
import json
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

#CREACIÓN CLASE EMERGENCIA
# Definición de tipo y límites de cada atributo dentro de la clase.
class emergencia:
    tipo_emergencia = {
        "Accidentes de tráfico": ["Policía", "Ambulancia", "Bomberos"],
        "Problemas médicos agudos": ["Ambulancia"],
        "Incendios": ["Bomberos"],
        "Delitos en progreso": ["Policía", "GEOs", "Militares"],
        "Situaciones de peligro para la seguridad pública": ["Policía", "GEOs", "Ejército"],
        "Desastres naturales": ["Bomberos", "Ejército", "Servicios de emergencia"],
        "Emergencias químicas o radiológicas": ["Bomberos", "Servicios de emergencia"],
        "Personas desaparecidas": ["Policía"],
        "Rescates": ["Bomberos", "Forestales"],
        "Emergencias en el mar o montañas": ["Guardia Costera", "Forestales"],
        "Accidentes laborales": ["Ambulancia", "Bomberos"],
        "Emergencias ambientales": ["Servicios de emergencia", "Bomberos"]
        }
    grado = [
    "Urgencia extrema",
    "Urgente",
    "Moderado",
    "Leve"]
    fake = Faker('es_ES')
    def __init__(self):
        self.tipo_emergencia = random.choice(list(emergencia.tipo_emergencia))
        self.cuerpo_necesario = random.choice(emergencia.tipo_emergencia[self.tipo_emergencia])
        if self.cuerpo_necesario in ["GEOs","Militares"]:
            self.grado = random.choice(["Urgencia extrema","Urgente"])
        else:
            grados_urgencia = ['Leve', 'Moderado', 'Urgente', 'Urgencia extrema']
            probabilidades = [0.35, 0.45, 0.15, 0.05]
            self.grado = np.random.choice(grados_urgencia,p=probabilidades)
        self.localizacion = emergencia.fake.city()
        self.fecha = emergencia.generar_fecha_aleatoria()
        if self.cuerpo_necesario == "Ambulancia":
            self.requiere_medico = "Si"
        else:
            self.requiere_medico = random.choice(["Si", "No"])
        self.contacto = emergencia.fake.phone_number()
        self.contacto = emergencia.fake.phone_number()
    
    @staticmethod
    def generar_fecha_aleatoria():
        start_date = datetime.today().replace(year=datetime.today().year - 1)
        end_date = datetime.today()
        tiempo_entre_fechas = end_date - start_date
        dias_aleatorios = random.randrange(tiempo_entre_fechas.days)
        fecha_aleatoria = start_date + timedelta(days=dias_aleatorios)
        
        # Generar una hora, minutos y segundos aleatorios
        hora_aleatoria = random.randint(0, 23)
        minutos_aleatorios = random.randint(0, 59)
        segundos_aleatorios = random.randint(0, 59)

        # Combinar la fecha aleatoria con la hora, minutos y segundos aleatorios
        fecha_hora_aleatoria = fecha_aleatoria.replace(hour=hora_aleatoria, minute=minutos_aleatorios, second=segundos_aleatorios)
        return fecha_hora_aleatoria
    
    def to_json(self):
        data = self.__dict__.copy()
        data['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return json.dumps(data)

#GENERACIÓN DATA SET Y ALMACENAMIENTO EN DF:
registros = [emergencia() for _ in range(1000)]

data = {
    'Tipo de Emergencia': [registro.tipo_emergencia for registro in registros],
    'Grado': [registro.grado for registro in registros],
    'Cuerpo Necesario': [registro.cuerpo_necesario for registro in registros],
    'Localización': [registro.localizacion for registro in registros],
    'Fecha': [registro.fecha for registro in registros],
    'Requiere Médico': [registro.requiere_medico for registro in registros],
    'Contacto': [registro.contacto for registro in registros]
}

df_emergencias = pd.DataFrame(data)

#ORGANIZAMOS EL DATA SET POR FECHA (DE MÁS ANTIGUO A MÁS RECIENTE)
df_emergencias['Fecha'] = pd.to_datetime(df_emergencias['Fecha'])
df_emergencias['Fecha'] = df_emergencias['Fecha'].dt.strftime('%d/%m/%Y%H:%M:')
df_emergencias = df_emergencias.sort_values(by='Fecha')
df_emergencias = df_emergencias.reset_index(drop=True)