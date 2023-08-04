"""
                                    Instagram Following Bot
Date:- August 04,2023
Developer:- Dinesh Singh

Description : This project is build by using Python's Selenium module. In this project, I automate following by the use of
python program where we don't need to manualy follow the users. Here I select a account and follow all its follower automatically
by using programming.

"""

#Your chromedriver and instagram account setup
CHROMEDRIVER_PATH = CHROME_DRIVER_PATH
TARGET_ACCOUNT = "https://www.instagram.com/_university_of_allahabad_1887_/"
UNAME = YOUR_INSTAGRAM_UNAME
PASSWORD = YOUR_INSTAGRAM_PASSWORD

#Necessary modules are imported here
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaFollower:
    def __init__(self):
        #variable declaration and intialization
        self.service = Service()
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service,options=self.option)
        self.no_of_followers = None
        self.loginid = None
        self.password = None
    def login(self):
        """Here we simply login into the instagram"""
        #Opening the instagram website login page
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(5)
        #filling the username field
        self.loginid = self.driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.loginid.send_keys(UNAME)
        #Filling the password field and login
        self.password = self.driver.find_element(by=By.XPATH,value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        self.password.send_keys(Keys.ENTER)
        sleep(5)

    def find_follower(self):
        """Here we opend target instagram account whose follower we want to follow"""
        self.driver.get(url=TARGET_ACCOUNT) #opeing the account
        sleep(5)
        #Get the account's follower number
        followers = self.driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span')
        self.no_of_followers = int((followers.text.strip()).replace(",",""))
        sleep(5)

    def follow(self):
        """Here we follow all the account"""
        #Opening the followers dialog-box
        follow = self.driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        follow.click()
        sleep(5)
        #Following all the followers one by one
        for i in range(13):
            xpath = f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i+1}]/div/div/div/div[3]/div/button'
            follow = self.driver.find_element(by=By.XPATH,value=xpath)
            #Using this condition we looking for those who we don't follow
            if follow.text == "Follow":
                follow.click()
            sleep(3)
        sleep(15)

#Methods Call
instaFollower = InstaFollower()
instaFollower.login() #login to the instagram
instaFollower.find_follower() #get the account total no. of follwer
instaFollower.follow() #follow all the followers
