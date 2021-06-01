# リポジトリについて
データ分析をする際に必要なライブラリが用意されたPythonによる環境を提供しています。
Docker, gitを利用しています。
# ディレクトリ

- `notebook/dataset/`.....データセットを保存しているディレクトリ。このディレクトリ下のファイルはGitにPushされません。
- `notebook/kaggle/`.....Kaggleで利用したNotebookを入れるフォルダです。
- `notebook/Nishika/`....Nishikaで利用したNotebookを入れるフォルダです。
- `notebook/Nishika/{コンペ名}/models`....モデルを入れるフォルダ。GitにPushされません。
#  ライブラリの追加

ライブラリを永続的にインストールする場合、libraries/Dockerfileにインストールするライブラリを追加してください。

```
# python libraries
RUN pip install -U pip && \
        pip install fastprogress japanize-matplotlib \
        new library here
```

# リポジトリのダウンロード

```
git clone https://github.com/jinwatanabe/data_analysis.git
```

`data_analysis`というフォルダがクローンされるので以降はそのフォルダで作業をします。

# 起動方法
1. `docker-compose build`
2. `docker-compose up`

Webブラウザを開き`localhost`にアクセスする。

![bandicam 2021-05-28 21-30-20-860](https://user-images.githubusercontent.com/46788746/119984205-17639c80-bffc-11eb-9d66-7a420aa77150.jpg)

作業の後には`docker-compose down`をしてください。