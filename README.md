# Monitor

A lightweight Linux monitoring agent built to monitor a personal remote server and deliver alerts through Telegram.

## Why I Built This

After setting up a remotely accessible Linux machine using SSH and Tailscale, I realized I had a new problem:

How would I know if something went wrong?

Questions I wanted answered included:

* Is the machine still online?
* Are important services running?
* Is disk usage becoming a problem?
* Is memory usage becoming excessive?
* Has the machine restarted?

Rather than relying on manually checking the system, I decided to build a lightweight monitoring agent.

Monitor is the result.

---

## Features

### Service Monitoring

Monitor checks the health of configured services.

Examples:

* ssh
* tailscaled
* custom services

### Disk Monitoring

Monitor checks disk utilization and generates alerts when configured thresholds are exceeded.

### Memory Monitoring

Monitor checks memory usage and reports when usage exceeds configured limits.

### Telegram Notifications

Alerts can be delivered directly to Telegram.

Examples:

* Service failures
* Daily health reports
* Boot notifications

### Daily Health Reports

A scheduled summary can be sent containing:

* Disk usage
* Memory usage
* Service status
* System health information

### Boot Notifications

Receive a Telegram message whenever the monitored machine starts.

### Systemd Integration

Monitor is designed to run using:

* systemd services
* systemd timers

allowing it to operate automatically without requiring additional infrastructure.

---

## Example Notification

```text
📊 Daily Server Report

Disk Usage: 34%
Memory Usage: 41%

ssh: Running
tailscaled: Running
```

---

## Architecture

```text
systemd timer
       │
       ▼
monitor.service
       │
       ▼
Monitor Agent
       │
       ├── Disk Checks
       ├── Memory Checks
       ├── Service Checks
       │
       ▼
Telegram Notifications
```

---

## Technologies

* Python
* uv
* systemd
* Telegram Bot API
* Linux

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/richardayikwei/monitor.git

cd monitor
```

### Install Dependencies

Install both runtime and development dependencies:

```bash
uv sync --all-groups
```

---

## Configuration

Application settings are stored separately from secrets.

### Create Configuration Files

```bash
cp config.example.toml config.toml

cp .env.example .env
```

### Configuration

Example:

```toml
disk_threshold = 90

memory_threshold = 90

services = [
    "ssh",
    "tailscaled"
]
```

### Environment Variables

```text
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
```

---

## Telegram Setup

### Create a Bot

1. Open Telegram.
2. Search for BotFather.
3. Run:

```text
/newbot
```

4. Follow the prompts.
5. Copy the bot token.

### Get Your Chat ID

Send a message to your bot.

Then visit:

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

## Running Manually

Run a health check:

```bash
uv run python src/monitor/main.py
```

Run a daily report:

```bash
uv run python src/monitor/daily_report.py
```

Run a boot notification:

```bash
uv run python src/monitor/boot_notification.py
```

---

## Systemd Integration

### Monitor Service

Example:

```ini
[Unit]
Description=Monitor Health Check

[Service]
Type=oneshot
WorkingDirectory=/path/to/monitor
ExecStart=/path/to/uv run python src/monitor/main.py
```

### Monitor Timer

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

## Daily Reports

A dedicated service and timer can be used to generate daily reports.

Example schedule:

```text
08:00 every day
```

---

## Boot Notifications

A dedicated service can be configured to send a notification whenever the machine starts.

Useful for:

* Power outages
* Unexpected reboots
* Remote servers
* Home lab environments

---

## Development

### Commitizen

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

### Documentation

This project uses docstrings to document modules, functions, and classes.

#### Generate Docstring Templates

The project uses Pyment to generate docstring skeletons for existing code.

Preview changes without modifying a file:

```bash
uv run pyment src/monitor/checks/memory.py
```

Generate and write docstrings to a file:

```bash
uv run pyment -w -o google src/monitor/checks/memory.py
```

Generate docstrings for an entire directory:

```bash
uv run pyment -w -o google src/
```

> **Note:** It is recommended to review and improve generated docstrings manually. Pyment generates the structure, but meaningful descriptions should be written by the developer.

#### Validate Documentation

The project uses pydocstyle to identify missing or incorrectly formatted docstrings.

Run:

```bash
uv run pydocstyle src/
```

This will report issues such as:

* Missing module docstrings
* Missing function docstrings
* Missing class docstrings

#### Documentation Philosophy

The goal of documentation is not only to describe what the code does, but also to explain why it exists.

When adding or updating code, contributors are encouraged to document:

* The purpose of the module
* The purpose of public functions
* Function arguments
* Return values
* Important side effects
* Design decisions that may not be immediately obvious

```
```

### Development Environment

Install all development dependencies:

```bash
uv sync --all-groups
```

---

## Roadmap

Planned improvements include:

* State-based alerts
* Service recovery notifications
* Historical reporting
* Node-to-node monitoring
* Integration with future Community Compute experiments

---

## Motivation

This project began as part of a larger learning journey involving:

* Linux administration
* Remote server management
* SSH
* Tailscale
* systemd
* Infrastructure monitoring

The goal was not only to solve a practical problem but also to gain a deeper understanding of operating and maintaining real systems.

---

## Changelog

See:

```text
CHANGELOG.md
```

for release history.

---

## Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

If you find an issue or have an idea for improvement, please open an issue or submit a pull request.

---

## License

Released under the MIT License.

