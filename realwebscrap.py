from bs4 import BeautifulSoup
import requests,time

#filter of unfamiliar skill {


# print('Put some skill that you are not familiar with')
# unfamiliar_skill= input('>')
# print(f'Filtering  Out : {unfamiliar_skill}')


#}

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    print("\n----------------JOB POSTED FEW DAYS AGO----------------\n")
    with open(f'Job_posts/job_list.txt','w') as f:
        for index,job in enumerate(jobs):
            published_date=job.find('span',class_='sim-posted').span.text
        
            #Publication Date filter
            if 'few' in published_date:

                company_name = job.find('h3', class_='joblist-comp-name').text
                skills=job.find('span',class_='srp-skills').text.lower()
                more_info=job.header.h2.a['href']

                #unfamiliar skill filter if you want to remove filter than remove if condition.
                #if unfamiliar_skill.lower() not in skills:

                f.write(f"Job Number       : {index+1}\n")
                f.write(f"Company name     : {company_name.strip()}\n")
                f.write(f"Required Skills  : {skills.strip()}\n")
                f.write(f"More Information : {more_info}\n")
                f.write("\n\n")    

        print(f'File saved : job_list.txt')
                        


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=0.5
        print(f'Waiting {time_wait} Minutes...')
        time.sleep(30)