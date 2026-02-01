import panel as pn

pn.extension()

# Define colors mapping to button types
color_map = {
    "Red": "danger",
    "Green": "success",
    "Blue": "primary",
    "Yellow": "warning"
}

# RadioButtonGroup
favorite_color = pn.widgets.RadioButtonGroup(
    name="Choose Your Favorite Color",
    options=list(color_map.keys()),
    button_type="default"  # initial style
)

# Output area
output = pn.pane.Markdown("Select a color and all buttons will change to that color!")

# Callback function
def change_button_color(event):
    selected = favorite_color.value
    # Update button_type for all buttons
    favorite_color.button_type = color_map[selected]
    output.object = f"🎨 All buttons are now **{selected}**!"

# Watch for changes
favorite_color.param.watch(change_button_color, 'value')

# Layout
app = pn.Column(
    "# 🌈 Dynamic Color Buttons",
    "Click a button and all buttons change color:",
    favorite_color,
    output
)

app.servable()
