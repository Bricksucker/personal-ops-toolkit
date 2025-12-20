# Personal Ops Toolkit

A personal, evolving operations toolkit focused on **cybersecurity experimentation**, **infrastructure management**, and **defensive awareness**.

This repository serves two purposes:

1. A **practical toolbox** I actively use for reconnaissance, scanning, analysis, and system operations.
2. A **living knowledge base** that documents techniques, experiments, and lessons learned across multiple domains of cybersecurity.

The emphasis is on *clarity, responsibility, and real-world usefulness* rather than flashy or weaponized tooling.

---

## Philosophy & Scope

* **Cybersecurity-first**: Most tools map directly to established security domains (recon, scanning, crypto, detection, etc.)
* **Separation of concerns**:

  * **Python** → logic, analysis, data processing
  * **Bash** → orchestration, system interaction, automation
* **Modular & reusable**: Small tools that do one thing well
* **Educational & defensive-minded**: Exploitation is limited to demos, labs, and controlled environments
* **Ongoing project**: This repo is expected to grow, refactor, and improve over time

---

## Repository Structure

```
personal-ops-toolkit/
│
├── docs/                  # High-level documentation & policies
├── common/                # Shared helpers (Python & Bash)
│
├── reconnaissance/        # Host & information discovery
├── scanning/              # Port, service, and vulnerability scanning
├── exploitation/          # Controlled demos & lab tooling
├── post_exploitation/     # Enumeration & access analysis
├── cryptography/          # Hashing, entropy, and crypto experiments
├── detection_defense/     # Blue-team and detection tooling
├── infrastructure/        # Cluster & system management
├── misc_tools/            # Non-security utilities
│
├── broken_and_fixed/      # Debugging write-ups & lessons learned
└── README.md
```

Each major category contains its own `README.md` explaining intent, limitations, and usage examples.

---

## Tooling Breakdown

### Reconnaissance

**Purpose:** Identify hosts, services, and passive information.

* Host discovery
* DNS enumeration
* MAC vendor identification
* Lightweight passive recon helpers

### Scanning

**Purpose:** Identify exposed services and configurations.

* Nmap wrappers & profiles
* Service fingerprinting
* Safe vulnerability detection helpers (no exploit delivery)

### Exploitation (Controlled)

**Purpose:** Demonstrate *how* weaknesses are abused — not to weaponize them.

* Authentication testing demos
* Payload handling & validation
* Lab-focused tooling only

### Post-Exploitation

**Purpose:** Analyze system state *after access is obtained* (theoretically or in labs).

* Privilege enumeration
* User & system surveys
* Persistence **detection**, not implanting

### Cryptography

**Purpose:** Evaluate strength and performance of cryptographic primitives.

* Hash performance benchmarks
* Wordlist effectiveness testing
* Entropy analysis

### Detection & Defense

**Purpose:** Build blue-team credibility.

* Log analysis
* Baseline deviation detection
* Simple anomaly indicators

### Infrastructure

**Purpose:** Manage and observe real systems.

* Pi cluster health checks
* SSH key management
* Parallel execution helpers

### Broken & Fixed

**Purpose:** Document real debugging experience.

* What broke
* Symptoms
* Root cause
* Fix
* Takeaways

This section exists to preserve knowledge and demonstrate systematic troubleshooting skills.

---

## Responsible Use

All tools in this repository are intended for:

* Personal systems
* Lab environments
* Capture-the-flag challenges
* Explicitly authorized testing

No tool is designed to be stealthy, persistent, or destructive.

If a technique could reasonably be misused, it is documented defensively and scoped appropriately.

---

## Environment

* Python 3.9+
* Bash (POSIX-compatible, some tools may assume GNU utilities)
* Common dependencies documented per submodule

An environment setup guide lives in `docs/environment-setup.md`.

---

## TODO Roadmap

### Core Infrastructure

* [ ] Establish shared Python logging utilities
* [ ] Create Bash argument parsing helpers
* [ ] Add consistent output formats (JSON / text)

### Reconnaissance

* [ ] Host discovery with multiple probing strategies
* [ ] DNS enumeration tool
* [ ] MAC vendor lookup with offline cache
* [ ] Passive recon script wrapper

### Scanning

* [ ] Nmap profile presets (fast, full, stealth-aware)
* [ ] Python-based service fingerprinting
* [ ] Scan result normalization to JSON

### Cryptography

* [ ] Hash performance benchmarking suite
* [ ] Wordlist effectiveness tester
* [ ] Password entropy estimator
* [ ] Visualization of attempts/sec over time

### Detection & Defense

* [ ] Authentication log analyzer
* [ ] Baseline behavior generator
* [ ] Simple anomaly scoring system

### Infrastructure

* [ ] Pi cluster node discovery
* [ ] Cluster health dashboard (CLI)
* [ ] SSH key synchronization tool
* [ ] Parallel command execution helper

### Documentation

* [ ] Category-level READMEs
* [ ] Threat modeling document
* [ ] Responsible use policy
* [ ] Example outputs & screenshots

### Broken & Fixed

* [ ] nmcli unmanaged interface write-up
* [ ] dhcpcd missing service analysis
* [ ] USB Wi-Fi driver issues
* [ ] Router vulnerability scan interpretation

---

## Status

This is an **active, evolving project**. Expect refactors, new tools, and improved documentation as understanding deepens and requirements change.

Contributions are not currently accepted; this repository is intentionally personal in scope.

---

*Built to be useful first, impressive second.*

