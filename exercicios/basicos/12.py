rendTrib = int(input('Digite um valor a ser tributado: '))

imposto = 0

if rendTrib <= 10000:
    print('O imposto de renda a ser pago é de: ', imposto)
elif rendTrib > 10000 and rendTrib <= 20000:
    imposto = (rendTrib-10000)*0.1
    print('O imposto de renda a ser pago é de: ', imposto)
else:
    imposto = 10000*0.0 + 10000*0.1 + (rendTrib-20000)*0.2
    print('O imposto de renda a ser pago é de: ', imposto)
    


# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0

#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100

#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)
    