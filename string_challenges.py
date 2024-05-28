# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len([s for s in word if s.lower() == 'а']))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([s for s in word if s.lower() in 'а, я, у, ю, о, е, ё, э, и, ы']))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*([w[0] for w in sentence.split()]), sep='\n')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(int(sum([len(w) for w in sentence.split()]) / 4))