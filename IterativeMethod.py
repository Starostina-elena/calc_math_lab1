class IterativeMethod:

    matrix = []
    right_matrix = []
    n = 0
    cur_iter_x = []
    cur_iter_number = -1
    new_iter_x = []
    eps = 0.1
    delta = []

    def __init__(self, matrix, right_matrix, n, eps):
        self.matrix = matrix
        self.right_matrix = right_matrix
        self.n = n
        self.cur_iter_x = [0] * n
        self.new_iter_x = [0] * n
        self.eps = eps
        self.delta = [0] * n
        if not self.check_diagonal():
            print('Need to permutate matrix')
            self.permutate_matrix()
        if not self.check_diagonal():
            print('Diagonal elements are not dominant, quit')
            return
        norm = self.calc_norm()
        if norm > 1:
            print('Norm > 1, quit')
            return
        self.go()

    def make_iteration(self):
        self.cur_iter_number += 1
        for i in range(self.n):
            new_x = self.right_matrix[i] / self.matrix[i][i]
            for j in range(self.n):
                if j != i:
                    new_x -= self.matrix[i][j] / self.matrix[i][i] * self.cur_iter_x[j]
            self.new_iter_x[i] = new_x

    def check_stop(self):
        for i in range(self.n):
            if abs(self.new_iter_x[i] - self.cur_iter_x[i]) > self.eps:
                self.cur_iter_x = self.new_iter_x.copy()
                return False
            self.delta[i] = abs(self.new_iter_x[i] - self.cur_iter_x[i])
        return True

    def go(self):
        self.make_iteration()
        while not self.check_stop():
            if self.cur_iter_number >= 1000:
                print('Too many iterations')
                return
            self.make_iteration()
        print('Number of iterations:', self.cur_iter_number)
        print('Result:', self.new_iter_x)
        print('Delta:', self.delta)

    def check_diagonal(self):
        flag = False
        for i in range(self.n):
            summ = 0
            for j in range(self.n):
                if i != j:
                    summ += abs(self.matrix[i][j])
            if abs(self.matrix[i][i]) < summ:
                return False
            if abs(self.matrix[i][i]) > summ:
                flag = True
        return flag

    def permutate_matrix(self):
        for _ in range(self.n):
            for i in range(self.n):
                max_el = self.matrix[i][i]
                correct_row = i
                for j in range(self.n):
                    if i != j and abs(self.matrix[i][j]) > max_el:
                        max_el = self.matrix[i][j]
                        correct_row = j
                self.matrix[i], self.matrix[correct_row] = self.matrix[correct_row], self.matrix[i]
                self.right_matrix[i], self.right_matrix[correct_row] = self.right_matrix[correct_row], self.right_matrix[i]
        print('Permutated matrix:', self.matrix)
        print('Permutated right matrix:', self.right_matrix)

    def calc_norm(self):
        res = 0
        for i in range(self.n):
            summ = 0
            for j in range(self.n):
                if i != j:
                    try:
                        summ += abs(self.matrix[i][j] / self.matrix[i][i])
                    except ZeroDivisionError:
                        print('Matrix norm: inf')
                        return 1000
            res = max(res, summ)
        print('Matrix norm:', res)
        return res
