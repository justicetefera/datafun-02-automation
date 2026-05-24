"""app_mos_mapper.py - Military MOS to Civilian Job Mapper"""

# === IMPORTS ===
import logging
from pathlib import Path
import sys
import typing

import matplotlib.pyplot as plt

# === LOGGER CONFIGURATION ===
LOG = logging.getLogger("MOS")
LOG.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
LOG.addHandler(console_handler)

def log_header(logger: logging.Logger, title: str) -> None:
    """Print a formatted header for log sections."""
    logger.info("=" * 60)
    logger.info(f"{title.center(60)}")
    logger.info("=" * 60)


# === GLOBAL CONSTANTS (FIXED) ===
ROOT_DIR: typing.Final[Path] = Path(__file__).resolve().parents[2]
DATA_DIR: typing.Final[Path] = ROOT_DIR / "data"
PROCESSED_DIR: typing.Final[Path] = DATA_DIR / "processed"
MOS_REPORT_DIR: typing.Final[Path] = PROCESSED_DIR / "mos_reports"

# === LOCAL PACKAGE SETUP ===
PACKAGE_ROOT = ROOT_DIR
sys.path.append(str(PACKAGE_ROOT))

# === DATASET ===

MOS_DATA: typing.Final[list[dict]] = [
    {
        "mos": "92F",
        "title": "Petroleum Supply Specialist",
        "civilian_jobs": [
            "Fuel Technician",
            "Logistics Coordinator",
            "Supply Chain Assistant",
        ],
        "avg_salary": 48000,
        "skills": ["logistics", "inventory", "equipment operation"],
    },
    {
        "mos": "42A",
        "title": "Human Resources Specialist",
        "civilian_jobs": [
            "HR Assistant",
            "Recruiting Coordinator",
            "Office Administrator",
        ],
        "avg_salary": 52000,
        "skills": ["administration", "records management", "customer service"],
    },
    {
        "mos": "25B",
        "title": "Information Technology Specialist",
        "civilian_jobs": [
            "IT Support",
            "Systems Technician",
            "Help Desk Analyst",
        ],
        "avg_salary": 62000,
        "skills": ["networking", "security", "troubleshooting"],
    },
    {
        "mos": "68W",
            "title": "Combat Medic Specialist",
        "civilian_jobs": [
            "Medical Assistant",
            "EMT",
            "Patient Care Technician",
        ],
        "avg_salary": 45000,
        "skills": ["medical care", "triage", "patient support"],
    },
    {
        "mos": "36B",
        "title": "Financial Management Technician",
        "civilian_jobs": [
            "Accounting Clerk",
            "Budget Analyst Assistant",
            "Payroll Technician",
        ],
        "avg_salary": 54000,
        "skills": ["finance", "budgeting", "data entry"],
    },
]

# === HELPERS ===

