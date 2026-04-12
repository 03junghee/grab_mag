# grab_survey/wsgi.py (실제 프로젝트 폴더 안)
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grab_survey.settings')

application = get_wsgi_application()
app = application  # 이 줄이 반드시 있어야 합니다!