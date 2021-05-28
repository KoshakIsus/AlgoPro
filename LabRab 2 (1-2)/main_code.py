pushkin = 'pushkin.txt'
potato = 'pattern.html'
result = pushkin.split('.')[0] + '.html'

f1 = open(pushkin, encoding='utf-8')
lines_f1 = f1.readlines()
f1.close()

fpotato = open(potato, encoding='utf-8')
lines_fpat = fpotato.readlines()
fpotato.close()

#  создание абзацев с разным кол-вом строк в абзацах
parags = []
for parag_lines in ''.join(lines_f1[2:]).split('\n\n'): #  2 переноса = новый абзац
    parags.append('<p>' + '<br>\n'.join(parag_lines.split('\n')) + '</p>\n')

# формируем строки итогового файла
lines_for_public = []
for line in lines_fpat: # читаем из шаблона
    lines_for_public.append(line) # добавляем в итоговый
    if '<title>' in line:
        lines_for_public.append(lines_f1[0].strip())
    if '<body>' in line:
        lines_for_public.extend(parags)

result_final = open(result, mode='w', encoding='utf-8')
result_final.writelines(lines_for_public)
result_final.close()
