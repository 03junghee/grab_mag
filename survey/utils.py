import requests

# 함수 정의 부분 (보통 utils.py 또는 views.py 상단)
def send_telegram_message(survey_data): # 인자를 1개만 받도록 수정
    bot_token = '8591374168:AAFEtiCnK4Nw8wRfMGKUShzqf4JoSbbR0wQ'
    chat_id = '8412088648'
    
    message = "🔔 **[Grab Magazine] 새로운 인터뷰 응답 도착!**\n"
    message += "━━━━━━━━━━━━━━━━━━━━\n"

    for key, value in survey_data.items():
        # 이미 views.py에서 key에 질문 제목을 넣어줬으므로 그대로 출력합니다.
        message += f"**{key}**\n"
        message += f"└ 답변: {value}\n\n"
    
    message += "━━━━━━━━━━━━━━━━━━━━"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    try:
        requests.post(url, data={'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'})
    except Exception as e:
        print(f"연결 오류: {e}")