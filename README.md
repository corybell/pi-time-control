# PI-TIME-CONTROL
python3 | pip3 | pipenv | flask | pytest

## INSTALL
`pipenv install`

## WEB SERVER
`pipenv run ./scripts/start.sh`

## TESTS
`pipenv run ./scripts/test.sh`

## HEALTH CHECK
http://localhost:5001/health-check

## SUPERVISOR
- move config file to: `/etc/supervisor/conf.d/pi-time-control.conf`
- restart: `sudo systemctl restart supervisor.service`
- open client: `sudo supervisorctl`
- get logs: `tail pi-time-control stderr`