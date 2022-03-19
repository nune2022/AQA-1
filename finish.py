from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.phptravels.net/signup")
driver.find_element_by_xpath("//*[@name='first_name']").send_keys("Nune")
driver.find_element_by_xpath("//*[@name='last_name']").send_keys("Sargsyan")
driver.find_element_by_xpath("//*[@name='phone']").send_keys("+3743344111")
driver.find_element_by_xpath("//*[@name='email']").send_keys("finish_task1111@gmail.com")
driver.find_element_by_xpath("//*[@name='password']").send_keys("finish_task1111")
driver.execute_script("window.scrollTo(0, 500)")
sleep(10)
driver.find_element_by_xpath("//button[@type='submit']").click()







