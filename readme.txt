流程如下:
在src/img中存有從網路上抓下來的各種情緒的圖片(e.g. angry,happy...)
->執行face_crop.py從各個圖片取出人臉
->cmd中workon(啟動)虛擬環境tensorflow->切換到含有retrain.py的資料夾
->將已擷取出的人臉圖片資料夾搬到含有retain.py的資料夾
->cmd中輸入"python retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images"
->人臉情緒模型已建立(上一步為呼叫tensorflow訓練模型)(會建立出retrained_graph.pb,retrained_labels.txt)
->執行label.py(使用人臉情緒模型分析webcam的使用者情緒)


!!!參考影片: https://www.youtube.com/watch?v=Dqa-3N8VZbw