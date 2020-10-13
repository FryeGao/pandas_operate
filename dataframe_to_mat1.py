"""
将dataframe文件转换成mat文件
"""
import scipy.io as sio
import numpy as np
import pandas as pd

input_path = r''
shipName = ''
df = pd.read_excel(input_path)
dfCleaned=df
# 将UNIX时间戳转换成日期数字（单位：日期，时间北京）
time_h=pd.DataFrame([])
for i in range(0,len(dfCleaned)):
    time_h=time_h.append(pd.DataFrame([float(dfCleaned.loc[i,'timestamp'])/86400+719529+8/24]),ignore_index=True)
time_h.columns=['timestamp']
dfCleaned_z=pd.concat([time_h,dfCleaned.iloc[:,1:]],axis=1)
dfCleaned_np=dfCleaned_z.values

# 所有字符串和空值替换成nan值
for column in range(0,len(dfCleaned_np[0,:])):
    for row in range(0,len(dfCleaned_np)):
        # 空值、字符串、nan值
        if dfCleaned_np[row,column]=='' or type(dfCleaned_np[row,column])==str or dfCleaned_np[row,column]!=dfCleaned_np[row,column]:
            dfCleaned_np[row,column]=np.nan

# 矩阵转化成列表格式，并保存为.mat的数组类型
# sio.savemat(shipName+'_'+timeFormat(beginTime)+'_'+timeFormat(endTime) + '.mat', {'Data':dfCleaned_np.tolist()})
sio.savemat(shipName+'满载.mat', {'Data':dfCleaned_np.tolist()})
print("Done")