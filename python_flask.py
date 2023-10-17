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
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    lang= request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello From Ting Ting, Chang" #回傳網站首頁的內容
    else:
        return "您好，歡迎光臨"

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

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Query String) 提供彈性: getSum?max=最大數字，若要求字串中沒有參數max，maxNumber預設值為100
@app.route("/getSum")
def getSum():  #1+2+3+...+max
    maxNumber= request.args.get("max", 100)
    #maxNumber從網址取得時為string的形式，要轉換成數字
    maxNumber=int(maxNumber)
    result=0
    for n in range(1,maxNumber+1):
        result+=n
    return "結果："+str(result)

#啟動網站伺服器，可透過"port"參數指定port
app.run(host="0.0.0.0", port=3000)

#若要終止程式按"ctrl+c" (每次要執行更新過的程式都要先終止目前的程式)
#打clear 清除之前的命令
