from os import path
import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#edit the values to your needs

update_custom_status_time = 7   #5sec is the minimum
is_random_custom_status = False
is_persistent_profile = True
headless_mode = True            #show/hide browser window

#only if you do not use an existing profile
#(every time you start, the program will need the credentials)
#does not work with 2FA yet
email_address = "YOUR EMAIL ADDRESS"
password = "YOUR PASSWORD"

#only if you use an existing profile
#it is recommended to create a new profile especially for this purpose
#make sure that the cookies are stored in there
profile_folder = "C:\\Users\\<user_name>\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\<profile_name>"

#enter your custom messages here
custom_status_list = ["ABC", "DEF", "GHI", "JKL"]




def start_driver():
    options_firefox = webdriver.FirefoxOptions()
    options_firefox.headless = headless_mode
    if (is_persistent_profile):

        #for an existing profile
        fp = webdriver.FirefoxProfile(profile_folder)
        driver = webdriver.Firefox(fp, options=options_firefox, service=Service(executable_path=GeckoDriverManager().install()))
        time.sleep(1)
        driver.get('https://discord.com/channels/@me')

    else:
        #for a new profile
        driver = webdriver.Firefox(options=options_firefox, service=Service(executable_path=GeckoDriverManager().install()))
        time.sleep(1)
        driver.get('https://discord.com/channels/@me')
        time.sleep(4)

        continue_in_browser_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/section/div/button[2]/div")                                                     
        continue_in_browser_field.click()
        time.sleep(1)

        #login
        email_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
        email_field.send_keys(email_address)
        password_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
        password_field.send_keys(password)
        login_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]")
        login_field.click()

    #update custom status random
    if (is_random_custom_status):
        while (True):
            time.sleep(2)
            time.sleep(update_custom_status_time - 5)
            profile_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/section/div[2]/div[1]/div")
            profile_field.click()
            time.sleep(1)

            set_a_custom_status_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div[7]/div").click()
            time.sleep(1)
            status_text_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/input").clear()
            status_text_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/input")
            status_text_field.send_keys(random.choice(custom_status_list))
            status_save_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[3]/button[1]").click()
            time.sleep(1)

    #update custom status in order
    else:
        while (True):
            for y in range(len(custom_status_list)):
                time.sleep(2)
                time.sleep(update_custom_status_time - 5)                
                profile_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/section/div[2]/div[1]/div")
                profile_field.click()                           
                time.sleep(1)

                set_a_custom_status_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div/div/div/div[7]/div").click()
                time.sleep(1)
                status_text_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/input").clear()
                status_text_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/input")
                current_status = custom_status_list[y]
                status_text_field.send_keys(current_status)
                status_save_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div/div[3]/button[1]").click()
                time.sleep(1)

if __name__ == '__main__':
    start_driver()
