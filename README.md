# Product Market Research Automation with Amazon Scraper

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![AWS Rekognition](https://img.shields.io/badge/AWS%20Rekognition-Ready-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This repository contains a suite of Python scripts designed to automate product market research. Leveraging web scraping techniques, these scripts empower e-commerce entrepreneurs with comprehensive insights into product pricing, details, and images sourced from Amazon. By seamlessly integrating into your workflow, these tools eliminate the tedious manual tasks associated with product research, allowing you to focus on strategic decisions to optimize your store's offerings.

---

## Key Components

### 1. `scrape_amazon_product_info.py`

This script is the heart of the operation, responsible for scraping essential product information from Amazon product pages. It utilizes the Selenium library to navigate through product listings, extract data such as title, price, and additional details, and save them to individual text files. The extracted data serves as the foundation for informed decision-making in product selection and pricing strategies.

### 2. `scrape_amazon_images.py`

Complementing the product information scraper, this script specializes in harvesting product images from Amazon listings. It employs web scraping techniques to locate and download images associated with each product, providing visual assets crucial for enhancing product listings on your Shopify store. With high-quality images at your disposal, you can create compelling product pages that captivate potential customers and drive conversions.

### 3. `helper_functions.py`

A collection of utility functions essential for enhancing the robustness and functionality of the scraping process. From handling errors gracefully to truncating text for concise presentation, these helper functions streamline the data extraction pipeline, ensuring smooth execution even in the face of dynamic webpage structures.

---

## How It Works

1. **Data Acquisition**: The `scrape_amazon_product_info.py` script initializes a Selenium WebDriver and navigates to the provided Amazon product links. Through meticulous DOM traversal, it locates and extracts pertinent product information, including title, price, and additional details. The data is then saved to structured text files within dedicated product folders.

2. **Image Scraping**: In parallel, the `scrape_amazon_images.py` script taps into the visual dimension of product research by retrieving product images from Amazon listings. Employing requests and DOM manipulation, it downloads and organizes images into an "Images" subfolder within each product directory, enriching the dataset with compelling visual assets.

---

## Usage

1. **Input Data**: Populate the `amazon_links.txt` file with Amazon product links, ensuring each link is on a separate line.

2. **Configuration**: Customize output directories and adjust scraping parameters as needed within the scripts.

3. **Execution**: Run the scripts individually or integrate them into your workflow to kickstart your product market research journey.

---

## Conclusion

With these sophisticated tools at your disposal, navigating the competitive landscape of e-commerce has never been easier. Harness the power of automation to elevate your store's product offerings, streamline your decision-making processes, and unlock new avenues for growth and profitability.

---

*Disclaimer: This repository is intended for educational and research purposes only. Please adhere to Amazon's Terms of Service and respect intellectual property rights when utilizing data scraped from their platform.*
