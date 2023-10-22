# import Flask, request, render_template
from flask import Flask, request, render_template
import os
import csv

# bulit application object
app=Flask(__name__)


uploaded_file = None
filepath = None
# 建立路徑 / 對應的處理函式
# /代表網站首頁
#使用GET來方法，處理路徑 / 的處理函式
@app.route("/", methods=["GET", "POST"])
def upload_file():
    upload_successful = False
    global uploaded_file
    global filepath
    if request.method == "POST":
        uploaded_file = request.files['file']
        filepath = os.path.join(app.config["file_uploads"], uploaded_file.filename)
        uploaded_file.save(filepath)
        if uploaded_file is not None:
            # 上傳成功
            upload_successful = True
        else:
            upload_successful = False

    if upload_successful:
        return render_template("index2.html")
    else:
        return render_template("index.html")

app.config["file_uploads"] = "C:\\Users\\melod\\OneDrive\\data_analysis_project\\file_upload"

# 處理路徑 /show_data 的對應函式
@app.route("/show_data")
def show_data():
    all_rows = []
    with open(filepath, encoding='utf-8-sig') as csvfile:
        raw_data= csv.reader(csvfile)
        # read raw data in row
        for row in raw_data:
            # data is added into list "all_rows"
            all_rows.append(row)
    
    return all_rows
    

# 處理路徑 /show 的對應函式
@app.route("/show")
def show():
    name= request.args.get("n", "")  #從query string中取得前端使用者在輸入框輸入的文字
    return "Hi," +name

# 使用POST方法，處利路徑 /calculate 的對應函式
@app.route("/calculate", methods=["POST"])
def calculate():
    # 接收GET方法的query string
    # max_number=request.args.get("max", "")
    
    #接收POST方法的query string
    max_number=request.form["max"]
    max_number=int(max_number)  #max_number為str要轉換成int，再計算
    # 1+2+...+max_number
    result=0
    for n in range(1, max_number+1):
        result += n
    return render_template("result.html", data= str(result))
    

# 動態路由: 建立路徑 /user/使用者名稱 對應的函式
@app.route("/user/<username>")
def handleusername(username):
    if username== "婷婷":
        return "Hello " +username
    else:
        return "Hello "+ username

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串 (Query String) 提供彈性: getSum?min=最小數字&max=最大數字&...
# 若要求字串中沒有參數min, max,...，則呈現預設值
@app.route("/getSum")
def getSum():  #min+(min+1)+(min+2)+...+max
    #接收要求字串中的參數資料
    maxNumber= request.args.get("max", 100)
    #maxNumber從網址取得時為string的形式，要轉換成數字
    maxNumber=int(maxNumber)
    minNumber= request.args.get("min", 1)
    minNumber=int(minNumber)
    #以下運算 min+(min+1)+(min+2)+...+max 總和的迴圈邏輯
    result=0
    for n in range(minNumber,maxNumber+1):
        result+=n
    #把結果回應給前端
    return "結果："+str(result)

#啟動網站伺服器，可透過"port"參數指定port
app.run(host="0.0.0.0", port=3000)

