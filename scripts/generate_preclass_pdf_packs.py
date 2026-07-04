from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "PDFs" / "Pre_Class_Briefs"
DOC_DIR = ROOT / "PDFs" / "Documents"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.58 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN


PALETTE = {
    "navy": colors.HexColor("#17324D"),
    "blue": colors.HexColor("#2B6CB0"),
    "teal": colors.HexColor("#1F8A83"),
    "green": colors.HexColor("#2F7D4F"),
    "amber": colors.HexColor("#C98218"),
    "red": colors.HexColor("#B84A4A"),
    "ink": colors.HexColor("#1F2933"),
    "muted": colors.HexColor("#667085"),
    "line": colors.HexColor("#D9E2EC"),
    "page": colors.HexColor("#F5F7FA"),
    "soft_blue": colors.HexColor("#EAF2FA"),
    "soft_teal": colors.HexColor("#E7F5F3"),
    "soft_amber": colors.HexColor("#FFF4DF"),
    "soft_red": colors.HexColor("#FCEBEC"),
    "white": colors.white,
}


WEEKS = [
    {
        "week": 1,
        "title": "Reporting Fire Drill",
        "tagline": "The Monday KPI pack is due, but the usual analyst is away.",
        "visual": "dashboard",
        "student_scene": [
            "Northstar Retail sends a weekly KPI pack to the COO. The report is due every Monday morning, but the current process depends on manual copying from several source files.",
            "The usual analyst is unavailable this week. The COO still needs a clear view of customer, revenue, and support performance.",
        ],
        "stakeholder_message": "I need the weekly numbers by 10:00. I do not need perfect slides; I need numbers I can trust.",
        "stakeholders": ["COO", "Analytics team", "Customer support lead"],
        "data": [
            ("week1_customers.csv", "Customer records, subscription status, plan type, login date, and paid status."),
            ("week1_sales.csv", "June order records, gross amount, and refund amount."),
            ("week1_support.csv", "Support ticket records, open/closed dates, and severity."),
            ("week1_metric_definitions.md", "Business definitions for the weekly KPI pack."),
        ],
        "fields": [
            "customer_id, subscription_status, plan, last_login_date, is_paid",
            "order_id, customer_id, order_date, gross_amount, refund_amount",
            "ticket_id, customer_id, opened_date, closed_date, severity",
        ],
        "questions": [
            "Which numbers would you expect in a weekly KPI pack for the COO?",
            "Which data file would you use for each number?",
            "Which words or business terms might need clarification before the report is sent?",
            "What would make you confident that a number in the report is traceable?",
            "What questions would you ask the COO before treating the report as final?",
        ],
        "bring": [
            "The Week 1 data files.",
            "One or two questions about field meanings.",
            "A short list of the KPI numbers you think the COO would expect.",
        ],
        "instructor": {
            "intent": "Students should arrive thinking about business definitions, source files, and traceability before they learn the agent-supervision workflow.",
            "release": "Release the student brief and the four Week 1 sample files. Do not release the exercise sheet or worked examples before class.",
            "withhold": [
                "Do not reveal the expected smoke-check values before the activity.",
                "Do not reveal the active-customer denominator trap.",
                "Do not show the generated dashboard or KPI report until the demonstration point.",
            ],
            "in_class_reveal": [
                "The approved active-customer KPI is paid active accounts, not recent login.",
                "The known sample checks are paid active accounts 6, recent-login customers 7, gross June revenue 2860, net June revenue 2660, and open support tickets 3.",
                "The main teachable contrast is plausible output versus checked output.",
            ],
            "watch_for": [
                "Students may treat every login as active customer status.",
                "Students may report gross revenue when the stakeholder expects net revenue.",
                "Students may focus on a polished report before checking definitions.",
            ],
        },
    },
    {
        "week": 2,
        "title": "The Board Number Is Wrong",
        "tagline": "Finance and Product both have churn numbers in the board pack, and they do not match.",
        "visual": "join",
        "student_scene": [
            "Northstar Retail is preparing board materials. Finance and Product have reported different churn numbers, and both teams believe their number is reasonable.",
            "The board paper needs one number that can be explained clearly. The team must understand what each source represents before choosing what to report.",
        ],
        "stakeholder_message": "Before this goes to the board, tell me which number we should use and what it actually means.",
        "stakeholders": ["Finance lead", "Product lead", "Board secretary"],
        "data": [
            ("week2_subscriptions.csv", "Subscription plan, billing status, billing start date, and billing end date."),
            ("week2_cancellations.csv", "Cancellation request date, billing end date, and cancellation reason."),
            ("week2_product_events.csv", "Recent product activity by customer, including sessions and active feature count."),
        ],
        "fields": [
            "customer_id, plan, billing_status, billing_start, billing_end",
            "customer_id, cancel_request_date, billing_end_date, cancel_reason",
            "customer_id, last_event_date, sessions_30d, active_feature_count",
        ],
        "questions": [
            "What might Finance mean by churn?",
            "What might Product mean by churn or customer activity?",
            "Which source would you expect each team to trust most?",
            "What information would you want before choosing one number for the board paper?",
            "What could make two reasonable teams report different numbers?",
        ],
        "bring": [
            "The three Week 2 data files.",
            "A short description of what each file appears to represent.",
            "Two questions you would ask Finance or Product before using the number.",
        ],
        "instructor": {
            "intent": "Students should enter class aware that different operational systems can produce different but defensible business views.",
            "release": "Release only the student brief and the three source files. Keep reconciliation report templates and worked examples for class.",
            "withhold": [
                "Do not reveal the row-count bridge or quarantine-table language in advance.",
                "Do not reveal which customer IDs are intentionally mismatched.",
                "Do not name inner joins as the main risk before class.",
            ],
            "in_class_reveal": [
                "Subscriptions has 10 rows, cancellations has 3 rows, and product events has 9 rows.",
                "C204 appears in subscription/cancellation data but has no product event.",
                "C999 appears in product events but not in subscriptions.",
                "The teachable point is not one perfect churn number; it is the reconciliation logic.",
            ],
            "watch_for": [
                "Students may assume the largest table is the source of truth.",
                "Students may want to delete unmatched records to make a clean table.",
                "Students may miss the difference between billing churn and product inactivity.",
            ],
        },
    },
    {
        "week": 3,
        "title": "Limited Retention Budget",
        "tagline": "The business can contact only a limited number of customers.",
        "visual": "funnel",
        "student_scene": [
            "Northstar Retail wants to reduce customer churn, but the business cannot offer every customer a retention incentive.",
            "Customer Success has limited time, and each offer has a cost. The business needs a practical way to decide which customers should be reviewed first.",
        ],
        "stakeholder_message": "If we can contact only a small group, who should we prioritise and why?",
        "stakeholders": ["Customer Success manager", "Finance lead", "Retention programme owner"],
        "data": [
            ("week3_retention_training.csv", "Customer-level data about tenure, monthly fee, usage, support tickets, plan type, discounts, offer response, and next-month retention."),
        ],
        "fields": [
            "customer_id, tenure_months, monthly_fee, usage_sessions_30d",
            "support_tickets_90d, plan_type, discount_last_90d",
            "post_offer_response, retained_next_month",
        ],
        "questions": [
            "What does the business need to decide?",
            "Which fields might indicate that a customer needs attention?",
            "Which fields might indicate that a customer is valuable to retain?",
            "What would make a simple prioritisation rule acceptable to a business stakeholder?",
            "What could go wrong if the business contacts the wrong customers?",
        ],
        "bring": [
            "The Week 3 data file.",
            "One simple customer-prioritisation idea.",
            "Two questions you would ask Customer Success before acting on the data.",
        ],
        "instructor": {
            "intent": "Students should arrive with decision-policy thinking rather than model-metric thinking.",
            "release": "Release the student brief and data file. Keep leakage audit, baseline guidance, and threshold economics for class.",
            "withhold": [
                "Do not reveal the leakage columns in advance.",
                "Do not reveal the break-even calculation in the pre-class material.",
                "Do not name top-N or threshold policy language before the activity.",
            ],
            "in_class_reveal": [
                "post_offer_response is post-decision information and should not be used as a predictor.",
                "retained_next_month is the outcome, not a decision-time feature.",
                "Offer cost is 25 and expected saved margin is 120, giving a 20.8 percent break-even save rate.",
            ],
            "watch_for": [
                "Students may ask for the best model before defining the decision.",
                "Students may use outcome or post-offer fields because they look useful.",
                "Students may ignore capacity and cost.",
            ],
        },
    },
    {
        "week": 4,
        "title": "From Notebook To Tool",
        "tagline": "Operations wants something usable, not a notebook that only one analyst can run.",
        "visual": "tool",
        "student_scene": [
            "Northstar Retail has analysis that may help Customer Success prioritise customers.",
            "Operations is interested, but they do not want to depend on an analyst manually running a notebook each time a decision is needed.",
        ],
        "stakeholder_message": "Can someone on my team use this safely without asking the analyst to run it?",
        "stakeholders": ["Operations manager", "Customer Success team", "Analytics team"],
        "data": [
            ("Week 3 decision context", "Customer-prioritisation logic or notes from the previous week."),
            ("Suggested request format", "Customer ID, tenure, fee, usage, support tickets, and plan type."),
        ],
        "fields": [
            "customer_id, tenure_months, monthly_fee",
            "usage_sessions_30d, support_tickets_90d, plan_type",
        ],
        "questions": [
            "Who would use this internal tool or process?",
            "What information would the user need to provide?",
            "What output would be useful to the user?",
            "What could make a tool confusing or risky for an operations user?",
            "What instructions would someone need if the original analyst is unavailable?",
        ],
        "bring": [
            "Your Week 3 prioritisation idea or notes.",
            "A sketch of what an operations user would enter.",
            "A sketch of what the user should receive back.",
            "Two questions you would ask Operations before releasing an internal tool.",
        ],
        "instructor": {
            "intent": "Students should arrive thinking about user needs, inputs, outputs, and operational handoff.",
            "release": "Release the student brief only. Keep input-contract templates, bad-input tests, and runbook examples for class.",
            "withhold": [
                "Do not reveal the specific validation rules in advance.",
                "Do not reveal the handoff-test structure.",
                "Do not show the runbook template before the exercise begins.",
            ],
            "in_class_reveal": [
                "The internal tool must reject missing customer_id, negative tenure, unknown plan type, and missing usage/support data.",
                "A tool is not ready simply because a happy-path request works.",
                "The operating evidence is the input contract, bad-request behaviour, tests, and runbook.",
            ],
            "watch_for": [
                "Students may design a dashboard without defining who uses it.",
                "Students may ignore bad or missing input.",
                "Students may assume the original author will always operate the tool.",
            ],
        },
    },
    {
        "week": 5,
        "title": "The Executive Question",
        "tagline": "The CEO wants to know why churn changed in June.",
        "visual": "sources",
        "student_scene": [
            "The CEO asks why churn changed in June. A useful answer must be clear, evidence-based, and careful about uncertainty.",
            "Northstar has several internal notes and summaries that may help answer the question.",
        ],
        "stakeholder_message": "Give me the short version, but make sure we are not overstating the evidence.",
        "stakeholders": ["CEO", "Analytics lead", "Customer Success lead", "Product lead"],
        "data": [
            ("week5_knowledge_base.md", "Short internal source notes about churn, pricing, support, product incidents, and marketing activity."),
        ],
        "fields": [
            "KPI Pack",
            "Pricing Note",
            "Support Summary",
            "Product Incident Note",
            "Marketing Campaign Note",
        ],
        "questions": [
            "What does the CEO likely want to know?",
            "Which source notes seem most relevant to the question?",
            "What would make an executive answer convincing?",
            "What would make an executive answer risky?",
            "What follow-up analysis might be needed before making a stronger claim?",
        ],
        "bring": [
            "The Week 5 source note.",
            "A short draft answer to: Why did churn rise in June?",
            "Two places where you think the available evidence is strong or weak.",
        ],
        "instructor": {
            "intent": "Students should arrive with a first executive explanation and a sense of uncertainty, before learning the evaluation harness.",
            "release": "Release the student brief and the knowledge base only. Keep evaluation cases for class.",
            "withhold": [
                "Do not release week5_eval_cases.csv before class.",
                "Do not pre-teach citation support checks.",
                "Do not identify the refusal cases before the activity.",
            ],
            "in_class_reveal": [
                "The evidence supports the observed churn pattern and a plausible onboarding-friction investigation.",
                "The evidence does not support a confident causal claim that the May price change caused June churn.",
                "The campaign started too late to support a full-month June churn claim.",
            ],
            "watch_for": [
                "Students may mistake a source mention for evidence support.",
                "Students may use causal language too quickly.",
                "Students may write a fluent answer without naming uncertainty.",
            ],
        },
    },
    {
        "week": 6,
        "title": "Launch Review",
        "tagline": "The launch committee wants a recommendation, not a feature tour.",
        "visual": "launch",
        "student_scene": [
            "Northstar Retail is considering whether the analytics work from the previous weeks is ready for use beyond the classroom setting.",
            "The launch committee wants to know what is ready, what is not ready, what evidence exists, and who would own follow-up actions.",
        ],
        "stakeholder_message": "What can go live, what should wait, and who owns it if something goes wrong?",
        "stakeholders": ["Launch committee", "Analytics lead", "Operations manager", "Customer Success manager", "Executive sponsor"],
        "data": [
            ("Week 1 reporting work", "KPI reporting artefact, definitions, and checks."),
            ("Week 2 reconciliation work", "Notes on conflicting numbers and source comparison."),
            ("Week 3 retention work", "Customer-prioritisation or decision notes."),
            ("Week 4 internal tool work", "Notes on user inputs, outputs, and operating needs."),
            ("Week 5 executive answer work", "Evidence-based answer and source notes."),
        ],
        "fields": [
            "Weekly artefacts and notes",
            "Evidence gathered across the course",
            "Questions, risks, and unresolved decisions",
        ],
        "questions": [
            "Which part of your work is most ready to use?",
            "Which part still needs more evidence?",
            "Who would own the work if it were used after class?",
            "What should stop the team from releasing something too broadly?",
            "What would you say if a stakeholder asks for a stronger claim than the evidence supports?",
        ],
        "bring": [
            "Your weekly artefacts or notes from Weeks 1-5.",
            "One claim you feel confident defending.",
            "One claim you are not yet confident defending.",
            "Two questions you expect the launch committee to ask.",
        ],
        "instructor": {
            "intent": "Students should arrive with evidence and judgement, not just demo material.",
            "release": "Release the student brief only. Keep launch checklist, incident injects, and viva prompts for class.",
            "withhold": [
                "Do not reveal the incident injects before class.",
                "Do not release the launch checklist as a completed structure.",
                "Do not frame full launch as the expected answer.",
            ],
            "in_class_reveal": [
                "A limited pilot or no-ship recommendation can be strong if evidence and ownership are clear.",
                "Incident response should pause, narrow, or redirect the launch claim when evidence fails.",
                "The final defence is about scope, owner, evidence, and no-ship conditions.",
            ],
            "watch_for": [
                "Students may turn the session into a feature tour.",
                "Students may hide weak evidence instead of scoping the recommendation.",
                "Students may name the system or agent as owner rather than a human role.",
            ],
        },
    },
]


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=30,
            alignment=TA_CENTER,
            textColor=PALETTE["navy"],
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSub",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            textColor=PALETTE["muted"],
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="WeekTitle",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=23,
            textColor=PALETTE["navy"],
            spaceBefore=4,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=PALETTE["navy"],
            spaceBefore=9,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodySmall",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.3,
            textColor=PALETTE["ink"],
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Muted",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.6,
            leading=11.2,
            textColor=PALETTE["muted"],
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Question",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            leftIndent=18,
            firstLineIndent=-12,
            textColor=PALETTE["ink"],
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCell",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.8,
            leading=9.8,
            textColor=PALETTE["ink"],
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeader",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.8,
            leading=9.8,
            textColor=PALETTE["white"],
        )
    )
    return styles


