CS50x End Project
Family Photos

For my end project I made a Python app that runs on Flask and makes use of the OpenCV Library.

This idea came from a need as I have thousands of old photos which were not scanned but photographed on a wooden background and I would like to auto-detect and crop them. The web version was made for demonstration purposes but the real use-case is as a command-line tool for faster execution and automation.

I used Flask, HTML, CSS and a little bit of Javascript for the front and python for the different back end functions.
These functions include loading and saving images, applying OpenCV image functions, checking the filename of the files obtained from the website.

I intend to build upon this project with the following goals in mind:

- improve accuracy of the tool
- have some sort of average of the different results of different methods to find edges 
- or an automatic selection of the best result
- integrate Google Cloud Vision API in addition to OpenCV visual tools
- eventually work in 2-pass for better results
- detect multiple objects in a single picture while maintaining accuracy

The webapp is hosted at https://dorskfr.pythonanywhere.com/

Youtube demo at https://www.youtube.com/watch?v=hSDUzDyC5UU
