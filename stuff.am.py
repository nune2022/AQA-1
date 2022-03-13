from selenium import webdriver
import re

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://staff.am/en/jobs?JobsFilter%5Bcompany%5D=&JobsFilter%5Bkey_word%5D=&JobsFilter%5Bjob_candidate_level%5D=&JobsFilter%5Bcategory%5D=&JobsFilter%5Bcategory%5D%5B%5D=2&JobsFilter%5Bjob_type%5D=&JobsFilter%5Bsalary%5D=&JobsFilter%5Bjob_term%5D=&JobsFilter%5Bjob_city%5D=&JobsFilter%5Bsort_by%5D=0&&JobsFilter%5Bsort_by%5D=0")

qa = driver.find_elements_by_xpath('//p[/*]')
for i in qa:
    if re.findall('QA',i.text):
        f=open('staff_qa.txt', "a")
        f.write(f'{i.text}\n')
with open(r"staff_qa.txt", 'r') as fp:
      x = len(fp.readlines())
print('job announcement:', x+1)

driver.close()
