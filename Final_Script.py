import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re

# Initialize a counter variable
product_counter = 0

def click_see_more(driver):
    try:
        # Find and click the "See more" button
        see_more_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'See more')
        see_more_button.click()
        time.sleep(1)  # Wait for the content to expand
    except Exception as e:
        # If the "See more" button is not found, continue without clicking
        print(f"See more button not found. Continuing without clicking.")
        pass

def truncate_text(text, max_words=6):
    # Truncate the input text to at most max_words words
    words = text.split()
    if len(words) <= max_words:
        return text
    else:
        return ' '.join(words[:max_words])

def scrape_amazon_product_info(driver, url, output_folder):
    global product_counter  # Access the global counter variable
    try:
        # Open the provided URL
        driver.get(url)
        # Wait for the page to load (you might need to adjust the wait time)
        time.sleep(5)

        # Check if the "See more" button exists and click it if found
        if driver.find_elements(By.PARTIAL_LINK_TEXT, 'See more'):
            click_see_more(driver)

        # Find the product title element
        product_title_element = driver.find_element(By.ID, 'productTitle')

        # Get the product title text
        product_title = product_title_element.text.strip()
        truncated_title = truncate_text(product_title, max_words=6)  # Truncate the title

        # Find the price element
        price_element = driver.find_element(By.ID, 'corePrice_feature_div')

        # Extract the price text from the element
        price = price_element.find_element(By.CLASS_NAME, 'a-price-whole').text + '.' + price_element.find_element(By.CLASS_NAME, 'a-price-fraction').text

        # Find the additional details text element, if it exists
        additional_details_element = None
        try:
            additional_details_element = driver.find_element(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-partial-collapse-content.a-expander-content-expanded')
        except:
            pass

        additional_details_text = additional_details_element.text.strip() if additional_details_element else ""

        # Find all div elements with class 'aplus-v2' and extract their text content
        aplus_divs = driver.find_elements(By.CLASS_NAME, 'aplus-v2')
        aplus_text = '\n'.join([div.text.strip() for div in aplus_divs])

        # Create the product folder
        product_name = re.sub(r'[^\w\s-]', '', truncated_title).strip()
        product_name = re.sub(r'[-\s]+', '-', product_name)
        product_counter += 1  # Increment the counter
        product_folder_name = f"{product_counter:03d}_{product_name}"  # Format the folder name
        product_folder = os.path.join(output_folder, product_folder_name)
        os.makedirs(product_folder, exist_ok=True)

        # Save the product title to a separate file
        with open(os.path.join(product_folder, "title.txt"), "w", encoding="utf-8") as title_file:
            title_file.write(product_title)

        # Save the price to a separate file
        with open(os.path.join(product_folder, "price.txt"), "w", encoding="utf-8") as price_file:
            price_file.write(f"${price}")

        # Save the additional info and A+ text to a single file
        with open(os.path.join(product_folder, "product_info.txt"), "w", encoding="utf-8") as info_file:
            info_file.write(f"Product title: {product_title}\n")
            info_file.write(f"Price: ${price}\n")
            info_file.write(f"Additional Info: {additional_details_text}\n")
            info_file.write(f"A+ Text: {aplus_text}\n")

        return product_folder
    except Exception as e:
        print(f"An error occurred while scraping the product info: {str(e)}")
        return None

def scrape_amazon_images(product_link, output_folder):
    # Set up the Selenium WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Get the product title, price, additional information, A+ content, and product folder
        product_folder = scrape_amazon_product_info(driver, product_link, output_folder)

        if product_folder is not None:
            # Create an "Images" subfolder within the product folder
            images_folder = os.path.join(product_folder, "Images")
            os.makedirs(images_folder, exist_ok=True)

            # Scroll down to the carousel section
            scroll_script = "arguments[0].scrollIntoView();"
            carousel = driver.find_element("css selector", "ol.a-carousel")
            driver.execute_script(scroll_script, carousel)
            time.sleep(3)  # Wait for the page to load completely

            # Extract data-url for each element in the carousel
            elements = driver.find_elements("css selector", "div._cr-media-carousel_style_media-thumbnail-container__2MRZY[data-url]")
            for i, element in enumerate(elements):
                image_url = element.get_attribute("data-url")
                if image_url:
                    # Download and save the image to the "Images" subfolder
                    response = requests.get(image_url, stream=True)
                    if response.status_code == 200:
                        image_filename = f"image_{i + 1}.jpg"
                        image_path = os.path.join(images_folder, image_filename)
                        with open(image_path, "wb") as image_file:
                            for chunk in response.iter_content(chunk_size=8192):
                                image_file.write(chunk)
                        print(f"Image {image_filename} saved to {images_folder}")
                    else:
                        print(f"Failed to download image {i + 1} from {image_url}")

            print("Product info and images saved successfully.")
    except Exception as e:
        print(f"An error occurred while processing the product: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Read Amazon product links from the "amazon_links.txt" file
    amazon_links_file = r"C:\Users\shaun\Desktop\Marketplace_Scripting\amazon_links.txt"
    with open(amazon_links_file, "r") as file:
        product_links = [line.strip() for line in file.readlines()]

    # Provide the output directory
    output_dir = r"C:\Users\shaun\Desktop\Marketplace_Scripting\chatgpt_website_data"

    # Loop through product links and scrape images and information
    for link in product_links:
        scrape_amazon_images(link, output_dir)
