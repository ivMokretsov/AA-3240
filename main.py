import requests
from dotenv import load_dotenv
import os
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Подавление предупреждений
warnings.simplefilter('ignore', InsecureRequestWarning)

load_dotenv()

# Замените эти значения на ваши данные
AWX_URL = 'https://89.169.132.192'
API_TOKEN = os.getenv('TOKEN')
JOB_TEMPLATE_ID = 7

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

# Получение информации о шаблоне задания
response = requests.get(f'{AWX_URL}/api/v2/job_templates/{JOB_TEMPLATE_ID}/', headers=headers, verify=False)

if response.status_code == 200:
    job_template = response.json()
    last_job = job_template['summary_fields']['last_job']
    print(last_job)
