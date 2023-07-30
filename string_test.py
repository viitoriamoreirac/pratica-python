string_test = "essa é uma frase para teste"

print (string_test, "- frase original")
print()

print (string_test.upper(), "(upper torna tudo maiusculo)")
print()

print (string_test.lower(), "(lower torna tudo minusculo)")
print()

print (string_test.capitalize(), "(capitalize torna a primeira letra da frase minuscula)")
print()

print (string_test.count("e"), "(.count(e), quantas vezes a letra e aparece)")
print()

print ("'.strip()' tira os espaços antes e depois da frase, porém essa não tem")
print()

print (string_test.replace("para teste", "muito legal"),"- .replace('para teste','muito legal'), substitui uma parte da frase")
print()

print (string_test.center(80))
print ("acima a frase foi centralizada com '.center(80)'")
print()

print (string_test.find("f"), "(.find(f) - encontra onde ocorre a primeira vez do string f na frase)")
print()

print ("ord('a') mostra a numeração de a, que é:",ord('a'))

