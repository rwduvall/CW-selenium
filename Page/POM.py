from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TopNav(object):

    def __init__(self, driver):
        self.driver = driver

    def nav_to_homepage(self):
        self.driver.find_element_by_class_name("navbar-brand").click()

    def nav_to_blog(self):
        self.driver.find_element_by_class_name("posts").click()

    def nav_to_services(self):
        self.driver.find_element_by_class_name("service-page").click()

    def nav_to_ourwork(self):
        self.driver.find_element_by_class_name("our-work").click()

    def nav_to_aboutus(self):
        self.driver.find_element_by_class_name("about-us").click()

    def nav_to_contact(self):
        self.driver.find_element_by_class_name("contact").click()


class ContactForm(object):

    def __init__(self, driver):
        self.driver = driver

    def first_name(self, first_name):
        self.driver.find_element_by_name("firstname").send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element_by_name("lastname").send_keys(last_name)

    def email(self, email):
        self.driver.find_element_by_name("email").send_keys(email)


class Homepage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_hero_image_button(self):
        hero_button = self.driver.find_element_by_class_name("button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button")))
        hero_button.click()

    def click_featured_case_study(self):
        self.driver.find_element_by_class_name("card-case-study").click()


class Footer(object):

    def __init__(self, driver):
        self.driver = driver

    def quick_links_services(self):
        # self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[1]/a""").click()
        # getting an error on the link.click link of the following:
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[1]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[1]/a""")))
        link.click()

    def quick_links_our_work(self):
        # self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[2]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[2]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[2]/a""")))
        link.click()

    def quick_links_about_us(self):
        # self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[3]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[3]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[3]/a""")))
        link.click()

    def quick_links_blog(self):
        # self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[4]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[4]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[4]/a""")))
        link.click()

    def quick_links_careers(self):
        # self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[3]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[5]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[5]/a""")))
        link.click()

    def quick_links_events(self):
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[6]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[6]/a""")))
        link.click()

    def quick_links_talks(self):
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[7]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[7]/a""")))
        link.click()

    def quick_links_press(self):
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[8]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[8]/a""")))
        link.click()

    def quick_links_contact(self):
        link = self.driver.find_element_by_xpath("""//*[@id="footer"]/div/div[1]/div[2]/ul/li[9]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="footer"]/div/div[1]/div[2]/ul/li[9]/a""")))
        link.click()
