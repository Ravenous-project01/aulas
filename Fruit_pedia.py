import tkinter as tk
import cv2
from tkinter import *
from tkinter import (
    messagebox,
    filedialog,
    Tk,
    Label,
    Entry,
    Button,
    END,
    scrolledtext,
    Frame,
)
import textwrap
from PIL import ImageTk, Image


window = Tk()
window.config(bg="#6A0909")

frutas = [
    ["gomu gomu", "ito ito", "bara bara", "yami yami"],
    ["kilo kilo", "sube sube", "bomu bomu", "gura gura"],
    ["hana hana", "doru doru", "baku baku", "mane mane"],
    ["supa supa", "bane bane", "toge toge", "ori ori"],
    ["doa doa", "ope ope", "horo horo", "nika nika"],
    ["magu magu", "mera mera", "suna suna", "hie hie"],
    ["yuki yuki", "guru guru", "mato mato", "mogu mogu"],
    ["bari bari", "tori tori", "inu inu", "ushi ushi"],
    ["hito hito", "uma uma", "neko neko", "hebi hebi"],
    ["kame kame", "zushi zushi", "mushi mushi", "sara sara"],
    ["daiya daiya", "yomi yomi", "mira mira", "beta beta"],
    ["nagi nagi", "mosa mosa", "shari shari", "kage kage"],
    ["sabi sabi", "giro giro", "asu asu", "jiki jiki"],
    [
        "mushi mushi (model: kabutomushi)",
        "mushi mushi (model: Suzumebachi)",
        "mushi mushi (model: Kumo)",
        "mushi mushi (model: Kamakiri)",
    ],
    ["tama tama", "ton ton", "mira mira", "mushi mushi (model: Wasp)"],
    [
        "mushi mushi (model: Cicada)",
        "mushi mushi (model: Rhinoceros Beetle)",
        "mushi mushi (model: Scorpion)",
        "uma uma (model: Pegasus)",
    ],
    [
        "uma uma (model: Zebra)",
        "uma uma (model: Kirin)",
        "uma uma (model: Bison)",
        "inu inu (model: Dachshund)",
    ],
    [
        "inu inu (model: Wolf)",
        "inu inu (model: Jackal)",
        "inu inu (model: Tanuki)",
        "tori tori (model: Falcon)",
    ],
    [
        "tori tori (model: Albatross)",
        "tori tori (model: Phoenix)",
        "tori tori (model: Eagle)",
        "neko neko (model: Leopard)",
    ],
    [
        "neko neko (model: Saber Tiger)",
        "hebi hebi (model: Anaconda)",
        "hebi hebi (model: King Cobra)",
        "ushi ushi (model: Bison)",
    ],
    [
        "ushi ushi (model: Giraffe)",
        "ushi ushi (model: Buffalo)",
        "ushi ushi (model: Cow)",
        "hito hito (model: Daibutsu)",
    ],
    [
        "hito hito (model: Onyudo)",
        "hito hito (model: Human)",
        "hito hito (model: Monster)",
        "ryu ryu (model: Allosaurus)",
    ],
    [
        "ryu ryu (model: Spinosaurus)",
        "ryu ryu (model: Pteranodon)",
        "ryu ryu (model: Brachiosaurus)",
        "uma uma (model: Horse)",
    ],
    ["uma uma (model: Donkey)", "uma uma (model: Mule)"],
]

pnl = Frame(
    window,
    bg="black",
    bd=3,
    relief="groove",
    padx=5,
    pady=5,
)
btt3 = Button(
    pnl, text="ver sobre", bg="dark blue", fg="white", font=("Arial", 10, "bold")
)

fruta = frutas[0]

teste = Image.open("img/Gomu Gomu.jpg").resize((200, 180)).convert("RGB")

imagem_teste = ImageTk.PhotoImage(teste)

infoPrin = textwrap.fill(
    "seja bem-vindo à Fruit Pedia - One Piece! Aqui você encontrará informações sobre as frutas do diabo do universo One Piece.",
    width=17,
)

