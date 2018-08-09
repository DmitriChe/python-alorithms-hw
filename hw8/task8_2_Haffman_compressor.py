from collections import Counter, OrderedDict


class MyNode:
    """ Если у узла left=None, right=None, то мы имеем дело с листом (от него нет путей)
        value - это значение узла, т.е. символ из введенной строки
        left или right содеражат экземпляры детей - узлы дерева"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def walk(self, code_dict, code):

        if self.left == self.right:  # если дети одинаковые, то это лист, т.к. детей нет, они = None
            code_dict[self.value] = code or "0"
        else:  # спускаемся в потомков, добавляя к префиксу 0 или 1
            self.left.walk(code_dict, code + "0")
            self.right.walk(code_dict, code + "1")


def huffman_compressor(s):
    # генерируем словарь типа {лист: частота} из словаря частот символов строки Counter(s)
    h = dict([(MyNode(ch), freq) for ch, freq in Counter(s).items()])
    # упорядочиваем словарь по частоте - создаем "очередь" по частотности
    h = OrderedDict(sorted(h.items(), key=lambda x: x[1]))

    while len(h) > 1:  # пока в "очереди"-словаре есть хотя бы 2 элемента
        left, freq1 = h.popitem(last=False)  # вынимаем первый элемент (с минимальной частотой)
        right, freq2 = h.popitem(last=False)  # и следующий элемент (с минимальной частотой)
        next_node = MyNode(left.value + right.value, left, right)
        h[next_node] = freq1 + freq2  # добавление в "очередь" нового узла с суммарной частотой потомков
        h = OrderedDict(sorted(h.items(), key=lambda x: x[1]))  # и снова сортируем по частотности

    code_dict = {}
    if h:
        root = tuple(h)[0]  # извлекаем в перем root последний объект из ключа словаря - хитрым способом!!!
        root.walk(code_dict, "")  # вызываем у объекта обход дерева с корня и заполнение словаря

    print(f'\nСловарь Хаффмана: {code_dict}\n')  # словарь вида {символ: код}
    print('Словарь Хаффмана в удобной форме:')
    for ch in sorted(code_dict):  # вывод упорядоченной по алфавиту таблицы соответствия символ: код
        print(f'{ch}: {code_dict[ch]}')

    encoded_str = "".join(code_dict[ch] for ch in s)  # конкат. финальной строки из кодировочного словаря
    return encoded_str


# s = 'beep boop beer!'
s = input('Введите строку их 3 слов: ')
print(f'\nЗакодированная строка:\n{huffman_compressor(s)}')  # вывод закодированной строки
