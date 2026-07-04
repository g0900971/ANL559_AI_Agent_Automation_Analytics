# Northstar Retail Weekly KPI Report

## Report Context

| Item | Value |
|---|---|
| Reporting period | June 2026 |
| Reference date | 2026-06-26 |
| Prepared for | COO |
| Generated from | `week1_customers.csv`, `week1_sales.csv`, `week1_support.csv`, `week1_metric_definitions.md` |
| Purpose | Produce a repeatable KPI pack with visible definitions and smoke checks. |

## Executive Summary

- Paid active accounts are **6** using the approved COO definition.
- Net June revenue is **$2,660**, after **$200** in refunds.
- Open support tickets are **3**, including **1** high-severity open ticket.
- Recent-login customers are **7** and must not be used as the paid-active denominator.

## KPI Summary

| Metric | Approved definition | Source | Actual | Expected smoke check | Status |
|---|---|---|---:|---:|---|
| Paid active accounts | `subscription_status = active` and `is_paid = true` | week1_customers.csv | 6 | 6 | PASS |
| Recent-login customers | `last_login_date` within 30 days of 2026-06-26 | week1_customers.csv | 7 | 7 | PASS |
| Gross June revenue | Sum `gross_amount` for June 2026 orders | week1_sales.csv | $2,860 | $2,860 | PASS |
| Net June revenue | Sum `gross_amount - refund_amount` for June 2026 orders | week1_sales.csv | $2,660 | $2,660 | PASS |
| Open support tickets | Tickets where `closed_date` is blank | week1_support.csv | 3 | 3 | PASS |

## Definition Notes

The approved active-customer KPI is **paid active accounts**, not recent-login customers.

- Recent-login customers who are not paid active accounts: C103 (cancelled, paid=false, last_login=2026-06-20), C106 (past_due, paid=false, last_login=2026-06-24)
- Paid active accounts without recent login in the 30-day window: C104 (active, paid=true, last_login=2026-05-12)

This is the main Week 1 reporting risk. A workflow that uses recent login as the denominator reports 7 active customers instead of the approved value of 6.

## Revenue Notes

- Gross June revenue: **$2,860**
- Refunds in June sample: **$200**
- Net June revenue: **$2,660**
- Refunded orders: O1003 (C103, refund=$100), O1006 (C106, refund=$100)

## Support Notes

- Open support tickets: T502 (C102, medium), T504 (C106, high), T505 (C108, medium)
- High-severity open tickets: T504 (C106)

## Smoke-Test Conclusion

All expected Week 1 smoke checks pass. The report is safe for classroom demonstration if the following limitations are kept visible:

- The data are synthetic and intentionally small.
- The report does not prove production readiness.
- The active-customer definition must remain owned by the business, not by the agent.
- Any future metric added to the pack needs its own approved definition and smoke check.

## Recommended COO Message

The weekly KPI workflow can be rerun from the provided source files. The checked numbers for the sample are 6 paid active accounts, $2,660 net June revenue, and 3 open support tickets. We rejected recent login as the active-customer denominator because it would overstate the approved KPI.
