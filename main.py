import re
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
from Base import (
    initialize_driver,
    click_element_xpath,
    get_element,
    get_element_xpath,
    get_list,
)


# Main crawling function
def crawl_india_code():
    """
    Main crawling function to scrape information for Act, Sections and Section Paragraphs from the India Code website.

    Returns:
    - list: A list containing dictionaries with act and section information and Section Paragraph.
    """
    driver = initialize_driver()
    driver.get("https://www.indiacode.nic.in/")

    all_data = []

    try:
        # Click on browse central acts
        click_element_xpath(driver, "/html/body/header/div[4]/div/nav/ul[1]/li[4]/a")

        # Select Enactment date
        click_element_xpath(
            driver, "/html/body/header/div[4]/div/nav/ul[1]/li[4]/ul/li[4]/a"
        )
        
        # Select Order by Descending
        dropdown_for_order = get_element_xpath(driver, '//*[@id="browse_controls"]/form/select[2]/option[2]')
        dropdown_for_order.click()

        # Select 100 Acts from dropdown
        dropdown_for_count = get_element_xpath(driver, '//*[@id="browse_controls"]/form/select[3]/option[20]')
        dropdown_for_count.click()

        # Click the Update button
        update_button = get_element_xpath(driver, '//*[@id="browse_controls"]/form/input[3]')
        update_button.click()
        
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
        # Click next button
        get_element(
            driver,
            By.CSS_SELECTOR,
            "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
        ).click()
            

        for k in range(9):
            # Get acts table
            tbody = get_element_xpath(driver, '//*[@id="content"]/div/div/div[2]/div/table/tbody')

            # Get list of tr tags - acts
            all_acts = get_list(tbody, By.TAG_NAME, "tr")
            print(len(all_acts))

            start_index = 36 if k == 0 else 2
            
            # Iterate through every acts
            for i in range(start_index, len(all_acts) + 1):
                sections_list = []
                # Act text Xpath
                act_index = (
                    f'//*[@id="content"]/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]'
                )
                # Act text
                act_name = get_element_xpath(driver, act_index).text

                # Section view link
                sections_link = (
                    f'//*[@id="content"]/div/div/div[2]/div/table/tbody/tr[{i}]/td[4]/a'
                )
                # Click view sections
                click_element_xpath(driver, sections_link)

                section_info = get_element_xpath(
                    driver, '//*[@id="myTableActSection_info"]'
                ).text
                if section_info == "Showing 0 to 0 of 0 entries":
                    driver.back()
                    continue

                # Select 100 limit
                select = Select(driver.find_element(By.XPATH, '//*[@id="myTableActSection_length"]/label/select'))
                select.select_by_value('100')

                while True:

                    # Get section table
                    sections_body = get_element_xpath(driver, '//*[@id="myTableActSection"]/tbody')

                    # Get all the sections
                    all_sections = get_list(sections_body, By.TAG_NAME, "tr")

                    print(f"Act: {act_name}")
                    print("Number of sections:", len(all_sections))

                    # Iterate through every sections
                    for j in range (0, len(all_sections)):
                        # For section name
                        section_name = get_element(all_sections[j], By.XPATH, "td/div/a").text
                        pattern = re.compile(r"repeal|omit", re.IGNORECASE)
                        if pattern.search(section_name):
                            continue
                        print(section_name)
                        
                        
                        click_button_1 = f"/html/body/main/div[1]/div/div/div[2]/div/div[13]/div[2]/div/div/div/table/tbody/tr[{j + 1}]/td/div/span"
                        click_button_2 = f"/html/body/main/div/div/div[1]/div[2]/div/div[13]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{j + 1}]/td/div/span"
                        
                        section_paragraph_1 = f'/html/body/main/div[1]/div/div/div[2]/div/div[13]/div[2]/div/div/div/table/tbody/tr[{j + 1}]/td/div/div/div/p'
                        section_paragraph_2 = f'/html/body/main/div/div/div/div[2]/div[1]/div[13]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{j + 1}]/td/div/div/div/p'
                        
                        try:
                            # Check if the first XPath is clickable
                            WebDriverWait(driver, 1).until(
                                EC.element_to_be_clickable((By.XPATH, click_button_1))
                            )
                            # If clickable, click the first XPath
                            click_element_xpath(driver, click_button_1)
                        except:
                            # If not clickable, click the second XPath
                            click_element_xpath(driver, click_button_2)
                        time.sleep(0.5)
                        
                        # Check if the first XPath is present
                        try:
                            section_paragraph_element = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.XPATH, section_paragraph_1))
                            )
                        except:
                            # If not present, try the second XPath
                            section_paragraph_element = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.XPATH, section_paragraph_2))
                            )

                        # Extract section paragraph text
                        section_paragraph_text = section_paragraph_element.text
                        print(section_paragraph_text)
                            
                        try:
                            # Check if the first XPath is clickable
                            WebDriverWait(driver, 1).until(
                                EC.element_to_be_clickable((By.XPATH, click_button_1))
                            )
                            # If clickable, click the first XPath
                            click_element_xpath(driver, click_button_1)
                        except:
                            # If not clickable, click the second XPath
                            click_element_xpath(driver, click_button_2)
                        #time.sleep(1)

                        # Append section data to the sections_list
                        sections_list.append({"Section": section_name, "Paragraph": section_paragraph_text})


                    # Check for the presence of the next button
                    next_button_xpath = '//*[@id="myTableActSection_next"]'
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, next_button_xpath))
                    )
                    if 'disabled' not in next_button.get_attribute('class'):
                        # Click the next button
                        click_element_xpath(driver, next_button_xpath)
                        print("Next button found")
                    else:
                        # No "Next" button found, break the loop
                        print("No next button")
                        break
                    
                # Append act data to all_data
                all_data.append({"act": act_name, "sections": sections_list})
                driver.back()


            # Click next button
            get_element(
                driver,
                By.CSS_SELECTOR,
                "#content > div > div > div:nth-child(2) > div > div.panel-footer.text-center > a.pull-right",  # noqa: E501
            ).click()
            print(f"{100 * (k+1)} acts")


    except Exception as ex:
        print(f"Exception - {ex}")
        return f"Exception occurred - {str(ex)}"
    finally:
        # Quite driver
        driver.quit()
        # Write the data to the JSON file
        with open("all_acts_sections.json", "w") as json_file:
            json.dump(all_data, json_file, indent=4)
        print("Json file successfully written...")
    return all_data

crawl_india_code()