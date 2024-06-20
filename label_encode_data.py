import os 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#I create a class to encode the data, cause the column Item is a string and I need to convert it to a number
#some algorithms such as naive bayes can't work good with strings, so I need to convert it to a number
class EncodeData():
    def __init__(self):
        #import the data
        #NOISE
        #self.file_name='Satisfaction_noise_short.csv'

        #NOT NOISE
        self.file_name='Satisfaction_noise_short.csv'
        self.path=os.path.join(".","Data",self.file_name)
        #read the data
    def read_data(self):
        df=pd.read_csv(self.path)
        return df

#this function encode the data and return the encoded data
    def LabelEncodeData(self):
        self.encode=LabelEncoder()
        self.df=self.read_data()
        self.encoded_items={}
        self.items=["Items"]
#as you can see i use the LabelEncoder from sklearn to encode the data
        for item in self.items:
            self.df[item]=self.encode.fit_transform(self.df[item])
            #I create a dictionary to save the encoded data, i concatebate the classes with the encoded classes
            encoded_item=dict(zip(self.encode.classes_,self.encode.transform(self.encode.classes_)))
            self.encoded_items[item]=encoded_item

#then i export the dataset with the column Items encoded
#so besisdes the file Satisfaction.csv,you will see the file Satisfaction_encoded.csv
    def ExportEncodedData(self):
        self.LabelEncodeData()
        #NOISE
        self.df.to_csv(os.path.join(".","Data","Satisfaction_noise_encoded_short.csv"),index=False)
        #NOT NOISE
        #self.df.to_csv(os.path.join(".","Data","Satisfaction_ notNoise_encoded_short.csv"),index=False)
        return self.df

#in oreder to visualize the encoded data, i create a function to print the encoded data
#this  function will print the encoded data in a file called Items_encoded_items.csv
    def PrintEncodedData(self):
        self.LabelEncodeData()
        encoded_df=pd.DataFrame()
        for key,value in self.encoded_items.items():
            temp_df=pd.DataFrame.from_dict({key:value},orient='index').transpose()
            encoded_df=pd.concat([encoded_df,temp_df])
        encoded_df.to_csv(os.path.join(".","Data","Items_encoded_items.csv"))
            
        

export=EncodeData()
export.ExportEncodedData()
export.PrintEncodedData()
