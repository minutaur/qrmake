from flask import Flask, request, send_file, render_template_string
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <h1>QR 코드 생성기</h1>
        <form action="/generate" method="post">
            <input type="text" name="data" placeholder="QR 코드에 담을 내용" required>
            <button type="submit">QR 코드 생성</button>
        </form>
    ''')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    qr = qrcode.make(data)
    

    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
