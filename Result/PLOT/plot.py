
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
accuracy=[0.9754768392370572,0.9727520435967303,0.9713896457765667]
cross_val=[0.9776490852934188,0.988539439296745,0.9751991483152425]
precision=[0.9771369385009392,0.9763432877072883,0.9723260263602204]
recall=[0.9754768392370572,0.9727520435967303,0.9713896457765667]
f1_score=[0.9751007958788537,0.9728886092661331,0.9708952220817667]

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