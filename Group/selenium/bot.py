from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os
import random
import csv


chrome_driver = os.getcwd()+"\\chromedriver.exe"
f = open('results.csv', 'a', encoding='UTF8', newline='')
writer = csv.writer(f)
# writer.writerow(['rating', 'review'])
driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.get('https://www.zomato.com/dublin/bobos-gourmet-burgers-temple-bar/reviews')
# driver.get('https://www.zomato.com/dublin/blue-bar-and-restaurant-skerries/reviews')
driver.get('https://www.zomato.com/dublin/hogs-heifers-swords/reviews')
driver.maximize_window()
num_of_reviews = int(driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/main/div/section[3]/section/section/div/div/div/section/div/div[2]/div[1]').text)
iterations = num_of_reviews//5
review = ""
rating = 0.0
arr = [""]*2
for j in range(1, iterations+1):
  k = 1
  for i in range(1, 6):
    try:
      driver.find_element_by_xpath(
          '/html/body/div[1]/div[2]/main/div/section[4]/div/div/section/div[2]/p['+str(i)+']/span[2]').click()
    except:
      print("")
    finally:
      if(j == 1):
        review = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/main/div/section[4]/div/div/section/div[2]/p['+str(i)+']').text
        print(review)
      else:
        review = driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/div/section[4]/div/div/section/div[2]/p['+str(i)+']').text
        review.replace("\n", " ").strip()
        print(review)
      while True:
        try:
          # print(f'{k} in try')
          if(j == 1):
            rating = float(driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/main/div/section[4]/div/div/section/div[2]/div['+str(k)+']/div/div[1]/div/div/div[1]').text)
          else:
            rating = float(driver.find_element_by_xpath(
                '/html/body/div[1]/div/main/div/section[4]/div/div/section/div[2]/div['+str(k)+']/div/div[1]/div/div/div[1]').text)
          print(f'{rating} stars')
        except NoSuchElementException:
          k += 1
          # print(f'{k} in except')
        else:
          k += 1
          # print(f'{k} in else')
          break
      arr[0] = str(rating)
      arr[1] = review
      writer.writerow(arr)
    sleep(2)
    if(i == 5):
      next = j+1
      print(next)
      sleep(3)
      if(j == 1):
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[2]/div[2]/i').click()
      driver.find_element_by_xpath(
          '/html/body/div[1]/div/main/div/section[4]/div/div/section/div[3]/div[2]/div/a['+str(next)+']/div').click()
      sleep(3)
