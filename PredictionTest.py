from sklearn import svm
import joblib
import numpy as np
import csv

svmFog = joblib.load('svmFog.pkl')
svmHaze = joblib.load('svmHaze.pkl')

def analyzeData(data):
    fog_predict = svmFog.predict(data)
    haze_predict = svmHaze.predict(data)
    return [str(fog_predict[0]), str(haze_predict[0])]

def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        return False
    return True

def PrintNegativePrediction():
    tNegativeList=[]
    tClass=[]
    f=open("NegativeTrain.csv")
    csv_f=csv.reader(f)
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        if len(new_list)!=5:
            print("ERROR")
            continue
        tNegativeList.append(new_list)
        tClass.append(0)

    tClass.append(1)
    tNegativeList.append(new_list)
    
    f = open('PredictionsNeg.csv', 'w')
    writer = csv.writer(f)
    writer.writerow('FH')
    for data in tNegativeList:
        prediction = analyzeData([data])
        writer.writerow(prediction)

    f.close()
def PrintFogPrediction():
    f=open("FogTrain.csv")
    csv_f= csv.reader(f)
    tFogList=[]
    tFogClass=[]
    counter=0
    
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            exit(2)
            continue
            
        tFogClass.append(1)
        tFogList.append(new_list)

    f = open('FogPredictions.csv', 'w')
    FogWriter = csv.writer(f)
    FogWriter.writerow('FH')
    for fog in tFogList:
        print("FOG DATA: ")
        print([fog])
        print(type(fog))
        prediction = analyzeData([fog])
        print(prediction)
        FogWriter.writerow(prediction)
    f.close()

def PrintHazePrediction():
    f = open("HazeTrain.csv")
    csv_f = csv.reader(f)
    tHazeList=[]
    tClass=[]
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        print(new_list)
        if len(new_list)!=5:
            print("ERROR")
            continue
        tHazeList.append(new_list)
        tClass.append(1)
    f.close()
   
    f = open('HazePredictions.csv', 'w')
    HazeWriter = csv.writer(f)
    HazeWriter.writerow('FH')
    for haze in tHazeList:
        prediction = analyzeData([haze])
        print(prediction)
        HazeWriter.writerow(prediction)
    f.close()
    
def main():
    PrintFogPrediction()
    PrintHazePrediction()
    PrintNegativePrediction()

if __name__ == "__main__":
    PrintFogPrediction()
