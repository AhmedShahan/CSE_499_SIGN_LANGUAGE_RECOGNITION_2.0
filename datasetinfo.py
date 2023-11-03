import pandas as pd
import os
Directory= "/media/shahan/New Volume2/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset_BSL_Bangla"
Catagory= os.listdir(Directory)
total_Dataset=len(Catagory)
# for i in range(0,total_Dataset+1):
path= os.path.join(Directory,Catagory[0])
dataset= pd.read_csv(path)

print(dataset.info())