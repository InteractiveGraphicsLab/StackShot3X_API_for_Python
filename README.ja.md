# StackShot3X API for Python
[**English**](./README.md)

StackShot3Xを操作するためのPython用API


# Environment
+ Python 3.8
+ PyFtdi 0.54.0


# Setup
+ StackShot3Xを操作するためには，USBドライバとしてlibusb-win32またはlibusbKをインストールする必要がある．以下に，[Zadig](https://zadig.akeo.ie/)を用いたドライバのインストール手順を示す．
	1. Zadigを起動し，*Options > List All Devices*を選択する．<br>
	![](/images/step1.png)

	1. デバイスのリストからStackShot3Xを選択する．<br>
	![](/images/step2.png)

	1. ドライバの種類をlibusb-win32またはlibusbKに設定し，*Replace Driver*を選択する．<br>
	![](/images/step3.png)

+ 本モジュールに必要なパッケージをインストールする
	```
	pip install pyftdi
	```

+ PySide6をインストールすることで，テスト用のGUIを用いてStackShot3Xを操作できる．
	```
	pip install PySide6
	python test.py
	```


# APIs
以下は，[こちら](https://www.cognisys-inc.com/downloads/stackshot/StackShotCommands_1_2.pdf)を参考に実装したものである．


## class StackShotController

### open(device=None)

> USBで接続されているStackShot3Xと通信を始める．
> `device`に指定した端末と通信を始める．
> 端末を指定しない(`device=None`)場合，USBで接続されているStackShot3Xのいずれかと通信を始める．
>
> 引数:
> - `device(Device)`: FTDI USBデバイス(PyUSBのインスタンス)
> 
> 返り値の型: `None`


### close()

> StackShot3Xとの通信を閉じる．  
>
> 返り値の型: `None`


### get_status(axis)

> `axis`に指定したStackShotの状態を取得する．
>
> 引数:
> - `axis(RailAxis)`: レールの軸
>
> 返り値の型: `RailStatus`
>
> 返り値: レールの状態

### move(axis, dir, dist, units)

> `axis`に指定したStackShotを動かす.
>
> 引数:
> - `axis(RailAxis)`: 動かすStackShot
> - `dir(RailDir)`: 動かす方向
> - `dist(float)`: 動かす距離
> - `units(RailUnits)`: distで指定した距離の単位
>
> 返り値の型: `None`


### stop(axis)

> `axis`に指定したStackShotの移動を停止する．
>
> 引数:
> - `axis(RailAxis)`: 停止するStackShot
>
> 返り値の型: `None`

### shutter(num_pulses, pulse_duration, pulse_off_time)

> カメラのシャッターを発火させる．  
>
> 引数:
> - `num_pulses(int)`: The number of pulses to generate on the shutter output.
> - `pulse_duration(float)`: The "on" time of each pulse, in seconds.
> - `pulse_off_time(float)`: The "off" time of each pulse, in seconds.
>
> 返り値の型: `None`


## class RailStatus

特定の軸におけるレールの状態を表す列挙型


## class StackShotStatus

StackShot3Xの状態を表す列挙型


## class RailAxis

StackShot3Xのレールの軸を表す列挙型


## class Cmd

StackShot3Xにおける各コマンドを表す列挙型


## class Action

StackShot3Xに対する挙動を表す列挙型


## class RailDir

レール上の進行方向を表す列挙型


## class RailUnits

レールを動かす距離の単位を表す列挙型


# 謝辞
本ソフトウエアは 日本学術振興会 科学研究費 基盤研究B 22H03710の助成を受けて開発されました.