STYLES = make_styles()


def p(text, style="BodySmall"):
    return Paragraph(text, STYLES[style])


def bullet_list(items, style="BodySmall"):
    flows = []
    for item in items:
        flows.append(Paragraph(item, STYLES["Question"], bulletText="-"))
    return flows


def numbered_list(items):
    flows = []
    for i, item in enumerate(items, 1):
        flows.append(Paragraph(item, STYLES["Question"], bulletText=f"{i}."))
    return flows


class WeekVisual(Flowable):
    def __init__(self, kind, width=CONTENT_WIDTH, height=116, audience="student"):
        super().__init__()
        self.kind = kind
        self.width = width
        self.height = height
        self.audience = audience

    def draw(self):
        c = self.canv
        w = self.width
        h = self.height
        c.saveState()
        bg = PALETTE["soft_blue"] if self.audience == "student" else PALETTE["soft_amber"]
        accent = PALETTE["teal"] if self.audience == "student" else PALETTE["amber"]
        c.setFillColor(bg)
        c.setStrokeColor(PALETTE["line"])
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=1)
        c.setStrokeColor(accent)
        c.setLineWidth(2)

        if self.kind == "dashboard":
            self._dashboard(c, w, h, accent)
        elif self.kind == "join":
            self._join(c, w, h, accent)
        elif self.kind == "funnel":
            self._funnel(c, w, h, accent)
        elif self.kind == "tool":
            self._tool(c, w, h, accent)
        elif self.kind == "sources":
            self._sources(c, w, h, accent)
        else:
            self._launch(c, w, h, accent)
        c.restoreState()

    def _label(self, c, text, x, y, size=8):
        c.setFillColor(PALETTE["muted"])
        c.setFont("Helvetica", size)
        c.drawString(x, y, text)

    def _dashboard(self, c, w, h, accent):
        labels = ["Customers", "Revenue", "Tickets"]
        values = ["?", "$?", "?"] if self.audience == "student" else ["6", "$2.66k", "3"]
        for i in range(3):
            x = 20 + i * ((w - 60) / 3)
            c.setFillColor(PALETTE["white"])
            c.roundRect(x, 58, 116, 36, 6, fill=1, stroke=0)
            c.setFillColor(PALETTE["navy"])
            c.setFont("Helvetica-Bold", 16)
            c.drawString(x + 10, 72, values[i])
            self._label(c, labels[i], x + 10, 62)
        for i, height in enumerate([22, 44, 30, 60, 48]):
            x = 28 + i * 18
            c.setFillColor(accent)
            c.rect(x, 18, 10, height, fill=1, stroke=0)
        label = "KPI pack awaiting source checks" if self.audience == "student" else "KPI pack with visible source checks"
        self._label(c, label, 145, 29, 10)

    def _join(self, c, w, h, accent):
        xs = [24, 180, 336]
        names = ["Billing", "Cancellations", "Product use"]
        for x, name in zip(xs, names):
            c.setFillColor(PALETTE["white"])
            c.roundRect(x, 62, 122, 28, 6, fill=1, stroke=0)
            self._label(c, name, x + 12, 73, 9)
            c.line(x + 60, 62, w / 2, 39)
        c.setFillColor(accent)
        c.roundRect(w / 2 - 62, 18, 124, 28, 6, fill=1, stroke=0)
        c.setFillColor(PALETTE["white"])
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(w / 2, 29, "Board number")

    def _funnel(self, c, w, h, accent):
        c.setFillColor(PALETTE["white"])
        c.roundRect(26, 74, w - 52, 18, 5, fill=1, stroke=0)
        c.roundRect(68, 48, w - 136, 18, 5, fill=1, stroke=0)
        c.setFillColor(accent)
        c.roundRect(125, 22, w - 250, 18, 5, fill=1, stroke=0)
        c.setFillColor(PALETTE["navy"])
        c.setFont("Helvetica-Bold", 9)
        c.drawString(38, 80, "All customers")
        c.drawString(80, 54, "Customers needing review")
        c.setFillColor(PALETTE["white"])
        c.drawCentredString(w / 2, 28, "Limited contact capacity")

    def _tool(self, c, w, h, accent):
        c.setFillColor(PALETTE["white"])
        c.roundRect(28, 30, 140, 56, 8, fill=1, stroke=0)
        c.roundRect(w - 168, 30, 140, 56, 8, fill=1, stroke=0)
        c.setFillColor(accent)
        c.roundRect(w / 2 - 58, 37, 116, 42, 8, fill=1, stroke=0)
        c.setStrokeColor(accent)
        c.line(168, 58, w / 2 - 58, 58)
        c.line(w / 2 + 58, 58, w - 168, 58)
        self._label(c, "User input", 66, 55, 10)
        c.setFillColor(PALETTE["white"])
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(w / 2, 54, "Internal tool")
        self._label(c, "Recommendation", w - 132, 55, 10)

    def _sources(self, c, w, h, accent):
        for i, name in enumerate(["KPI", "Pricing", "Support", "Incident", "Campaign"]):
            x = 24 + i * ((w - 64) / 5)
            c.setFillColor(PALETTE["white"])
            c.roundRect(x, 60, 72, 30, 5, fill=1, stroke=0)
            self._label(c, name, x + 11, 73, 8)
            c.line(x + 36, 60, w / 2, 37)
        c.setFillColor(accent)
        c.roundRect(w / 2 - 74, 16, 148, 30, 6, fill=1, stroke=0)
        c.setFillColor(PALETTE["white"])
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(w / 2, 27, "Executive answer")

    def _launch(self, c, w, h, accent):
        for i, color in enumerate([PALETTE["green"], PALETTE["amber"], PALETTE["red"]]):
            c.setFillColor(color)
            c.circle(52, 76 - i * 26, 9, fill=1, stroke=0)
        c.setFillColor(PALETTE["white"])
        c.roundRect(90, 28, w - 118, 60, 8, fill=1, stroke=0)
        self._label(c, "Evidence", 112, 67, 10)
        self._label(c, "Scope", 235, 67, 10)
        self._label(c, "Owner", 350, 67, 10)
        c.setStrokeColor(accent)
        c.line(112, 55, w - 52, 55)
        self._label(c, "Launch recommendation", 112, 38, 10)


