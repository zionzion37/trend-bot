import os
import requests
from pytrends.request import TrendReq

# 깃허브에 숨겨둔 텔레그램 정보 가져오기
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

def get_google_trends():
    pytrends = TrendReq(hl='ko-KR', tz=540)
    try:
        # 한국 기준 일별 인기 검색어 가져오기
        trending_df = pytrends.trending_searches(pn='south_korea')
        top10 = trending_df[0].tolist()[:10]
        
        message = "🔥 <b>오늘 아침 구글 트렌드 Top 10</b>\n\n"
        for i, keyword in enumerate(top10, 1):
            message += f"{i}. {keyword}\n"
        
        send_telegram_message(message)
    except Exception as e:
        send_telegram_message(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    get_google_trends()
