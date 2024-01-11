let rows = 6;
let columns = 7;
let board = new Array(rows);

for (let i = 0; i < rows; i++) {
    board[i] = new Array(columns);
  for (let j = 0; j < columns; j++) {
    board[i][j] = 0;
  }
}

console.log(board)