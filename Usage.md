# Introduction #

This page describes how to use pysubdownloader.

# Running pysubdownloader #

When you've installed python you can run pysubdownloader by using the following command:
`[python executable] pysubdownloader [options]`

## Command line arguments ##

When you run `[python executable] pysubdownloader -h` the following help text will appear:

```
Usage: pysubdownloader.py [options]

Options:
  -h, --help   show this help message and exit
  -f FOLDER    scan this folder and subfolders
  -l LANGUAGE  language to search subtitles for
```

this should be self explanatory but if the help text does not help you any further:

option: -f
this specifies the folder in which the tv series are located. This folder is scanned (recursive) to find movie files. Pysubdownloader currently finds movie files by looking at the extention of the file: .wmv, .mkv and .avi are considered movie files.

option: -l
this specifies the language in which the subtitles should be searched for. The language is specified according to the [ISO 3166](http://www.iso.org/iso/english_country_names_and_code_elements) list.
It defaults to English. To use Dutch use `-l nl`.

## Results ##

Pysubdownloader will log every attempt to search for a TV show on a specific site:

_date_ _time_ - Podnapisi - DEBUG - Search for serie: _Mythbusters_ Season: _7_ Episode: _2_

This logging will be optional with a command line argument in the future.

When a subtitle is found, it is downloaded, extracted (mostly zip files) and then placed in the same folder as the movie file is located, with the same name as the movie file, but with the .srt extention. Use your favorite movie player to display these subtitles.

## Automating your search ##

Use crontab or a scheduled task in Windows to automate the search of new subtitles.

# Features and limitations #
pysubdownloader is in development stage, so the following limitations apply:

## Sites ##
  1. It currently supports tvsubtitles.net (RSS based) and podnapisi.net (XML based) and Bierdopje (API) as source.
  1. An RSS based site should be checked regularly because the RSS feed shows only new subtitles for any episode. This means that your requested subtitle for any of your episode in your movie folder might not be listed at all! The length of the RSS feed is usually limited, so if you don't want to miss any items, you have to run pysubdownloader regularly. Rule of thumb: inspect the RSS feed, check the first entry, last entry and divide the time by two as a minimum between two searches.
  1. An XML or API based site checks every episode found in the movie folder. If there are multiple results the most recent entry will be downloaded.
  1. Once a subtitle is downloaded, it will not be updated again, because the inspector checks if your movie file already has a subtitle and discards the episode when a subtitle exists.
## Subtitles ##
  1. Only one .srt file per zip file is supported. If there are more files in the zip file, the zip file will be written to the folder where the movie is located as .zip file.
  1. Subtitles for double episodes might not be handled correctly.
## Filenames ##
It doesn't matter what file structure you have, eg. `Serie \ Season \ Episode.avi` or `Serie - Season \ Episode.avi` or `Serie \ Episode.avi` because all subdirs in the folder you specify are looped. However, pysubdownloader only supports the following filename format:

`Serie (Year) - #x## - Description`

or

`Serie - #x## - Description`

or

`Serie (Year) - S##E## - Description`

or

`Serie - S##E## - Description`

When a file doesn't match this pattern, it is ignored.

If you use hellavcr, sabnzbd and newzbin your episodes will be named as mentioned above. This script is designed to complement these programs.

If you have a file structure with proper filenames, you can of course always rewrite lib\FilenameParser.py to match your own filenames. When you do this, you can always drop me a line how you've implemented this and I can add this to the program.
