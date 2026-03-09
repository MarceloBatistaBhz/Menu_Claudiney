"""Menu Claudiney - Portal de entrada para aplicativos."""

import subprocess
import sys
import tkinter as tk

VERSION = "0.1.0"

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


def launch_app(path, root):
    """Executa o aplicativo selecionado e fecha o menu."""
    try:
        subprocess.Popen([path])
    except FileNotFoundError:
        tk.messagebox.showerror(
            "Erro", f"Executável não encontrado:\n{path}"
        )
        return
    root.destroy()


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
            command=lambda p=app["path"]: launch_app(p, root),
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
