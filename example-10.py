
import panel as pn

pn.extension()

# MultiSelect widget
favorite_fruits = pn.widgets.MultiSelect(
    name="Select Your Favorite Fruits",
    options=["Apple", "Banana", "Orange", "Strawberry", "Grapes"],
    size=6
)

# Output area
output = pn.pane.Markdown("Your selected fruits will appear here.")

# Callback function
def update_selection(event):
    selected = favorite_fruits.value
    if selected:
        output.object = f"🍎 You selected: **{', '.join(selected)}**"
    else:
        output.object = "You haven't selected any fruits yet."

# Watch for changes
favorite_fruits.param.watch(update_selection, "value")

# Layout
app = pn.Column(
    "# 🍇 MultiSelect Example",
    "Select one or more fruits from the list below:",
    favorite_fruits,
    output
)

app.servable()
