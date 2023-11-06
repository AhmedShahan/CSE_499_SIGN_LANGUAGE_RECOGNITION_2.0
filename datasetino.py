import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
# # Load the dataset

# dataset= pd.read_csv("/media/shahan/New Volume/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset/c4.csv")
Directory= "/media/shahan/New Volume2/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset_BSL_English"
Catagory= os.listdir(Directory)
total_Dataset=len(Catagory)
# for i in range(0,total_Dataset+1):
path= os.path.join(Directory,Catagory[12])
dataset= pd.read_csv(path)
# # shape of dataset
# print("The Shape of Dataset (Row,Column)= ",dataset.shape)

# # Title of the dataset/ column title
# print("Title of the dataset: ", dataset.columns)


# # Target Class
# Target_class= pd.value_counts(dataset["Alphabet"], sort=False)
# print("Target Class: ", Target_class)

### Target class based Bar plot
# Color for 26 Bar, 26 color
col=["b","c","g","m","k","lightpink","r","y","forestgreen","slategrey","bisque","royalblue","lime","darkorange","indigo","cyan","violet","olive","dodgerblue","crimson","gold","maroon","navy","tan","teal","tomato"]

# Target_class.plot(kind="bar",color=col)
# plt.title("Dataset Target Information")
# plt.show()

# sns.scatterplot(x = 'radius_worst', y = 'texture_worst', data = dataset)
for i in range (1,4):
    
#     # sns.kdeplot(x =f'F{i}', data = dataset,linewidth=3, color="red")
#     sns.boxplot(y =f'F{i}', data = dataset); 
    # sns.histplot(x = f'F{i}', data = dataset)
    # plt.figure(figsize=(1,2))
    # plt.savefig(f'figure/kde_plot{i}.png')
    # sns.histplot(x = f'F{i}', data =dataset, stat = 'probability', fill = False, element = 'step', cumulative = True);
    sns.histplot(data =dataset, stat = 'probability', fill = False, element = 'step', cumulative = True);

    plt.show()
# sns.boxplot(data = dataset); 
# sns.histplot(data =dataset)

# plt.show()
# print(dataset.isnull().sum())
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os 
import time
## Result section saved files
# print('Default Parameters: ',GaussianNB().get_params())
# accuracyFile= open("Result/accuracy.txt","w")
# Cross_valFile= open("Result/cross_val.txt","w")
# Cross_valFile_10_Fold= open("Result/10Fold_cross.txt","w")
# precisionFile= open("Result/precision.txt","w")
# recallFile= open("Result/recall.txt","w")
# f1File= open("Result/f1.txt","w")


# Directory= "/media/shahan/New Volume2/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset_BSL_Bangla"
# Catagory= os.listdir(Directory)
# total_Dataset=len(Catagory)
# for i in range(0,total_Dataset+1):
#         path= os.path.join(Directory,Catagory[i])
#         dataset= pd.read_csv(path)


#         # shuffle the dataset
#         dataset=dataset.sample(frac=True)
#         ## split the data into featurs and target
#         X= dataset.iloc[:,:-1].values
#         # print(X)

#         Y= dataset.iloc[:,-1:].values.ravel()


#         # print(Y)
#         pd.DataFrame.hist(Y)
#         # pd.DataFrame.plot(kind='hist')
#         # pd.DataFrame.plot.hist()
#         plt.show()
#         # dataset.plot(kind='hist',
#         #         alpha=0.7,
#         #         bins=30,
#         #         title='Histogram Of Test Scores',
#         #         rot=45,
#         #         grid=True,
#         #         figsize=(12,8),
#         #         fontsize=15)
#         # plt.show()
'''