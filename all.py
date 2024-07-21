import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import mysql.connector as sql
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

tdate = " "
category=""
#urllink="https://www.google.com/search?q=schools+in+bhimavaram&oq=schools+&gs_lcrp=EgZjaHJvbWUqDggBEEUYJxg7GIAEGIoFMgYIABBFGDkyDggBEEUYJxg7GIAEGIoFMhMIAhAAGIMBGJECGLEDGIAEGIoFMg0IAxAAGJECGIAEGIoFMg0IBBAAGJECGIAEGIoFMg0IBRAAGJECGIAEGIoFMg0IBhAAGJIDGIAEGIoFMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGI8C0gELMTMzMTkyajBqMTWoAgmwAgE&sourceid=chrome&ie=UTF-8"
#urllink="https://www.google.com/search?q=gyms+hyderabad&oq=gyms+&gs_lcrp=EgZjaHJvbWUqDQgCEAAYkgMYgAQYigUyBggAEEUYOTINCAEQABixAxjJAxiABDINCAIQABiSAxiABBiKBTINCAMQABiSAxiABBiKBTIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIKCAgQABixAxiABDIHCAkQABiABNIBCTkyMDVqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8"
driver = webdriver.Chrome()
#hotles
#urllink="https://www.google.com/search?q=hotels+in+hyderabad&sca_esv=d22370baf961194e&sca_upv=1&tbm=lcl&sxsrf=ADLYWIJn5NJpSH1p-5dhNnb74nykIQYLNQ%3A1718955330587&ei=Qi11ZrTKI5qf4-EPwJ-08AU&oq=hot&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIgNob3QqAggAMgQQIxgnMgQQIxgnMgsQABiABBiSAxiKBTILEAAYgAQYkQIYigUyDRAAGIAEGEMYyQMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigVI8lBQ7wNY1DhwA3gAkAEBmAGGAqABwxSqAQYwLjEzLjO4AQPIAQD4AQGYAg2gArIMqAIKwgIFEAAYgATCAggQABgWGAoYHsICBhAAGBYYHsICBxAjGCcY6gLCAgsQABiABBixAxiDAcICDRAAGIAEGLEDGBQYhwLCAggQABiABBixA8ICDhAAGIAEGJECGLEDGIoFwgIKEAAYgAQYyQMYCsICChAAGIAEGLEDGArCAgcQABiABBgKmAMCiAYBkgcFMy44LjKgB-50&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[17.4501494,78.4652933],[17.3964006,78.3570027]];tbs:lrf:!1m4!1u13!2m2!13m1!1b1!1m4!1u7!2m2!7m1!4e1!1m4!1u2!2m2!2m1!1e1!1m4!1u10!2m2!11m1!1e6!1m4!1u10!2m2!11m1!1e4!1m4!1u10!2m2!11m1!1e5!1m4!1u10!2m2!11m1!1e18!1m4!1u10!2m2!11m1!1e9!1m4!1u10!2m2!11m1!1e19!1m4!1u10!2m2!11m1!1e8!1m4!1u10!2m2!11m1!1e10!1m4!1u10!2m2!11m1!1e1!1m4!1u10!2m2!11m1!1e3!1m4!1u10!2m2!11m1!1e7!1m4!1u10!2m2!11m1!1e16!1m4!1u10!2m2!11m1!1e15!1m4!1u10!2m2!11m1!1e21!1m4!1u10!2m2!11m1!1e12!1m4!1u10!2m2!11m1!1e17!1m4!1u4!2m2!4m1!2e1!2m1!1e2!2m7!1e17!4m2!17m1!1e3!4m2!17m1!1e8!3sIAE,lf:1,lf_ui:6"
#Gym
#urllink="https://www.google.com/search?q=gyms+in+hyderabad&sca_esv=317e6ae4902de9ac&tbm=lcl&sxsrf=ADLYWII-zrgjKliTQvarGGK578Z6m7Mwyw%3A1719220062771&ei=Xjd5ZovcLrHd2roP64Sl-As&oq=gyms+in+hy&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIgpneW1zIGluIGh5KgIIADILEAAYgAQYkQIYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIkiZQwwdYhRJwAHgAkAEAmAGYAaAB1QaqAQMwLja4AQPIAQD4AQGYAgagAu0GwgIEECMYJ8ICCBAAGBYYChgewgIGEAAYFhgewgIKEAAYgAQYFBiHApgDAIgGAZIHAzAuNqAH2SU&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[17.4848709,78.45295980000002],[17.4138524,78.34294059999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"

