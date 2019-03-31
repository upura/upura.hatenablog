事業会社でデータアナリストをしているu++です。
普段は[はてなブログ](https://upura.hatenablog.com)でKaggleや競技プログラミングの記事を定期的に書いていて、「Kaggle Tokyo Meetup」というイベントで[登壇](https://speakerdeck.com/upura/kaggler-ja-driven-learning-kaggle-tokyo-meetup-number-5)した経験もあります。

本記事では「Kaggleに登録したら次にやること」と題して、Kaggleに入門したい方に向けて次のようなコンテンツを掲載します。

- Kaggleの概要
- 環境構築不要な「Kernel」の使い方
- 入門 10 Kernel
  - 1. まずはsubmit！ 順位表に載ってみよう
  - 2. 全体像を把握！ submitまでの処理の流れを見てみよう
  - 3. ここで差がつく！ 仮説に基づいて新しい特徴量を作ってみよう
  - 4. 勾配ブースティングが最強？！ いろいろな機械学習アルゴリズムを使ってみよう
  - 5. 機械学習アルゴリズムのお気持ち？！ ハイパーパラメータを調整してみよう
  - 6. submitのその前に！ 「Cross Validation」の大切さを知ろう
  - 7. 三人寄れば文殊の知恵！ アンサンブルを体験しよう
  - 8. Titanicの先へ行く①！ 複数テーブルを結合してみよう
  - 9. Titanicの先へ行く②！ 画像データに触れてみよう
  - 10. Titanicの先へ行く③！ テキストデータに触れてみよう
- メダルが獲得できる開催中のコンペティションに参加しよう
- さらなる学びのために

Kaggleの入門というと、チュートリアルとして用意されている「Titanic : Machine Learning from Disaster」が有名です。今回も最初はTitanicを題材に話を進めます。しかし個人的には、メダルが獲得できる開催中のコンペティションに参加してこそ、学びや楽しみも大きいのではないかと感じています。

本記事を経て、少しでも多くの方が開催中のコンテストに参加してくださったら嬉しいです。なお本記事執筆の背景はポエム要素を含むので、[はてなブログ](https://upura.hatenablog.com)に掲載しています。

# Kaggleの概要

[Kaggle](https://www.kaggle.com/)とは、主に機械学習モデルを構築するコンペティションのプラットフォームです。

![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/d78df200-d93c-30d9-d3a1-1b336010a8f9.png)
（DeNAでデータサイエンスチーム（通称Kaggle枠）のマネージャを務める原田さんの[資料](https://www.slideshare.net/HaradaKei/devsumi-2018summer)より引用）

キスモ取締役の大越さんの[資料](https://www.slideshare.net/ssuserafaae8/for-manabiya?ref=https://www.kysmo.tech/news/press24/)も、Kaggleとは何かが簡潔にまとめられています。原田さんの資料と合わせて、最初にご覧いただくのがオススメです。

# 環境構築不要な「Kernel」の使い方

## Kernelとは？

Kaggleには、Kernelと呼ばれるブラウザ上の実行環境が用意されています。言語としては現在、Python3とRが対応しています。それぞれScript形式かNotebook形式を選択可能です。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/71117865-ef5d-7d33-04fc-6c437c82d092.png)
Kernelには、機械学習モデルの構築に必要なさまざまなパッケージがあらかじめインストールされており、初心者がつまづきやすい環境構築が必要ありません。RAMは16Gあり、GPUも使用可能です。一般的なノートパソコン以上の性能が自由に使える環境が整っています。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/e4ac4f7e-cafa-56f0-2042-e5f6404c555d.png)

本記事では、このKernelを用いたKaggle入門コンテンツを提供します。
自分で手を動かしながらKaggleのエッセンスを学べるような10つのKernelを用意しました。
言語としてはPython3、形式はNotebookを選択します。

## Kernelの使い方

ここでは、Kernelの具体的な使い方を解説します。
次の章にある「1. まずはsubmit！ 順位表に載ってみよう」のリンクをクリックして、作業してみてください。

リンクを開くと、次のようなKernelのページが開きます。まずは右上の「Fork」をクリックしてください。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/e24a553b-799e-1528-ea57-4709ce282172.png)

すると、自分で編集できる画面に遷移します。ForkしたKernelは元のKernelとは別物なので、自分の好き勝手に編集して問題ありません。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/01d6d44b-cc15-41c8-77dc-fbe80744bf2b.png)

Kernelは「Public」「Private」という公開設定があります。現在の状況は右のサイドバー＞Settings＞Sharingから確認できます。例えば、私のKennelは皆さんに使ってもらうために「Public」になっています。デフォルトは「Private」なので、意図的に操作しない限りは「Public」にはなりません。安心して自由に記述することが可能です。

Kernelはいくつものセルに分割されています。セルには2種類あり、1つは説明文などを記述する「Markdown」、もう1つはPythonのコードを記述する「Code」です。次の写真で言うと、上のセルがMarkdown、下のセルがCodeです。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/bfd1d505-e6f6-ed34-4338-71eca815bc31.png)

