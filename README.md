# yolact
 

 
# Requirement
* Windows 11 Home
* logicool webカメラ 720p
* Python 3.7.15
* torch==1.13.0+cu117
 
# Usage
 
mainプログラムの実行方法
 
```
python main.py --trained_model=weights/yolact_resnet50_strawberry_105_12722_interrupt.pth --score_threshold=0.8 --top_k=15 --video_multiframe=4 --video=0
```
 
# Note
 サブプロセスを実行するスクリプトのpathをmainプログラムの中で変更していないのでpyqt_camera.pyに変更してください

