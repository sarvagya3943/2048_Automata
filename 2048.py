# Import Crap 
from selenium import webdriver
import random ,time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Get the browser going
browser = webdriver.Chrome('C:\Users\Sandeep Aggarwal\chromedriver_win32\chromedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')

# send keys to this grid
grid = browser.find_element_by_css_selector('body')

# return true if the game is over
def game_is_over() :
	try :
		browser.find_element_by_class_name('game-over')
	except NoSuchElementException : 
		return False 
	return True 

# actual Loop 
while True :
	if game_is_over() :
		button = browser.find_element_by_class_name('retry-button')
		print button
		button.click()
	x = random.randint(1,4) 
	if x==1 :
		grid.send_keys(Keys.UP)
		print 'UP'
	elif x==2 :
		grid.send_keys(Keys.DOWN)
		print 'DOWN'
	elif x==3 :
		grid.send_keys(Keys.LEFT)
		print 'LEFT'
	else :
		grid.send_keys(Keys.RIGHT)
		print 'RIGHT'
	# add a time.sleep() if you want to slow it down 