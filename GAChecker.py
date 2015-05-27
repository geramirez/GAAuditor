import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GAChecker:

    def __init__(self):
        d = DesiredCapabilities.PHANTOMJS
        d['loggingPrefs'] = {'browser': 'ALL'}
        self.browser = webdriver.PhantomJS(desired_capabilities=d)

    def get_url(self, url):
        """ Get URL fron browser """
        self.browser.get(url)
        time.sleep(3)

    def run_checker_script(self):
        """ Runs the GA checker script """
        self.browser.execute_script("""
if (typeof ga === "function") {
    console.log('ga_version: Google Analytics Universal');
    console.log('ga_ua_code: ' + ga.getAll()[0].get('trackingId'));
    console.log('ga_ua_anon: ' + ga.getAll()[0].get('anonymizeIp'));
}
else if (typeof _sendPageview === "function") {
    console.log('ga_version: Google Analytics Legacy');
    console.log('ga_ua_code: ' + oCONFIG.GWT_UAID[0]);
    console.log('ga_ua_anon: ' + oCONFIG.ANONYMIZE_IP);
}
else {
    console.log('ga_version: No Google Analytics');
    console.log('ga_ua_code: No UA Code');
    console.log('ga_ua_anon: No UA Code');

}
        """)

    def clean_message(self, element, message):
        """ Cleans the message log """
        return message.split(element)[-1].replace(' (:)', '').strip(': ')

    def parse_log(self):
        """ Check the log for the GA version """
        data = {}
        for item in self.browser.get_log('browser'):
            message = item.get('message', '')
            if "ga_version:" in message:
                data['ga_version'] = self.clean_message('ga_version', message)
            elif "ga_ua_code:" in message:
                data['ga_ua_code'] = self.clean_message('ga_ua_code', message)
            elif "ga_ua_anon" in message:
                data['ga_ua_anon'] = self.clean_message('ga_ua_anon', message)
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
