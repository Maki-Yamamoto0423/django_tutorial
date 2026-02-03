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
