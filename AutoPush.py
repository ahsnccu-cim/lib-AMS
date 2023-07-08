from git import Repo
import schedule
import datetime
import time
import sys
import pandas as pd
import re

def add_last_update_time_todaypage(today, now_time, user_historyfile):
    #Read today's xlsx as DataFrame
    df1 = pd.read_excel(f"{user_historyfile}/{today}.xlsx", index_col=None)
    #不讀取今日 html ，直接儲存覆蓋
    output_html = f'''
        <!DOCTYPE html>
        <html lang="zh-tw">
            <head>
                <meta charset="utf-8">
                <title> 進出館記錄 </title>
            </head>
        <body>
            <p> 最後更新時間：{now_time} </p>
        '''
    output_html += df1.to_html(index=False)
    output_html += "\n</body>\n</html>"
    with open(f"{user_historyfile}/{today}.html", 'w', encoding="utf-8") as file:
        file.write(output_html)

def git_push():
    user_historyfile = sys.argv[1]
    today = datetime.datetime.now().strftime('%Y-%m-%d %A')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %A, %H:%M')
    add_last_update_time_todaypage(today, now_time, user_historyfile)
    repo = Repo(sys.argv[1])
    repo.git.add(all=True)
    repo.index.commit(now_time, 'Auto Push')
    repo.remotes.origin.pull()
    origin = repo.remote('origin')
    origin.push()

schedule.every().day.at("00:05").do(git_push)
schedule.every().day.at("06:00").do(git_push)
schedule.every().day.at("08:35").do(git_push)
schedule.every().day.at("09:35").do(git_push)
schedule.every().day.at("10:35").do(git_push)
schedule.every().day.at("11:35").do(git_push)
schedule.every().day.at("12:35").do(git_push)
schedule.every().day.at("13:35").do(git_push)
schedule.every().day.at("14:35").do(git_push)
schedule.every().day.at("15:35").do(git_push)
schedule.every().day.at("16:35").do(git_push)
schedule.every().day.at("17:35").do(git_push)
schedule.every().day.at("19:00").do(git_push)
schedule.every().day.at("23:55").do(git_push)

while True:
    schedule.run_pending()
    time.sleep(40)