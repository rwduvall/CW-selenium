import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
from selenium.webdriver.support.ui import Select
# seems like I shouldn't have to import each class
from Page.POM import TopNav
from Page.POM import ContactForm
from Page.POM import Homepage
from Page.POM import Footer
from selenium.webdriver.common import by

# should find a way to make the links work for either environment if we are really going to use this
# what would it take it take to get selenium set up on CW?
# headless driver


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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_verify_blog_page_title(self):
        # Navigates to the blog and verifies the title includes the word Blog

        self.topnav.nav_to_blog()
        # verify that Blog is in the title of the blog page
        self.assertIn("Blog", self.driver.title)
        #    self.driver.get_screenshot_as_file("/Users/robbie/Desktop/auto/blog_page_title_%s.png" % self.screen_name)

    def test_hero_button_loads_services_page(self):
        # Verify that the button in the hero image loads the services page
        self.topnav.nav_to_homepage()
        self.homepage.click_hero_image_button()
        # add a verification step here

    def test_casestudies_cards_navigation(self):
        # Verify that
        self.homepage.click_featured_case_study()
        # see if there is a way to use an assert here that knows what the featured case study is
        print("This should be the name of the case study featured on the homepage: " + self.driver.title)
        #    self.driver.get_screenshot_as_file("/Users/robbie/Desktop/auto/test_CS_cards_nav_%s.png" % self.screen_name)

    def test_count_blog_cards(self):
        # use the page object to nav to blog page instead of find element here
        self.topnav.nav_to_blog()
        # click view more posts and wait(sleep)
        self.driver.find_element_by_id("next").click()
        sleep(3)
        # count the number of cards
        posts_count = self.driver.find_elements_by_class_name("card-common--image_container")
        # verify the number of posts that display
        assert (len(posts_count) == 12)
        #    self.driver.get_screenshot_as_file("/Users/robbie/Desktop/auto/count_blog_cards_%s.png" % self.screen_name)

    # see if I can figure out how to test "Tech Talks card in resources section has most recent talk"

    # Footer tests cases:
    # Maybe it would be better to test by the H1 then the title??
    def test_footer_services(self):
        # Verify that services link in footer loads correct page
        self.footer.quick_links_services()
        assert self.driver.title == "Web Development and Consulting Services | Caktus Group"

    def test_footer_our_work(self):
        # Verify that our work link in footer loads correct page
        self.footer.quick_links_our_work()
        assert self.driver.title == "Django and SMS App Development Case Studies | Caktus Group"
        print("should be our work: " + self.driver.title)

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
        self.footer.quick_links_press()
        assert self.driver.title == "Contact Us for Custom Web Development | Caktus Group", \
            self.driver.get_screenshot_as_file("/Users/robbie/Desktop/auto/count_blog_cards_%s.png" % self.screen_name)



class ContactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")
        self.driver.get("https://caktus:pointy@staging.caktusgroup.com")

    def tearDown(self):
        self.driver.quit()

    def test_contact_form(self):
        # Use the POM class to navigate to contact page
        navigation = TopNav(self.driver)
        navigation.nav_to_contact()
        # Use the POM class to enter text in the contact form
        form = ContactForm(self.driver)
        form.first_name("MRtest")
        form.last_name("LastName")
        form.email("example@example.com")


class OtherTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/robbie/Downloads/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_4(self):
        # test that events match drop down selection
        self.driver.get("https://caktus:pointy@staging.caktusgroup.com/events/")
        # select an option from the drop down on events page by the visible text
        select = Select(self.driver.find_element_by_id("event-year"))
        select.select_by_value("2018")
        # verify the year in the date field
        # event_date = self.driver.find_elements_by_class_name("call-out")
        # self.assertIn("2018", event_date)


if __name__ == '__main__':
    unittest.main()
