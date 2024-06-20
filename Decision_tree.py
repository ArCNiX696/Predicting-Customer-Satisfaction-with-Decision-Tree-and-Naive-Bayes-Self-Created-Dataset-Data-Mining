import os 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score,classification_report,precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


class DecisionTree():
    def __init__(self):
        #firts i import the data, in this case i use the encoded data
        #NOT NOISE
        #self.file_name='Satisfaction_ notNoise_encoded.csv'
        #NOISE
        self.file_name='Satisfaction_noise_encoded.csv'
        self.path=os.path.join(".","Data",self.file_name)
        self.df=pd.read_csv(self.path)


    #then i split the data in x and y
    def SplitData(self):
        self.X=self.df.drop('Satisfaction',axis=1)#i drop the column Satisfaction cause is the feature that i want to predict
        
        #THIS LINE DROPS ALL THE REDUNDANT AND NOSIE FEATURES AND THE FEATURE WE WANT TO PREDICT      
        #NOISE
        #self.X=self.df.drop(['Satisfaction',"Hungry?","Payment Method","Cashier Gender","Weather","Cashier Mood"],axis=1)
        #NOT NOISE
        #self.X=self.df.drop(['Satisfaction',"Hungry?","Payment Method","Cashier Gender"],axis=1)
        self.y=self.df['Satisfaction']#then i create a variable y with the feature that i want to predict
        print(self.X)
        #then i split the data in train and test
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.3,random_state=42)   
        

    def TrainModel(self):
        #create the model object
        #self.DecisionTreeMdl=DecisionTreeClassifier(max_depth=23, min_samples_split=2, min_samples_leaf=2)
        self.DecisionTreeMdl=DecisionTreeClassifier()

        #train the model
        self.DecisionTreeMdl.fit(self.X_train,self.y_train)


    def EvaluateModel(self):
        #make the predictions
        self.y_pred=self.DecisionTreeMdl.predict(self.X_test)
        self.accuracy=accuracy_score(self.y_test,self.y_pred)
        self.precision,self.recall,self.f1_score,self.support=precision_recall_fscore_support(self.y_test,self.y_pred)

    #this is a code to visualize a confusion matrix
    def PlotConfusionMatrix(self):
        cm = confusion_matrix(self.y_test, self.y_pred)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot(ax=ax, cmap='Blues')
        
        ax.set_title('Decision Tree Confusion Matrix')
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('True Label')

        plt.show()

    #this is a code to visualize the data frame
    def VisualizeDataFrame(self):
        fig, ax = plt.subplots(figsize=(15, 15)) 
        ax.axis('off')
        table_s=ax.table(cellText=self.df.head(15).values, colLabels=self.df.columns, cellLoc='center', loc='center')
        table_s.scale(1.2, 2.5)
        plt.show()
