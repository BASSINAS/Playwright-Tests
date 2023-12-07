from typing import Any
import pytest
import re
from playwright.sync_api import Page, expect


class Application(Page):

    def __init__(self):
        self.page_accueil = Page()
        
        
    def loadpage(self):
        self.page_accueil.goto("https://google.com")  


def test_loadpage():
    application = Application()
    application.loadpage() 
    expect(application.get_by_role('button', name='Recherche Google ')).to_be_visible



    
           

    