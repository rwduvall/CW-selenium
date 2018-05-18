from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# this file finds all the elements on the page


class TopNavLocators(object):

    logo = (By.CLASS_NAME, "navbar-brand")
    blog = (By.CLASS_NAME, "posts")
    services = (By.CLASS_NAME, "service-page")
    our_work = (By.CLASS_NAME, "our-work")
    about_us = (By.CLASS_NAME, "about-us")
    contact = (By.CLASS_NAME, "contact")


class FooterLocators(object):

    services = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 1)
    our_work = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 2)
    about_us = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 3)
    blog = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 4)
    careers = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 5)
    events = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 6)
    talks = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 7)
    press = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 8)
    contact = (By.XPATH, """//*[@class="half site-map"]/ul/li[%s]/a""" % 9)
    privacy_policy = (By.XPATH, """//*[@class="half newsletter-sign-up"]/p/a""")
    twittericon = (By.XPATH, """//*[@class="socialicons"]/ul/li[%s]/a""" % 1)
    githubicon = (By.XPATH, """//*[@class="socialicons"]/ul/li[%s]/a""" % 2)


class BlogLocators(object):

    load_more = (By.XPATH, """//*[@id="next"]""")
    blog_cards_images = (By.CLASS_NAME, "card-common--image_container")


class HomepageLocators(object):
    hero_button = (By.CLASS_NAME, "button")
    # success model link in the why caktus seciton
    success_model = (By.LINK_TEXT, "Success Model")
    # the What Can We Do For You? section
    service_card_1 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 1)
    service_card_2 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 2)
    service_card_3 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 3)
    service_card_4 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 4)
    service_card_5 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 5)
    service_card_6 = (By.XPATH, """//*[@class="card-wrapper full"]/li[%s]/a""" % 6)
    view_services_button = (By.XPATH, """//*[@id="our-services"]/div/div/a""")
    # casestudies section
    featured_case_study = (By.CLASS_NAME, "card-case-study")
    read_our_case_studies_button = (By.XPATH, """//*[@id="case-studies-showcase"]/div/div[2]/a""")
    # rescources section
    blog_card_title = (By.XPATH, """//*[@id="our-resources"]/div/ul/li[1]/h3/a""")


class ServicesLocators(object):

    card_1 = (By.XPATH, """//*[@class="card-wrapper full"]/li[1]""")
    card_2 = (By.XPATH, """//*[@class="card-wrapper full"]/li[2]""")
    card_3 = (By.XPATH, """//*[@class="card-wrapper full"]/li[3]""")
    card_4 = (By.XPATH, """//*[@class="card-wrapper full"]/li[4]""")
    card_5 = (By.XPATH, """//*[@class="card-wrapper full"]/li[5]""")
    card_6 = (By.XPATH, """//*[@class="card-wrapper full"]/li[6]""")
    contact_button_servicedetail = (By.XPATH, """//*[@id="main-content"]/section[3]/a""")  # class="contact-button"
    see_more_servicedetail_top = (By.XPATH, """//*[@class="components-wrapper wrapper"]/a[1]""")


class ContactLocators(object):

    first_name = (By.NAME, "firstname")
    last_name = (By.NAME, "lastname")
    email = (By.NAME, "email")
    phone_number = (By.NAME, "phone")
    company_name = (By.NAME, "company")
    message = (By.NAME, "message")

    hubspot_error = (By.CLASS_NAME, "hubspot-error")
    send_button = (By.XPATH, """//*[@class="actions"]/input""")


class EventsPageLocators(object):

    dropdown = (By.ID, "event-year")
    date_on_card = (By.CLASS_NAME, "call-out")


class PageTitles(object):
    # Page titles used for verification steps
    # Main pages:
    homepage = "Django Web Development Company | Durham, NC | Caktus Group"
    services = "Web Development and Consulting Services | Caktus Group"
    casestudies = "Django and SMS App Development Case Studies | Caktus Group"
    blog = "Blog | Django and Python Tutorials | News | Caktus Group"
    about_us = "About Caktus Group | Django Web Development"
    careers = "Careers | Caktus Group"
    contact = "Contact Us for Custom Web Development | Caktus Group"
    events = "Events in Durham and Beyond | Caktus Group"
    talks = "Web Development Talks | Caktus Group"
    press = "Awards and Press | Caktus Group"
    # service cards:
    service_card_1 = "Custom Web App Development | Caktus Group"
    service_card_2 = "Discovery Workshops and Product Definition | Caktus Group"
    service_card_3 = "Team Augmentation | Developer Staffing | Caktus Group"
    service_card_4 = "Project Management, QA, Agile Consulting | Caktus Group"
    service_card_5 = "SMS App Development | Django and RapidSMS | Caktus Group"
    service_card_6 = "Hosting, Django Upgrades, Website Maintenance | Caktus Group"
    # All the other pages
    success_model_blog = "The Caktus Success Model | Caktus Group"
    privacy_policy = "Privacy Policy | Caktus Group"

    featured_casestudy = "Live Event Management App | Caktus Group"

    twitter = "Caktus Group (@CaktusGroup) | Twitter"
    # using URL for this instead of title b/c title wasn't working
    github_url = "https://github.com/caktus"
