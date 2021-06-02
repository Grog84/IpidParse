from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from googleSheetInterface import MyGoogleSheet

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--window-size=1900,1000")

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

Goog = MyGoogleSheet("1CYtmbpPsTMIkgKHp0zGkCxB4chcSNEB-qL2Ifb4d6pw")
Goog.Init()


companiesName = []
GetFromIPID = False

starting_idx = -1

if GetFromIPID:
    driver.get("https://www.ipid.dev/mappa/")

    try:
        IPID_companies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.sorting_1.wpgmza_table_title"))
        )
    except:
        driver.quit()

    IPID_companies = driver.find_elements_by_css_selector("td.sorting_1.wpgmza_table_title")
    print(len(IPID_companies))
    
    for s in IPID_companies:
        companiesName.append([s.text])
        print(s.text)

    Goog.WriteData("CompaniesRef!A2", companiesName)

    driver.quit()
else:
    starting_idx = 92
    final_idx = starting_idx + 15
    companiesName = Goog.ReadData("CompaniesRef!A" + str(starting_idx) + ":A" + str(final_idx))

# Getting all links

print(companiesName)

companiesLinks = []

driver.get("https://www.dnb.com")

time.sleep(2)
DnB_search_button = driver.find_element_by_id("search_button")
# DnB_search_button.send_keys(Keys.RETURN)
DnB_search_button.click()

time.sleep(3)

DnB_search_query_button = driver.find_element_by_id("search_query")
for company_string_name in companiesName:
    
    for char in company_string_name[0]:
        DnB_search_query_button.send_keys(char)
        time.sleep(0.2)

    time.sleep(1)
    try:
        Company_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.company_profile_link"))
        )
    except:
        Company_link = None

    # Company_link = driver.find_element_by_css_selector("a.company_profile_link")
    if Company_link is not None:
        link = Company_link.get_attribute('href')
        companiesLinks.append([link])
    else:
        companiesLinks.append([""])

    for char in company_string_name[0]:
        DnB_search_query_button.send_keys(Keys.BACKSPACE)
        time.sleep(0.2)

if starting_idx == -1:
    Goog.WriteData("CompaniesRef!B2", companiesLinks)
else:
    Goog.WriteData("CompaniesRef!B" + str(starting_idx), companiesLinks)

driver.quit()