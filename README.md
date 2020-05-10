# typeracer-bot

A python script that plays Typeracer practice mode automatically

The Typeracer '[Cheating Universe](https://play.typeracer.com/?universe=insane)' sandbox, as announced [here](https://blog.typeracer.com/2017/07/16/typeracer-bans-2500-cheaters-and-spammers-thanks-to-new-moderation-team/), is used in the script. The sandbox is separate to the main site and where anyone is free to test out their cheats / hacks without getting banned.

## Setup

1. Clone the repo and navigate to it
2. Set up a virtual envrionment for project and install dependencies from requirements.txt in an **active venv**
  ```
  python -m venv venv/
  source venv/Scripts/activate
  pip install -r requirements.txt
  ```
3. Download correct version of [ChromeDriver](https://chromedriver.chromium.org/downloads) and put into repo.
   - If not using Chrome, get the WebDriver for your chosen browser and update the line which creates the instance of WebDriver

## Run

1. Execute in IDE / text editor / command line
```
python typeracer-bot.py
```

## Useful Links
- Selenium Docs
  - Selenium (official): [Link](https://www.selenium.dev/documentation/en/)
  - Selenium with Python (unofficial): [Link](https://selenium-python.readthedocs.io/index.html)
    - [Waits](https://selenium-python.readthedocs.io/waits.html)
    - [WebDriver API](https://selenium-python.readthedocs.io/api.html)
- Troubleshooting
  - Evaluate and validate XPath/CSS selectors in Chrome Developer Tools: [Link](https://yizeng.me/2014/03/23/evaluate-and-validate-xpath-css-selectors-in-chrome-developer-tools/)
  - Error Handling in Selenium on Python: [Link](https://www.pingshiuanchua.com/blog/post/error-handling-in-selenium-on-python)
- Virtual Environments
  - The Hitchhiker's Guide to Python - Virtual Envs: [Link](https://docs.python-guide.org/dev/virtualenvs/)
  - A Guide to Python’s Virtual Environments: [Link](https://towardsdatascience.com/virtual-environments-104c62d48c54)