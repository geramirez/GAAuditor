# GA Auditor
A script that collects urls from Cloud Foundry and extracts the version of GA running along with the UA code.

## Installation
##### Install Python requirements
```bash
pip install -r requirements.txt
```
##### Install the Chrome Selenium Driver MAC OS
1. Download the driver from [here](https://code.google.com/p/selenium/wiki/ChromeDriver)
2. Place the ChromeDriver into the `/usr/local/bin` dir

[Video tutorial](https://www.youtube.com/watch?v=XFVXaC41Xac)

## Usage
Set the following env variables
```bash
export CF_URL="18f.gov"
export CF_USERNAME="CF username"
export CF_PASSWORD="CF password"
```

To run
```bash
python Audit.py
```