class CoverVisual(Flowable):
    def __init__(self, audience, width=CONTENT_WIDTH, height=210):
        super().__init__()
        self.audience = audience
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        w = self.width
        h = self.height
        c.saveState()
        c.setFillColor(PALETTE["soft_teal"] if self.audience == "student" else PALETTE["soft_amber"])
        c.roundRect(0, 0, w, h, 16, fill=1, stroke=0)
        c.setStrokeColor(PALETTE["navy"])
        c.setLineWidth(2)
        c.line(18, 18, w - 18, h - 18)
        c.setFillColor(PALETTE["white"])
        for i in range(6):
            x = 28 + (i % 3) * 155
            y = 114 - (i // 3) * 72
            c.roundRect(x, y, 126, 48, 8, fill=1, stroke=0)
            c.setFillColor(PALETTE["navy"])
            c.setFont("Helvetica-Bold", 11)
            c.drawString(x + 12, y + 29, f"Week {i + 1}")
            c.setFillColor(PALETTE["teal"] if self.audience == "student" else PALETTE["amber"])
            c.rect(x + 12, y + 12, 26 + i * 9, 7, fill=1, stroke=0)
            c.setFillColor(PALETTE["white"])
        c.restoreState()


class NotesBox(Flowable):
    def __init__(self, width=CONTENT_WIDTH, height=160):
        super().__init__()
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(colors.white)
        c.setStrokeColor(PALETTE["line"])
        c.roundRect(0, 0, self.width, self.height, 8, fill=1, stroke=1)
        c.setFillColor(PALETTE["navy"])
        c.setFont("Helvetica-Bold", 10)
        c.drawString(12, self.height - 22, "Pre-class notes")
        c.setStrokeColor(PALETTE["line"])
        c.setLineWidth(0.5)
        y = self.height - 42
        while y > 16:
            c.line(12, y, self.width - 12, y)
            y -= 20
        c.restoreState()


def cover_story(title, subtitle, audience):
    if audience == "student":
        body = "Read each scenario, inspect the listed data files, and bring your own questions and assumptions to class."
    else:
        body = "Use this companion as the private teaching map for release timing, reveal points, likely misconceptions, and in-class framing."
    return [
        Spacer(1, 0.3 * inch),
        p(title, "CoverTitle"),
        p(subtitle, "CoverSub"),
        Spacer(1, 0.12 * inch),
        CoverVisual(audience),
        Spacer(1, 0.22 * inch),
        p("Northstar Retail case sequence", "Section"),
        p(body, "BodySmall"),
    ]


def section_title(text):
    return [Spacer(1, 3), p(text, "Section")]


def data_table(rows):
    data = [
        [Paragraph("File or material", STYLES["TableHeader"]), Paragraph("What it contains", STYLES["TableHeader"])]
    ]
    for left, right in rows:
        data.append([Paragraph(left, STYLES["TableCell"]), Paragraph(right, STYLES["TableCell"])])
    table = Table(data, colWidths=[1.85 * inch, CONTENT_WIDTH - 1.85 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["navy"]),
                ("GRID", (0, 0), (-1, -1), 0.25, PALETTE["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALETTE["page"]]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return [table, Spacer(1, 6)]


def stakeholder_box(text, audience):
    bg = PALETTE["soft_teal"] if audience == "student" else PALETTE["soft_amber"]
    label = "Stakeholder note" if audience == "student" else "Instructor framing"
    table = Table(
        [[Paragraph(f"<b>{label}</b><br/>{text}", STYLES["BodySmall"])]],
        colWidths=[CONTENT_WIDTH],
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("BOX", (0, 0), (-1, -1), 0.5, PALETTE["line"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return [table, Spacer(1, 6)]


def student_week_story(week, start_new_page=True):
    flows = []
    if start_new_page:
        flows.append(PageBreak())
    flows.append(p(f"Week {week['week']} - {week['title']}", "WeekTitle"))
    flows.append(p(week["tagline"], "Muted"))
    flows.append(WeekVisual(week["visual"], audience="student"))
    flows.extend(stakeholder_box(week["stakeholder_message"], "student"))
    flows.extend(section_title("Problem Context"))
    for para in week["student_scene"]:
        flows.append(p(para))
    flows.extend(section_title("People In The Room"))
    flows.extend(bullet_list(week["stakeholders"]))
    flows.extend(section_title("Data Available"))
    flows.extend(data_table(week["data"]))
    flows.extend(section_title("Fields To Notice"))
    flows.extend(bullet_list(week["fields"]))
    flows.append(
        KeepTogether(
            section_title("Bring To Class")
            + bullet_list(week["bring"])
        )
    )
    flows.extend(section_title("Pre-Class Thinking"))
    flows.extend(numbered_list(week["questions"]))
    flows.append(Spacer(1, 8))
    flows.append(NotesBox())
    return flows


def instructor_week_story(week, start_new_page=True):
    inst = week["instructor"]
    flows = []
    if start_new_page:
        flows.append(PageBreak())
    flows.append(p(f"Instructor Week {week['week']} - {week['title']}", "WeekTitle"))
    flows.append(p(week["tagline"], "Muted"))
    flows.append(WeekVisual(week["visual"], audience="instructor"))
    flows.extend(stakeholder_box(inst["intent"], "instructor"))
    flows.extend(section_title("Release Before Class"))
    flows.append(p(inst["release"]))
    flows.extend(section_title("Keep Private Until Class"))
    flows.extend(bullet_list(inst["withhold"]))
    flows.extend(section_title("In-Class Reveal Points"))
    flows.extend(bullet_list(inst["in_class_reveal"]))
    flows.extend(section_title("What To Watch For"))
    flows.extend(bullet_list(inst["watch_for"]))
    flows.extend(section_title("Student Brief Summary"))
    flows.append(p("Student-facing data/materials listed for pre-class reading:"))
    flows.extend(data_table(week["data"]))
    return flows


def footer(canvas, doc, title):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(PALETTE["muted"])
    canvas.drawString(MARGIN, 0.38 * inch, title)
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 0.38 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(path, story, title):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title=title,
    )
    doc.build(
        story,
        onFirstPage=lambda c, d: footer(c, d, title),
        onLaterPages=lambda c, d: footer(c, d, title),
    )


def build_student_pack():
    story = cover_story(
        "ANL559 Student Pre-Class Problem Briefs",
        "Realistic weekly business scenarios for preparation before class.",
        "student",
    )
    for week in WEEKS:
        story.extend(student_week_story(week, start_new_page=True))
    build_pdf(DOC_DIR / "ANL559_Student_Pre_Class_Brief_Pack.pdf", story, "ANL559 Student Pre-Class Brief Pack")


def build_instructor_pack():
    story = cover_story(
        "ANL559 Instructor Pre-Class Companion",
        "Private teaching notes for releasing student briefs and planning the in-class reveal.",
        "instructor",
    )
    for week in WEEKS:
        story.extend(instructor_week_story(week, start_new_page=True))
    build_pdf(DOC_DIR / "ANL559_Instructor_Pre_Class_Companion.pdf", story, "ANL559 Instructor Pre-Class Companion")


def build_individual_pdfs():
    for week in WEEKS:
        student_story = cover_story(
            f"Week {week['week']} Student Brief",
            week["title"],
            "student",
        )
        student_story.extend(student_week_story(week, start_new_page=True))
        build_pdf(
            OUT_DIR / f"Student_Week_{week['week']}_Pre_Class_Brief.pdf",
            student_story,
            f"Week {week['week']} Student Pre-Class Brief",
        )

        instructor_story = cover_story(
            f"Week {week['week']} Instructor Brief",
            week["title"],
            "instructor",
        )
        instructor_story.extend(instructor_week_story(week, start_new_page=True))
        build_pdf(
            OUT_DIR / f"Instructor_Week_{week['week']}_Pre_Class_Brief.pdf",
            instructor_story,
            f"Week {week['week']} Instructor Pre-Class Brief",
        )


def main():
    build_student_pack()
    build_instructor_pack()
    build_individual_pdfs()
    print(f"Wrote PDF packs to {DOC_DIR}")
    print(f"Wrote weekly PDFs to {OUT_DIR}")


if __name__ == "__main__":
    main()
