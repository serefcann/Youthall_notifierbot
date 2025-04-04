from bs4 import BeautifulSoup
import requests
import json
import os

bot_token = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']
global myfile_path
myfile_path = 'youthall_jobs_links.json'

def scrape_jobs():
    url = 'https://www.youthall.com/tr/jobs/?order=1'
    response = requests.get(url).text
    parsedHtml = BeautifulSoup(response,'html.parser')
    jobSection = parsedHtml.find('div',{'class':'l-grid u-gap-bottom-25'})
    if not jobSection:
        print('is ilanlari bolumu bulunamadi')
        return []
    jobs = jobSection.find_all('a')
    return [job.get('href') for job in jobs]

def dump_jobs(new_jobs):
    with open(myfile_path,'w+') as f:
        json.dump(new_jobs,f,ensure_ascii=False,indent=1)

def load_jobs():
    with open(myfile_path,'r') as f:
        jobs = json.load(f)
        return jobs

def get_recent_jobs(new_jobs,saved_jobs):
    new_jobsset,saved_jobsset = set(new_jobs),set(saved_jobs)
    recent_jobs = new_jobsset-saved_jobsset
    return list(recent_jobs)

bot_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

if '__main__' == __name__:
    new_jobs = scrape_jobs()
    saved_jobs = load_jobs()
    recent_jobs = get_recent_jobs(new_jobs,saved_jobs)
    if recent_jobs:
        print('yeni is ilanlari bulundu!',recent_jobs)
        for job_link in recent_jobs:
            r = requests.post(bot_url,data={'chat_id':chat_id,'text':job_link})
        if r.status_code == 200:
            print('Linkler Gonderildi')
            #dump_jobs(saved_jobs+recent_jobs)
        else:
            print('bir hata meydana geldi')
    else:
        print('yeni is ilani bulunmadi')
    
    
    





