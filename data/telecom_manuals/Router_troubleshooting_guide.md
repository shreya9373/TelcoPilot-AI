# Router Troubleshooting Guide

**Document ID:** DT-NOC-GUIDE-021

**Department:** Access Network Operations

**Version:** 2.5

**Classification:** Internal

**Last Updated:** May 2026

---

# Purpose

This guide provides standardized troubleshooting procedures for router connectivity issues affecting residential broadband and enterprise customers.

It should be used whenever users report complete loss of internet connectivity, unstable Wi-Fi, intermittent packet loss, or router hardware failures.

---

# Common Customer Complaints

Typical reports include:

- My router is not working.
- Internet connection is unavailable.
- Wi-Fi is connected but there is no internet.
- Internet disconnects frequently.
- Router LEDs are blinking red.
- Slow browsing despite strong Wi-Fi signal.

---

# Initial Verification

Before performing advanced diagnostics, verify:

1. Router power status.
2. WAN cable connection.
3. Optical Network Terminal (ONT) status.
4. Broadband authentication status.
5. DHCP lease allocation.
6. Internet service availability.
7. Recent maintenance activities.

---

# Common Root Causes

## Router Power Failure

Symptoms:

- Router LEDs OFF
- No Wi-Fi network visible

Recommended actions:

- Verify power adapter.
- Restart router.
- Replace faulty power supply if necessary.

---

## WAN Link Failure

Symptoms:

- Wi-Fi available
- Internet unavailable

Possible causes:

- ISP outage
- Fiber cable disconnected
- ONT offline

Recommended actions:

- Verify WAN interface.
- Check ONT alarms.
- Verify upstream connectivity.
- Contact transport operations if required.

---

## Authentication Failure

Symptoms:

- Router online
- PPPoE authentication fails

Possible causes:

- Incorrect credentials
- Authentication server unavailable

Recommended actions:

- Verify PPPoE configuration.
- Reset authentication session.
- Check authentication server logs.

---

## DNS Resolution Failure

Symptoms:

- Websites fail to load
- Ping to IP address successful

Recommended actions:

- Verify DNS server availability.
- Switch to backup DNS.
- Flush DNS cache.
- Monitor DNS response time.

---

## Wi-Fi Performance Issues

Possible causes:

- Channel interference
- Weak signal strength
- High client density

Recommended actions:

- Change Wi-Fi channel.
- Verify signal strength.
- Restart wireless service.
- Update router firmware.

---

# Escalation Criteria

Escalate the incident if:

- Multiple customers report the same issue.
- ONT alarms are active.
- Fiber infrastructure failure is suspected.
- Authentication services remain unavailable.
- Hardware replacement is required.

---

# Resolution Checklist

Before closing the incident verify:

✓ Internet connectivity restored

✓ DNS resolution successful

✓ Router LEDs normal

✓ Customer confirms service restoration

✓ No active alarms remain

---

# Related Documents

- Fiber Backhaul Runbook
- 5G Core Operations Manual
- DT-NOC-SOP-017