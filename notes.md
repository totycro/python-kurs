# Boku Python Kurs


## Plan pandas, etc

gute pandas infos (in ./downloaded-blog-posts):  
https://towardsdatascience.com/data-preprocessing-with-python-pandas-part-3-normalisation-5b5392d27673

scikit learn: iris clustering example:
https://jakevdp.github.io/PythonDataScienceHandbook/05.02-introducing-scikit-learn.html



## Plan 2020 / 2021
* testing / git (fix einbauen!)
* datetime (auch durchmachen, ist nicht so lange)
* file / path handling (pathlib, file operations)
* error handling (exceptions)
* linear programming
* pip (requirements.txt, venv, conda, conda env)
* openpyxl durchgehen
  https://towardsdatascience.com/automate-excel-reporting-with-python-233dd61fb0f2
  example: report files for every month, then add formula in every file
  https://towardsdatascience.com/automate-these-3-boring-excel-tasks-with-python-666b4ded101b
* schedule ( code-examples/my_schedule.py )
  cron: jeden tag um 9 arbeiten -> schedule https://pypi.org/project/schedule/
* mail ( code-examples/mail.py )  
* linear programming: beispiel von tutorial durchgehen
* regular expressions (find, substitute)
* OOP: classes, data hiding, inheritance, polymorphism
* IDEs: linting, type checking, completion, documentation
* SQL: Datenbank und Abfragen (sqlite?)
* Webserver programmieren
* advanced python features:
  * type annotations
  * with statement
  * decorators
  * generator expression
  * magic methods, __iter__
  * generators
  * coroutinges
* multiprocessing, dask


* geopandas lightning talk https://gist.github.com/jorisvandenbossche/7b30ed43366a85af8626
* GIS ganze lecture: https://automating-gis-processes.github.io/CSC18/#


### ferner
 * [DONE] excel sheet parsen und stats
 * [DONE (außer openpyxl] grafiken -> matplotlib, openpyxl in excel
 * jupyter notebooks
   * erstes notebook: https://github.com/inwe-boku/lecture-scientific-computing/blob/master/lecture03-python-introduction/lecture03.ipynb
   * public toilets: https://github.com/inwe-boku/lecture-scientific-computing/blob/master/lecture04-python-scientific-ecosystem/lecture04.ipynb
 * project euler? (see recap)

## Kurs Inhalt
* Pandas/mypy
* jupyter
* testing
* git
* file handing, shutil
* openpyxl  
  https://realpython.com/openpyxl-excel-spreadsheets-python/  
  automate the boring stuff
* numpy  
  https://jakevdp.github.io/PythonDataScienceHandbook/index.html  
  https://numpy.org/devdocs/user/quickstart.html  

<!--
## Inputs Richard
* programmieren (schleifen, datentypen, listen, dictionary)
* datenauswertung excel / R -> grafik
* simulationsprozesse
* heuristiken

- gibt folien von extra LVA die Richard macht
- Konkrete beispiele in Excel, R

-->

## Mein Vorschlag Format

* etwas frontal, dann aber auch Fokus auf selber programmieren
* Studi-Abgabe bzw. Musterlösung besprechen
* Studi-Lösungen verbessern / optimieren
* etwas live coding


## TODO

<!--
* xkcd python
* import antigravity -> import webbrowser
* debugger kurz vorzeigen
* help(log) für optional argument
* help(math) geht nur nach import math
* math.cos: immer diese variante, kein "import *"
* python erklären: sprache VS interpreter VS thonny
* hint: aufgabe replace: nur 1 zeile
* analysemodus von thonny einbauen
* suche bei google: python how do i (stackoverflow)
-->




## Inhalte

Wichtig zum einbauen:
* git
* testing

#### Python

Überblick über Einführungen für "Non-Programmers" (Englisch): https://wiki.python.org/moin/BeginnersGuide/NonProgrammers
Python guru (Englisch): https://thepythonguru.com/
Python basics (Englisch): https://pythonbasics.org/
Computer Science Circles (Viele gut dokumentierte Übungen): https://cscircles.cemc.uwaterloo.ca/4-types/
Detaillierter Kurs: https://www.python-kurs.eu/
Offizielle Python-Einführung (Englisch) (vor allem Kapitel 3-5): https://docs.python.org/3/tutorial/index.html  

Schneller Walkthrough: https://tutorial.djangogirls.org/de/python_introduction/  
Anfängertutorial mit Online-Interpreter: https://www.learnpython.org/en/Welcome https://www.w3schools.com/python/  

Python for you and me (Englisch, buch): https://pymbook.readthedocs.io

PythonTutor Visualizer (Englisch): http://pythontutor.com/visualize.html


exercises: https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

automate the boring stuff

Print-Bücher kann ich bei bedarf raussuchen

Üben ist zentral, nicht nur lesen, auch am besten an eigenen Beispielen ausprobieren

* Geschichte von Python, Eigenschaften der Sprache (Wikipedia kurz)
* python 3!
* repl
    * mathematische ausdrücke (komplizierteres eher später)
* Primitive Datentypen + operationen
* variablen, assignment
* naming
* if else
* kommentare
* Listen, Tupel, Map (keine Sets)
    * len
* Funktionen
* Daten import/export
* Einfache Datenanalysen
* plots
* jupyter notebooks -> plots!
* numpy?

#### "Echte" Anwendungen
* plots
* auswertungen
* emails?

