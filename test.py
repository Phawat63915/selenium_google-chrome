from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#create chromeoptions instance
options1 = webdriver.ChromeOptions()
options2 = webdriver.ChromeOptions()
# options.add_argument("--headless")
options1.add_argument("--no-sandbox")
options2.add_argument("--no-sandbox")

#provide location where chrome stores profiles
options1.add_argument(r"--user-data-dir=C:/Users/Phawat/AppData/Local/Google/Chrome/User Data")
options2.add_argument(r"--user-data-dir=C:/Users/Phawat/AppData/Local/Google/Chrome/User Data")

#provide the profile name with which we want to open browser
options1.add_argument(r'--profile-directory=Profile 124')
options2.add_argument(r'--profile-directory=Profile 125')

#specify where your chrome driver present in your pc
driver1 = webdriver.Chrome(options=options1)
driver2 = webdriver.Chrome(options=options1)

#provide website url here
driver1.get("https://www.google.com/")
driver2.get("https://www.google.com/")
time.sleep(1)
search_box = driver1.find_element("name", "q")  # Find the search input element by its name attribute
search_box.send_keys("Phawat")  # Enter the search term
search_box.clear()
search_box.send_keys("Phawatsf Total")  # Enter the search term
search_box.clear()
search_box.submit()  # Submit the search form

# Wait for a few seconds to see the search results (You can adjust the sleep time as needed)
time.sleep(2)
driver1.get("https://www.phawat.ovh/")
time.sleep(5)

# Close the WebDriver
driver1.quit()
driver2.quit()