import os
import time
from selenium import webdriver

def scrape_amazon_image_links(product_link, output_filename):
    # Set up the Selenium WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the product page
        driver.get(product_link)

        # Scroll down to the carousel section
        scroll_script = "arguments[0].scrollIntoView();"
        carousel = driver.find_element("css selector", "ol.a-carousel")
        driver.execute_script(scroll_script, carousel)
        time.sleep(3)  # Wait for the page to load completely

        # Extract data-url for each element in the carousel
        image_links = []
        elements = driver.find_elements("css selector", "div._cr-media-carousel_style_media-thumbnail-container__2MRZY[data-url]")
        for element in elements:
            image_url = element.get_attribute("data-url")
            image_links.append(image_url)
            print(f"Extracted image URL: {image_url}")

        # Save image links to the text file
        with open(output_filename, "w") as file:
            for link in image_links:
                file.write(link + "\n")

        print("Image links saved successfully.")

    finally:
        # Close the WebDriver
        driver.quit()

# Provide the Amazon product link and output file path
product_link = "https://www.amazon.ca/Ceiling-Compatible-Dimmable-Profile-Installation/dp/B07WY3VM1M/ref=pd_bxgy_img_sccl_2/131-1334241-0828667?pd_rd_w=cFvl9&content-id=amzn1.sym.93ae3f3f-3555-4971-a952-df8053b1d375&pf_rd_p=93ae3f3f-3555-4971-a952-df8053b1d375&pf_rd_r=PF2EVN9YA8X2JJ1YCYZW&pd_rd_wg=8XQV1&pd_rd_r=3bd6d0c1-aefa-48db-8df0-014e1d19e70d&pd_rd_i=B07WY3VM1M&th=1"
output_dir = r"C:\Users\shaun\Desktop\Marketplace_Scripting"
output_filename = os.path.join(output_dir, "amazon_image_links.txt")

# Call the scraping method
scrape_amazon_image_links(product_link, output_filename)
