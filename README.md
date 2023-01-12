# LAB - Class 18

## Project: Caesar Cipher

## Author: Harper Foley

## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/caesar-cipher)

## Setup

* To set up this repo create a local repository on your machine
* Create a virtual environment for Python
  * `python3.11 -m venv .venv`
* Activate the venv file
  * `source .venv/bin/activate`
* Install `pytest`
  * This will allow you to run tests on the program
  * `pip install pytest`
* Install `ntlk` library
  * This will give you access to a number of words used to crach the cipher
  * `pip install ntlk`
* Use `git clone` to clone the repo to your local machine
  * `git clone https://github.com/hfoley2013/caesar-cipher.git`

## How to initialize/run your application

* To start the program, run `python3.11 -m modules.caesar_cipher` in your terminal
* You will then be prompted with options to `encrypt`, `decrypt`, or `crack` a message, or terminate the program
* The program will then ask for your `message`, followed by the number of `shifts` you want in your message
  * *Shifts* refers to how many letter over the program will shift the letters of your message
    * EX: Message: ab, Shift: 2 => Message: cd
* The program will continue to encode and decode your messages until you quit
* In order to `crack` a message, only an encrypted message is required
  * The program will execute a brute force attack on the message and go through all 26 possible shifts of the message and return the most coherent one

## Tests

* How do you run tests?
  * Tests are conducted via `pytest`
  * You may need to specify the location of the tests as follows:
    * `pytest tests/test_caesar_cipher.py`
* Tests check for the following:
  * Shifts ocurred properly on all lowercase words
  * Shifts ocurred properly on all uppercase words
  * Shifts ocurred properly on messages containing a mix of upper and lowercase words with not special characters
  * Shifts ocurred properly on messages containing a mix of upper and lowercase words with special characters
  * Brute force attacks on encrypted words returned the expected decrypted word
  * Brute force attacks on encrypted phrases returned the expected decrypted phrase
  * Nonsense strings of letters returned `''` to the user, since they are meaningless
