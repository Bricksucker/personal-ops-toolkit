# Infrastructure

## Overview

The **Infrastructure** module contains tools and scripts for managing, monitoring, and interacting with systems and small-scale environments (e.g., personal labs, clusters, and networked devices).

This section focuses on **operational control, visibility, and automation**, rather than offensive or exploitative capabilities.

It is designed to support:

* Lab environments (e.g., Raspberry Pi clusters)
* Networked system management
* Secure and repeatable operations

---

## Scope

This module includes:

* Node discovery and inventory
* System health monitoring
* SSH management and automation
* Parallel command execution
* Lightweight orchestration tools

All tools are designed to be:

* Transparent (no hidden behavior)
* Non-persistent
* Safe for controlled environments

---

## Directory Structure

```
infrastructure/
├── python/
│   ├── cluster_health.py
│   └── ssh_key_sync.py
├── bash/
│   ├── node_discover.sh
│   └── parallel_exec.sh
└── README.md
```

---

## Tool Descriptions

### `node_discover.sh`

**Purpose:**
Identify active nodes on a local network.

**Features:**

* Basic network scanning (ping or ARP-based)
* Outputs reachable hosts
* Useful for lab or cluster environments

---

### `cluster_health.py`

**Purpose:**
Check the status of multiple systems.

**Features:**

* Uptime checks
* Basic resource checks (CPU, memory, disk)
* Aggregated output for multiple nodes

---

### `ssh_key_sync.py`

**Purpose:**
Distribute SSH keys across systems for secure, passwordless access.

**Features:**

* Copies public keys to remote hosts
* Simplifies cluster setup
* Ensures consistent authentication

---

### `parallel_exec.sh`

**Purpose:**
Run commands across multiple systems simultaneously.

**Features:**

* Executes commands over SSH
* Works with a list of hosts
* Useful for updates, checks, and automation

---

## Design Principles

* **Automation-first:** Reduce repetitive manual tasks
* **Minimalism:** Keep tools simple and composable
* **Visibility:** Prefer readable output over silent execution
* **Security-aware:** Use SSH and avoid unsafe practices

---

## Example Workflow

1. Discover nodes:

```bash
./node_discover.sh 192.168.1.0/24
```

2. Sync SSH keys:

```bash
python ssh_key_sync.py hosts.txt
```

3. Check system health:

```bash
python cluster_health.py hosts.txt
```

4. Run a command across all nodes:

```bash
./parallel_exec.sh hosts.txt "uptime"
```

---

## Use Cases

* Managing a Raspberry Pi cluster
* Monitoring lab environments
* Automating system administration tasks
* Supporting cybersecurity testing infrastructure

---

## Notes

* These tools assume **authorized access** to all systems
* Designed for **personal labs and controlled environments**
* Not intended for unauthorized network interaction

---

## Future Improvements

* [ ] Add real-time status dashboard (CLI)
* [ ] Improve error handling and retries
* [ ] Add JSON output for integration with other modules
* [ ] Integrate with scanning/recon modules for asset tracking
* [ ] Add logging and audit trails

---

## Summary

The Infrastructure module provides the **operational backbone** of this toolkit — enabling reliable interaction with systems, supporting other modules, and reinforcing a structured, automation-driven workflow.
