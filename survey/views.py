from django.shortcuts import render, redirect
from .utils import send_telegram_message

# 이미지 파일명은 실제 static/images/ 폴더 내 파일명과 맞춰주세요!
# survey/views.py

QUESTIONS = {
    0: { 
        'title': '',
        'sub_title': '20대 트렌드 매거진 그랩이라고 합니다!\n트렌드 리서치를 위한 그랩 길거리 인터뷰에\n응해주셔서 감사합니다 :)',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '몇 년 생이신가요?',
        'button_text': '> 인터뷰 시작!',
    },
    1: {
        'title': 'Q1',
        'sub_title': '길거리 인터뷰 콘텐츠 트렌드!\n알고 계시나요?',
        'type': 'radio',
        'options': ['나에게 온다면 어떻게 대답할지 상상한다.', '본 적도 들은 적도 없다.', '기타'],
        'img': 'thank_you_icon.png',
    },
    2: {  
        'title': 'Q2',
        'sub_title': '응답자의 MBTI를 알려주세요!',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': 'MBTI',
        'button_text': '> 다음 문제',
    },
    3: {  
        'title': 'Q3',
        'sub_title': '그랩은 혼족과 같은 메가트렌드를 예측하고자 합니다 :D\n요즘 나는 어떤 하루를 보내고,\n어떤 생각을 자주 하나요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
    4: {
        'title': 'Q4',
        'sub_title': '[취미 트렌드 조사]\n취미는 나에게?',
        'type': 'radio',
        'options': ['없으면 안돼! 스트레스를 푸는 수단~', '있으면 좋지~ 행복을 더해주는 수단!'],
        'img': 'thank_you_icon.png',
    },
    5: { 
        'title': 'Q5',
        'sub_title': '[취미 트렌드 조사]\n어떤 취미가 있으신가요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
    6: {
        'title': 'Q6',
        'sub_title': '[취미 트렌드 조사]\n나는 트렌드를 즐길 때?',
        'type': 'radio',
        'options': ['얕고 넓게 다양한 것을 즐기는 편!', '깊고 좁게, 진심으로 덕질하는 편!'],
        'img': 'thank_you_icon.png',
    },
    7: {  
        'title': 'Q7',
        'sub_title': '[취미 트렌드 조사]\n최근 즐겼던 트렌드의 흐름이 있다면요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': 'like 두쫀쿠,,,버터떡,,,',
        'button_text': '> 다음 문제',
    },
    8: {  
        'title': 'Q7',
        'sub_title': '[취미 트렌드 조사]\n하루의 언제 주로 취미를 즐기시나요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
    9: {
        'title': 'Q9',
        'sub_title': '[인테리어 트렌드 조사]\n내가 자취하면 화이트톤 vs 우드톤 vs 블랙실버모던',
        'type': 'radio',
        'options': ['올 화이트톤 !', '푸릇 싱싱 우드톤!', '블랙 실버 모던톤!', '나만의 독보적인 취향✨'],
        'img': 'thank_you_icon.png',
    },
    10: {
        'title': 'Q10',
        'sub_title': '[인테리어 트렌드 조사]\n잠깐! 무지성 밸겜 TIME!',
        'type': 'radio',
        'options': ['내가 애인 집 가기', '애인이 내 집 오기'],
        'img': 'thank_you_icon.png',
    },
    11: {
        'title': 'Q11',
        'sub_title': '[여행 트렌드 조사]\n생각만 해도 행복한 여름 방학/휴가!\n무엇을 하며 보내실 예정인가요?',
        'type': 'checkbox',
        'options': ['여행/휴식 :)', '비자발적 일정 :(', '미래를 위한 준비 !', '기타'],
        'img': 'thank_you_icon.png',
    },
    12: {  
        'title': 'Q12',
        'sub_title': '[여행 트렌드 조사]\n구체적인 계획이 있다면 알려주세요!',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
    13: {
        'title': 'Q13',
        'sub_title': '[20대 생각 트렌드 조사]\n잠깐! QUIZE TIME!\n1년 후의 나는 어떤 모습일 것 같나요?',
        'type': 'radio',
        'options': ['나만의 추구미 실현하기', '롤모델 모습에 한발짝 다가가기', '버킷릿스트 n개 이루기'],
        'img': 'thank_you_icon.png',
    },
    14: {
        'title': 'Q14',
        'sub_title': '[20대 생각 트렌드 조사]\n최근 나만의 고민 트렌드가 있다면?',
        'type': 'radio',
        'options': ["'나 이거 잘 맞나'진로 고민!", "'저 사람은 뭐가 문젤까'인간관계 고민!", "'뭐 먹고 살지'인생 고민!"],
        'img': 'thank_you_icon.png',
    },
    15: {
        'title': 'Q15',
        'sub_title': '[20대 생각 트렌드 조사]\n요즘 관심 가는 트렌드를 골라주세요!',
        'type': 'checkbox',
        'options': ['피젯토이(키캡, 스트레스볼,,,)', '디저트(두쫀쿠, 버터떡,,,)', '거지모먼트(도시락, 절약 릴스,,,)', '주식(국장, 미장, 전쟁주,,,)', '타투(미니, 레터링, 올드스쿨,,,)', '기타'],
        'img': 'thank_you_icon.png',
    },
    16: {  
        'title': 'Q16',
        'sub_title': '[20대 생각 트렌드 조사]\n나를 움직이게 하는 원동력은 무엇인가요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
    17: {  
        'title': 'Q17',
        'sub_title': '[20대 생각 트렌드 조사]\n요즘 가장 오래 붙잡고 있는 고민은?\n그 고민이 시작된 계기는 무엇인가요?',
        'type': 'text', 
        'img': 'thank_you_icon.png',
        'placeholder': '텍스트를 입력해 주세요.',
        'button_text': '> 다음 문제',
    },
}

def main(request):
    # 이 함수는 오직 '이야기 시작!' 버튼이 있는 첫 화면만 보여줍니다.
    return render(request, 'survey/main.html')

def home(request):
    if request.method == 'POST':
        request.session['survey_data'] = {}
        return redirect('survey_step', step=1)
    
    # 만약 step1.html이 따로 없고 survey_step.html을 같이 쓴다면 이름을 맞춰주세요!
    return render(request, 'survey/survey_step.html', {'step': 1, 'question': QUESTIONS[1]})

def survey_step(request, step):
    if request.method == 'POST':
        data = request.session.get('survey_data', {})
        # 질문 제목과 함께 저장해서 텔레그램에서 보기 편하게 만듭니다.
        q_title = QUESTIONS[step]["title"]
        data[f"{step}. {q_title}"] = request.POST.get('answer')
        request.session['survey_data'] = data
        
        if step < 17:  # 이제 17단계까지 갑니다!
            return redirect('survey_step', step=step + 1)
        else:
            # 17번 답변까지 완료 후 텔레그램 발송
            send_telegram_message(data)
            return redirect('result')
    
    # 해당 스텝의 질문 데이터 전달
    context = {
        'step': step,
        'question': QUESTIONS.get(step),
    }
    return render(request, 'survey/survey_step.html', context)

def result(request):
    return render(request, 'survey/result.html')