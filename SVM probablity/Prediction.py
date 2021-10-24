from sklearn import svm
import joblib
import numpy as np
import csv


def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        return False
    return True


#this function opens and reads positivehaze.csv & positivefog.csv files 
#stores the appropriate information from the data into tList, tClass [haze] & tFogList, tFogClass [fog]
#the tList & tFogList are used by the analyseData function
def PrintPredictionPositive():
    
    #opens and reads positivehaze.csv and stores appropriate data into tList & tClass
    f = open("HazeTrain.csv")
    csv_f = csv.reader(f)
    tList=[]
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
        if len(new_list)!=5:
            print("ERROR")
            continue
        tList.append(new_list)
        tClass.append(1)
    f.close()
   
    #opens and reads positiveFog.csv and stores appropriate data into tFogList & tFogClass
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
        if len(new_list)!=5:
            exit(2)
            continue
            
        tFogClass.append(1)
        tFogList.append(new_list)
    

    f.close()
    '''
    f = open('Predictions.csv', 'w')
    writer = csv.writer(f)
    '''
    
    #tList & tFogList are transfered to the analyseData function
    analyzeData(tList, tFogList)




def analyzeData(tList, tFogList):

    #the data from pickle files are extracted
    svmFog = joblib.load('svmFog.pkl')
    svmHaze = joblib.load('svmHaze.pkl')
    



    #the inputed data is used as a parameter for predict() function
    fog_predict = svmFog.predict(tFogList)
    haze_predict = svmHaze.predict(tList)
    
   



    #the predict_proba() function is used for haze data (svmHaze) and haze list (tList)
    haze_probablility = svmHaze.predict_proba(tList)
    
    #each value from haze_probablility list is looped through
    # prob = each value from the list being looped through (a list with probability of 0 & probability of 1 [probability of 0, probability of 1])
    # num = numbering of each looped value to reference location      
    for num, prob in enumerate(haze_probablility):

        #for each value in the haze_probability list
        #'Haze' string is printed
        #the value at location '1' in the prob list is printed (probability of 1)
        #the numerical location (num) is used to access the value from the haze_predict list in that location 
        pass
        print('Haze')
        input(prob)
        input(haze_predict[num])

    



    
    #the predict_proba() function is used for fog data (svmFog) and haze list (tFogList)
    fog_probability = svmFog.predict_proba(tFogList)

    #each value from fog_probablility list is looped through
    # prob2 = each value from the list being looped through (a list with probability of 0 & probability of 1 [probability of 0, probability of 1])
    # num2 = numbering of each looped value to reference location
    for num2, prob2 in enumerate(fog_probability):
        
        #for each value in the fog_probability list
        #'Fog' string is printed
        #the value at location '1' in the prob list is printed (probability of 1)
        #the numerical location (num) is used to access the value from the fog_predict list in that location
        if(int(fog_predict[num2]) == 1):
            print('Fog')
            print(prob2[1])
            input(fog_predict[num2])
        
    
    
    

    
    #the haze_predict list is looped through 
    #for each 1 value, counter variable is incremented 
    #the final value of counter variable is the number of 1s in haze_predict
    counter = 0
    for haze in haze_predict:
        #input(haze)
        
        if(str(haze) == '1'):
            counter += 1

    #the length of haze_predict is defined in haze_len variable
    haze_len = len(haze_predict)

    #input(fog_len)
    
    #value_haze variable is the percentage of 1s in haze data
    value_haze = counter/haze_len
    
    print('haze')
    print(haze_predict)
    input(value_haze*100)

    
    #the fog_predict list is looped through 
    #for each 1 value, counter variable is incremented 
    #the final value of counter variable is the number of 1s in fog_predict
    counter2 = 0
    for fog in fog_predict:
        #input(fog)
        
        if(str(fog) == '1'):
            counter2 += 1
    
    #the length of fog_predict is defined in fog_len variable
    fog_len = len(fog_predict)
    
    #value_fog variable is the percentage of 1s in fog data
    value_fog = counter2/fog_len
    
    
    print('fog')
    print(fog_predict)
    input(value_fog*100)
    
    
    
        
    


#the main code where the PrintPredictionPositive() is ran
if __name__ == "__main__":
    PrintPredictionPositive()
