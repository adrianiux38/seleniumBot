
from selenium import webdriver
import time

def blast():
    userId = "antunezdiana106@gmail.com"
    password = "106dianaantunez"
    browser = webdriver.Chrome("/usr/local/bin/chromedriver")
    
    # The complete post URL directly with Login, at first directly go to the story without signing in to FB, from there click on Login button, then your get a URl something like below
    postURL = "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fstory.php%3Fstory_fbid%3D2719021618424341%26id%3D100015616535127&ref=104&rs=26&rid=100047630109182&refsrc=https%3A%2F%2Fm.facebook.com%2Fstory.php&refid=52"
    browser.get(postURL)
    userIdField = browser.find_element_by_id("m_login_email")
    passwordField = browser.find_element_by_id("m_login_password")    
    loginButton = browser.find_elements_by_tag_name("button")[0]
    userIdField.send_keys(userId)
    passwordField.send_keys(password)
    loginButton.click()
    time.sleep(10)
    # comment 100 times
    for i in range(100):
        time.sleep(3)
        commentBox = browser.find_element_by_id("composerInput")
        commentBox.send_keys("botCmnt")
        time.sleep(1)
        sendButton = browser.find_elements_by_tag_name("button")[0]
        sendButton.click()
        
blast()