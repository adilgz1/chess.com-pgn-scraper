# chess.com-pgn-scraper
this downloads all your games from chess.com in pgn format.

you need to setup selenium for this to work. run 'pip install selenium' in cmd. 
you also need to download chrome driver from https://chromedriver.chromium.org/downloads. extract the folder and put the chromedriver.exe file in the main C drive. you can put it somewhere else too if you'd like and specify the path(plus file name) in line 7 of the code. 


once you've installed selenium and downloaded chromedriver you can run this script anywhere you want. it'll open a chrome window and navigate it itself. it'll visit all the pages and download your games (in separate pgns) for every page.