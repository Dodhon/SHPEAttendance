import pandas as pd
import os, sys
import csv


allPeople = set()
masterDf = pd.DataFrame

def createTable():
    
    createNamesColumn(masterDf)
    dfs = list()
    

def updateTable():
    files = getFiles()
    dfs = list()
    for file in files:
        dfs.append(pd.read_csv(file)) ## dfs is now a list of dataframes. Each data frame is one attendance form 
    for df in dfs:
        allPeople.add(getEmails(df))

def createEmailColumn(df):
    if "Hawk Email" not in df:
            df.insert(0,"Hawk Email", allPeople)

def getEmails(df): ## will return list of all names of people that attended a given event
    emails = list()
    for e in df["Hawk Email"]:
        pass
    return emails
def processName(name):
    return str(name).lower.replace(" ", "")





def getFiles(): ## returns a list of all attendance files
    path = "attendanceFormResponses"
    dirs = os.listdir(path)
    csvFiles = list()

    for file in dirs:
        try:
            file == '*.csv'
            csvFiles.append(file)
        except:
            os.remove(file)
    
    return csvFiles