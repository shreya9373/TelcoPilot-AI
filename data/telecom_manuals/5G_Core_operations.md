# 5G Core Operations Manual

**Document ID:** DT-CORE-005

**Department:** Core Network Operations

**Version:** 2.8

**Classification:** Internal

**Last Updated:** February 2026

---

# Overview

The 5G Core (5GC) is responsible for authentication, mobility management, session establishment, policy enforcement, and user plane traffic forwarding.

A failure in the 5G Core can impact thousands of subscribers simultaneously, making rapid detection and recovery critical.

---

# Core Network Functions

## Access and Mobility Management Function (AMF)

Responsibilities:

- User registration
- Authentication
- Mobility management
- Connection management
- Security procedures

Common alarms:

- Registration Failure
- Authentication Timeout
- AMF Overload
- Signaling Congestion

---

## Session Management Function (SMF)

Responsibilities:

- PDU Session Establishment
- IP Address Allocation
- Session Modification
- QoS Policy Assignment

Common alarms:

- Session Setup Failure
- PDU Establishment Timeout
- QoS Configuration Failure

---

## User Plane Function (UPF)

Responsibilities:

- Packet Forwarding
- User Traffic Routing
- Traffic Filtering
- Usage Reporting

Common alarms:

- High Packet Loss
- High Throughput Utilization
- UPF CPU Overload
- Interface Failure

---

# Health Checks

Network engineers should verify:

- AMF Registration Success Rate
- SMF Session Success Rate
- UPF Packet Forwarding Rate
- CPU Utilization
- Memory Utilization
- Interface Availability
- Heartbeat Status

---

# Common Failure Scenarios

## Authentication Failure

Possible causes:

- Subscriber database unavailable
- Authentication server timeout
- Certificate expiration

Recommended actions:

- Verify UDM connectivity.
- Check authentication logs.
- Restart affected authentication services.

---

## Session Establishment Failure

Symptoms:

- Users cannot access mobile data.
- PDU sessions fail.
- Internet connectivity unavailable.

Possible causes:

- SMF failure
- UPF overload
- Policy Control Function unavailable

---

## High User Plane Latency

Possible causes:

- UPF congestion
- High CPU utilization
- Packet processing delays
- Transport network issues

Recommended actions:

- Verify UPF health.
- Check packet forwarding statistics.
- Inspect transport latency.
- Enable traffic redistribution.

---

# Performance Thresholds

Recommended operational limits:

- CPU Utilization < 80%
- Memory Utilization < 75%
- Packet Loss < 1%
- Session Success Rate > 99%
- Authentication Success Rate > 99%
- Average Core Latency < 20 ms

---

# Escalation Criteria

Immediately escalate if:

- Multiple AMFs become unavailable.
- Authentication success rate falls below 95%.
- Session establishment failures exceed operational thresholds.
- Multiple UPFs report critical alarms.

---

# Related Documents

- DT-NOC-SOP-017
- Fiber Backhaul Runbook
- Incident Escalation Matrix