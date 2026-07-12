# 5G High Latency Troubleshooting

## Overview
High latency in a 5G network causes delayed responses, slow internet browsing, buffering during video streaming, and poor application performance.

## Symptoms
- Ping exceeds 150 ms
- Slow browsing
- Video buffering
- Increased response time
- High user complaints

## Possible Causes
- Tower congestion
- High CPU utilization on gNodeB
- Fiber backhaul degradation
- Packet loss
- DNS resolution delays

## Troubleshooting Procedure
1. Check latency metrics.
2. Verify packet loss.
3. Inspect CPU utilization of the serving tower.
4. Verify fiber backhaul connectivity.
5. Compare KPIs with neighboring towers.
6. Restart affected network function if required.

## Resolution
If CPU utilization exceeds 90% and packet loss exceeds 5%, enable traffic load balancing or initiate capacity expansion.