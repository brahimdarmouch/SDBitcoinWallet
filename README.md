SDBitcoinWallet
===========
SDBitcoinWallet is a small script that create a Bitcoin wallet
using a secure random hex, you can also fetch wallet info from
WIF key

![alt text](https://i.imgur.com/KmTrETZ.png)

Installation
-------------
First of all, you need Python 3.x <br/>
secondly, you need to install Prerequisites (in requirements.txt) :
```bash
$ pip install -r requirements.txt
```
Execution
-------------
```bash
$ python sd_wallet.py
```
Output looks like this :
```bash

$ python sd_wallet.py
======================= [ BITCOIN PRIVATE KEYS ] =======================
Hex Private Key         :  29b47e8bacf35d4533159d30bfda5775f1dc56fb2c2d926368ac219........
Decimal Private Key     :  1886373264926014189606725413642967972415009094506665993999186467........
Uncompressed Private Key:  5J8et4aCAZiJ6aMU6yAJb7cENXyEM34oxUd9hC5Vi5d........
Compressed Private Key  :  KxcnCNmWHDPGTcDLdLt4daAW23hBuS7pFrvZNPtqiKS........
======================== [ BITCOIN PUBLIC KEYS ] ========================
Uncompressed Public Key :  04b58c32f259b3e6cff51e0ba5b98086ce5437119d68187c2e4742bbc395e68d8937fcce9ecd745b46a47cddbc55f76435bb623951b9d840073646314668f45346
Compressed Public Key   :  02b58c32f259b3e6cff51e0ba5b98086ce5437119d68187c2e4742bbc395e68d89
=========================== [ BITCOIN ADDRESS ] ===========================
Uncompressed Address    :  1PGQ3yzojJ6ZFAPRAMJMyRYaGuf1pwrcyy
Compressed Address      :  19P8b6jqJXb3kVCKoLFKNsL7bV9oVDrhtL
P2SH Address            :  3GcQ2gB5aSksSFkE2MJUom7cgvf4zqrQky
BECH32 Address          :  bc1qt0c8m5h505kemduex38yr353e3yy6f5n234naz
```
In case you have the private key WIF(Wallet Import Format)<br/>
and you want to fetch wallet info, simply just uncomment the [line 53](https://github.com/brahimdarmouch/SDBitcoinWallet/blob/master/sd_wallet.py#L53) like this :
```python
hexPrv = wifToPrvHex("WIF_KEY_HERE") # 5J8et4aCAZiJ6aMU6yAJb7cENXyEM34oxUd9hC5Vi5d........
```
