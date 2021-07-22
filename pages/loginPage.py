class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        self.usrname_textbox_xpath="//input[@name='txtUsername' and @id='txtUsername']"
        self.psw_textbox_xpath="//input[@name='txtPassword' and @id='txtPassword']"
        self.login_button_xpath="//input[@name='Submit' and @id='btnLogin']"

    def enter_usrname(self,usrname):
        self.driver.find_element_by_xpath(self.usrname_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.usrname_textbox_xpath).send_keys("Admin")
    def enter_psw(self,psw):
        self.driver.find_element_by_xpath(self.psw_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.psw_textbox_xpath).send_keys("admin123")
    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()


