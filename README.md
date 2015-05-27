# GA Auditor
A script that collects urls from Cloud Foundry and extracts the version of GA running along with the UA code.

## Installation
##### Install Python requirements
```bash
pip install -r requirements.txt
```
##### Install PhantomJS Headless Browser
Mac with brew
```bash
brew install phantomjs
```

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

