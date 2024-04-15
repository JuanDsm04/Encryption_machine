class Machine:
    def __init__(self):
        self.hashmap = {}
        self.set_keys()

    def add_char(self, character, caracter):
        self.hashmap[character] = caracter

    def encrypt_phrase(self, phrase):
        words = phrase.split()
        encrypted_phrase = ""

        for word in words:
            word_encrypted = ""
            for character in word:
                if character in self.hashmap:
                    word_encrypted += self.hashmap[character]
                else:
                    word_encrypted += character
            encrypted_phrase += word_encrypted + " "

        return encrypted_phrase.strip()
    
    def find_key(self, value):
        for key, val in self.hashmap.items():
            if val == value:
                return key
        
    def reveal_phrase(self, code):
        words = code.split()
        code_decodificado = ""

        for word in words:
            word_deencrypted = ""
            for caracter in word:
                if caracter in self.hashmap.values():
                    word_deencrypted += self.find_key(caracter)
                else:
                    word_deencrypted += caracter
            code_decodificado += word_deencrypted + " "
        return code_decodificado.strip()

    def set_keys(self):
        self.add_char('A', '@')
        self.add_char('a', '#')
        self.add_char('B', '$')
        self.add_char('b', '%')
        self.add_char('C', '&')
        self.add_char('c', '*')
        self.add_char('Ch', '+')
        self.add_char('ch', '/')
        self.add_char('D', '=')
        self.add_char('d', 'ö')
        self.add_char('E', '!')
        self.add_char('e', ';')
        self.add_char('F', ':')
        self.add_char('f', ',')
        self.add_char('G', '.')
        self.add_char('g', '<')
        self.add_char('H', '>')
        self.add_char('h', '(')
        self.add_char('I', ')')
        self.add_char('i', '[')
        self.add_char('J', ']')
        self.add_char('j', '{')
        self.add_char('K', '}')
        self.add_char('k', '|')
        self.add_char('L', '^')
        self.add_char('l', '"')
        self.add_char('Ll', "'")
        self.add_char('ll', '~')
        self.add_char('M', '_')
        self.add_char('m', '-')
        self.add_char('N', '×')
        self.add_char('n', '¿')
        self.add_char('Ñ', '¡')
        self.add_char('ñ', '?')
        self.add_char('O', '»')
        self.add_char('o', '«')
        self.add_char('P', '£')
        self.add_char('p', '¥')
        self.add_char('Q', '¢')
        self.add_char('q', '­­­÷')
        self.add_char('R', '♥')
        self.add_char('r', 'æ')
        self.add_char('S', 'Ø')
        self.add_char('s', '¶')
        self.add_char('T', '↑')
        self.add_char('t', '♦')
        self.add_char('U', '♀')
        self.add_char('u', '♫')
        self.add_char('V', '♪')
        self.add_char('v', '▲')
        self.add_char('W', '►')
        self.add_char('w', '◄')
        self.add_char('X', '♣')
        self.add_char('x', '→')
        self.add_char('Y', '↕')
        self.add_char('y', '◘')
        self.add_char('Z', 'ƒ')
        self.add_char('z', '±')