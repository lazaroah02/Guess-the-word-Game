import random
from tkinter import *
from mis_librerias.Centrar_Ventana import centrar_ventana
from tkinter import messagebox
from mis_librerias.RGB import rgb

class Ahorcado():
    def __init__(self):
        self.palabras = ["MANGOS", "FANGOS", "PELOTA", "REBOTA", "REPASO", "SANDIA", "RETAZO", "SAPOTE", "SUNDAY", "FRIDAY", "RAYAZO"]
        self.palabra_a_adivinar = random.choice(self.palabras)
        
        self.root = Tk()
        self.root.title("Ahorcado")
        self.root.resizable(0,0)
        self.root.geometry(centrar_ventana(600,400,self.root))
        
        self.frame = Frame(self.root)
        self.frame.config(bg = rgb((84,146,203)))
        self.frame.pack(fill = "both", expand = True)
        
        self.label_title = Label(self.frame, text = "Juego Ahorcado")
        self.label_title.config(bg = rgb((84,146,203)), font = ("Courier", 18))
        self.label_title.place(x = "200", y = "0")
        
        self.imagen = PhotoImage(file="imagenes/Fondo.png")
        self.pizarra = Label(self.frame, image = self.imagen)
        self.pizarra.config(width = 400, height = 200)
        self.pizarra.place(x = "100", y = "30")
        
        self.raya_1 = Text(self.frame)
        self.raya_1.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_1.place(x = "150", y = "250")
        
        self.raya_2 = Text(self.frame)
        self.raya_2.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_2.place(x = "200", y = "250")
        
        self.raya_3 = Text(self.frame)
        self.raya_3.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_3.place(x = "250", y = "250")
        
        self.raya_4 = Text(self.frame)
        self.raya_4.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_4.place(x = "300", y = "250")
        
        self.raya_5 = Text(self.frame)
        self.raya_5.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_5.place(x = "350", y = "250")
        
        self.raya_6 = Text(self.frame)
        self.raya_6.config(width = 2, height =1, state = "disabled", font = ("Courier", 16))
        self.raya_6.place(x = "400", y = "250")    
        
        self.boton1 = Button(self.frame, text = "a", command = self.codigo_boton1)
        self.boton1.config(width = 4, height = 2)
        self.boton1.place(x = 50, y = "300")
        
        self.boton2 = Button(self.frame, text = "a", command = self.codigo_boton2)
        self.boton2.config(width = 4, height = 2)
        self.boton2.place(x = 90, y = "300")
        
        self.boton3 = Button(self.frame, text = "a", command = self.codigo_boton3)
        self.boton3.config(width = 4, height = 2)
        self.boton3.place(x =130, y = "300")
        
        self.boton4 = Button(self.frame, text = "a", command = self.codigo_boton4)
        self.boton4.config(width = 4, height = 2)
        self.boton4.place(x = 170, y = "300")
        
        self.boton5 = Button(self.frame, text = "a", command = self.codigo_boton5)
        self.boton5.config(width = 4, height = 2)
        self.boton5.place(x = 210, y = "300")
        
        self.boton6 = Button(self.frame, text = "a", command = self.codigo_boton6)
        self.boton6.config(width = 4, height = 2)
        self.boton6.place(x = 250, y = "300")
        
        self.boton7 = Button(self.frame, text = "a", command = self.codigo_boton7)
        self.boton7.config(width = 4, height = 2)
        self.boton7.place(x = 290, y = "300")
        
        self.boton8 = Button(self.frame, text = "a", command = self.codigo_boton8)
        self.boton8.config(width = 4, height = 2)
        self.boton8.place(x = 330, y = "300")
        
        self.boton9 = Button(self.frame, text = "a", command = self.codigo_boton9)
        self.boton9.config(width = 4, height = 2)
        self.boton9.place(x = 370, y = "300")
        
        self.boton10 = Button(self.frame, text = "a", command = self.codigo_boton10)
        self.boton10.config(width = 4, height = 2)
        self.boton10.place(x = 410, y = "300")
        
        self.boton11 = Button(self.frame, text = "a", command = self.codigo_boton11)
        self.boton11.config(width = 4, height = 2)
        self.boton11.place(x = 450, y = "300")
        
        self.boton12 = Button(self.frame, text = "a", command = self.codigo_boton12)
        self.boton12.config(width = 4, height = 2)
        self.boton12.place(x = 490, y = "300")
        
        self.boton13 = Button(self.frame, text = "a", command = self.codigo_boton13)
        self.boton13.config(width = 4, height = 2)
        self.boton13.place(x =530, y = "300")
        
        self.boton14 = Button(self.frame, text = "a", command = self.codigo_boton14)
        self.boton14.config(width = 4, height = 2)
        self.boton14.place(x = 50, y = "350")
        
        self.boton15 = Button(self.frame, text = "a", command = self.codigo_boton15)
        self.boton15.config(width = 4, height = 2)
        self.boton15.place(x = 90, y = "350")
        
        self.boton16 = Button(self.frame, text = "a", command = self.codigo_boton16)
        self.boton16.config(width = 4, height = 2)
        self.boton16.place(x = 130, y = "350")
        
        self.boton17 = Button(self.frame, text = "a", command = self.codigo_boton17)
        self.boton17.config(width = 4, height = 2)
        self.boton17.place(x = 170, y = "350")
        
        self.boton18 = Button(self.frame, text = "a", command = self.codigo_boton18)
        self.boton18.config(width = 4, height = 2)
        self.boton18.place(x = 210, y = "350")
        
        self.boton19 = Button(self.frame, text = "a", command = self.codigo_boton19)
        self.boton19.config(width = 4, height = 2)
        self.boton19.place(x = 250, y = "350")
        
        self.boton20 = Button(self.frame, text = "a", command = self.codigo_boton20)
        self.boton20.config(width = 4, height = 2)
        self.boton20.place(x = 290, y = "350")
        
        self.boton21 = Button(self.frame, text = "a", command = self.codigo_boton21)
        self.boton21.config(width = 4, height = 2)
        self.boton21.place(x = 330, y = "350")
        
        self.boton22 = Button(self.frame, text = "a", command = self.codigo_boton22)
        self.boton22.config(width = 4, height = 2)
        self.boton22.place(x = 370, y = "350")
        
        self.boton23 = Button(self.frame, text = "a", command = self.codigo_boton23)
        self.boton23.config(width = 4, height = 2)
        self.boton23.place(x = 410, y = "350")
        
        self.boton24 = Button(self.frame, text = "a", command = self.codigo_boton24)
        self.boton24.config(width = 4, height = 2)
        self.boton24.place(x = 450, y = "350")
        
        self.boton25 = Button(self.frame, text = "a", command = self.codigo_boton25)
        self.boton25.config(width = 4, height = 2)
        self.boton25.place(x = 490, y = "350")
        
        self.boton26 = Button(self.frame, text = "a", command = self.codigo_boton26)
        self.boton26.config(width = 4, height = 2)
        self.boton26.place(x = 530, y = "350")
        
        self.imagen_reinicio = PhotoImage(file = "imagenes/reset.png")
        self.boton_reiniciar = Button(self.frame, image = self.imagen_reinicio, command = self.reiniciar_juego)
        self.boton_reiniciar.place(x = 530, y = 50)
        
        self.funciones_de_botones = [self.codigo_boton1,self.codigo_boton2,self.codigo_boton3,self.codigo_boton4,self.codigo_boton5,
                                     self.codigo_boton6,self.codigo_boton7,self.codigo_boton8,self.codigo_boton9,self.codigo_boton10,
                                     self.codigo_boton11,self.codigo_boton12,self.codigo_boton13,self.codigo_boton14,self.codigo_boton15,
                                     self.codigo_boton16,self.codigo_boton17,self.codigo_boton18,self.codigo_boton19,self.codigo_boton20,
                                     self.codigo_boton21,self.codigo_boton22, self.codigo_boton23,self.codigo_boton24,self.codigo_boton25,
                                     self.codigo_boton26]
          
        self.botones = [self.boton1, self.boton2, self.boton3, self.boton4, self.boton5, self.boton6, self.boton7, self.boton8, self.boton9,
                        self.boton10,self.boton11, self.boton12, self.boton13,self.boton14, self.boton15, self.boton16, self.boton17,
                        self.boton18, self.boton19, self.boton20, self.boton21, self.boton22, self.boton23, self.boton24,self.boton25,self.boton26]  
        
        self.rayas = [self.raya_1,self.raya_2,self.raya_3,self.raya_4,self.raya_5,self.raya_6]
        self.letras_botones = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.contador_letras_correctas = 0
        self.contador_letras_incorrectas = 6
        
        self.label_mostrar_intentos = Label(self.frame, text = (f"Intentos: {str(self.contador_letras_incorrectas)}"))
        self.label_mostrar_intentos.config(bg = rgb((84,146,203)), font = ("Courier", 12))
        self.label_mostrar_intentos.place(x = 450, y = 250)
        
        Ahorcado.asignar_letra_botones(self)
        Ahorcado.mostrar_letra_de_palabra(self)    
        self.root.mainloop()
        
    def codigo_boton1(self):
        if self.letras_botones[0] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[0])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[0])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1 
            Ahorcado.mostrar_mono(self)
        self.boton1.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)       
                
                  
    def codigo_boton2(self):
        if self.letras_botones[1] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[1])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[1])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self) 
        self.boton2.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)       
        
    def codigo_boton3(self):
        if self.letras_botones[2] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[2])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[2])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton3.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)        
        
    def codigo_boton4(self):
        if self.letras_botones[3] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[3])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[3])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton4.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)        
        
    def codigo_boton5(self):
        if self.letras_botones[4] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[4])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[4])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton5.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)            
        
    def codigo_boton6(self):
        if self.letras_botones[5] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[5])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[5])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton6.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)        
        
    def codigo_boton7(self):
        if self.letras_botones[6] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[6])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[6])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton7.config(state = "disabled")  
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)      
        
    def codigo_boton8(self):
        if self.letras_botones[7] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[7])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[7])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton8.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)        
        
    def codigo_boton9(self):
        if self.letras_botones[8] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[8])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[8]) 
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton9.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)        
        
    def codigo_boton10(self):
        if self.letras_botones[9] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[9])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[9])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton10.config(state = "disabled")  
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)          
    
    def codigo_boton11(self):
        if self.letras_botones[10] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[10])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[10])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton11.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
    
    def codigo_boton12(self):
        if self.letras_botones[11] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[11])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[11])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton12.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
        
    def codigo_boton13(self):
        if self.letras_botones[12] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[12])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[12])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton13.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
        
    def codigo_boton14(self):
        if self.letras_botones[13] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[13])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[13])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton14.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
        
    def codigo_boton15(self):
        if self.letras_botones[14] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[14])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[14])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton15.config(state = "disabled")        
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)    
    
    def codigo_boton16(self):
        if self.letras_botones[15] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[15])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[15])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton16.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
    
    def codigo_boton17(self):
        if self.letras_botones[16] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[16])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[16])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton17.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
    
    def codigo_boton18(self):
        if self.letras_botones[17] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[17])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[17])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton18.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
    
    def codigo_boton19(self):
        if self.letras_botones[18] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[18])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[18])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton19.config(state = "disabled")
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
     
    def codigo_boton20(self):
        if self.letras_botones[19] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[19])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[19])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton20.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
        
    def codigo_boton21(self):
        if self.letras_botones[20] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[20])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[20])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton21.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self) 
     
    def codigo_boton22(self):
        if self.letras_botones[21] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[21])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[21])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton22.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)  
        
    def codigo_boton23(self):
        if self.letras_botones[22] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[22])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[22])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton23.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)
        
    def codigo_boton24(self):
        if self.letras_botones[23] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[23])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[23])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton24.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self) 
     
    def codigo_boton25(self):
        if self.letras_botones[24] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[24])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[24])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton25.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self) 
      
    def codigo_boton26(self):
        if self.letras_botones[25] in self.palabra_a_adivinar:
            pos = self.palabra_a_adivinar.index(self.letras_botones[25])
            raya = self.rayas[pos]
            raya.config(state = "normal")
            raya.insert(INSERT, self.letras_botones[25])
            raya.config(state = "disabled")
            self.contador_letras_correctas += 1
        else:
            self.contador_letras_incorrectas -= 1
            Ahorcado.mostrar_mono(self)
        self.boton26.config(state = "disabled") 
        Ahorcado.ganaste(self)
        Ahorcado.perdiste(self)                   
              
    def asignar_letra_botones(self):
        cont = 0
        for boton in self.botones:
            boton.config(text = self.letras_botones[cont])
            cont += 1
    
    def ganaste(self):
        if self.contador_letras_correctas == (len(self.palabra_a_adivinar) - 1):
            messagebox.showinfo("FELICIDADES","FELICIDADES GANASTE")
            Ahorcado.reiniciar_juego(self)
    
    def perdiste(self):
        self.label_mostrar_intentos.config(text = (f"Intentos: {self.contador_letras_incorrectas}"))
        if self.contador_letras_incorrectas == 0:
            for boton in self.botones:
                boton.config(state = "disabled")
            
    
    def reiniciar_juego(self):
        for boton in self.botones:
            boton.config(state = "normal")
        for raya in self.rayas:
            raya.config(state = "normal")
            raya.delete(1.0, "end") 
            raya.config(state = "disabled")
            
        self.contador_letras_incorrectas = 6
        self.contador_letras_correctas = 0
        self.label_mostrar_intentos.config(text = (f"Intentos: {self.contador_letras_incorrectas}"))
        self.palabra_a_adivinar = random.choice(self.palabras)
        self.imagen = PhotoImage(file = "imagenes/Fondo.png")
        self.pizarra.config(image = self.imagen) 
             
        Ahorcado.asignar_letra_botones(self)
        Ahorcado.mostrar_letra_de_palabra(self)
        
    def mostrar_letra_de_palabra(self):
        a = random.randint(0, (len(self.palabra_a_adivinar) - 1))

        self.rayas[a].config(state = "normal")
        self.rayas[a].insert(INSERT,self.palabra_a_adivinar[a])
        self.rayas[a].config(state = "disabled")
        
        b = self.letras_botones.index(self.palabra_a_adivinar[a])
        self.botones[b].config(state = "disabled") 
           
    def mostrar_mono(self):
        if self.contador_letras_incorrectas == 5:
            self.imagen = PhotoImage(file="imagenes/Cuerda.png")
            self.pizarra.config(image = self.imagen)
        
        elif self.contador_letras_incorrectas == 4:
            self.imagen = PhotoImage(file="imagenes/Cabeza.png")
            self.pizarra.config(image = self.imagen)
        
        elif self.contador_letras_incorrectas == 3:
            self.imagen = PhotoImage(file="imagenes/Cuerpo.png")
            self.pizarra.config(image = self.imagen)
        
        elif self.contador_letras_incorrectas == 2:
            self.imagen = PhotoImage(file="imagenes/Brazos.png")
            self.pizarra.config(image = self.imagen)
        
        elif self.contador_letras_incorrectas == 1:
            self.imagen = PhotoImage(file="imagenes/Piernas.png")
            self.pizarra.config(image = self.imagen)
        
        elif self.contador_letras_incorrectas == 0:
            self.imagen = PhotoImage(file="imagenes/Death.png")
            self.pizarra.config(image = self.imagen)                                                    
                         
                                                   
        
ahorcado = Ahorcado()                  
