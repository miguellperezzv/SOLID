# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:24:07 2019

@author: personal
"""

class ProdAseo:
   codigo=1
   def get_name(self) -> str:
        pass
   def get_codigo(self):
       return self.codigo
   def precio(self):
        pass
   def limpiar(self):
        return("Producto para limpieza")
   
        
class ProdComestible:
   codigo=2
   def get_name(self) -> str:
        pass
   def get_codigo(self):
       return self.codigo
   def precio(self):
        pass
   def comer(self):
        return ("Producto comestible")
        
class Producto(ProdAseo, ProdComestible):
    
    
    def get_name(self) -> str:
        pass

    def precio(self):
        pass
   

class Galleta(ProdComestible):
    descuento = False
    
    def __init__(self, name: str):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
    
    def precio(self):
        if(self.descuento==True):
            valor = int(900-(900*0,1))
            return valor
        else:
            return 900
    

class Frituras(ProdComestible):
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name
        
    def precio(self):
        return 1200


class Menta(ProdComestible):
    def __init__(self, name: str):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
        
    def precio(self):
        return 200

class Cloro( ProdAseo):
    def __init__(self, name: str):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
        
    def precio(self):
        return 2000
 
def listar_precios(productos: list):
    for producto in productos:
        print ("codigo", producto.get_codigo())
        if(producto.get_codigo()==1):
            
            print("N:" ,producto.get_name()," V:",producto.precio(), "C",producto.limpiar())
        else:
            print("N:" ,producto.get_name()," V:",producto.precio(), "C",producto.comer())
class Principal:
    
    cond="y"
    productos =[]
    while(cond==("y")):
        numero =int (input("Introduce un numero: \n 1. Galleta \n 2. Frituras \n 3. Menta \n 4. Cloro\n" ))
        if numero ==1 :
            productos.append(Galleta("Galleta"))
        elif (numero == 2):
            productos.append(Frituras("Frituras"))
        elif (numero==3):
            productos.append(Menta("Menta"))
        elif (numero==4):
            productos.append(Cloro("Cloro"))
        cond=input("Continuar y/n?")   
    #print("productos ",productos)   
    
    listar_precios(productos)

    
    

        

        










