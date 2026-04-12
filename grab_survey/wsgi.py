# grab_survey/wsgi.py (또는 프로젝트명/wsgi.py)

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grab_survey.settings')

application = get_wsgi_application()

# Vercel이 인식할 수 있도록 application을 app으로 연결
app = application