＜実行条件＞
判定したいコードの名前はa.py, b.pyなど一文字
ディレクトリ内にdataフォルダがある

＜実行方法＞
.pyコードがあるディレクトリ内で
auto.sh
を実行する
引数には

{abc or agc}{番号} {a-e}

を入れる

＜仕組み＞
yacoo/tool　内の3つのファイルにより実行される

auto.sh
→auto_check.pyファイルを実行するシェル

test.sh
→提出するpyコードを実行するシェル

auto_check.py
→メインのプログラム
1．HPからサンプル入力、出力を取得し保存
2．test.shを実行し、出力を保存
3．1と2の出力を比較し、判定を行う

＜備考＞
TLEには対応していない。実行時間が長すぎたら止めるような処理が欲しいところ
auto.shを保管しているフォルダ（tool）は環境変数PATHに追加しているため
どのフォルダでも実行が可能。
なので他にも便利なシェルを作ったらtoolに投げ込もう（kaggleの提出コードとか良いかも）

