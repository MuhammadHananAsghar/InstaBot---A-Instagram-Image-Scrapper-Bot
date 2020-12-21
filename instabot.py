from selenium import webdriver
from time import sleep
from tkinter import filedialog
import urllib.request
import datetime

USERNAME = "XXXXXXXXXXXXXXXXXXX"
PASSWORD = "XXXXXXXXXXXXXXXXXXX"


class InstaBot:
	def __init__(self, user):
		self.user = user
		self.url = "https://www.instagram.com/"+self.user
		self.site = "https://www.instagram.com/"
		self.path = "/XXXXXXXXXXXXXXXXXXXXXXX/geckodriver"
		
		self.__start(self.site, self.path, self.url)


	def __start(self, site, path, url):
		print("Bot is Started")
		driver = webdriver.Firefox(executable_path=path)
		driver.get(site)
		sleep(2)

		if self.__login(driver):
			sleep(2)
			self.__scrape(url, driver)
		else:
			print("Failed")


	def __login(self, driver):
		print("Bot is Loging In")
		try:
			username = driver.find_element_by_name("username")
			username.clear()
			username.send_keys(USERNAME)
			sleep(2)
			password = driver.find_element_by_name("password")
			password.clear()
			password.send_keys(PASSWORD)
			sleep(2)
			driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
			sleep(10)
			driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
			return True
		except:
			return False


	def __scrape(self, url, driver):
		print("Bot is Fetching Username")
		driver.get(url)
		sleep(2)
		self.__scroll(driver)
		sleep(2)
		print("Select Path")
		path_storage = filedialog.askdirectory()
		print("Bot is Fetching Data")
		data = driver.find_elements_by_class_name("FFVAD")
		if data:
			img_id = 0
			for i in data:
				self.__save(i.get_attribute("src"), path_storage, img_id)
				img_id += 1
		return


	def __save(self, image, path, id):
		suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
		filename = "_".join([self.user, suffix])
		urllib.request.urlretrieve(f"{image}", f"{path}/{str(filename)}_{str(id)}.jpg")
		print("Saved File", str(filename)+".jpg")
		print("Bot Has Saved the Data")
		return


	def __scroll(self, driver):
		print("Bot is Scrolling")
		times = 0
		SCROLL_PAUSE_TIME = 2
		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")
		while True:
		    # Scroll down to bottom
		    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    # Wait to load page
		    sleep(SCROLL_PAUSE_TIME)
		    # Calculate new scroll height and compare with last scroll height
		    new_height = driver.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height
		    times += 1
		    if times == 10:
		    	break
		return


bot = InstaBot("XXXXXXXXXXXXXX")
