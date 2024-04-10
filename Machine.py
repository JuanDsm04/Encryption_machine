class Machine:
    def __init__(self):
        self.diccionario = {}

    def agregar_letra(self, letra, caracter):
        self.diccionario[letra] = caracter

    def codificar_frase(self, frase):
        palabras = frase.split()
        frase_codificada = ""

        for palabra in palabras:
            palabra_codificada = ""
            for letra in palabra:
                if letra in self.diccionario:
                    palabra_codificada += self.diccionario[letra]
                else:
                    palabra_codificada += letra
            frase_codificada += palabra_codificada + " "

        return frase_codificada.strip()
    
    def encontrar_llave(self, value):
        for llave, val in self.diccionario.items():
            if val == value:
                return llave
        
    def decodificar_frase(self, codigo):
        palabras = codigo.split()
        codigo_decodificado = ""

        for palabra in palabras:
            palabra_decodificada = ""
            for caracter in palabra:
                if caracter in self.diccionario.values():
                    palabra_decodificada += machine.encontrar_llave(caracter)
                else:
                    palabra_decodificada += caracter
            codigo_decodificado += palabra_decodificada + " "
        return codigo_decodificado.strip()


machine = Machine()
machine.agregar_letra('A', '@')
machine.agregar_letra('a', '#')
machine.agregar_letra('B', '$')
machine.agregar_letra('b', '%')
machine.agregar_letra('C', '&')
machine.agregar_letra('c', '*')
machine.agregar_letra('Ch', '+')
machine.agregar_letra('ch', '/')
machine.agregar_letra('D', '=')
machine.agregar_letra('d', 'ö')
machine.agregar_letra('E', '!')
machine.agregar_letra('e', ';')
machine.agregar_letra('F', ':')
machine.agregar_letra('f', ',')
machine.agregar_letra('G', '.')
machine.agregar_letra('g', '<')
machine.agregar_letra('H', '>')
machine.agregar_letra('h', '(')
machine.agregar_letra('I', ')')
machine.agregar_letra('i', '[')
machine.agregar_letra('J', ']')
machine.agregar_letra('j', '{')
machine.agregar_letra('K', '}')
machine.agregar_letra('k', '|')
machine.agregar_letra('L', '^')
machine.agregar_letra('l', '"')
machine.agregar_letra('Ll', "'")
machine.agregar_letra('ll', '~')
machine.agregar_letra('M', '_')
machine.agregar_letra('m', '-')
machine.agregar_letra('N', '×')
machine.agregar_letra('n', '¿')
machine.agregar_letra('Ñ', '¡')
machine.agregar_letra('ñ', '?')
machine.agregar_letra('O', '»')
machine.agregar_letra('o', '«')
machine.agregar_letra('P', '£')
machine.agregar_letra('p', '¥')
machine.agregar_letra('Q', '¢')
machine.agregar_letra('q', '­­­÷')
machine.agregar_letra('R', '♥')
machine.agregar_letra('r', 'æ')
machine.agregar_letra('S', 'Ø')
machine.agregar_letra('s', '¶')
machine.agregar_letra('T', '↑')
machine.agregar_letra('t', '♦')
machine.agregar_letra('U', '♀')
machine.agregar_letra('u', '♫')
machine.agregar_letra('V', '♪')
machine.agregar_letra('v', '▲')
machine.agregar_letra('W', '►')
machine.agregar_letra('w', '◄')
machine.agregar_letra('X', '♣')
machine.agregar_letra('x', '→')
machine.agregar_letra('Y', '↕')
machine.agregar_letra('y', '◘')
machine.agregar_letra('Z', 'ƒ')
machine.agregar_letra('z', '±')

frase_usuario = input("Ingrese una frase: ")
frase_codificada = machine.codificar_frase(frase_usuario)
print("Frase convertida:", frase_codificada)
print('Frase a encontrar: '+frase_codificada)
print('Frase decodificada: '+machine.decodificar_frase(frase_codificada))