from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(r"C:\Python\add.crx")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(r"C:\Python\chromedriver.exe", options=chrome_options)
driver.set_window_size(720,750)

driver.get('https://www.yourquote.in/login/')
sleep(3)
gmail = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[1]/main/div/div/div[2]/div[1]/div').click()
usr = input('Enter your username or email id: ')
pwd = getpass('Enter your password : ')
base_window = driver.window_handles[0]  
driver.switch_to.window(driver.window_handles[1])
sleep(2)
gmail_user= driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(usr)
nex=driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
sleep(2)
password_box = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pwd)
nx = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()  
sleep(2)
driver.switch_to.window(driver.window_handles[0])
# driver.get('https://www.yourquote.in/explore')
sleep(3)
ex=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/a[2]/div/div').click()
sleep(3)
driver.maximize_window()
sleep(2)
p=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]').click()
#for remove  ads
# all_iframes = driver.find_elements_by_tag_name("iframe")
# if len(all_iframes) > 0:
#     print("Ad Found\n")
#     driver.execute_script("""
#         var elems = document.getElementsByTagName("iframe"); 
#         for(var i = 0, max = elems.length; i < max; i++)
#              {
#                  elems[i].hidden=true;
#              }
#                           """)
#     print('Total Ads: ' + str(len(all_iframes)))
# else:
#     print('No frames found')
scroll_box = driver.find_element_by_xpath('//*[@id="__nuxt"]')
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
for n in range(1, 1000):
    sleep(1)
    # follow=driver.find_element_by_xpath('//span[text()="FOLLOW"]').click()
    like=driver.find_element_by_xpath('//div[@title="Like"]').click()

    sleep(2)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)


