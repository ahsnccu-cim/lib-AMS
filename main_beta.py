import pandas as pd
import tkinter as tk
import datetime
import os
from git import Repo
import subprocess
import time
import sys
import schedule

#使用者自行輸入環境設置
setup_confirm_general = 'n'
while setup_confirm_general != 'y':
    user_windows_title = input("視窗標題：") #國立政大附中圖書館進出館管理系統
    user_header_zhtw = input("中文標題：") #國立政大附中圖書館進出館管理系統
    user_header_en = input("英文標題：") #AHSNCCU Library Access Management System
    setup_confirm_general = input(f"您目前的設置如下：\n視窗標題：{user_windows_title}\n中文標題：{user_header_zhtw}\n英文標題：{user_header_en}\n確認繼續[y/n]？")
setup_confirm_address = 'n'
while setup_confirm_address != 'y':
    user_exe = input("儲存程式「資料夾」路徑：") #D:/programing/swiftx/ahsnccu-lib-AMS/ahsnccu-lib-AMS_myGit
    user_idfile = input("學生證內碼檔案路徑：") #D:/programing/swiftx/ahsnccu-lib-AMS/ahsnccu-lib-AMS_myGit/學生證內碼/悠遊卡內碼.csv
    user_historyfile = input("儲存進出記錄「資料夾」路徑：") #C:/Users/user/OneDrive/文件/圖書館進出
    setup_confirm_address = input(f"您目前的設置如下：\n程式儲存「資料夾」路徑：{user_exe}\n學生證內碼檔案路徑：{user_idfile}\n儲存進出記錄「資料夾」路徑：{user_historyfile}\n確認繼續[y/n]？")

#建立主頁 html
html_content = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>國立政大附中圖書館學生進出記錄</title>
  </head>
  <body>
    <h1> 國立政大附中圖書館進出記錄 </h1>
  </body>
