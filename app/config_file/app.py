import newrelic.agent
#newrelic.agent.initialize('.../newrelic.ini')

import custom_module

if __name__ == "__main__":
	cf = custom_module.ClassFunction()
	while True:
		custom_module.func()
		cf.another_function()
