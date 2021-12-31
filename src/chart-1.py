import csv
import json
import os



script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "..\\resources"
abs_file_path = os.path.join(script_dir, rel_path)

datafields = '''[{
                "type": "PieSeries",
                "dataFields": {
                    "value": "Status",
                    "category": "URLs"
                }
            }]'''

csvfile =  open(os.path.join(abs_file_path,'output.csv'), 'r')

fieldnames = ("URLs","ExpectedOutput","Status")
reader = csv.DictReader( csvfile, fieldnames)
next(reader, None)
out = json.dumps( [ row for row in reader ] )
#print(f'json: {out}')

with open(os.path.join(abs_file_path,'report\\template.html'),'r', encoding='utf-8') as template:
    filedata = template.read()    
    #print(f'filedata: {filedata}')
    filedata = filedata.replace('datafields', datafields)
    filedata = filedata.replace('jsondata', out)
    #print(f'filedata: {filedata}')
    with open(os.path.join(abs_file_path,'report\\index.html'),'w', encoding='utf-8') as report:    
        report.write(filedata)
