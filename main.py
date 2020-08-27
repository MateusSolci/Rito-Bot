import mechanize 
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from login import Login

load_dotenv()

urlLogin = "https://siga.cps.sp.gov.br/aluno/login.aspx"
pageInicial = "https://siga.cps.sp.gov.br/aluno/home.aspx"

USER = os.environ.get('user')
PASSWORD = os.environ.get('password')

def main():
    site = Login(USER, PASSWORD).configBrowser()
    responseLogin = Login(USER, PASSWORD).loginSiga(site, urlLogin, pageInicial)

    print(responseLogin)


if __name__ == "__main__":
    main()