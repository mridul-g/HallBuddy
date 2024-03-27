from selenium import webdriver
from selenium.webdriver.common.by import By

class Tests:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.fullscreen_window()
        self.driver.get("https://hallbuddyweb.pythonanywhere.com/")
        self.driver.implicitly_wait(0.5)

    def student_login(self):
        usrname = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")

        usrname.send_keys("mridulg22")
        password.send_keys("P@ssword12")
        submit_button.click()

    def admin_login(self):
        usrname = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")

        usrname.send_keys("admin")
        password.send_keys("admin")
        submit_button.click()
    
    def logout(self):
        logout_btn = self.driver.find_element(By.LINK_TEXT, "Logout")
        self.driver.get(logout_btn.get_attribute('href'))

    def dashboard_student(self):
        self.student_login()
        # Home tab and then links
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text20").click()
        # Map
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-fibsmapmarker").click()
        # Shop
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text14").click()
        # Dashboard
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-group52").click()
        #Dues
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text06").click()
        #contact
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text10").click()

        self.logout()

    def dashboard_admin(self):
        self.admin_login()
        # Home tab and then links
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text20").click()
        # Map
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-fibsmapmarker").click()
        # Shop
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text14").click()
        # Dashboard
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-group52").click()
        #Dues
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text06").click()
        #contact
        self.driver.find_element(By.CLASS_NAME, "guest-room-booking-text10").click()

        self.logout()

    def __del__(self):
        self.driver.quit()

    def correct_OTP(self):
        otp=input("OTP has been sent, please input it in the console ")
        self.driver.find_element(By.ID, "otp").send_keys(otp)
        self.driver.find_element(By.NAME, "submit_btn").click()

    def matching_password(self):
        self.driver.find_element(By.NAME, "password1").send_keys("1234@Pass")
        self.driver.find_element(By.NAME, "password2").send_keys("1234@Pass")
        self.driver.find_element(By.NAME, "submit_btn").click()

    def mismatching_password(self):
        self.driver.find_element(By.NAME, "password1").send_keys("1234@Pass")
        self.driver.find_element(By.NAME, "password2").send_keys("1234@Pass1")
        self.driver.find_element(By.NAME, "submit_btn").click()

    def hallmanager_signup(self):
        self.driver.get("https://hallbuddyweb.pythonanywhere.com")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign up").click()
        self.driver.find_element(By.ID, "name").send_keys("Tester")
        self.driver.find_element(By.ID, "username").send_keys("tester")
        self.driver.find_element(By.ID, "designation").send_keys("Hall Manager")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        self.correct_OTP()
        self.matching_password()
        # can't create the hall manager as one already exists
        in_wait = input("press to quit hall_manager: ")
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Someone already exists with this designation"
        print("Hall Manager already exists")

    def student_signup(self):
        self.driver.get("https://hallbuddyweb.pythonanywhere.com")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign up").click()
        self.driver.find_element(By.ID, "name").send_keys("Tester_student")
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.ID, "designation").send_keys("Student")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        self.correct_OTP()
        self.matching_password()
        in_wait = input("press to quit student account: ")


    def authentication_tests(self):

        self.hallmanager_signup()
        self.student_signup()

        self.driver.find_element(By.ID, "username").send_keys("tester")
        self.driver.find_element(By.ID, "password").send_keys("1234@Pass")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        in_wait = input("press to quit")
        self.driver.logout()




if(__name__ == "__main__"):
    test = Tests()
    # test.dashboard_student()
    # test.dashboard_admin()
    test.authentication_tests()