'''


Reference:
    - https://ithelp.ithome.com.tw/articles/10246297
'''
from datetime import date, datetime
from gtts import gTTS
from playsound import playsound
import datetime

tts = gTTS(text='我們常常聽到的google小姐聲音，\
    即可透過gTTS來將文字轉為google語音，\
    在合成語音的資料庫當中，算是我們比較熟悉的，\
    其他也有許多使用免費的TTS服務可以搜尋得到，\
    當然也已經被大量運用在軟體開發上，\
    不過從入門開始的話，我們就先使用gTTS的應用作為示範吧', 
    lang='zh-tw',
    slow=False,
    )
d = datetime.datetime.now()


# [:19]
print(d.strftime)

tts.save("E:/audio/ex.mp3")