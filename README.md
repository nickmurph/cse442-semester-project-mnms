# A stock trading dashboard written in Python, the semester long group project for CSE442: Software Engineering 
Our 4-developer team used industry standard collaborative methods such as Agile sprinting, user stories, a Kanban board, issue tracking and frequent deployments. 
CSE442: Software Engineering focused specifically on these tools for working as part of a modern software development team.

Technologies used: Python, Kivy GUI framework, CSV, Kanban, Yahoo! Stocks API

Features:
- Stock charts generated for multiple timeframes (1 day, 1 month, 6 months, 1 year, 5 years, Maximum) with buttons to let the user switch between them
- Live price of the stock updated periodically during trading hours
- For each stock queried, user dashboard displays financial metrics: Market Cap, Dividend Rate, 52 Week High/Low, Trailing P/E, Trailing EPS, Beta, and Earnings Growth
- User clicking on any of the financial metrics mentioned brings up a pop-up box with a brief explanation of the metric and how it's useful to a trader
- Beneath the financial metrics are three recent news stories featuring the stock/company that can be clicked for the full article (external browser triggered)
- to the right of the stock chart is a more in-depth finance/accounting sheet with data reported by the company as of the last quarterly earnings report
- Users can use the toolbar in the top-right to quickly enter a valid ticker symbol and load that stock
- If the ticker symbol isn't known, a searching system is provided that allows users to enter partial tickers or company names
- Watchlist function, where users can add stocks to their watchlist and then view those in a separate tab
- Skeleton GUI/logic for a portfolio that tracks the user's stocks (ticker, # of shares, value, etc). Beyond the scope of the sprints allocated in CSE442
- Skeleton GUI/logic for user profiles, including logging in and out, username, etc. Also beyond the scope of the sprints allocated in CSE442




To install and run our project here are the steps required:
1. Copy/clone the contents of this repository
2. Run the GUIwithkv.py file
3. It will open up MnMs Financial Tool App
4. Please note CSE442 students were graded on their ability to use modern collaboration tools to set complex goals and meet them in allocated sprints, not on the aesthetic beauty of their python desktop app :)
