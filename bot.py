from selenium import webdriver
from time import sleep
import random

class my_bot():
	
	def __init__(self, username, password):

		self.username = username
		self.password = password
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(1)

	def signIn(self):
		self.browser.get('https://instagram.com')
		sleep(1)

		username_input = self.browser.find_element_by_css_selector("input[name='username']")
		password_input = self.browser.find_element_by_css_selector("input[name='password']")

		username_input.send_keys(self.username)
		password_input.send_keys(self.password)

		login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()

		sleep(2)

		info_save = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
		info_save.click()
		sleep(5)
		not_now = self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
		not_now.click()
	


	def follow_a_users_followers(self, u_name):
		self.browser.get('https://instagram.com/'+ u_name)
		sleep(0.5)
		followers = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
		followers.click()
		sleep(4)
		
		my_bot.scrollDown(self)
		
		follow_followers = self.browser.find_elements_by_css_selector('.FPmhX.notranslate._0imsa')
		num = 0
		for takipci in follow_followers:
			num += 1
			print(str(num) + ')' + takipci.text)

		follow_button = self.browser.find_elements_by_css_selector('.sqdOP.L3NKy.y3zKF')

		for a in follow_button:

			if a.text == 'Takip Et':
				a.click()
				sleep(random.randint(2, 5))
				print("followed")
			else:
				pass


	def scrollDown(self):

		JsCommand = """

			page = document.querySelector(".isgrP");
			page.scrollTo(0, page.scrollHeight)
			var pageend = page.scrollHeight;
			return pageend

		"""
		pageend = self.browser.execute_script(JsCommand)
		while True:
			end = pageend
			sleep(1)
			pageend = self.browser.execute_script(JsCommand)
			if end == pageend:
				break 

	def like_by_tag_and_follow(self, tag):

		self.browser.get("https://www.instagram.com/explore/tags/" + tag)
		sleep(5)
		posts = self.browser.find_elements_by_class_name("eLAPa")

		for post in posts: 
			post.click()
			follow_button = self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
			if follow_button.text == "Takip Et":
				follow_button.click()
			else: 
				pass
			like_button = self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button/div')
			like_button.click()
			close_button = self.browser.find_element_by_xpath('/html/body/div[6]/div[3]/button')
			close_button.click()
			sleep(random.randint(1, 5))


user = my_bot('your username', 'your password')
user.signIn()
user.follow_a_users_followers('odtu_2021_girisliler')

