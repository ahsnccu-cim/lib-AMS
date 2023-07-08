import pandas as pd
import datetime

#讀取學生證內碼與學生資訊對應資料檔
df = pd.read_csv('學生證內碼/ahsnccu-112id.csv', header='infer', encoding='utf-8-sig')

#抓取學生資訊
def find_st_info(idnum):
    index = 0
    for i in df['卡片內碼']:
        if str(i) == idnum:
            class_ = df.loc[index, '班級']
            number = df.loc[index, '座號']
            name = df.loc[index, '姓名']
            break
        index += 1
    return class_, number, name

#建立出入館紀錄表
column_name = ['班級','座號','姓名','入館時間','出館時間','Status'] #建立column name
df1 = pd.DataFrame([],columns=column_name) #建立DataFrame
#以下動作，確保excel file的存取權持續在這份code手上
df1.to_excel("C:/Users/user/OneDrive/文件/attend-record2.xlsx") #先把DataFrame輸出至local
df1 = pd.read_excel('C:/Users/user/OneDrive/文件/attend-record2.xlsx') #再讀取前一行建立的excel file

while True:
    idnum = input()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    class_, number, name = find_st_info(idnum)
    print(idnum, class_, number, name, time)
    get_near_record = 0 #用於控制：要新增資料(入館)還是修改資料(出館)，避免完成修改資料後又新增資料
    if len(df1) > 0: #第二筆資料開始跑這邊
        for i in range(len(df1)-1,-1,-1): #尋找是否還未出館
            if (df1.loc[i, '姓名'] == name) and (df1.loc[i, 'Status'] == 'IN'): #TRUE=未出館
                df1.loc[i, 'Status'] = 'OUT'
                df1.loc[i, '出館時間'] = time
                get_near_record = 1 #完成修改資料，切到1
                break #不再尋找
        if get_near_record == 0: #要新增資料
            df1 = df1.append(pd.DataFrame([[class_,number,name,time,'','IN']], columns=['班級','座號','姓名','入館時間','出館時間','Status']), ignore_index=True)
    else: #僅用於"新增"第一筆資料
        df1 = df1.append(pd.DataFrame([[class_,number,name,time,'','IN']], columns=['班級','座號','姓名','入館時間','出館時間','Status']), ignore_index=True)
    df1.to_excel("C:/Users/user/OneDrive/文件/attend-record2.xlsx") #輸出至local, OneDrive會auto sync