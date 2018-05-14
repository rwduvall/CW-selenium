import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from datetime import datetime
from time import sleep

from Page.POM import TopNav, ContactForm, Homepage, Footer, EventsPage, ServicesLandingPage, ServiceDetail
from Page.Locators import PageTitles

# should find a way to make the links work for either environment if we are really going to use this
# headless driver
# create a wait until clickable function


# class SmokeTests(unittest.TestCase):
# Maybe this needs to be its own file that calls tests from other places


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.screen_name = datetime.now()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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


class BlogPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.screen_name = datetime.now()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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
# this needs a wait
        self.driver.find_element_by_id("next").click()
        sleep(3)
        # count the number of cards. Finding by class name in the test is not the best practice should change this later
        posts_count = self.driver.find_elements_by_class_name("card-common--image_container")
        # verify the number of posts that display
        assert (len(posts_count) == 12)

    # see if I can figure out how to test "Tech Talks card in resources section has most recent talk"


class FooterTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.screen_name = datetime.now()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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


class FooterSocial(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://caktus:pointy@staging.caktusgroup.com")

    def tearDown(self):
        self.driver.quit()

    def test_twitter(self):
        Footer(self.driver).twitter()
        self.driver.switch_to.window(main_window)
        print(self.driver.current_url)
        # need to figure out how to switch tabs
        assert self.driver.title == "Caktus Group (@CaktusGroup) | Twitter"


class ServicesTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.screen_name = datetime.now()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Services Page
    def test_services_first_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).first_card()
        assert self.driver.title == PageTitles.service_card_1

    def test_servicedetail_see_more(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).first_card()
        ServiceDetail(self.driver).see_more()
        assert self.driver.title == PageTitles.services

    def test_services_second_card(self):
        TopNav(self.driver).nav_to_services()
        ServicesLandingPage(self.driver).second_card()
        assert self.driver.title == PageTitles.service_card_2
        # Navigate back to services page for the next test
        ServiceDetail(self.driver).see_more()


class ContactFormTest(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.driver.set_window_size(1920, 1080)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_contact_form(self):
        # Use the POM class to navigate to contact page
        TopNav(self.driver).nav_to_contact()
        # Use the POM class to enter text in the contact form
        ContactForm(self.driver).first_name("MRtest")
        ContactForm(self.driver).last_name("LastName")
        ContactForm(self.driver).email("example@example.com")


class OtherTests(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com/events/")
        cls.driver.set_window_size(1920, 1080)
        cls.eventpage = EventsPage

    def tearDown(self):
        self.driver.quit()

    # def test_4(self):
        # test that events match drop down selection
        # select an option from the drop down on events page
            # self.eventpage.event_dropdwon_select_year(1)
        # verify the year in the date field
            # self.assertIn("2018", self.eventpage.date_field())


class A(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.driver.set_window_size(1920, 1080)
        # cls.asdf = TopNav(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1(self):
        TopNav(self.driver).nav_to_contact()
        TopNav(self.driver).nav_to_homepage()
        Footer(self.driver).quick_links_contact()


if __name__ == '__main__':
    unittest.main()
