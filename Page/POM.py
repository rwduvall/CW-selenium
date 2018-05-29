from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Page.Locators import (TopNavLocators, FooterLocators, HomepageLocators, BlogLocators, ServicesLocators,
                           EventsLocators, ContactLocators, AboutUsLocators)

# This file does all of the click and other actions


class Base(object):

    def __init__(self, driver):
        self.driver = driver


class TopNav(Base):

    def logo(self):
        link = self.driver.find_element(*TopNavLocators.logo)
        link.click()

    def services(self):
        link = self.driver.find_element(*TopNavLocators.services)
        link.click()

    def our_work(self):
        link = self.driver.find_element(*TopNavLocators.our_work)
        link.click()

    def about_us_nav(self):
        link = self.driver.find_element(*TopNavLocators.about_us)
        link.click()

    def careers(self):
        link = self.driver.find_element(*TopNavLocators.careers)
        link.click()

    def blog(self):
        link = self.driver.find_element(*TopNavLocators.blog)
        link.click()

    def contact(self):
        link = self.driver.find_element(*TopNavLocators.contact)
        link.click()


class Homepage(Base):

    def hero_image_button(self):
        hero_button = self.driver.find_element(*HomepageLocators.hero_button)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.hero_button))
        hero_button.click()

    def featured_case_study(self):
        link = self.driver.find_element(*HomepageLocators.featured_case_study)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.featured_case_study))
        link.click()

    def why_caktus_success_model(self):
        link = self.driver.find_element(*HomepageLocators.success_model)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.success_model))
        link.click()

    def service_card_1(self):
        link = self.driver.find_element(*HomepageLocators.service_card_1)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_1))
        link.click()

    def service_card_2(self):
        link = self.driver.find_element(*HomepageLocators.service_card_2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_2))
        link.click()

    def service_card_3(self):
        link = self.driver.find_element(*HomepageLocators.service_card_3)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_3))
        link.click()

    def service_card_4(self):
        link = self.driver.find_element(*HomepageLocators.service_card_4)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_4))
        link.click()

    def service_card_5(self):
        link = self.driver.find_element(*HomepageLocators.service_card_5)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_5))
        link.click()

    def service_card_6(self):
        link = self.driver.find_element(*HomepageLocators.service_card_6)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.service_card_6))
        link.click()

    def view_services_button(self):
        link = self.driver.find_element(*HomepageLocators.view_services_button)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.view_services_button))
        link.click()

    def read_our_case_studies(self):
        link = self.driver.find_element(*HomepageLocators.read_our_case_studies_button)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.read_our_case_studies_button))
        link.click()

    def resources_blog_card_title(self):
        link = self.driver.find_element(*HomepageLocators.blog_card_title)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.blog_card_title))
        link.click()

    def resources_tech_talks_card_title(self):
        link = self.driver.find_element(*HomepageLocators.tech_talks_card_title)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomepageLocators.tech_talks_card_title))
        link.click()


class Services(Base):
    # need to figure out waits with the locators file
    def first_card(self):
        link = self.driver.find_element(*ServicesLocators.card_1)
        link.click()

    def second_card(self):
        link = self.driver.find_element(*ServicesLocators.card_2)
        link.click()

    def third_card(self):
        link = self.driver.find_element(*ServicesLocators.card_3)
        link.click()

    def fourth_card(self):
        link = self.driver.find_element(*ServicesLocators.card_4)
        link.click()

    def fifth_card(self):
        link = self.driver.find_element(*ServicesLocators.card_5)
        link.click()

    def sixth_card(self):
        link = self.driver.find_element(*ServicesLocators.card_6)
        link.click()


class ServiceDetail(Base):

    def see_more(self):
        link = self.driver.find_element(*ServicesLocators.see_more_servicedetail_top)
        link.click()

    def contact_button(self):
        link = self.driver.find_element(*ServicesLocators.contact_button_servicedetail)
        link.click()


