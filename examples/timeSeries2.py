import pyjoyplot as pjp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joypy


df = pd.read_csv('RevData/sample/MyoData1515714132.65.csv')

unit1 = [] 
unit2 = []
unit3 = []
unit4 = []
unit5 = []
unit6 = []
unit7 = []
unit8 = []
index = []

combine = []

for a in range(len(df.values)):
	if(a%5 == 0):
		combine.append(['Unit 1', df.values[a][0]])
		combine.append(['Unit 2', df.values[a][1]])
		combine.append(['Unit 3', df.values[a][2]])
		combine.append(['Unit 4', df.values[a][3]])
		combine.append(['Unit 5', df.values[a][4]])
		combine.append(['Unit 6', df.values[a][5]])
		combine.append(['Unit 7', df.values[a][6]])
		combine.append(['Unit 8', df.values[a][7]])
		index.append(a)
		index.append(a)
		index.append(a)
		index.append(a)
		index.append(a)
		index.append(a)
		index.append(a)
		index.append(a)
		'''
		data['Units'].append('Unit 1')
		data['Value'].append(df.values[a][0])
		data['Units'].append('Unit 2')
		data['Value'].append(df.values[a][1])
		data['Units'].append('Unit 3')
		data['Value'].append(df.values[a][2])
		data['Units'].append('Unit 4')
		data['Value'].append(df.values[a][3])
		data['Units'].append('Unit 5')
		data['Value'].append(df.values[a][4])
		data['Units'].append('Unit 6')
		data['Value'].append(df.values[a][5])
		data['Units'].append('Unit 7')
		data['Value'].append(df.values[a][6])
		data['Units'].append('Unit 8')
		data['Value'].append(df.values[a][7])
		'''
		'''
		unit1.append(df.values[a][0])
		unit2.append(df.values[a][1])
		unit3.append(df.values[a][2])
		unit4.append(df.values[a][3])
		unit5.append(df.values[a][4])
		unit6.append(df.values[a][5])
		unit7.append(df.values[a][6])
		unit8.append(df.values[a][7])
		index.append(a)
		'''



#data = {'Unit 1': unit1,'Unit 2': unit2,'Unit 3': unit3,'Unit 4': unit4,'Unit 5': unit5,'Unit 6': unit6,'Unit 7': unit7,'Unit 8': unit8}

df1 = pd.DataFrame(data = combine)
df1.columns = ['Units', 'Vals']



df.columns = ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Unit 8']

df1['index'] = index

print(df1)

#joypy.joyplot(df1, by="Units")
pjp.plot(data=df1, x='index', y='Vals', hue='Units', smooth=10)


'''
plt.subplot(241)
plt.plot( index, unit1, marker='D', alpha=0.4)
plt.subplot(242)
plt.plot( index, unit2, marker='o', color="orange", alpha=0.3)
plt.subplot(243)
plt.plot( index, unit3, marker='D', color="green", alpha=0.3)
plt.subplot(244)
plt.plot( index, unit4, marker='o', color="grey", alpha=0.3)

plt.subplot(245)
plt.plot( index, unit5, marker='D', color="pink", alpha=0.6)
plt.subplot(246)
plt.plot( index, unit6, marker='o', color="red", alpha=0.3)
plt.subplot(247)
plt.plot( index, unit7, marker='D', color="black", alpha=0.3)
plt.subplot(248)
plt.plot( index, unit8, marker='o', color="yellow", alpha=0.3)
'''

#joypy.joyplot(df1, by="Year", column="Anomaly", labels=labels, range_style='own',grid="y", linewidth=1, legend=False, figsize=(6,5),title="Global daily temperature 1880-2014 \n(C above 1950-80 average)",colormap=cm.autumn_r)
plt.show()
