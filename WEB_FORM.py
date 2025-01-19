from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# アップロードフォルダの設定
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# "/" ルート：submit_form.html を表示
@app.route('/')
def home():
    return render_template('submit_form.html')  # mainブランチ直下のsubmit_form.htmlを表示

# "/submit" エンドポイント：フォームデータの処理
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.to_dict()  # フォームデータを取得
    files = request.files  # アップロードされたファイルを取得
    
    # 画像ファイルの保存
    for key in files:
        file = files[key]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        data[key] = file.filename  # ファイル名をデータに追加
    
    # ここでデータを保存 (例: データベースまたはファイル)
    print(data)  # コンソールで確認用
    return jsonify({"message": "フォームが送信されました", "data": data}), 200

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    app.run(debug=True)

