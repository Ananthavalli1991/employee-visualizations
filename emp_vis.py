"""
employee_dept_hist_report.py
Creates:
 - prints frequency count for "Marketing" department
 - an interactive department histogram (plotly)
 - an HTML report file "employee_report.html"

Verification email included in this script for submission:
23f1001029@ds.study.iitm.ac.in
"""

import pandas as pd
import plotly.express as px
import pathlib
import datetime

# ----- Replace this block with reading your real CSV file -----
# For demonstration, we'll create a DataFrame from the sample lines (first 5 rows).
sample_csv = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Finance,Europe,65.17,12,4
EMP002,Sales,Europe,93.06,11,4
EMP003,Marketing,Asia Pacific,69.51,4,4.2
EMP004,Operations,Africa,79.72,9,3.4
EMP005,HR,Europe,93.38,12,4.7
"""
# If you have a file `employees.csv`, replace the read step below accordingly.
# df = pd.read_csv("employees.csv")

from io import StringIO
df = pd.read_csv(StringIO(sample_csv))
# ---------------------------------------------------------------

# Compute department counts
dept_counts = df["department"].value_counts()
marketing_count = int((df["department"] == "Marketing").sum())

# Print frequency count for Marketing
print(f"Frequency count for 'Marketing' department: {marketing_count}")
print("\nFull department frequency distribution:")
print(dept_counts.to_string())

# Create department histogram (bar chart) using Plotly
fig = px.bar(
    x=dept_counts.index,
    y=dept_counts.values,
    labels={"x": "Department", "y": "Count"},
    title="Department Distribution (Employee Count)",
    text=dept_counts.values
)
fig.update_traces(textposition="outside")
fig.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")

# Prepare HTML report with embedded plot
out_dir = pathlib.Path(".")
html_path = out_dir / "employee_report.html"

report_html = f"""
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Employee Department Report</title>
</head>
<body>
  <h1>Employee Department Report</h1>
  <p><strong>Generated:</strong> {datetime.datetime.utcnow().isoformat()} UTC</p>
  <h2>Verification</h2>
  <p>Email for verification: <strong>23f1001029@ds.study.iitm.ac.in</strong></p>
  <h2>Frequency count for "Marketing"</h2>
  <p><strong>Marketing count:</strong> {marketing_count}</p>
  <h2>Full Department Frequency Distribution</h2>
  <pre>{dept_counts.to_string()}</pre>
  <h2>Department Distribution (interactive plot)</h2>
  <!-- Plotly chart will be embedded below -->
  <div id="plotly-div"></div>
</body>
</html>
"""

# write the base HTML
with open(html_path, "w", encoding="utf-8") as f:
    f.write(report_html)

# append the interactive plotly div/script to the HTML file (without duplicating <html> basics)
# fig.to_html returns a full HTML string; we only want the div+script part.
plotly_fragment = fig.to_html(full_html=False, include_plotlyjs="cdn")

with open(html_path, "a", encoding="utf-8") as f:
    f.write("\n<!-- Plotly chart -->\n")
    f.write(plotly_fragment)

print(f"\nHTML report saved to: {html_path.resolve()}")
print("To view: open the file in a browser or upload to a public GitHub repo and use the raw URL.")
