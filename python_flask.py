# import Flask
from flask import Flask
# bulit application object 
app=Flask(__name__)

# 建立網站首頁的回應方式
# /代表網站首頁
@app.route("/")
#用來回應網站首頁連線的函式
def index():
    return "Hello From Ting Ting, Chang" #回傳網站首頁的內容

#啟動網站伺服器
app.run(host="0.0.0.0", port=3000)

#若要終止程式按"ctrl+c" (每次要執行更新過的程式都要先終止目前的程式)
#打clear 清除之前的命令
