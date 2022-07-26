import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#import datetime
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="session", autouse=True)
def test_setup():
    global driver, a
    driver = webdriver.Chrome(executable_path="D:/final year/bachelor project/intern/sifu selenium/chromedriver.exe") 
    driver.get("https://idm.sifu.tmrnd.com.my/auth/realms/sifu/protocol/openid-connect/auth?client_id=app-access&redirect_uri=https%3A%2F%2Fems.sifu.tmrnd.com.my%2Fevent-maintenance%2Fevent-master&state=fdbf3c29-da79-471f-88da-6d44f6bf081c&response_mode=fragment&response_type=code&scope=openid&nonce=5f740217-9e33-45b0-9ef4-ca8fb72b997a")
    driver.implicitly_wait(10)
    driver.maximize_window()
    a = ActionChains(driver)
   

def test_login():
    #enter username
    username = driver.find_element(By.CSS_SELECTOR, '[placeholder="Username"]')
    username.send_keys('sqa0001')
    time.sleep(2)

    #enter password
    password = driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]')
    password.send_keys('pass1234')
    time.sleep(2)

    #login
    login_btn = driver.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    login_btn.click()
    time.sleep(2)

       
# CREATE NEW EVENT 
def test_NewEvent():

    #identify element newevent
    newevent = driver.find_element_by_xpath("//*[@class='me-2 main-btn appearance-filled size-small shape-rectangle icon-start status-info ng-star-inserted nb-transition']")
    newevent.click()
    time.sleep(2)

# ENTER EVENT DETAILS
def test_EventDetails():
    #identify element newevent
    eventname = driver.find_element_by_xpath("//input[@name='eventName']")
    eventname.send_keys('testing1234')
    time.sleep(2)
    eventdate = driver.find_element_by_xpath("//input[@name='startDate']")
    a.move_to_element(eventdate).click().perform()
    


    time.sleep(2)

    driver.close()

































    






















    

 

    

    
    




    
   

