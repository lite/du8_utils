#!/usr/bin/env python
# coding=utf-8

import unittest
import sys
sys.path.append('./src')

from du8 import Du8Doc

class TestDu8(unittest.TestCase):
    def setUp(self):
        self.doc = Du8Doc()
        self.url = "http://www.du8du8.net/book/8/8592/"

    def test_from_html_with_br(self):
        txt = self.doc.from_html("<p>hello<br/>word</p>")
        assert txt != None, "txt is None."

    def test_from_html_with_comments(self):
        txt = self.doc.from_html("<p>hello <!--this is comments--> word</p>")
        assert txt != None, "txt is None."
        
    def test_get_links(self):
        links = self.doc.get_links(self.url)
        assert links != None, "links is None."
        assert links[0] == u"949276.html", "first link is incorrect."
        assert links[1] == u"954639.html", "second link is incorrect."
        assert links[2] == u"958107.html", "third link is incorrect."
        
    def test_get_content(self):
        title, chapter, content = self.doc.get_content(self.url + "949276.html")
        assert content != None, "content is None."
        assert content.startswith(u"“唔。”"), "content is incorrect."

    def test_get_title(self):
        title, chapter, content = self.doc.get_content(self.url + "954639.html")
        assert title != None, "title is None."
        assert title.startswith(u"武动乾坤"), "title is incorrect."
    
    def test_get_chapter(self):
        title, chapter, content = self.doc.get_content(self.url + "958107.html")
        assert chapter != None, "chapter is None."
        assert chapter.startswith(u"正文 第三章 古怪的石池"), "chapter is incorrect."
        
if __name__=="__main__":
    reload(sys).setdefaultencoding('utf8')
    unittest.main()