class AboutUs(Base):

    def meet_our_team_button(self):
        link = self.driver.find_element(*AboutUsLocators.meet_team_button)
        link.click()

    def browse_contributions_button(self):
        link = self.driver.find_element(*AboutUsLocators.browse_our_contributions)
        link.click()

    def women_in_tech(self):
        link = self.driver.find_element(*AboutUsLocators.women_in_tech)
        link.click()

    def code_durham(self):
        link = self.driver.find_element(*AboutUsLocators.code_for_durham)
        link.click()

    def girl_dev_it(self):
        link = self.driver.find_element(*AboutUsLocators.girl_dev_it_rdu)
        link.click()

    def pyladies(self):
        link = self.driver.find_element(*AboutUsLocators.pyladies)
        link.click()

    def trianglepython(self):
        link = self.driver.find_element(*AboutUsLocators.trianglepython)
        link.click()

    def django_girls(self):
        link = self.driver.find_element(*AboutUsLocators.django_girls)
        link.click()

    def view_more_press_button(self):
        link = self.driver.find_element(*AboutUsLocators.view_more_press)
        link.click()

    def colin_bio(self):
        link = self.driver.find_element(*AboutUsLocators.colin)
        link.click()

    def were_hiring_button(self):
        link = self.driver.find_element(*AboutUsLocators.were_hiring)
        link.click()


class Blog(Base):

    def load_more(self):
        link = self.driver.find_element(*BlogLocators.load_more)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*BlogLocators.load_more))
        link.click()

    def more_events_button(self):
        link = self.driver.find_element(*BlogLocators.view_more_events)
        link.click()

    def testing_qa_filter(self):
        link = self.driver.find_element(*BlogLocators.test_qa_topic)
        link.click()

    def technical_filter(self):
        link = self.driver.find_element(*BlogLocators.technical_topic)
        link.click()


class ContactForm(Base):

    def first_name(self, first_name):
        self.driver.find_element(*ContactLocators.first_name).send_keys(first_name)

    def last_name(self, last_name):
        self.driver.find_element(*ContactLocators.last_name).send_keys(last_name)

    def email(self, email):
        self.driver.find_element(*ContactLocators.email).send_keys(email)

    def submit(self):
        link = self.driver.find_element(*ContactLocators.send_button)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*ContactLocators.send_button))
        link.click()


class Footer(Base):

    def quick_links_services(self):
        link = self.driver.find_element(*FooterLocators.services)
        link.click()

    def quick_links_our_work(self):
        link = self.driver.find_element(*FooterLocators.our_work)
        link.click()

    def quick_links_about_us(self):
        link = self.driver.find_element(*FooterLocators.about_us)
        link.click()

    def quick_links_blog(self):
        link = self.driver.find_element(*FooterLocators.blog)
        link.click()

    def quick_links_careers(self):
        link = self.driver.find_element(*FooterLocators.careers)
        link.click()

    def quick_links_events(self):
        link = self.driver.find_element(*FooterLocators.events)
        link.click()

    def quick_links_talks(self):
        link = self.driver.find_element(*FooterLocators.talks)
        link.click()

    def quick_links_press(self):
        link = self.driver.find_element(*FooterLocators.press)
        link.click()

    def quick_links_contact(self):
        link = self.driver.find_element(*FooterLocators.contact)
        link.click()

    def privacy_policy(self):
        link = self.driver.find_element(*FooterLocators.privacy_policy)
        link.click()

    def twitter(self):
        link = self.driver.find_element(*FooterLocators.twitter_icon)
        link.click()

    def github(self):
        link = self.driver.find_element(*FooterLocators.github_icon)
        link.click()

    def facebook(self):
        link = self.driver.find_element(*FooterLocators.facebook_icon)
        link.click()

    def google_plus(self):
        link = self.driver.find_element(*FooterLocators.google_plus_icon)
        link.click()

    def linkedin(self):
        link = self.driver.find_element(*FooterLocators.linkedIn)
        link.click()


class Events(Base):

    def event_dropdown_select_year(self, value):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*EventsLocators.dropdown))
        select = Select(self.driver.find_element(*EventsLocators.dropdown))
        select.select_by_value(value)

    def date_field(self):
        self.driver.find_elements(*EventsLocators.date_on_card)


class TestUtils(Base):

    def switch_new_tab(self):
        # switch to the new tab by finding the second window handle
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def close_cookie_banner(self):
        link = self.driver.find_element(*TopNavLocators.x_cookie_banner)
        link.click()
