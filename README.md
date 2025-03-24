# Telegram Connection Monitor Bot

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot_API-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A real-time network monitoring bot that tracks ESTABLISHED connections on port 9192 and sends Telegram notifications for connection events.

## Features

- Real-time monitoring of port 9192 connections
- Instant Telegram notifications for:
  - New connections
  - Connection terminations
  - Fast connections (<1 minute)
- Connection duration tracking
- Proxy support
- Persian language notifications (fully customizable)

## Prerequisites

- Python 3.6+
- Windows OS (uses Windows-specific commands)
- Telegram Bot Token
- (Optional) Proxy credentials if behind corporate firewall

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-connection-monitor.git
cd telegram-connection-monitor
```

2. Install required packages:
```bash
pip install python-telegram-bot
```

3. Create a config.py file with your credentials:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CID = "YOUR_CHAT_ID"

# Proxy configuration (if needed)
P_URL = "http://your.proxy.url:port"
P_USER = "proxy_username"
P_PASS = "proxy_password"
```

Usage
Run the monitoring script:

```bash
python bot.py
```


The bot will:
1. Send a startup notification
2. Continuously monitor port 9192 connections
3. Send notifications for all connection events



