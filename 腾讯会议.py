import os
import pandas as pd
import pyautogui
import time
from datetime import datetime
import cv2
def imgAutoCick(tempFile, whatDo, debug=False):
    '''
        temFile :需要匹配的小图
        whatDo  :需要的操作
                pyautogui.moveTo(w/2, h/2)# 基本移动
                pyautogui.click()  # 左键单击
                pyautogui.doubleClick()  # 左键双击
                pyautogui.rightClick() # 右键单击
                pyautogui.middleClick() # 中键单击
                pyautogui.tripleClick() # 鼠标当前位置3击
                pyautogui.scroll(10) # 滚轮往上滚10， 注意方向， 负值往下滑
        更多详情：https://blog.csdn.net/weixin_43430036/article/details/84650938
        debug   :是否开启显示调试窗口
    '''
    pyautogui.screenshot('big.png')
    gray = cv2.imread("big.png",0)
    img_template = cv2.imread(tempFile,0)
    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top+h/2, left+w/2)
    whatDo(x)

    if debug:
        img = cv2.imread("big.png",1)
        cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    os.remove("big.png")
    
def signIn(meeting_id):
    '''
    本模块主要引入腾讯会议号，进入会议之中；
    '''
    # 这一步是使用腾讯会议的绝对路径调用并启动腾讯会议
    os.startfile("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
    time.sleep(7)# 等待启动
    imgAutoCick("joinbtn.png", pyautogui.click, False)
    time.sleep(1)# 截取需要点击的地方的小
    imgAutoCick("meeting_id.png", pyautogui.click, False)
    pyautogui.write(meeting_id)
    time.sleep(2)
    imgAutoCick("final.png", pyautogui.click, False)
    time.sleep(1)

while True:
    now = datetime.now().strftime("%m-%d-%H:%M")
    if now=="01-19-10:43":
        meeting_id = '**********'# 此处填入会议号
        time.sleep(5)
        signIn(meeting_id)
        time.sleep(2)
        print('signed in')
        break
    