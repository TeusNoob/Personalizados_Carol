#!/usr/bin/env python3
import os
import re
import json
import customtkinter as ctk
from tkinter import messagebox, filedialog, StringVar
from PIL import Image, ImageTk
from tkinterdnd2 import TkinterDnD, DND_FILES
import tempfile
import urllib.request

# Configuração de tema moderno
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RedirectProApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal
        self.title("RedirectPro - Gerador Avançado de Redirecionamentos")
        self.geometry("1200x800")
        self.minsize(1100, 750)
        
        # Carregar ícone
        self.load_icon()
        
        # Cores personalizáveis
        self.load_settings()
        
        # Variáveis
        self.html_base_name = self.settings.get("html_base_name", "pagina")
        self.image_base_name = self.settings.get("image_base_name", "imagem")
        self.image_ext = StringVar(value=self.settings.get("image_ext", "jpg"))
        self.output_dir_html = StringVar(value=self.settings.get("output_dir_html", "redirecionamentos"))
        self.output_dir_images = StringVar(value=self.settings.get("output_dir_images", "redirecionamentos"))
        self.accent_color = self.settings.get("accent_color", "#1e90ff")
        self.quantity = 5
        self.pages = []
        self.temp_files = []

        # Configurar janela
        self.configure(bg=self.bg_color)
        self.create_widgets()
    
    def load_icon(self):
        """Carrega o ícone do aplicativo"""
        try:
            if os.path.exists("./ico.png"):
                img = Image.open("./ico.png")
                photo = ImageTk.PhotoImage(img)
                self.iconphoto(True, photo)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

    def load_settings(self):
        """Carrega as configurações salvas"""
        self.settings = {}
        try:
            if os.path.exists("redirectpro_settings.json"):
                with open("redirectpro_settings.json", "r") as f:
                    self.settings = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")

        # Definir cores padrão
        self.bg_color = "#2b2b2b"
        self.card_color = "#3b3b3b"
        self.text_color = "#ffffff"
        self.danger_color = "#ff4500"
        self.success_color = "#32cd32"
    
    def save_settings(self):
        """Salva as configurações atuais"""
        self.settings = {
            "html_base_name": self.html_base_name,
            "image_base_name": self.image_base_name,
            "image_ext": self.image_ext.get(),
            "output_dir_html": self.output_dir_html.get(),
            "output_dir_images": self.output_dir_images.get(),
            "accent_color": self.accent_color
        }
        
        try:
            with open("redirectpro_settings.json", "w") as f:
                json.dump(self.settings, f)
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")

    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Notebook (abas)
        self.tabview = ctk.CTkTabview(main_frame, 
                                    segmented_button_selected_color=self.accent_color,
                                    segmented_button_selected_hover_color=self.lighten_color(self.accent_color))
        self.tabview.pack(fill="both", expand=True)
        
        # Abas
        self.tab_simple = self.tabview.add("Configuração Rápida")
        self.tab_advanced = self.tabview.add("Configuração Avançada")
        self.tab_settings = self.tabview.add("Configurações")
        
        self.create_simple_tab()
        self.create_advanced_tab()
        self.create_settings_tab()
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def lighten_color(self, color, amount=0.2):
        """Clareia uma cor hex em uma quantidade específica"""
        try:
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            
            lighter = []
            for component in rgb:
                lighter.append(min(255, int(component + (255 - component) * amount)))
            
            return f"#{lighter[0]:02x}{lighter[1]:02x}{lighter[2]:02x}"
        except:
            return "#4aa8ff"  # Fallback
    
    def create_settings_tab(self):
        """Cria a aba de configurações"""
        frame = ctk.CTkFrame(self.tab_settings, fg_color=self.card_color)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        title = ctk.CTkLabel(frame, 
                           text="Configurações do Aplicativo", 
                           font=ctk.CTkFont(size=18, weight="bold"),
                           text_color=self.text_color)
        title.pack(pady=(0, 20))
        
        # Formulário de configurações
        form = ctk.CTkFrame(frame, fg_color=self.card_color)
        form.pack(fill="x", padx=20, pady=10)
        
        # Cor de destaque
        ctk.CTkLabel(form, text="Cor de Destaque:", text_color=self.text_color).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_accent_color = ctk.CTkEntry(form, 
                                             fg_color="#4a4a4a", 
                                             border_color=self.accent_color,
                                             placeholder_text="Código HEX (ex: #1e90ff)")
        self.entry_accent_color.insert(0, self.accent_color)
        self.entry_accent_color.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        btn_color = ctk.CTkButton(form, text="Aplicar Cor", width=120,
                                fg_color=self.accent_color, 
                                hover_color=self.lighten_color(self.accent_color),
                                command=self.update_accent_color)
        btn_color.grid(row=0, column=2, padx=5, pady=5)
        
        # Diretório de saída HTML
        ctk.CTkLabel(form, text="Diretório HTML:", text_color=self.text_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_output_dir_html = ctk.CTkEntry(form, 
                                                fg_color="#4a4a4a", 
                                                border_color=self.accent_color)
        self.entry_output_dir_html.insert(0, self.output_dir_html.get())
        self.entry_output_dir_html.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        btn_dir_html = ctk.CTkButton(form, text="Selecionar", width=120,
                                   fg_color=self.accent_color, 
                                   hover_color=self.lighten_color(self.accent_color),
                                   command=lambda: self.select_directory(self.entry_output_dir_html))
        btn_dir_html.grid(row=1, column=2, padx=5, pady=5)
        
        # Diretório de saída Imagens
        ctk.CTkLabel(form, text="Diretório Imagens:", text_color=self.text_color).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_output_dir_images = ctk.CTkEntry(form, 
                                                 fg_color="#4a4a4a", 
                                                 border_color=self.accent_color)
        self.entry_output_dir_images.insert(0, self.output_dir_images.get())
        self.entry_output_dir_images.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        btn_dir_images = ctk.CTkButton(form, text="Selecionar", width=120,
                                     fg_color=self.accent_color, 
                                     hover_color=self.lighten_color(self.accent_color),
                                     command=lambda: self.select_directory(self.entry_output_dir_images))
        btn_dir_images.grid(row=2, column=2, padx=5, pady=5)
        
        # Botão para salvar configurações
        btn_save = ctk.CTkButton(frame, text="Salvar Configurações", 
                                fg_color=self.success_color, 
                                hover_color=self.lighten_color(self.success_color),
                                command=self.save_settings)
        btn_save.pack(pady=20)
        
        form.columnconfigure(1, weight=1)
    
    def update_accent_color(self):
        """Atualiza a cor de destaque do aplicativo"""
        new_color = self.entry_accent_color.get()
        if re.match(r'^#[0-9a-fA-F]{6}$', new_color):
            self.accent_color = new_color
            self.save_settings()
            messagebox.showinfo("Sucesso", "Cor atualizada com sucesso!\nReinicie o aplicativo para aplicar todas as mudanças.")
        else:
            messagebox.showerror("Erro", "Formato de cor inválido!\nUse o formato HEX (ex: #1e90ff)")
    
    def select_directory(self, entry_widget):
        """Seleciona um diretório e atualiza o campo correspondente"""
        dir_path = filedialog.askdirectory()
        if dir_path:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, dir_path)
    
    def create_simple_tab(self):
        frame = ctk.CTkFrame(self.tab_simple, fg_color=self.card_color)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        title = ctk.CTkLabel(frame, 
                           text="Configuração Rápida", 
                           font=ctk.CTkFont(size=18, weight="bold"),
                           text_color=self.text_color)
        title.pack(pady=(0, 20))
        
        # Formulário
        form = ctk.CTkFrame(frame, fg_color=self.card_color)
        form.pack(fill="x", padx=20, pady=10)
        
        # Nome base HTML
        ctk.CTkLabel(form, text="Nome base HTML:", text_color=self.text_color).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_html_base = ctk.CTkEntry(form, placeholder_text="Ex: meusite, landing",
                                          fg_color="#4a4a4a", border_color=self.accent_color)
        self.entry_html_base.insert(0, self.html_base_name)
        self.entry_html_base.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Nome base Imagem
        ctk.CTkLabel(form, text="Nome base Imagem:", text_color=self.text_color).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_image_base = ctk.CTkEntry(form, placeholder_text="Ex: img, foto",
                                           fg_color="#4a4a4a", border_color=self.accent_color)
        self.entry_image_base.insert(0, self.image_base_name)
        self.entry_image_base.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Extensão da imagem
        ctk.CTkLabel(form, text="Formato da imagem:", text_color=self.text_color).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.image_ext_menu = ctk.CTkOptionMenu(form, variable=self.image_ext, 
                                              values=["jpg", "png", "webp"],
                                              fg_color="#4a4a4a", button_color=self.accent_color)
        self.image_ext_menu.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Quantidade
        ctk.CTkLabel(form, text="Quantidade:", text_color=self.text_color).grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.spin_quantity = ctk.CTkOptionMenu(form, values=[str(i) for i in range(1, 101)],
                                             fg_color="#4a4a4a", button_color=self.accent_color)
        self.spin_quantity.set(str(self.quantity))
        self.spin_quantity.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        form.columnconfigure(1, weight=1)
        
        # Botão
        btn = ctk.CTkButton(frame, text="Pré-configurar na Aba Avançada", 
                           fg_color=self.accent_color, hover_color=self.lighten_color(self.accent_color),
                           command=self.prepare_advanced_tab)
        btn.pack(pady=20)
    
    def create_advanced_tab(self):
        main_frame = ctk.CTkFrame(self.tab_advanced, fg_color=self.card_color)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cabeçalho superior
        header_top = ctk.CTkFrame(main_frame, fg_color=self.card_color)
        header_top.pack(fill="x", padx=10, pady=(10, 5))
        
        # Nome base HTML
        ctk.CTkLabel(header_top, text="HTML:", text_color=self.text_color).pack(side="left", padx=(0, 5))
        self.entry_html_base_adv = ctk.CTkEntry(header_top, width=150,
                                              fg_color="#4a4a4a", border_color=self.accent_color)
        self.entry_html_base_adv.insert(0, self.html_base_name)
        self.entry_html_base_adv.pack(side="left")
        
        # Nome base Imagem
        ctk.CTkLabel(header_top, text="Imagem:", text_color=self.text_color).pack(side="left", padx=(10, 5))
        self.entry_image_base_adv = ctk.CTkEntry(header_top, width=150,
                                               fg_color="#4a4a4a", border_color=self.accent_color)
        self.entry_image_base_adv.insert(0, self.image_base_name)
        self.entry_image_base_adv.pack(side="left")
        
        # Extensão da imagem
        ctk.CTkLabel(header_top, text="Ext:", text_color=self.text_color).pack(side="left", padx=(10, 5))
        self.image_ext_menu_adv = ctk.CTkOptionMenu(header_top, variable=self.image_ext, 
                                                  values=["jpg", "png", "webp"], width=80,
                                                  fg_color="#4a4a4a", button_color=self.accent_color)
        self.image_ext_menu_adv.pack(side="left")
        
        # Botões de ação global
        action_frame = ctk.CTkFrame(header_top, fg_color="transparent")
        action_frame.pack(side="left", padx=(20, 0))
        
        btn_update = ctk.CTkButton(action_frame, text="Atualizar Nomes", width=120,
                                 fg_color=self.accent_color, hover_color=self.lighten_color(self.accent_color),
                                 command=self.update_all_names)
        btn_update.pack(side="left", padx=5)
        
        # Menu suspenso para limpeza
        btn_clear_menu = ctk.CTkButton(action_frame, text="Limpar", width=120,
                                     fg_color=self.danger_color, hover_color=self.lighten_color(self.danger_color),
                                     command=self.show_clear_menu)
        btn_clear_menu.pack(side="left", padx=5)
        
        # Cabeçalho com botões de ação
        header = ctk.CTkFrame(main_frame, fg_color=self.card_color)
        header.pack(fill="x", padx=10, pady=5)
        
        btn_add = ctk.CTkButton(header, text="+ Adicionar Página", width=150,
                              fg_color=self.accent_color, hover_color=self.lighten_color(self.accent_color),
                              command=self.add_page_card)
        btn_add.pack(side="left", padx=5)
        
        btn_import = ctk.CTkButton(header, text="Importar Links", width=150,
                                 fg_color=self.accent_color, hover_color=self.lighten_color(self.accent_color),
                                 command=self.import_links)
        btn_import.pack(side="left", padx=5)
        
        btn_generate = ctk.CTkButton(header, text="Gerar Arquivos", width=150,
                                   fg_color=self.success_color, hover_color=self.lighten_color(self.success_color),
                                   command=self.generate_files)
        btn_generate.pack(side="left", padx=5)
        
        # Área de cards com scroll e DnD
        self.canvas = ctk.CTkCanvas(main_frame, bg=self.card_color, highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color=self.card_color)
        
        # Configuração avançada do DnD
        self.scrollable_frame.drop_target_register(DND_FILES)
        self.scrollable_frame.dnd_bind('<<Drop>>', self.handle_drop)
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.sync_entries()
    
    def show_clear_menu(self):
        """Mostra um menu popup com opções de limpeza"""
        menu = ctk.CTk()
        menu.geometry("200x160")
        menu.title("Opções de Limpeza")
        menu.resizable(False, False)
        
        btn_clear_all = ctk.CTkButton(menu, text="Limpar Tudo",
                                    fg_color=self.danger_color,
                                    hover_color=self.lighten_color(self.danger_color),
                                    command=lambda: [self.clear_all(), menu.destroy()])
        btn_clear_all.pack(pady=5, padx=10, fill="x")
        
        btn_clear_images = ctk.CTkButton(menu, text="Limpar Imagens",
                                       fg_color=self.danger_color,
                                       hover_color=self.lighten_color(self.danger_color),
                                       command=lambda: [self.clear_images(), menu.destroy()])
        btn_clear_images.pack(pady=5, padx=10, fill="x")
        
        btn_clear_names = ctk.CTkButton(menu, text="Limpar Nomes",
                                      fg_color=self.danger_color,
                                      hover_color=self.lighten_color(self.danger_color),
                                      command=lambda: [self.clear_names(), menu.destroy()])
        btn_clear_names.pack(pady=5, padx=10, fill="x")
        
        btn_clear_links = ctk.CTkButton(menu, text="Limpar Links",
                                      fg_color=self.danger_color,
                                      hover_color=self.lighten_color(self.danger_color),
                                      command=lambda: [self.clear_links(), menu.destroy()])
        btn_clear_links.pack(pady=5, padx=10, fill="x")
        
        menu.mainloop()
    
    def clear_images(self):
        """Remove todas as imagens dos cards"""
        if not self.pages:
            return
            
        if not messagebox.askyesno("Confirmar", "Tem certeza que deseja remover TODAS as imagens dos cards?"):
            return
        
        for page in self.pages:
            self.remove_image(page)
    
    def clear_names(self):
        """Reseta todos os nomes dos arquivos HTML"""
        if not self.pages:
            return
            
        if not messagebox.askyesno("Confirmar", "Tem certeza que deseja resetar TODOS os nomes dos arquivos HTML?"):
            return
        
        html_base = self.entry_html_base_adv.get() or "pagina"
        
        for page in self.pages:
            page["name_entry"].delete(0, "end")
            page["name_entry"].insert(0, f"{html_base}{page['number']}.html")
    
    def clear_links(self):
        """Reseta todos os URLs"""
        if not self.pages:
            return
            
        if not messagebox.askyesno("Confirmar", "Tem certeza que deseja resetar TODOS os links de redirecionamento?"):
            return
        
        for page in self.pages:
            page["url_entry"].delete(0, "end")
            page["url_entry"].insert(0, f"https://www.site.com/{page['name_entry'].get().replace('.html', '')}")
    
    def clear_all(self):
        """Remove todos os cards e limpa tudo"""
        if not self.pages:
            return
            
        if not messagebox.askyesno("Confirmar", "Tem certeza que deseja remover TODOS os cards e configurações?"):
            return
        
        for page in self.pages[:]:
            self.remove_page_card(page["frame"])
        
        # Resetar entradas
        self.entry_html_base_adv.delete(0, "end")
        self.entry_html_base_adv.insert(0, "pagina")
        self.entry_image_base_adv.delete(0, "end")
        self.entry_image_base_adv.insert(0, "imagem")
        self.image_ext_menu_adv.set("jpg")
    
    def import_links(self):
        """Importa links de um arquivo TXT"""
        filetypes = (("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
        
        filepath = filedialog.askopenfilename(title="Selecionar Arquivo de Links", filetypes=filetypes)
        
        if not filepath:
            return
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                links = [line.strip() for line in f.readlines() if line.strip()]
            
            if not links:
                messagebox.showwarning("Aviso", "Nenhum link válido encontrado no arquivo!")
                return
            
            # Limpar tudo antes de importar
            self.clear_all()
            
            # Adicionar um card para cada link
            for i, link in enumerate(links, 1):
                self.add_page_card(
                    filename=f"{self.entry_html_base_adv.get()}{i}.html",
                    url=link,
                    image_path="",
                    index=i
                )
            
            messagebox.showinfo("Sucesso", f"{len(links)} links importados com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível importar os links:\n{str(e)}")
    
    def sync_entries(self):
        """Sincroniza as entradas entre as abas"""
        self.entry_html_base.bind("<KeyRelease>", lambda e: self.entry_html_base_adv.delete(0, "end") or self.entry_html_base_adv.insert(0, self.entry_html_base.get()))
        self.entry_html_base_adv.bind("<KeyRelease>", lambda e: self.entry_html_base.delete(0, "end") or self.entry_html_base.insert(0, self.entry_html_base_adv.get()))
        
        self.entry_image_base.bind("<KeyRelease>", lambda e: self.entry_image_base_adv.delete(0, "end") or self.entry_image_base_adv.insert(0, self.entry_image_base.get()))
        self.entry_image_base_adv.bind("<KeyRelease>", lambda e: self.entry_image_base.delete(0, "end") or self.entry_image_base.insert(0, self.entry_image_base_adv.get()))
    
    def handle_drop(self, event):
        """Manipula o evento de arrastar e soltar de qualquer origem"""
        try:
            data = event.data
            file_paths = re.findall(r'\{([^}]*)\}|(\S+)', data)
            file_paths = [f[0] or f[1] for f in file_paths if f[0] or f[1]]
            
            if not file_paths:
                return
            
            file_path = file_paths[0]
            
            if file_path.startswith(('http://', 'https://')):
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.tmp')
                temp_file.close()
                
                try:
                    urllib.request.urlretrieve(file_path, temp_file.name)
                    file_path = temp_file.name
                    self.temp_files.append(file_path)
                except Exception as e:
                    messagebox.showerror("Erro", f"Não foi possível baixar a imagem:\n{str(e)}")
                    return
            
            x, y = self.scrollable_frame.winfo_pointerxy()
            target_widget = self.scrollable_frame.winfo_containing(x, y)
            
            while target_widget and not hasattr(target_widget, 'is_card'):
                target_widget = target_widget.master
            
            if target_widget and hasattr(target_widget, 'is_card'):
                for page in self.pages:
                    if page["frame"] == target_widget:
                        self.update_card_image(page, file_path)
                        break
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao processar arquivo arrastado:\n{str(e)}")
    
    def update_card_image(self, page, file_path):
        """Atualiza a imagem de um card específico"""
        if os.path.isfile(file_path):
            try:
                Image.open(file_path).verify()
                page["image_path"] = file_path
                page["image_name_entry"].delete(0, "end")
                page["image_name_entry"].insert(0, f"{self.entry_image_base_adv.get()}{page['number']}.{self.image_ext.get()}")
                
                # Atualizar preview corretamente
                page["image_preview"].configure(text="")  # Limpa texto "Sem imagem"
                self.load_image_preview(file_path, page["image_preview"])
                page["remove_image_btn"].configure(state="normal", 
                                                fg_color=self.danger_color,
                                                hover_color=self.lighten_color(self.danger_color))
                
            except Exception as e:
                messagebox.showerror("Erro", f"Arquivo não é uma imagem válida:\n{str(e)}")
    
    def remove_image(self, page):
        """Remove a imagem de um card específico"""
        page["image_path"] = ""
        page["image_name_entry"].delete(0, "end")
        page["image_name_entry"].insert(0, f"{self.entry_image_base_adv.get()}{page['number']}.{self.image_ext.get()}")
        
        # Limpar preview completamente
        page["image_preview"].configure(image=None, text="Sem imagem", width=100, height=100)
        if hasattr(page["image_preview"], 'image'):
            del page["image_preview"].image
        
        page["remove_image_btn"].configure(state="disabled", fg_color="#555555", hover_color="#666666")
    
    def update_all_names(self):
        """Atualiza todos os nomes com as configurações atuais"""
        html_base = self.entry_html_base_adv.get() or "pagina"
        image_base = self.entry_image_base_adv.get() or "imagem"
        ext = self.image_ext.get()
        
        for page in self.pages:
            page["name_entry"].delete(0, "end")
            page["name_entry"].insert(0, f"{html_base}{page['number']}.html")
            
            if page["image_path"]:
                page["image_name_entry"].delete(0, "end")
                page["image_name_entry"].insert(0, f"{image_base}{page['number']}.{ext}")
    
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def add_page_card(self, filename="", url="", image_path="", index=None):
        page_number = index if index is not None else len(self.pages) + 1
        
        # Card principal com sombra sutil
        card = ctk.CTkFrame(self.scrollable_frame, 
                           fg_color="#3a3a3a",
                           border_color="#505050",
                           border_width=1,
                           corner_radius=8)
        card.pack(fill="x", padx=10, pady=8, ipady=8)
        card.is_card = True
        
        # Frame principal do card
        main_frame = ctk.CTkFrame(card, fg_color="transparent")
        main_frame.pack(fill="x", expand=True, padx=5, pady=5)
        
        # Número da página com estilo moderno
        label_frame = ctk.CTkFrame(main_frame, fg_color="transparent", width=80)
        label_frame.pack(side="left", padx=(5, 0))
        
        label_number = ctk.CTkLabel(label_frame, 
                                  text=f"{page_number}", 
                                  width=30,
                                  font=ctk.CTkFont(size=14, weight="bold"),
                                  text_color=self.accent_color)
        label_number.pack()
        
        # Frame dos campos editáveis
        fields_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        fields_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        # Nome do arquivo HTML
        row1 = ctk.CTkFrame(fields_frame, fg_color="transparent")
        row1.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(row1, text="HTML:", width=50, text_color=self.text_color).pack(side="left")
        entry_name = ctk.CTkEntry(row1, 
                                fg_color="#4a4a4a",
                                border_color=self.accent_color,
                                placeholder_text="nome_arquivo.html")
        entry_name.insert(0, filename or f"{self.entry_html_base_adv.get()}{page_number}.html")
        entry_name.pack(side="left", fill="x", expand=True, padx=5)
        
        # URL
        row2 = ctk.CTkFrame(fields_frame, fg_color="transparent")
        row2.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(row2, text="URL:", width=50, text_color=self.text_color).pack(side="left")
        entry_url = ctk.CTkEntry(row2, 
                               fg_color="#4a4a4a",
                               border_color=self.accent_color,
                               placeholder_text="https://...")
        entry_url.insert(0, url or f"https://www.site.com/{entry_name.get().replace('.html', '')}")
        entry_url.pack(side="left", fill="x", expand=True, padx=5)
        
        # Linha da imagem
        row3 = ctk.CTkFrame(fields_frame, fg_color="transparent")
        row3.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(row3, text="Imagem:", width=50, text_color=self.text_color).pack(side="left")
        
        # Nome da imagem
        entry_image_name = ctk.CTkEntry(row3, 
                                      fg_color="#4a4a4a",
                                      border_color=self.accent_color,
                                      placeholder_text="nome_imagem.jpg",
                                      width=150)
        entry_image_name.insert(0, f"{self.entry_image_base_adv.get()}{page_number}.{self.image_ext.get()}")
        entry_image_name.pack(side="left", padx=5)
        
        # Frame dos botões de imagem
        img_btn_frame = ctk.CTkFrame(row3, fg_color="transparent")
        img_btn_frame.pack(side="left", fill="x", expand=True)
        
        # Botão para selecionar imagem
        btn_select = ctk.CTkButton(img_btn_frame, text="Selecionar", width=90,
                                 fg_color=self.accent_color, 
                                 hover_color=self.lighten_color(self.accent_color),
                                 command=lambda: self.select_image(entry_image_name, image_preview, page_number))
        btn_select.pack(side="left", padx=2)
        
        # Botão para remover imagem
        remove_image_btn = ctk.CTkButton(img_btn_frame, text="Remover", width=90,
                                       fg_color="#555555", hover_color="#666666",
                                       state="disabled",
                                       command=lambda: self.remove_image(self.pages[-1] if index is None else next(p for p in self.pages if p["number"] == page_number)))
        remove_image_btn.pack(side="left", padx=2)
        
        # Preview da imagem (agora maior)
        preview_frame = ctk.CTkFrame(row3, fg_color="#252525", width=100, height=100, corner_radius=4)
        preview_frame.pack(side="left", padx=5)
        preview_frame.pack_propagate(False)
        
        image_preview = ctk.CTkLabel(preview_frame, text="Sem imagem", 
                                   text_color="#888888", fg_color="transparent")
        image_preview.pack(expand=True, fill="both")
        
        if image_path and os.path.exists(image_path):
            self.load_image_preview(image_path, image_preview)
            remove_image_btn.configure(state="normal", 
                                     fg_color=self.danger_color, 
                                     hover_color=self.lighten_color(self.danger_color))
        
        # Botão remover card
        btn_remove = ctk.CTkButton(main_frame, text="×", width=30, height=30,
                                 fg_color="transparent", hover_color="#ff4500",
                                 text_color="#aaaaaa", font=ctk.CTkFont(size=16),
                                 command=lambda: self.remove_page_card(card))
        btn_remove.pack(side="right", padx=5)
        
        # Armazenar referências
        page_data = {
            "frame": card,
            "label": label_number,
            "name_entry": entry_name,
            "url_entry": entry_url,
            "image_name_entry": entry_image_name,
            "image_path": image_path,
            "image_preview": image_preview,
            "remove_image_btn": remove_image_btn,
            "number": page_number
        }
        
        self.pages.append(page_data)
        
        # Retorna a referência para o novo card
        return page_data
    
    def select_image(self, entry_image_name, preview_label, page_number):
        filetypes = (("Imagens", "*.jpg *.jpeg *.png *.webp"), ("Todos os arquivos", "*.*"))
        
        filepath = filedialog.askopenfilename(title="Selecionar Imagem", filetypes=filetypes)
        
        if filepath:
            new_name = f"{self.entry_image_base_adv.get()}{page_number}.{self.image_ext.get()}"
            entry_image_name.delete(0, "end")
            entry_image_name.insert(0, new_name)
            
            for page in self.pages:
                if page["number"] == page_number:
                    page["image_path"] = filepath
                    self.load_image_preview(filepath, preview_label)
                    page["remove_image_btn"].configure(state="normal", 
                                                     fg_color=self.danger_color,
                                                     hover_color=self.lighten_color(self.danger_color))
                    break
    
    def load_image_preview(self, image_path, preview_label):
        try:
            img = Image.open(image_path)
            img.thumbnail((100, 100))
            
            # Fundo escuro para imagens com transparência
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGBA', img.size, (0x25, 0x25, 0x25, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            
            photo = ImageTk.PhotoImage(img)
            
            preview_label.configure(image=photo, text="")
            preview_label.image = photo
            
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem:\n{str(e)}")
    
    def remove_page_card(self, card):
        for page in self.pages[:]:
            if page["frame"] == card:
                card.destroy()
                self.pages.remove(page)
                break
        
        self.renumber_pages()
    
    def renumber_pages(self):
        for i, page in enumerate(self.pages, 1):
            page["number"] = i
            page["label"].configure(text=f"{i}")
            
            current_html = page["name_entry"].get()
            html_base = self.entry_html_base_adv.get() or "pagina"
            
            if current_html.startswith(html_base) and current_html[len(html_base):].split('.')[0].isdigit():
                page["name_entry"].delete(0, "end")
                page["name_entry"].insert(0, f"{html_base}{i}.html")
            
            current_image = page["image_name_entry"].get()
            image_base = self.entry_image_base_adv.get() or "imagem"
            ext = self.image_ext.get()
            
            if current_image.startswith(image_base) and current_image[len(image_base):].split('.')[0].isdigit():
                page["image_name_entry"].delete(0, "end")
                page["image_name_entry"].insert(0, f"{image_base}{i}.{ext}")
    
    def prepare_advanced_tab(self):
        try:
            self.html_base_name = self.entry_html_base.get() or "pagina"
            self.image_base_name = self.entry_image_base.get() or "imagem"
            self.quantity = int(self.spin_quantity.get())
            
            self.entry_html_base_adv.delete(0, "end")
            self.entry_html_base_adv.insert(0, self.html_base_name)
            
            self.entry_image_base_adv.delete(0, "end")
            self.entry_image_base_adv.insert(0, self.image_base_name)
            
            for page in self.pages[:]:
                self.remove_page_card(page["frame"])
            
            for i in range(1, self.quantity + 1):
                self.add_page_card(
                    filename=f"{self.html_base_name}{i}.html",
                    url=f"https://www.site.com/{self.html_base_name}{i}",
                    image_path="",
                    index=i
                )
            
            self.tabview.set("Configuração Avançada")
            
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    def generate_files(self):
        try:
            if not self.pages:
                messagebox.showerror("Erro", "Nenhuma página configurada!")
                return
            
            # Criar diretórios de saída
            os.makedirs(self.output_dir_html.get(), exist_ok=True)
            os.makedirs(self.output_dir_images.get(), exist_ok=True)
            
            generated = 0
            images_copied = 0
            
            for page in self.pages:
                # Processa HTML
                html_name = page["name_entry"].get()
                if not html_name.endswith('.html'):
                    html_name += '.html'
                
                with open(f'{self.output_dir_html.get()}/{html_name}', 'w', encoding='utf-8') as f:
                    f.write(self.generate_html_content(page["url_entry"].get()))
                generated += 1
                
                # Processa imagem
                if page["image_path"] and os.path.exists(page["image_path"]):
                    img_name = page["image_name_entry"].get()
                    ext = self.image_ext.get()
                    
                    if not img_name.lower().endswith(f'.{ext}'):
                        img_name = f"{os.path.splitext(img_name)[0]}.{ext}"
                    
                    try:
                        img = Image.open(page["image_path"])
                        
                        if ext == 'jpg':
                            if img.mode in ('RGBA', 'LA'):
                                background = Image.new('RGB', img.size, (255, 255, 255))
                                background.paste(img, mask=img.split()[-1])
                                img = background
                            img.save(f'{self.output_dir_images.get()}/{img_name}', 'JPEG', quality=90)
                        else:
                            img.save(f'{self.output_dir_images.get()}/{img_name}', ext.upper())
                        
                        images_copied += 1
                    except Exception as e:
                        messagebox.showwarning("Aviso", f"Erro ao salvar {img_name}:\n{str(e)}")
            
            msg = f"""✅ Arquivos gerados com sucesso!

• HTMLs: {generated} (em: {os.path.abspath(self.output_dir_html.get())})
• Imagens: {images_copied} ({self.image_ext.get().upper()}, em: {os.path.abspath(self.output_dir_images.get())})"""
            
            messagebox.showinfo("Sucesso", msg)
            
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    
    @staticmethod
    def generate_html_content(url):
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0;url={url}">
    <script>window.location.replace("{url}");</script>
</head>
<body style="margin:0;padding:0;background:transparent;">
</body>
</html>"""

    def on_close(self):
        """Limpa arquivos temporários ao fechar a aplicação"""
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception:
                pass
        
        self.save_settings()
        self.destroy()

if __name__ == "__main__":
    try:
        from PIL import Image
        import tkinterdnd2
    except ImportError:
        messagebox.showerror("Erro", "Dependências necessárias:\npip install pillow tkinterdnd2")
        exit()
    
    app = RedirectProApp()
    app.mainloop()