セルは自由に追加・削除ができます。新規追加は上の画像で出ている「+Code」「+Markdown」から可能で、移動・削除はセルを選択した状態でメニューバーの「Edit」「Insert」から操作できます。

Codeセル内でSHIFT+ENTERすると、個々の単位でプログラムを実行できます。段階的にプログラムを処理できるので、個々のセルで何が起きているかが理解しやすいかと思います。

Kernelの操作方法やショートカットなどは、Jupyter Notebookとほぼ同様です。さらなる便利な使い方の詳細が知りたい場合は「Jupyter Notebook 使い方」などで調べると良いでしょう。

# 入門 10 Kernel

ここでは、自分で手を動かしながらKaggleのエッセンスを学べるような10つのKernelを掲載します。

本記事内では理論的な面を解説し、各テーマに対応するKernelで実践していただく構成になっています。本記事を読むだけでも理解できるような構成にしていますが、ぜひKernelをForkしてご自身で操作してみてください。

現在、最初の2つのKernelを公開しています。今後、随時更新予定です。

## [1. まずはsubmit！ 順位表に載ってみよう](https://www.kaggle.com/sishihara/upura-kaggle-tutorial-01-first-submission)

この[Kernel](https://www.kaggle.com/sishihara/upura-kaggle-tutorial-01-first-submission)では、Kaggleでのsubmitの方法を学びます。

Kaggleでは、いくつかの方法で自分が作成した機械学習モデルの予測結果をsubmit可能です。（Kernel経由でしかsubmitできないコンペティションも存在します）

- Kernel経由
- csvファイルを直接アップロード
- [Kaggle API](https://github.com/Kaggle/kaggle-api)を利用

今回は、Kernel経由でsubmitしてみましょう。

このKernelにはいろいろなセルが含まれていますが、一旦は何も考えずに右上の「COMMIT」をクリックしてみてください。

次のような画面が立ち上がり、Kernel全体が実行されます。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/e13b7277-7249-0184-0360-041399c734fe.png)

実行が終わったら「Open Version」をクリックしましょう。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/f5e3c35a-1b38-aae7-743e-91a0ba484c13.png)

実行されたKernelの情報が表示されています。KernelはCOMMITするごとに、自動的にバージョンが管理されます。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/2aa139f2-a8e9-ce72-f8ab-007d0a5b2053.png)

左の「Output」タブを押すと、このバージョンのKernelでの予測結果が「submission.csv」というファイルで保存されています。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/a2e8055a-6111-de31-220e-a15ac9164f48.png)

「Submit to Competition」を押すと、このファイルがsubmitされます。スコアが計算され、今回の場合は「0.66507」という値が算出されています。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/637a2e65-f460-68d1-01a0-2f719724b965.png)

