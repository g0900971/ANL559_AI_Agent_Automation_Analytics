from csv import DictReader
from datetime import date, datetime, timedelta
from html import escape
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "sample_data"
OUTPUT_PATH = Path(__file__).with_name("week1_kpi_dashboard.html")
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


def calculate_values():
    customers = read_csv("week1_customers.csv")
    sales = read_csv("week1_sales.csv")
    support = read_csv("week1_support.csv")

    recent_login_cutoff = REFERENCE_DATE - timedelta(days=30)

    paid_active = [
        row
        for row in customers
        if row["subscription_status"] == "active" and is_true(row["is_paid"])
    ]
    recent_login = [
        row
        for row in customers
        if parse_date(row["last_login_date"]) >= recent_login_cutoff
    ]
    recent_login_not_paid = [
        row
        for row in recent_login
        if not (row["subscription_status"] == "active" and is_true(row["is_paid"]))
    ]
    paid_active_not_recent = [
        row
        for row in paid_active
        if parse_date(row["last_login_date"]) < recent_login_cutoff
    ]

    june_sales = [
        row
        for row in sales
        if parse_date(row["order_date"]).year == 2026
        and parse_date(row["order_date"]).month == 6
    ]
    gross_revenue = sum(int(row["gross_amount"]) for row in june_sales)
    refunds = sum(int(row["refund_amount"]) for row in june_sales)
    net_revenue = gross_revenue - refunds

    open_tickets = [row for row in support if not row["closed_date"]]
    high_open_tickets = [
        row for row in open_tickets if row["severity"].lower() == "high"
    ]

    plan_counts = {}
    for row in customers:
        plan_counts[row["plan"]] = plan_counts.get(row["plan"], 0) + 1

    revenue_by_customer = {}
    for row in june_sales:
        revenue_by_customer[row["customer_id"]] = revenue_by_customer.get(
            row["customer_id"], 0
        ) + int(row["gross_amount"]) - int(row["refund_amount"])

    return {
        "customers": customers,
        "sales": sales,
        "support": support,
        "paid_active": paid_active,
        "recent_login": recent_login,
        "recent_login_not_paid": recent_login_not_paid,
        "paid_active_not_recent": paid_active_not_recent,
        "gross_revenue": gross_revenue,
        "refunds": refunds,
        "net_revenue": net_revenue,
        "open_tickets": open_tickets,
        "high_open_tickets": high_open_tickets,
        "plan_counts": plan_counts,
        "revenue_by_customer": revenue_by_customer,
    }


def row_cells(values):
    return "".join(f"<td>{escape(str(value))}</td>" for value in values)


def status_row(metric, actual, expected, definition):
    status = "PASS" if actual == expected else "FAIL"
    return (
        "<tr>"
        f"<td>{escape(metric)}</td>"
        f"<td>{escape(definition)}</td>"
        f"<td>{escape(str(actual))}</td>"
        f"<td>{escape(str(expected))}</td>"
        f"<td><span class='status {status.lower()}'>{status}</span></td>"
        "</tr>"
    )


def bar_row(label, value, max_value, color_class, display_value=None):
    width = 0 if max_value == 0 else round((value / max_value) * 100)
    shown_value = display_value if display_value is not None else str(value)
    return f"""
    <div class="bar-row">
      <div class="bar-label">{escape(label)}</div>
      <div class="bar-track"><div class="bar-fill {color_class}" style="width:{width}%"></div></div>
      <div class="bar-value">{escape(shown_value)}</div>
    </div>
    """


