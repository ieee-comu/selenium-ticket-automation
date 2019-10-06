## Selenium Ticket Automation Project

### Preview


## Introduction

This project checks whether the ticket purchase system works on [Onur Air](https://www.onurair.com/en/)'s website. This test is only set to run until the time of payment.

## Prerequisites

On Ubuntu 18.04:

**Python 2.7, 3.4+**

**python-pip, python3-pip**
<pre>
  $ sudo apt install python-pip
  $ sudo apt install python3-pip
</pre>

**geckodriver**

* [download](https://github.com/mozilla/geckodriver/releases) geckodriver then run the following command:

<pre>
  $ tar -xf geckodriver-v0.24.0-linux64.tar.gz (depending on your OS/distribution)
</pre>

* move `geckodriver` file to /usr/local/bin/
<pre>
  $ sudo mv ./geckodriver /usr/local/bin/
</pre>

**selenium 3.141+**
* download as root
<pre>
  $ sudo -i
</pre>
* install
<pre>
  pip install selenium
</pre>

* If you are on `PyCharm`, follow these steps:

`ctrl`+`alt`+`s`(settings) > `Project` > `Project Interpreter` > click `+` > search `selenium` > `install package`

* move selenium packages
<pre>
  $ cp -r /home/user/.local/lib/python2.7/site-packages/selenium* /usr/local/lib/python3.6/dist-packages
</pre>

## Installation

<pre>
  $ git clone https://github.com/ieee-comu/selenium-ticket-automation.git
  $ cd ./selenium-ticket-automation
</pre>
* run
<pre>
  $ python3 ticket-test.py
</pre>

## License
* [GNU General Public License v3.0](https://github.com/ieee-comu/selenium-ticket-automation/blob/master/LICENSE)
