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
    
    # �摜�t�@�C���̕ۑ�
    for key in files:
        file = files[key]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        data[key] = file.filename  # �t�@�C�������f�[�^�ɒǉ�
    
    # �����Ńf�[�^��ۑ� (��: �f�[�^�x�[�X�܂��̓t�@�C��)
    print(data)  # �m�F�p
    return jsonify({"message": "�t�H�[�������M����܂���", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)

