#Header
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from tabulate import tabulate
import math
import os
import sys
import openai
import json


#OpenAI - Config
openai.api_key  = "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"
    
    # Def de funciones Chat GPT
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

# Google - Config
    #Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('high-gecko-385718-0c4e9540b0b3.json', scope)
client = gspread.authorize(credentials)

    # Abre la hoja de cálculo por su nombre
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Il4rM35RQWDMRU_4gMP3LmyGpuA2HWLGEeVCKIcGDzo/edit?usp=sharing'
spreadsheet = client.open_by_url(spreadsheet_url)




def conexion(i):
  #connexion con Google Sheets
  worksheet = spreadsheet.get_worksheet(i)

      # Obtén los datos como una lista de diccionarios
  data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
  df = pd.DataFrame(data)

  #respuestas_objetivos = []
  df = pd.DataFrame(data)

  row_index = 0  

  return (df)


def write_to_cell(spreadsheet, sheet_number, row, col, value):
    try:
        # Get the specified worksheet
        worksheet = spreadsheet.get_worksheet(sheet_number)

        # Update the specified cell with the provided value
        worksheet.update_cell(row, col, value)

    except Exception as e:
        print(f"An error occurred: {str(e)}")



def procesar_preguntas(df):
    i = 0
    for _, row in df.iterrows():
        i = i+1 
        NUMERO = row['NUMERO']
        pregunta = row['PREGUNTA']
        print("\n")      
        print(pregunta)

        respuesta = input(f"Respuesta para la pregunta {NUMERO}: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        df.at[_, 'RESPUESTA'] = respuesta
        write_to_cell(spreadsheet, sheet_number=2, row=i+1 , col=4, value=respuesta)





#INICIO DE LA APLICACIÓN
print ('\nHola Agustín!!👋')
print('\nTu primer entrenamiento es mañana. 😄😄😄\n')
print('\nTe comparto mi recomendación de cómo llevarlo adelante, pero sabé que el que tiene la última palabra sos vos, yo soy tu co-piloto.\n')
df = conexion(10)
tabla = tabulate(df, headers='keys', tablefmt='pretty', showindex=False, stralign="left") 
print(tabla)
print('\nSi queres información mas detallada de los ejercicios o quieres buscar alternativas a los que te compartimos podes entrar a la siguiente link: https://conecta.rugby/library-all')
print('\nBuena suerte en el entrenamiento de mañana, después voy a hacerte algunas preguntas asi retroalimentamos los ejercicios.')
print('\nHasta luego 👋👋👋\n')
sys.exit()

