# employee_analysis.py
# Email: 23f1001029@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Frequency count for Marketing
marketing_count = (df["department"] == "Marketing").sum()
print("Marketing Department Count:", marketing_count)

# Histogram of department distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="department", palette="viridis")
plt.title("Employee Distribution by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("department_distribution.png")

# Save code + visualization to HTML
with open("employee_analysis.html", "w") as f:
    f.write("<h2>Employee Analysis Report</h2>")
    f.write("<p><b>Email:</b> 23f1001029@ds.study.iitm.ac.in</p>")
    f.write("<pre><code>")
    with open(__file__, "r") as code_file:
        f.write(code_file.read())
    f.write("</code></pre>")
    f.write("<h3>Visualization</h3>")
    f.write('<img src="department_distribution.png" width="600">')
