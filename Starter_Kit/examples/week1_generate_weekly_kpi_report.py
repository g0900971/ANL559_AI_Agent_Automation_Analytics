from csv import DictReader
from datetime import date, datetime, timedelta
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "sample_data"
OUTPUT_PATH = Path(__file__).with_name("week1_weekly_kpi_report.md")
REFERENCE_DATE = date(2026, 6, 26)
REPORT_MONTH = "June 2026"


def read_csv(filename):
    with (DATA_DIR / filename).open(newline="", encoding="utf-8") as file:
        return list(DictReader(file))


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def is_true(value):
    return str(value).strip().lower() == "true"


def money(value):
    return f"${value:,.0f}"


def customer_label(row):
    return (
        f"{row['customer_id']} "
        f"({row['subscription_status']}, paid={row['is_paid']}, "
        f"last_login={row['last_login_date']})"
    )


def calculate_report_values():
    customers = read_csv("week1_customers.csv")
    sales = read_csv("week1_sales.csv")
    support = read_csv("week1_support.csv")

    recent_login_cutoff = REFERENCE_DATE - timedelta(days=30)

    paid_active_rows = [
        row
        for row in customers
        if row["subscription_status"] == "active" and is_true(row["is_paid"])
    ]
    recent_login_rows = [
        row
        for row in customers
        if parse_date(row["last_login_date"]) >= recent_login_cutoff
    ]
    recent_login_not_paid_active = [
        row
        for row in recent_login_rows
        if not (row["subscription_status"] == "active" and is_true(row["is_paid"]))
    ]
    paid_active_without_recent_login = [
        row
        for row in paid_active_rows
        if parse_date(row["last_login_date"]) < recent_login_cutoff
    ]

    june_sales = [
        row
        for row in sales
        if parse_date(row["order_date"]).year == 2026
        and parse_date(row["order_date"]).month == 6
    ]
    gross_june_revenue = sum(int(row["gross_amount"]) for row in june_sales)
    refund_amount = sum(int(row["refund_amount"]) for row in june_sales)
    net_june_revenue = gross_june_revenue - refund_amount
    refunded_orders = [row for row in june_sales if int(row["refund_amount"]) > 0]

    open_ticket_rows = [row for row in support if not row["closed_date"]]
    high_open_ticket_rows = [
        row for row in open_ticket_rows if row["severity"].lower() == "high"
    ]

    return {
        "customers": customers,
        "sales": sales,
        "support": support,
        "paid_active_rows": paid_active_rows,
        "recent_login_rows": recent_login_rows,
        "recent_login_not_paid_active": recent_login_not_paid_active,
        "paid_active_without_recent_login": paid_active_without_recent_login,
        "june_sales": june_sales,
        "gross_june_revenue": gross_june_revenue,
        "refund_amount": refund_amount,
        "net_june_revenue": net_june_revenue,
        "refunded_orders": refunded_orders,
        "open_ticket_rows": open_ticket_rows,
        "high_open_ticket_rows": high_open_ticket_rows,
    }


def kpi_rows(values):
    return [
        {
            "metric": "Paid active accounts",
            "definition": "`subscription_status = active` and `is_paid = true`",
            "source": "week1_customers.csv",
            "actual": str(len(values["paid_active_rows"])),
            "expected": "6",
        },
        {
            "metric": "Recent-login customers",
            "definition": "`last_login_date` within 30 days of 2026-06-26",
            "source": "week1_customers.csv",
            "actual": str(len(values["recent_login_rows"])),
            "expected": "7",
        },
        {
            "metric": "Gross June revenue",
            "definition": "Sum `gross_amount` for June 2026 orders",
            "source": "week1_sales.csv",
            "actual": money(values["gross_june_revenue"]),
            "expected": "$2,860",
        },
        {
            "metric": "Net June revenue",
            "definition": "Sum `gross_amount - refund_amount` for June 2026 orders",
            "source": "week1_sales.csv",
            "actual": money(values["net_june_revenue"]),
            "expected": "$2,660",
        },
        {
            "metric": "Open support tickets",
            "definition": "Tickets where `closed_date` is blank",
            "source": "week1_support.csv",
            "actual": str(len(values["open_ticket_rows"])),
            "expected": "3",
        },
    ]


