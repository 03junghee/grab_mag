from django.shortcuts import render, redirect
from .utils import send_telegram_message

# QUESTIONS 딕셔너리는 그대로 유지하되, 흐름을 0번부터 12번까지 매끄럽게 연결합니다.
QUESTIONS = {
    0: {
        'sub_title': '길거리 인터뷰 콘텐츠 트렌드!\n알고 계시나요?',
        'type': 'radio',
        'options': ['나에게 온다면 어떻게 대답할지 상상한다.', '본 적도 들은 적도 없다.', '기타'],
        'img': 'https://i.imgur.com/enmH0m1.jpeg',
        'button_text': '> 다음 문제',
    },
    1: {  
        'sub_title': '<span style="font-size: 15px; font-weight: 500;">그랩은 혼족과 같은 메가트렌드를 예측하고자 합니다 :D</span>\n요즘 나는 어떤 하루를 보내고,\n어떤 생각을 자주 하나요?',
        'type': 'radio',
        'img': 'https://i.imgur.com/MTw0c4O.jpeg',
        'options': ['남들과 비슷한 듯 평범한 일상~', '남들과는 다른 나만의 특별한 일상!'],
        'button_text': '> 다음 문제',
    },
    2: {
        'sub_title': '[인테리어 트렌드 조사]\n내가 자취하면?',
        'type': 'radio',
        'options': ['블랙 엔 화이트 모던톤!', '푸릇 싱싱 우드톤!', '나만의 독보적인 취향✨'],
        'img': 'https://i.imgur.com/7HoVQ2u.jpeg',
        'button_text': '> 다음 문제',
    },
    3: {
        'sub_title': '[취미 트렌드 조사]\n나는 트렌드를 즐길 때?',
        'type': 'radio',
        'options': ['얕고 넓게 다양한 것을 즐기는 편!', '깊고 좁게, 진심으로 덕질하는 편!'],
        'img': 'https://i.imgur.com/E5u2eGv.jpeg',
        'button_text': '> 다음 문제',
    },    
    4: {
        'sub_title': '[취미 트렌드 조사]\n취미는 나에게?',
        'type': 'radio',
        'options': ['없으면 안돼! 스트레스를 푸는 수단~', '있으면 좋지~ 행복을 더해주는 수단!'],
        'img': 'https://i.imgur.com/BjNmt6M.jpeg',
        'button_text': '> 다음 문제',
    },    
    5: {  
        'sub_title': '[취미 트렌드 조사]\n하루의 언제 주로 취미를 즐기시나요?',
        'type': 'radio',
        'img': 'https://i.imgur.com/duuRlU9.jpeg',
        'options': ['하루의 시작, 아침', '여유로운 낮 시간대', '모든 일과가 끝난 저녁시간'],
        'button_text': '> 다음 문제',
    },    
    6: { 
        'sub_title': '[디저트 트렌드 조사]\n두쫀쿠, 버터떡.. 많은 디저트가 유행하고 있는데요!',
        'type': 'radio',
        'img': 'https://i.imgur.com/hezby3K.jpeg',
        'options': ['직접 사먹기', '애인이 사줘서 먹기', '친구들과 함께 있을 때 사먹기'],
        'button_text': '> 다음 문제',
    },    
    7: {
        'sub_title': '[여행 트렌드 조사]\n생각만 해도 행복한 여름 방학/휴가!\n무엇을 하며 보내실 예정인가요?',
        'type': 'radio',
        'options': ['여행/휴식 :)', '비자발적 일정 :(', '미래를 위한 준비 !'],
        'img': 'https://i.imgur.com/wWPu820.jpeg',
        'button_text': '> 다음 문제',
    },
    8: {
        'sub_title': '[20대 생각 트렌드 조사]\n1년 후의 나는 어떤 모습일 것 같나요?',
        'type': 'radio',
        'options': ['나만의 추구미 실현하기', '롤모델 모습에 한발짝 다가가기', '버킷리스트 n개 이루기'],
        'img': 'https://i.imgur.com/TemSdBU.jpeg',
        'button_text': '> 다음 문제',
    },    
    9: {
        'sub_title': '[20대 생각 트렌드 조사]\n최근 나만의 고민 트렌드가 있다면?',
        'type': 'radio',
        'options': ["'나 이거 잘 맞나'진로 고민!", "'저 사람은 뭐가 문젤까'인간관계 고민!", "'뭐 먹고 살지'인생 고민!"],
        'img': 'https://i.imgur.com/nQQKbAK.jpeg',
        'button_text': '> 다음 문제',
    },
    10: {
        'sub_title': '[20대 생각 트렌드 조사]\n요즘 관심 가는 트렌드를 골라주세요!',
        'type': 'checkbox',
        'options': ['피젯토이(키캡, 스트레스볼...)', '디저트(두쫀쿠, 버터떡...)', '거지모먼트(도시락, 절약 릴스...)', '주식(국장, 미장, 전쟁주...)', '타투(미니, 레터링, 올드스쿨...)', '기타'],
        'img': '',
        'button_text': '> 다음 문제',
    },
    11: {
        'title': '인터뷰 만족도',
        'sub_title': '참여해주셔서 감사합니다 :)\n인터뷰 만족도 조사 한번 부탁드려요!',
        'type': 'score', 
        'img': 'https://i.imgur.com/Loh8PoD.jpeg',
        'button_text': '다음 문제',
    },
    12: {
        'title': '마지막으로 정보를 입력해주세요!',
        'type': 'final_contact',
        'fields': [
            {'name': 'name', 'label': '이름(닉네임)', 'placeholder': '홍길동'},
            {'name': 'phone', 'label': '연락처(선택)', 'placeholder': '010-0000-0000'}
        ],
        'button_text': '완료하기',
    }
}

