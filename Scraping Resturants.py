from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv



options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



search_url = "https://www.google.com/search?q=restaurants+in+City+Stars,+Cairo&hl=en"
driver.get(search_url)
time.sleep(5)



try:
    show_more_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Odp5De"]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/h3/g-more-link/a'))
    )
    driver.execute_script("arguments[0].click();", show_more_button)
    time.sleep(5)
except:
    pass



restaurant_xpath = '//*[@id="rl_ist0"]/div/div[1]/div[3]//div[@jscontroller="AtSb"]//a'
restaurants = driver.find_elements(By.XPATH, restaurant_xpath)

restaurant_data = set()

for index in range(len(restaurants)):
    try:
        restaurants = driver.find_elements(By.XPATH, restaurant_xpath)
        driver.execute_script("arguments[0].click();", restaurants[index])
        time.sleep(3)

        # Extracted details using JavaScript
        name = driver.execute_script("""
            let nameElement = document.querySelector("h2[data-attrid='title'] span");
            return nameElement ? nameElement.innerText : null;
        """)

        address = driver.execute_script("""
            let addressElement = document.querySelector("span.LrzXr");
            return addressElement ? addressElement.innerText : "N/A";
        """)

        rating = driver.execute_script("""
            let ratingElement = document.querySelector("span.Aq14fc");
            return ratingElement ? ratingElement.innerText : "N/A";
        """)

        phone = driver.execute_script("""
            let phoneElement = document.querySelector("span.LrzXr.zdqRlf.kno-fv");
            return phoneElement ? phoneElement.innerText : "N/A";
        """)

        restaurant_data.add((name, address, rating, phone))

    except Exception as e:
        print(f"Error processing restaurant {index + 1}: {e}")

# Save the data
with open("restaurant_details.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Address", "Rating", "Phone"])
    writer.writerows(restaurant_data)

driver.quit()