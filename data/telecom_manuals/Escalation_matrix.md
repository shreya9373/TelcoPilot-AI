# Network Incident Escalation Matrix

**Document ID:** DT-NOC-POLICY-003

**Department:** Network Operations Center (NOC)

**Version:** 5.0

**Classification:** Internal

**Last Updated:** June 2026

---

# Purpose

This document defines the standard escalation procedures for network incidents. It ensures that incidents are routed to the appropriate operational team based on the incident type, severity, customer impact, and service-level agreements (SLAs).

---

# Severity Levels

## Severity 1 (Critical)

Characteristics:

- Complete service outage
- Nationwide or regional impact
- Multiple enterprise customers affected
- Revenue impact
- SLA breach likely

Response Time:

- Immediate (within 5 minutes)

Escalate to:

- NOC Manager
- Core Network Operations
- Transport Network Team
- Regional Field Operations

---

## Severity 2 (High)

Characteristics:

- Service degradation
- High latency
- Packet loss
- Cell congestion
- Multiple customer complaints

Response Time:

- Within 15 minutes

Escalate to:

- Senior NOC Engineer
- Transport Operations
- Radio Access Network (RAN) Team

---

## Severity 3 (Medium)

Characteristics:

- Individual site issues
- Router failures
- Authentication failures
- Localized performance degradation

Response Time:

- Within 30 minutes

Escalate to:

- Access Network Team
- Customer Support Engineering

---

## Severity 4 (Low)

Characteristics:

- Single customer issue
- Configuration request
- Information request
- Minor alarm

Response Time:

- Within 2 hours

Escalate to:

- Service Desk
- Technical Support

---

# Incident Type Mapping

## High Latency

Primary Team:

- Transport Operations

Secondary Team:

- Core Network Operations

---

## Packet Loss

Primary Team:

- Transport Operations

Secondary Team:

- RAN Optimization Team

---

## Fiber Backhaul Failure

Primary Team:

- Fiber Maintenance Team

Secondary Team:

- Regional Field Engineers

---

## Router Failure

Primary Team:

- Access Network Team

Secondary Team:

- Customer Support

---

## DNS Resolution Failure

Primary Team:

- Core Network Operations

Secondary Team:

- Infrastructure Services

---

## Authentication Failure

Primary Team:

- Core Network Operations

Secondary Team:

- Identity Management Team

---

# Customer Communication Guidelines

For Severity 1 and Severity 2 incidents:

- Notify impacted enterprise customers.
- Provide updates every 30 minutes.
- Record all mitigation activities.
- Publish service restoration updates.

---

# Incident Closure Requirements

An incident may only be closed after:

- Root cause identified.
- Corrective actions completed.
- Monitoring confirms service stability.
- Customer impact resolved.
- Incident report approved by the duty manager.

---

# Related Documents

- DT-NOC-SOP-017
- Fiber Backhaul Operations Runbook
- Router Troubleshooting Guide
- 5G Core Operations Manual