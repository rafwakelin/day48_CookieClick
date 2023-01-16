# day48_CookieClick
Website Scrapping with Selenium

This script is using Selenium webdriver and Python to automate clicking on the "cookie" button on the "http://orteil.dashnet.org/experiments/cookie/" website. It also tracks the player's money and periodically checks if they can afford to purchase various upgrades such as a time machine, portal, or alchemy lab. If the player can afford an upgrade, the script will automatically click on the corresponding button to purchase it. The script is set to run an infinite loop, continuously clicking on the "cookie" and checking for upgrades. The script is intended to run indefinitely until it is manually stopped.

It is important to note that there is a time limit set on the script using a variable "five_min" which is set at the end of the file, this will not affect the script execution, this was intended to be used to limit the time of execution but it was not implemented properly. The script also uses some hardcoded xpaths to select the elements on the website.

The script is a proof of concept, it is not recommended to use it on any other website or in any other way, this script is provided as is and the author is not responsible for any damage caused by the usage of this script.
