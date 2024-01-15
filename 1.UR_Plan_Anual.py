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
#openai.api_key  = "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"
    
    # Def de funciones Chat GPT
'''def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
'''

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

        respuesta = input(f"Respuesta: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        df.at[_, 'RESPUESTA'] = respuesta
        write_to_cell(spreadsheet, sheet_number=2, row=i+1 , col=4, value=respuesta)



def procesar_preguntas_amateur(df):
    i = 0
    for _, row in df.iterrows():
        i = i+1 
        NUMERO = row['NUMERO']
        pregunta = row['PREGUNTA']
        print("\n")      
        print(pregunta)

        respuesta = input(f"Respuesta: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        df.at[_, 'RESPUESTA'] = respuesta
        write_to_cell(spreadsheet, sheet_number=4, row=i+1, col=4, value=respuesta) 

def procesar_preguntas_minima(df):
    i = 0
    for _, row in df.iterrows():
        i = i+1 
        NUMERO = row['NUMERO']
        pregunta = row['PREGUNTA']
        print("\n")      
        print(pregunta)

        respuesta = input(f"Respuesta: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        df.at[_, 'RESPUESTA'] = respuesta
        write_to_cell(spreadsheet, sheet_number=3, row=i+1, col=4, value=respuesta) 

#df = conexion(3)
#print(df)







#INICIO DE LA APLICACIÓN
print ('\nHola Agustín!!👋')
print('\nMi nombre es Martín Gaitán 🏉 y soy tu copiloto de la UAR durante la campaña 2024 de Trelew Rugby.\n')
print('En la UAR estamos comprometidos con la formación de entrenadores, por eso creamos Connecta Rugby en donde brindamos cursos on-line certificados por la World Rugby.\n')
print('Basado en estos conceptos mi objetivo es ayudarte a que:')
print('- Compartas tiempo de calidad con los chicos y chicas')
print('- Logres resultados con mayor calidad.')
print('\nAntes de arrancar, necesitamos conocer mejor a tu equipo y sus objetivos.')
print ('\nEmpecemos!😀')

#INICIO BLOQUE 1 - PLAN ANUAL
sheet_number = 2  #Hola 3  
df = conexion(sheet_number)
procesar_preguntas(df)
#print(df)
cell_value = df.iloc[0, 3] 
#print(cell_value)
cell_value = cell_value.lower()

print('\n\nAquí terminan las preguntas de diagnóstico general.')



'''
if cell_value == "a":
    print('\nFelicitaciones por elegir el plan de 9 horas, este es el mejor plan que ofrecemos.')
    print('\nLa confección de este plan dura aproximadamente 1 hora de trabajo pero para hacerlo tenés que hacer los cursos de Entrenadores Nivel I y Nivel II que duran 4 horas cada uno. Vemos que hiciste el curso de Entrenador Nivel I, competá el curso de Entrenadores Nivel 2 ingresando al siguiente link: https://app.conecta.rugby/curso/960587')
    print('\nTe espero cuando tengas la certifiación. 🏉🏉🏉')
    sys.exit()
'''

if cell_value == "a":
    print('\nFelicitacion por elegir el plan de 4 horas y media.')
    print('\nLa confección de este plan dura aproximadamente 30 minutos de trabajo ya que tenes el curso Entrenadores Nivel I certificado en Conecta. Te recomendamos que hagas el Nivel II. Te recuerdo el link a Conecta Rugby: link: https://app.conecta.rugby/curso/960587')
    print('\nAhora si, manos a la obra')
    i = 4  ### Sheet de Plan Amateur 
    df = conexion(i)
    # Llamar a la función con tu DataFrame
    #procesar_preguntas(df)
    procesar_preguntas_amateur(df)
    print('\nEl plan anual esta listo! 🏉🏉🏉')
    i = 6  ### Sheet de Plan Amateur 
    df = conexion(i)
    tabla = tabulate(df, headers='keys', tablefmt='pretty', showindex=False, stralign="left")
    print(tabla)
    print('\nEntrá a la siguiente url para observarlo en detalle: https://shorturl.at/jqsFK')
    print('\nBuena suerte para el torneo 👊 Te voy a escribir unos días antes del primer entrenamiento para ayudarte a planificar la primer semana de trabajo!\n')
    sys.exit()


elif cell_value == "b":
    print('\nLamentamos que solo tengas 10 minutos para confeccionar algo tan importante como el Plan Anual 😕😕😕\nDejamos a tu disposición el material de Conecta Rugby, el portal educativo de la UAR, te sugerimos que hagas el curso de Entrenadores Nivel I ingresando a https://app.conecta.rugby/curso/960587')
    i = 3  ### Sheet de Plan de Minima 
    df = conexion(i)
    print('\nAhora si, manos a la obra')
    # Llamar a la función con tu DataFrame
    procesar_preguntas_minima(df)
    print('\nEl plan anual esta listo! 🏉🏉🏉')
    i = 5  ### Sheet de Plan Amateur 
    df = conexion(i)
    tabla = tabulate(df, headers='keys', tablefmt='pretty', showindex=False, stralign="left")
    print(tabla)
    print('\nEntrá a la siguiente url para observarlo en detalle: https://t.ly/jnd6W')
    print('\nBuena suerte para el torneo 👊 Te voy a escribir unos días antes del primer entrenamiento para ayudarte a planificar la primer semana de trabajo!\n')



    #print('\nEl plan anual esta listo! 🏉🏉🏉 Entrá a la siguiente url para observarlo: https://t.ly/jnd6W')
    #print('\nBuena suerte para el torneo 👊 Te voy a escribir el día antes del primer entrenamiento para ayudarte a planificar la primer semana de trabajo!\n')
    sys.exit()

else:
    print("Parece que no elgiste ningun plan.")
    sys.exit()

### FIN DE LA APLICACIÓN      






'''def procesar_introduccion(df):
    for _, row in df.iterrows():
        NUMERO = row['NUMERO']
        pregunta = row['PREGUNTA']
        print(pregunta)
'''
#procesar_introduccion(df)

        #respuesta = input(f"Respuesta para la pregunta {NUMERO}: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        #df.at[_, 'RESPUESTA'] = respuesta



'''def procesar_preguntas(df, sheet_number):
    j = 0
    s = sheet_number
    for _, row in df.iterrows():
        j = j+1 
        NUMERO = row['NUMERO']
        pregunta = row['PREGUNTA']
        print("\n")      
        print(pregunta)

        respuesta = input(f"Respuesta para la pregunta {NUMERO}: ")
        
        # Aquí puedes hacer algo con la respuesta, como almacenarla en otra lista, DataFrame, etc.
        # Por ejemplo, puedes crear una nueva columna 'RESPUESTA' en el DataFrame original y asignarle el valor de la respuesta.
        df.at[_, 'RESPUESTA'] = respuesta
        write_to_cell(spreadsheet = 0, sheet_number = s, row=j+1, col=4, value=respuesta)
'''


# Supongamos que tienes un DataFrame llamado 'df' con columnas 'NUMERO' y 'PREGUNTA'.
# Puedes crear una nueva columna 'RESPUESTA' para almacenar las respuestas

'''if your_dataframe is not None:
    # Now you can work with 'your_dataframe' which contains the data from the specified worksheet.
    print(your_dataframe.head())  # Print the first few rows of the DataFrame


worksheet = spreadsheet.get_worksheet(0)

    # Obtén los datos como una lista de diccionarios
data = worksheet.get_all_records()

    # Crea un DataFrame de pandas con los datos
df = pd.DataFrame(data)

Ver que numero tiene cada sheet


x = 0
for x in range(1, 14):
      worksheet = spreadsheet.get_worksheet(x)
      cell_value = worksheet.acell("B2").value
      print(cell_value)

#Loop de pregutas
'''


#Iniciacion de variables
'''length = 20
zero_array = [0] * length
    
    # Crea la funcion filtrado de jugadores

'''
# Define the filter_and_sort_players function
def filter_and_sort_players(df, puesto):
    # Check if 'PUESTO' column exists in the DataFrame
    if 'PUESTO' not in df.columns:
        raise ValueError("DataFrame does not contain a 'PUESTO' column.")

    # Initialize an empty DataFrame
    jugador = pd.DataFrame()

    # Filter players by 'PUESTO' and 'TIPO' if the column exists
    if 'PUESTO' in df.columns:
        jugador = df[df['PUESTO'] == puesto]

    # Check if any data was found
    if jugador.empty:
        return "No players found for the given 'PUESTO'."

    # Truncate 'PERFILADO' to integer
    jugador['PERFILADO'] = jugador['PERFILADO'].astype(int)

    # Sort players by 'PERFILADO'
    jugador_sorted = jugador.sort_values(by='PERFILADO', ascending=False)

    # Define column selection based on 'PUESTO'
    if puesto in [1]:
        columnas_seleccionadas = jugador_sorted[['NOMBRE', 'PESO', 'ESTATURA', 'SCRUM', 'GENERAL', 'PERFILADO', 'GRUPO']]
    else:
        print("So boludo")
    
    # Convert the selected columns to a formatted table
    tabla = tabulate(columnas_seleccionadas, headers='keys', tablefmt='pretty', showindex=False)

    return tabla

'''
sheet_number = 2  # Change this to the desired sheet number
df = get_data_as_dataframe(spreadsheet, sheet_number=sheet_number)
#row_index = 0
#respuesta = input("Respuesta: ")
cell_value = df.loc[2, 5]
pritn(cell_value)

if cell_value == "a":
  print("Pro")
elif cell_value == "b":
  print("https://shorturl.at/jqsFK")
else:
  print ("Minma")
'''

'''
if Calidad_Plan == 'a':
    print(Calidad_Plan)
    print('PRO - Seccion en construcción')

elif Calidad_Plan == 'b':
    print(Calidad_Plan)
    print('Plan Amateur: Para hacer este plan es mandatorio que hagas nuestro Curso de entrenadores Nivel I en https://app.conecta.rugby/curso/960587')
    print('Ahora si, manos a la obra')
    #  print('Amateur - Seccion en construcción')
    sheet_number = 4
    df = get_data_as_dataframe(spreadsheet, sheet_number=sheet_number)

    # Llamar a la función con tu DataFrame
    procesar_preguntas(df)

    print('El plan anual esta listo! 🏉🏉🏉 Entrá a la siguiente url para observarlo: https://shorturl.at/jqsFK')
    sys.exit()

else:
    print(Calidad_Plan)
    print('Minima - Seccion en construcción')
    print("https://shorturl.at/aqTU2")
    # error: AR0C02GL0N1Q05N:UR eferrero$ python ur_2.py
    # File "/Applications/MAMP/htdocs/UR/ur_2.py", line 243
    # else:
    # ^^^^
    # SyntaxError: invalid syntax

row_index = 0
Calidad_Plan = ''
Calidad_Plan= Calidad_Plan.lower()

if Calidad_Plan == 'a':
  print('PRO - Seccion en construcción')

elif Calidad_Plan == 'b':
  print('Plan Amateur: Para hacer este plan es mandatorio que hagas nuestro Curso de entrenadores Nivel I en https://app.conecta.rugby/curso/960587')
  print('Ahora si, manos a la obra')
#  print('Amateur - Seccion en construcción')
  sheet_number = 4
  df = get_data_as_dataframe(spreadsheet, sheet_number=sheet_number)

  

sheet_number = 4  # Change this to the desired sheet number

df = get_data_as_dataframe(spreadsheet, sheet_number=sheet_number)


# Llamar a la función con tu DataFrame
procesar_preguntas(df)

print ('El plan anual esta listo! 🏉🏉🏉 Entrá a la siguiente url para observarlo: https://shorturl.at/jqsFK')
sys.exit()

else:
  print('Minima - Seccion en construcción')
  print("https://shorturl.at/aqTU2")
'''
'''row_index = 0
for _, row in df.iterrows():
      row_index = row_index+1
#     print()
#      cell_value = worksheet.acell("A1").value
#      print(cell_value)
      NUMERO = row['NUMERO']
      pregunta = row['PREGUNTA']
      
      print(pregunta)
      respuesta = input("Respuesta: ")

      #Update sheet
print ('El plan anual esta listo! 🏉🏉🏉 Entrá a la siguiente url para observarlo: https://shorturl.at/aqTU2')
sys.exit()

#  print('\nAccedé al siguiente enlace en donde vas a encontrar tu plan anual')

      
else: 
print("Minima - Seccion en construcción")
exit()

#connexion con Google Sheets
worksheet = spreadsheet.get_worksheet(3)

      # Obtén los datos como una lista de diccionarios
data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
df = pd.DataFrame(data)

  #respuestas_objetivos = []
df = pd.DataFrame(data)

# Llamar a la función con tu DataFrame
procesar_preguntas(df)

# Ahora el DataFrame original 'df' tiene una nueva columna 'RESPUESTA' con las respuestas del usuario.
print(df)


  #connexion con Google Sheets
worksheet = spreadsheet.get_worksheet(4)

      # Obtén los datos como una lista de diccionarios
data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
df = pd.DataFrame(data)

  #respuestas_objetivos = []
df = pd.DataFrame(data)

cell_value = worksheet.acell("B2").value
print(cell_value)
worksheet.update_cell(1, 1, cell_value)

print ('El plan anual esta listo! 🏉🏉🏉 Entrá a la siguiente url para observarlo: https://shorturl.at/aqTU2')
#  print('\nAccedé al siguiente enlace en donde vas a encontrar tu plan anual')

sys.exit()

'''



'''

  # 1. Mi equipo
def Diagnostico_General():
  print('Aca van las preguntas de Gaitán')

Diagnostico_General()

def Diagnostico_Jugadores():

  # Pilares titulo
  print('\n\n1.DIAGNOSTICO \n1.1.TU EQUIPO \nVamos a mostrarte datos de tus jugadores que los podes editar ingresando a la siguiente url: https://shorturl.at/kEIYZ. Te recomendamos que completes el excel con el técnico del año pasado.\n\nEl GENERAL es el promedio de todas las dimensiones;el PERFILADO es propio de cada posición.\n\nPilares: PERFILADO: Peso, Estatura y Scrum\n')


  print('1')
  puesto = 1
  tabla = filter_and_sort_players(df,puesto)
  print(tabla)


  # Pilar derecho -  Mostrar los resultados en forma de tabla en la consola
  print('\n3')
  puesto = 3
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print ('\nSUGERENCIA: POWERED BY UAR\n')

  # Pilar derecho -  Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")

  if respuesta.lower() == 'salir':
    sys.exit()

  # Hooker título
  print('\nHooker: \nPERFILADO: Peso, Line, y Scrum')
  puesto = 2
  tabla = filter_and_sort_players(df, puesto)
  print('\n2')
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')

  # Hooker - Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
      

  if respuesta.lower() == 'salir':
    sys.exit()

  # Segunda línea - Título
  print('\n\nSegunda linea: \nPERFILADO: Estatura, Peso y Line\n')

  print('4')
  puesto = 4
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print('\n5')
  puesto = 5
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print ('\nSUGERENCIA: POWERED BY UAR\n')
  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
      
  if respuesta.lower() == 'salir':
    sys.exit()
    
  # Tercera línea - Título
  print('\n\nTercera linea: \nPERFILADO: Peso, Ataque,y Defensa \n')
  print('6')
  puesto = 6
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print('\n7')
  puesto = 7
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  puesto = 8
  tabla = filter_and_sort_players(df, puesto)
  print('\n8')
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')

  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
      
  if respuesta.lower() == 'salir':
    sys.exit

  # Medio Scrum - Título
  print('\n\nMedio Scrum: \nPERFILADO: Ataque, Defensa, Pase y Kick')
  print('\n9')
  puesto = 9
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')


  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
      
  if respuesta.lower() == 'salir':
    sys.exit()

  # Apetura - Título
  print('\n\nApertura: \nPERFILADO: Ataque, Defensa, Pase y Kick ')

  print('\n10')
  puesto = 10
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')

  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")

  #print ('\nSUGERENCIA: \n')
  if respuesta.lower() == 'salir':
    sys.exit()

  # Centros - Título
  print('\n\nCentros: \nPERFILADO: Juego aéreo, Ataque y Defensa y Line')
  print('\n12')
  puesto = 12
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print('\n13')
  puesto = 13
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')


  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")


  if respuesta.lower() == 'salir':
    sys.exit()

  # Wings y Full back - Título
  print('\n\nWings y Full back: \nPERFILADO: Ataque, Peso y Defensa ')

  print('\n11')
  puesto = 11
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print('\n14')
  puesto = 14
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)

  print('\n15')
  puesto = 15
  tabla = filter_and_sort_players(df, puesto)
  print(tabla)
  print ('\nSUGERENCIA: POWERED BY UAR\n')


  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")



  if respuesta.lower() == 'salir':
    sys.exit()

Diagnostico_Jugadores()

def Diagnostico_Rivales():

  print('Diagnostico interno TERMINADO :) \n\n1.2. RIVALES:\n Vamos a ir mostrandote los equipos ordenados por su posicion en el último torneo.\n La idea es trabajar en conjunto con los entrenadores de la campaña 2023.')

  comentarios_clubes = []  # Esto crea una lista vacía
  row_index = 0
  
  for x in range(1, 11):
      if respuesta == 'salir':
          sys.exit()
          
      POSICION = x
      table = filter_and_sort_club(df, POSICION)
      print(table)
      comentario = input("Ingresa un comentario del club (o 'salir' para terminar): ")
      print("\n")

      worksheet.update_cell(x+1, 18, comentario)

  # print(comentarios_clubes)


  print ('\nFIN DE LA ETAPA 1.DIAGNOSTICO\n')

Diagnostico_Rivales()

# 2) OBJETIVOS
def Objetivos():
  #Google Sheets 
  worksheet = spreadsheet.get_worksheet(4)

      # Obtén los datos como una lista de diccionarios
  data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
  df = pd.DataFrame(data)

  #respuestas_objetivos = []
  df = pd.DataFrame(data)


  print ('2.OBJETIVOS:')
  print ('Vamos a hacerte las preguntas necesarias para poder definir el objetivo con claridad y presentarte una primera versión del plan anual trimestralizado.')


  respuesta = ""
  if respuesta.lower() == 'salir':
    sys.exit()

  #Las 15 preguntas    
  #respuestas_objetivos = [] 
  row_index = 0

  for _, row in df.iterrows():
      row_index = row_index+1
      NUMERO = row['NUMERO']
      pregunta = row['PREGUNTA']
      
      #Imprimo la pregunta
      print(pregunta)
      respuesta = input("Respuesta ('salir' para salir): ")
      
      #Update sheet
      worksheet.update_cell(row_index+1, 4, respuesta)

      # Combina la cadena JSON con el texto
      #full_prompt = "Como entrenador de rugby de la M16 de GER creo que " + respuesta + ". Contestame en 1 palabra."
      #prompt =  "[ {'role':'user', 'content':" + full_prompt + "}]"
      # Luego, utiliza full_prompt en tu llamada a la función get_completion_from_messages
      #response = get_completion_from_messages(full_prompt, temperature=0)

      if respuesta.lower() == 'salir':
          sys.exit()

      # Update the DataFrame with the response using loc
      #df.loc[df['NUMERO'] == NUMERO, 'RESPUESTA'] = respuesta
      # Update a cell using row and column indices
      print()

  if respuesta.lower() == 'salir':
    sys.exit()

Objetivos()


# 3) PLAN
def Plan():

  #Google Sheets 
  worksheet = spreadsheet.get_worksheet(6)

      # Obtén los datos como una lista de diccionarios
  data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
  df = pd.DataFrame(data)

  #respuestas_objetivos = []
  df = pd.DataFrame(data)
  
  columnas_seleccionadas = df[['ETAPA', 'MES', 'OBJETIVO', 'INICIO', 'DURACION (SEMANAS)', 'FERIADOS']]
    
  tabla = tabulate(columnas_seleccionadas, headers='keys', tablefmt='pretty', showindex=False, stralign="left")
  
  print ('3.PLAN:\n')
  print ('Vamos a dividir el año en 5 etapas como se muestra a continuación:\n')
  print(tabla)
  # Preguntar al usuario si desea continuar
  respuesta = input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
      
  if respuesta.lower() == 'salir':
    sys.exit


  #PLAN ---- Pre-temporada
  #Google Sheets 
  worksheet = spreadsheet.get_worksheet(7)

      # Obtén los datos como una lista de diccionarios
  data = worksheet.get_all_records()

      # Crea un DataFrame de pandas con los datos
  df = pd.DataFrame(data)

  #respuestas_objetivos = []
  df = pd.DataFrame(data)
  
  columnas_seleccionadas = df[['BLOQUE', 'ACTIVIDAD', 'MINUTOS']]
    
  tabla = tabulate(columnas_seleccionadas, headers='keys', tablefmt='pretty', showindex=False, stralign="left")
  
  
  
  print ('\n3.1. Plan de Pre-temporada:')
  print ('\nProponemos que sean 9 semanas de 3 sesiones: martes y jueves de 20 a 22hs en la cancha de GER con entrenadores; y el sabado por su cuenta. Sugerimos la siguiente estructura tipo para los entrenamientos:')
  print(tabla)
  print ('Sugerimos fuertemente hacer el Test Bronco. El trabajo fisico queda liderado por Guille.')
  print ('\nCon respecto a las "Destrezas" vamos a trabajar sobre el RUCK y el TACKLE elegidas las destrezas CLAVE.\nEn el siguiente link tenes acceso a mas de 100 ejercicios de cada destreza. ')
  print ('\nPor último, en este link tenés mas de 50 ejercicios de "Juego con pelota" ')
Plan()

#4) EJECUCION --- Pre-temporada
def Ejecucion():
  print('4. EJECUCION')
  print('4. PRE-TEMPORADA')
  respuesta = input ('¿Cómo fue ese primer entrenamiento?')
  print('BUENISIMO A SEGUIR METIENDOLE')
#Ejecucion() '''

'''# Example usage:
if __name__ == "__main__":
    # Sample DataFrame (replace this with your actual DataFrame loading code)
    data = {
        'NOMBRE': ['Player1', 'Player2', 'Player3'],
        'PUESTO': [1, 2, 1],
        'PESO': [80, 90, 85],
        'ESTATURA': [180, 185, 175],
        'SCRUM': [70, 65, 75],
        'GENERAL': [85, 80, 90],
        'PERFILADO': [88.5, 82.3, 91.2]
    }
'''    


'''def filter_and_sort_players(df, puesto):
    # Filter players by 'PUESTO' and 'TIPO'
    # jugador = df[(df['PUESTO'] == puesto)]
    jugador = 0
    print(type(jugador))

    print(jugador)

    # jugador['PUESTO'] = jugador['PUESTO']
    print(jugador)
    # Truncate 'PERFILADO' to integer
    jugador['PERFILADO'] = jugador['PERFILADO'].astype(int)

    # Sort players by 'PERFILADO'
    jugador_sorted = jugador.sort_values(by='PERFILADO', ascending=False)

    # Filter players with 'GENERAL' greater than 49 (you can uncomment this line if needed)
    #jugadores_filtrados = jugador_sorted[jugador_sorted['GENERAL'] > 49]

    # Sort filtered players by 'PERFILADO' again
    jugadores_ordenados = jugador_sorted.sort_values(by='PERFILADO', ascending=False)

    # Select columns based on 'PUESTO'
    if puesto in [1]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ESTATURA', 'SCRUM', 'GENERAL', 'PERFILADO']]
   
    elif puesto in [2]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'LINE','SCRUM', 'GENERAL', 'PERFILADO']]
   
    elif puesto in [3]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ESTATURA', 'SCRUM', 'GENERAL', 'PERFILADO']]

    elif puesto in [4]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ESTATURA', 'LINE', 'GENERAL', 'PERFILADO']]

    elif puesto in [5]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ESTATURA', 'LINE', 'GENERAL', 'PERFILADO']]

    elif puesto in [6]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
    
    elif puesto in [7]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
   
    elif puesto in [8]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
   
    elif puesto in [9]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
    
    elif puesto in [10]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]


    elif puesto in [12]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
    
    elif puesto in [13]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'PESO', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
    
    elif puesto in [11]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]
    
    elif puesto in [14]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]

    elif puesto in [15]:
        columnas_seleccionadas = jugadores_ordenados[['NOMBRE', 'ATAQUE', 'DEFENSA', 'GENERAL', 'PERFILADO']]

    else:
        raise ValueError("Invalid 'PUESTO' value. Supported values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15.")
    
    tabla = tabulate(columnas_seleccionadas, headers='keys', tablefmt='pretty', showindex=False)

    return tabla
puesto = 1
tabla = filter_and_sort_players(df, puesto)
print (tabla)
'''

'''def filter_and_sort_club(df, posicion):
    # Filter players by 'POSICION' and 'TIPO'
    jugador = df[(df['POSICION'] == posicion) & (df['TIPO'] == 'CLUB')].copy()

    # Truncate 'PERFILADO' to integer
    jugador['POSICION'] = jugador['POSICION'].astype(int)

    # Select columns based on 'PUESTO'
 
    columnas_seleccionadas = jugador[['NOMBRE', 'POSICION', 'GENERAL', 'BENCHMARK', 'PESO', 'ESTATURA' ]]
    
    tabla = tabulate(columnas_seleccionadas, headers='keys', tablefmt='pretty', showindex=False, stralign="left")

    return tabla
'''

