"""Menu Claudiney - Portal de entrada para aplicativos."""

import base64
import subprocess
import sys
import tkinter as tk

VERSION = "0.1.0"

# Ícone exit_to_app (Material Symbols) renderizado como PNG 48x48, vermelho
EXIT_ICON_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAACJ0lEQVR4nO2Y34eWQRTHP+/j"
    "7Wb7C44kRZJuorqbm2r7pRFdl35IFFFJbP/B2ohulkSy6q6rzN3qIo6oNkpSSySlSReVaIl2"
    "y/As47XleTPzvPtmPjfvmXHe88z3MeeceQYKhUJhkHSaOnprTgIXgPVAlWk9C8AsMC5Op5IJ"
    "8NacBiZpl6NNRDR9k+HNt81YE6duw2DrIvslcIQ8TAEba3tDSgHxVpsTpzNkwFsz1+/uyJWM"
    "rVHlCOqt2emtaVzhlpUAb81xYBq41oaIKmUwb80B4HqdM6FvTOYW0W3ody+yQ6P5E8+A98Ca"
    "enwKmAfOkIlO6oDemrXAfWB1NH1VnJ5r8N8ZYMviWJx2Ws8BcfoG2AF8iKbPemuuMCxVSJy+"
    "BrYDH6Pp896aiYHkgLfmV6LnXfTWzIvTS4niMYhGNuatOTTMAqaBO22X0W3/EHslcBtYFc09"
    "AA6K0x+0KUD6PLx5a1YAd3sW/xTYL06/s8yPEh3gBrC3p/ntEadfB1WFRqPhN3H66C/ul4HD"
    "0fgtsEucfiID3T4Sb5EnwNalnLw1x3q+3kIfGBWn78hElThe2PcvavsLsLtuagyFAHH6OSwaeA"
    "7sE6fhNytV6oDiNJyBNovTh7RAlSOoOA33O61QMeR0G/r9jHxHvDVLVqEEjET2QkoBoRFtqu1"
    "wb/OY/Mym3ELjtM9EMgHi9Fa4q6xv5XIm6ALwCjghTm9mfE6hUCgUCoXCf8Fvc/eOXsYrPy0A"
    "AAAASUVORK5CYII="
)

APPS = [
    {
        "label": "SoftSACI5",
        "path": r"C:\Program Files\SoftSACI5\SoftSACI5.exe",
        "color": "#E74C3C",
        "hover": "#C0392B",
    },
    {
        "label": "Rastreamento",
        "path": r"C:\Program Files\rastreamentoGeo\rastreamento_v010.exe",
        "color": "#3498DB",
        "hover": "#2980B9",
    },
    {
        "label": "ProdEstacas",
        "path": r"C:\Program Files\ProdEstacas\ProdEstacas.exe",
        "color": "#2ECC71",
        "hover": "#27AE60",
    },
    {
        "label": "Edita Imei/Apelido",
        "path": r"C:\Program Files\EditorImei\EditorImei.exe",
        "color": "#F39C12",
        "hover": "#D68910",
    },
]


def launch_app(path):
    """Executa o aplicativo selecionado."""
    try:
        subprocess.Popen([path])
    except FileNotFoundError:
        from tkinter import messagebox
        messagebox.showerror("Erro", f"Executável não encontrado:\n{path}")


def main():
    root = tk.Tk()
    root.title(f"Menu Claudiney v{VERSION}")
    root.resizable(False, False)
    root.configure(bg="#2C3E50")

    # Título
    title_frame = tk.Frame(root, bg="#2C3E50")
    title_frame.pack(pady=(20, 10))

    tk.Label(
        title_frame,
        text="Menu Claudiney",
        font=("Segoe UI", 22, "bold"),
        fg="#ECF0F1",
        bg="#2C3E50",
    ).pack()

    tk.Label(
        title_frame,
        text=f"v{VERSION}",
        font=("Segoe UI", 11),
        fg="#BDC3C7",
        bg="#2C3E50",
    ).pack()

    # Grid de botões
    btn_frame = tk.Frame(root, bg="#2C3E50")
    btn_frame.pack(padx=30, pady=(10, 25))

    btn_width = 20
    btn_height = 3

    for i, app in enumerate(APPS):
        row, col = divmod(i, 2)
        btn = tk.Button(
            btn_frame,
            text=app["label"],
            font=("Segoe UI", 12, "bold"),
            bg=app["color"],
            fg="white",
            activebackground=app["hover"],
            activeforeground="white",
            width=btn_width,
            height=btn_height,
            cursor="hand2",
            relief="flat",
            bd=0,
            command=lambda p=app["path"]: launch_app(p),
        )
        btn.grid(row=row, column=col, padx=8, pady=8)

        def on_enter(e, color=app["hover"]):
            e.widget.configure(bg=color)

        def on_leave(e, color=app["color"]):
            e.widget.configure(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Botões desabilitados - "Futura Implementação"
    for j in range(2):
        btn = tk.Button(
            btn_frame,
            text="Futura Implementação",
            font=("Segoe UI", 12),
            bg="#7F8C8D",
            fg="#BDC3C7",
            width=btn_width,
            height=btn_height,
            relief="flat",
            bd=0,
            state="disabled",
            disabledforeground="#BDC3C7",
        )
        btn.grid(row=2, column=j, padx=8, pady=8)

    # Botão de sair (ícone exit_to_app) no canto inferior direito
    exit_frame = tk.Frame(root, bg="#2C3E50")
    exit_frame.pack(fill="x", padx=30, pady=(0, 15))

    exit_icon = tk.PhotoImage(data=base64.b64decode(EXIT_ICON_B64))
    exit_btn = tk.Label(
        exit_frame,
        image=exit_icon,
        bg="#2C3E50",
        cursor="hand2",
    )
    exit_btn.image = exit_icon  # manter referência para evitar garbage collection
    exit_btn.pack(side="right")
    exit_btn.bind("<Button-1>", lambda e: root.destroy())

    # Centralizar janela na tela
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()
