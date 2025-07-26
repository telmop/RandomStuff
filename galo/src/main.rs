use std::collections::HashMap;
use std::env;
use std::fmt;
use std::io;

const SIDE: usize = 3;
const SIZE: usize = SIDE * SIDE;

#[derive(Clone, Copy, Debug, PartialEq)]
enum Piece {
    O,
    X,
}

impl Piece {
    fn swap(&self) -> Self {
        use crate::Piece::{O, X};
        match *self {
            O => X,
            X => O,
        }
    }
}

impl fmt::Display for Piece {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            Piece::O => write!(f, "O"),
            Piece::X => write!(f, "X"),
        }
    }
}

#[derive(PartialEq)]
enum BoardPos {
    Empty(usize),
    Played(Piece),
}

impl fmt::Display for BoardPos {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match *self {
            BoardPos::Empty(n) => write!(f, "{}", n),
            BoardPos::Played(piece) => write!(f, "{}", piece),
        }
    }
}

struct Board {
    board: Vec<BoardPos>,
}

impl fmt::Display for Board {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for (i, pos) in self.board.iter().enumerate() {
            write!(f, "{}", pos)?;
            if i % SIDE == SIDE - 1 {
                write!(f, "\n")?;
            } else if i != SIZE - 1 {
                write!(f, "|")?;
            }
        }
        Ok(())
    }
}

impl Board {
    fn new() -> Self {
        Board {
            board: (1..=SIZE).map(|i| BoardPos::Empty(i)).collect(),
        }
    }

    fn play(&mut self, pos: usize, piece: Piece) -> Option<()> {
        if pos < 1 || pos > SIZE {
            return None;
        }
        match &self.board[pos - 1] {
            BoardPos::Empty(_) => {
                self.board[pos - 1] = BoardPos::Played(piece);
                Some(())
            }
            _ => None,
        }
    }

    // For internal use only. Used in minmax.
    fn undo_play(&mut self, pos: usize) {
        self.board[pos - 1] = BoardPos::Empty(pos);
    }

    fn get_empty_positions(&self) -> Vec<usize> {
        self.board
            .iter()
            .filter_map(|x| match x {
                BoardPos::Empty(n) => Some(*n),
                _ => None,
            })
            .collect()
    }

    fn is_winner(&self, piece: Piece) -> bool {
        let pos = BoardPos::Played(piece);
        let player_pieces: Vec<bool> = self.board.iter().map(|x| *x == pos).collect();

        // Horizontal lines.
        for row in 0..SIDE {
            if (0..SIDE)
                .map(|i| (i + row * SIDE))
                .all(|i| player_pieces[i])
            {
                return true;
            }
        }

        // Vertical lines.
        for col in 0..SIDE {
            if (col..SIZE).step_by(SIDE).all(|i| player_pieces[i]) {
                return true;
            }
        }

        // Diagonal lines.
        if (0..SIZE).step_by(SIDE + 1).all(|i| player_pieces[i]) {
            return true;
        }
        if (SIDE - 1..SIZE - 1)
            .step_by(SIDE - 1)
            .all(|i| player_pieces[i])
        {
            return true;
        }
        false
    }

    fn get_winner(&self) -> Option<Piece> {
        if self.is_winner(Piece::O) {
            Some(Piece::O)
        } else if self.is_winner(Piece::X) {
            Some(Piece::X)
        } else {
            None
        }
    }

    fn has_ended(&self) -> bool {
        if !self.get_winner().is_none() {
            return true;
        }

        for piece in &self.board {
            match *piece {
                BoardPos::Empty(_) => return false,
                _ => (),
            }
        }
        true
    }
}

fn read_choice() -> usize {
    println!("Pick you choice [1-9]: ");
    loop {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Error reading user input");
        if input.trim() == "q" {
            std::process::exit(0);
        }
        match input.trim().parse::<usize>() {
            Ok(n) => {
                if n >= 1 && n <= SIZE {
                    return n;
                }
            }
            _ => (),
        }
        println!("Invalid choice. Pick your choice [1-9]: ");
    }
}

type Score = isize;

struct Agent {
    map: HashMap<String, (usize, Score)>,
}

impl Agent {
    fn new() -> Self {
        let mut agent = Agent {
            map: HashMap::new(),
        };
        agent.initialize();
        agent
    }

    fn initialize(&mut self) {
        let mut board = Board::new();
        let player = Piece::O; // O starts.
        self.minimax(&mut board, player);
    }

    fn score_board(&self, board: &Board, player: Piece) -> Option<Score> {
        if !board.has_ended() {
            return None;
        }
        match board.get_winner() {
            Some(w) => {
                if w == player {
                    Some(1)
                } else {
                    Some(-1)
                }
            }
            None => Some(0),
        }
    }

    fn serialize(&self, board: &Board, player: Piece) -> String {
        format!("{}:{}", player, board)
    }

    fn minimax_score(&mut self, board: &mut Board, player: Piece, pos: usize) -> Score {
        board.play(pos, player);
        let serialized = self.serialize(board, player);
        if let Some(pos_score) = self.map.get(&serialized) {
            board.undo_play(pos);
            return pos_score.1;
        }

        if let Some(score) = self.score_board(board, player) {
            self.map.insert(serialized, (pos, score));
            board.undo_play(pos);
            return score;
        }

        // Negative score because the current player wins when the next loses.
        let score = -self.minimax(board, player.swap());
        self.map.insert(serialized, (pos, score));
        board.undo_play(pos);
        score
    }

    fn minimax(&mut self, board: &mut Board, player: Piece) -> Score {
        let best_pos_score = board.get_empty_positions()
            .into_iter()
            .map(|pos| (pos, self.minimax_score(board, player, pos)))
            .max_by_key(|pos_score| pos_score.1)
            .unwrap();
        let serialized = self.serialize(board, player);
        self.map.insert(serialized, best_pos_score);
        best_pos_score.1
    }

    fn play(&self, board: &Board, player: Piece) -> usize {
        let serialized = self.serialize(board, player);
        self.map[&serialized].0
    }
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    let mut player_piece = Piece::O;
    if args.len() == 1 && args[0] == "--start" {
        player_piece = Piece::X;
    }

    let agent = Agent::new();
    let mut board = Board::new();
    let ai_piece = player_piece.swap();
    if ai_piece == Piece::O {
        // AI starts.
        let _ = board.play(agent.play(&board, ai_piece), ai_piece);
    }
    println!("{}", board);
    loop {
        let choice = read_choice();
        if board.play(choice, player_piece).is_none() {
            println!("{} was already played!", choice);
        }
        if !board.has_ended() {
            board.play(agent.play(&board, ai_piece), ai_piece);
            println!("{}", board);
        }
        if board.has_ended() {
            break;
        }
    }
}
