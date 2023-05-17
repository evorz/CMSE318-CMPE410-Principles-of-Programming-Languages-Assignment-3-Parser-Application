class Parser:
    def __init__(self, file_name):
        self.file = open("Assaignment3 CMSE318\\CMSE318-CMPE410-Principles-of-Programming-Languages-Assignment-3-Parser-Application\\input.txt", 'r')
        self.error = False
        self.next_token = ''
    
    def lex(self):
        # Reads the next character from the input file and stores it as the next token
        self.next_token = self.file.read(1)
        # Skips any whitespace characters
        while self.next_token.isspace():
            self.next_token = self.file.read(1)
    
    def unconsumed_input(self):
        # Returns the remaining unconsumed input in the file along with '$' signifying the end of input
        return self.file.read() + '$'
    
    def G(self):
        # Starting symbol G
        self.lex()
        print("G -> E")
        # Non-terminal E
        self.E()
        if self.next_token == '$' and not self.error:
            # Successful parsing if all input is consumed and no error occurred
            print("success")
        else:
            # Parsing failure if there is unconsumed input or an error occurred
            print(f"failure: unconsumed input = {self.unconsumed_input()}")
    
    def E(self):
        if self.error:
            return
        print("E -> T R")
        # Non-terminal T
        self.T()
        # Non-terminal R
        self.R()
    
    def R(self):
        if self.error:
            return
        if self.next_token == '+':
            print("R -> + T R")
            self.lex()
            # Non-terminal T
            self.T()
            # Non-terminal R
            self.R()
        elif self.next_token == '-':
            print("R -> - T R")
            self.lex()
            # Non-terminal T
            self.T()
            # Non-terminal R
            self.R()
        else:
            # Empty production (epsilon)
            print("R -> ε")
    
    def T(self):
        if self.error:
            return
        print("T -> F S")
        # Non-terminal F
        self.F()
        # Non-terminal S
        self.S()
    
    def S(self):
        if self.error:
            return
        if self.next_token == '*':
            print("S -> * F S")
            self.lex()
            # Non-terminal F
            self.F()
            # Non-terminal S
            self.S()
        elif self.next_token == '/':
            print("S -> / F S")
            self.lex()
            # Non-terminal F
            self.F()
            # Non-terminal S
            self.S()
        else:
            # Empty production (epsilon)
            print("S -> ε")
    
    def F(self):
        if self.error:
            return
        if self.next_token == '(':
            print("F -> ( E )")
            self.lex()
            # Non-terminal E
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
            # Non-terminal M
            self.M()
        elif self.next_token in '0123':
            print("F -> N")
            # Non-terminal N
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
    # Create a Parser instance and parse the input
    parser = Parser('Assaignment3 CMSE318\\CMSE318-CMPE410-Principles-of-Programming-Languages-Assignment-3-Parser-Application\\input.txt')
    parser.G()

if __name__ == '__main__':
    main()
