from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.generate("490.302.922-02"))

cpfs = [
    "490.302.922-02"
]

print(cpf.validate_list(cpfs))





