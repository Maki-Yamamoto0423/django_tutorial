学習内容メモ

⭐️2026/02/02

Django ORM
Pythonで書いたコードを、DjangoがSQLに翻訳して
データベースを操作してくれる仕組み

Django shellを開始してDBを操作した

気づき💡
DrizzleORMと同じことしてる
言語がTSかPythonかの違い

---

仮想環境は「自動でON」にはならないため、自分で有効化する必要がある
仮想環境を有効化
source .venv/bin/activate

しかし、Uv run コマンドを使用すれば、有効化することができるため、上記を実行する必要がなくなる

---

📂django_tutorial/settings.py
INSTALLED_APPS は「このプロジェクトで使うアプリ一覧」

ここに書かれていないアプリは：

- models を書いても無視される
- makemigrations しても検出されない
- admin にも出ない

⭐️2026/02/03
URLは仕様変更が一番起きやすいため、Djangoでは「変更されやすいもの（URL）」
を「1ファイルに隔離」する。

URLを直接書かかずに、名前で指定する
urls.py で「URLの実体」と「名前」を1回だけ定義すると、
その名前をプロジェクト中どこからでも再利用できる

---

📂polls/urls.py

path("<int:pk>/", views.DetailView.as_view(), name="detail")

<int:pk>/　実際のURL構造
name="detail"　意味（名前）

---

URLの名前を再利用する例

① テンプレート
<a href="{% url 'polls:detail' question.id %}">

② views（Python）
reverse("polls:detail", args=(question.id,))

③ redirect
return redirect("polls:detail", pk=question.id)

コメント
Reactのコンポーネント設計みたい

---

⭐️2026/02/04

【各ファイルの役割】

📂manage.py
・Djangoを操作する司令塔

例：
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

📂db.sqlite3
・DB本体
・設計図と履歴をもとに、実際に作られた「実体（箱）」
・本チュートリアルでは、Question や Choice のデータが入ってる

イメージ図

1. 設計図を書く: models.py
2. 履歴書を作る: python manage.py makemigrations → migrations/XXXX.py ができる
3. 箱に反映する: python manage.py migrate → db.sqlite3 の中身が更新される

📂django_tutorial
・アプリケーション共通の設定

django_tutorial/
├── settings.py
├── urls.py
├── asgi.py
├── wsgi.py

📂settings.py
・Django 全体の設定ファイル
→　DB設定
→　テンプレート設定
→　セキュリティ設定

📂urls.py（プロジェクト側）
・「このURLは、どのアプリに渡すか」を決める

例：
path("polls/", include("polls.urls"))
/polls/ → polls アプリに渡す

📂asgi.py / wsgi.py
・本番環境で使用するため、いまは使わない

📂polls/
・アプリケーション本体

polls/
├── models.py
├── views.py
├── urls.py
├── templates/
├── admin.py
└── migrations/

📂models.py
・データの設計図

例：
class Question(models.Model):

→ DBのテーブル構造
→ DjangoがSQLを書いてくれる

📂views.py
・処理の中核になる部分

役割
・DBからデータ取得
・POST処理
・テンプレートに渡す

📂urls.py（polls 側）
・URLと view の対応表

"" → 一覧
"<pk>/" → 詳細
"vote/" → 処理
"results/" → 結果

📂templates/polls/
・画面（HTML）

templates/polls/
├── index.html
├── detail.html
└── results.html

📂admin.py
・Django 管理画面の設定

→ /admin/でDBをGUIで操作できる

【実行時の流れ】

ブラウザ
↓
django_tutorial/urls.py
↓
polls/urls.py
↓
views.py
↓
models.py（必要なら）
↓
templates/
↓
HTMLレスポンス

【汎用ビュー】
汎用ビューとは、よくある画面の処理を、Djangoがあらかじめ用意してくれていること

⭕️使うとき
・一覧表示
・詳細表示
・結果表示
・CRUD画面

❌使わないとき
・複雑な業務ロジック
・POST処理

表示系（GET）は汎用ビュー
処理系（POST/ロジック）は自分で書く
