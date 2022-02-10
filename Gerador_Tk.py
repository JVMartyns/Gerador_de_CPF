from tkinter import *
from tkinter import ttk
from random import randint

cor = {'preto': '#000000', 'branco': '#ffffff', 'azul1': '#5191c1', 'azul2': '#002152', 'azul3': '#001A40',
       'verde': '#00403F', 'laranja': '#0a4b75', 'vermelho': '#FF4C4C'}

estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'PA',
           'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

class App:

    def aba1(self):
        self.hide_aba2()
        self.label.configure(text='')
        self.checkbox.grid(row=3, column=0, columnspan=3, pady=10)
        self.combo.grid(row=3, column=3, pady=10)
        self.texto_do_combobox.grid(row=3, column=3, columnspan=3)
        self.label.grid(row=5, column=2, columnspan=2, pady=10)
        self.entry.grid(row=7, rowspan=2, column=1, columnspan=4)
        self.bt_gerar.grid(row=10, column=1, columnspan=2, pady=20)
        self.bt_copiar.grid(row=10, column=3, columnspan=2, pady=20)

    def aba2(self):
        self.hide_aba1()
        self.label.grid(row=3, column=2, columnspan=2, pady=10)
        self.entry.grid(row=5, rowspan=2, column=1, columnspan=4)
        self.bt_validar.grid(row=8, rowspan=2, column=2, columnspan=2, pady=10)

    def hide_aba1(self):
        self.checkbox.grid_forget()
        self.combo.grid_forget()
        self.texto_do_combobox.grid_forget()
        self.label.configure(text='')
        self.entry.grid_forget()
        self.bt_gerar.grid_forget()
        self.bt_copiar.grid_forget()

    def hide_aba2(self):
        self.label.grid_forget()
        self.entry.grid_forget()
        self.bt_validar.grid_forget()

    def gerar(self):
        if self.entry.get():
            self.entry.delete(0, END)
        self.entry.insert(END, self.gerar_cpf())
        self.label.configure(text='CPF gerado', fg=cor['branco'])

    def get_estado(self):
        estado = self.combo.get().upper()
        if estado in ['RS']:
            return '0'
        if estado in ['DF', 'GO', 'MS', 'TO']:
            return '1'
        if estado in ['PA', 'AM', 'AC', 'AP', 'RO', 'RR']:
            return '2'
        if estado in ['CE', 'MA', 'PI']:
            return '3'
        if estado in ['PE', 'RN', 'PB', 'AL']:
            return '4'
        if estado in ['BA', 'SE']:
            return '5'
        if estado in ['MG']:
            return '6'
        if estado in ['RJ', 'ES']:
            return '7'
        if estado in ['SP']:
            return '8'
        if estado in ['PR', 'SC']:
            return '9'
        if estado == 'ALEATÓRIO':
            return '10'

    def gerar_cpf(self):
        estado = '10'
        cpf = ''
        if self.combo.get():
            estado = self.get_estado()
        for c in range(0, 8):
            cpf += str(randint(0, 9))
        if int(estado) in range(0, 9):
            cpf += estado
        else:
            cpf += str(randint(0, 9))
        for c in range(2):
            soma = 0
            i = len(cpf) + 1
            for n in cpf:
                soma += int(n) * i
                i -= 1
            if (soma % 11) < 2:
                cpf += '0'
            else:
                cpf += str(11 - (soma % 11))
        if self.formatar.get():
            cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:12]
            return cpf_formatado
        else:
            return cpf

    def validar(self):
        if self.entry.get():
            cpf = self.entry.get()
            if '-' or '.' in cpf:
                cpf = self.entry.get().replace('.', '').replace('-', '')

                if self.cpf_válido(cpf):
                    self.label.configure(text='CPF Válido', fg=cor['branco'])
                else:
                    self.label.configure(text='CPF Inválido', fg=cor['vermelho'])
        else:
            self.label.configure(text='Insira um CPF', fg=cor['vermelho'])

    def cpf_válido(self, cpf):
        digito = False
        loop = 2
        d = 9
        i = 10
        for c in range(loop):
            soma = 0
            for n in cpf[:d]:
                soma += int(n) * i
                i -= 1
            if ((soma % 11) < 2 and cpf[d] == '0') or (int(cpf[d]) == (11 - (soma % 11))):
                digito = True
            else:
                digito = False
            if digito:
                loop = 3
                d = 10
                i = 11
        if digito:
            return True
        else:
            return False

    def copiar(self):
        if self.entry.get():
            root.clipboard_clear()
            root.clipboard_append(self.entry.get())
            self.label.configure(text='CPF Copiado', fg=cor['branco'])
        else:
            self.label.configure(text='Gere um CPF', fg=cor['vermelho'])

    def __init__(self, toplevel):
        self.frame1 = Frame(toplevel).grid(rowspan=8, columnspan=4)

        # ABAS
        self.aba1 = Button(self.frame1,
                           text='GERAÇÃO DE CPF',
                           font='Arial, 10',
                           width=30, height=2,
                           bg=cor['azul3'], fg=cor['branco'],
                           activebackground=cor['azul2'],
                           activeforeground=cor['branco'],
                           highlightbackground=cor['azul3'],
                           border=0,
                           relief=FLAT,
                           command=self.aba1)
        self.aba2 = Button(self.frame1,
                           text='VALIDAÇÃO DE CPF',
                           font='Arial, 10',
                           width=30, height=2,
                           bg=cor['azul3'], fg=cor['branco'],
                           activebackground=cor['azul2'],
                           activeforeground=cor['branco'],
                           highlightbackground=cor['azul3'],
                           border=0,
                           relief=FLAT,
                           command=self.aba2)
        self.aba1.grid(row=0, rowspan=2, column=0, columnspan=3)
        self.aba2.grid(row=0, rowspan=2, column=3, columnspan=3)

        # CONTEÚDO ABA1
        self.formatar = BooleanVar()
        self.label = Label(bg=cor['verde'])
        self.checkbox = Checkbutton(text='CPF formatado',
                                    variable=self.formatar,
                                    bg=cor['verde'], fg=cor['branco'],
                                    activebackground=cor['verde'],
                                    activeforeground=cor['branco'],
                                    highlightbackground=cor['verde'],
                                    selectcolor=cor['azul3'])
        self.texto_do_combobox = Label(text='Estado',
                                       bg=cor['verde'], fg=cor['branco'],
                                       activebackground=cor['verde'],
                                       highlightbackground=cor['verde'])
        self.combo = ttk.Combobox(self.frame1, values=estados, width=3)
        ttk.Style().configure('TCombobox', relief='flat',
                              background=cor['verde'],
                              foreground=cor['branco'],
                              fieldbackground=cor['azul3'],
                              fieldforegroud=cor['branco'],
                              selectbackground=cor['verde'],
                              arrowcolor=cor['preto'],
                              insertcolor=cor['branco'])
        ttk.Style().master.option_add('*TCombobox*Listbox.background', cor['azul3'])
        ttk.Style().master.option_add('*TCombobox*Listbox.foreground', cor['branco'])
        ttk.Style().master.option_add('*TCombobox*Listbox.selectBackground', cor['branco'])
        self.entry = Entry(justify=CENTER,
                           font='Arial, 20',
                           bg=cor['verde'], fg=cor['branco'],
                           highlightbackground=cor['branco'],
                           highlightcolor=cor['branco'],
                           insertbackground=cor['branco'],
                           border=0,
                           relief=FLAT)
        self.bt_gerar = Button(self.frame1,
                               text='GERAR NOVO',
                               bg=cor['azul3'], fg=cor['branco'],
                               activebackground=cor['azul2'],
                               activeforeground=cor['branco'],
                               highlightbackground=cor['azul2'],
                               width=20,
                               relief=FLAT,
                               command=self.gerar)
        self.bt_copiar = Button(self.frame1,
                                text='COPIAR',
                                width=20,
                                bg=cor['azul3'], fg=cor['branco'],
                                activebackground=cor['azul2'],
                                activeforeground=cor['branco'],
                                highlightbackground=cor['azul2'],
                                relief=FLAT,
                                command=self.copiar)

        self.checkbox.grid(row=3, column=0, columnspan=3, pady=10)
        self.combo.grid(row=3, column=3, pady=10)
        self.texto_do_combobox.grid(row=3, column=3, columnspan=3)
        self.label.grid(row=5, column=2, columnspan=2, pady=10)
        self.entry.grid(row=7, rowspan=2, column=1, columnspan=4)
        self.bt_gerar.grid(row=10, column=1, columnspan=2, pady=20)
        self.bt_copiar.grid(row=10, column=3, columnspan=2, pady=20)

        # CONTEÚDO ABA2
        self.bt_validar = Button(self.frame1,
                                 text='VALIDAR',
                                 width=20,
                                 bg=cor['azul3'], fg=cor['branco'],
                                 activebackground=cor['azul2'],
                                 activeforeground=cor['branco'],
                                 highlightbackground=cor['azul2'],
                                 relief=FLAT,
                                 command=self.validar)

root = Tk()
root.configure(bg=cor['verde'])
App(root)
root.mainloop()