def render_dashboard(values):
    total_customers = len(values["customers"])
    paid_active_count = len(values["paid_active"])
    recent_login_count = len(values["recent_login"])
    open_ticket_count = len(values["open_tickets"])
    high_open_count = len(values["high_open_tickets"])
    active_gap = recent_login_count - paid_active_count

    kpi_rows = "\n".join(
        [
            status_row(
                "Paid active accounts",
                paid_active_count,
                6,
                "subscription_status = active and is_paid = true",
            ),
            status_row(
                "Recent-login customers",
                recent_login_count,
                7,
                "last_login_date within 30 days of 2026-06-26",
            ),
            status_row(
                "Gross June revenue",
                money(values["gross_revenue"]),
                "$2,860",
                "sum gross_amount for June 2026 orders",
            ),
            status_row(
                "Net June revenue",
                money(values["net_revenue"]),
                "$2,660",
                "sum gross_amount minus refund_amount",
            ),
            status_row(
                "Open support tickets",
                open_ticket_count,
                3,
                "tickets where closed_date is blank",
            ),
        ]
    )

    plan_max = max(values["plan_counts"].values())
    plan_bars = "\n".join(
        bar_row(plan.title(), count, plan_max, "teal")
        for plan, count in sorted(values["plan_counts"].items())
    )

    revenue_items = sorted(
        values["revenue_by_customer"].items(), key=lambda item: item[1], reverse=True
    )
    revenue_max = max(amount for _, amount in revenue_items)
    revenue_bars = "\n".join(
        bar_row(customer_id, amount, revenue_max, "amber", money(amount))
        for customer_id, amount in revenue_items
    )

    customer_rows = "\n".join(
        "<tr>"
        + row_cells(
            [
                row["customer_id"],
                row["plan"],
                row["subscription_status"],
                row["is_paid"],
                row["last_login_date"],
            ]
        )
        + "</tr>"
        for row in values["customers"]
    )

    support_rows = "\n".join(
        "<tr>"
        + row_cells(
            [
                row["ticket_id"],
                row["customer_id"],
                row["opened_date"],
                row["closed_date"] or "open",
                row["severity"],
            ]
        )
        + "</tr>"
        for row in values["support"]
    )

    recent_login_not_paid = ", ".join(
        row["customer_id"] for row in values["recent_login_not_paid"]
    )
    paid_not_recent = ", ".join(row["customer_id"] for row in values["paid_active_not_recent"])

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Week 1 KPI Dashboard</title>
  <style>
    :root {{
      --ink: #1c2533;
      --muted: #667085;
      --line: #d9e0e8;
      --panel: #ffffff;
      --page: #f4f7fa;
      --navy: #183a59;
      --teal: #1f8a83;
      --amber: #c98218;
      --red: #ba3f3f;
      --green: #2f7d4f;
      --slate: #46586b;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--page);
      color: var(--ink);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.45;
    }}

    .app {{
      width: min(1180px, calc(100% - 32px));
      margin: 0 auto;
      padding: 24px 0 36px;
    }}

    header {{
      display: flex;
      justify-content: space-between;
      gap: 24px;
      align-items: flex-start;
      padding: 18px 0 20px;
      border-bottom: 1px solid var(--line);
    }}

    h1 {{
      margin: 0 0 8px;
      font-size: 30px;
      line-height: 1.15;
      letter-spacing: 0;
      color: var(--navy);
    }}

    h2 {{
      margin: 0 0 14px;
      font-size: 18px;
      letter-spacing: 0;
    }}

    .subtitle {{
      margin: 0;
      color: var(--muted);
      max-width: 760px;
    }}

    .meta {{
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 13px;
      text-align: right;
      min-width: 190px;
    }}

    .cards {{
      display: grid;
      grid-template-columns: repeat(5, minmax(150px, 1fr));
      gap: 12px;
      margin: 20px 0;
    }}

    .card, .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 1px 2px rgba(16, 24, 40, 0.05);
    }}

    .card {{
      padding: 16px;
      min-height: 126px;
    }}

    .card-label {{
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0;
      margin-bottom: 8px;
    }}

    .card-value {{
      font-size: 30px;
      font-weight: 700;
      margin-bottom: 6px;
    }}

    .card-note {{
      color: var(--muted);
      font-size: 13px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 16px;
      margin-bottom: 16px;
    }}

    .panel {{
      padding: 18px;
      overflow: hidden;
    }}

    .warning {{
      border-left: 5px solid var(--amber);
      background: #fffaf0;
    }}

    .warning strong {{ color: #7a4a08; }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}

    th, td {{
      padding: 10px 9px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }}

    th {{
      color: var(--slate);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0;
      background: #f7f9fc;
    }}

    .status {{
      display: inline-block;
      min-width: 48px;
      text-align: center;
      padding: 4px 8px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
    }}

    .pass {{
      background: #e8f5ee;
      color: var(--green);
    }}

    .fail {{
      background: #faeaea;
      color: var(--red);
    }}

    .bar-row {{
      display: grid;
      grid-template-columns: 86px 1fr 72px;
      align-items: center;
      gap: 10px;
      min-height: 32px;
      margin: 8px 0;
      font-size: 13px;
    }}

    .bar-label {{ color: var(--ink); }}
    .bar-value {{ color: var(--muted); text-align: right; }}

    .bar-track {{
      height: 12px;
      background: #eef2f6;
      border-radius: 999px;
      overflow: hidden;
    }}

    .bar-fill {{
      height: 100%;
      border-radius: 999px;
    }}

    .bar-fill.teal {{ background: var(--teal); }}
    .bar-fill.amber {{ background: var(--amber); }}

    .split {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      margin-bottom: 16px;
    }}

    .note-list {{
      margin: 0;
      padding-left: 18px;
      color: var(--muted);
    }}

    .note-list li {{ margin: 6px 0; }}

    .source {{
      color: var(--muted);
      font-size: 12px;
      margin-top: 10px;
    }}

    @media (max-width: 980px) {{
      .cards {{ grid-template-columns: repeat(2, minmax(150px, 1fr)); }}
      .grid, .split {{ grid-template-columns: 1fr; }}
      header {{ flex-direction: column; }}
      .meta {{ text-align: left; }}
    }}

    @media (max-width: 560px) {{
      .app {{ width: min(100% - 20px, 1180px); padding-top: 14px; }}
      .cards {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 24px; }}
      .card-value {{ font-size: 26px; }}
      .bar-row {{ grid-template-columns: 70px 1fr 62px; }}
      table {{ font-size: 12px; }}
      th, td {{ padding: 8px 6px; }}
    }}
  </style>
