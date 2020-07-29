# newrelic-python-docker

A simple Python script that demonstrates custom instrumentation via `newrelic.ini` configuration file within a container!
Script will continously run until stopped.

The setup follows the instructions in the NR documentation [here](https://docs.newrelic.com/docs/agents/python-agent/installation/install-new-relic-python-agent-docker#build).

## Get started

1. Build the base Python image w/ Python NR-APM agent
  * Change the `FROM` in the `Dockerfile` to whichever Python version or Linux distro you wish to use
  * `docker build -t python_newrelic:latest .`
2. `CD` into `/app/` and build the Python script image
  * Make changes to `../app/config_file/newrelic.ini` as you see fit.
  * `docker build -t python_app:latest .`
3. Run the Python script image

```
docker run -e NEW_RELIC_CONFIG_FILE=/usr/local/config_file/newrelic.ini \
	-e NEW_RELIC_LICENSE_KEY=YOUR_LICENSE_HERE \
	python_app:latest
```

4. View data in New Relic.