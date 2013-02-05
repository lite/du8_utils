du8_utils
===========

    pip install virtualenv
    pip install virtualenvwrapper
    pip freeze > requirements.txt
    pip install -r requirements.txt
    workon du8

Test
====

	nosetests -w . ./test
	nosetests -w . ./test/test_du8.py
	python test/test_du8.py

Thanks
====

+ [nose](https://github.com/nose-devs/nose)
+ [PyYAML](http://pyyaml.org/wiki/PyYAMLDocumentation)
+ [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)
+ [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
+ [html5lib](https://code.google.com/p/html5lib/wiki/UserDocumentation)
