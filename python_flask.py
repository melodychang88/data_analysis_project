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

#啟動網站伺服器py
app.run()

#若要終止程式按"ctrl+c"
#打clear 清除之前的命令
