import pandas as pd 
# note , if you want a less pythonic way of doing this , you can always mess around with the webpage text to get what you need . 
# this just seemed better . 


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time 

driver = webdriver.Chrome("C:\\Users\\raosa\\Desktop\\PROJECTS\\chromedriver.exe")
driver.get("https://mymasonportal.gmu.edu/webapps/login/?action=relogin")
driver.implicitly_wait(15)
driver.maximize_window()



driver.find_element_by_id("user_id").send_keys("GMU ID")
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_id("entry-login").click()
time.sleep(7)
driver.find_element_by_link_text("Courses").click()
driver.find_element_by_link_text("201770.73833 DAEN-690-001 (Fall 2017)").click()
driver.find_element_by_link_text("Discussion Board").click()
driver.find_element_by_link_text("Curiosity and Knowledge Discovery/Seeking/Sharing Cafe").click() 
time.sleep(7)

pag.click(x=628,y=555)
driver.find_element_by_id("reply__5608179_1").click()
pag.press('tab')
time.sleep(5)
pag.typewrite('I like dank memes and I cannot lie')
time.sleep(5)
driver.find_element_by_id("bottom_submitBtn").click()
time.sleep(3)
driver.quit()





#enter lat long values 


w
"""
driver.find_element_by_id("lat").send_keys("31.2")
driver.find_element_by_id("lon").send_keys("-73.4")

# enter date ranges . 
#For testing , even if we do not have what we need , we can still check . Take care of this later . Update : done
# what I am basically doing here is clicking the lon value , hitting tab thrice to get to the year , and then getting to the year 1983

driver.find_element_by_id("lon").click()
lonelement=driver.find_element_by_id("lon")
lonelement.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP+Keys.UP)


# shitty method , but gets the work done , so I'm cool either way . 
# see if there is any way I can kinda scale for this . For example , for a 1920 * 1080 , i need the below values . 
# similarly , for a lower res , can I scale what I need ? 
pag.click(x=930,y=807)
pag.keyDown('ctrl')
pag.press('a')
pag.keyUp('ctrl')

text1="lat is this long is that"


driver.find_element_by_name("submit").click()

driver.find_element_by_link_text("Download a text file").click()
time.sleep(3)
pag.keyDown('ctrl')
pag.press('s')
pag.keyUp('ctrl')
time.sleep(3)
pag.typewrite(text1)
time.sleep(3)
pag.press('enter')
time.sleep(3)





# select all that we need ... try clicking on one of them and then doing a ctrl + a 
#driver.find_element_by_id("t2m").click() # this is for air temp at 2 m ... thanks obama , not working :| 

# if we do not have a method to work with , as a last resort , we can do this . 
# but this is a shitty way of doing it , i admit . 
el=driver.find_element_by_id(lon")

action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(el, 50, 50)
action.click()
action.perform()




# SMILE UR ON CAMERA 
#driver.get_screenshot_as_file('dank.png')

#driver.quit()
"""