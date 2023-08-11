
<h1> 政附電資社群 AMS 進出管理系統 操作說明 </h1>
國立政大附中學生證進出管理系統<br>
AHSNCCU Access Management System (AMS)
<p></p>
<blockquote>
<ul>
    <li>適用於 Windows 10, 11。</li>
    <li>Linux(Ubuntu 22.04) 與 MacOS 測試中...</li>
</ul>
</blockquote>
<p align="center"> (🚧文件施工中🚧) </p>
<h2>部屬環境</h2>
<ol>
    <li>請事先安裝好 Python 3.x</li>
    <li><strong>請點擊執行 <code>setup.bat</code></strong></li>
</ol>
<h2>啟動程式</h2>
<p><strong>請點擊執行 <code>main_beta.exe</code></strong></p>
<h3>介面自定義</h3>
<p>依照畫面提示進行以下步驟</p>
<ol>
    <li>輸入 GUI 視窗標題 (optional, 僅在切換視窗時會顯示)</li>
    <li>輸入介面中文標題</li>
    <li>輸入介面英文標題</li>
</ol>
<ul><li>  輸入完成，確認後依照提示：確認輸入 <code>y</code> ；需重新更正輸入 <code>n</code></li></ul>

![](https://hackmd.io/_uploads/HJTx4nMn2.png)
<p align="center">GUI 介面範例</p>

<h3>環境自定義</h3>
<p>依照畫面提示進行以下步驟</p>
<ul><li>注意！輸入檔案與資料夾路徑時，<strong>請使用 <code>/</code></strong>，勿使用 Windows 系統預設的 <code>\</code></li></ul>
<ol>
    <li>輸入用來儲存所有程式的<strong>資料夾路徑</strong><br>例如：<code>C:/user/user/文件/lib-AMS-dev</code></li>
    <li>輸入學生證內碼 csv <strong>檔案路徑</strong><br>例如：<code>C:/user/user/文件/lib-AMS-dev/學生證內碼/悠遊卡內碼.csv</code></li>
    <li>輸入儲存每日進出紀錄檔案的<strong>資料夾路徑</strong><br>例如：<code>C:/user/user/文件/lib-AMS-dev/進出紀錄</code></li>
</ol>
<ul><li>輸入完成，確認後依照提示：確認輸入 <code>y</code> ；需重新更正輸入 <code>n</code></li></ul>

## 版本更新
1. 開啟 Command Prompt<br>
2. 下載新版程式：<br>

```md
git clone -b dev https://github.com/ahsnccu-scit/lib-AMS.git
```

3. 將新版程式覆蓋舊版檔案</li>
4. 執行前述<a href="#部屬環境">部屬與啟動步驟</a></li>


---
<h3> <p align="center"> 開發團隊  </p>
</h3>

<p align="center"> • 國立政大附中第十六屆校友 • </p>
<p align="center"> <a href="https://linktr.ee/whyhugo">王修佑</a> ｜ 沈至萱 ｜ 李馨亞 </p>
<p></p>
<p align="center"> Powered by 國立政大附中學生校友電資社群<br><a href='https://github.com/ahsnccu-scit/lib-AMS/tree/dev'> 開放原始碼 </a> </p>

---
