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

## Configuration

Application settings are stored separately from secrets.

### Configuration

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
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
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

## License

Released under the MIT License.

