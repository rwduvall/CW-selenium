import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
from time import sleep

from Page.POM import TopNav, ContactForm, Homepage, Footer, EventsPage, ServicesLandingPage, ServiceDetail, BlogPage
from Page.Locators import PageTitles, BlogLocators, EventsPageLocators
from Page.POM import ContactLocators as CL


# url for the tests, putting it here so that its easier to update for all the tests at once
url = "https://caktus:pointy@staging.caktusgroup.com"
driver_location = "/Users/robbie/Downloads/chromedriver"
# this adds headless driver so that tests run in the background
chrome_options = Options()
chrome_options.add_argument("--headless")


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        cls.screen_name = datetime.now()

    def test_hero_button_loads_services_page(self):
        # Verify that the button in the hero image loads the services page
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_hero_image_button()
        assert self.driver.title == PageTitles.services

    def test_success_model_link(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_why_caktus_success_model()
        assert self.driver.title == PageTitles.success_model_blog

    def test_homepage_service_card_1(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_1()
        assert self.driver.title == PageTitles.service_card_1

    def test_homepage_service_card_2(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_2()
        assert self.driver.title == PageTitles.service_card_2

    def test_homepage_service_card_3(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_3()
        assert self.driver.title == PageTitles.service_card_3

    def test_homepage_service_card_4(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_4()
        assert self.driver.title == PageTitles.service_card_4

    def test_homepage_service_card_5(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_5()
        assert self.driver.title == PageTitles.service_card_5

    def test_homepage_service_card_6(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_service_card_6()
        assert self.driver.title == PageTitles.service_card_6

    def test_view_services_button(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_view_services_button()
        assert self.driver.title == PageTitles.services

    def test_casestudies_cards_navigation(self):
        TopNav(self.driver).nav_to_homepage()
        # Verify the featured case study on the homepage takes the user to the correct page
        Homepage(self.driver).click_featured_case_study()
        assert self.driver.title == PageTitles.featured_casestudy

    def test_read_our_case_studies_button(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_read_our_case_studies()
        assert self.driver.title == PageTitles.casestudies

    def test_resource_blog_card_title(self):
        TopNav(self.driver).nav_to_homepage()
        Homepage(self.driver).click_resources_blog_card_title()
        assert self.driver.title == PageTitles.blog

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class BlogPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        cls.screen_name = datetime.now()

    def test_verify_blog_page_title(self):
        # Navigates to the blog with the top navigation and verifies the title includes the word Blog
        TopNav(self.driver).nav_to_blog()
        # verify that Blog is in the title of the blog page
        assert self.driver.title == PageTitles.blog
        # self.assertIn("Blog", self.driver.title)

    def test_count_blog_cards(self):
        # Verify that clicking view more on the blog page loads 6 more posts for a total of 12
        TopNav(self.driver).nav_to_blog()
        # click view more posts and wait(sleep)
        BlogPage(self.driver).load_more()
        sleep(3)
        # count the number of cards. Finding by class name in the test is not the best practice should change this later
        posts_count = self.driver.find_elements(*BlogLocators.blog_cards_images)
        # verify the number of posts that display
        assert (len(posts_count) == 12)

    # add tests for resources cards

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FooterTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        cls.screen_name = datetime.now()

    # Quick links
    def test_footer_services(self):
        # Verify that services link in footer loads correct page
        Footer(self.driver).quick_links_services()
        assert self.driver.title == PageTitles.services

    def test_footer_our_work(self):
        # Verify that our work link in footer loads correct page
        Footer(self.driver).quick_links_our_work()
        assert self.driver.title == PageTitles.casestudies

    def test_quick_links_about_us(self):
        # Verify that about us link in footer loads correct page
        Footer(self.driver).quick_links_about_us()
        assert self.driver.title == PageTitles.about_us

    def test_quick_links_blog(self):
        # Verify that blog link in footer loads correct page
        Footer(self.driver).quick_links_blog()
        assert self.driver.title == PageTitles.blog

    def test_footer_careers(self):
        # Verify that careers link in footer loads correct page
        Footer(self.driver).quick_links_careers()
        assert self.driver.title == PageTitles.careers

    def test_footer_events(self):
        # Verify that events link in footer loads correct page
        Footer(self.driver).quick_links_events()
        assert self.driver.title == PageTitles.events

    def test_footer_talks(self):
        # Verify that talks link in footer loads correct page
        Footer(self.driver).quick_links_talks()
        assert self.driver.title == PageTitles.talks

    def test_footer_press(self):
        # Verify that press link in footer loads correct page
        Footer(self.driver).quick_links_press()
        assert self.driver.title == PageTitles.press

    def test_footer_contact(self):
        # Verify that press link in footer loads correct page
        Footer(self.driver).quick_links_contact()
        assert self.driver.title == PageTitles.contact

    def test_privacy_policy(self):
        Footer(self.driver).privacy_policy()
        assert self.driver.title == PageTitles.privacy_policy

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FooterSocial(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(driver_location, options=chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get(url)

    def test_twitter(self):
        Footer(self.driver).twitter()
        # switch to the new tab
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        assert self.driver.title == PageTitles.twitter

    def test_github(self):
        Footer(self.driver).github()
        # switch to the new tab
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

        assert self.driver.current_url == PageTitles.github_url
        
    def tearDown(self):
        self.driver.quit()


class ServicesTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        cls.screen_name = datetime.now()

    def test_services_first_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).first_card()
        assert self.driver.title == PageTitles.service_card_1

    def test_servicedetail_see_more(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).first_card()
        ServiceDetail(self.driver).see_more()
        assert self.driver.title == PageTitles.services

    def test_servicedetail_contact_button(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).first_card()
        ServiceDetail(self.driver).contact_button()
        assert self.driver.title == PageTitles.contact

    def test_services_second_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).second_card()
        assert self.driver.title == PageTitles.service_card_2

    def test_services_third_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).third_card()
        assert self.driver.title == PageTitles.service_card_3

    def test_services_fourth_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).fourth_card()
        assert self.driver.title == PageTitles.service_card_4

    def test_services_fifth_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).fifth_card()
        assert self.driver.title == PageTitles.service_card_5

    def test_services_sixth_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).sixth_card()
        assert self.driver.title == PageTitles.service_card_6

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class ContactFormTest(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.get(url)
        cls.driver.set_window_size(1920, 1080)

    def test_contact_form(self):
        # Use the POM class to navigate to contact page
        TopNav(self.driver).nav_to_contact()
        # Use the POM class to enter text in the contact form
        ContactForm(self.driver).first_name("MRtest")
        ContactForm(self.driver).last_name("LastName")
        ContactForm(self.driver).email("exampl@example.com")
        ContactForm(self.driver).submit()

        # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name("hubspot-error"))
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CL.hubspot_error))
        assert element.is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class OtherTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.get(url)
        cls.driver.set_window_size(1920, 1080)

    def test_4(self):
        # test that first event card matchs the year selected from the drop down
        year = "2017"
        # select an option from the drop down on events page
        Footer(self.driver).quick_links_events()
        EventsPage(self.driver).event_dropdwon_select_year(year)
        # verify the year in the date field
        event_date = self.driver.find_element(*EventsPageLocators.date_on_card).text
        self.assertIn(year, event_date)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
