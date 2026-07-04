# Week 1 Metric Definitions

## Paid Active Accounts

Count customers where `subscription_status` is `active` and `is_paid` is `true`.

## Recent Login Customers

Count customers with `last_login_date` within 30 days of 2026-06-26.

## Gross June Revenue

Sum `gross_amount` for orders with `order_date` in June 2026.

## Net June Revenue

Sum `gross_amount - refund_amount` for orders with `order_date` in June 2026.

## Open Support Tickets

Count tickets where `closed_date` is blank.
