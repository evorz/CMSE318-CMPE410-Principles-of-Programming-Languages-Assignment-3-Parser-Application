class Parser:
    def __init__(self, file_name):
        self.file = open("Assaignment3 CMSE318\CMSE318-CMPE410-Principles-of-Programming-Languages-Assignment-3-Parser-Application\input.txt", 'r')
        self.error = False
        self.next_token = ''
    
    def lex(self):
        self.next_token = self.file.read(1)
        while self.next_token.isspace():
            self.next_token = self.file.read(1)
    
    def unconsumed_input(self):
        return self.file.read() + '$'
    
    def G(self):
        self.lex()
        print("G -> E")
        self.E()
        if self.next_token == '$' and not self.error:
            print("success")
        else:
            print(f"failure: unconsumed input = {self.unconsumed_input()}")
    
    def E(self):
        if self.error:
            return
        print("E -> T R")
        self.T()
        self.R()
    
    def R(self):
        if self.error:
            return
        if self.next_token == '+':
            print("R -> + T R")
            self.lex()
            self.T()
            self.R()
        elif self.next_token == '-':
            print("R -> - T R")
            self.lex()
            self.T()
            self.R()
        else:
            print("R -> ε")
    
    def T(self):
        if self.error:
            return
        print("T -> F S")
        self.F()
        self.S()
    
    def S(self):
        if self.error:
            return
        if self.next_token == '*':
            print("S -> * F S")
            self.lex()
            self.F()
            self.S()
        elif self.next_token == '/':
            print("S -> / F S")
            self.lex()
            self.F()
            self.S()
        else:
            print("S -> ε")
    
    def F(self):
        if self.error:
            return
        if self.next_token == '(':
            print("F -> ( E )")
            self.lex()
            self.E()
            if self.next_token == ')':
                self.lex()
            else:
                self.error = True
                print(f"error: unexpected token {self.next_token}")
                print(f"unconsumed input = {self.unconsumed_input()}")
                return
        elif self.next_token in 'abcd':
            print("F -> M")
            self.M()
        elif self.next_token in '0123':
            print("F -> N")
            self.N()
        else:
            self.error = True
            print(f"error: unexpected token {self.next_token}")
            print(f"unconsumed input = {self.unconsumed_input()}")
    
    def M(self):
        if self.error:
            return
        if self.next_token in 'abcd':
            print(f"M -> {self.next_token}")
            self.lex()
        else:
            self.error = True
            print(f"error: unexpected token {self.next_token}")
            print(f"unconsumed input = {self.unconsumed_input()}")
    
    def N(self):
        if self.error:
            return
        if self.next_token in '0123':
            print(f"N -> {self.next_token}")
            self.lex()
        else:
            self.error = True
            print(f"error: unexpected token {self.next_token}")
            print(f"unconsumed input = {self.unconsumed_input()}")

def main():
    parser = Parser('Assaignment3 CMSE318\CMSE318-CMPE410-Principles-of-Programming-Languages-Assignment-3-Parser-Application\input.txt')
    parser.G()

if __name__ == '__main__':
    main()
