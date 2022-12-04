#Julian Ricardo Calvo Montoya
#Edwin Steven Bernal Morales
#Para el correcto funcionamiento los botones de +, -, * y / para obtener su resultado siempre se debe dar en igual
#Solo se suma, restan, dividen o multiplican de a dos numeros
#El resto de los botones de funciones dan el resultado con el numero ingresado o el que esta en el label
#Se importa math para el uso de seno, coseno y tangente
import math
from calculadora1_ui import * #Se importa el archivo .py que contiene todos los botones pero en codigo
result=0 #Variable numerica que se utilizara en las funciones
resultado='' #Variable str que se usara en la interfaz
num=0 #Variable que guarda los numeros ingresados
num1=0 #Variable numerica que tendra el primer numero en la operacion o el unico numero en la operacion
num2=0 #Variable numeroca que tendra el segundo numero en la operacion.
opcion=0 #Variable que conectara las funciones de +,-,*,/ con el igual
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Creacion de la clase para manejar la interfaz
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        global num1, num2, result #Llamada a las variables  a utilizar
        #Conexion de los botones al hacer click en ellos con las funciones que ejecutaran
        self.btn_suma.clicked.connect(self.suma)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_multiplicacion.clicked.connect(self.multiplicacion)
        self.btn_division.clicked.connect(self.division)
        self.btn_mas_menos.clicked.connect(self.mas_menos)
        self.btn_porcentaje.clicked.connect(self.porcentaje)
        self.btn_num1.clicked.connect(self.numero1)
        self.btn_num2.clicked.connect(self.numero2)
        self.btn_num3.clicked.connect(self.numero3)
        self.btn_num4.clicked.connect(self.numero4)
        self.btn_num5.clicked.connect(self.numero5)
        self.btn_num6.clicked.connect(self.numero6)
        self.btn_num7.clicked.connect(self.numero7)
        self.btn_num8.clicked.connect(self.numero8)
        self.btn_num9.clicked.connect(self.numero9)
        self.btn_num0.clicked.connect(self.numero0)
        self.btn_punto.clicked.connect(self.punto_)
        self.btn_igual.clicked.connect(self.igual)
        self.btn_sin.clicked.connect(self.seno)
        self.btn_cos.clicked.connect(self.coseno)
        self.btn_tan.clicked.connect(self.tan)
        self.btn_clear.clicked.connect(self.clear)
    #Creacion de las funciones que se ejecutaran a dar click sobre los numeros de interfaz
    def numero1 (self):
        global resultado, num #Se llaman las variables a utilizar 
        num=1 #Se le asiga el numero que corresponde al boton
        num=str(num) #Se pasa a string para usarlo en la interfaz
        resultado=resultado+num #A ese string se le va concatenando cada numero clickeado
        self.lbl_num.setText(resultado) #Se va mostrando el numero en el label
    def numero2(self):
        global resultado,num
        num=2
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero3 (self):
        global resultado,num
        num=3
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero4 (self):
        global resultado,num
        num=4
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero5 (self):
        global resultado,num
        num=5
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero6 (self):
        global resultado, num
        num=6
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero7 (self):
        global resultado, num
        num=7
        num=str(num1)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero8 (self):
        global resultado, num
        num=8
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero9 (self):
        global resultado, num
        num=9
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def numero0 (self):
        global resultado, num
        num=0
        num=str(num)
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    def punto_(self):
        global resultado, num
        num='.'
        resultado=resultado+num
        self.lbl_num.setText(resultado)
    #Creacion de las funciones operacionales 
    def suma(self):
        global resultado,opcion #Se llaman las variables a utilizar
        self.lbl_res.setText(resultado) #Se pasa lo que hay dentro de la variable resultado al segundo label
        self.lbl_num.clear()#Se limpia el primer label
        resultado=''#se vuelve la variable a vacio para volverla a usar
        opcion=1# si se necesita el igual se le da el numero de opcion de la funcion a utilizar
    def resta(self):
        global resultado,opcion
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        resultado=''
        opcion=2
    def multiplicacion(self):
        global resultado,opcion
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        resultado=''
        opcion=3
    def division(self):
        global resultado,opcion
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        resultado=''
        opcion=4
    def porcentaje(self):
        global resultado,num1,result
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        num1=float(self.lbl_res.text()) #Se toma lo que hay dentro del label para pasarlo a numero y poder realizar la operacion
        result=num1/100
        resultado=str(result) #se devuelve el resultado a string
        self.lbl_num.setText(resultado)#Se pone el resutlado en el primer label
    def mas_menos(self):
        global resultado,num1,result
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        num1=float(self.lbl_res.text())
        result=num1*-1
        resultado=str(result)
        self.lbl_num.setText(resultado) 
    def seno(self):
        global resultado,num1,result
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        num1=float(self.lbl_res.text())
        result=math.sin(num1) #Para esta operacion se utiliza la libreria math 
        resultado=str(result)
        self.lbl_num.setText(resultado) 
    def coseno(self):
        global resultado,num1,result
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        num1=float(self.lbl_res.text())
        result=math.cos(num1)
        resultado=str(result)
        self.lbl_num.setText(resultado) 
    def tan(self):
        global resultado,num1,result
        self.lbl_res.setText(resultado)
        self.lbl_num.clear()
        num1=float(self.lbl_res.text())
        result=math.tan(num1)
        resultado=str(result)
        self.lbl_num.setText(resultado) 
    def clear(self):
        global result,num1,num2,num,opcion,resultado
        result=0
        num1=0
        num2=0
        num=0
        opcion=0
        resultado=''
        self.lbl_num.clear()
        self.lbl_res.clear()
    #Funcion principal que devolvera los resultados de +,-,*,/
    def igual (self):
        global num1, num2, result, opcion, resultado #Se llaman las variables a utilizar
        if opcion ==1:
            num1=float(self.lbl_res.text())#Se toma lo que hay en el segundo label con primer numero
            num2=float(self.lbl_num.text())#Se toma lo que hay en el primer label como numero dos
            result=num1+num2
            resultado=str(result)
            self.lbl_num.setText(resultado)#Se devuelve el resultado a string y se imprime en el primer label
            self.lbl_res.setText('')#Se limpia el segundo label
        elif opcion ==2:
            num1=float(self.lbl_res.text())
            num2=float(self.lbl_num.text())
            result=num1-num2
            resultado=str(result)
            self.lbl_num.setText(resultado)
            self.lbl_res.setText('')
        elif opcion ==3:
            num1=float(self.lbl_res.text())
            num2=float(self.lbl_num.text())
            result=num1*num2
            resultado=str(result)
            self.lbl_num.setText(resultado)
            self.lbl_res.setText('')
        elif opcion ==4:
            try:
                num1=float(self.lbl_res.text())
                num2=float(self.lbl_num.text())
                result=num1/num2
                resultado=str(result)
                self.lbl_num.setText(resultado)
                self.lbl_res.setText('')
            except ZeroDivisionError:
                self.lbl_num.setText("Error matematico")
                self.lbl_res.setText('')
#Funcion que ejecuta la interfaz
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




    
    