import matplotlib.pyplot as plt
import panda as pd 

df=pd.read_excel('Corona Cases.xlsx')
plt.plot(day,corona_cases)
plt.margins(x=0,y=0)
plt.axis([0,12,0,100])
plt.xlabel("State")
plt.ylabel("corona case reported")
plt.title("State-wise Corona cases reported till June 30,2022")
plt.show()