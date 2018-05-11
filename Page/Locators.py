from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# https://github.com/levi-rs/explicit/blob/master/explicit/waiter.py
# def element_clickable_xpath(driver, elm_path, by, timeout=TIMEOUT, poll_frequency=0.5):
    # wait = WebDriverWait(timeout, poll_frequency)
    # return wait.until(EC.element_to_be_clickable((by, elm_path)))


class TopNavLocators(object):

    logo = (By.CLASS_NAME, "navbar-brand")


class FooterQuickLinks(object):

    contact = (By.XPATH, """//*[@class="half site-map"]/ul/li[9]/a""")


class HomepageLocators(object):
    # success model link in the why caktus seciton
    success_model = (By.LINK_TEXT, "Success Model")
    # the What Can We Do For You? section
    service_card_1 = (By.XPATH, """//*[@class="card-wrapper full"]/li[1]/a""")
    service_card_2 = (By.XPATH, """//*[@id="our-services"]/div/div/a""")
    view_services_button = (By.XPATH, """//*[@id="our-services"]/div/div/a""")
    # casestudies section
    read_our_case_studies_button = (By.XPATH, """//*[@id="case-studies-showcase"]/div/div[2]/a""")
    # rescources section
    blog_card_title = (By.XPATH, """//*[@id="our-resources"]/div/ul/li[1]/h3/a""")




class PageTitles(object):

    services = "Web Development and Consulting Services | Caktus Group"
    service_card_1_title = "Custom Web App Development | Caktus Group | Caktus Group"
    service_card_2_title = "Discovery Workshops and Product Definition | Caktus Group"

    casestudies = "Django and SMS App Development Case Studies | Caktus Group"

    blog = "Blog | Django and Python Tutorials | News | Caktus Group"
