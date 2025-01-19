from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    files = request.files
    
    # 画像ファイルの保存
    for key in files:
        file = files[key]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        data[key] = file.filename  # ファイル名をデータに追加
    
    # ここでデータを保存 (例: データベースまたはファイル)
    print(data)  # 確認用
    return jsonify({"message": "フォームが送信されました", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)

