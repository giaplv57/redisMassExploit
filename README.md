# redisMassExploit
Some handy script to collect hosts installed redis (using Shodan search engine) and exploit them

Requirements: `requests` and `paramiko` python modules, `redis-cli` program 

##How to use
Using shodanCollector first to get a list of hosts installed redis (can collect more than 3000 IP at my execution time).
(I remove most of the hosts in this repo due to security concern)

Copy the archieved IP list to the "targets" file (in proper format) and run massAttack!!!

For further information and workaround, please take a look on [my post](https://medium.com/@giaplvk57/pwn-a-bunch-of-servers-using-a-redis-misconfiguration-and-shodan-search-engine-eaeeb2a1a14c#.vp18yclvg "Pwn a bunch of servers via a Redis misconfiguration and the Shodan search engine") in medium.
