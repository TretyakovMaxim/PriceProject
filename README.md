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

![bot image](https://github.com/TretyakovMaxim/PriceProject/blob/priceChecker/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-02-09%2014-35-52.png)

After the release, you will be able to try the bot  [here](https://t.me/PriceCheckerPro_bot)

### Assembly of the repository and local launch.
***
```
git clone https://github.com/TretyakovMaxim/PriceProject.git
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
