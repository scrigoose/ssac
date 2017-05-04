# Simple Server Availability Checker
Checks TCP connection to given hosts on given ports. Servers are provided in file. 

Each line should contain:

`host[:port]`

If port is not given, `80` is taken by default.
Check `server.list` for exaple input.

## Usage
`$ python3 ssac.py`

## Output
Output is in form:

`host:port -- time -- status`

where

> **time** - required time for connection creation

> **status** - status of connection creation

### Output example

```
www.google.com:80    --  0.156s -- OK
 www.yahoo.com:80    --  0.208s -- OK
www.github.com:443   --  0.519s -- OK
     127.0.0.1:22    --  0.001s -- Failed
     127.0.0.1:9090  --  0.001s -- Failed
 192.168.1.254:80    --  0.002s -- OK
 192.168.1.254:443   --  0.002s -- OK
 192.168.1.254:8080  --  0.004s -- OK
 192.168.1.254:9090  --  0.003s -- Failed
```