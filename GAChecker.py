import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GAChecker:

    def __init__(self):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        self.browser = webdriver.Chrome(desired_capabilities=d)

    def get_url(self, url):
        """ Get URL fron browser """
        self.browser.get(url)
        time.sleep(3)

    def run_checker_script(self):
        """ Runs the GA checker script """
        self.browser.execute_script("""
        if (typeof ga === "function") {
            console.log('ga_version: Google Analytics Recent');
            console.log('ga_ua_code: ' + ga.getAll()[0].get('trackingId'));
        }
        else if (typeof _sendPageview === "function") {
            console.log('ga_version: Google Analytics Old');
            console.log('ga_ua_code: ' + oCONFIG.GWT_UAID[0]);
        }
        else {
            console.log('ga_version: No Google Analytics');
            console.log('ga_ua_code: No UA Code');
        }
        """)

    def parse_log(self):
        """ Check the log for the GA version """
        data = {}
        for item in self.browser.get_log('browser'):
            message = item.get('message', '')
            if "ga_version:" in message:
                data['ga_version'] = message.split('ga_version: ')[-1]
            if "ga_ua_code:" in message:
                data['ga_ua_code'] = message.split('ga_ua_code: ')[-1]

        return data

    def check_for_ga(self, url):
        """ Check what version of google analytics this site has """
        self.get_url(url)
        self.run_checker_script()
        return self.parse_log()

    def quit_browser(self):
        """ stops browser """
        self.browser.quit()

if __name__ == "__main__":
    checker = GAChecker()
    print(checker.check_for_ga('https://open.foia.gov'))
    print(checker.check_for_ga('http://iipdigital.usembassy.gov/'))
    print(checker.check_for_ga('http://quotas-db.cf.18f.us'))

    checker.quit_browser()