maxximo = 1


def main():
    global catalogo
    global window
    global frutas
    global fruta
    global btt
    global maxximo
    global btt3
    global txt
    global btt2_1
    global btt2_2
    btt.grid_forget()

    def catalogo():
        global fruta
        global pnl

        # Limpa o painel antes de adicionar os novos widgets
        for widget in pnl.winfo_children():
            widget.destroy()

        for idx, nome in enumerate(fruta, 1):
            linha = Frame(pnl, bg="black")
            linha.pack(anchor="w", pady=3)

            lbl = Label(
                linha,
                text=f"{idx} - {nome}",
                fg="white",
                bg="black",
                font=("Segoe UI", 16, "italic"),
                justify="left",
            )
            lbl.pack(side="left", padx=(0, 10))

            btn = Button(
                linha,
                text="Ver sobre",
                command=lambda n=nome: select(n),
                bg="dark blue",
                fg="white",
                font=("Arial", 10, "bold"),
            )
            btn.pack(side="left")

    catalogo()

    def reset():
        global txt
        global pnl
        global paineu
        global btt2_1
        global btt2_2
        global back

        back.grid_forget()

        txt["text"] = "Fruit Pedia - One Piece"
        txt["font"] = ("Arial", 20, "bold")

        btt2_1.grid(row=2, column=1)
        btt2_2.grid(row=2, column=2)

        for widget in window.grid_slaves(row=1, column=0):
            if isinstance(widget, Frame) and widget != pnl:
                widget.destroy()

        if not txt.winfo_ismapped():
            txt.pack(side="left", padx=(0, 10))

        pnl.grid(row=1, column=0, sticky="nsew")

        catalogo()

    def click2():
        global fruta
        global frutas
        global maxximo
        global catalogo
        global btt3
        if fruta == frutas[23]:

            maxximo = 89
            fruta = frutas[22]
            catalogo()
        elif fruta == frutas[22]:

            maxximo = 85
            fruta = frutas[21]
            catalogo()
        elif fruta == frutas[21]:

            maxximo = 81
            fruta = frutas[20]
            catalogo()
        elif fruta == frutas[20]:

            maxximo = 77
            fruta = frutas[19]
            catalogo()
        elif fruta == frutas[19]:

            maxximo = 73
            fruta = frutas[18]
            catalogo()
        elif fruta == frutas[18]:

            maxximo = 69
            fruta = frutas[17]
            catalogo()
        elif fruta == frutas[17]:

            maxximo = 65
            fruta = frutas[16]
            catalogo()
        elif fruta == frutas[16]:

            maxximo = 61
            fruta = frutas[15]
            catalogo()
        elif fruta == frutas[15]:

            maxximo = 57
            fruta = frutas[14]
            catalogo()
        elif fruta == frutas[14]:

            maxximo = 53
            fruta = frutas[13]
            catalogo()
        elif fruta == frutas[13]:

            maxximo = 49
            fruta = frutas[12]
            catalogo()
        elif fruta == frutas[12]:

            maxximo = 45
            fruta = frutas[11]
            catalogo()
        elif fruta == frutas[11]:

            maxximo = 41
            fruta = frutas[10]
            catalogo()
        elif fruta == frutas[10]:

            maxximo = 37
            fruta = frutas[9]
            catalogo()
        elif fruta == frutas[9]:

            maxximo = 33
            fruta = frutas[8]
            catalogo()
        elif fruta == frutas[8]:

            maxximo = 29
            fruta = frutas[7]
            catalogo()
        elif fruta == frutas[7]:

            maxximo = 25
            fruta = frutas[6]
            catalogo()
        elif fruta == frutas[6]:

            maxximo = 21
            fruta = frutas[5]
            catalogo()
        elif fruta == frutas[5]:

            maxximo = 17
            fruta = frutas[4]
            catalogo()
        elif fruta == frutas[4]:

            maxximo = 13
            fruta = frutas[3]
            catalogo()
        elif fruta == frutas[3]:

            maxximo = 9
            fruta = frutas[2]
            catalogo()
        elif fruta == frutas[2]:

            maxximo = 5
            fruta = frutas[1]
            catalogo()
        elif fruta == frutas[1]:

            maxximo = 1
            fruta = frutas[0]
            catalogo()

    def select(fruta):
        global frutas
        global maxximo
        global txt
        global back
        txt.destroy()

        pnl2 = Frame(window, bg="black", bd=3, relief="groove", padx=5, pady=5)
        pnl2.grid(row=1, column=0, sticky="nsew")
        linha2 = Label(
            pnl2,
            text=f"{fruta}: \n\n",
            bg="black",
            fg="white",
            font=("Arial", 15, "italic"),
            justify="left",
        )
        linha2.pack(anchor="w", pady=3)

        txt = Label(paineu, text="", bg="black", fg="white", font=("Arial", 15, "bold"))
        txt.pack()
        info = ""
        if fruta == "gomu gomu":
            txt["text"] = "Gomu Gomu No Mi"
            info = (
                "Paramecia que torna o corpo do usuário elástico como borracha. "
                "Permite ataques e defesas criativos. Usuário: Monkey D. Luffy."
            )
        elif fruta == "ito ito":
            txt["text"] = "Ito Ito No Mi"
            info = (
                "Permite criar e manipular fios extremamente resistentes, podendo controlar pessoas e cortar objetos. "
                "Usuário: Donquixote Doflamingo."
            )
        elif fruta == "bara bara":
            txt["text"] = "Bara Bara No Mi"
            info = "Permite separar o corpo em partes e controlá-las à distância. Imune a cortes. Usuário: Buggy."
        elif fruta == "yami yami":
            txt["text"] = "Yami Yami No Mi"
            info = (
                "Logia que permite criar e controlar a escuridão, absorvendo tudo ao redor e anulando poderes de outras frutas. "
                "Usuário: Marshall D. Teach (Barba Negra)."
            )
        elif fruta == "kilo kilo":
            txt["text"] = "Kilo Kilo No Mi"
            info = "Permite alterar o peso do usuário de 1 a 10.000 quilos sem mudar o tamanho do corpo. Usuária: Miss Valentine."
        elif fruta == "sube sube":
            txt["text"] = "Sube Sube No Mi"
            info = "Deixa o corpo liso, fazendo ataques escorregarem. Usuária: Alvida."
        elif fruta == "bomu bomu":
            txt["text"] = "Bomu Bomu No Mi"
            info = "Transforma o corpo em bomba, podendo explodir partes do corpo sem se ferir. Usuário: Mr. 5."
        elif fruta == "gura gura":
            txt["text"] = "Gura Gura No Mi"
            info = "Permite criar terremotos e maremotos, podendo destruir o mundo. Usuários: Barba Branca e Barba Negra."
        elif fruta == "hana hana":
            txt["text"] = "Hana Hana No Mi"
            info = "Permite fazer partes do corpo brotarem em qualquer superfície. Usuária: Nico Robin."
        elif fruta == "doru doru":
            txt["text"] = "Doru Doru No Mi"
            info = "Permite criar e manipular cera como se fosse aço. Usuário: Mr. 3 (Galdino)."
        elif fruta == "baku baku":
            txt["text"] = "Baku Baku No Mi"
            info = "Permite comer qualquer coisa e incorporar as propriedades do que foi comido. Usuário: Wapol."
        elif fruta == "mane mane":
            txt["text"] = "Mane Mane No Mi"
            info = "Permite copiar a aparência de qualquer pessoa tocada. Usuário: Bentham (Mr. 2 Bon Clay)."
        elif fruta == "supa supa":
            txt["text"] = "Supa Supa No Mi"
            info = "Permite transformar partes do corpo em lâminas de aço. Usuário: Mr. 1 (Daz Bones)."
        elif fruta == "bane bane":
            txt["text"] = "Bane Bane No Mi"
            info = "Permite transformar partes do corpo em molas. Usuário: Bellamy."
        elif fruta == "toge toge":
            txt["text"] = "Toge Toge No Mi"
            info = "Permite criar espinhos em todo o corpo. Usuária: Miss Doublefinger."
        elif fruta == "ori ori":
            txt["text"] = "Ori Ori No Mi"
            info = "Permite criar grilhões e prender pessoas instantaneamente. Usuária: Hina."
        elif fruta == "doa doa":
            txt["text"] = "Doa Doa No Mi"
            info = "Permite criar portas em qualquer superfície, inclusive no ar. Usuário: Blueno."
        elif fruta == "ope ope":
            txt["text"] = "Ope Ope No Mi"
            info = "Permite criar uma 'sala' onde pode manipular tudo livremente, inclusive realizar cirurgias milagrosas. Usuário: Trafalgar Law."
        elif fruta == "horo horo":
            txt["text"] = "Horo Horo No Mi"
            info = "Permite criar fantasmas que podem enfraquecer o espírito das pessoas. Usuária: Perona."
        elif fruta == "nika nika":
            txt["text"] = "Nika Nika No Mi"
            info = "Permite transformar o corpo em borracha com poderes lendários do Deus do Sol Nika. Usuário: Monkey D. Luffy (forma desperta)."
        elif fruta == "magu magu":
            txt["text"] = "Magu Magu No Mi"
            info = "Permite criar, controlar e se transformar em magma. Usuário: Akainu (Sakazuki)."
        elif fruta == "mera mera":
            txt["text"] = "Mera Mera No Mi"
            info = "Permite criar, controlar e se transformar em fogo. Usuários: Portgas D. Ace e Sabo."
        elif fruta == "suna suna":
            txt["text"] = "Suna Suna No Mi"
            info = "Permite criar, controlar e se transformar em areia. Usuário: Crocodile."
        elif fruta == "hie hie":
            txt["text"] = "Hie Hie No Mi"
            info = "Permite criar, controlar e se transformar em gelo. Usuário: Aokiji (Kuzan)."
        elif fruta == "yuki yuki":
            txt["text"] = "Yuki Yuki No Mi"
            info = "Permite criar, controlar e se transformar em neve. Usuária: Monet."
        elif fruta == "guru guru":
            txt["text"] = "Guru Guru No Mi"
            info = "Permite girar partes do corpo como hélices. Usuário: Buffalo."
        elif fruta == "mato mato":
            txt["text"] = "Mato Mato No Mi"
            info = "Permite marcar um alvo e sempre acertá-lo com projéteis. Usuário: Vander Decken IX."
        elif fruta == "mogu mogu":
            txt["text"] = "Mogu Mogu No Mi"
            info = (
                "Permite se transformar em uma toupeira. Usuária: Miss Merry Christmas."
            )
        elif fruta == "bari bari":
            txt["text"] = "Bari Bari No Mi"
            info = "Permite criar barreiras intransponíveis. Usuário: Bartolomeo."
        elif fruta == "tori tori":
            txt["text"] = "Tori Tori No Mi"
            info = "Permite se transformar em pássaro. Existem vários modelos: Falcão, Albatross, Phoenix, etc."
        elif fruta == "inu inu":
            txt["text"] = "Inu Inu No Mi"
            info = "Permite se transformar em cachorro. Existem vários modelos: Lobo, Dachshund, etc."
        elif fruta == "ushi ushi":
            txt["text"] = "Ushi Ushi No Mi"
            info = "Permite se transformar em bovino. Existem vários modelos: Bison, Giraffe, etc."
        elif fruta == "hito hito":
            txt["text"] = "Hito Hito No Mi"
            info = "Permite a um animal se transformar em humano. Usuário: Tony Tony Chopper."
        elif fruta == "uma uma":
            txt["text"] = "Uma Uma No Mi"
            info = "Permite se transformar em cavalo. Existem vários modelos: Zebra, Bison, etc."
        elif fruta == "neko neko":
            txt["text"] = "Neko Neko No Mi"
            info = "Permite se transformar em felino. Existem vários modelos: Leopardo, Saber Tiger, etc."
        elif fruta == "hebi hebi":
            txt["text"] = "Hebi Hebi No Mi"
            info = "Permite se transformar em cobra. Existem vários modelos: Anaconda, King Cobra, etc."
        elif fruta == "kame kame":
            txt["text"] = "Kame Kame No Mi"
            info = "Permite se transformar em tartaruga. Usuário: Pekoms."
        elif fruta == "zushi zushi":
            txt["text"] = "Zushi Zushi No Mi"
            info = "Permite controlar a gravidade. Usuário: Fujitora (Issho)."
        elif fruta == "mushi mushi":
            txt["text"] = "Mushi Mushi No Mi"
            info = "Permite se transformar em inseto. Existem vários modelos: Kabutomushi, Suzumebachi, etc."
        elif fruta == "sara sara":
            txt["text"] = "Sara Sara No Mi"
            info = "Permite se transformar em axolote. Usuário: Smiley."
        elif fruta == "daiya daiaya":
            txt["text"] = "Daiya Daiya No Mi"
            info = "Permite transformar o corpo em diamante. Usuário: Jozu."
        elif fruta == "yomi yomi":
            txt["text"] = "Yomi Yomi No Mi"
            info = "Permite ao usuário voltar à vida após a morte. Usuário: Brook."
        elif fruta == "mira mira":
            txt["text"] = "Mira Mira No Mi"
            info = "Permite criar e manipular espelhos. Usuária: Charlotte Brûlée."
        elif fruta == "beta beta":
            txt["text"] = "Beta Beta No Mi"
            info = "Permite criar e manipular uma substância pegajosa. Usuário: Trebol."
        elif fruta == "nagi nagi":
            txt["text"] = "Nagi Nagi No Mi"
            info = "Permite anular sons ao redor do usuário. Usuário: Donquixote Rosinante."
        elif fruta == "mosa mosa":
            txt["text"] = "Mosa Mosa No Mi"
            info = "Permite acelerar o crescimento de plantas. Usuário: Binz."
        elif fruta == "shari shari":
            txt["text"] = "Shari Shari No Mi"
            info = "Permite transformar partes do corpo em rodas. Usuário: Sharinguru."
        elif fruta == "kage kage":
            txt["text"] = "Kage Kage No Mi"
            info = "Permite controlar sombras e colocá-las em outros corpos. Usuário: Gecko Moria."
        elif fruta == "sabi sabi":
            txt["text"] = "Sabi Sabi No Mi"
            info = "Permite enferrujar qualquer coisa tocada. Usuária: Shu."
        elif fruta == "giro giro":
            txt["text"] = "Giro Giro No Mi"
            info = "Permite ver através de objetos e ler mentes. Usuária: Viola."
        elif fruta == "asu asu":
            txt["text"] = "Asu Asu No Mi"
            info = "Permite acelerar o envelhecimento de seres vivos. Usuária: Jewelry Bonney."
        elif fruta == "jiki jiki":
            txt["text"] = "Jiki Jiki No Mi"
            info = "Permite controlar o magnetismo. Usuário: Eustass Kid."
        elif fruta == "mushi mushi (model: kabutomushi)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Kabutomushi"
            info = "Permite se transformar em um besouro-rinoceronte. Usuário: Kabu."
        elif fruta == "mushi mushi (model: Suzumebachi)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Suzumebachi"
            info = "Permite se transformar em uma vespa gigante. Usuário: Bian."
        elif fruta == "mushi mushi (model: Kumo)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Kumo"
            info = "Permite se transformar em uma aranha. Usuário: Black Maria."
        elif fruta == "mushi mushi (model: Kamakiri)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Kamakiri"
            info = "Permite se transformar em um louva-a-deus. Usuário: Desconhecido."
        elif fruta == "tama tama":
            txt["text"] = "Tama Tama no Mi"
            info = "Permite ao usuário criar ovos de qualquer parte do corpo. Usuário: Tamago."
        elif fruta == "ton ton":
            txt["text"] = "Ton Ton no Mi"
            info = "Permite alterar o peso do usuário até 100 toneladas. Usuária: Machvise."
        elif fruta == "mira mira":
            txt["text"] = "Mira Mira no Mi"
            info = "Permite criar e manipular espelhos, inclusive viajar por eles. Usuária: Charlotte Brûlée."
        elif fruta == "mushi mushi (model: Wasp)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Wasp"
            info = "Permite se transformar em uma vespa. Usuário: Desconhecido."
        elif fruta == "mushi mushi (model: Cicada)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Cicada"
            info = "Permite se transformar em uma cigarra. Usuário: Desconhecido."
        elif fruta == "mushi mushi (model: Rhinoceros Beetle)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Rhinoceros Beetle"
            info = "Permite se transformar em um besouro-rinoceronte. Usuário: Desconhecido."
        elif fruta == "mushi mushi (model: Scorpion)":
            txt["text"] = "Mushi Mushi no Mi, Modelo: Scorpion"
            info = "Permite se transformar em um escorpião. Usuário: Desconhecido."
        elif fruta == "uma uma (model: Pegasus)":
            txt["text"] = "Uma Uma no Mi, Modelo: Pegasus"
            info = (
                "Permite se transformar em um cavalo alado (Pégaso). Usuário: Stronger."
            )
        elif fruta == "uma uma (model: Zebra)":
            txt["text"] = "Uma Uma no Mi, Modelo: Zebra"
            info = "Permite se transformar em uma zebra. Usuário: Desconhecido."
        elif fruta == "uma uma (model: Kirin)":
            txt["text"] = "Uma Uma no Mi, Modelo: Kirin"
            info = "Permite se transformar em um Kirin (criatura mitológica). Usuário: Desconhecido."
        elif fruta == "uma uma (model: Bison)":
            txt["text"] = "Uma Uma no Mi, Modelo: Bison"
            info = "Permite se transformar em um bisão. Usuário: Dalton."
        elif fruta == "inu inu (model: Dachshund)":
            txt["text"] = "Inu Inu no Mi, Modelo: Dachshund"
            info = "Permite se transformar em um cachorro da raça Dachshund. Usuário: Lassoo."
        elif fruta == "inu inu (model: Wolf)":
            txt["text"] = "Inu Inu no Mi, Modelo: Wolf"
            info = "Permite se transformar em um lobo. Usuário: Jabra."
        elif fruta == "inu inu (model: Jackal)":
            txt["text"] = "Inu Inu no Mi, Modelo: Jackal"
            info = "Permite se transformar em um chacal. Usuário: Chaka."
        elif fruta == "inu inu (model: Tanuki)":
            txt["text"] = "Inu Inu no Mi, Modelo: Tanuki"
            info = "Permite se transformar em um tanuki (cão-guaxinim japonês). Usuário: Bunbuku."
        elif fruta == "tori tori (model: Falcon)":
            txt["text"] = "Tori Tori no Mi, Modelo: Falcon"
            info = "Permite se transformar em um falcão. Usuário: Pell."
        elif fruta == "tori tori (model: Albatross)":
            txt["text"] = "Tori Tori no Mi, Modelo: Albatross"
            info = "Permite se transformar em um albatroz. Usuário: Morgans."
        elif fruta == "tori tori (model: Phoenix)":
            txt["text"] = "Tori Tori no Mi, Modelo: Phoenix"
            info = "Permite se transformar em uma fênix, com poderes de regeneração. Usuário: Marco."
        elif fruta == "tori tori (model: Eagle)":
            txt["text"] = "Tori Tori no Mi, Modelo: Eagle"
            info = "Permite se transformar em uma águia. Usuário: Desconhecido."
        elif fruta == "neko neko (model: Leopard)":
            txt["text"] = "Neko Neko no Mi, Modelo: Leopard"
            info = "Permite se transformar em um leopardo. Usuário: Rob Lucci."
        elif fruta == "neko neko (model: Saber Tiger)":
            txt["text"] = "Neko Neko no Mi, Modelo: Saber Tiger"
            info = "Permite se transformar em um tigre-dentes-de-sabre. Usuário: Who's Who."
        elif fruta == "hebi hebi (model: Anaconda)":
            txt["text"] = "Hebi Hebi no Mi, Modelo: Anaconda"
            info = "Permite se transformar em uma anaconda. Usuário: Boa Sandersonia."
        elif fruta == "hebi hebi (model: King Cobra)":
            txt["text"] = "Hebi Hebi no Mi, Modelo: King Cobra"
            info = "Permite se transformar em uma cobra-rei. Usuário: Boa Marigold."
        elif fruta == "ushi ushi (model: Bison)":
            txt["text"] = "Ushi Ushi no Mi, Modelo: Bison"
            info = "Permite se transformar em um bisão. Usuário: Dalton."
        elif fruta == "ushi ushi (model: Giraffe)":
            txt["text"] = "Ushi Ushi no Mi, Modelo: Giraffe"
            info = "Permite se transformar em uma girafa. Usuário: Kaku."
        elif fruta == "ushi ushi (model: Buffalo)":
            txt["text"] = "Ushi Ushi no Mi, Modelo: Buffalo"
            info = "Permite se transformar em um búfalo. Usuário: Minotaurus."
        elif fruta == "ushi ushi (model: Cow)":
            txt["text"] = "Ushi Ushi no Mi, Modelo: Cow"
            info = "Permite se transformar em uma vaca. Usuário: Desconhecido."
        elif fruta == "hito hito (model: Daibutsu)":
            txt["text"] = "Hito Hito no Mi, Modelo: Daibutsu"
            info = (
                "Permite se transformar em um Buda gigante dourado. Usuário: Sengoku."
            )
        elif fruta == "hito hito (model: Onyudo)":
            txt["text"] = "Hito Hito no Mi, Modelo: Onyudo"
            info = "Permite se transformar em um monge gigante. Usuário: Onimaru."
        elif fruta == "hito hito (model: Human)":
            txt["text"] = "Hito Hito no Mi, Modelo: Human"
            info = "Permite se transformar em humano. Usuário: Chopper (forma base)."
        elif fruta == "hito hito (model: Monster)":
            txt["text"] = "Hito Hito no Mi, Modelo: Monster"
            info = "Permite se transformar em um monstro gigante. Usuário: Chopper (forma Monster Point)."
        elif fruta == "ryu ryu (model: Allosaurus)":
            txt["text"] = "Ryu Ryu no Mi, Modelo: Allosaurus"
            info = "Permite se transformar em um allossauro. Usuário: X Drake."
        elif fruta == "ryu ryu (model: Spinosaurus)":
            txt["text"] = "Ryu Ryu no Mi, Modelo: Spinosaurus"
            info = "Permite se transformar em um espinossauro. Usuário: Page One."
        elif fruta == "ryu ryu (model: Pteranodon)":
            txt["text"] = "Ryu Ryu no Mi, Modelo: Pteranodon"
            info = "Permite se transformar em um pteranodonte. Usuário: King."
        elif fruta == "ryu ryu (model: Brachiosaurus)":
            txt["text"] = "Ryu Ryu no Mi, Modelo: Brachiosaurus"
            info = "Permite se transformar em um braquiossauro. Usuário: Queen."
        elif fruta == "uma uma (model: Horse)":
            txt["text"] = "Uma Uma no Mi, Modelo: Horse"
            info = "Permite se transformar em um cavalo. Usuário: Desconhecido."
        elif fruta == "uma uma (model: Donkey)":
            txt["text"] = "Uma Uma no Mi, Modelo: Donkey"
            info = "Permite se transformar em um burro. Usuário: Desconhecido."
        elif fruta == "uma uma (model: Mule)":
            txt["text"] = "Uma Uma no Mi, Modelo: Mule"
            info = "Permite se transformar em uma mula. Usuário: Desconhecido."

        else:
            txt["text"] = fruta
            info = "Informação não cadastrada para esta fruta."
        texto_larg = textwrap.fill(info, width=50)

        linha2["text"] = texto_larg

        back = Button(
            window,
            text="Voltar",
            command=reset,
            bg="dark red",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        back.grid(row=4, column=0)
        btt2_1.grid_forget()
        btt2_2.grid_forget()
        btt3.destroy()

    def click1():
        global fruta
        global maxximo
        if fruta == frutas[0]:
            fruta = frutas[1]
            catalogo()
        elif fruta == frutas[1]:
            fruta = frutas[2]
            catalogo()
        elif fruta == frutas[2]:
            fruta = frutas[3]
            catalogo()
        elif fruta == frutas[3]:
            fruta = frutas[4]
            catalogo()
        elif fruta == frutas[4]:
            fruta = frutas[5]
            catalogo()
        elif fruta == frutas[5]:
            fruta = frutas[6]
            catalogo()
        elif fruta == frutas[6]:
            fruta = frutas[7]
            catalogo()
        elif fruta == frutas[7]:
            fruta = frutas[8]
            catalogo()
        elif fruta == frutas[8]:
            fruta = frutas[9]
            catalogo()
        elif fruta == frutas[9]:
            fruta = frutas[10]
            catalogo()
        elif fruta == frutas[10]:
            fruta = frutas[11]
            catalogo()
        elif fruta == frutas[11]:
            fruta = frutas[12]
            catalogo()
        elif fruta == frutas[12]:
            fruta = frutas[13]
            catalogo()
        elif fruta == frutas[13]:
            fruta = frutas[14]
            catalogo()
        elif fruta == frutas[14]:
            fruta = frutas[15]
            catalogo()
        elif fruta == frutas[15]:
            fruta = frutas[16]
            catalogo()
        elif fruta == frutas[16]:
            fruta = frutas[17]
            catalogo()
        elif fruta == frutas[17]:
            fruta = frutas[18]
            catalogo()
        elif fruta == frutas[18]:
            fruta = frutas[19]
            catalogo()
        elif fruta == frutas[19]:
            fruta = frutas[20]
            catalogo()
        elif fruta == frutas[20]:
            fruta = frutas[21]
            catalogo()
        elif fruta == frutas[21]:
            fruta = frutas[22]
            catalogo()
        elif fruta == frutas[22]:
            fruta = frutas[23]
            catalogo()

    btt2_1 = Button(window, text="<-", command=click2, bg="dark blue", fg="white")
    btt2_1.grid(row=2, column=1)
    btt2_2 = Button(window, text="->", command=click1, bg="dark blue", fg="white")
    btt2_2.grid(row=2, column=2)


window.title("Fruit Pedia - One Piece")
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("500x300")
window.resizable(False, False)

paineu = Frame(window, bg="black", bd=3, relief="groove", padx=5, pady=5)
txt = Label(
    paineu,
    text="Fruit Pedia - One Piece",
    fg="white",
    bg="black",
    font=("Arial", 20, "bold"),
    justify="left",
)
maxx = Label(window, text="", bg="#6A0909")
btt = Button(window, text="catálogo", command=main, bg="dark blue", fg="white")

telaImg = Label(pnl, image=imagem_teste, bg="black", bd=3, relief="groove")
telaImg.pack(side="left", padx=(0, 10))
telaText = Label(
    pnl,
    text=infoPrin,
    fg="white",
    bg="black",
    font=("Arial", 16, "italic"),
    justify="left",
)
telaText.pack(side="right", padx=(0, 10))

btt.grid(row=3, column=1)
maxx.grid(row=10, column=10)
paineu.grid(row=0, column=0, sticky="ew")
pnl.grid(row=1, column=0, sticky="nsew")

txt.pack(side="left", padx=(0, 10))

window.mainloop()
