from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

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

    def matching_password_2(self):
        self.driver.find_element(By.NAME, "password1").send_keys("1234@Pass2")
        self.driver.find_element(By.NAME, "password2").send_keys("1234@Pass2")
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
        self.mismatching_password()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Passwords don't match"

        self.matching_password()
        # can't create the hall manager as one already exists
        # in_wait = input("press to quit hall_manager: ")
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
        self.mismatching_password()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Passwords don't match"

        self.matching_password()
        # in_wait = input("press to quit student account: ")

    def wrong_then_correct_test_student(self):
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.ID, "password").send_keys("1234@Pass123")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Incorrect Password or Username"
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.ID, "password").send_keys("1234@Pass")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()

    def wrong_then_correct_test_student_2(self):
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.ID, "password").send_keys("1234@Pass123")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Incorrect Password or Username"
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.ID, "password").send_keys("1234@Pass2")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()

    def incorrect_then_resend_otp(self):
        self.driver.find_element(By.ID, "otp").send_keys("0000")
        self.driver.find_element(By.NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Incorrect OTP"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Resend OTP").click()
        self.correct_OTP()

    def reset_password(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Password").click()
        self.driver.find_element(By.ID, "username").send_keys("tester_student")
        self.driver.find_element(By.CSS_SELECTOR, value='button').click()
        self.incorrect_then_resend_otp()
        self.mismatching_password()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Passwords don't match"
        self.mismatching_password()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Passwords don't match"
        self.mismatching_password()
        assert self.driver.find_element(By.CLASS_NAME, "alert-danger").text == "Passwords don't match"
        self.matching_password_2()

        # in_wait = input("press to quit student account: ")
        self.wrong_then_correct_test_student_2()

    def authentication_tests(self):

        print("Begining Authentication Tests")
        self.hallmanager_signup()
        self.student_signup()
        self.wrong_then_correct_test_student()
        # in_wait = input("press to quit")
        self.logout()
        self.reset_password()
        self.logout()
        print("Authentication Tests Passed")

    def complaints_student(self):
        self.student_login()
        self.driver.implicitly_wait(0.5)
        self.driver.find_elements(By.CLASS_NAME, "guest-room-booking-text16")[0].click()
        
        

        #clinking on new-complaint
        self.driver.find_elements(By.CLASS_NAME, "btn.btn-success")[0].click()

        #making requests

        #request 1 : 
        self.driver.find_elements(By.CLASS_NAME, "room_text")[1].send_keys("D-213")

        #complaint sub-cateogry and category :
        self.driver.find_element(By.ID, "dropdown1").send_keys("Electrical")
        self.driver.find_element(By.ID, "dropdown2").send_keys("Fan not working")


        self.driver.find_elements(By.CLASS_NAME, "comments_rec")[0].send_keys("Room check")
        self.driver.find_elements(By.CLASS_NAME, "submit_rec")[0].click()
        self.logout()

        #admin_login
        self.driver.implicitly_wait(0.5)
        self.admin_login()
        self.driver.explicitly_wait(5)
        self.driver.find_elements(By.CLASS_NAME, "guest-room-booking-text16")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "mridulg22")

    def mark_resolved_complaint(self):
        self.student_login()
        self.driver.implicitly_wait(0.5)
        self.driver.find_elements(By.CLASS_NAME, "guest-room-booking-text16")[0].click()

        #mark_resolved
        self.driver.find_elements(By.CLASS_NAME, "btn.btn-outline-success.btn-sm")[0].click()

        #try to mark some-one else's complaint as resolved 
        self.driver.find_elements(By.CLASS_NAME, "btn.btn-outline-success.btn-sm")[1].click()

    def test1_new_annc(self,catch_item):
         #Announcement being added correctly in the admin page
        self.admin_login()
        self.driver.find_element(By.NAME, "add_hidden_item").click()        
        self.driver.find_element(By.NAME, catch_item).send_keys("Test Announcement")
        self.driver.find_element(By.NAME, "submit").click() 
        assert(self.driver.find_elements(By.CLASS_NAME, "alert-success")[0].text == "Changes made successfully.")
        time.sleep(5)
        self.logout()
        #New Announcement visible to the user
        self.student_login()
        assert(self.driver.find_elements(By.TAG_NAME, "td")[4].text == "Test Announcement" and self.driver.find_elements(By.TAG_NAME, "td")[5].text ==datetime.date.today().strftime("%B %d, %Y"))
        time.sleep(5)
        self.logout()

    def test2_edit_annc(self,catch_item):
         #Announcement being edited correctly in the admin page
        self.admin_login()
        self.driver.find_element(By.NAME, "edit").click() 
        self.driver.find_element(By.NAME, catch_item).clear()       
        self.driver.find_element(By.NAME, catch_item).send_keys("Test Announcement Edited")
        self.driver.find_element(By.NAME, "submit").click() 
        assert(self.driver.find_elements(By.CLASS_NAME, "alert-success")[0].text == "Changes made successfully.")
        time.sleep(5)
        self.logout()
        #Edited Announcement visible to the user
        self.student_login()
        assert(self.driver.find_elements(By.TAG_NAME, "td")[4].text == "Test Announcement Edited" and self.driver.find_elements(By.TAG_NAME, "td")[5].text ==datetime.date.today().strftime("%B %d, %Y"))
        time.sleep(5)
        self.logout()

    def delete_test_annc(self):
        self.admin_login()
        self.driver.find_elements(By.TAG_NAME, "td")[5].click()
        time.sleep(5)
        self.logout()
        
        
    def announcements_test(self):
        annc_num=39
        catch_item="item"+str(annc_num)
        self.test1_new_annc(catch_item)
        self.test2_edit_annc(catch_item)
        self.delete_test_annc()


if(__name__ == "__main__"):
    test = Tests()
    # test.dashboard_student()
    # test.dashboard_admin()
    test.authentication_tests()
    test.complaints_student()