import pywhatkit as kit

# Set up the message
message = """
Olá, aqui é da Perícia Médica da Unidade SIASS da UFRN.

Verificamos aqui que o(a) senhor(a) tem um processo para se agendado e, para melhor atende-lo(a), gostaríamos de uma informação...

O(a) senhor(a) está em condições de comparecer presencialmente no DAS da UFRN para passar pela perícia? Caso não esteja em condições, pedimos que nos informe seu endereço completo e sobre a sua situação, justificando o porquê não poderia realizar essa locomoção até nós.

Desde já, agradecemos. E pedimos que aguarde o nosso retorno com relação ao agendamento da perícia.
"""

# Send the message

kit.sendwhatmsg_instantly("+558499479679", message)
kit.sendwhatmsg_instantly("+5584999720867", message)
kit.sendwhatmsg_instantly("+5584999573606", message)
kit.sendwhatmsg_instantly("+5584992120651", message)

