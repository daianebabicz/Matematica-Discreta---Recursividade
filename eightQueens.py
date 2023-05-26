def is_safe(board, row, col):
    # Verificar a linha no lado esquerdo
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Verificar diagonal superior
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Verificar diagonal inferior
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # Caso base: se todas as rainhas estão posicionadas
    if col >= len(board):
        return True

    # Considerar essa coluna e tentar colocar a rainha em todas as linhas uma por uma
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Colocar a rainha nesta posição
            board[i][col] = 1

            # Recursão para colocar o resto das rainhas
            if solve_n_queens(board, col + 1):
                return True

            # Se colocar a rainha na posição do tabuleiro não levar a uma solução, então remover rainha
            board[i][col] = 0

    # Se a rainha não puder ser colocada em nenhuma linha nesta coluna, retornar falso
    return False

def solve():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if not solve_n_queens(board, 0):
        print("Solução não encontrada")
    else:
        for row in board:
            print(row)

solve()
