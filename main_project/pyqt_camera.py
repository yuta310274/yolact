import sys
import cv2
import numpy as np
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QFrame, QWidget, QGridLayout, QLineEdit
import mediapipe as mp
import matplotlib.pyplot as plt
from PySide6.QtCore import Qt
from PySide6 import QtWidgets, QtCore, QtGui
from arrangement_widget import ArrangementWidget



class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test")

        self.main_widget = QtWidgets.QWidget(parent=self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QtWidgets.QGridLayout(self.main_widget)

        self.banner = QtWidgets.QLabel(self.main_widget)
        self.banner.setAlignment(QtCore.Qt.AlignCenter)
        self.banner.setText(
            "<font color='white'>パックを指定してください</font><br><font color='white'>組み合わせ重量<font color='yellow'>0g</font>"
        )
        self.banner_font = QtGui.QFont()
        self.banner_font.setPointSize(24)
        self.banner.setFont(self.banner_font)
        self.banner.setStyleSheet("background-color: blue")
        self.main_layout.addWidget(self.banner, 0, 0, 1, 4)

        self.frame_label = QtWidgets.QLabel(self.main_widget)
        self.main_layout.addWidget(self.frame_label, 1, 1, 1, 2)

        self.left_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.left_layout, 1, 0)

        self.pack1 = ArrangementWidget("秀・15玉", "images/strawberry1.png")
        self.pack1_font = QtGui.QFont()
        self.pack1_font.setPointSize(15)
        self.pack1.setFont(self.pack1_font)
        self.left_layout.addWidget(self.pack1)

        self.pack2 = ArrangementWidget("秀・11玉", "images/strawberry2.png")
        self.pack2_font = QtGui.QFont()
        self.pack2_font.setPointSize(15)
        self.pack2.setFont(self.pack2_font)
        self.left_layout.addWidget(self.pack2)

        self.right_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.right_layout, 1, 3)



        # 右のレイアウトを3分割、3つのレイアウトを作成
        self.sub_layout1 = QtWidgets.QVBoxLayout()
        self.sub_layout2 = QtWidgets.QVBoxLayout()
        self.sub_layout3 = QtWidgets.QVBoxLayout()

        # サブレイアウトを追加
        self.right_layout.addLayout(self.sub_layout1)
        self.right_layout.addLayout(self.sub_layout2)
        self.right_layout.addLayout(self.sub_layout3)

        # ラジオボタンの作成
        self.radio_button1 = QtWidgets.QRadioButton("秀:3玉,パック重量60g")
        self.radio_button2 = QtWidgets.QRadioButton("秀:4玉,パック重量90g")
        self.radio_button3 = QtWidgets.QRadioButton("秀:5玉,パック重量120g")

        self.font = QtGui.QFont()
        self.font.setPointSize(13)  # フォントサイズを13に設定
        self.radio_button1.setFont(self.font)
        self.radio_button2.setFont(self.font)
        self.radio_button3.setFont(self.font)


        # セット完了ボタンの作成
        self.set_button = QtWidgets.QPushButton("セット完了")

        self.sub_layout1.addWidget(self.radio_button1)
        self.sub_layout1.addWidget(self.radio_button2)
        self.sub_layout1.addWidget(self.radio_button3)
        self.sub_layout1.addWidget(self.set_button)

        self.label = QtWidgets.QLabel(self.main_widget)
        self.label.setText(f"現在のパックの状態:セットなし")
        self.label.setFont(self.font)
        self.sub_layout1.addWidget(self.label)


        # セット完了ボタンのクリックイベントと関数の接続
        self.set_button.clicked.connect(self.on_set_button_clicked)


        self.right_label = QtWidgets.QLabel(self.main_widget)
        self.right_label.setText(f"現在の合計0.00g\n0.00g: [{0}/0粒]\n")
        self.right_label_font = QtGui.QFont()
        self.right_label_font.setPointSize(24)
        self.right_label.setFont(self.right_label_font)
        self.sub_layout2.addWidget(self.right_label)

        #再計算ボタンを表示
        self.button1 = QtWidgets.QPushButton("再計算", self)


        self.button1.setStyleSheet('QPushButton {background: cyan; \
                                                height: 40px; \
                                                color: black; \
                                                font: 30px; \
                                                } \
                                   QPushButton:pressed {background: #000080}')
        self.sub_layout3.addWidget(self.button1)
        self.button1.clicked.connect(self.pushed_button1)




        #self.main_layout.addWidget(self.right_label, 1, 3)


        #super(MainWindow, self).__init__()

        #ウィンドウの設定
        #self.setWindowTitle("Full Screen Window")
        #self.setGeometry(0, 0, 800, 600)


        # ウィンドウの背景色を黒に設定
        #self.setStyleSheet("background-color: black;")



        self.h=480
        self.w=640
        self.w_trans = 1920 # 変更したいフレームの幅の値
        self.h_trans = round(self.h * (self.w_trans/self.w))

        # ディスプレイの解像度を取得
        #desktop = QApplication.desktop()
        #screen_rect = desktop.screenGeometry()
        #screen_width, screen_height = screen_rect.width(), screen_rect.height()

        # ウィンドウをディスプレイの解像度に合わせる
        #self.setGeometry(0, 0, screen_width, screen_height)
        # ウィンドウをディスプレイの解像度に合わせる
        #self.setGeometry(0, 0, self.w_trans, self.h_trans)
        # ウィジェットを作成してウィンドウに追加
        #self.label = QLabel("This is a full screen window", self)
        #self.label.setAlignment(Qt.AlignCenter)
        #self.label.setGeometry(0, 0, self.w_trans, self.h_trans)


        #self.label = QLabel(self)
        #self.label.setGeometry(0, 0, 800, 600)

        self.flag = 0
        self.flag_b = 0
        self.flag_d = 0

        # num_dets_to_considerを読み込む
        self.num_dets_to_consider = int(np.loadtxt('num_dets_to_consider.txt'))

        # instance_numberrを読み込む
        #instance_numbers = int(np.loadtxt('instance_number.txt'))
        # instance_number.txt ファイルからデータを読み込む
        self.instance_numbers = np.genfromtxt('instance_number.txt')

        # データを整数に変換
        self.instance_numbers = self.instance_numbers.astype(int)

        # boxesを読み込む
        self.boxes = np.loadtxt('boxes.txt')

        # estimated_weightsを読み込む
        self.estimated_weights = np.loadtxt('estimated_weights.txt')

        # itemsを読み込む
        #items = np.loadtxt('items.txt')
        self.items = np.load('items.npy')
        self.items = self.items.tolist()
        print(self.items)
        # lstを読み込む
        self.lst = np.loadtxt('lst.txt')

        # E_Cを読み込む
        # ファイルからデータを読み込む
        self.E_C = np.loadtxt('E_C.txt', delimiter=',', dtype={'names': ('e', 'c', 'r', 'g', 'b'), 'formats': ('<U10', '<U10', 'i', 'i', 'i')})
        #E_C = np.loadtxt('E_C.txt')

        # ウェブカメラのキャプチャを開始
        #cap = cv2.VideoCapture(0)



        self.instance_number=0
        self.instance=[]

        self.estimated_weights_position=[]
        #items=[]

        #選択したいちごを入れるリスト
        self.check = []

        #最小距離、インスタンス番号、推定重量を格納するリストを初期化する
        self.min_distances_info = [(np.inf, None, None)] * self.num_dets_to_consider



        # ウェブカメラのキャプチャを開始
        self.cap = cv2.VideoCapture(0)

        # mediapipeの準備
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils






        # タイマーを設定して、カメラ画像を更新する
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(100)  # 100 milliseconds

    #再計算ボタンを押した時の関数
    def pushed_button1(self):
        
        if self.radio_button1.isChecked():
            p,self.lst = self.knapsack(0,60)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()
            self.label = QtWidgets.QLabel(self.main_widget)
            self.label.setText(f"秀:{len(self.lst)}玉,パック重量60g")
            self.label.setFont(self.font)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")

            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>60g</font>"
            )         
        elif self.radio_button2.isChecked():
            print("選択肢2が選択されました")
            if self.label is not None:
                self.sub_layout1.removeWidget(self.label)
                self.label.deleteLater()  # 削除されたウィジェットをメモリから解放する

            p,self.lst = self.knapsack(0,90)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()            
            self.label = QtWidgets.QLabel(self.main_widget)

            self.label.setText(f"秀:{len(self.lst)}玉,パック重量90g")
            self.label.setFont(self.font)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>90g</font>"
            )

        elif self.radio_button3.isChecked():
            print("選択肢3が選択されました")
            if self.label is not None:
                self.sub_layout1.removeWidget(self.label)
                self.label.deleteLater()  # 削除されたウィジェットをメモリから解放する

            p,self.lst = self.knapsack(0,120)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()
            self.label = QtWidgets.QLabel(self.main_widget)

            self.label.setText(f"秀:{len(self.lst)}玉,パック重量120g")
            self.label.setFont(self.font)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>120g</font>"
            )
        else:
            print("再計算出来ません")

    #ラジオボタンが押された時の関数
    def on_set_button_clicked(self):
        if self.radio_button1.isChecked():
            print("選択肢1が選択されました")
            if self.label is not None:
                self.sub_layout1.removeWidget(self.label)
                self.label.deleteLater()  # 削除されたウィジェットをメモリから解放する

            p,self.lst = self.knapsack(0,60)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()
            self.label = QtWidgets.QLabel(self.main_widget)
            self.label.setText(f"秀:{len(self.lst)}玉,パック重量60g")
            self.label.setFont(self.font)
            self.sub_layout1.addWidget(self.label)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>60g</font>"
            )


        elif self.radio_button2.isChecked():
            print("選択肢2が選択されました")
            if self.label is not None:
                self.sub_layout1.removeWidget(self.label)
                self.label.deleteLater()  # 削除されたウィジェットをメモリから解放する

            p,self.lst = self.knapsack(0,90)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()            
            self.label = QtWidgets.QLabel(self.main_widget)
            self.label.setText(f"秀:{len(self.lst)}玉,パック重量90g")
            self.label.setFont(self.font)
            self.sub_layout1.addWidget(self.label)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>90g</font>"
            )

        elif self.radio_button3.isChecked():
            print("選択肢3が選択されました")
            if self.label is not None:
                self.sub_layout1.removeWidget(self.label)
                self.label.deleteLater()  # 削除されたウィジェットをメモリから解放する

            p,self.lst = self.knapsack(0,120)
            print(self.lst)
            self.lst_d(self.lst,self.estimated_weights_position,self.img_numpy,self.check)
            self.flag+=1
            self.check.clear()
            self.label = QtWidgets.QLabel(self.main_widget)
            self.label.setText(f"秀:{len(self.lst)}玉,パック重量120g")
            self.label.setFont(self.font)
            self.sub_layout1.addWidget(self.label)
            self.right_label.setText(f"合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
            self.banner.setText(
                f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>120g</font>"
            )
        else:
            print("どの選択肢も選択されていません")



    def set_frame(self, img_np):
        h, w, ch = img_np.shape
        bytes_per_line = ch * w

        q_img = QtGui.QImage(img_np.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(q_img)
        self.frame_label.setPixmap(pixmap.scaled(800, 600))

    def set_right_label(self, text):
        self.right_label.setText(text)


    #ナップサック関数
    def knapsack(self,i, w):
        if i>=len(self.items):
            return 0,[]
        elif  w - self.items[i][0] < 0.0:
            return self.knapsack(i+1, w)
        else:
            p1,l1 = self.knapsack(i+1, w)
            p2,l2 = self.knapsack(i+1, w - self.items[i][0]) 
            p2 += self.items[i][1]
            l2.append(i)
        if p1>p2:
            return p1,l1
        else:
            return p2,l2

    #ナップサックの結果を表示する関数
    def lst_d(self,lst,estimated_weights_position,img_numpy,check):

        for j in lst:

            
            for s,t in enumerate(estimated_weights_position):
                
                if estimated_weights_position[s][0]==self.items[j][0]:
                    if j < len(estimated_weights_position):

                        v1=estimated_weights_position[j][1]
                        u1=estimated_weights_position[j][2]
                        v2=estimated_weights_position[j][3]
                        u2=estimated_weights_position[j][4]
                        
                        found_match = False
                        for item in check:
                            if item[1] == self.items[j][0]:
                                found_match = True
                                
                                break 

                        if found_match:
                            pass

                        else:
                            cv2.rectangle(img_numpy, (v1-3, u1-3), (v2+3, u2+3),(0,255,255) , 1)
                            
            





    def update_frame(self):

        ret, img_numpy1 = self.cap.read()

        if ret:



            # ウェブカメラからフレームをキャプチャ
            ret, img_numpy1 = self.cap.read()
            # フレームの回転（180度）
            img_numpy = cv2.rotate(img_numpy1, cv2.ROTATE_180)


            # 画像をRGB形式に変換
            img_numpy = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2RGB)

            # リサイズ
            img_numpy = cv2.resize(img_numpy, (640, 480))  # mediapipeが適切に処理するためのリサイズ 

            for j in reversed(range(self.num_dets_to_consider)):
        
            
                x1, y1, x2, y2 = self.boxes[j, :]

                x1=int(x1)
                y1=int(y1)
                x2=int(x2)
                y2=int(y2)
                '''
                x1_scaled = int(x1 * w_trans / w)
                y1_scaled = int(y1 * h_trans / h)
                x2_scaled = int(x2 * w_trans / w)
                y2_scaled = int(y2 * h_trans / h)
                '''

                estimated_weight = self.estimated_weights[j]
 
                instance_number = self.instance_numbers[j]


                k="g"

                e_c = self.E_C[j]
                #print(e_c)
                #sys.exit()
                color1 = np.array([e_c[2],e_c[3],e_c[4]])
                color1=color1.tolist()
                #color1=e_c[2]
                #color_1 = (color1[0], color1[1], color1[2])

                #text_str = '%s:%.2f' % (instance_number,area) if args.display_scores else _class
                #text_str = '%s:%s' % (e,c) 
                text_str = '{}:{}:{}'.format(instance_number, e_c[0], e_c[1])
                #text_str = '%s' % (c) if args.display_scores else _class
                #text_str1 = '%.1f%s' % (estimated_weight,k)
                text_str1 = '{:.1f}{}'.format(estimated_weight, k)
                #text_str = '%s: %.2f: %.2f' % (_class, score,area) if args.display_scores else _class
                font_face = cv2.FONT_HERSHEY_DUPLEX
                font_scale = 0.5
                #font_scale = 0.8
                font_scale1 = 0.55
                font_thickness = 1

                text_w, text_h = cv2.getTextSize(text_str, font_face, font_scale, font_thickness)[0]

                text_pt = (int(x1), int(y1 - 5))
                #text_pt = (x1, y1 +20)
                text_pt1 = (int(x1+2), int(y1 + 25))
                text_color = [255, 255, 255]
                text_color1 = [255, 255, 255]
            
                self.estimated_weights_position.append([estimated_weight,x1,y1,x2,y2])  

                found_match = False
                for item in self.check:
                    if item[0] == instance_number:
                        found_match = True
                        break  
                

                if found_match:
                    pass

                else:
                
                    #cv2.rectangle(img_numpy, (int(x1), int(y1-3)), (int(x1 + text_w), int(y1 - text_h-3) ), color1, -1)
                    cv2.rectangle(img_numpy, (x1, y1-3), (x1 + text_w, y1 - text_h-3 ), color1, -1)
                    cv2.putText(img_numpy, text_str, text_pt, font_face, font_scale, text_color, font_thickness, cv2.LINE_AA)
                    #cv2.rectangle(img_numpy, (x1, y1), (x1 + text_w, y1 - text_h - 4), color, -1)
                    cv2.putText(img_numpy, text_str1, text_pt1, font_face, font_scale1, text_color1, font_thickness, cv2.LINE_AA)

                # バウンディングボックスの幅と高さの閾値
                threshold_width = 200
                threshold_height = 200
                #cv2.rectangle(img_numpy, (x1, y1), (x2, y2), color, 1)
                # バウンディングボックスの幅と高さが閾値以下の場合にのみ描画を行う
                if found_match:
                    pass

                else:

                    if (x2 - x1) <= threshold_width and (y2 - y1) <= threshold_height:
                        cv2.rectangle(img_numpy, (x1, y1), (x2, y2), color1, 1)

                '''    
                if estimated_weight>=20.0 and estimated_weight<200 and e_c[1]=="Ripe":
                    items.append([estimated_weight,3])
                elif estimated_weight<20.0 and estimated_weight>=17.0 and e_c[1]=="Ripe":
                    items.append([estimated_weight,5])
                else:
                    items.append([estimated_weight,1])

                '''

                        
            #if self.flag==0:

                #p,self.lst = self.knapsack(0,60)
                #print(self.lst)
                #self.lst_d(self.lst,self.estimated_weights_position,img_numpy,self.check)
            
            #self.flag+=1
            if self.flag>0:
                self.lst_d(self.lst,self.estimated_weights_position,img_numpy,self.check)
                #print("TOTAL PRICE=",p)
                #print("ITEMS : {}".format(','.join(str(items[i]) for i in lst)))


                #print("TOTAL PRICE=",p)
                #print("ITEMS : {}".format(','.join(str(items[i]) for i in lst)))

            '''
            def knapsack(i, w):
                if i>=len(items):
                    return 0,[]
                elif  w - items[i][0] < 0.0:
                    return knapsack(i+1, w)
                else:
                    p1,l1 = knapsack(i+1, w)
                    p2,l2 = knapsack(i+1, w - items[i][0]) 
                    p2 += items[i][1]
                    l2.append(i)
                if p1>p2:
                    return p1,l1
                else:
                    return p2,l2
            p,lst = knapsack(0,100)
            print("TOTAL PRICE=",p)
            print("ITEMS : {}".format(','.join(str(items[i]) for i in lst)))

            for j in lst:

                for s,t in enumerate(estimated_weights_position):
                
                    if estimated_weights_position[s][0]==items[j][0]:
                        if j < len(estimated_weights_position):

                            v1=estimated_weights_position[j][1]
                            u1=estimated_weights_position[j][2]
                            v2=estimated_weights_position[j][3]
                            u2=estimated_weights_position[j][4]
                            cv2.rectangle(img_numpy, (v1-3, u1-3), (v2+3, u2+3),(255,255,0) , 1)
           '''
            # 手のランドマークを取得し、描画

            results = self.hands.process(img_numpy)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i, lm in enumerate(hand_landmarks.landmark):
                        height, width, channel = img_numpy.shape
                        cx, cy = int(lm.x * width), int(lm.y * height)
                        cv2.putText(img_numpy, str(i + 1), (cx + 10, cy + 10), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv2.LINE_AA)
                        cv2.circle(img_numpy, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                    self.mp_draw.draw_landmarks(img_numpy, hand_landmarks, self.mp_hands.HAND_CONNECTIONS) 

                    for j in reversed(range(self.num_dets_to_consider)):


                        instance_number=self.instance_numbers[j]
                        estimated_weight = self.estimated_weights[j]
            
                        x1, y1, x2, y2 = self.boxes[j, :]

                        x1=int(x1)
                        y1=int(y1)
                        x2=int(x2)
                        y2=int(y2)

                        # バウンディングボックスの中心座標を計算
                        center_x = (x1 + x2) // 2
                        center_y = (y1 + y2) // 2


                        '''
                        # 三平方の定理より，一指し指の先端との直線距離を計算
                        distance = np.sqrt((center_x - int(hand_landmarks.landmark[8].x ))**2 + (
                            center_y - int(hand_landmarks.landmark[8].y ))**2)
                        '''
                        # ユークリッド距離の計算
                        #distance = np.linalg.norm(hand_landmarks.landmark[8] - hand_landmarks.landmark[4])
                        #print(distance)
                        # 手のランドマークから親指と人差し指の先端の座標を取得
                        thumb_tip = np.array([hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x, hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y])
                        index_tip = np.array([hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x, hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y])
                    
                        # 人差し指の先端の座標を取得
                        index_tip_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
                        index_tip_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)


                        # 親指の先端の座標を取得
                        thumb_tip_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * width)
                        thumb_tip_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * height)



                        # ユークリッド距離の計算
                        distance = np.linalg.norm(thumb_tip - index_tip)

                        if distance < 0.1:
                            self.flag_d = 1

                        # バウンディングボックス内に人差し指があるか判定する
                        inside_x_range = x1 <= index_tip_x <= x2
                        inside_y_range = y1 <= index_tip_y <= y2

                        is_inside_box = inside_x_range and inside_y_range

                        # バウンディングボックス内に親指があるか判定する
                        inside_x_range = x1 <= thumb_tip_x <= x2
                        inside_y_range = y1 <= thumb_tip_y <= y2

                        is_thumb_box = inside_x_range and inside_y_range

                        if  is_inside_box and is_thumb_box and self.flag_d >=1:
                            self.flag_b = 1 
                        else:
                            self.flag_b = 0
                        
                        
                        if self.flag_b >=1 and self.flag_d >=1:

                            if any(self.items[lst_1][0] == estimated_weight for lst_1 in self.lst):
                                if not any(item[0] == instance_number for item in self.check):
                                    self.check.append([instance_number,estimated_weight])
                        #print(self.check)
                        print("Current check list:", self.check)

                        if not self.check:
                           
                            self.right_label.setText(f"現在の合計0.00g\n0.00g: [{0}/{len(self.lst)}粒]\n")
                        else:
                            self.total_weight = sum(item[1] for item in self.check)
                            self.right_label.setText(f"現在の合計{self.total_weight:.2f}g\n{self.check[-1][1]:.2f}g: [{len(self.check)}/{len(self.lst)}粒]\n")
                            if(len(self.check)==len((self.lst))):
                                if self.radio_button1.isChecked():
                                    self.banner.setText(
                                        f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>60g</font><br><font color='white'>パックは成立しました</font>"
                                    )
                                elif self.radio_button2.isChecked():
                                    self.banner.setText(
                                        f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>90g</font><br><font color='white'>パックは成立しました</font>"
                                    )
                                elif self.radio_button3.isChecked():
                                    self.banner.setText(
                                        f"<font color='white'>秀・{len(self.lst)}玉[M]パック（対象{len(self.lst)}粒）</font><br><font color='white'>組み合わせ重量<font color='yellow'>120g</font><br><font color='white'>パックは成立しました</font>"
                                    )
                                else:
                                    print("パックは成立していません")

                        self.sub_layout2.addWidget(self.right_label)

                        print(distance)

                        #print(instance_number,distance)



            # BGR形式に変換して描画
            #img_numpy = cv2.cvtColor(img_numpy, cv2.COLOR_RGB2BGR)



            # 新しいフレームのサイズを取得
            h, w, _ = img_numpy.shape
            h_trans = round(h * (self.w_trans/w))
        
            img_numpy = cv2.resize(img_numpy, dsize=(self.w_trans,h_trans))                      

            self.img_numpy = img_numpy

            self.set_frame(self.img_numpy)
            # ウィンドウに表示
            #h, w, ch = img_numpy.shape
            #bytes_per_line = ch * w
            #q_img = QImage(img_numpy.data, w, h, bytes_per_line, QImage.Format_RGB888)
            #pixmap = QPixmap.fromImage(q_img)
            
            # ウィンドウの中央に画像を表示
            #self.label.setPixmap(pixmap.scaled(800, 600))  # 画像のサイズをウィンドウに合わせてスケーリング
        else:
            self.cap.release()
            self.timer.stop()

if __name__ == '__main__':

    #app = QApplication(sys.argv)
    app = QtWidgets.QApplication([])
    win = MainWidget()
    #window.show()
    win.show()  # ウィンドウをフルスクリーン表示
    app.exec()
    #sys.exit(app.exec_())
