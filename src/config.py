import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    STORM_PROXY_USERNAME = os.getenv('STORM_PROXY_USERNAME')
    STORM_PROXY_PASSWORD = os.getenv('STORM_PROXY_PASSWORD')
    STORM_PROXY_ENDPOINT = os.getenv('STORM_PROXY_ENDPOINT')
    
    SCRAPE_INTERVAL_MINUTES = 30
    MAX_PAGES_PER_SEARCH = 3
    DELAY_BETWEEN_REQUESTS = 5
    
    DATABASE_PATH = 'jobs.db'
    
    JOB_KEYWORDS = ['software engineer', 'developer', 'programmer']
    EXCLUDE_KEYWORDS = ['intern', 'internship']
    TARGET_LOCATIONS = ['San Francisco', 'New York', 'Remote']