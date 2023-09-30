
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
accuracy=[0.9495412844036697,0.9472477064220184,0.9311926605504587,0.9472477064220184,0.9541284403669725,0.9357798165137615,0.9518348623853211]
cross_val=[0.9481418847503488,0.9490508603559802,0.9508962922250876,0.9472244535576883,0.9485963725531645,0.9444721599797065,0.9495159176425823]
precision=[0.9589857952068762,0.958038895692363,0.9439925189397225,0.9528842220872183,0.9619645925669941,0.9454621287634246,0.9580510844146195]
recall=[0.9495412844036697,0.9472477064220184,0.9311926605504587,0.9472477064220184,0.9541284403669725,0.9357798165137615,0.9518348623853211]
f1_score=[0.9589857952068762,0.958038895692363,0.9439925189397225,0.9528842220872183,0.9619645925669941,0.9454621287634246,0.9580510844146195]

# print(len(accuracy))
# print(len(precision))
# print(len(recall))
# print(len(cross_val))
# print(len(f1_score))

### COMBINED ALL ACCURACY MATRICES

xaxis= []
for i in range(1,5):
    xaxis.append("P"+str(i))

for i in range(2,5):
    xaxis.append("C"+str(i))

plt.plot(xaxis, accuracy, linewidth=2.5)
plt.plot(xaxis, cross_val, linewidth=2.5)
plt.plot(xaxis, precision, linewidth=2.5)
plt.plot(xaxis, recall, linewidth=2.5)
plt.plot(xaxis, f1_score, linewidth=2.5)
plt.grid()
plt.legend(["Accuracy", "Cross Validation","precision", "Recall", "F1_Score"])
plt.show()

# xaxis= []
# for i in range(1,5):
#     xaxis.append("P"+str(i))

# for i in range(2,5):
#     xaxis.append("C"+str(i))
# # plt.plot(xaxis, accuracy, linewidth=2.5)
# # plt.plot(xaxis, cross_val, linewidth=2.5, color="g")
# # plt.plot(xaxis, precision, linewidth=2.5, color="b")
# # plt.plot(xaxis, recall, linewidth=2.5, color="y")
# plt.plot(xaxis, f1_score, linewidth=2.5, color="m")
# plt.grid()
# # plt.legend(["Accuracy"])
# # plt.legend(["Cross Validation"])
# # plt.legend(["precision"])
# # plt.legend(["Recall"])
# plt.legend(["F1_Score"])
plt.show()