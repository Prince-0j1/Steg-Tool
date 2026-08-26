import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from .core import METHODS, supported_methods, encode, decode

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StegApp — File Steganography")
        self.geometry("760x560")
        self.minsize(680,500)
        self._build()

    def _build(self):
        style=ttk.Style(self)
        try: style.theme_use("clam")
        except tk.TclError: pass
        nb=ttk.Notebook(self); nb.pack(fill="both",expand=True,padx=12,pady=12)
        self.hide=ttk.Frame(nb,padding=16); self.extract=ttk.Frame(nb,padding=16)
        nb.add(self.hide,text="Hide / Encode"); nb.add(self.extract,text="Extract / Decode")
        self._hide_tab(); self._extract_tab()

    def _hide_tab(self):
        f=self.hide
        ttk.Label(f,text="Carrier file").grid(row=0,column=0,sticky="w",pady=6)
        self.h_path=tk.StringVar()
        ttk.Entry(f,textvariable=self.h_path).grid(row=0,column=1,sticky="ew",padx=8)
        ttk.Button(f,text="Browse",command=self._browse_hide).grid(row=0,column=2)
        ttk.Label(f,text="Method").grid(row=1,column=0,sticky="w",pady=6)
        self.h_method=tk.StringVar()
        self.h_combo=ttk.Combobox(f,textvariable=self.h_method,state="readonly")
        self.h_combo.grid(row=1,column=1,sticky="ew",padx=8); self.h_combo.bind("<<ComboboxSelected>>",lambda e:self._update_method())
        ttk.Label(f,text="Secret text").grid(row=2,column=0,sticky="nw",pady=6)
        self.h_text=tk.Text(f,height=12,wrap="word"); self.h_text.grid(row=2,column=1,columnspan=2,sticky="nsew",padx=8)
        self.h_password=tk.StringVar()
        ttk.Label(f,text="Password (optional)").grid(row=3,column=0,sticky="w",pady=6)
        ttk.Entry(f,textvariable=self.h_password,show="*").grid(row=3,column=1,sticky="ew",padx=8)
        ttk.Button(f,text="Encode & Save",command=self._encode).grid(row=4,column=1,sticky="e",pady=14)
        f.columnconfigure(1,weight=1); f.rowconfigure(2,weight=1)

    def _extract_tab(self):
        f=self.extract
        ttk.Label(f,text="Stego file").grid(row=0,column=0,sticky="w",pady=6)
        self.e_path=tk.StringVar()
        ttk.Entry(f,textvariable=self.e_path).grid(row=0,column=1,sticky="ew",padx=8)
        ttk.Button(f,text="Browse",command=self._browse_extract).grid(row=0,column=2)
        ttk.Label(f,text="Method").grid(row=1,column=0,sticky="w",pady=6)
        self.e_method=tk.StringVar()
        self.e_combo=ttk.Combobox(f,textvariable=self.e_method,state="readonly",values=list(METHODS))
        self.e_combo.grid(row=1,column=1,sticky="ew",padx=8)
        self.e_password=tk.StringVar()
        ttk.Label(f,text="Password").grid(row=2,column=0,sticky="w",pady=6)
        ttk.Entry(f,textvariable=self.e_password,show="*").grid(row=2,column=1,sticky="ew",padx=8)
        ttk.Button(f,text="Extract",command=self._decode).grid(row=3,column=1,sticky="e",pady=10)
        ttk.Label(f,text="Extracted text").grid(row=4,column=0,sticky="nw",pady=6)
        self.e_text=tk.Text(f,height=14,wrap="word"); self.e_text.grid(row=4,column=1,columnspan=2,sticky="nsew",padx=8)
        ttk.Button(f,text="Copy",command=self._copy).grid(row=5,column=1,sticky="e",pady=8)
        ttk.Button(f,text="Save Text",command=self._save_text).grid(row=5,column=2,sticky="w",padx=8)
        f.columnconfigure(1,weight=1); f.rowconfigure(4,weight=1)

    def _browse_hide(self):
        p=filedialog.askopenfilename()
        if not p:return
        self.h_path.set(p)
        vals=supported_methods(p)
        self.h_combo["values"]=vals
        self.h_method.set(vals[0] if vals else "")

    def _browse_extract(self):
        p=filedialog.askopenfilename()
        if p:self.e_path.set(p)

    def _update_method(self): pass

    def _encode(self):
        p=self.h_path.get(); method=self.h_method.get(); text=self.h_text.get("1.0","end-1c")
        if not p or not method: return messagebox.showerror("Error","Select a carrier file and method.")
        out=filedialog.asksaveasfilename(initialfile=Path(p).stem+"_stego"+Path(p).suffix)
        if not out:return
        try:
            encode(p,out,text,method,self.h_password.get() or None)
            messagebox.showinfo("Success",f"Stego file saved to:\n{out}")
        except Exception as e: messagebox.showerror("Encoding failed",str(e))

    def _decode(self):
        p=self.e_path.get(); method=self.e_method.get()
        if not p or not method:return messagebox.showerror("Error","Select a file and method.")
        try:
            text=decode(p,method,self.e_password.get() or None)
            self.e_text.delete("1.0","end"); self.e_text.insert("1.0",text)
        except Exception as e: messagebox.showerror("Extraction failed",str(e))

    def _copy(self):
        text=self.e_text.get("1.0","end-1c")
        self.clipboard_clear(); self.clipboard_append(text); self.update()

    def _save_text(self):
        text=self.e_text.get("1.0","end-1c")
        if not text:return
        p=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
        if p:
            Path(p).write_text(text,encoding="utf-8")

def main():
    App().mainloop()
