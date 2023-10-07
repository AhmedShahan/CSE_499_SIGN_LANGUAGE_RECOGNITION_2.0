import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix, precision_recall_fscore_support, classification_report
# import matplotlib.pyplot as plt
import os 
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import GridSearchCV
## Result section saved files

accuracyFile= open("Result/accuracy.txt","w")
Cross_valFile= open("Result/cross_val.txt","w")
Cross_valFile_10_Fold= open("Result/10Fold_cross.txt","w")
precisionFile= open("Result/precision.txt","w")
recallFile= open("Result/recall.txt","w")
f1File= open("Result/f1.txt","w")
tuningParameter= open("Result/tuning.txt","w")


Directory= "/media/shahan/New Volume1/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset"
Catagory= os.listdir(Directory)

total_Dataset=len(Catagory)
for i in range(0,total_Dataset):
    path= os.path.join(Directory,Catagory[total_Dataset-1])
    # path= os.path.join(Directory,Catagory[total_Dataset-1])
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
    param_grid = {'C': [0.1, 1, 10, 100, 1000], 
                'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
                'kernel': ('linear', 'poly', 'rbf', 'sigmoid')}

    

    # param_grid={'C': [0.1, 1, 10, 100, 1000],
    #                         'gamma': [1, 0.1, 0.01, 0.001, 0.0001, 1.1],
    #                         'kernel': ('linear', 'poly', 'rbf', 'sigmoid')}
    gs = GridSearchCV(SVC(), param_grid, verbose = 1, cv=10, n_jobs = -1)
    g_res = gs.fit(x_train, y_train)

    print("Optimized Best Score = ", g_res.best_score_)
    print("Optimized Best Parameters = ", g_res.best_params_)
    t_parameter=str(g_res.best_score_) + "," + str(g_res.best_params_)
    tuningParameter.write(str(t_parameter)+",")
    tuningParameter.write("------")



    #### Model training
    call_svm = svm.SVC(kernel=g_res.best_params_["kernel"], C=g_res.best_params_["C"],gamma=g_res.best_params_["gamma"],probability=True)
    # Gausian Naive base instance


    # fit the model
    model_svm= call_svm.fit(x_train,y_train)
    # e_fit=time.time()
    # predict from the model
    prediction= model_svm.predict(x_test)
    # p_fit=time.time()

    ## Evaluating based on prediction & ytest
    # print("Prediction = ",prediction)
    # print("Y Test     = ",y_test)

    ################################# Accuracy   ########################################
    accuracy= accuracy_score(y_test,prediction)
    print("Accuracy = ",accuracy)
    accuracyFile.write(str(accuracy)+",")


    # # ################################# Cross Validation   ########################################
    # for i in range (4,13):
    #     cross_val=cross_val_score(model_GaussianNB, X, Y,cv=i)
    #     # print(cross_val)
    #     sum_cross_val= cross_val.sum()
    #     cv=sum_cross_val/i
    #     # print(cv)
    #     Cross_valFile.write(str(cv)+",")
    #     # print(cross_val)
    # # Cross_valFile.write("\n")


    # # ################################# 10 Fold Cross   ########################################
    cross_val=cross_val_score(model_svm, X, Y,cv=10)
    # print(cross_val)
    sum_cross_val= cross_val.sum()
    cv=sum_cross_val/10
    print("10 Fold Cross validation",cv)
    Cross_valFile_10_Fold.write(str(cv)+",")


    # # ########################## Confussion Matrix ############################# 
    # cm_result=confusion_matrix(y_test,prediction)

    # print(cm_result)
    # fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens,class_names=model_svm.classes_)
    # # fig, ax = plot_confusion_matrix(conf_mat=cm_result,cmap=plt.cm.Greens)
    # plt.xlabel('Predictions', fontsize=18)
    # plt.ylabel('Actuals', fontsize=18)
    # plt.title('Confusion Matrix', fontsize=18)
    # # plt.savefig("cm.png")
    # plt.show()


    # # ############ Presition, Recall, F1 ####################
    precision,recall,f1,support=precision_recall_fscore_support(y_test,prediction, average="weighted")
    print("Prec Recall F1 Supppor= ",precision_recall_fscore_support(y_test,prediction, average="weighted"))
    precisionFile.write(str(precision)+",")
    recallFile.write(str(recall)+",")
    f1File.write(str(f1)+",")



    ########### Classification Report ########### 
    # # print("Classification Report: ", classification_report(y_test, y_pred=prediction))
    # print("-------Time complexity--------")
    # # print("Hyper-perameter: ",(e_Parameter-s_Parameter))
    # print("Fit: ",(e_fit-e_Parameter))
    # print("predict: ",(p_fit-e_fit))