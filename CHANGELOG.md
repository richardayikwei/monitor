## 1.0.0 (2026-06-01)

### BREAKING CHANGE

- All systemd services had to be refactored to accomadate changes to app

### Feat

- **services.py**: add function for telegram bot to check for services running
- **disk.py**: add a function that will be used by telegram bot to check disk usage

### Fix

- **whole-project**: Turn porject into package to solve import issues

## 0.6.0 (2026-05-29)

### Feat

- **telegram.py**: Send messages to the telegram bot

## 0.5.0 (2026-05-29)

### Feat

- **recovery/services.py**: add system restart when any of the services stop

## 0.4.0 (2026-05-29)

### Feat

- **heartbeat.py,-main.py**: add system heartbeat monitor

## 0.3.0 (2026-05-29)

### Feat

- **config.py,-disk.py,-services.py,-memory.py,-main.py**: use config to update parameters in functions

## 0.2.0 (2026-05-29)

### Feat

- **disk.py,-memory.py,-services.py,-logger.py,-main.py**: build base monitor
