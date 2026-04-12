import requests

def send_telegram_message(survey_data):
    # 본인의 실제 정보로 교체하세요!
    bot_token = '8591374168:AAFEtiCnK4Nw8wRfMGKUShzqf4JoSbbR0wQ'
    chat_id = '8412088648'  # 403 에러 방지를 위해 @userinfobot에서 받은 숫자 ID 입력
    
    message = "🔔 **[Grab Magazine] 새로운 인터뷰 응답 도착!**\n"
    message += "━━━━━━━━━━━━━━━━━━━━\n"
    
    for key, value in survey_data.items():
        # 질문 번호만 추출하거나 간략하게 표현
        q_label = key.split('_')[0] 
        q_title = key.split('_')[1] if '_' in key else ""
        
        message += f"**[{q_label}]** {q_title}\n"
        message += f"└ 답변: {value}\n\n"
    
    message += "━━━━━━━━━━━━━━━━━━━━"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    try:
        response = requests.post(url, data={'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'})
        if response.status_code != 200:
            print(f"텔레그램 전송 실패: {response.text}")
    except Exception as e:
        print(f"연결 오류: {e}")