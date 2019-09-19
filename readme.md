# 推播式虛擬助手

---
## 開發影片連結：
https://youtu.be/Y05_3lJD7Lw
## 開發目的：
完成一個基於HTTP接收訊息的推播助手，並且推播至指定的裝置
預計支援 PC、IOS

## 開發進度：
- 剛完成基礎骨架
- 完成Websocket server與溝通指令
- 初步完成Weboscket 與介面串接測試
- 完成基於 electron 的彈窗介面
- 完成與後端的串接，並且可以隱藏與置頂窗口

## 使用說明
- 環境安裝
```
pip install -r requirements.txt
cd Node_UI
npm install
```

- 啟動
```
Python端
python Assistant.py

```

- 測試發送訊息

```
請在任意瀏覽器網址列輸入
http://127.0.0.1:5000/push/自訂訊息
即可以推播
```
