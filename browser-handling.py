from selenium import webdriver
import time

main_url = 'https://www.20min.ch'
tab_url = 'https://www.google.com'

# set Chrome options
browser_options = webdriver.ChromeOptions()
browser_options.add_argument("--start-fullscreen")

# open main window
browser = webdriver.Chrome(options=browser_options)
browser.get(main_url)
print("Current Page Title is: {}".format(browser.title))

time.sleep(5)

# open a new window
browser.execute_script("window.open('');")

# switch to new window and open new tab
browser.switch_to.window(browser.window_handles[1])
browser.get(tab_url)
print("Current Page Title is {}".format(browser.title))

# close the browser page
browser.close()

# switch back to the first window and open main url
browser.switch_to.window(browser.window_handles[0])
print("Current Page Title is {}".format(browser.title))
