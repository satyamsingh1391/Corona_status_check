import requests
import plyer
import datetime
import bs4
from tkinter import  *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
def get_html_data(url):
    data=requests.get()
    return data
def get_corona_detail():
    url = "VISIT THE MHRD"
    html_data=get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')


    ## ACTIVE CASES
    count_Active=bs.find("li",class_="bg-blue").find_all("strong")
    for active in count_Active:
        active.get_text()
    string_Active = bs.find("li", class_="bg-blue").find_all("span")
    for text in string_Active:
        text.get_text()
    active_details=(str(text.get_text())+":"+str(active.get_text()))
    ##DISCHARGED CASES
    count_discharged=bs.find("li",class_="bg-green").find_all("strong")
    for discharge in count_discharged:
        discharge.get_text()
    string_discharged = bs.find("li", class_="bg-green").find_all("span",class_="mob-hide")
    for text1 in string_discharged:
        text1.get_text()

    cured_details=(str(text1.get_text()) + ":" + str(discharge.get_text()))
    ##Deaths
    count_deaths=bs.find("li",class_="bg-red").find_all("strong")
    for deaths in count_deaths:
        deaths.get_text()
    string_deaths=bs.find("li",class_="bg-red").find_all("span")
    for text2 in string_deaths:
        text2.get_text()
    deaths_details=(str(text2.get_text())+":"+deaths.get_text())
    ##MIGRATED
    count_migrated = bs.find("li", class_="bg-orange").find_all("strong")
    for migrated in count_migrated:
        migrated.get_text()
    string_migrated = bs.find("li", class_="bg-orange").find_all("span")
    for text3 in string_migrated:
        text3.get_text()
    migrated_details=(str(text3.get_text()) + ":" + migrated.get_text())
    all_details=active_details+"\n"+cured_details+"\n"+deaths_details+"\n"+migrated_details
    return all_details

print(get_corona_detail())