# computer institutes
#urllink="https://www.google.com/search?q=computer+institute+in+hyderabad&sca_esv=d22370baf961194e&sca_upv=1&tbm=lcl&sxsrf=ADLYWILCi4TVXhxd4z9PgaIrTLLMLtAv7A%3A1719219273155&ei=STR5ZumLCeXS2roPh6OH6Aw&oq=computer+in+in+hyderabad&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIhhjb21wdXRlciBpbiBpbiBoeWRlcmFiYWQqAggAMgYQABgHGB4yCBAAGAcYHhgPMggQABgHGAgYHjIIEAAYBxgIGB4yCBAAGAcYCBgeMggQABgHGAgYHjIIEAAYBxgIGB4yCBAAGAcYCBgeMggQABgHGAgYHjIKEAAYBRgHGB4YD0i_OlDcAljuLXAAeACQAQCYAeIBoAHjF6oBBjAuMTUuM7gBA8gBAPgBAZgCDKAC_Q_CAg0QABiABBixAxhDGIoFwgIFEAAYgATCAggQABiABBjnBMICChAAGIAEGBQYhwLCAgIQJsICBhAAGAUYHsICBhAAGAgYHpgDAIgGAZIHBjAuMTEuMaAH-oQB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[17.518639099999998,78.5606073],[17.289676999999998,78.3454794]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
urllink="https://www.google.com/search?q=beauty+parlour+in+hyderabad&tbm=lcl"
#urllink="https://www.google.com/search?q=schools+in+hyderabad&sca_esv=d22370baf961194e&sca_upv=1&tbm=lcl&sxsrf=ADLYWILTavnYO_tuc5913a4H00HCp1tmPg%3A1719221583009&ei=Tz15ZuwZu-Haug_Nir6AAQ&ved=0ahUKEwis_fq99_OGAxW7sFYBHU2FDxAQ4dUDCAk&uact=5&oq=schools+in+hyderabad&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIhRzY2hvb2xzIGluIGh5ZGVyYWJhZDILEAAYgAQYkQIYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGAcYHjIFEAAYgAQyBhAAGAcYHkjCKlCGAljyInAAeACQAQCYAcEBoAHeFqoBBDAuMTm4AQPIAQD4AQGYAgmgAtsKwgINEAAYgAQYsQMYQxiKBcICChAAGIAEGBQYhwLCAgQQIxgnwgICECbCAgcQABiABBgNmAMAiAYBkgcDMC45oAejnQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[17.528886099999998,78.40311650000001],[17.386327299999998,78.3146876]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"

#urllink="https://www.google.com/search?q=Private+Institution+in+hyderabad&sca_esv=d22370baf961194e&sca_upv=1&tbm=lcl&sxsrf=ADLYWILOFkxUD0-xjPvxe9aZTgfMpnfeWw%3A1719341435820&ei=exF7Zo3dMcHE4-EP8bya0A4&ved=0ahUKEwjNhp78tfeGAxVB4jgGHXGeBuoQ4dUDCAk&uact=5&oq=Private+Institution+in+hyderabad&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIiBQcml2YXRlIEluc3RpdHV0aW9uIGluIGh5ZGVyYWJhZDIKECEYoAEYwwQYCkioClDNA1jNA3AAeACQAQCYAaEBoAGjAqoBAzAuMrgBA8gBAPgBAZgCAqACpwLCAggQABiABBiiBJgDAIgGAZIHAzAuMqAHqQY&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[17.583638099999998,78.5553448],[17.1901945,78.33818]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
driver.get(urllink)
time.sleep(1)

