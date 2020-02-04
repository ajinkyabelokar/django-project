from selenium import webdriver

# open IE 
driver = webdriver.Ie("E:\drivers\IEDriverServer.exe")

driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://www.facebook.com")
