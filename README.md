@"
# MOS Mapper — Military MOS to Civilian Job Translator

This project analyzes U.S. Army Military Occupational Specialty (MOS) codes and translates them into civilian career language. It takes structured MOS data—such as job titles, core duties, and required skills—and connects it to civilian job roles, salary ranges, and demand indicators. The goal is to help service members, veterans, and career counselors quickly understand how military experience maps to real-world job opportunities, what pay they might expect, and which skills are most marketable in the civilian workforce. Along the way, the project also generates visualizations and reports that make these relationships easy to explore, compare, and explain.

It is built as a modular Python package using a `src/` layout and runs inside a virtual environment managed with `uv`.

---

## Features

- Generate MOS-specific text reports (one file per MOS)
- Create salary, skill, and job frequency summaries
- Produce bar charts and pie charts using Matplotlib
- Save all outputs under `data/processed/`
- Uses structured logging for clear, readable execution output
- Runs as a module: `uv run python -m mos_mapper.app_mos_mapper`


---

## How to Run

From the project root, with the virtual environment active:
 `uv run python -m mos_mapper.app_mos_mapper`

 # Trigger CI rerun - Justice workflow test


This will:

- Generate MOS text reports in `data/processed/mos_reports/`
- Generate summary text files in `data/processed/`
- Generate charts in `data/processed/visuals/`

---

## Requirements

- Python 3.11+
- uv (recommended)
- Matplotlib
"@ | Set-Content -Path README.md
## Visual Examples

### Salary by MOS
![MOS Salary Chart](data/processed/visuals/mos_salary_chart.png)

### Salary Distribution (Pie Chart)
![MOS Salary Pie Chart](data/processed/visuals/mos_salary_pie_chart.png)

## Sample Output
2026-05-28 11:47:43,088 - INFO - ============================================================
2026-05-28 11:47:43,088 - INFO -                          MOS MAPPER
2026-05-28 11:47:43,089 - INFO - ============================================================
2026-05-28 11:47:43,089 - INFO - START main()
2026-05-28 11:47:43,089 - INFO - FUNCTION 1: generate_mos_reports()
2026-05-28 11:47:43,104 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_92F.txt
2026-05-28 11:47:43,106 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_42A.txt
2026-05-28 11:47:43,108 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_25B.txt
2026-05-28 11:47:43,109 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_68W.txt
2026-05-28 11:47:43,112 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_36B.txt
2026-05-28 11:47:43,112 - INFO - FUNCTION 2: generate_salary_summary()
2026-05-28 11:47:43,114 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_salary_summary.txt
2026-05-28 11:47:43,114 - INFO - FUNCTION 3: generate_skill_summary()
2026-05-28 11:47:43,116 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_skill_summary.txt
2026-05-28 11:47:43,116 - INFO - FUNCTION 4: generate_job_summary()
2026-05-28 11:47:43,118 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_job_summary.txt
2026-05-28 11:47:43,118 - INFO - FUNCTION 5: generate_salary_chart()
2026-05-28 11:47:47,141 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_salary_chart.png
2026-05-28 11:47:47,141 - INFO - FUNCTION 6: generate_skill_chart()
2026-05-28 11:47:47,509 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_skill_chart.png
2026-05-28 11:47:47,510 - INFO - FUNCTION 7: generate_job_chart()
2026-05-28 11:47:47,921 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_job_chart.png
2026-05-28 11:47:47,921 - INFO - FUNCTION 8: generate_salary_pie_chart()
2026-05-28 11:47:48,261 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_salary_pie_chart.png
2026-05-28 11:47:48,261 - INFO - FUNCTION 9: generate_skill_pie_chart()
2026-05-28 11:47:48,536 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_skill_pie_chart.png
2026-05-28 11:47:48,537 - INFO - FUNCTION 10: generate_job_pie_chart()
2026-05-28 11:47:48,834 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_job_pie_chart.png
2026-05-28 11:47:48,834 - INFO - Executed successfully!
2026-05-28 11:47:49,766 - INFO - ============================================================
2026-05-28 11:47:49,767 - INFO -                          MOS MAPPER
2026-05-28 11:47:49,767 - INFO - ============================================================
2026-05-28 11:47:49,767 - INFO - START main()
2026-05-28 11:47:49,767 - INFO - FUNCTION 1: generate_mos_reports()
2026-05-28 11:47:49,768 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_92F.txt
2026-05-28 11:47:49,770 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_42A.txt
2026-05-28 11:47:49,772 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_25B.txt
2026-05-28 11:47:49,774 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_68W.txt
2026-05-28 11:47:49,775 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_reports\mos_36B.txt
2026-05-28 11:47:49,776 - INFO - FUNCTION 2: generate_salary_summary()
2026-05-28 11:47:49,777 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_salary_summary.txt
2026-05-28 11:47:49,777 - INFO - FUNCTION 3: generate_skill_summary()
2026-05-28 11:47:49,779 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_skill_summary.txt
2026-05-28 11:47:49,779 - INFO - FUNCTION 4: generate_job_summary()
2026-05-28 11:47:49,780 - INFO - Wrote file: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\mos_job_summary.txt
2026-05-28 11:47:49,780 - INFO - FUNCTION 5: generate_salary_chart()
2026-05-28 11:47:50,150 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_salary_chart.png
2026-05-28 11:47:50,151 - INFO - FUNCTION 6: generate_skill_chart()
2026-05-28 11:47:50,514 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_skill_chart.png
2026-05-28 11:47:50,514 - INFO - FUNCTION 7: generate_job_chart()
2026-05-28 11:47:50,827 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_job_chart.png
2026-05-28 11:47:50,827 - INFO - FUNCTION 8: generate_salary_pie_chart()
2026-05-28 11:47:51,061 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_salary_pie_chart.png
2026-05-28 11:47:51,061 - INFO - FUNCTION 9: generate_skill_pie_chart()
2026-05-28 11:47:51,354 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_skill_pie_chart.png
2026-05-28 11:47:51,354 - INFO - FUNCTION 10: generate_job_pie_chart()
2026-05-28 11:47:51,645 - INFO - Wrote chart: C:\Users\JTEFE\Repos\datafun-02-automation\data\processed\visuals\mos_job_pie_chart.png
2026-05-28 11:47:51,645 - INFO - Executed successfully!