</html>
'''
with open(f"{user_historyfile}/政附圖書館進出記錄.html", 'w', encoding="utf-8") as file:
    file.write(html_content)

#建立今日 xlsx
def create_today_xlsx(filename):
    column_name = ['班級','座號','姓名','入館時間','出館時間','Status']
    df1 = pd.DataFrame([],columns=column_name)
    df1.to_excel(f"{filename}.xlsx", index=False)

#建立今日 html
def create_today_html(filename):
    df1 = pd.read_excel(f"{filename}.xlsx", index_col=None)
    html_table = '''
    <!DOCTYPE html>
    <html lang="zh-tw">
        <head>
            <meta charset="utf-8">
            <title> 進出館記錄 </title>
            </head>
        <body>
    '''
    html_table += df1.to_html(index=False)
    html_table += "\n</body>\n</html>"
    # 將 HTML 寫入檔案
    with open(f'{filename}.html', 'w', encoding='utf-8') as file:
        file.write(html_table)

def new_day(user_historyfile):
    today = datetime.datetime.now().strftime('%Y-%m-%d %A')
    if not os.path.isfile(f"{user_historyfile}/{today}.xlsx"):
        create_today_xlsx(f"{user_historyfile}/{today}")
    elif not os.path.isfile(f"{user_historyfile}/{today}.html"):
        create_today_html(f"{user_historyfile}/{today}")

new_day(user_historyfile)

#呼叫其他程式
print('ready subprocess newday')
subprocess.Popen(['python', f'{user_exe}/NewDay.py', user_historyfile])
print('ready subprocess autopush')
subprocess.Popen(['python', f'{user_exe}/AutoPush.py', user_historyfile])

print('subprocess [FINISH]')

#讀取學生證內碼與學生資訊對應資料檔
df = pd.read_csv(user_idfile, header='infer', encoding='utf-8-sig')

print('df(id.csv) read [FINISH]')

#建立tkinter視窗與標題
window = tk.Tk()
window.title(user_windows_title)
window.attributes('-fullscreen', True)

#建立tkinter label(用於固定顯示)
header_label = tk.Label(window, text=f'\n{user_header_zhtw}\n{user_header_en}', font=('Noto Sans TC', 30)) #大標題
annotation = tk.Label(window, text='請刷學生證', font=('Noto Sans TC', 30), fg='red') #請刷學生證提示文字
header_label.pack()
annotation.pack(pady=20)
developers = tk.Label(window, text='開發團隊：政附第十六屆 · 王修佑 · 沈至萱 · 李馨亞\n政附學生校友電資社群', font=('辰宇落雁體 Thin Monospaced', 20))
developers.pack(side='bottom', pady=10)

#建立tkinter label(用於情境顯示)
inn = tk.Label(window, text='歡迎入館，請取卡', font=('Noto Sans TC', 30), bg='green', fg='white') #入館顯示
out = tk.Label(window, text='出館成功，請取卡', font=('Noto Sans TC', 30), bg='blue', fg='white') #出館顯示
erro = tk.Label(window, text='刷卡錯誤！', font=('Noto Sans TC', 30), bg='red', fg='white')
blank3 = tk.Label(window, text='', font=('Noto Sans TC', 30))
a = tk.StringVar()
st_info = tk.Label(window, textvariable=a, font=('Noto Sans TC', 30)) #顯示學生資訊
b = tk.StringVar()
time_show = tk.Label(window, textvariable=b, font=('Noto Sans TC', 30)) #顯示當前時間
c = tk.StringVar()
now_c = tk.Label(window, textvariable=c, font=('Noto Sans TC', 20)) #顯示人次
c_temp = tk.Label(window, text=f"場館人數：0  今日人次：0", font=('Noto Sans TC', 20))
c_temp.pack(pady=15)

#結束顯示當前資訊(入館)
def hide_inn():
    inn.pack_forget()
    st_info.pack_forget()
    time_show.pack_forget()

#結束顯示當前資訊(出館)
def hide_out():
    out.pack_forget()
    st_info.pack_forget()
    time_show.pack_forget()

def hide_erro():
    blank3.pack_forget()
    erro.pack_forget()
    
#入館顯示
def pack_inn():
    now_c.pack(pady=15)
    st_info.pack()
    inn.pack(ipadx=35, ipady=8)
    time_show.pack()
    window.after(3000, hide_inn) #2000ms後結束顯示

#出館顯示
def pack_out():
    now_c.pack(pady=15)
    st_info.pack()
    out.pack(ipadx=35, ipady=8)
    time_show.pack()
    window.after(3000, hide_out) #2000ms後結束顯示

#錯誤顯示
def pack_erro():
    now_c.pack(pady=15)
    blank3.pack()
    erro.pack(ipadx=35, ipady=8)
    window.after(3000, hide_erro)

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

#計算館內人數
def count_in(df1):
    count = 0
    for i in df1['Status']:
        if i == 'IN':
            count += 1
    return count

print('sub def run [FINISH]')

#主程式
def main():
    idnum = input("待機模式，請刷卡：")
    date = datetime.datetime.now().strftime('%Y-%m-%d %A')
    df1 = pd.read_excel(f"{user_historyfile}/{date}.xlsx", index_col=None)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    class_, number, name = find_st_info(idnum)
    print(idnum, class_, number, name, time)
    a.set(f"班級：{class_}   座號：{number}\n姓名：{name}\n")
    b.set(f"\n現在時間：{time}")
    get_near_record = 0 #用於控制：要新增資料(入館)還是修改資料(出館)，避免完成修改資料後又新增為入館資料
    if len(df1) > 0: #第二筆資料開始跑這邊
        for i in range(len(df1)): #尋找是否還未出館
            if (df1.loc[i, '姓名'] == name) and (df1.loc[i, 'Status'] == 'IN'): #TRUE=這人要出館
                df1.loc[i, 'Status'] = 'OUT'
                df1.loc[i, '出館時間'] = time
                get_near_record = 1 #出館，完成修改資料，切到1
                count_ = count_in(df1)
                c_temp.pack_forget()
                c.set(f"場館人數：{count_}  今日人次：{len(df1)}")
                pack_out()
                break #不再尋找
        if get_near_record == 0: #入館，要新增資料
            new_data = pd.DataFrame(pd.DataFrame([[class_,number,name,time,'','IN']], columns=['班級','座號','姓名','入館時間','出館時間','Status']))
            df1 = pd.concat([new_data, df1], ignore_index=True)
            count_ = count_in(df1)
            c_temp.pack_forget()
            c.set(f"場館人數：{count_}  今日人次：{len(df1)}")
            pack_inn()
    else: #僅用於"新增"第一筆資料
        new_data = pd.DataFrame(pd.DataFrame([[class_,number,name,time,'','IN']], columns=['班級','座號','姓名','入館時間','出館時間','Status']))
        df1 = pd.concat([new_data, df1], ignore_index=True)        
        count_ = count_in(df1)
        c_temp.pack_forget()
        c.set(f"場館人數：{count_}  今日人次：{len(df1)}")
        pack_inn()
    df1.to_excel(f"{user_historyfile}/{date}.xlsx", index=False) #輸出至local, OneDrive會auto sync
    '''
    with xw.App(visible=False) as app:
        wb = xw.Book(f"{user_historyfile}/{date}.xlsx")
        sheet = wb.sheets['Sheet1']
        used_range = sheet.used_range
        used_range.columns.autofit()
        wb.save()
    window.after(3100, main) #等待2100ms後迴圈 
    '''
    '''
    except:
        pack_erro()
        window.after(2600, main)
    '''
    
    window.after(3100, main) #等待2100ms後迴圈 

print('ready to run main')
main()

window.mainloop()