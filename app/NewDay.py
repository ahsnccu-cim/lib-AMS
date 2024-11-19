import schedule
import datetime
import time
import sys
import pandas as pd


def create_today_xlsx(filename):
    column_name = ['班級','座號','姓名','入館時間','出館時間','Status']
    df1 = pd.DataFrame([],columns=column_name)
    df1.to_excel(f"{filename}.xlsx", index=False)

def create_today_html(filename):
    df1 = pd.read_excel(f"{filename}.xlsx", index_col=None)
    html_table = '''
    <!DOCTYPE html>
    <html lang="zh-tw">
        <head>
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-TK7JBP6B2H"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());
                gtag('config', 'G-TK7JBP6B2H');
            </script>
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

def new_day():
    user_historyfile = sys.argv[1]
    today = datetime.datetime.now().strftime('%Y-%m-%d %A')
    create_today_xlsx(f"{user_historyfile}/{today}")
    create_today_html(f"{user_historyfile}/{today}")

schedule.every().day.at("00:00").do(new_day)

while True:
    schedule.run_pending()
    time.sleep(40)

'''
每日零時，
新增當日 excel。
新增當日 html。
將當日 html 新增至主頁。
註：僅新增於本地端，未進行推送。
'''