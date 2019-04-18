import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from locate.kiev_locate import ParsKievLocate


def do_with_except(d, path, text=None, click=None):
    try:
        elem = d.find_element_by_xpath(path)
    except ElementNotInteractableException:
        return True
    if text:
        write_text(d, path, text)
    if click:
        elem.click()
    return False


def write_text(driver, path, text, subm=None):
    elem = driver.find_element_by_xpath(path)
    elem.send_keys(text)
    if subm:
        elem.submit()


# with webdriver.Chrome(ChromeDriverManager().install()) as d:
d = webdriver.Chrome(ChromeDriverManager().install())
d.implicitly_wait(10)
d.get('https://instagram.com')
d.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
write_text(d, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input[1]', 'livanskee')
write_text(d, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/div[1]/input[1]', 'tohalivs')
d.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
if do_with_except(d, '/html/body/div[3]/div/div/div[3]/button[2]', click=True):
    print('can\'t find')
write_text(d, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input', 'Kyiv, Ukraine')
d.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
pars = ParsKievLocate(d)
print('pars good start')
pars.run(4)
print('pars finish')
time.sleep(15)

