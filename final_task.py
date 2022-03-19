from selenium import webdriver
from time import sleep
import unittest

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.phptravels.net/login')

driver.find_element_by_xpath("//*[@name='email']").send_keys("finish_task1110@gmail.com")
driver.find_element_by_xpath("//*[@name='password']").send_keys("finish_task1110")
driver.find_element_by_xpath("//*[@id='fadein']/div[1]/div/div[2]/div[2]/div/form/div[3]/button").click()
driver.find_element_by_xpath("//*[@id='fadein']/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a").click()
driver.find_element_by_xpath('//*[@id="select2-hotels_city-container"]').click()
driver.find_element_by_class_name('select2-search__field').send_keys("Yerevan")
driver.find_element_by_xpath('//*[text()="Yerevan,Armenia"]').click()
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//i[@class="la la-angle-right"]').click()
driver.switch_to.window(driver.window_handles[1])
sleep(15)
driver.execute_script("window.scrollTo(0, 500)")
sleep(15)
driver.find_element_by_xpath('//h3[@class="PropertyCard__HotelName"][text()="Kantar Hotel"]').click()
sleep(5)
driver.switch_to.window(driver.window_handles[2])
driver.find_element_by_xpath('//*[@id="hotelNavBar"]/div/div/div/div').click()
driver.find_element_by_xpath('//button[@type="button"][text()="Book now"]').click()
driver.find_element_by_xpath('//input[@id="firstName_lastName"]').send_keys("Nune Sargsyan")
driver.find_element_by_xpath('//input[@id="email"]').send_keys("finish_task1111@gmail.com")
driver.find_element_by_xpath('//input[@id="retypeEmail"]').send_keys("finish_task1111@gmail.com")
driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys("3743344111")
driver.find_element_by_xpath('//*[text()="NEXT: FINAL STEP"]').click()

class TestFinal(unittest.TestCase):
    final_step_is_done = driver.find_element_by_css_selector("[data-component=mob-flight-payment-subHeader]")
    finalStep = final_step_is_done.text
    manual_version = "All card information is fully encrypted, secure and protected."

    def setUp(self):
      print('Test case started')

    def test_payment_page(self):
        manual_vs = self.manual_version
        selenium_vs = self.finalStep
        assert manual_vs == selenium_vs

    def tearDown(self):
        print("work is done")

if __name__ == '__main__':
    unittest.main()

driver.close()


