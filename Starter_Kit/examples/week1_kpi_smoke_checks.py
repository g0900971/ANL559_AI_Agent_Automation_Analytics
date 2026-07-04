from csv import DictReader
from datetime import date, datetime, timedelta
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "sample_data"
REFERENCE_DATE = date(2026, 6, 26)


def read_csv(filename):
    with (DATA_DIR / filename).open(newline="", encoding="utf-8") as file:
        return list(DictReader(file))


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def is_true(value):
    return str(value).strip().lower() == "true"


def calculate_kpis():
    customers = read_csv("week1_customers.csv")
    sales = read_csv("week1_sales.csv")
    support = read_csv("week1_support.csv")

    paid_active_accounts = sum(
        1
        for row in customers
        if row["subscription_status"] == "active" and is_true(row["is_paid"])
    )

    recent_login_cutoff = REFERENCE_DATE - timedelta(days=30)
    recent_login_customers = sum(
        1
        for row in customers
        if parse_date(row["last_login_date"]) >= recent_login_cutoff
    )

    june_sales = [
        row
        for row in sales
        if parse_date(row["order_date"]).year == 2026
        and parse_date(row["order_date"]).month == 6
    ]

    gross_june_revenue = sum(int(row["gross_amount"]) for row in june_sales)
    net_june_revenue = sum(
        int(row["gross_amount"]) - int(row["refund_amount"])
        for row in june_sales
    )

    open_support_tickets = sum(1 for row in support if not row["closed_date"])

    return {
        "paid_active_accounts": paid_active_accounts,
        "recent_login_customers": recent_login_customers,
        "gross_june_revenue": gross_june_revenue,
        "net_june_revenue": net_june_revenue,
        "open_support_tickets": open_support_tickets,
    }


def run_smoke_checks(actual):
    expected = {
        "paid_active_accounts": 6,
        "recent_login_customers": 7,
        "gross_june_revenue": 2860,
        "net_june_revenue": 2660,
        "open_support_tickets": 3,
    }

    all_passed = True
    for metric, expected_value in expected.items():
        actual_value = actual[metric]
        passed = actual_value == expected_value
        all_passed = all_passed and passed
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {metric} expected {expected_value}, got {actual_value}")

    return all_passed


if __name__ == "__main__":
    kpis = calculate_kpis()
    print("Week 1 KPI smoke checks")
    print("-" * 30)
    passed = run_smoke_checks(kpis)
    print("-" * 30)
    print("All checks passed." if passed else "Some checks failed.")
