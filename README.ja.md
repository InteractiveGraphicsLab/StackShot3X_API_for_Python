# StackShot3X API for Python


## 概要
PythonでStackShot3Xを操作するためのAPI


## 実行環境
+ Python 3.10.6
+ PyFtdi 0.54.0


## セットアップ
+ StackShot3Xを操作するためには，USBドライバとしてlibusb-win32またはlibusbKをインストールする必要があります．これらは，[Zadig](https://zadig.akeo.ie/)を使うことで簡単にインストールできます．
	1. zadigを起動し，*Options > List All Devices*を選択する．
	![](/images/step1.png)

	1. デバイスのリストからStackShot3Xを選択する．
	![](/images/step2.png)

	1. ドライバの種類をlibusb-win32/libusbKに設定し，Replace Driverを選択する．
	![](/images/step3.png)


+ 本モジュールに必要なパッケージをインストールする
	```
	pip install pyftdi
	```


## 使用方法
+ def open()  
StackShot3Xとの接続を開始する．
ただし，StackShot3Xが複数台接続されている場合，どの端末と接続されるかは未定義．


+ def close()  
StackShot3Xとの接続を閉じる．


+ def move(axis: RailAxis, dir: RailDir, dist: float, units: RailUnits)  
	引数で指定した軸を移動させる.  
	引数：
	- axis: 動かす軸(X/Y/Z)
	- dir: 動かす方向()
	- dist: 動かす距離
	- units: distで指定した距離の単位


+ def stop(axis: RailAxis)  
	引数で指定した軸の移動を停止させる．  
	引数：
	- axis: 停止させる軸


+ def shutter(num_pulses: int, pulse_duration: float, pulse_off_time: float)  
	カメラのシャッターを発火させる．  
	引数：
	- num_pulses: 
	- pulse_duration:
	- pulse_off_time:
