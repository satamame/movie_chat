## プロジェクトとアプリを作成

```
(.venv)> pip install django
 ...
(.venv)> django-admin startproject movie_chat .
 ...
(.venv)> django-admin startapp idea
```

## Settings

- `INSTALLED_APPS` に 'idea' を追加。
- `LANGUAGE_CODE` を 'ja' にする。
- `TIME_ZONE` を 'Asia/Tokyo' にする。

## コード

- Form を作成 (idea/forms.py)。
- View を作成 (idea/views.py)。
- ルーティングを作成 (movie_chat/urls.py, idea/urls.py)。
- テンプレートを作成 (idea/templates/idea/idea.html)。
- モデルを作成 (idea/models.py)。
- モデルを admin 画面に登録 (idea/admin.py)。

## 環境変数

```
(.venv)> pip install django-environ
```

- settings.py を書き換える。
  - `env` を作って `read_env()` する。
  - `SECRET_KEY` を `env` から読むようにする。
  - `DEBUG` を `env` から読むようにする。
  - `DATABASES['default']` を `env.db()` にする。
- .env ファイルを追加。
  - `DEBUG`
  - `SECRET_KEY`
  - `DATABASE_URL`

## データベース

```
(.venv)> pip install mysqlclient
```

- ローカルの MySQL に `movie_chat` スキーマを作成。
- db.sqlite3 ファイルは削除。

.env
```
DATABASE_URL=mysql://user:pass@127.0.0.1:3306/movie_chat
```

コマンド
```
(.venv)> python manage.py makemigrations
 ...
(.venv)> python manage.py migrate
```

## スーパーユーザ

```
(.venv)> python manage.py createsuperuser
```

## 静的ファイル

settings.py
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

- static/css/base.css を作成。

テンプレートで以下のように読込む。
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  ...
  <link rel="stylesheet" href="{% static 'css/base.css' %}" type="text/css">
</head>
```
