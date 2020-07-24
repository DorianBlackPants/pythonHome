#### Задание 3
# Вспоминаем работу с файлом.
# Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и `map`,
# без единого цикла!

def word_counter (words):
   y = { x : words.count(x) for x in words}
   return y

with open ("text.txt") as f:
   x = f.read().split()
   print(word_counter(x))

