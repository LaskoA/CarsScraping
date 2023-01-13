# Cars scraping
There is a file car.csv with some random card models inside. My idea was to search automatically for those cars in 
Wikipedia, get production years and print them. File regular.py perform synchronous search, fast.py - asynchronous. 
Unfortunately, their speed is equal... 
## Installation

Python3 must be installed

```shell
git clone https://github.com/LaskoA/CarsScraping

cd CarsScraping

Virtual environment install for Windows:
  - python3 -m venv venv
  - source venv/bin/activate
  
Virtual environment install for Mac:
  - sudo pip install virtualenv
  - virtualenv env
  - source env/bin/activate

pip install -r requirements.txt  

Put proper path to Chrome Web Driver on your PC for both files.
```
