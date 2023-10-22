# import Flask, request, render_template
from flask import Flask, request, render_template
import os
from DM_digestibility_analysis import (
    read_csv,
    raw_data_to_dict,
    multiply_data,
    subtract_data,
    calculate_DM_digestibility,
)

# bulit application object
app = Flask(__name__)


filepath = None


# 建立路徑 / 對應的處理函式
# /代表網站首頁
# 使用GET來方法，處理路徑 / 的處理函式
@app.route("/", methods=["GET", "POST"])
def upload_file():
    upload_successful = False
    global filepath
    if request.method == "POST":
        uploaded_file = request.files["file"]
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


app.config[
    "file_uploads"
] = "C:\\Users\\melod\\OneDrive\\data_analysis_project\\file_upload"


# 處理路徑 /show_data 的對應函式
@app.route("/show_data")
def show_data():
    file_csv = read_csv(filepath)
    return render_template("show_data_page.html", data=file_csv)


@app.route("/data_analysis")
def data_analysis():
    file_csv = read_csv(filepath)
    data_dict = raw_data_to_dict(file_csv)
    data_multiply = multiply_data(
        data_dict, new_key="Diet_DM", key1="Diet_weight", key2="Diet_DM_percentage"
    )
    data_substract = subtract_data(
        data_dict,
        new_key="Digesta_weight",
        key1="Freeze_dry_weight",
        key2="Tube_weight",
    )
    data_result = calculate_DM_digestibility(data_multiply, data_substract)
    return render_template("show_data_analysis_result.html", data=data_result)


# 啟動網站伺服器，可透過"port"參數指定port
app.run(host="0.0.0.0", port=3000)
