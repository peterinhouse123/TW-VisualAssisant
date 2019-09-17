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
cd ./Module
python Websocket.py

介面端 
cd ./Node_UI
electron .
```

- 測試發送訊息

```
請用任意的WEBSOCKET連接工具連接到
ws://127.0.0.1:7777
發送 eyJvcmRlciI6ICJwdXNoX21zZyIsICJkZXRhaWwiOiAiXHU2M2E4XHU5MDAxXHU2ZTJjXHU4YTY2In0=

```
