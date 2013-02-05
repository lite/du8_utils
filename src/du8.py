#!/usr/bin/env python
# coding=utf-8

import string,re
from mechanize import Browser
from bs4 import BeautifulSoup

class Du8Doc:

    def __init__(self):
        self.br = Browser()
        
    def from_html(self, html):
        text = re.sub("<.+>\n", "", html)
        text = re.sub("</.+>\n", "", text)
        text = re.sub('(<br/?>\s*)+', '\n', text)
        text = re.sub('&nbsp;', ' ', text)
        return text

    def get_links(self, url):
        res = self.br.open(url)
        data = res.get_data() 
        soup = BeautifulSoup(data, "html5lib")
        div_content = soup.find('table')
        urls = div_content.find_all("a")
        return [url.get('href') for url in urls ]        
        
    def get_content(self, link):
        res = self.br.open(link)
        data = res.get_data() 
        soup = BeautifulSoup(data, "html5lib")
        title, chapter = soup.html.title.string.split("-")[0:2]
        div_content = soup.find(id="content").prettify()
        content = self.from_html(div_content)
        return title, chapter, content
