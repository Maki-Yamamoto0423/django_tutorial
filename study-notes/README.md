学習内容メモ

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
