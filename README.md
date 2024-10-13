# raft-election-algorithm

Python implementation of Raft Consensus Protocol for Log Replication in a distributed system.

---

##### Authors:

| Name                  | Email                                                                      | Github                                        |
|-----------------------|----------------------------------------------------------------------------|-----------------------------------------------|
| **Iskander Nafikov**  | [i.nafikov@innopolis.university](mailto:i.nafikov@innopolis.university)    | [iskanred](https://github.com/iskanred)       |
| **Ivan Inchin**       | [i.inchin@innopolis.university](mailto:i.inchin@innopolis.university)      | [extrabution](https://github.com/Extrabution) |                                                        |

---

## Description
### What is Raft?
Raft is a **consensus** algorithm that is designed to be easy to understand.
It's equivalent to [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) in fault-tolerance and performance.
The difference is that it's decomposed into relatively independent subproblems,
and it cleanly addresses all major pieces needed for practical systems.

### What is Consensus?
Consensus is a fundamental problem in fault-tolerant distributed systems.
Consensus involves multiple servers agreeing on values.
Once they reach a decision on a value, that decision is final.
Typical consensus algorithms make progress when any majority of their servers is available; for example,
a cluster of 5 servers can continue to operate even if 2 servers fail.
If more servers fail, they stop making progress (but will never return an incorrect result).

Consensus typically arises in the context of replicated state machines, a general approach to building fault-tolerant systems.
Each server has a state machine and a log.
The state machine is the component that we want to make fault-tolerant, such as a hash table.
It will appear to clients that they are interacting with a single, reliable state machine, even if a minority of the servers in the cluster fail.
Each state machine takes as input commands from its log.
In our hash table example, the log would include commands like set x to 3.
A consensus algorithm is used to agree on the commands in the servers' logs.
The consensus algorithm must ensure that if any state machine applies set x to 3 as the nth command,
no other state machine will ever apply a different nth command.
As a result, each state machine processes the same series of commands and thus produces the same series of results and arrives at the same series of states.

## Our Solution
### Introduction
The best way to understand **Raft** is to implement this algorithm. Therefore, we have implemented the consensus algorithm.
Since Raft is often used for replication we have also implemented Log Replication mechanism in a form of KV storage.

To keep things simple we emulated a distributed system on the same machine with the ability to suspend some nodes emulating behavior of losing
network connection with this node. However, there is an ability to run this code on the same network on several machines.

What is more, we have implemented client application which supports several features to interact with the servers' nodes.

To summarize, we have implemented:
1. Server-side application of a KV storage using Raft algorithm for Log Replication in a distributed system.
2. Client-side application to interact with the servers' nodes.

### Implementation
We used **gRPC** protocol for inter-server communication and communication between a client and servers.
**Protobuf** is used as a messaging protocol.

There are several important files for the project:
* `client.py` contains client-side application's code
* `server.py` contains server-side application's code
* `config.conf` contains the list of the servers in such a format: `{id} {ip_addr} {port}`
Config is needed for servers to know the number and the location of other servers.
* `raft.proto` is a description of messages in Protobuf format

The algorithm work exactly as in the [tutorial](https://thesecretlivesofdata.com/).

Each of the servers contains the following gRPC operations:
* **Request Vote**: a server, that is a candidate to become a leader, requests a vote from other servers.
* **Append Entries**: a leader server sends a heartbeat to other servers containing also:
current storage info, current leader, current election term, current commit.
* **GetLeader**: a client asks some server which of the node is the current leader.
* **Suspend**: a client requests a server to suspend its work for the given number of seconds.
* **SetVal**: a client requests to put some value in our KV storage that will be replicated then.
* **GetVal**: a client requests to get some value by a key from out KV storage.

### Runbook
#### Server
To set up a server:
1. Copy `server.py`, `config.conf`, `raft_pb.py`, `raft_pb2_grpc.py` files to the server's machine.
2. Check that `config.py` file contains addresses of all the other server nodes in the form: `{id} {ip_addr} {port}`.
3. Configure your python environment. Make sure that `grpcio` and `grpcio-tools` modules are installed to the python environment.
4. Choose which id will current server have.
5. Run the server-side application using python: `python3 server.py {current_server_id}`

Depending on the number of server nodes `N` the first `N / 2` servers will not find the leader properly and will continue endless election process.
It happens because for a node to become a leader the majority of votes must be received.
To fix it just run all the servers.

The interesting thing is that often in the classical log replication problem using RAFT
the client is always communicating with the current leader. However, our implementation offers an
opportunity to interact with any desires server node, and it can propagate a client's requests to the current leader.
For example, 

#### Client
To set up a client applicaiton:
1. Copy `client.py`, `raft_pb.py`, `raft_pb2_grpc.py` files to the server's machine.
2. Configure your python environment. Make sure that `grpcio` and `grpcio-tools` modules are installed to the python environment.
3. Run the client-side application using python: `python3 client.py`

Afterward, you will see a simple CLI from where you can execute the following commands:
1. `connect {server_ip_addr} {server_port}`: connect to a specific server by its IPv4 address and a port number.
2. `getleader`: asks current server which node is the current leader.
3. `setval {key} {value}`: put a key value pair into the storage being connected to some server.
4. `getval {key}`: get a value by a key being connected to some server. `None` will be returned if no such a key exists.
5. `suspend {sec}`: suspend the current server node on the given number of seconds.`` 
This operation emulates network unavailability of a given node.
For instance, if you suspend a leader node, the re-election process will start in some amount of time.
6. `quit`: quits a client-side application.

### Demonstration
You can check video demo of how it all works using this link:
> https://drive.google.com/file/d/1WmoABCR_M-zQ9MEbe5QVmKHu7JlvgPLA/view?usp=sharing

If you are interested, you can also check our presentation of our solution:
> https://docs.google.com/presentation/d/167CMdcotDNh_1SLCEnPaL0eU7bv399L5X8cRSZYs1vw/edit?usp=sharing

## References
* [Paxos algorithm](https://en.wikipedia.org/wiki/Paxos_(computer_science))
* [Raft algorithm description with interactive animation](https://raft.github.io/)
* [Raft algorithm tutorial](https://thesecretlivesofdata.com/raft/) 
* [Our Raft implementation in GitHub](https://github.com/iskanred/raft-election-algorithm)
* [Our video demo](https://drive.google.com/file/d/1WmoABCR_M-zQ9MEbe5QVmKHu7JlvgPLA/view?usp=sharing)
* [Our presentation](https://docs.google.com/presentation/d/167CMdcotDNh_1SLCEnPaL0eU7bv399L5X8cRSZYs1vw/edit?usp=sharing)
