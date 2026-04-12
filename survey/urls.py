from django.urls import path
from . import views

urlpatterns = [
    # 주소창에 아무것도 안 쳤을 때 (127.0.0.1:8000) -> 메인 화면
    path('', views.main, name='main'), 
    
    # 질문 단계들 (127.0.0.1:8000/step/1/ ...)
    path('step/<int:step>/', views.survey_step, name='survey_step'),
    
    # 결과 화면
    path('result/', views.result, name='result'),
]