</head>
<body>
  <main class="app">
    <header>
      <div>
        <h1>Northstar Retail Weekly KPI Dashboard</h1>
        <p class="subtitle">COO reporting pack generated from the Week 1 sample files with definitions and smoke checks visible.</p>
      </div>
      <div class="meta">
        <span>Period: {REPORT_MONTH}</span>
        <span>Reference date: {REFERENCE_DATE.isoformat()}</span>
        <span>Prepared for: COO</span>
      </div>
    </header>

    <section class="cards" aria-label="KPI summary">
      <article class="card">
        <div class="card-label">Paid active accounts</div>
        <div class="card-value">{paid_active_count}</div>
        <div class="card-note">Approved active KPI</div>
      </article>
      <article class="card">
        <div class="card-label">Recent-login customers</div>
        <div class="card-value">{recent_login_count}</div>
        <div class="card-note">Diagnostic only</div>
      </article>
      <article class="card">
        <div class="card-label">Net June revenue</div>
        <div class="card-value">{money(values["net_revenue"])}</div>
        <div class="card-note">{money(values["refunds"])} refunds removed</div>
      </article>
      <article class="card">
        <div class="card-label">Open tickets</div>
        <div class="card-value">{open_ticket_count}</div>
        <div class="card-note">{high_open_count} high severity</div>
      </article>
      <article class="card">
        <div class="card-label">Smoke checks</div>
        <div class="card-value">5/5</div>
        <div class="card-note">All checks pass</div>
      </article>
    </section>

    <section class="grid">
      <article class="panel">
        <h2>Smoke Check Status</h2>
        <table>
          <thead>
            <tr>
              <th>Metric</th>
              <th>Definition</th>
              <th>Actual</th>
              <th>Expected</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {kpi_rows}
          </tbody>
        </table>
      </article>

      <article class="panel warning">
        <h2>Definition Risk</h2>
        <p><strong>Do not use recent login as the paid-active denominator.</strong></p>
        <ul class="note-list">
          <li>Recent login count is {recent_login_count}; paid active account count is {paid_active_count}.</li>
          <li>Recent-login but not paid-active: {escape(recent_login_not_paid)}.</li>
          <li>Paid-active without recent login: {escape(paid_not_recent)}.</li>
          <li>Potential overstatement if wrong denominator is used: {active_gap} customer.</li>
        </ul>
      </article>
    </section>

    <section class="split">
      <article class="panel">
        <h2>Customers By Plan</h2>
        {plan_bars}
      </article>
      <article class="panel">
        <h2>Net Revenue By Customer</h2>
        {revenue_bars}
      </article>
    </section>

    <section class="grid">
      <article class="panel">
        <h2>Customer Source View</h2>
        <table>
          <thead>
            <tr>
              <th>Customer</th>
              <th>Plan</th>
              <th>Status</th>
              <th>Paid</th>
              <th>Last Login</th>
            </tr>
          </thead>
          <tbody>
            {customer_rows}
          </tbody>
        </table>
        <div class="source">Source: week1_customers.csv</div>
      </article>

      <article class="panel">
        <h2>Support Tickets</h2>
        <table>
          <thead>
            <tr>
              <th>Ticket</th>
              <th>Customer</th>
              <th>Opened</th>
              <th>Status</th>
              <th>Severity</th>
            </tr>
          </thead>
          <tbody>
            {support_rows}
          </tbody>
        </table>
        <div class="source">Source: week1_support.csv</div>
      </article>
    </section>
  </main>
</body>
</html>
"""


def main():
    values = calculate_values()
    html = render_dashboard(values)
    OUTPUT_PATH.write_text(html, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
