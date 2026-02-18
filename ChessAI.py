from ChessGameRules import chessGameRules
from copy import copy, deepcopy
import time
import multiprocessing as mp

class chessGameAI:
	AIgame = chessGameRules();
	chessScore = 0;
	chessBoardCopy=None;
	maxScore = 0;
	minScore = 0;

	def __init__(self):
		self.AIgame = chessGameRules();
		self._transposition = {};
		self._node_count = 0;

	def _iter_moves(self, player):
		if player == "black":
			allMoves = self.generateMovesBlack();
		else:
			allMoves = self.generateMovesWhite();
		for moves in allMoves:
			from_pos = moves[len(moves)-1];
			fx = from_pos[0];
			fy = from_pos[1];
			for i in range(len(moves)-1):
				tx = int(moves[i][0]);
				ty = int(moves[i][2]);
				yield fx, fy, tx, ty;

	def _piece_value(self, piece):
		if piece == "sp":
			return 0;
		p = piece[0];
		if p == "p":
			return 1;
		if p == "n" or p == "b":
			return 3;
		if p == "r":
			return 5;
		if p == "q":
			return 9;
		if p == "k":
			return 100;
		return 0;

	def _ordered_moves(self, player):
		moves = [];
		for fx, fy, tx, ty in self._iter_moves(player):
			captured = self.AIgame.returnChessPieces(tx, ty);
			moves.append((self._piece_value(captured), fx, fy, tx, ty));
		moves.sort(key=lambda m: m[0], reverse=True);
		for _, fx, fy, tx, ty in moves:
			yield fx, fy, tx, ty;

	def _make_move(self, fx, fy, tx, ty):
		moving = self.AIgame.returnChessPieces(fx, fy);
		captured = self.AIgame.returnChessPieces(tx, ty);
		self.AIgame.setChessPieces(tx, ty, moving);
		self.AIgame.setChessPieces(fx, fy, "sp");
		return moving, captured;

	def _undo_move(self, fx, fy, tx, ty, moving, captured):
		self.AIgame.setChessPieces(fx, fy, moving);
		self.AIgame.setChessPieces(tx, ty, captured);

	def _hash_board(self, board, player):
		return (player, tuple(cell[0] for row in board for cell in row));

	
	def generateMovesWhite(self):
		allPiecesMoves=[];
		z=[7,6,5,4,3,2,1,0];
		index = 0;
		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.AIgame.chessBoard[x][y][0];
				tempMove = [y,z[int(x)]];

				if chessPiece == "r1": 
					temp = self.AIgame.findPossibleMovesRook(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "p1": 
					temp = self.AIgame.findPossibleMovesPawn(tempMove, False);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "n1": 
					temp = self.AIgame.findPossibleMovesKnight(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "b1": 
					temp = self.AIgame.findPossibleMovesBishop(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "k1": 
					temp = self.AIgame.findPossibleMovesKing(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "q1": 
					temp = self.AIgame.findPossibleMovesQueen(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);
		return allPiecesMoves;

	def generateMovesBlack(self):
		allPiecesMoves=[];
		z=[7,6,5,4,3,2,1,0];
		index = 0;
		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.AIgame.chessBoard[x][y][0];
				tempMove = [y,z[int(x)]];

				if chessPiece == "r2": 
					temp = self.AIgame.findPossibleMovesRook(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "p2": 
					temp = self.AIgame.findPossibleMovesPawn(tempMove, False);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "n2": 
					temp = self.AIgame.findPossibleMovesKnight(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "b2": 
					temp = self.AIgame.findPossibleMovesBishop(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "k2": 
					temp = self.AIgame.findPossibleMovesKing(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);

				if chessPiece == "q2": 
					temp = self.AIgame.findPossibleMovesQueen(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPiecesMoves.append(temp);
		#self.AIgame.printBoard();
		return allPiecesMoves;


	def PositionEvaluation(self):
		chessScore = 0;

		king = [[-3,-4,-4,-5,-5,-4,-4,-3],
		[-3,-4,-4,-5,-5,-4,-4,-3],
		[-3,-4,-4,-5,-5,-4,-4,-3],
		[-3,-4,-4,-5,-5,-4,-4,-3],
		[-2,-3,-3,-4,-4,-3,-3,-2],
		[-1,-2,-4,-5,-5,-4,-4,-3],
		[2,2,0,0,0,0,2,2],
		[2,3,1,0,0,1,3,2]];

		queen = [[-2,-1,-1,-5,-5,-1,-1,-2],
		[-1,0,0,0,0,0,0,-1],
		[-1,0,5,5,5,5,0,-1],
		[-5,0,5,5,5,5,0,-5],
		[0,0,5,5,5,5,0,-5],
		[-1,5,5,5,5,5,0,-1],
		[-1,0,5,0,0,0,0,-1],
		[-2,-1,-1,-5,-5,-1,-1,-2]];

		rook = [[0,0,0,0,0,0,0,0],
		[5,1,1,1,1,1,1,5],
		[-5,0,0,0,0,0,0,-5],
		[-5,0,0,0,0,0,0,-5],
		[-5,0,0,0,0,0,0,-5],
		[-5,0,0,0,0,0,0,-5],
		[-5,0,0,0,0,0,0,-5],
		[0,0,0,5,5,0,0,0]];

		bishop = [[-2,-1,-1,-1,-1,-1,-1,-2],
		[-1,0,0,0,0,0,0,-1],
		[-1,0,5,1,1,5,0,-1],
		[-1,5,5,1,1,5,5,-1],
		[-1,0,1,1,1,1,0,-1],
		[-1,1,1,1,1,1,1,-1],
		[-1,5,0,0,0,0,5,-1],
		[-2,-1,-1,-1,-1,-1,-1,-2]];

		
		knight = [[-5,-4,-3,-3,-3,-3,-4,-5],
		[-4,-2,0,0,0,0,-2,-4],
		[-3,0,1,1.5,1.5,1,0,-3],
		[-3,0.5,1.5,2,2,1.5,0.5,-3],
		[-3,0.5,1.5,2,2,1.5,0.5,-3],
		[-3,0,1,1.5,1.5,1,0,-3],
		[-4,-2,0,0.5,0.5,0,-2,-4],
		[-5,-4,-3,-3,-3,-3,-4,-5]];	

		pawn = [[0,0,0,0,0,0,0,0],
		[5,5,5,5,5,5,5,5],
		[1,1,2,3,3,2,1,1],
		[0.5,0.5,1,2.5,2.5,1,0.5,0.5],
		[0,0,0,2,2,0,0,0],
		[0.5,-0.5,-1,0,0,-1,-0.5,0.5],
		[5,1,1,-2,-2,1,1,0.5],
		[0,0,0,0,0,0,0,0]];	
		
		z=[7,6,5,4,3,2,1,0];
		
		for x in range(0,8):
			for y in range(0,8):
				if self.AIgame.returnChessPieces(x,y) == "p1":
					chessScore = chessScore+10+pawn[x][z[y]];
				
				if self.AIgame.returnChessPieces(x,y) == "b1":
					chessScore = chessScore+30+bishop[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "n1":
					chessScore = chessScore+30+knight[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "r1":
					chessScore = chessScore+50+rook[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "q1":
					chessScore = chessScore+90+queen[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "k1":
					chessScore = chessScore+900+king[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "p2":
					chessScore = chessScore-10-pawn[x][z[y]];
				
				if self.AIgame.returnChessPieces(x,y) == "b2":
					chessScore = chessScore-30-bishop[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "n2":
					chessScore = chessScore-30-knight[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "r2":
					chessScore = chessScore-50-rook[x][z[y]];
					#print(rook[x][z[y]])

				if self.AIgame.returnChessPieces(x,y) == "q2":
					chessScore = chessScore-90-queen[x][z[y]];

				if self.AIgame.returnChessPieces(x,y) == "k2":
					chessScore = chessScore-900-king[x][z[y]];
		self.chessScore = chessScore;
		return self.chessScore;

	def calculateBestMove(self,Player):
		if Player == "black":
			allMoves = self.generateMovesBlack();
		else:
			allMoves = self.generateMovesWhite();
		if not allMoves:
			return None;
		ratedMoves=[];
		#self.chessBoardCopy = deepcopy(self.AIgame.chessBoard);
		for moves in allMoves:
			#print(moves[len(moves)-1], len(moves));
			for i in range(len(moves)-1):
				p=self.AIgame.returnChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1]);
				killPiece = self.AIgame.returnChessPieces(int(moves[i][0]),int(moves[i][2]));
				self.AIgame.setChessPieces(int(moves[i][0]),int(moves[i][2]),p);
				self.AIgame.setChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1],"sp");
				self.PositionEvaluation();
				ratedMoves.append([[moves[len(moves)-1][0],moves[len(moves)-1][1]],[int(moves[i][0]),int(moves[i][2])],[self.chessScore]]);
				self.chessScore = 0;
				self.AIgame.setChessPieces(int(moves[i][0]),int(moves[i][2]),killPiece);
				self.AIgame.setChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1],p);
		#self.AIgame.printBoard();

		if not ratedMoves:
			return None;
		ScoreList = [];
		bestScore = 0;
		for moves in ratedMoves:
			ScoreList.append(moves[len(moves)-1][0]);
			bestScore = min(ScoreList);

		for moves in ratedMoves:
			if moves[len(moves)-1][0] == bestScore:
				#print(moves);
				return moves;


	def setChessBoard(self, newChessBoard):
		self.AIgame.chessBoard = newChessBoard;
		#print("setChessBoard");
			

	def generateBoards(self, Player):
		if Player == "black":
			allMoves = self.generateMovesBlack();
		else:
			allMoves = self.generateMovesWhite();
		ratedMoves=[];
		#self.chessBoardCopy = deepcopy(self.AIgame.chessBoard);
		for moves in allMoves:
			#print(moves[len(moves)-1], len(moves));
			for i in range(len(moves)-1):
				p=self.AIgame.returnChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1]);
				killPiece = self.AIgame.returnChessPieces(int(moves[i][0]),int(moves[i][2]));
				self.AIgame.setChessPieces(int(moves[i][0]),int(moves[i][2]),p);
				self.AIgame.setChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1],"sp");

				self.PositionEvaluation();
				
				ratedMoves.append([deepcopy(self.AIgame.chessBoard) , [moves[len(moves)-1][0],moves[len(moves)-1][1]], [int(moves[i][0]),int(moves[i][2])], [self.chessScore]]);
				
				self.AIgame.setChessPieces(int(moves[i][0]),int(moves[i][2]),killPiece);
				self.AIgame.setChessPieces(moves[len(moves)-1][0],moves[len(moves)-1][1],p);
		if Player == "black":
			return sorted(ratedMoves, key=lambda move: move[3] , reverse=False);
		else:
			return sorted(ratedMoves, key=lambda move: move[3], reverse=True);
		return ratedMoves


	def _minimax(self, depth, alpha, beta, player, deadline):
		self._node_count = self._node_count + 1;
		if deadline is not None and time.perf_counter() >= deadline:
			return [None, None, [self.PositionEvaluation()]];
		if depth == 0:
			return [None, None, [self.PositionEvaluation()]];

		key = (depth, self._hash_board(self.AIgame.chessBoard, player));
		if key in self._transposition:
			return self._transposition[key];

		if player:
			bestScore = -99999;
			bestMove = None;
			for fx, fy, tx, ty in self._ordered_moves("white"):
				moving, captured = self._make_move(fx, fy, tx, ty);
				score = self._minimax(depth - 1, alpha, beta, False, deadline)[2][0];
				self._undo_move(fx, fy, tx, ty, moving, captured);
				if score > bestScore or bestMove is None:
					bestScore = score;
					bestMove = [[fx, fy], [tx, ty], [score]];
				alpha = max(alpha, score);
				if beta <= alpha:
					break;
		else:
			bestScore = 99999;
			bestMove = None;
			for fx, fy, tx, ty in self._ordered_moves("black"):
				moving, captured = self._make_move(fx, fy, tx, ty);
				score = self._minimax(depth - 1, alpha, beta, True, deadline)[2][0];
				self._undo_move(fx, fy, tx, ty, moving, captured);
				if score < bestScore or bestMove is None:
					bestScore = score;
					bestMove = [[fx, fy], [tx, ty], [score]];
				beta = min(beta, score);
				if beta <= alpha:
					break;

		self._transposition[key] = bestMove;
		return bestMove;

	def minimax(self, state, depth, alpha, beta, player):
		self.AIgame.chessBoard = state;
		return self._minimax(depth, alpha, beta, player, None);

	def search_best_move(self, state, player, max_depth, time_limit=1.0, use_multiprocessing=False):
		self.AIgame.chessBoard = state;
		self._transposition = {};
		self._node_count = 0;
		deadline = None;
		if time_limit is not None:
			deadline = time.perf_counter() + time_limit;

		best_move = None;
		for depth in range(1, max_depth + 1):
			if deadline is not None and time.perf_counter() >= deadline:
				break;
			if use_multiprocessing and deadline is None and depth == max_depth:
				best_move = self._search_root_multiprocessing(player, depth);
			else:
				best_move = self._minimax(depth, -9999, 9999, player == "white", deadline);
			if best_move is None:
				break;
		return best_move;

	def _search_root_multiprocessing(self, player, depth):
		moves = list(self._ordered_moves(player));
		if not moves:
			return None;
		args = [];
		for fx, fy, tx, ty in moves:
			args.append((deepcopy(self.AIgame.chessBoard), (fx, fy, tx, ty), depth - 1, player == "black"));
		with mp.Pool() as pool:
			results = pool.map(_evaluate_root_move, args);
		if player == "white":
			best = max(results, key=lambda r: r[1]);
		else:
			best = min(results, key=lambda r: r[1]);
		(fx, fy, tx, ty), score = best;
		return [[fx, fy], [tx, ty], [score]];



def _evaluate_root_move(args):
	board, move, depth, minimizing = args;
	ai = chessGameAI();
	ai.AIgame.chessBoard = board;
	fx, fy, tx, ty = move;
	moving, captured = ai._make_move(fx, fy, tx, ty);
	score = ai._minimax(depth, -9999, 9999, not minimizing, None)[2][0];
	ai._undo_move(fx, fy, tx, ty, moving, captured);
	return (move, score);
