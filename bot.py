from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
import string
import time
import random
import configparser
config = configparser.ConfigParser()

config.read('config.txt')
proxy_to_use = config.get('settings', 'proxy_')
print(f'proxy: {proxy_to_use}')
emails_used=[]
code_used=[]
done=0
while True:
    try:
        host,port,proxy_user,proxy_password=proxy_to_use.split(':')
        driver=Driver(proxy=f'{proxy_user}:{proxy_password}@{host}:{port}')

        def generate_code(prefix="2921dvcs", random_length=7):
            allowed_chars = string.ascii_lowercase + string.digits  # a-z + 0-9
            random_part = ''.join(random.choices(allowed_chars, k=random_length))
            return prefix + random_part

        survey_code=generate_code()
        print(survey_code)
        if survey_code in code_used:
            driver.quit()
            continue
        def clicker_(xpathe):
            WebDriverWait(driver,9).until(EC.element_to_be_clickable((By.XPATH, xpathe))).click()

        driver.get('https://myzaxbysfeedback.com/')
        code_used.append(survey_code)

        WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, '//input[@name="CN1"]'))).send_keys(survey_code)
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        all_good_optioms=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH, '//form[@id="surveyForm"]//tr')))
        all_opt=len(all_good_optioms)
        i=1
        while i<all_opt:
            i+=1
            clicker_(f'((//form[@id="surveyForm"]//tr)[{str(i)}]//input[@type="radio"])[1]/..')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)
        clicker_('//div[@class="Opt1 rbloption"]//span[@class="radioButtonHolder"]')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        all_good_optioms=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH, '//form[@id="surveyForm"]//tr')))
        all_opt=len(all_good_optioms)
        i=1
        while i<all_opt:
            i+=1
            clicker_(f'((//form[@id="surveyForm"]//tr)[{str(i)}]//input[@type="radio"])[1]/..')

        clicker_('//input[@id="NextButton"]')
        time.sleep(3)
        all_good_optioms=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH, '//form[@id="surveyForm"]//tr')))
        all_opt=len(all_good_optioms)
        i=1
        while i<all_opt:
            i+=1
            clicker_(f'((//form[@id="surveyForm"]//tr)[{str(i)}]//input[@type="radio"])[1]/..')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)
        clicker_('(//form[@id="surveyForm"]//tr//input[@type="radio"]/..)[2]')
        clicker_('//input[@id="NextButton"]')

        time.sleep(3)
        all_good_optioms=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH, '//form[@id="surveyForm"]//tr')))
        all_opt=len(all_good_optioms)
        i=1
        while i<all_opt:
            i+=1
            clicker_(f'((//form[@id="surveyForm"]//tr)[{str(i)}]//input[@type="radio"])[1]/..')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)
        clicker_('//div[@class="Opt1 rbloption"]//span[@class="radioButtonHolder"]')
        clicker_('//input[@id="NextButton"]')

        def load_comments(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    comments = [line.strip() for line in file if line.strip()]
                return comments
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
                return []
            except Exception as e:
                print(f"Error reading file: {e}")
                return []
        comments=load_comments('comments.txt')
        usernames=load_comments('usernames.txt')
        emails=load_comments('emails.txt')

        comment_to_use=random.choice(comments)
        name_to_use=random.choice(usernames)
        email_to_use=random.choice(emails)
        print(comment_to_use)
        print(name_to_use)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//textarea'))).send_keys(comment_to_use)
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        clicker_('(//form[@id="surveyForm"]//tr//input[@type="radio"]/..)[1]')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="textinputwrapper"]//input'))).send_keys(name_to_use)
        comment_to_use=random.choice(comments)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//textarea'))).send_keys(comment_to_use)

        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        clicker_('//div[@class="cataOption"]//label[contains(text(),"None of the above")]/..//span[@class="checkboxholder"]')
        clicker_('//input[@id="NextButton"]')
        time.sleep(3)

        clicker_('//div[@class="cataOption"]//label[contains(text(),"Other")]/..//span[@class="checkboxholder"]')
        time.sleep(2)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="textinputwrapper"]//input'))).send_keys('Fries')
        except:
            pass
        clicker_('//input[@id="NextButton"]')

        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[1]'))).send_keys(email_to_use)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[2]'))).send_keys(email_to_use)
        clicker_('//input[@id="NextButton"]')
        time.sleep(5)
        driver.quit()
        done+=1
        print(f'Reviews Submitted : {done}')
        
    except:
        driver.quit()
        continue