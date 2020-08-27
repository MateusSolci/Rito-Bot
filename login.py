import mechanize 
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class Login():

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def configBrowser(self):
        browser = mechanize.Browser()

        # browser.set_handle_equiv(True)
        # browser.set_handle_gzip(False)
        # browser.set_handle_redirect(True)
        # browser.set_handle_referer(True)
        browser.set_handle_robots(False)
        # browser.set_handle_refresh(False)

        cookies = mechanize.CookieJar()
        browser.set_cookiejar(cookies)

        browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206')]
        
        return browser

    def loginSiga(self, site, link, nextPage):
        site.open(link)
        site.select_form(nr=0)
        try:
            site.form["vSIS_USUARIOID"] = self.user
            site.form["vSIS_USUARIOSENHA"] = self.password
            sub = site.submit()
        except:
            print("DEU RUIM")

        response = site.open(sub.geturl())
        parsedResponse = BeautifulSoup(response, "html.parser")

        return parsedResponse