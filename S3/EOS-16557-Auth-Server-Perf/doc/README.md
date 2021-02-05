
TEST: 
-----
Measure the performance of the Auth Server by issuing around 3000-4000 requests per second

APPROACHES:
-----------
1) Test with the script shared by Shalaka.
2) Wrote a script that spawns multiple processes and issues the requests
3) Apache Bench
4) Locust-Load Testing Tool.Integrated Locust with S3iamcli code so that getuser requests are sent out and the time for getuser requests is measured.


OBSERVATIONS:
------------
1)With Approach 1 and 2, I could not reach beyond 10-15 rps.Increasing the number of processes or threads did not help.

3)With Apache bench:
Apachebench is good for simple hammering of a single URL.Using this, i could see ~600rps on a VM.

4)Locust parameters had to be modified to improve the performance
-Modified the wait times so that there is no delay between sending of requests
-changed the number of clients and the hatch rates
But this improved the RPS only marginally.On VM i could see around 15 rps on HW it was around 20-25rps

Going ahead, Locust needs to be configured in a distributed mode with master slave.
But even with this it not clear if we might achieve the RPS that is needed.So, more study is needed on this.

From https://k6.io/blog/comparing-best-open-source-load-testing-tools
Python is actually both the biggest upside and the biggest downside with Locust. The downside part of it stems from the fact that Locust is written in Python. Python code is slow, and that affects Locust's ability to generate traffic and provide reliable measurements.
 Locust was single-threaded, so if you did not run multiple Locust processes, Locust could only use one CPU core and would not be able to generate much traffic at all. Luckily, Locust had support for distributed load generation even then, and that made it go from the worst performer to the second worst, in terms of how much traffic it could generate from a single physical machine. Another negative thing about Locust back then was that it tended to add huge amounts of delay to response time measurements, making them very unreliable.
 
With this information,in hindsight, Jmeter might have been tool of choice.




