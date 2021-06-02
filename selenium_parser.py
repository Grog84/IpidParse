from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from googleSheetInterface import MyGoogleSheet

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get("https://www.dnb.com/business-directory/company-profiles.34bigthings_srl.a0afafb424d5824e9e5fb9722827673e.html")
# driver.close()

Goog = MyGoogleSheet("1CYtmbpPsTMIkgKHp0zGkCxB4chcSNEB-qL2Ifb4d6pw")
Goog.Init()

driver.get("https://www.ipid.dev/mappa/")

try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.sorting_1.wpgmza_table_title"))
    )
except:
    driver.quit()

search = driver.find_elements_by_css_selector("td.sorting_1.wpgmza_table_title")
print(len(search))
companiesName = []
for s in search:
    companiesName.append([s.text])
    print(s.text)

Goog.WriteData("CompaniesRef!A2", companiesName)


driver.quit()