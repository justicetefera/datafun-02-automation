# Data Analytics Fundamentals

## Custom Project — Military MOS to Civilian Job Mapper

### Dataset
This project uses a curated dataset of U.S. Army MOS (Military Occupational Specialty) codes.
Each record includes:

- MOS code
- Official MOS title
- Civilian job equivalents
- Average civilian salary
- Key transferable skills

The dataset is embedded directly inside the script (`app_mos_mapper.py`) as a Python list of dictionaries.
It represents a small but realistic sample of military-to-civilian transition data.

### Signals
The system generates several analytical signals from the dataset:

- **Salary Signals** — Ranking MOS codes by civilian earning potential and identifying the top three highest-paying transitions.
- **Skill Frequency Signals** — Aggregating skills across all MOS roles to determine which skills appear most often.
- **Job Frequency Signals** — Counting how often each civilian job appears across MOS roles to reveal common transition pathways.
- **Transition Signals** — Showing how military experience maps to civilian job clusters, supporting workforce and career planning.

These signals form the foundation for the project’s summaries and visualizations.

### Experiments
A series of modification experiments were conducted to enhance interpretability and automation:

- **Automated Report Generation** — Each MOS produces a standalone text report saved to `data/processed/mos_reports/`.
- **Summary File Experiments** — Salary, skill, and job summaries are generated to highlight patterns across MOS roles.
- **Visualization Experiments** — Bar charts and pie charts were created to compare salaries, skills, and job frequencies.
- **Pipeline Automation** — The `main()` function executes all 10 processing steps in sequence, producing a complete analytics pipeline.

These experiments demonstrate how structured data can be transformed into actionable insights.

### Results
Running the MOS Mapper produces:

- **Five MOS-specific reports**
- **Three summary files** (salary, skills, jobs)
- **Six visualizations** (three bar charts and three pie charts)
- **A fully automated processing pipeline** with clear logging output

All results are saved to the `data/processed/` directory, with visuals stored in `data/processed/visuals/`.

### Interpretation
The analysis reveals several key insights:

- IT-related MOS roles (e.g., 25B) show the highest civilian salary potential.
- Skills such as logistics, administration, and networking are highly transferable across MOS roles.
- Civilian job matches cluster around IT, HR, medical, and logistics fields.
- The system demonstrates how structured MOS data can be transformed into **career-ready intelligence** for transitioning service members.

This project provides a practical example of how data analytics can support veteran transition programs, workforce development, and career counseling.

Many instructions are common to all projects.
See [⭐ **Workflow: Apply Example**](https://github.com/justicetefera/datafun-02-automation)
to get this project running on your machine.

## Project Materials

- [project-instructions](./project-instructions.md)
- [mos-mapper script](../src/datafun/app_mos_mapper.py)
- [processed data](../data/processed/)
- [raw data](../data/raw/)
- [visualizations](../data/processed/visuals/)
- [tests](../tests/)
- [module](./module/index.md)
- [glossary](./glossary.md)
- [api](./api.md)
