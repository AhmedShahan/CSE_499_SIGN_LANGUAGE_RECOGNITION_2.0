import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
dataset= pd.read_csv("/media/shahan/New Volume/CSE_499_SIGN_LANGUAGE_RECOGNITION_2.0/Dataset/c4.csv")

# shape of dataset
print("The Shape of Dataset (Row,Column)= ",dataset.shape)

# Title of the dataset/ column title
print("Title of the dataset: ", dataset.columns)


# Target Class
Target_class= pd.value_counts(dataset["Alphabet"], sort=False)
print("Target Class: ", Target_class)

### Target class based Bar plot
# Color for 26 Bar, 26 color
col=["b","c","g","m","k","lightpink","r","y","forestgreen","slategrey","bisque","royalblue","lime","darkorange","indigo","cyan","violet","olive","dodgerblue","crimson","gold","maroon","navy","tan","teal","tomato"]

Target_class.plot(kind="bar",color=col)
plt.title("Dataset Target Information")
plt.show()