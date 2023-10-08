
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
accuracy=[0.9727520435967303,0.9863760217983651,0.9659400544959128]
cross_val=[0.9820147303397482,0.9858220479923971,0.9732910468873304]
precision=[0.9751873542745478,0.9883742052679382,0.9683302531248178]
recall=[0.9727520435967303,0.9863760217983651,0.9659400544959128]
f1_score=[0.9719531136705364,0.9864641528133989,0.9659874619187573]

# print(len(accuracy))
# print(len(precision))
# print(len(recall))
# print(len(cross_val))
# print(len(f1_score))

### COMBINED ALL ACCURACY MATRICES

xaxis= []
for i in range(1,3):
    xaxis.append("P"+str(i))

for i in range(2,3):
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