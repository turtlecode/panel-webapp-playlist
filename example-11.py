import panel as pn
from datetime import date

pn.extension()

# Date picker
birth_date = pn.widgets.DatePicker(
    name="Pick your birth date 📅"
)

# Output areas (side by side)
selected_date_output = pn.pane.Markdown("No date selected yet.")
age_output = pn.pane.Markdown("Age will appear here.")

# Callback function
def calculate_age(event):
    selected = birth_date.value

    if not selected:
        selected_date_output.object = "No date selected yet."
        age_output.object = "Age will appear here."
        return

    today = date.today()
    total_days = (today - selected).days

    years = total_days // 365
    remaining_days = total_days % 365

    selected_date_output.object = f"📅 You selected: **{selected}**"
    age_output.object = f"🎂 You are **{years} years {remaining_days} days** old"

# Watch for changes
birth_date.param.watch(calculate_age, "value")

# Layout (YAN YANA OUTPUT)
app = pn.Column(
    "# 🎂 Age Calculator (DatePicker)",
    "Select your birth date below:",
    birth_date,
    pn.Row(
        selected_date_output,
        age_output
    )
)

app.servable()
