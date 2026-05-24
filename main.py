# main.py

from ui import create_ui
from logic import feet_to_meters


def calculate(ui):
    try:
        feet = float(ui["feet_var"].get())
        meters = feet_to_meters(feet)
        ui["meters_var"].set(meters)
    except ValueError:
        ui["meters_var"].set("Invalid input")


def main():
    ui = create_ui()

    # Botón
    ui["calculate_button"].configure(
        command=lambda: calculate(ui)
    )

    # Tecla Enter
    ui["feet_entry"].bind(
        "<Return>",
        lambda event: calculate(ui)
    )

    ui["root"].mainloop()


if __name__ == "__main__":
    main()