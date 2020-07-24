# 2. Заканчиваем прошлые задачи,
# украшаем работу физбазов работой со строками,
# списками, пробуем генераторы списков и прочие новые красоты, которые выучили.
# Доводим код до идеала!



fizz = int(input("Type the first number here: "))
buzz = int(input("Type the second number here: "))
n = int(input("Type the third number here: "))


print(" ".join(["FizzBuzz" if not i % fizz and not i % buzz else "Fizz" if not i%fizz else "Buzz" if not i%buzz else str(i) for i in range(1, n+1)]))