elements = driver.find_elements(By.CSS_SELECTOR, ".vwVdIc")



portalid=
memberid=
parentportalid=

# Get the current date
current_date = datetime.date.today()

# Format the date in the desired format
formatted_date = current_date.strftime("%Y-%m-%d")

mydb=sql.connect(
   host="",
    user="",
    password="",
    database="",
    port="")

mycursor = mydb.cursor()


# Click on each element one by one


for element in elements:
    element.click()
    wait= WebDriverWait(driver,100)
    time.sleep(2)
    titl = ""
    mylink = ""
    addr = ""
    phone = ""

    try:
        titl = driver.find_element(By.XPATH,'//h2[@data-attrid="title"]')
        titl = titl.text
        print(titl)

    except NoSuchElementException:
        pass


    try:
        link = driver.find_element(By.CSS_SELECTOR, "a.dHS6jb")
        mylink=link.get_attribute("href")

        if "google" in mylink:
            mylink = ""

        print(mylink)

    except NoSuchElementException:
        pass

    try:
        addr = driver.find_element(By.XPATH,'//span[@class="LrzXr"]')
        addr=addr.text

        print(addr)
    except NoSuchElementException:
        pass


    try:
        phone_num = driver.find_element(By.XPATH,"//span[contains(@aria-label,'Call')]")
        phone=phone_num.text
        phone=phone.replace(" ", "")
        print(phone)

    except NoSuchElementException:
        pass

    sql = "INSERT INTO kf_vendor(VEND_TITL, PORTAL_ID, MEMBERID,PARENTPORTALID,VEND_CON_ADDR, vend_url, phone,VEND_SDATE,VEND_CATEGRY) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
    val = (titl, portalid, memberid, parentportalid, addr, mylink, phone, tdate,category)
    mycursor.execute(sql, val)
    mydb.commit()




num_loops = 50

for i in range(2, num_loops):
    # Form the dynamic aria-label value based on the loop number
    aria_label_value = f'Page {i}'
    try:
        # Find the link element by its aria-label attribute
        link_element = driver.find_element(By.CSS_SELECTOR, f'a[aria-label="{aria_label_value}"]')

        # Click on the link
        link_element.click()
        time.sleep(10)
        elements = driver.find_elements(By.CSS_SELECTOR, ".vwVdIc")
        for element in elements:
            element.click()
            time.sleep(2)
            titl = ""
            mylink = ""
            addr = ""
            phone = ""

            try:

                titl = driver.find_element(By.XPATH,'//h2[@data-attrid="title"]')
                titl = titl.text
                print(titl)

            except NoSuchElementException:
                pass

            try:
                link = driver.find_element(By.CSS_SELECTOR, "a.dHS6jb")
                mylink = link.get_attribute("href")

                if "google" in mylink:
                    mylink = ""

                print(mylink)

            except NoSuchElementException:
                pass

            try:
                addr = driver.find_element(By.XPATH,'//span[@class="LrzXr"]')
                addr = addr.text

                print(addr)
            except NoSuchElementException:
                pass

            try:
                phone_num = driver.find_element(By.XPATH,"//span[contains(@aria-label,'Call')]")
                phone = phone_num.text
                phone = phone.replace(" ", "")
                print(phone)

            except NoSuchElementException:
                pass

            sql = "INSERT INTO kf_vendor(VEND_TITL, PORTAL_ID, MEMBERID,PARENTPORTALID,VEND_CON_ADDR, vend_url, phone,VEND_SDATE,VEND_CATEGRY) VALUES (%s,%s, %s, %s, %s, %s, %s, %s,%s)"
            val = (titl, portalid, memberid, parentportalid, addr, mylink, phone, tdate, category)
            mycursor.execute(sql, val)
            mydb.commit()

    except NoSuchElementException:
        pass
