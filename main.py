from IterativeMethod import IterativeMethod

def interact_with_user():
    print('Hello :) Choose the preferable way of input:')
    print('1. From file')
    print('2. From console')
    choice = input()
    while choice != '1' and choice != '2':
        print('Wrong input. Try again:')
        choice = input()
    eps = 0
    n = 0
    matrix = []
    right_matrix = []
    if choice == '1':
        print('Make sure that the first line of the file is epsilon, second is the size of the matrix (<=20), then goes the matrix itself')
        print('Example for {x1 + 2 * x2 = 7 && x1 + x2 = 5}:')
        print(0.01, 2, '1 2 7', '1 1 5', sep='\n')
        print('Enter the name of the file:')
        filename = input()
        try:
            with open(filename) as f:
                eps = float(f.readline().replace(',', '.'))
                n = int(f.readline())
                if n > 20 or n < 1:
                    raise ValueError
                matrix = []
                right_matrix = []
                for i in range(n):
                    line = list(map(float, f.readline().replace(',', '.').split()))
                    if len(line) != n + 1:
                        raise ValueError
                    matrix.append(line[:-1])
                    right_matrix.append(line[-1])
        except FileNotFoundError:
            print('File not found')
            return
        except ValueError or IndexError:
            print('Data is incorrect')
            return
        except Exception as e:
            print('Error while opening the file:', e)
            return
    else:
        eps = input('Enter epsilon: ')
        while True:
            try:
                eps = float(eps.replace(',', '.'))
                break
            except ValueError:
                print('Wrong input, try again')
                eps = input('Enter epsilon: ')
        n = input('Enter the size of the matrix (<=20): ')
        while True:
            try:
                n = int(n)
                if n > 20 or n < 1:
                    raise ValueError
                break
            except ValueError:
                print('Wrong input, try again')
                n = input('Enter the size of the matrix: ')
        print('Enter the matrix. Example: line should be like "1 2 7" for {x1 + 2 * x2 = 7}')
        for i in range(n):
            while True:
                try:
                    line = list(map(float, input().replace(',', '.').split()))
                    if len(line) != n + 1:
                        raise ValueError
                    break
                except ValueError:
                    print('Wrong input, try again')
            matrix.append(line[:-1])
            right_matrix.append(line[-1])
    IterativeMethod(matrix, right_matrix, n, eps)

if __name__ == '__main__':
    interact_with_user()
