# Introduction #

On this page, I'll explain how to setup your Python libraries in order to use this script.


# Requirements #

This script is designed to work on every OS. I have tested it so far on Windows, but I'm planning on using it on my Synology DS207+ NAS with optware installed. So this script should work on every platform that has a Python interpreter and all required libraries.

  1. Fist of all, you need Python 2.5, which you can download on the [Python official site](http://python.org/download/releases/2.5.4/) or install using your package manager.
  1. When Python is installed, you have to install some required libraries:

  * [libxml2](http://xmlsoft.org/downloads.html) and [libxslt](http://xmlsoft.org/XSLT/downloads.html) are required for lxml (see installation instructions below).
  * [lxml](http://codespeak.net/lxml/installation.html) is required to parse HTML documents
> > Install setuptools and run `easy_install lxml`.
  * [Universal Feed Parser](http://www.feedparser.org/) is required to parse RSS feeds.
  * [Spring Python](http://www.springsource.org/extensions/se-springpython-py) is required as the application uses Spring Python internally to create objects.

# Installation #

## Linux ##
Use your favorite package manager to install: libxml2, libxslt, python2.5.
Make sure you have gcc installed.

I have tested these instructions on my DiskStation NAS with optware installed. I use the following package feed:

Install these packages in the following order:
  1. python2.5: Self-explanatory
  1. py25-setuptools: This will install easy\_install, required for installing lxml
  1. libxml2, libxsl: These packages are required for lxml
  1. py25-lxml: Bindings for libxml2 and libxslt with python2.5. If you don't install this package, lxml will not build.
  1. easy\_install lxml: This will install lxml, required for processing HTML pages.
  1. py25-feedparser: This will install the universal feed parser for processing RSS feeds.
  1. download Spring python from the link above or install using easy\_install springpython

When you're done, you're ready to use pysubdownloader.

## Windows ##
Install the binary versions in this order:
  1. python2.5, see python.org
  1. [libxml2](http://xmlsoft.org/sources/win32/python/libxml2-python-2.7.3.win32-py2.5.exe),
  1. [setuptools](http://pypi.python.org/packages/2.5/s/setuptools/setuptools-0.6c9.win32-py2.5.exe#md5=602d06054ec1165e995ae54ac30884d7),
  1. lxml (run `easy_install lxml` from the Scripts folder in your Python installation dir),
  1. use `easy_install feedparser` or download source of Universal Feed Parser and run `setup.py install`
  1. download Spring python from the link above or install using easy\_install springpython

When you're done, you're ready to use pysubdownloader.

# Configuration #

In order to use the site Bierdopje, you have to obtain an API key.
When obtained, place the API key in the app-config.yml file.

```
    - object: bierdopjeApi
      class: sites.components.search.api.bierdopje.BierdopjeAPI
      scope: singleton
      properties:
        urlHandler: {ref: urlHandler}
      constructor-args:
        apiurl: http://api.bierdopje.com/
        # Place your own API key:
        apikey: <INSERT KEY>
```

To enable or disable certain sites, modify app-config.yml:

```
    - object: enabledsites
      list:
        - podnapisi
        - tvsubtitles
        - bierdopje
```

The order of these sites can be changed, this will be reflected in the run of the sites.
When a site is commented out (using #) it will not be searched.

The script will search only for newly added files, based on the last modification date. A specified number of days must be between the last modification date and the system time. This parameter can be edited in the configuration files:

```
    - object: maxdays
      int: 10
```

The default is 10, so when a subtitle isn't found for 10 days after the last modification date, the episode will be skipped.