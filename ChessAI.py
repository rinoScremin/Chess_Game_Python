from ChessGameRules import chessGameRules
from copy import copy, deepcopy

class chessGameAI:

	AIgame = chessGameRules();
	chessScore = 0;
	chessBoardCopy=None;
	maxScore = 0;
	minScore = 0;

	
	def generateMovesWhite(self):
		allPeacesMoves=[];
		z=[7,6,5,4,3,2,1,0];
		index = 0;
		for x in range(0,8):
			for y in range(0,8):
				chessPeace = self.AIgame.chessBoard[x][y][0];
				tempMove = [y,z[int(x)]];

				if chessPeace == "r1": 
					temp = self.AIgame.findPossibleMovesRook(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "p1": 
					temp = self.AIgame.findPossibleMovesPawn(tempMove, False);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "n1": 
					temp = self.AIgame.findPossibleMovesKnight(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "b1": 
					temp = self.AIgame.findPossibleMovesBishop(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "k1": 
					temp = self.AIgame.findPossibleMovesKing(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "q1": 
					temp = self.AIgame.findPossibleMovesQueen(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);
		return allPeacesMoves;

	def generateMovesBlack(self):
		allPeacesMoves=[];
		z=[7,6,5,4,3,2,1,0];
		index = 0;
		for x in range(0,8):
			for y in range(0,8):
				chessPeace = self.AIgame.chessBoard[x][y][0];
				tempMove = [y,z[int(x)]];

				if chessPeace == "r2": 
					temp = self.AIgame.findPossibleMovesRook(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "p2": 
					temp = self.AIgame.findPossibleMovesPawn(tempMove, False);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "n2": 
					temp = self.AIgame.findPossibleMovesKnight(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "b2": 
					temp = self.AIgame.findPossibleMovesBishop(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "k2": 
					temp = self.AIgame.findPossibleMovesKing(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);

				if chessPeace == "q2": 
					temp = self.AIgame.findPossibleMovesQueen(tempMove);
					if temp[0] != "e":
						temp.append(tempMove);
						allPeacesMoves.append(temp);
		#self.AIgame.printBoard();
		return allPeacesMoves;


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


	def minimax(self, state, depth, alpha, beta, player):
		self.AIgame.chessBoard = state;
		bestMovelist = [];
		scoreList = [];
		bestMove = None;
		chessBoardCopy = deepcopy(self.AIgame.chessBoard);
		newGameMoves = None;

		if depth == 0:
			return bestMove;

		if player:	
			newGameMoves = self.generateBoards("white");
		else:
			newGameMoves = self.generateBoards("black");

		if player:
			for i in range(len(newGameMoves)):
				self.AIgame.chessBoard = newGameMoves[i][0];
				score = self.PositionEvaluation();
				try:
					player=False;
					score = self.minimax(self.AIgame.chessBoard, depth - 1, alpha, beta, player)[2][0];
					bestMovelist.append([newGameMoves[i][1], newGameMoves[i][2], [score]]);
					scoreList.append(score);
					bestScore = max(scoreList);
					bestMove = bestMovelist[scoreList.index(bestScore)];
				except:
					bestMovelist.append([newGameMoves[i][1], newGameMoves[i][2], [score]]);
					scoreList.append(score);
					bestScore = max(scoreList);
					bestMove = bestMovelist[scoreList.index(bestScore)];
				alpha = max(alpha, score);
				if beta <= alpha:
					break
			return bestMove;
		else:
			for i in range(len(newGameMoves)):
				self.AIgame.chessBoard = newGameMoves[i][0];
				score = self.PositionEvaluation();
				try:
					player=True;
					score = self.minimax(self.AIgame.chessBoard, depth - 1, alpha, beta, player)[2][0];
					bestMovelist.append([newGameMoves[i][1], newGameMoves[i][2], [score]]);
					scoreList.append(score);
					bestScore = min(scoreList);
					bestMove = bestMovelist[scoreList.index(bestScore)];
				except:
					bestMovelist.append([newGameMoves[i][1], newGameMoves[i][2], [score]]);
					scoreList.append(score);
					bestScore = min(scoreList);
					bestMove = bestMovelist[scoreList.index(bestScore)];

				beta = min(beta, score);
				if beta <= alpha:
					break
			return bestMove;




			
				
		

#chessBoard = [[["r2",0],["sp",0],["b2",0],["q2",0],["k2",0],["b2",0],["sp",0],["r2",0]],
#	[["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1]],
#	[["sp",0],["sp",0],["n2",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
#	[["sp",0],["sp",0],["sp",0],["p1",0],["sp",0],["sp",0],["sp",0],["sp",0]],
#	[["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
#	[["sp",0],["n2",0],["p1",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
#	[["p1",1],["p1",1],["sp",1],["sp",1],["p1",1],["p1",1],["p1",1],["p1",1]],
#	[["r1",0],["n1",0],["b1",0],["q1",0],["k1",0],["b1",0],["n1",0],["r1",0]]];		
			

#test = chessGameAI();
#test.AIgame.chessBoard = chessBoard;
#print(test.PositionEvaluation());

#test.AIgame.chessBoard = chessBoard;
#i=0;
#for moves in test.generateBoards("black"):
#	i=i+1;
#	print(moves[3][0], "list # : " ,i);
#	test.AIgame.chessBoard = moves[0];
#	test.AIgame.printBoard();


#print(test.minimax(chessBoard,2,-9999,9999,False));
#test.AIgame.printBoard();

#print(test.minimax(test.AIgame.chessBoard,1,-9999,9999,False));
#test.AIgame.printBoard();




#print(test.generateBoards("black")[6]);
#test.test(3, True);
#print(test.calculateBestMove());
#print(test.generateMovesBlack());
