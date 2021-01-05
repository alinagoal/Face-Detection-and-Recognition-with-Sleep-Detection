import csv
import json

csvfile = open('D:\drowsy\python_env\FaceTrainDubey\StudentDetails\StudentDetails.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Id","Name","mail","pnumber")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')




# import csv
# import json

# csvfile = open('D:\drowsy\python_env\FaceTrainDubey\StudentDetails\StudentDetails.csv', 'r')
# jsonfile = open('file.json', 'w')

# fieldnames = ("Id","Name","mail","pnumber")
# reader = csv.DictReader( csvfile, fieldnames)
# out = json.dumps( [ row for row in reader ] )
# jsonfile.write(out)