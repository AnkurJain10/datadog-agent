from datadog import initialize, statsd
import time

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

while(1):
  statsd.increment('example5_metric.increment', tags=["env:dev","dummy:123"])
  statsd.decrement('example5_metric.decrement', tags=["env:dev","dummy:123"])
  time.sleep(10)
