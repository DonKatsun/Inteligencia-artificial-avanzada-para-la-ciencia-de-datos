import os
import csv
import pathlib
ejemplo_dir = 'images'
contenido = os.listdir(ejemplo_dir)
imagenes = []
nombres = []
stage = []
discharge = []
stageF = []
dischargeF = []

with open('2012_2019_PlatteRiverWeir_features_merged_all.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nombres.append(row[' Filename'])
        stage.append(row[' Stage'])
        discharge.append(row[' Discharge'])

carpetas=os.listdir(ejemplo_dir)
directorio = pathlib.Path(ejemplo_dir)
index=0
for i in nombres:
    for j in carpetas:
        if(i in os.listdir(ejemplo_dir+'/'+str(j))):
            imagenes.append('file:///C:/Users/edgar/OneDrive/Escritorio/Tec/reto/images/' +str(j)+'/'+str(i))
            stageF.append(stage[index])
            dischargeF.append(discharge[index])
            break
    index+=1

    
with open('data.csv', 'w', newline='') as data:
    writer = csv.writer(data)
    writer.writerow(["img","stage","discharge"])
    for i in range(len(imagenes)):
        writer.writerow([imagenes[i], stageF[i], dischargeF[i]])

print(os.listdir('images/20150718'))
#print(imagenes)