import os
from dotenv_vault import load_dotenv

load_dotenv()

# APP URL
APP_URL = os.getenv('APP_URL')
APP_CATALOG_URL = os.getenv('APP_CATALOG_URL')

# CREDENTIALS
STANDARD_USER = os.getenv('STANDARD_USER')
LOCKED_OUT_USER = os.getenv('LOCKED_OUT_USER')
PROBLEM_USER = os.getenv('PROBLEM_USER')
PERFORMANCE_GLITCH_USER = os.getenv('PERFORMANCE_GLITCH_USER')
ERROR_USER = os.getenv('ERROR_USER')
VISUAL_USER = os.getenv('VISUAL_USER')

# ATTRIBUTES TEST ID
TEST_ID_ATTRIBUTE = 'data-test'
