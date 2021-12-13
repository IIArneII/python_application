class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def is_sheet(self):
        if self.left_child or self.right_child:
            return True
        return False

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t


if __name__ == '__main__':
    tree = BinaryTree('Это млекопитающее?')
    tree.left_child = BinaryTree('Кошка')
    tree.right_child = BinaryTree('Рыба')
    while True:
        print(tree.key)
        answer = input()
        if answer.lower() == 'да':
            if not tree.left_child:
                tree = tree.left_child
            else:
                print('Сдаюсь. Какое животное вы загадали?')
                key = input()
                print(f'Какой вопрос позволит отличить {tree.key} от {key}')
                question = input()
                print(f'Для {key} ответ утвердительный?')
                answer = input().lower()
                tree.insert_left()



        if answer.lower() == 'нет':
            tree = tree.get_right_child()
