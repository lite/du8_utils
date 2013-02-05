#!/usr/bin/env python
# coding=utf-8

import sys
import time
from du8 import Du8Doc

def usage():
    print("./src/%s <book_url>" %sys.argv[0]); 
    print("\t<book_url> is the book url in du8du8"); 
    print
    print("\texample:")
    print("\t\thttp://www.du8du8.net/book/8/8592/")
    print

if "__main__" == __name__:  
    if len(sys.argv) != 2:  
        usage()  
        sys.exit(1)  
	
    reload(sys).setdefaultencoding('utf8')
    url = sys.argv[1]
    doc = Du8Doc()
    links = doc.get_links(url)
    for link in links:
        print link
        title, chapter, content = doc.get_content(url + link)
        print title, chapter, content
		