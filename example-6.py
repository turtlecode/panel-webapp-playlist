import panel as pn

pn.extension()

# Checkbox widget
newsletter_checkbox = pn.widgets.Checkbox(
    name="Subscribe to newsletter",
    value=False
)

# Toggle switch widget
dark_mode_toggle = pn.widgets.Toggle(
    name="Dark Mode",
    value=False,
    button_type="primary"
)

# Output area
output = pn.pane.Markdown("Make a selection above to see a response.")

# Update function
def update_output(event):
    newsletter = newsletter_checkbox.value
    dark_mode = dark_mode_toggle.value

    message = "### Your Preferences:\n\n"

    if newsletter:
        message += "✔️ You are subscribed to the newsletter.\n"
    else:
        message += "❌ You are NOT subscribed to the newsletter.\n"

    if dark_mode:
        message += "🌙 Dark mode is ON."
    else:
        message += "☀️ Dark mode is OFF."

    output.object = message

# Watch both widgets
newsletter_checkbox.param.watch(update_output, "value")
dark_mode_toggle.param.watch(update_output, "value")

# Layout
app = pn.Column(
    "# ✅ Checkbox & Toggle Example",
    "Select your preferences below.",
    newsletter_checkbox,
    dark_mode_toggle,
    output
)

app.servable()
