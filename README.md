# Monitor

A lightweight Linux monitoring and operations agent built for personal servers, remote systems, and home lab environments.

Monitor delivers alerts through Telegram and provides an interactive bot interface for querying server health from anywhere.

---

# Why I Built This

After setting up a remotely accessible Linux machine using SSH and Tailscale, I realized I had a new problem:

**How would I know if something went wrong?**

Questions I wanted answered included:

* Is the machine still online?
* Are important services running?
* Is disk usage becoming a problem?
* Is memory usage becoming excessive?
* Has the machine restarted?

Rather than relying on manually checking the system, I decided to build a lightweight monitoring agent.

Monitor is the result.

---

# Features

## Service Monitoring

Monitor checks the health of configured services.

Examples:

* ssh
* tailscaled
* custom services

## Disk Monitoring

Monitor checks disk utilization and generates alerts when configured thresholds are exceeded.

## Memory Monitoring

Monitor checks memory usage and reports when usage exceeds configured limits.

## Telegram Notifications

Alerts can be delivered directly to Telegram.

Examples:

* Service failures
* Daily health reports
* Boot notifications

## Daily Health Reports

A scheduled summary can be sent containing:

* Disk usage
* Memory usage
* Service status
* System health information

## Boot Notifications

Receive a Telegram message whenever the monitored machine starts.

Useful for:

* Power outages
* Unexpected reboots
* Remote servers
* Home lab environments

## Interactive Telegram Bot

Monitor includes a Telegram bot that allows remote interaction with the monitored server.

Current commands:

* /help
* /memory
* /disk
* /services

The bot runs as a persistent systemd service and allows administrators to query server status without opening an SSH session.

## Systemd Integration

Monitor is designed to run using:

* systemd services
* systemd timers

allowing it to operate automatically without requiring additional infrastructure.

---

# Example Notification

```text
📊 Daily Server Report

Disk Usage: 34%
Memory Usage: 41%

ssh: Running
tailscaled: Running
```

---

# Example Bot Interaction

```text
/help
```

Response:

```text
Available Commands

/help
/memory
/disk
/services
```

---

# Architecture

```text
                    Telegram
                       ▲
                       │
        ┌──────────────┴──────────────┐
        │                             │
        │                             │
        ▼                             ▼

 monitor-bot.service         monitor.service
        │                           │
        │                           │
        ▼                           ▼

 Telegram Commands          Scheduled Checks
 (/memory, /disk,           (disk, memory,
  /services, etc.)           services)

        │                           │
        └──────────────┬────────────┘
                       │
                       ▼

                 Monitor Core
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼

       Disk        Memory       Services
       Checks      Checks       Checks
```

---

# Technologies

* Python
* uv
* systemd
* Telegram Bot API
* Linux
* Tailscale

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/richardayikwei/monitor.git

cd monitor
```

## Install Dependencies

Install runtime and development dependencies:

```bash
uv sync --all-groups
```

## Install Package in Editable Mode

```bash
uv pip install -e .
```

Monitor uses an editable installation during development.

This allows source code changes to take effect immediately without requiring reinstallation.

---

# Configuration

Application settings are stored separately from secrets.

## Create Configuration Files

```bash
cp config.example.toml config.toml

cp .env.example .env
```

## Configuration

Example:

```toml
disk_threshold = 90

memory_threshold = 90

services = [
    "ssh",
    "tailscaled"
]
```

## Environment Variables

```text
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
```

---

# Telegram Setup

## Create a Bot

1. Open Telegram.
2. Search for BotFather.
3. Run:

```text
/newbot
```

4. Follow the prompts.
5. Copy the bot token.

## Get Your Chat ID

Send a message to your bot.

Visit:

```text
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

Locate:

```text
chat.id
```

and place it in:

```text
TELEGRAM_CHAT_ID
```

---

# Running Manually

## Health Check

```bash
uv run monitor
```

## Daily Report

```bash
uv run monitor-daily-report
```

## Boot Notification

```bash
uv run monitor-boot-notification
```

## Telegram Bot

```bash
uv run monitor-bot
```

---

# Systemd Integration

## Monitor Service

Runs scheduled health checks.

Example:

```ini
[Unit]
Description=Monitor Health Check

[Service]
Type=oneshot
WorkingDirectory=/path/to/monitor
ExecStart=/path/to/.venv/bin/monitor
```

## Monitor Timer

Example:

```ini
[Unit]
Description=Run Monitor Every 15 Minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=15min

[Install]
WantedBy=timers.target
```

Enable:

```bash
sudo systemctl daemon-reload

sudo systemctl enable --now monitor.timer
```

---

## Daily Report Service

Runs a scheduled report.

Example schedule:

```text
08:00 every day
```

Typically implemented using:

```text
daily-report.service
daily-report.timer
```

---

## Boot Notification Service

Runs once whenever the machine starts.

Typically implemented using:

```text
boot-notification.service
```

No timer is required.

---

## Telegram Bot Service

Runs continuously and listens for Telegram commands.

Example:

```ini
[Unit]
Description=Monitor Telegram Bot
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/path/to/monitor
ExecStart=/path/to/.venv/bin/monitor-bot

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable:

```bash
sudo systemctl daemon-reload

sudo systemctl enable --now monitor-bot.service
```

---

# Telegram Commands

| Command   | Description                      |
| --------- | -------------------------------- |
| /help     | Show available commands          |
| /memory   | Display current memory usage     |
| /disk     | Display current disk usage       |
| /services | Display monitored service status |

Planned commands:

* /status
* /uptime
* /report

---

# Development

## Commitizen

This project uses Commitizen for conventional commits and automated version management.

Create commits using:

```bash
uv run cz commit
```

Generate a version bump:

```bash
uv run cz bump
```

View available commands:

```bash
uv run cz --help
```

---

## Documentation

This project uses docstrings to document modules, functions, and classes.

### Generate Docstring Templates

Preview changes:

```bash
uv run pyment src/monitor/checks/memory.py
```

Generate and write docstrings:

```bash
uv run pyment -w -o google src/monitor/checks/memory.py
```

Generate docstrings for an entire directory:

```bash
uv run pyment -w -o google src/
```

> Pyment generates the structure, but meaningful descriptions should be written by the developer.

### Validate Documentation

```bash
uv run pydocstyle src/
```

This reports:

* Missing module docstrings
* Missing function docstrings
* Missing class docstrings

### Documentation Philosophy

The goal of documentation is not only to describe what the code does, but also to explain why it exists.

Contributors are encouraged to document:

* Module purpose
* Public functions
* Function arguments
* Return values
* Important side effects
* Non-obvious design decisions

---

## Development Environment

Install all development dependencies:

```bash
uv sync --all-groups
```

---

# Roadmap

Planned improvements include:

* Service recovery notifications
* State-based alerts
* Historical reporting
* Enhanced Telegram bot commands
* Multi-node monitoring
* Integration with Community Compute experiments

---

# Motivation

This project began as part of a larger learning journey involving:

* Linux administration
* Remote server management
* SSH
* Tailscale
* systemd
* Infrastructure monitoring

The goal was not only to solve a practical problem but also to gain a deeper understanding of operating and maintaining real systems.

---

# Changelog

See:

```text
CHANGELOG.md
```

for release history.

---

# Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

If you find an issue or have an idea for improvement, please open an issue or submit a pull request.

---

# License

Released under the MIT License.
