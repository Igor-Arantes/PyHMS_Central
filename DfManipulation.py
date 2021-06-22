from os import replace
import pandas as pd


#Variables
#-----------------------------------------------------

#Dict to rename
dict_columns = {'ptchupvok':'Pitch','heavprok':'Heave','heavvlok':'Heave Rate','rollptvok':'Roll',
'relhumiok':'Umidade','headvsok':'Aproamento','windspdok':'Intensidade de Vento','localtime':'Data e Hora',
'winddirok':'Direção de Vento','airpresok':'Pressão','airtempok':'Temperatura'}

#List to reorder    
columns_order=['Data e Hora','Pitch', 'Roll','Heave','Heave Rate', 'Intensidade de Vento',
'Direção de Vento', 'Aproamento','Temperatura','Umidade', 'Pressão']

#Dict Status
dict_status={True:'Ok',False:'NOk'}

#-------------------------------------------------------


#Fucntions
#-------------------------------------------------------

#Rename columns
def rename_columns(df, dict):
    return(df.rename(columns=dict))


#Reorder columns
def reorder_columns(df,order):
    return(df.reindex(columns=order))


#Styliyng

def background_color(val):
    if val == 'Nok':
        color = 'red'
    elif val == 'Ok':
        color = 'Green'
    elif val == '--':
        color = 'Black'    
    return 'background-color: %s' % color

def coloring(df):
    return df.style.applymap(background_color)

def status_rename(df,dict):
    return df.replace(dict)