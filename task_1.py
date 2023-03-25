import random
n_set = set(random.randint(1, 10) for k in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(random.randint(1, 10) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)