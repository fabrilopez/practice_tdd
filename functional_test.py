from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith hast heard about a cool new on-line to-do app. she goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.faul('Finish the test!')



if __name__ == '__main__':
    unittest.main(warnings='ignore')




