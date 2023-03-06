# StackShot3X API for Python


## Abstruction
---
StackShot3Xを操作するためのPython用API


## Environment
---
+ Python 3.8
+ PyFtdi 0.54.0


## Setup
---
+ StackShot3Xを操作するためには，USBドライバとしてlibusb-win32またはlibusbKをインストールする必要があります．これらは，[Zadig](https://zadig.akeo.ie/)を使うことで簡単にインストールできます．
	1. zadigを起動し，*Options > List All Devices*を選択する．
	![](/images/step1.png)

	1. デバイスのリストからStackShot3Xを選択する．
	![](/images/step2.png)

	1. ドライバの種類をlibusb-win32またはlibusbKに設定し，Replace Driverを選択する．
	![](/images/step3.png)


+ 本モジュールに必要なパッケージをインストールする
	```
	pip install pyftdi
	```


## Definisions
以下は，[こちら](https://www.cognisys-inc.com/downloads/stackshot/StackShotCommands_1_2.pdf)を参考に作成したものである．

> class RailStatus

軸の状態を表すIntEnum

> class StackShotStatus

StackShotの状態を表すIntEnum

> class RailAxis

StackShot3Xの軸を表すIntEnum

> class Cmd

StackShot3Xにおける各コマンドを表すIntEnum

> class Action

StackShot3Xに対する挙動を表すIntEnum

> class RailDir

レールの方向を表すIntEnum

> class RailUnits

レールを動かすときの距離の単位を表すIntEnum


## APIs
---
> class StackShotController

> open(device=None)

USBで接続されているStackShot3Xと通信を始める．
`device`に指定した端末と通信を始める．
端末を指定しない(`device=None`)場合，接続されているStackShot3Xのいずれかと通信を始める．

**引数**:
- `device(Device)`: FTDI USBデバイス(PyUSBのインスタンス)

**返り値の型**: `None`


> close()

接続しているStackShot3Xとの通信を閉じる．  

**返り値の型**: `None`


> rail_status(axis)

`axis`に指定した軸の状態を確認する．

**引数**:
- `axis(RailAxis)`: 状態を取得したい軸

**返り値の型**: `RailStatus`

**返り値**: 軸の状態

> move(axis, dir, dist, units)

`axis`に指定した軸を移動させる.  

**引数**:
- `axis`: 動かす軸(`RailAxis`)
- `dir`: 動かす方向(`RailDir`)
- `dist`: 動かす距離(`float`)
- `units`: distで指定した距離の単位(`RailUnits`)

**返り値の型**: `None`


> stop(axis)

`axis`に指定した軸の移動を停止させる．  

**引数**:
- `axis(RailAxis)`: 停止させる軸

**返り値の型**: `None`

> shutter(num_pulses, pulse_duration, pulse_off_time)

カメラのシャッターを発火させる．  

**引数**:
- `num_pulses(int)`: The number of pulses to generate on the shutter output.
- `pulse_duration(float)`: The "on" time of each pulse, in seconds.
- `pulse_off_time(float)`: The "off" time of each pulse, in seconds.

**返り値の型**: `None`
