import pandas as pd
import os, sys
import csv


allPeople = set()

def createTable():
    files = getFiles()
    masterDf = pd.DataFrame
    dfs = list()
    for file in files:
        dfs.append(pd.read_csv(file)) ## dfs is now a list of dataframes. Each data frame is one attendance form 
    for df in dfs:
        allPeople.add(getNames(df))
        


def getNames(df): ## will return list of all names of people that attended a given event
    pass 



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