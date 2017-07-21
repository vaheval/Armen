#include <iostream>
#include <cstdlib>

struct Possition 
{
	int x;
	int y;
};
typedef struct Possition possition;	

void init_board(int board[][8], int row[], int col[]);
void print_board(int board[][8]);
void set_possition(int board[][8], possition*);
void update_board(int board[][8], possition*, int row[], int col[]);
//void next_cell(int board[][8], possition* curentCell);


int main()
{
	possition* curentCell = (possition*)malloc(sizeof(possition));
	curentCell->x = 0;
	curentCell->y = 0;
	int row [] = {2, 2, -2, -2, 1, 1, -1, -1};
	int col [] = {-1, 1, -1, 1, 2, -2, 2, -2};
	int board[8][8] = {0};
	init_board(board, row, col);
	print_board(board);
	for (int n = 0; n < 64; n ++){
		set_possition(board, curentCell);
		update_board(board, curentCell, row, col);	
	}
	print_board(board);
	return 0;
}

void init_board(int board[][8], int row[], int col[])
{	
	int res = 0;
	for (int x = 0; x < 8; x++){
		for (int y = 0; y < 8; y++){
			for (int i = 0; i < 8; i++){
				if (x+row[i] >= 0 && x + row[i] <8 && y + col[i] >= 0 && y + col[i] <8 ){
					res ++;
				}	
				board[x][y] = res;
			}
				res = 0;
		}
	}
}

void print_board(int board[8][8])
{
	for (int i = 0; i < 8; i++){
		for(int j = 0; j < 8; j++){
			std::cout <<(board[i][j]) << "  ";
		}
			std::cout << "\n";
	}	
}

void set_possition(int board[][8], possition* curentCell)
{
	board[curentCell->x][curentCell->y] = 88;
}

void update_board(int board[][8], possition* curentCell, int row[], int col[])
{	
	int min = 100;
	int x = curentCell->x;
	int y = curentCell->y;
		for (int i = 0; i < 8; i++){
			if (x+row[i] >= 0 && x + row[i] < 8 && y + col[i] >= 0 && y + col[i] < 8){
				if(board[x + row[i]][y + col[i]] != 88){						
					board[x + row[i]][y + col[i]] --;
				}
				if (board[x + row[i]][y + col[i]] < min && board[x + row[i]][y + col[i]] >= 0) {
					min = board[x + row[i]][y + col[i]];
					curentCell->x = x + row[i];
					curentCell->y = y + col[i];	
				}
			}
		}
	
}

//void next_cell(int board[][8], possition* curentCell)
//{
//	
//}



