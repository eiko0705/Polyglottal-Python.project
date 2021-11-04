This was created during my time as a student at Code Chrysalis.
# New News App 📰
1. [About](#About)
2. [Getting Started](#Getting%20Started)
3. [Tech Stack](#Tech%20Stack)

# About 💁‍♀️
If you use this App, you can easily check the latest news of "The Japan Times" even when you are busy.  
The App summarize the news in only 3 lines for you! And also if you were not good at English, it translates the summary into Japanese (currently it's a little weird translation, though).

# Getting Started 👊
Follow this guide to set up your environment.
To clone and run this application, you'll need Python3, and pip installed on your computer.

## 1. Framework
To run this code, you need to install flamework for python.  
```
pip install flask
```

## 2. Scraping
To scrape the news data, you need to install a library "BeautifulSoup".
```
pip install beautifulsoup4
```

## 3. Summarize
To summarize the news, you need to install a library "sumy".
```
pip install sumy
```

## 4. Tranlate
To translate the summary, you need to install a library "googletrans". 
(It seems that googletrans is unstable and some people (depending on the country) may get an error, so I used the latest version this time even though it's alpha one.)
```
pip install googletrans==4.0.0-rc1
```

## 5. Inplement
Now run the code and see the app in your browser localhost:8000!
```
python flask_app.py
```

# Tech Stack 🤖
I used 



