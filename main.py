import flet as ft

def main(page: ft.Page):
    page.title = "Neon Calculator"
    page.bgcolor = "#0B0C10"
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False
    
    # Calculator display window with a cyan neon glow border
    display = ft.Text(value="0", color="#66FCF1", size=38, text_align=ft.TextAlign.RIGHT)
    
    def btn_click(e):
        data = e.control.text
        if data == "C":
            display.value = "0"
        elif data == "=":
            try:
                # Handle standard math symbols
                expr = display.value.replace("×", "*").replace("÷", "/")
                display.value = str(eval(expr))
            except:
                display.value = "Error"
        else:
            if display.value == "0" or display.value == "Error":
                display.value = data
            else:
                display.value += data
        page.update()

    # Helper function to generate styled neon buttons
    def neon_button(text, color="#45A29E"):
        return ft.Container(
            content=ft.TextButton(
                text=text,
                on_click=btn_click,
                style=ft.ButtonStyle(
                    color=color,
                    text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD),
                ),
            ),
            alignment=ft.alignment.center,
            bgcolor="#1F2833",
            border=ft.border.all(1, color),
            border_radius=8,
            expand=1,
            height=60
        )

    # Building the interface layout
    page.add(
        ft.Container(
            content=display,
            alignment=ft.alignment.center_right,
            padding=15,
            bgcolor="#1F2833",
            border=ft.border.all(2, "#66FCF1"),
            border_radius=10,
            margin=ft.margin.only(bottom=15, top=10)
        ),
        ft.Column(
            controls=[
                ft.Row(controls=[neon_button("C", "#FF007F"), neon_button("÷", "#66FCF1"), neon_button("×", "#66FCF1"), neon_button("-", "#66FCF1")]),
                ft.Row(controls=[neon_button("7"), neon_button("8"), neon_button("9"), neon_button("+", "#66FCF1")]),
                ft.Row(controls=[neon_button("4"), neon_button("5"), neon_button("6")]),
                ft.Row(controls=[neon_button("1"), neon_button("2"), neon_button("3")]),
                ft.Row(controls=[neon_button("0"), neon_button("."), neon_button("=", "#00FF66")]),
            ],
            spacing=10
        )
    )

ft.app(target=main)
