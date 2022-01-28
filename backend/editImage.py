import cv2
import base64
import numpy as np
import datetime


def edit(image):
    # 画像のdataUrlをデコードする
    encoded_data = image.split(',')[1]
    img_data = base64.b64decode(encoded_data)
    img_np = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)

    # 2. 顔抽出
    # カスケード分類器の準備
    path = "/usr/local/Cellar/opencv/4.5.2_4/share/opencv4/haarcascades/"
    facecc_xml = path + "haarcascade_frontalface_alt2.xml"
    eyecc_xml = path + "haarcascade_eye.xml"
    facecc = cv2.CascadeClassifier(facecc_xml)
    eyecc = cv2.CascadeClassifier(eyecc_xml)

    # 顔を検出
    face_list = facecc.detectMultiScale(img, minSize=(20, 20))
    for (fx, fy, fw, fh) in face_list:
        face_area = img[fy:fy+fh, fx:fx+fw]
        # 顔に枠をつける
        # cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 0, 255), 1)
        # 顔を保存
        # cv2.imwrite('face_cut.jpg', face_area)
        print(face_area)

    # 目を検出
    eye_list = eyecc.detectMultiScale(img)
    for (ex, ey, ew, eh) in eye_list:
        eye_area = img[ey:ey+eh, ex:ex+ew]
        # 目に枠をつける
        # cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)

        # 目を大きくする
        big_eye = cv2.resize(eye_area, None, fx=1.3, fy=1.2)
        # 目を貼り付ける
        img[ey:ey+big_eye.shape[0],
            ex:ex+big_eye.shape[1]] = big_eye

    dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S.jpg')
    print(dt_now)
    # cv2.imwrite('out.jpg', img)

    result, dst_data = cv2.imencode('.png', img)
    dst_base64 = base64.b64encode(dst_data).decode()
    return "data:image/png;base64," + dst_base64
