import tkinter

# Nombre : Sergio Daniel Velasquez Pobre.
# Codigo: 20161146458

# *************************************************************************************
#   FUNCIONES
# *************************************************************************************
global listadoVerbos,listadoAdjetivos,listadoSustantivos
listadoVerbos=[]
listadoAdjetivos=[]
listadoSustantivos=[]


def identificarSustantivos(__listaPalabras):
    __listadoSustantivos = []
    iteraciones=-1
    for i in __listaPalabras:
        iteraciones+=1
        letra=listaPalabras[iteraciones]
        if letra[0]>='A' and letra[0]<='Z':
            __listadoSustantivos.append(i)
    for i in __listaPalabras:
        for j in listadoSustantivos:
            if i == j:
                __listadoSustantivos.append(i)
                continue

    return __listadoSustantivos


def identificarAdjetivos(__listaPalabras):
    __listadoAdjetivos = []
    for i in __listaPalabras:
        for j in listadoAdjetivos:
            if i == j:
                __listadoAdjetivos.append(i)
                continue
    return __listadoAdjetivos


def identificarVerbos(__listaPalabras):
    __verbosIdentificados=[]
    for i in __listaPalabras:
        for j in listadoVerbos:
            if i == j:
                __verbosIdentificados.append(i)
                continue
    return __verbosIdentificados


def resumirTexto(__listaOraciones,listaPalabras,texto):

    Rtexto=""
    __texto=__listaOraciones
    iteracion=-1
    print(__listaOraciones)
    for i in __listaOraciones:
        iteracion+=1
        if iteracion%2==0:
            Rtexto += __texto[iteracion]
            print("lalala")

    if not __listaOraciones or len(__listaOraciones)<2:
        return texto
    return Rtexto

listaOraciones=[]
listaPalabras=[]

oracion = ""
palabra = ""

def dar_click():

    __texto = Area_texto.get("1.0", "end-1c")

    for i in __texto:
        global oracion
        global palabra

        oracion += str(i)
        palabra += str(i)
        if i==";":
            print("si sirve")
        if i==" " or i==".":
            if len(palabra)<=3:
                palabra = ""
                continue
            listaPalabras.append(palabra.strip().strip(".").strip(";").strip(":").strip(","))

            palabra=""
        if i==".": # Se busca un punto en el texto para separar las oraciones.
            listaOraciones.append(oracion)
            oracion=""


    oracion = ""
    palabra = ""
    sustantivo.config(text="Sustantivo :"+str(identificarSustantivos(listaPalabras)))
    adjetivo.config(text="Adjetivo :"+str(identificarAdjetivos(listaPalabras)))
    verbo.config(text="Verbo :"+str(identificarVerbos(listaPalabras)))

    R_Area_texto.delete("1.0", "end-1c")
    R_Area_texto.insert("1.0", resumirTexto(listaOraciones,listaPalabras,__texto))

    print("Listado de oraciones : ",listaOraciones)
    print("Listado de palabras: ",listaPalabras)
    print("Texto completo:   ", __texto)
    del listaOraciones[:] # Se vacia la lista.kkñ
    del listaPalabras[:]
# *************************************************************************************
# *************************************************************************************



# *************************************************************************************
# Ejecucion principal
# *************************************************************************************

#--Carga el listado de palabras

f=open('source/verbos.txt', 'r', encoding="utf8")
for v_palabra in f:
    listadoVerbos.append(v_palabra[:-1])
f.close()

f=open('source/adjetivos.txt', 'r')
for adj_palabra in f:
    listadoAdjetivos.append(adj_palabra[:-1])
f.close()

f=open('source/sustantivos.txt', 'r', encoding="utf8")
for sustantivo in f:
    listadoSustantivos.append(sustantivo[:-1])
f.close()

#---Ventana -----
ventana = tkinter.Tk()
ventana.title("Resumidor- Daniel Velasquez")
ventana.config(background="lightgreen")
ventana.resizable(width=False, height=False)
ventana.minsize(width=700,height=400)


#-----layout -----
layoutTagHeader=tkinter.Frame(ventana)
layoutTagHeader.grid(column=0, row=0,padx=(10, 10),pady=(10, 25))  # Layout
layoutTagHeader.columnconfigure(0, weight=1)  # Se deben conservar las palabras reservadas en los parametros.
layoutTagHeader.rowconfigure(0, weight=1)

layoutWidgets = tkinter.Frame(ventana)  # lienzo donde se dibujan los elementos.
layoutWidgets.grid(column=0, row=1,padx=(10, 10),pady=(10, 10))  # Layout
layoutWidgets.columnconfigure(0, weight=1)  # Se deben conservar las palabras reservadas en los parametros.
layoutWidgets.rowconfigure(0, weight=1)

layoutTagFooter = tkinter.Frame(ventana)  # lienzo donde se dibujan los elementos.
layoutTagFooter.grid(column=0, row=2,padx=(10, 10),pady=(5, 10))  # Layout
layoutTagFooter.columnconfigure(0, weight=1)  # Se deben conservar las palabras reservadas en los parametros.
layoutTagFooter.rowconfigure(0, weight=1)

#---Etiquetas ------
etiquetaIngreso = tkinter.Label(layoutTagHeader, text=" Ingrese el texto que desea resumir: ",font=("Courier 12 bold"))
etiquetaIngreso.grid(column=1, row=0)
# textoResumen.pack()  Se empaqueta dentro de la ventana.

etiquetaResumen = tkinter.Label(layoutTagHeader, text=" Este es el resumen del texto:",font=("Courier 12 bold"))
etiquetaResumen.grid(column=2, row=0)

#---Texto, button. ---
Area_texto = tkinter.Text(layoutWidgets, width=25, height=25)
Area_texto.grid(column=1, row=0)

R_Area_texto = tkinter.Text(layoutWidgets, width=25, height=25, foreground="brown")
R_Area_texto.grid(column=3, row=0)

btn_aceptar = tkinter.Button(layoutWidgets, text="RESUMIR", command=dar_click,background="skyblue", foreground="darkblue",width=15,height=2)  # command es un evento.
btn_aceptar.grid(column=2, row=1)


#-----Etiquetas sustantivo,adjetivo,verbo ------

sustantivo = tkinter.Label(layoutTagFooter, text="Sustantivo: Ninguno", foreground="red")
sustantivo.grid(column=0, row=1)

adjetivo = tkinter.Label(layoutTagFooter, text="Adjetivo: Ninguno", foreground="blue")
adjetivo.grid(column=0, row=2)

verbo = tkinter.Label(layoutTagFooter, text="Verbo: Ninguno", foreground="green")
verbo.grid(column=0, row=3)


ventana.mainloop()

# *************************************************************************************
# *************************************************************************************

