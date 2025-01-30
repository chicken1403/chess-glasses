def generate_fen(piece_positions, active_color='w', castling_rights='KQkq', en_passant='-', halfmove_clock=0, fullmove_number=1):
    """
    Generates a FEN string from a given chessboard position.

    piece_positions: Dictionary mapping (row, col) -> piece symbol.
                     Example: {(0, 0): 'r', (0, 4): 'k', (7, 4): 'K'}
    active_color: 'w' for white to move, 'b' for black.
    castling_rights: Castling availability (e.g., 'KQkq' or '-').
    en_passant: En passant target square (or '-').
    halfmove_clock: Number of half-moves since last capture or pawn move.
    fullmove_number: Full move counter (incremented every black move).
    """
    board = [[' ' for _ in range(8)] for _ in range(8)]
    
    # Place pieces on the board with correct row mapping (flipped)
    for (row, col), piece in piece_positions.items():
        board[7 - row][col] = piece  # Flip row index to match FEN order

    # Convert board to FEN notation
    fen_rows = []
    for row in reversed(board):  # Process rows from 8th rank to 1st
        empty_count = 0
        fen_row = ""
        for cell in row:
            if cell == ' ':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += cell
        if empty_count > 0:
            fen_row += str(empty_count)
        fen_rows.append(fen_row)

    piece_placement = "/".join(fen_rows)

    # Construct final FEN string
    fen = f"{piece_placement} {active_color} {castling_rights} {en_passant} {halfmove_clock} {fullmove_number}"
    return fen

# Example Input: Chessboard with kings and pawns
piece_positions = {
    (0, 4): 'k',  # Black King at e8
    (7, 4): 'K',  # White King at e1
    (1, 4): 'p',  # Black Pawn at e7
    (6, 3): 'P',  # White Pawn at d2
}

fen_string = generate_fen(piece_positions)
print(fen_string)