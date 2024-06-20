import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from Naive_bayes import NaiveBayes
from Decision_tree import DecisionTree


#Code to activate Naive Bayes algorithm

Naive_bayes=NaiveBayes()
#Naive_bayes.VisualizeDataFrame()
Naive_bayes.SplitData()
Naive_bayes.TrainModel()
Naive_bayes.EvaluateModel()
Naive_bayes.PlotConfusionMatrix()

classes=['Unsatisfied','Satisfied']
precision=Naive_bayes.precision
recall=Naive_bayes.recall
f1_score=Naive_bayes.f1_score
accuracy=Naive_bayes.accuracy
support=Naive_bayes.support

#create grafics to visualize the results

fig,axes=plt.subplots(1,4,figsize=(15,6))

#plot the precision
axes[0].bar(classes,precision,color="blue")
axes[0].set_title("Precision by class")
axes[0].set_xlabel("Classes")
axes[0].set_ylabel("Precision")
axes[0].set_ylim([0,1])

#plot the recall
axes[1].bar(classes,recall,color="red")
axes[1].set_title("Recall by class")
axes[1].set_xlabel("Classes")
axes[1].set_ylabel("Recall")
axes[1].set_ylim([0,1])

#plot the F1 score
axes[2].bar(classes,f1_score,color="green")
axes[2].set_title("F1 score by class")
axes[2].set_xlabel("Classes")
axes[2].set_ylabel("F1 score")
axes[2].set_ylim([0,1])

#plot the support
axes[3].bar(classes,support,color="pink")
axes[3].set_title("Support by class")
axes[3].set_xlabel("Classes")
axes[3].set_ylabel("Support")
axes[3].set_ylim([0,300])


#show grafics
plt.tight_layout()
plt.show()

#print the accuracy
print(f'Overall Model Accuracy: {accuracy}')


#Code to activate Decision Tree algorithm

Decision_tree=DecisionTree()
#Decision_tree.VisualizeDataFrame()
Decision_tree.SplitData()
Decision_tree.TrainModel()
Decision_tree.EvaluateModel()
Decision_tree.PlotConfusionMatrix()

classes=['Unsatisfied','Satisfied']
precision=Decision_tree.precision
recall=Decision_tree.recall
f1_score=Decision_tree.f1_score
accuracy=Decision_tree.accuracy
support=Decision_tree.support

#Visualize the tree
plt.figure(figsize=(10,10))
plot_tree(Decision_tree.DecisionTreeMdl,
            feature_names=Decision_tree.X.columns,
            class_names=classes,
            filled=True,
            rounded=True,
            fontsize=14)

plt.show()

#plot the tree
fig,axes=plt.subplots(1,4,figsize=(15,6))

#plot the precision
axes[0].bar(classes,precision,color="blue")
axes[0].set_title("Precision by class")
axes[0].set_xlabel("Classes")
axes[0].set_ylabel("Precision")
axes[0].set_ylim([0,1])

#plot the recall
axes[1].bar(classes,recall,color="red")
axes[1].set_title("Recall by class")
axes[1].set_xlabel("Classes")
axes[1].set_ylabel("Recall")
axes[1].set_ylim([0,1])

#plot the F1 score
axes[2].bar(classes,f1_score,color="green")
axes[2].set_title("F1 score by class")
axes[2].set_xlabel("Classes")
axes[2].set_ylabel("F1 score")
axes[2].set_ylim([0,1])

#plot the support
axes[3].bar(classes,support,color="pink")
axes[3].set_title("Support by class")
axes[3].set_xlabel("Classes")
axes[3].set_ylabel("Support")
axes[3].set_ylim([0,300])

#show grafics
plt.tight_layout()
plt.show()


print(f'Accuaracy: {Decision_tree.accuracy}')
