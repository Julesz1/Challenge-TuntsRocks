import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sheet = '_Engenharia de Software – Desafio [Julia Venancio].xlsx' #defining the file i'm gonna read

df_grades = pd.read_excel(sheet, skiprows=2) #doing the dataframe of the grades and all stuff related to the student 

df_grades['Media'] = np.round((df_grades['P1'] + df_grades['P2'] + df_grades['P3']) / 3,2) #defining the calculation of the mean


conditions = [    #here i made something like an if but more simple, without the necessity of a loop, i made the verifications one by one and use them with the results respectively
    (df_grades['Faltas'] > 15),
    (df_grades['Media'] < 50),
    (df_grades['Media'] >= 50) & (df_grades['Media'] <= 70),
    (df_grades['Media'] > 70),
  ]


results = ['Reprovado por falta', 'Reprovado por nota', 'Exame', 'Aprovado']


df_grades['Situação'] = np.select(conditions, results) #write on the column "Situação" the situation after calculate the media and compare with the metrics

conditions_naf = [  #doing the same thing but this time with the naf
    (df_grades['Situação'] == 'Exame')
]

results_naf = [
    100 - (df_grades['Media'])
]

df_grades['Nota para Aprovação Final'] = np.select(conditions_naf, results_naf)

df_grades.to_excel(sheet, index=False) #i am sending my changes to the original file. In future, to improve this process, I could consume the Google API and update it in the cloud.
    




