import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from Page.Locators import PageTitles, BlogLocators, EventsLocators
from Page.POM import (TopNav, ContactForm, Homepage, Footer, Events, Services, ServiceDetail, Blog,
                      TestUtils, AboutUs, ContactLocators)

# from ddt import ddt, data


# url for the tests, putting it here so that its easier to update for all the tests at once

url = "http://caktusgroup.com"
driver_location = "/Users/robbie/Documents/driver/chromedriver"

# this adds headless driver so that tests run in the background
chrome_options = Options()
# chrome_options.set_headless(headless=True)
chrome_options.add_argument("--headless")

# ff_options = Options()
# ff_options.set_headless(headless=True)


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_hero_button_loads_services_page(self):
        # Verify that the button in the hero image loads the services page
        TopNav(self.driver).logo()
        Homepage(self.driver).hero_image_button()
        assert self.driver.title == PageTitles.services

    def test_success_model_link(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).why_caktus_success_model()
        assert self.driver.title == PageTitles.success_model_blog

    # These tests verify that the service cards load the correct pages
    def test_homepage_service_card_1(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_1()
        assert self.driver.title == PageTitles.service_card_1

    def test_homepage_service_card_2(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_2()
        assert self.driver.title == PageTitles.service_card_2

    def test_homepage_service_card_3(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_3()
        assert self.driver.title == PageTitles.service_card_3

    def test_homepage_service_card_4(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_4()
        assert self.driver.title == PageTitles.service_card_4

    def test_homepage_service_card_5(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_5()
        assert self.driver.title == PageTitles.service_card_5

    def test_homepage_service_card_6(self):
        TopNav(self.driver).logo()
        Homepage(self.driver).service_card_6()
        assert self.driver.title == PageTitles.service_card_6

    def test_view_services_button(self):
        # Verify that the services button takes the user to the services page
        TopNav(self.driver).logo()
        Homepage(self.driver).view_services_button()
        assert self.driver.title == PageTitles.services

    def test_featured_casestudy_card(self):
        # Verify the featured case study on the homepage takes the user to the correct page
        TopNav(self.driver).logo()
        Homepage(self.driver).featured_case_study()
        assert self.driver.title == PageTitles.featured_casestudy

    def test_read_our_case_studies_button(self):
        # Verify that the read our case studies button takes user to correct page
        TopNav(self.driver).logo()
        Homepage(self.driver).read_our_case_studies()
        assert self.driver.title == PageTitles.casestudies

    def test_resource_blog_card_title(self):
        # Verify that the blog link in resource card takes user to blog page
        TopNav(self.driver).logo()
        Homepage(self.driver).resources_blog_card_title()
        assert self.driver.title == PageTitles.blog

    def test_resource_tech_talks_card_title(self):
        # Verify that the blog link in resource card takes user to blog page
        TopNav(self.driver).logo()
        Homepage(self.driver).resources_tech_talks_card_title()
        assert self.driver.title == PageTitles.talks

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class ServicesTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_services_first_card(self):
        TopNav(self.driver).services()
        Services(self.driver).first_card()
        assert self.driver.title == PageTitles.service_card_1

    def test_services_second_card(self):
        TopNav(self.driver).services()
        Services(self.driver).second_card()
        assert self.driver.title == PageTitles.service_card_2

    def test_services_third_card(self):
        TopNav(self.driver).services()
        Services(self.driver).third_card()
        assert self.driver.title == PageTitles.service_card_3

    def test_services_fourth_card(self):
        TopNav(self.driver).services()
        Services(self.driver).fourth_card()
        assert self.driver.title == PageTitles.service_card_4

    def test_services_fifth_card(self):
        TopNav(self.driver).services()
        Services(self.driver).fifth_card()
        assert self.driver.title == PageTitles.service_card_5

    def test_services_sixth_card(self):
        TopNav(self.driver).services()
        Services(self.driver).sixth_card()
        assert self.driver.title == PageTitles.service_card_6

    def test_servicedetail_see_more(self):
        # Verify the see more breadcrumb on service detail page opens services page
        TopNav(self.driver).services()
        Services(self.driver).first_card()
        ServiceDetail(self.driver).see_more()
        assert self.driver.title == PageTitles.services

    def test_servicedetail_contact_button(self):
        # Verify that the contact button on services page opens the contact page
        TopNav(self.driver).services()
        Services(self.driver).first_card()
        ServiceDetail(self.driver).contact_button()
        assert self.driver.title == PageTitles.contact

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class CaseStudiesTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_(self):
        # Verify that the Our Work option in the top nav loads the /casestudies page
        TopNav(self.driver).our_work()
        assert self.driver.title == PageTitles.casestudies

    # Add tests for the cards once we implement the reusable card component

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class AboutUsTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(driver_location)
        self.driver.get(url)
        self.driver.set_window_size(1920, 1080)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(self.driver).close_cookie_banner()

    def test_view_more_press(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).view_more_press_button()
        assert self.driver.title == PageTitles.press

    def test_team_bio_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).colin_bio()
        assert self.driver.title == PageTitles.colin

    def test_were_hiring_button(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).were_hiring_button()
        assert self.driver.title == PageTitles.careers

    # tech community engagement links, this may fail because of issue with their sites
    def test_our_contributions_button(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).browse_contributions_button()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.current_url == PageTitles.github_url

    def test_women_in_tech_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).women_in_tech()
        TestUtils(self.driver).switch_new_tab()
        print(self.driver.title)
        assert self.driver.title == PageTitles.durham_women_in_tech

    def test_code_durham_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).code_durham()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.code_for_durham, print(self.driver.title)

    def test_girl_dev_it_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).girl_dev_it()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.girl_dev_it

    def test_pyladies_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).pyladies()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.pyladies

    """ def test_trianglepython_link(self):
        TopNav(self.driver).nav_to_aboutus()
        AboutUs(self.driver).trianglepython_click()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.current_url == PageTitles.trianlgepython_url
    """

    def test_django_girls_link(self):
        TopNav(self.driver).about_us_nav()
        AboutUs(self.driver).django_girls()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.django_girls

    def tearDown(self):
        self.driver.quit()


class CareersTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.get(url)
        cls.driver.set_window_size(1920, 1080)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test(self):
        TopNav(self.driver).careers()
        assert self.driver.title == PageTitles.careers

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class ContactFormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.get(url)
        cls.driver.set_window_size(1920, 1080)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_contact_form(self):
        # Use the POM class to navigate to contact page
        TopNav(self.driver).contact()
        # Use the POM class to enter text in the contact form
        ContactForm(self.driver).first_name("test")
        ContactForm(self.driver).last_name("LastName")
        ContactForm(self.driver).email("exampl@example.com")
        ContactForm(self.driver).submit()
        # verify that an error is displayed for the required field that was not entered
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*ContactLocators.hubspot_error))
        assert element.is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class BlogPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_blog_page_title(self):
        # Navigates to the blog with the top navigation and verifies the title includes the word Blog
        TopNav(self.driver).blog()
        # verify that Blog is in the title of the blog page
        assert self.driver.title == PageTitles.blog

    def test_count_blog_cards(self):
        # Verify that clicking view more on the blog page loads 6 more posts for a total of 12
        TopNav(self.driver).blog()
        # click view more posts and wait(sleep)
        Blog(self.driver).load_more()
        sleep(2)
        # count the number of cards
        posts_count = self.driver.find_elements(*BlogLocators.blog_cards_images)
        # verify the number of posts that display
        assert (len(posts_count) == 12)

    def test_view_more_events(self):
        # Verify that clicking the view more events button loads the events page
        TopNav(self.driver).blog()
        Blog(self.driver).more_events_button()
        assert self.driver.title == PageTitles.events

    def test_testing_topic(self):
        # Verify that the topics on the first 3 cards include 'QA'
        TopNav(self.driver).blog()
        Blog(self.driver).testing_qa_filter()
        self.assertIn("QA", self.driver.find_element(*BlogLocators.first_card_topics).text)
        self.assertIn("QA", self.driver.find_element(*BlogLocators.second_card_topics).text)
        self.assertIn("QA", self.driver.find_element(*BlogLocators.third_card_topics).text)

    def test_technical_topic(self):
        # Verify that the topics on the first 3 cards include 'Technical'
        TopNav(self.driver).blog()
        Blog(self.driver).technical_filter()
        self.assertIn("Technical", self.driver.find_element(*BlogLocators.first_card_topics).text)
        self.assertIn("Technical", self.driver.find_element(*BlogLocators.second_card_topics).text)
        self.assertIn("Technical", self.driver.find_element(*BlogLocators.third_card_topics).text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


class FooterTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_quick_links_services(self):
        # Verify that services link in footer loads correct page
        Footer(self.driver).quick_links_services()
        assert self.driver.title == PageTitles.services

    def test_quick_links_our_work(self):
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

    def test_quick_links_careers(self):
        # Verify that careers link in footer loads correct page
        Footer(self.driver).quick_links_careers()
        assert self.driver.title == PageTitles.careers

    def test_quick_links_events(self):
        # Verify that events link in footer loads correct page
        Footer(self.driver).quick_links_events()
        assert self.driver.title == PageTitles.events

    def test_quick_links_talks(self):
        # Verify that talks link in footer loads correct page
        Footer(self.driver).quick_links_talks()
        assert self.driver.title == PageTitles.talks

    def test_quick_links_press(self):
        # Verify that press link in footer loads correct page
        Footer(self.driver).quick_links_press()
        assert self.driver.title == PageTitles.press

    def test_quick_links_contact(self):
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

    # not using setUpClass here because that would make switching tabs harder
    def setUp(self):
        self.driver = webdriver.Chrome(driver_location, options=chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get(url)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(self.driver).close_cookie_banner()

    def test_twitter(self):
        # Verify that the twitter icon in the footer opens the correct page
        Footer(self.driver).twitter()
        # switch to the new tab by finding the second window handle
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.twitter

    def test_github(self):
        # Verify that the github icon in the footer opens the correct page
        Footer(self.driver).github()
        # switch to the new tab by finding the second window handle
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.current_url == PageTitles.github_url

    def test_facebook(self):
        # Verify that the facebook icon in the footer opens the correct page
        Footer(self.driver).facebook()
        # switch to the new tab by finding the second window handle
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.current_url == PageTitles.facebook_url

    def test_google_plus(self):
        # Verify that the google+ icon in the footer opens the correct page
        Footer(self.driver).google_plus()
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.current_url == PageTitles.google_plus_url

    def test_linkedIn(self):
        # Verify that the google+ icon in the footer opens the correct page
        # linked in is opening a sign in page instead of the caktus linked in page for the automation browser
        Footer(self.driver).linkedin()
        # switch to the new tab by finding the second window handle
        TestUtils(self.driver).switch_new_tab()
        assert self.driver.title == PageTitles.linkedIn_title

    def tearDown(self):
        self.driver.quit()


# @ddt
class EventsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(driver_location, options=chrome_options)
        cls.driver.get(url)
        cls.driver.set_window_size(1920, 1080)
        # close the cookie banner in set up so its closed for all the tests
        TestUtils(cls.driver).close_cookie_banner()

    def test_events_dropdown(self):
        # Verify that first event card matches the 'year' selected from the drop down
        year = "2017"
        # select an option from the drop down on events page
        Footer(self.driver).quick_links_events()
        Events(self.driver).event_dropdown_select_year(year)
        # verify the year in the date field
        event_date = self.driver.find_element(*EventsLocators.date_on_card).text
        self.assertIn(year, event_date)
    # uncomment out ddt/data lines, comment out/remove the year= line and add a parameter 'year' after self to use ddt
    # @data("2018", "2017", "2016", "2015", "2014", "2013", "2012")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
