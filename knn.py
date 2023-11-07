import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix, precision_recall_fscore_support, classification_report
from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import os 
import time
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
## Result section saved files
# print('Default Parameters: ',GaussianNB().get_params())
accuracyFile= open("Result/accuracy.txt","w")
Cross_valFile= open("Result/cross_val.txt","w")
Cross_valFile_10_Fold= open("Result/10Fold_cross.txt","w")
precisionFile= open("Result/precision.txt","w")
recallFile= open("Result/recall.txt","w")
f1File= open("Result/f1.txt","w")
tuningParameter= open("Result/tuning.txt","w")


Directory= "/media/shahan/New Volume/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset_BSL_Bangla"
Catagory= os.listdir(Directory)
total_Dataset=len(Catagory)

# for i in range(0,total_Dataset):
path= os.path.join(Directory,Catagory[total_Dataset-1])
# path= os.path.join(Directory,Catagory[i])
dataset= pd.read_csv(path)


# shuffle the dataset
dataset=dataset.sample(frac=True)
## split the data into featurs and target
X= dataset.iloc[:,:-1].values
# print(X)

Y= dataset.iloc[:,-1:].values.ravel()


## split traing & testing
x_train, x_test, y_train, y_test=train_test_split(X,Y,random_state=10,test_size=0.2)



############ Number of each Alphabet after spleating ###########
# count_class= pd.value_counts(y_test, sort=True)
# print(count_class)
# # col=["Red","Green","Blue","Orange","Magenta","Yellow","Black","Purple","Orange","LightGreen","Gray","LightBlue","LightRed","LightGreen","DarkBlue","DarkRed","DarkGreen", "DarkBlue","DarkRed","DarkGreen","DarkBlue","DarkRed","DarkGreen""DarkBlue","DarkRed","DarkGreen"]
# col=["b","c","g","m","k","lightpink","r","y","forestgreen","slategrey","bisque","royalblue","lime","darkorange","indigo","cyan","violet","olive","dodgerblue","crimson","gold","maroon","navy","tan","teal","tomato"]
# count_class.plot(kind="bar",color=col)
# # plt.title("Bar Chart")
# plt.show()

# dataset.plot(kind="kde",color=col)
# plt.show()


## Parameter
s_Parameter=time.time()
n_neighbour=np.arange(3,100,2)
grid_params = { 'n_neighbors' :n_neighbour,
            'weights' : ['uniform','distance'],
            'metric' : ['minkowski','euclidean','manhattan'],
            'algorithm' : ['auto','ball_tree','kd_tree','brute'],
            }

gs = GridSearchCV(KNeighborsClassifier(), grid_params, verbose = 1, cv=10, n_jobs = -1)
g_res = gs.fit(x_train, y_train)
print("Optimized Best Score = ", g_res.best_score_)
print("Optimized Best Parameters = ", g_res.best_params_)
t_parameter=str(g_res.best_score_) + "," + str(g_res.best_params_)
tuningParameter.write(str(t_parameter)+",")
tuningParameter.write("------")



#### Model training

# Gausian Naive base instance
e_Parameter=time.time()
call_knn= KNeighborsClassifier(n_neighbors=g_res.best_params_['n_neighbors'],weights=g_res.best_params_['weights'], metric=g_res.best_params_['metric'],algorithm=g_res.best_params_['algorithm'])

# fit the model
model_knn= call_knn.fit(x_train,y_train)

'''
e_fit=time.time()
# predict from the model
prediction= model_knn.predict(x_test)
p_fit=time.time()

## Evaluating based on prediction & ytest
# print("Prediction = ",prediction)
# print("Y Test     = ",y_test)

################################# Accuracy   ########################################
# accuracy= accuracy_score(y_test,prediction)
# print("Accuracy = ",accuracy)
# accuracyFile.write(str(accuracy)+",")

# # ################################# 10 Fold Cross   ########################################
cross_val=cross_val_score(model_knn, X, Y,cv=10)
# print(cross_val)
sum_cross_val= cross_val.sum()
cv=sum_cross_val/10
print("Cross Validation= ",cv)
Cross_valFile_10_Fold.write(str(cv)+",")


# ########################## Confussion Matrix ############################# 
cm_result=confusion_matrix(y_test,prediction)

print(cm_result)
fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens,class_names=model_knn.classes_)
# fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens)
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
# plt.savefig("cm.png")
plt.show()


# # ############ Presition, Recall, F1 ####################
precision,recall,f1,support=precision_recall_fscore_support(y_test,prediction, average="weighted")
print("Prec Recall F1 Supppor= ",precision_recall_fscore_support(y_test,prediction, average="weighted"))
precisionFile.write(str(precision)+",")
recallFile.write(str(recall)+",")
f1File.write(str(f1)+",")



########### Classification Report ########### 
# # print("Classification Report: ", classification_report(y_test, y_pred=prediction))
print("-------Time complexity--------")
print("Hyper-perameter: ",(e_Parameter-s_Parameter))
print("Fit: ",(e_fit-e_Parameter))
print("predict: ",(p_fit-e_fit))
'''



## save model
#=============== Save model #############

# Pkl_Filename = "model/KNN_model_Bangla.pkl"  

# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(model_knn, file)