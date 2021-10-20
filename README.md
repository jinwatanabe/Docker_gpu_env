# リポジトリについて
データ分析をする際に必要なライブラリが用意されたPythonによる環境を提供しています。
コンテナ内はGPUにも対応しています。
WSL2, Docker, gitを利用しています。

GPUはGTX 1650で確認済みです。

# ディレクトリ

- `notebook/dataset/`.....ここに.ipynbファイルやデータなどを追加します。

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
git clone https://github.com/jinwatanabe/Docker_gpu_env.git
```

`Docker_gpu_env`というフォルダがクローンされるので以降はそのフォルダで作業をします。

# 起動方法
1. `docker-compose build`
2. `docker-compose up`

Webブラウザを開き`localhost`にアクセスする。

![bandicam 2021-05-28 21-30-20-860](https://user-images.githubusercontent.com/46788746/119984205-17639c80-bffc-11eb-9d66-7a420aa77150.jpg)

作業の後には`docker-compose down`をしてください。

# GPUの設定

以下の記事を参考に設定を行う。

- [待ってました CUDA on WSL 2](https://qiita.com/ksasaki/items/ee864abd74f95fea1efa)