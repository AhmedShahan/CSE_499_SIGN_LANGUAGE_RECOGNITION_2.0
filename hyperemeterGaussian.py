import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix, precision_recall_fscore_support, classification_report
import os 
import time
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
import seaborn as sns
import numpy as np
## Result section saved files
# print('Default Parameters: ',GaussianNB().get_params())
accuracyFile= open("Result/accuracy.txt","w")
Cross_valFile= open("Result/cross_val.txt","w")
Cross_valFile_10_Fold= open("Result/10Fold_cross.txt","w")
precisionFile= open("Result/precision.txt","w")
recallFile= open("Result/recall.txt","w")
f1File= open("Result/f1.txt","w")


Directory= "/media/shahan/New Volume/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset_BSL_English"
Catagory= os.listdir(Directory)
total_Dataset=len(Catagory)
# for i in range(0,total_Dataset):
path= os.path.join(Directory,Catagory[total_Dataset-1])
dataset= pd.read_csv(path)


# shuffle the dataset
dataset=dataset.sample(frac=True)
## split the data into featurs and target
X= dataset.iloc[:,:-1].values
# print(X)

Y= dataset.iloc[:,-1:].values.ravel()
# print(Y)
# pd.DataFrame.hist(Y)
# pd.DataFrame.plot(kind='hist')
# # pd.DataFrame.plot.hist()
# plt.show()
# dataset.plot(kind='hist',
#         alpha=0.7,
#         bins=30,
#         title='Histogram Of Test Scores',
#         rot=45,
#         grid=True,
#         figsize=(12,8),
#         fontsize=15)
# plt.show()

# ## split traing & testing
x_train, x_test, y_train, y_test=train_test_split(X,Y,random_state=10,test_size=0.2)


# ########### Hyperperemeter ################
# import numpy as np
# from sklearn.model_selection import RepeatedStratifiedKFold


# np.logspace(0,-9, num=10)

# NVG=GaussianNB()
# cv_method = RepeatedStratifiedKFold(n_splits=5, 
#                                     n_repeats=3, 
#                                     random_state=999)

# from sklearn.preprocessing import PowerTransformer
# params_NB = {'var_smoothing': np.logspace(0,-9, num=100)}

# gs_NB = GridSearchCV(estimator=NVG, 
#                      param_grid=params_NB, 
#                      cv=cv_method,
#                      verbose=1, 
#                      scoring='accuracy')

# Data_transformed = PowerTransformer().fit_transform(x_test)

# gs_NB.fit(Data_transformed, y_test)

# print("Best Parameters: ",gs_NB.best_params_)
# print("Best Score ",gs_NB.best_score_)


# results_NB = pd.DataFrame(gs_NB.cv_results_['params'])
# results_NB['test_score'] = gs_NB.cv_results_['mean_test_score']

# plt.plot(results_NB['var_smoothing'], results_NB['test_score'], marker = '.')    
# plt.xlabel('Var. Smoothing')
# plt.ylabel("Mean CV Score")
# plt.title("NB Performance Comparison")
# plt.show()

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






### Model training

# Gausian Naive base instance
e_Parameter=time.time()
GausianNb= GaussianNB()

# fit the model
model_GaussianNB= GausianNb.fit(x_train,y_train)
e_fit=time.time()
# predict from the model
predictionOnTest= model_GaussianNB.predict(x_test)
predictionOnTrain= model_GaussianNB.predict(x_train)


p_fit=time.time()

# Evaluating based on prediction & ytest
# print("Prediction = ",prediction)
# print("Y Test     = ",y_test)







################################# Accuracy   ########################################
accuracyOnTrain= accuracy_score(y_train,predictionOnTrain)
accuracyOnTest= accuracy_score(y_test,predictionOnTest)


print("Training Accuracy = ",accuracyOnTrain)
print("Testing Accuracy = ",accuracyOnTest)

# accuracyFile.write(str(accuracy)+",")


############# Plot Confusion Matrix on Training and Testing ####
# f,a =  plt.subplots(1,2,sharex=True,sharey=True,squeeze=False)

# #Plotting confusion matrix for the different models for the Training Data

# plot_0 = sns.heatmap((metrics.confusion_matrix(y_train,predictionOnTrain)),annot=True,fmt='.5g',cmap="YlGn",ax=a[0][0]);
# a[0][0].set_title('Training Data')
# plot_1 = sns.heatmap((metrics.confusion_matrix(y_test,predictionOnTest)),annot=True,fmt='.5g',cmap="YlGn",ax=a[0][1]);
# a[0][1].set_title('Test Data')
# # plt.show()



############# Training and testing graph ############
# train_accuracy = []
# test_accuracy = []
# num_epochs=100
# # Training loop (for example, in the context of epochs in deep learning)
# for epoch in range(num_epochs):
#     x_train, x_test, y_train, y_test=train_test_split(X,Y,random_state=epoch,test_size=0.2)    
#     model_GaussianNB.fit(x_train, y_train)
    
#     # Calculate training accuracy and append to the list
#     y_train_pred = model_GaussianNB.predict(x_train)
#     train_acc = accuracy_score(y_train, y_train_pred)
#     train_accuracy.append(train_acc)
    
#     # Calculate testing accuracy and append to the list
#     y_test_pred = model_GaussianNB.predict(x_test)
#     test_acc = accuracy_score(y_test, y_test_pred)
#     test_accuracy.append(test_acc)

# # Create the accuracy graphs
# epochs = range(1, num_epochs + 1)
# plt.plot(epochs, train_accuracy, label='Training Accuracy')
# plt.plot(epochs, test_accuracy, label='Testing Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.show()


# # ################################# 10 Fold Cross   ########################################
cross_val=cross_val_score(model_GaussianNB, X, Y,cv=10)
# print(cross_val)
sum_cross_val= cross_val.sum()
cv=sum_cross_val/10
# print(cv)
# Cross_valFile_10_Fold.write(str(cv)+",")


# # ########################## Confussion Matrix ############################# 
# cm_result=confusion_matrix(y_test,prediction)

# print(cm_result)
# fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens,class_names=model_GaussianNB.classes_)
# # fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens)
# plt.xlabel('Predictions', fontsize=18)
# plt.ylabel('Actuals', fontsize=18)
# plt.title('Confusion Matrix', fontsize=18)
# plt.savefig("cm.png")
# plt.show()

# # fig, ax = plot_confusion_matrix(conf_mat=cm_result,
# #                                 show_absolute=True,
# #                                 show_normed=True,
# #                                 colorbar=True)
# # # plt.show
# # # fig.plot()
# # ax.plot()
# # ax.show()





# # ############ Presition, Recall, F1 ####################
# precision,recall,f1,support=precision_recall_fscore_support(y_test,prediction, average="weighted")
# print("Prec Recall F1 Supppor= ",precision_recall_fscore_support(y_test,prediction, average="weighted"))
# precisionFile.write(str(precision)+",")
# recallFile.write(str(recall)+",")
# f1File.write(str(f1)+",")



########### Classification Report ########### 
# print("Classification Report: ", classification_report(y_test, y_pred=prediction))
print("-------Time complexity--------")
# print("Hyper-perameter: ",(e_Parameter-s_Parameter))
print("Fit: ",(e_fit-e_Parameter))
print("predict: ",(p_fit-e_fit))
