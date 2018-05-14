from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Page.Locators import TopNavLocators, FooterLinks, HomepageLocators, BlogLinks


# using link = ... so that its easier to come back later and add waits if I need to

# class WaitTill(object):
# can't get a wait class to work
# https://github.com/levi-rs/explicit/blob/master/explicit/waiter.py
# def element_clickable_xpath(driver, elm_path, by, timeout=TIMEOUT, poll_frequency=0.5):
    # wait = WebDriverWait(timeout, poll_frequency)
    # return wait.until(EC.element_to_be_clickable((by, elm_path)))


class Base(object):

    def __init__(self, driver):
        self.driver = driver


class TopNav(Base):

    def nav_to_homepage(self):
        link = self.driver.find_element(*TopNavLocators.logo)
        link.click()

    def nav_to_blog(self):
        link = self.driver.find_element_by_class_name("posts")
        link.click()

    def nav_to_services(self):
        link = self.driver.find_element_by_class_name("service-page")
        link.click()

    def nav_to_ourwork(self):
        link = self.driver.find_element_by_class_name("our-work")
        link.click()

    def nav_to_aboutus(self):
        link = self.driver.find_element_by_class_name("about-us")
        link.click()

    def nav_to_contact(self):
        link = self.driver.find_element_by_class_name("contact")
        link.click()


class ContactForm(Base):

    def first_name(self, first_name):
        self.driver.find_element_by_name("firstname").send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element_by_name("lastname").send_keys(last_name)

    def email(self, email):
        self.driver.find_element_by_name("email").send_keys(email)


class Homepage(Base):

    def click_hero_image_button(self):
        hero_button = self.driver.find_element_by_class_name("button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button")))
        hero_button.click()

    def click_featured_case_study(self):
        self.driver.find_element_by_class_name("card-case-study").click()

    def click_why_caktus_success_model(self):
        link = self.driver.find_element(*HomepageLocators.success_model)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located(link))
        link.click()

    def click_service_card_1(self):
        link = self.driver.find_element(*HomepageLocators.service_card_1)
        link.click()

    def click_service_card_2(self):
        link = self.driver.find_element(*HomepageLocators.service_card_2)
        link.click()

    def click_service_card_3(self):
        link = self.driver.find_element(*HomepageLocators.service_card_3)
        link.click()

    def click_service_card_4(self):
        link = self.driver.find_element(*HomepageLocators.service_card_4)
        link.click()

    def click_service_card_5(self):
        link = self.driver.find_element(*HomepageLocators.service_card_5)
        link.click()

    def click_service_card_6(self):
        link = self.driver.find_element(*HomepageLocators.service_card_6)
        link.click()

    def click_view_services_button(self):
        link = self.driver.find_element(*HomepageLocators.view_services_button)
        link.click()

    def click_read_our_case_studies(self):
        link = self.driver.find_element(*HomepageLocators.read_our_case_studies_button)
        link.click()

    def click_resources_blog_card_title(self):
        link = self.driver.find_element(*HomepageLocators.blog_card_title)
        link.click()


class EventsPage(Base):

    def event_dropdwon_select_year(self):
        select = Select(self.driver.find_element_by_id("event-year"))
        select.select_by_value("2018")
        # self.driver.Select(self.driver.find_element_by_id("event-year")).select_by_value(value)

    def date_field(self):
        self.driver.find_elements_by_class_name("call-out")


class ServicesLandingPage(Base):

    def first_card(self):
        link = self.driver.find_element_by_xpath("""//*[@class="card-wrapper full"]/li[1]""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="card-wrapper full"]/li[1]""")))
        link.click()

    def second_card(self):
        link = self.driver.find_element_by_xpath("""//*[@class="card-wrapper full"]/li[2]""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="card-wrapper full"]/li[2]""")))
        link.click()

    def contact_button(self):
        link = self.driver.find_element_by_class("contact-button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "contact-button")))
        link.click()


class ServiceDetail(Base):

    def see_more(self):
        link = self.driver.find_element_by_class_name("link-common-breadcrumb")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.NAME, "link-common-breadcrumb")))
        link.click()


class BlogPage(Base):

    def load_more(self):
        link = self.driver.find_element(*BlogLinks.load_more)
        link.click()


class Footer(Base):

    def quick_links_services(self):
        # self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[1]/a""").click()
        # getting an error on the link.click link of the following:
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[1]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[1]/a""")))
        link.click()

    def quick_links_our_work(self):
        # self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[2]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[2]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[2]/a""")))
        link.click()

    def quick_links_about_us(self):
        # self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[3]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[3]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[3]/a""")))
        link.click()

    def quick_links_blog(self):
        # self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[4]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[4]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[4]/a""")))
        link.click()

    def quick_links_careers(self):
        # self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[3]/a""").click()
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[5]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[5]/a""")))
        link.click()

    def quick_links_events(self):
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[6]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[6]/a""")))
        link.click()

    def quick_links_talks(self):
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[7]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[7]/a""")))
        link.click()

    def quick_links_press(self):
        link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[8]/a""")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[8]/a""")))
        link.click()

    def quick_links_contact(self):
        # link = self.driver.find_element_by_xpath("""//*[@class="half site-map"]/ul/li[9]/a""")
        link = self.driver.find_element(*FooterLinks.contact)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@class="half site-map"]/ul/li[9]/a""")))
        link.click()

    def privacy_policy(self):
        link = self.driver.find_element(*FooterLinks.privacy_policy)
        link.click()

    def twitter(self):
        link = self.driver.find_element(*FooterLinks.twittericon)
        link.click()

    def github(self):
        link = self.driver.find_element(*FooterLinks.githubicon)
        link.click()