def main(request):
    return render(request, 'survey/main.html')

def home(request):
    if request.method == 'POST':
        request.session['survey_data'] = {}
        # 첫 번째 질문인 0번부터 시작하도록 수정합니다.
        return redirect('survey_step', step=0)
    
    return render(request, 'survey/survey_step.html', {'step': 0, 'question': QUESTIONS[0]})

def survey_step(request, step):
    question_info = QUESTIONS.get(step)
    
    # 예외 처리: 존재하지 않는 단계 요청 시 메인으로
    if not question_info:
        return redirect('main')

    if request.method == 'POST':
        data = request.session.get('survey_data', {})
        
        q_title = question_info.get("title", f"Q{step}")
        q_sub_title = question_info.get("sub_title", "").replace('\n', ' ')
        
        # [수정] 타입별 데이터 저장 로직 세분화
        if question_info.get('type') == 'checkbox':
            answer = request.POST.getlist('answer')
            data[f"[{step}. {q_title}] {q_sub_title}"] = answer
        elif question_info.get('type') == 'final_contact':
            # 12번 단계: 'answer'가 아니라 fields에 정의된 name들로 데이터를 직접 가져옵니다.
            contact_info = {
                'name': request.POST.get('name', '').strip(),
                'phone': request.POST.get('phone', '').strip()
            }
            data[f"[{step}. {q_title}]"] = contact_info
        else:
            answer = request.POST.get('answer')
            data[f"[{step}. {q_title}] {q_sub_title}"] = answer
            
        request.session['survey_data'] = data
        
        # [수정] 단계별 이동 흐름 제어 (최대 인덱스 12 기준)
        if step < 11:
            # 0~10단계는 다음 질문으로
            return redirect('survey_step', step=step + 1)
        
        elif step == 11:
            # 11단계(만족도) 완료 후 중간 결과 페이지(result)로 이동
            return redirect('result')
        
        elif step == 12:
            # 12단계(연락처) 완료 후 텔레그램 발송 및 세션 초기화
            send_telegram_message(data)
            if 'survey_data' in request.session:
                del request.session['survey_data']
            return redirect('main') 

    # GET 요청 처리
    context = {
        'step': step,
        'question': question_info,
        'score_range': range(11),
    }
    return render(request, 'survey/survey_step.html', context)

def result(request):
    # result.html 내부의 '확인/다음' 버튼은 POST 방식으로 url 'survey_step' step=12 로 요청해야 합니다.
    return render(request, 'survey/result.html')