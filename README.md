# Assignments
This repository contains four modules that serve different purposes:
## 1. Weather Data Processing and Reporting

This Python script processes weather data from CSV files and generates annual reports on temperature and humidity.

    1. Annual Max/Min Temp: Print a table like formatted output as follows

        Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity
        --------------------------------------------------------------------------
        1996        40              2               94                  20
        1997        40              1               86                  10
        1998        40              3               80                  30
        

    2. Hottest days of each year
    Year        Date          Temp
    ------------------------------
    2006        21/6/2006     45
    2007        21/6/2007     47
    2008        21/6/2008     46
    2009        21/6/2009     43
## Introduction

This script processes weather data stored in CSV files and provides two types of annual reports:
1. **Annual Max/Min Temperature and Humidity Report**: Displays maximum and minimum temperatures and humidities for each year.
2. **Hottest Days Report**: Lists the hottest days along with their temperatures for each year.

The script uses Python's `defaultdict` and `namedtuple` for efficient data processing and reporting.

## Usage

To generate the weather reports, run the script using the following     command:

```bash
python weather_man.py report_number weather_data_dir
```

Program should take two parameters: report number and weather data directory. If no parameter is provided print the application usage info. According to above reports a usage output could be like

```bash
    Usage: weatherman [report#] [data_dir]

    [Report #]
    1 for Annual Max/Min Temperature
    2 for Hottest day of each year

    [data_dir]
    Directory containing weather data files
```

## 2. Word Frequency Counter

This Python script reads a text file, calculates the frequency of each word, and displays the words along with their frequencies in a formatted table.


## Introduction

This script provides a convenient way to analyze the word frequency distribution in a text file. It preprocesses the text data, removes special characters, and counts the occurrences of each word. The script is especially useful for tasks such as understanding the most common words in a document or checking for specific keywords.

## Usage

To use this script, follow the instructions below.

Execute the code using python.Run the file main.py on your python terminal

Word frequency counter takes a file input and process the file to output frequency of each word in the file.

Run module in python terminal

Keep  your text file in the same directory as the module

Input file name as an argument to the module

```bash
    Usage: main.py [file.txt]

```
## 3. Scrapy project for E-Commerce website
This is a scrapy application with spiders to automate searching from an e-commerce website.

## Introduction
This project includes Scrapy spiders designed to scrape product information from the www.paklap.pk website. The spiders are tailored to extract details about laptops and AirPods products.

Both the spiders are designed to scrape information about the specific product available on the website. It starts by navigating to the category page and then follows pagination links to scrape information from multiple pages.

## Spiders included:

* laptop_spider
* airpod_spider


## Usage:

```
$ cd myscrapper
$ pip install -r requirements.txt
$ scrapy crawl <spider-name> -o output.csv
```
## 4. Django Rest Framework
This module contains the code for developing custom APIs for an e-commerce database using Django Rest Framework. The purpose of this branch, named `api_customization`, is to focus on creating, customizing, and enhancing APIs that drive the functionality of our e-commerce database.

## Usage


In this project, we use `local_template.py` as a template for environment-specific settings. Here's how it works:

1. **Environment Configuration**: The project uses different configurations for different environments, such as development, production, and testing.

2. **Template File**: `local_template.py` serves as a template for environment-specific settings. It includes placeholder values for settings like `DEBUG`, database configurations, and secret keys.

3. **Creating Environment-Specific Files**: To configure your project for a specific environment, create an environment-specific settings file (e.g., `local.py` for local development) based on the `local_template.py` template.

## APIs

The following APIs have been implemented

### User Registration
Endpoint: /api/auth/register/

    Method: POST
    Description: Register a new user.
    Parameters:
        first name: User's first name
        last name: User's last name
        email: User's email address
        password: User's chosen password

### User Login
Endpoint: /api/auth/login/

    Method: POST
    Description: Authenticate a user and get an access token.
    Parameters:
        email: User's email address
        password: User's password

### Product List
Endpoint: /api/products/

    Method: GET
    Description: Retrieve a list of all available products.

### Product Search
Endpoint: /api/products/?color=white&brand=hp

    Method: GET
    Description: Search for products based on a query.
    Parameters:
        color: Filter products by color (optional).
        brand: Filter products by brand (optional).        

### Product Detail
To interact with products using this API, please use valid product IDs within the range of 132 to 265.

Endpoint: /api/products/<int:product_id>/

    Method: GET
    Description: Retrieve detailed information about a specific product.
    Parameters:  
        product_id: Product ID

### User Wishlist

Endpoint: /api/wishlist/

    Method: GET
    Description: Retrieve the wishlist of the owner.
  
### Add to Wishlist

Endpoint: /api/wishlist/

    Method: POST
    Description: Add a product to the wishlist.
    Body : 
        {
            "product_id": <product_id>
        }

### Remove from Wishlist 

Endpoint: /api/wishlist/

    Method: DELETE
    Description: Remove a product from the wishlist.
    Body : 
        {
            "product_id": <product_id>
        }