無事にスコアが付いたので、順位表にも自分のアカウントが登場しました。
![image.png](https://qiita-image-store.s3.amazonaws.com/0/322566/40b98d60-db64-8448-e612-f24504856941.png)

このKernelでは、Kernel経由でsubmitする方法を学びました。「Output」タブから「submission.csv」をダウンロードすることも可能なので、csvファイルを直接アップロードする方法も試してみてください。

なおKaggle APIを利用してsubmitする方法に興味があれば、こちらの[ブログ](http://www.currypurin.com/entry/2018/kaggle-api)などをご覧ください。

## [2. 全体像を把握！ submitまでの処理の流れを見てみよう](https://www.kaggle.com/sishihara/upura-kaggle-tutorial-02-overview)

この[Kernel](https://www.kaggle.com/sishihara/upura-kaggle-tutorial-02-overview)では、前回は一旦無視したKernelの処理の流れを具体的に見ていきます。ぜひ、実際に一番上からセルを実行しながら読み進めてみてください。

具体的な処理の流れは、次のようになっています。

1. パッケージの読み込み
2. データの読み込み
3. 特徴量エンジニアリング
4. 機械学習アルゴリズムの学習・予測
5. submit（提出）

このKernelでは、submitに向けたKaggleでの処理の流れを追いました。

次のKernelでは特徴量エンジニアリングの部分に手を加え、スコアの向上を体験してみましょう。

##  3. ここで差がつく！ 仮説に基づいて新しい特徴量を作ってみよう

##  4. 勾配ブースティングが最強？！ いろいろな機械学習アルゴリズムを使ってみよう

##  5. 機械学習アルゴリズムのお気持ち？！ ハイパーパラメータを調整してみよう

https://nykergoto.hatenablog.jp/entry/2019/03/29/%E5%8B%BE%E9%85%8D%E3%83%96%E3%83%BC%E3%82%B9%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%A7%E5%A4%A7%E4%BA%8B%E3%81%AA%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1

##  6. submitのその前に！ 「Cross Validation」の大切さを知ろう

##  7. 三人寄れば文殊の知恵！ アンサンブルを体験しよう

##  8. Titanicの先へ行く①！ 複数テーブルを結合してみよう

##  9. Titanicの先へ行く②！ 画像データに触れてみよう

##  10. Titanicの先へ行く③！ テキストデータに触れてみよう

# メダルが獲得できる開催中のコンペティションに参加しよう



#  さらなる学びのために

最後に、さらなる学びに向けたリンクをいくつか掲載します。

## [kagger-ja slack](https://kaggler-ja.herokuapp.com/)

主に日本人のKagglerが集まっているSlackのワークスペースです。質問が飛び交うチャンネルやコンペティションの解法を共有するチャンネルなどが活発で、参加して閲覧しているだけでも多くの知見が得られると思います。メールアドレスをフォームに入力するだけで、誰でも参加可能です。

過去ログは[こちら](https://kaggler-ja-slack-archive.appspot.com/)で公開されています。

## [kaggler-ja wiki](http://kaggler-ja-wiki.herokuapp.com/)

kagger-ja slackで話題になった内容などを体系的にまとめたページです。次のようなコンテンツがまとめられています。

- kaggle初心者ガイド
- なんでもkaggle関連リンク
- よくある質問
- 過去コンペ情報

## Kaggle Tokyo Meetupの動画・資料

Kaggle Tokyo Meetupは、Kagglerが一堂に会すイベントです。上位に入賞した方が解法をプレゼンしたり、多種多様なLTがあったり、学びの多いイベントです。

過去5回開催されており、特に第4回は動画も公開されているのでオススメです。

- #1 [資料](https://atnd.org/events/74953)
- #2 [資料](https://techplay.jp/event/613561)
- #3 [資料](http://yutori-datascience.hatenablog.com/entry/2017/10/29/205433)
- #4 [資料](https://connpass.com/event/82458/presentation/), [動画](https://www.youtube.com/watch?v=VMjnhGW2MgU&list=PLkBjLQIGEjJlciM9lEz1AsuZZ8lDgyxDu)
- #5 [資料](https://connpass.com/event/105298/presentation/)

## [tkm2261さんのKaggle入門動画](http://yutori-datascience.hatenablog.com/entry/2017/10/24/215647)

次のコンテンツが動画で用意されています。

- Kaggleについて
- Porto Seguroコンペについて
- GCP立ち上げ（アカウント作ると付いてくる$300クーポン使用）
- Bitbucketでgitリポジトリ作成
- GCPの使い方
- Ubuntuセットアップ
- Anacondaセットアップ
- Pythonコーディング (Pandas, scikit-learn, xgboost)
- Gitの使い方
- loggerの使い方
- ロジスティック回帰
- Cross Validation解説
- Grid Search解説
- xgboost解説
- on hot encoding解説
- Kaggleの提出方法
- おまけ: 私の過去コンペのコードの解説

## [twitter Kaggle リスト](https://mobile.twitter.com/upura0/lists/kaggle1)

私が日々見ているKagglerを集めたtwitterのリストです。Kaggleに取り組む方々の日常から、さまざまな刺激を受けています。

# おわりに

本記事では「Kaggleに登録したら次にやること」と題して、Kaggleに入門したい方に向けた情報を掲載しました。少しでも多くの方のお役に立てていれば幸いです。

Kaggle入門者に向けたより良いコンテンツになるよう、随時更新を重ねていきたいと思います。
