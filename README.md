# is-it-in-stock

Get notified when things you want are in stock! This script can be used to create a more dynamic application to scrape pages dynamically.

The base script works well deployed on a Raspberry Pi.

## Getting Started

Follow the below instructions to get a local environment setup.

### Prerequisites

1. Python 3.10
2. Visual Studio Code

### Setup

1. Clone this repo
2. Create a virtual environment and activate it

```
pip install virtualenv
python3 -m venv .venv
source .env/bin/activate
```

3. Install the required packages

```
pip install -r requirements.txt
```

4. Create a `.env` file and add the values needed

### Development

1. Modify the logic in the results variable to find the data needed
2. Run script

```
python main.py
```

### Deployment

This script can be deployed as a serverless application or a Raspberry Pi can also be a great place to host this script.

1. Setup a Raspberry Pi
2. Follow the [Setup](#setup) and [Development](#development) section
3. Setup a job with crontab to run as frequently as you want

```
> sudo crontab -e

# Add the following entry into the file
0 0 * * * python /path/to/main.py
```
