## Selenium Ticket Automation Project

## Introduction

This project checks whether the ticket purchase system works on Onur Air's website

## Prerequisites
* Python 2.7, 3.4+
* python-pip, python3-pip
<pre>
  $ sudo apt install python-pip
  $ sudo apt install python3-pip
</pre>

## Installation

On Ubuntu 18.04:

**geckodriver**

* [download](https://github.com/mozilla/geckodriver/releases) geckodriver then run the following command:

<pre>
  $ tar -xf geckodriver-v0.24.0-linux64.tar.gz (depending on your OS)
</pre>

* move geckodriver file to /usr/local/bin/
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
