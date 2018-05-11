import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from datetime import datetime
from time import sleep

from Page.POM import TopNav, ContactForm, Homepage, Footer, EventsPage, ServicesLandingPage, ServiceDetail

# should find a way to make the links work for either environment if we are really going to use this
# headless driver
# create a wait until clickable function


class SmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.maximize_window()
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.screen_name = datetime.now()
        cls.topnav = TopNav(cls.driver)
        cls.homepage = Homepage(cls.driver)
        cls.footer = Footer(cls.driver)
        cls.services = ServicesLandingPage(cls.driver)
        cls.service_detail = ServiceDetail(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_verify_blog_page_title(self):
        # Navigates to the blog with the top navigation and verifies the title includes the word Blog
        self.topnav.nav_to_blog()
        # verify that Blog is in the title of the blog page
        self.assertIn("Blog", self.driver.title)

    def test_hero_button_loads_services_page(self):
        # Verify that the button in the hero image loads the services page
        self.topnav.nav_to_homepage()
        self.homepage.click_hero_image_button()
        assert self.driver.title == "Web Development and Consulting Services | Caktus Group"

    def test_casestudies_cards_navigation(self):
        # Verify the featured case study on the homepage takes the user to the correct page
        self.homepage.click_featured_case_study()
        assert self.driver.title == "Live Event Management App | Caktus Group"

    def test_count_blog_cards(self):
        # Verify that clicking view more on the blog page loads 6 more posts for a total of 12
        self.topnav.nav_to_blog()
        # click view more posts and wait(sleep)
        self.driver.find_element_by_id("next").click()
        sleep(3)
        # count the number of cards. Finding by class name in the test is not the best practice should change this later
        posts_count = self.driver.find_elements_by_class_name("card-common--image_container")
        # verify the number of posts that display
        assert (len(posts_count) == 12)

    # see if I can figure out how to test "Tech Talks card in resources section has most recent talk"

    # Footer tests cases:
    def test_footer_services(self):
        # Verify that services link in footer loads correct page
        self.footer.quick_links_services()
        assert self.driver.title == "Web Development and Consulting Services | Caktus Group"

    def test_footer_our_work(self):
        # Verify that our work link in footer loads correct page
        self.footer.quick_links_our_work()
        assert self.driver.title == "Django and SMS App Development Case Studies | Caktus Group"

    def test_quick_links_about_us(self):
        # Verify that about us link in footer loads correct page
        self.footer.quick_links_about_us()
        assert self.driver.title == "About Caktus Group | Django Web Development"

    def test_quick_links_blog(self):
        # Verify that blog link in footer loads correct page
        self.footer.quick_links_blog()
        assert self.driver.title == "Blog | Django and Python Tutorials | News | Caktus Group"

    def test_footer_careers(self):
        # Verify that careers link in footer loads correct page
        self.footer.quick_links_careers()
        assert self.driver.title == "Careers | Caktus Group"

    def test_footer_events(self):
        # Verify that events link in footer loads correct page
        self.footer.quick_links_events()
        assert self.driver.title == "Events in Durham and Beyond | Caktus Group"

    def test_footer_talks(self):
        # Verify that talks link in footer loads correct page
        self.footer.quick_links_talks()
        assert self.driver.title == "Web Development Talks | Caktus Group"

    def test_footer_press(self):
        # Verify that press link in footer loads correct page
        self.footer.quick_links_press()
        assert self.driver.title == "Awards and Press | Caktus Group"

    def test_footer_contact(self):
        # Verify that press link in footer loads correct page
        self.footer.quick_links_contact()
        assert self.driver.title == "Contact Us for Custom Web Development | Caktus Group"

    # Services Page
    def test_services_first_card(self):
        self.services.first_card()
        assert self.driver.title == "| Caktus Group"

    def test_servicedetail_see_more(self):
        self.service_detail.see_more()
        assert self.driver.title == "Web Development and Consulting Services | Caktus Group"

    def test_services_second_card(self):
        self.services.second_card()
        assert self.driver.title == "| Caktus Group"
        # Navigate back to services page for the next test
        self.service_detail.see_more()


class ContactFormTest(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.topnav = TopNav(cls.driver)
        cls.contactfrom = ContactForm(cls.driver)

    def tearDown(self):
        self.driver.quit()

    def test_contact_form(self):
        # Use the POM class to navigate to contact page
        self.topnav.nav_to_contact()
        # Use the POM class to enter text in the contact form
        self.contactfrom.first_name("MRtest")
        self.contactfrom.last_name("LastName")
        self.contactfrom.email("example@example.com")

"""
class OtherTests(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com/events/")
        cls.eventpage = EventsPage

    def tearDown(self):
        self.driver.quit()

    def test_4(self):
        # test that events match drop down selection
        # select an option from the drop down on events page
        self.eventpage.event_dropdwon_select_year(1)
        # verify the year in the date field
        self.assertIn("2018", self.eventpage.date_field())
"""

class A(unittest.TestCase):

    # need to add the variable to the set up for this class
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        cls.driver.get("https://caktus:pointy@staging.caktusgroup.com")
        cls.asdf = TopNav(cls.driver)

    def test_1(self):
        self.asdf.nav_to_contact()
        self.asdf.nav_to_homepage()


if __name__ == '__main__':
    unittest.main()
