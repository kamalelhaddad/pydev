import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        #csvReader = csv.DictReader(csvf)
        csvReader = csv.reader(csvf, delimiter=';') 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            name = row[0].split('\t')
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'data.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)