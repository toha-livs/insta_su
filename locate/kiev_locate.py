import random
import time


class ParsKievLocate:

    path = '//*[@id="react-root"]/section/main/article/div[2]/div/div[{}]/div[{}]/a'

    def __init__(self, driver):
        self.driver = driver

    def rand_post(self):
        return random.randint(1, 3)

    def scroll_window(self, col=None):
        if col is None:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            for i in range(col):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

    def find_element(self, pathh):
        try:
            element = self.driver.find_element_by_xpath(pathh)
            return element
        except:
            print('ne poshlo zhahozhu v recurs')
            self.scroll_window()
            element = self.find_element(pathh)
            print('wrode vse horosh, nado viberatsia')
            return element

    def run(self, scroll: int):
        print('startuem')
        rows = random.choices(range(1, 14), k=5)
        print(rows, 'rows')
        rows.sort()
        self.scroll_window(col=scroll)
        for row in rows:
            print('nachal for')
            pathh = self.path.format(row, self.rand_post())
            print(pathh)
            elem = self.find_element(pathh)
            if elem is not None:
                elem.click()
                print('nashol element')
                nick = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2').text
                like = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div').text
                print(like)
                self.driver.find_element_by_xpath('/html/body/div[3]/button[1]').click()
            else:
                raise RecursionError


#   //*[@id="react-root"]/section/main/article/div[2]/div/div[24]/div[1]/a
