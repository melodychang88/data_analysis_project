# import Flask
from flask import Flask
# import request object
from flask import request

# bulit application object ,可以設定靜態檔案的路徑
app=Flask(__name__, static_folder="static",   #靜態檔案的資料夾名稱
    static_url_path="/"    #靜態檔案對應的網址名稱
    )
#所有在static 資料夾底下的檔案，都對應到網址路徑 /檔案名稱

# 建立路徑 / 對應的處理函式
# /代表網站首頁
@app.route("/")
#用來回應路徑 / 的處理函式
def index():
    return "Hello From Ting Ting, Chang" #回傳網站首頁的內容

#建立路徑 /data 對應的處理函式
@app.route("/data")
#用來回應路徑"/data"的處理函式
def handledata():
    return "My data"

# 動態路由: 建立路徑 /user/使用者名稱 對應的函式
@app.route("/user/<username>")
def handleusername(username):
    if username== "婷婷":
        return "Hello " +username
    else:
        return "Hello "+ username

#啟動網站伺服器，可透過"port"參數指定port
app.run(host="0.0.0.0", port=3000)

#若要終止程式按"ctrl+c" (每次要執行更新過的程式都要先終止目前的程式)
#打clear 清除之前的命令
