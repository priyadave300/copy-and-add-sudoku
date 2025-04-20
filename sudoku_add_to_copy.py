# Write your solution here
##here in print_sudoku()we run first main for loop to transverse across each row and then another for loop 
##to transverse across each element of each row from range(0,9). Then we have if condn where we check whether 
##i !=0 and also whether i% 3==0 for row and if yes then print(). then for j !=0 and j%3 ==0 then print " " 
##and then use end and then print eleements and when j is at 8 print() for new line and then return sudoku
def print_sudoku(sudoku: list):
    for i in range(0,9):
        if i !=0 and i % 3 == 0:
            print()
        for j in range(0,9):
            if j !=0 and j % 3 == 0:
                print(" ", end ="")
            if sudoku[i][j]== 0:
                print("_ ", end ="")
            if sudoku[i][j]!= 0:
                print(sudoku[i][j] , end= "")
        print()
    return sudoku

##this function is to print modified sudoku by creating new sudoku which is copying every element of each 
##row of orig sudoku and then taking input of row and then col and then replacing the element with userno
##and then return new sudoku
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku =  [item[:] for item in sudoku]
    row = new_sudoku[row_no]
    row[column_no] = number
    return new_sudoku


if __name__ == "__main__":
    sudoku  = [
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