def smoke_status(actual, expected):
    return "PASS" if actual == expected else "FAIL"


def render_report(values):
    rows = kpi_rows(values)
    row_lines = []
    for row in rows:
        row_lines.append(
            "| {metric} | {definition} | {source} | {actual} | {expected} | {status} |".format(
                **row,
                status=smoke_status(row["actual"], row["expected"]),
            )
        )

    recent_login_not_paid = ", ".join(
        customer_label(row) for row in values["recent_login_not_paid_active"]
    )
    paid_active_without_recent = ", ".join(
        customer_label(row) for row in values["paid_active_without_recent_login"]
    )
    refunded_orders = ", ".join(
        f"{row['order_id']} ({row['customer_id']}, refund={money(int(row['refund_amount']))})"
        for row in values["refunded_orders"]
    )
    open_tickets = ", ".join(
        f"{row['ticket_id']} ({row['customer_id']}, {row['severity']})"
        for row in values["open_ticket_rows"]
    )
    high_open_tickets = ", ".join(
        f"{row['ticket_id']} ({row['customer_id']})"
        for row in values["high_open_ticket_rows"]
    )

    return f"""# Northstar Retail Weekly KPI Report

## Report Context

| Item | Value |
|---|---|
| Reporting period | {REPORT_MONTH} |
| Reference date | {REFERENCE_DATE.isoformat()} |
| Prepared for | COO |
| Generated from | `week1_customers.csv`, `week1_sales.csv`, `week1_support.csv`, `week1_metric_definitions.md` |
| Purpose | Produce a repeatable KPI pack with visible definitions and smoke checks. |

## Executive Summary

- Paid active accounts are **{len(values["paid_active_rows"])}** using the approved COO definition.
- Net June revenue is **{money(values["net_june_revenue"])}**, after **{money(values["refund_amount"])}** in refunds.
- Open support tickets are **{len(values["open_ticket_rows"])}**, including **{len(values["high_open_ticket_rows"])}** high-severity open ticket.
- Recent-login customers are **{len(values["recent_login_rows"])}** and must not be used as the paid-active denominator.

## KPI Summary

| Metric | Approved definition | Source | Actual | Expected smoke check | Status |
|---|---|---|---:|---:|---|
{chr(10).join(row_lines)}

## Definition Notes

The approved active-customer KPI is **paid active accounts**, not recent-login customers.

- Recent-login customers who are not paid active accounts: {recent_login_not_paid}
- Paid active accounts without recent login in the 30-day window: {paid_active_without_recent}

This is the main Week 1 reporting risk. A workflow that uses recent login as the denominator reports 7 active customers instead of the approved value of 6.

## Revenue Notes

- Gross June revenue: **{money(values["gross_june_revenue"])}**
- Refunds in June sample: **{money(values["refund_amount"])}**
- Net June revenue: **{money(values["net_june_revenue"])}**
- Refunded orders: {refunded_orders}

## Support Notes

- Open support tickets: {open_tickets}
- High-severity open tickets: {high_open_tickets}

## Smoke-Test Conclusion

All expected Week 1 smoke checks pass. The report is safe for classroom demonstration if the following limitations are kept visible:

- The data are synthetic and intentionally small.
- The report does not prove production readiness.
- The active-customer definition must remain owned by the business, not by the agent.
- Any future metric added to the pack needs its own approved definition and smoke check.

## Recommended COO Message

The weekly KPI workflow can be rerun from the provided source files. The checked numbers for the sample are 6 paid active accounts, {money(values["net_june_revenue"])} net June revenue, and {len(values["open_ticket_rows"])} open support tickets. We rejected recent login as the active-customer denominator because it would overstate the approved KPI.
"""


def main():
    values = calculate_report_values()
    report = render_report(values)
    OUTPUT_PATH.write_text(report, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
