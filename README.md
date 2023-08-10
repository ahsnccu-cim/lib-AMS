# 政附電資社群 AMS 進出管理系統 操作說明
> 國立政大附中學生證進出管理系統
> AHSNCCU Access Management System (AMS)

+ 適用於 Windows 10, 11。
+ Linux(Ubuntu 22.04) 與 MacOS 測試中...

---
[ToC]

---
<center> (🚧文件施工中🚧) </center>

## 部屬環境

+ 請事先安裝好 Python 3.x
+ **請點擊執行 `setup.bat`**

## 啟動程式
* **請點擊執行 `main_beta.exe`**

### 介面自定義
依照畫面提示進行以下步驟
1. 輸入 GUI 視窗標題 (optional, 僅在切換視窗時會顯示)
2. 輸入介面中文標題
3. 輸入介面英文標題

+  輸入完成，確認後依照提示：確認輸入 `y` ；需重新更正輸入 `n`

![](https://hackmd.io/_uploads/HJTx4nMn2.png)<center>GUI 介面範例</center>


### 環境自定義
依照畫面提示進行以下步驟

+ 注意！輸入檔案與資料夾路徑時，**請使用 `/`**，勿使用 Windows 系統預設的 `\`

1. 輸入用來儲存所有程式的**資料夾路徑**
   例如：`C:/user/user/文件/lib-AMS-dev`
2. 輸入學生證內碼 csv **檔案路徑**
   例如：`C:/user/user/文件/lib-AMS-dev/學生證內碼/悠遊卡內碼.csv`
3. 輸入儲存每日進出紀錄檔案的**資料夾路徑**
   例如：`C:/user/user/文件/lib-AMS-dev/進出紀錄`

+ 輸入完成，確認後依照提示：確認輸入 `y` ；需重新更正輸入 `n`



## 版本更新
1. 開啟 Command Prompt
2. 下載新版程式：輸入 `git clone -b dev https://github.com/ahsnccu-scit/lib-AMS.git`
3. 將新版程式覆蓋舊版檔案
4. 執行前述[部屬與啟動步驟](#部屬環境)




<html>
    <head>
        <style>
        hr.style-two {
            border: 0;
            height: 1.5px;
            background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.75), rgba(0,0,0,0));
        }
        </style>
    </head>
    <body>
        

<hr class="style-two" 
    style="margin-bottom: -12.5px;
           margin-top: 90px;"/>
<h3> <center> 開發團隊 </center> </h3>
<hr class="style-two" 
    style="margin-bottom: 20px;
           margin-top: -2px;"/>
<center> • 國立政大附中第十六屆校友 • </center>
<center> <a href="https://linktr.ee/whyhugo">王修佑</a> ｜ 沈至萱 ｜ 李馨亞 </center>
<p></p>
<center> Powered by 國立政大附中學生校友電資社群<br><a href='https://github.com/ahsnccu-scit/lib-AMS/tree/dev'> 開放原始碼 </a> </center>
    </body>
</html>