def write_text_file(*, path: Path, content: str) -> None:
    """Write text to a file, ensuring directories exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    LOG.info(f"Wrote file: {path}")


def ensure_visual_dir() -> Path:
    """Ensure visuals directory exists."""
    visuals_dir = PROCESSED_DIR / "visuals"
    visuals_dir.mkdir(parents=True, exist_ok=True)
    return visuals_dir


# === FUNCTION 1: MOS REPORTS ===

def generate_mos_reports() -> None:
    LOG.info("FUNCTION 1: generate_mos_reports()")

    for record in MOS_DATA:
        mos = record["mos"]
        title = record["title"]
        jobs = record["civilian_jobs"]
        salary = record["avg_salary"]
        skills = record["skills"]

        filename = f"mos_{mos}.txt"
        path = MOS_REPORT_DIR / filename

        content = (
            f"=== MOS REPORT: {mos} ===\n"
            f"Title: {title}\n\n"
            f"Civilian Job Matches:\n"
            + "\n".join([f" - {job}" for job in jobs])
            + "\n\n"
            f"Average Salary: ${salary:,.0f}\n\n"
            f"Key Skills:\n"
            + "\n".join([f" - {skill}" for skill in skills])
            + "\n"
        )

        write_text_file(path=path, content=content)


# === FUNCTION 2: SALARY SUMMARY ===

def generate_salary_summary() -> None:
    LOG.info("FUNCTION 2: generate_salary_summary()")

    sorted_mos = sorted(MOS_DATA, key=lambda r: r["avg_salary"], reverse=True)
    top_three = sorted_mos[:3]

    path = PROCESSED_DIR / "mos_salary_summary.txt"

    lines = ["=== TOP 3 HIGHEST PAYING MOS TRANSITIONS ===\n"]

    for record in top_three:
        line = f"{record['mos']} - {record['title']}: ${record['avg_salary']:,.0f}"
        lines.append(line)

    write_text_file(path=path, content="\n".join(lines) + "\n")


# === FUNCTION 3: SKILL SUMMARY ===

def generate_skill_summary() -> None:
    LOG.info("FUNCTION 3: generate_skill_summary()")

    all_skills = [skill for record in MOS_DATA for skill in record["skills"]]

    skill_counts = {}
    for skill in all_skills:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

    sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

    path = PROCESSED_DIR / "mos_skill_summary.txt"

    lines = ["=== MOS SKILL FREQUENCY SUMMARY ===\n"]
    for skill, count in sorted_skills:
        lines.append(f"{skill}: {count}")

    write_text_file(path=path, content="\n".join(lines) + "\n")


# === FUNCTION 4: JOB SUMMARY ===

def generate_job_summary() -> None:
    LOG.info("FUNCTION 4: generate_job_summary()")

    all_jobs = [job for record in MOS_DATA for job in record["civilian_jobs"]]

    job_counts = {}
    for job in all_jobs:
        job_counts[job] = job_counts.get(job, 0) + 1

    sorted_jobs = sorted(job_counts.items(), key=lambda x: x[1], reverse=True)

    path = PROCESSED_DIR / "mos_job_summary.txt"

    lines = ["=== MOS CIVILIAN JOB FREQUENCY SUMMARY ===\n"]
    for job, count in sorted_jobs:
        lines.append(f"{job}: {count}")

    write_text_file(path=path, content="\n".join(lines) + "\n")


# === FUNCTION 5: SALARY BAR CHART ===

def generate_salary_chart() -> None:
    LOG.info("FUNCTION 5: generate_salary_chart()")

    mos_codes = [record["mos"] for record in MOS_DATA]
    salaries = [record["avg_salary"] for record in MOS_DATA]

    chart_path = ensure_visual_dir() / "mos_salary_chart.png"

    plt.figure(figsize=(10, 6))
    plt.bar(mos_codes, salaries, color="steelblue")
    plt.title("Average Civilian Salary by MOS", fontsize=16, fontweight="bold")
    plt.xlabel("MOS Code", fontsize=14)
    plt.ylabel("Average Salary ($)", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")


# === FUNCTION 6: SKILL BAR CHART ===

def generate_skill_chart() -> None:
    LOG.info("FUNCTION 6: generate_skill_chart()")

    all_skills = [skill for record in MOS_DATA for skill in record["skills"]]

    skill_counts = {}
    for skill in all_skills:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

    sorted_items = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

    skills = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    chart_path = ensure_visual_dir() / "mos_skill_chart.png"

    plt.figure(figsize=(12, 6))
    plt.bar(skills, counts, color="seagreen")
    plt.title("Skill Frequency Across MOS", fontsize=16, fontweight="bold")
    plt.xlabel("Skill", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")


# === FUNCTION 7: JOB BAR CHART ===

def generate_job_chart() -> None:
    LOG.info("FUNCTION 7: generate_job_chart()")

    all_jobs = [job for record in MOS_DATA for job in record["civilian_jobs"]]

    job_counts = {}
    for job in all_jobs:
        job_counts[job] = job_counts.get(job, 0) + 1

    sorted_items = sorted(job_counts.items(), key=lambda x: x[1], reverse=True)

    jobs = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    chart_path = ensure_visual_dir() / "mos_job_chart.png"

    plt.figure(figsize=(12, 6))
    plt.bar(jobs, counts, color="darkorange")
    plt.title("Civilian Job Frequency Across MOS", fontsize=16, fontweight="bold")
    plt.xlabel("Civilian Job Title", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")


# === FUNCTION 8: SALARY PIE CHART ===

def generate_salary_pie_chart() -> None:
    LOG.info("FUNCTION 8: generate_salary_pie_chart()")

    mos_codes = [record["mos"] for record in MOS_DATA]
    salaries = [record["avg_salary"] for record in MOS_DATA]

    chart_path = ensure_visual_dir() / "mos_salary_pie_chart.png"

    plt.figure(figsize=(8, 8))
    plt.pie(salaries, labels=mos_codes, autopct="%1.1f%%", startangle=140)
    plt.title("Salary Distribution Across MOS", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")


# === FUNCTION 9: SKILL PIE CHART ===

def generate_skill_pie_chart() -> None:
    LOG.info("FUNCTION 9: generate_skill_pie_chart()")

    all_skills = [skill for record in MOS_DATA for skill in record["skills"]]

    skill_counts = {}
    for skill in all_skills:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

    skills = list(skill_counts.keys())
    counts = list(skill_counts.values())

    chart_path = ensure_visual_dir() / "mos_skill_pie_chart.png"

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=skills, autopct="%1.1f%%", startangle=140)
    plt.title("Skill Frequency Distribution", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")


# === FUNCTION 10: JOB PIE CHART ===

def generate_job_pie_chart() -> None:
    LOG.info("FUNCTION 10: generate_job_pie_chart()")

    all_jobs = [job for record in MOS_DATA for job in record["civilian_jobs"]]

    job_counts = {}
    for job in all_jobs:
        job_counts[job] = job_counts.get(job, 0) + 1

    jobs = list(job_counts.keys())
    counts = list(job_counts.values())

    chart_path = ensure_visual_dir() / "mos_job_pie_chart.png"

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=jobs, autopct="%1.1f%%", startangle=140)
    plt.title("Civilian Job Frequency Distribution", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    LOG.info(f"Wrote chart: {chart_path}")

# === MAIN ===

def main() -> None:
    log_header(LOG, "MOS MAPPER")

    LOG.info("START main()")

    generate_mos_reports()
    generate_salary_summary()
    generate_skill_summary()
    generate_job_summary()
    generate_salary_chart()
    generate_skill_chart()
    generate_job_chart()
    generate_salary_pie_chart()
    generate_skill_pie_chart()
    generate_job_pie_chart()

    LOG.info("Executed successfully!")


if __name__ == "__main__":
    main()
