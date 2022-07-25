#!/usr/bin/env python3

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def download(url):
    driver = webdriver.Chrome()
    urlp = "https://doi.org/" + url
    print(urlp)
    driver.get(urlp)
    elem_pdf = driver.find_element(By.CSS_SELECTOR, "a[aria-label='PDF']")
    elem_pdf.click()
    time.sleep(3)
    elem_download = driver.find_element(By.CSS_SELECTOR, ".navbar-download")
    elem_download.click();
    time.sleep(3)
for line in sys.stdin:
    download(line.rstrip())
