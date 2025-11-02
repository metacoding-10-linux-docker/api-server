from flask import Flask, Response, send_file
import redis
import os

app = Flask(__name__)

# Redis 연결
r = redis.Redis(host='redis', port=6379, db=0)

# 메인 페이지
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
      <body>
        <h2>NGINX CACHE / Redis API</h2>
      </body>
    </html>
    """
    return Response(html, mimetype="text/html")
  
# 이미지 요청
@app.route("/image.png")
def get_image():
    image_path = os.path.join(os.path.dirname(__file__), "image.png")
    return send_file(image_path, mimetype="image/png")

# 이름 저장
@app.route("/save")
def save_name():
    r.set("name", "jooho")
    return "이름이 저장되었습니다."

# 이름 불러오기기
@app.route("/read")
def read_name():
    value = r.get("name")
    if value is None:
        return "저장된 이름이 없습니다."
    return f"name = {value.decode('utf-8')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
