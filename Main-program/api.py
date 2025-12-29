from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # 外部API（テスト用データ）からJSONを取得
    # ここでは例としてJSONPlaceholderの投稿一覧を取得しています
    api_url = "https://api.wolfx.jp/jma_eew.json"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status() # エラーがあれば例外を発生させる
        data = response.json()      # JSONデータをPythonのリスト/辞書に変換
    except Exception as e:
        data = [{"title": "エラー", "body": f"データの取得に失敗しました: {e}"}]

    # 取得したデータを 'posts' という名前で index.html へ渡す
    return render_template('index.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)

