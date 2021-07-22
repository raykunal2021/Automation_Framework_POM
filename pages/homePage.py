class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_linktext = "Welcome Paul"
        self.logout_link_linktext = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_partial_link_text(self.welcome_link_linktext).click()

    def click_logout(self):
        self.driver.find_element_by_partial_link_text(self.logout_link_linktext).click()

