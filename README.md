# Price Checker
***

___Price Checker___ - this is a Telegram bot for searching mobile 
phones at competitive prices.  

The user enters the model and brand 
of the phone they need and receives a keyboard in response, where 
they can choose the characteristics: color and memory capacity. 
By selecting the desired device from the models listed and clicking 
on the corresponding keyboard button, the user receives a link to 
a website where the price for that model is lower.

![bot image](venv/фото бота.jpg)

After the release, you will be able to try the bot  [here](https://t.me/PriceCheckerPro_bot)

### Assembly of the repository and local launch.
***
```
git clone https://
pip install -r requirments.txt
```
### Configuration.
***
In the Price_Checker_bot.py file:
```python
BOT = Bot ('Your API key obtained from BotFather')
```
### Populating the database:
Run the parser from the qTechno directory:
```python
scrapy crawl q_techno
```
Run the parser from the rozetka_parser directory:
```python
scrapy crawl rozetka
```
### Parsers on schedule.
The project has shell scripts that run the parsers at certain time 
intervals. These scripts automate the data parsing process, 
simplifying the control of important information.
### Usage
Each shell script is responsible for launching a specific parser 
at a specified interval. To use the parser, simply add the 
corresponding script to the system's task scheduler, such as cron.
### sh Files
* q-techno.sh: This script launches the q_techno parser.
* rozetks.sh: This script launches the rozetka parser.  
These files will be used to schedule the parsers using a task 
scheduler (such as cron).
### Launch
To launch the bot, execute in the root of the project:
```python
python3 Price_Checker_bot.py
```
### Notes
If you have noticed any issues or bugs in the script operation, 
please report them in the "Issues" section in the GitHub repository.
