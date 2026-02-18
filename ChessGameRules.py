from copy import deepcopy

class chessGameRules:
	
	chessBoard = [[["r2",0],["n2",0],["b2",0],["q2",0],["k2",0],["b2",0],["n2",0],["r2",0]],
		[["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1],["p2",1]],
		[["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
		[["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
		[["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
		[["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0],["sp",0]],
		[["p1",1],["p1",1],["p1",1],["p1",1],["p1",1],["p1",1],["p1",1],["p1",1]],
		[["r1",0],["n1",0],["b1",0],["q1",0],["k1",0],["b1",0],["n1",0],["r1",0]]];

	gameLoopBool = True;
	turnCounter = True;
	playerInCheck = None;
	inputP1 = "";
	inputP2 = "";

	def printBoard(self):
		z = 8;
		for x in range(0,8):
			z = z-1;
			print(z ,end = " --- " );
			for y in range(0,8):
				tempPiece = self.chessBoard[x][y][0];
				print(tempPiece[0].upper(), end="");
				if tempPiece[1] == "1" or tempPiece[1] == "2":
					print(tempPiece[1], end=" ");
				else:
					print(tempPiece[1].upper(), end=" ");
				#print(chessBoard[x][y][0], end =" ")
			print();
		print();
		print("      |  |  |  |  |  |  |  |");
		print();
		print("      0  1  2  3  4  5  6  7");
		print();

	def returnChessPieces(self,x,y):
		z = [7,6,5,4,3,2,1,0];	
		return self.chessBoard[z[y]][x][0];

	def setChessPieces(self,x,y,Pieces):
		z = [7,6,5,4,3,2,1,0];	
		self.chessBoard[z[y]][x][0] = Pieces;
		
	def findPossibleMovesRook(self, pieceCoordinate):
		z = [7,6,5,4,3,2,1,0];	
		x = int(pieceCoordinate[1]);
		y = int(pieceCoordinate[0]);
		chessPiece = self.chessBoard[z[x]][y][0];
		PossibleMoves = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		PossibleMovesCounter = 0;
		countMovesLeft = -1;	
		countMovesRight = -1;
		countUp = -1;
		countDown = -1;
		if chessPiece[0] == "r" or chessPiece[0] == "q":
			#print("you have selected the rook your possable moves are");
			for yDown in range(x-1,-1,-1):
				if self.chessBoard[z[yDown]][y][0] == "sp":
					PossibleMoves[PossibleMovesCounter] = str(y) + ","+ str(yDown);
					PossibleMovesCounter=PossibleMovesCounter+1;
				else:
					try:
						P=self.chessBoard[z[yDown]][y][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							PossibleMoves[PossibleMovesCounter] = str(y) + ","+ str(yDown);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
					except:
						break;
				countDown = countDown+1;
			for yUp in range(x+1,8):
				if self.chessBoard[z[yUp]][y][0] == "sp":
					PossibleMoves[PossibleMovesCounter] = str(y) + ","+ str(yUp);
					PossibleMovesCounter=PossibleMovesCounter+1;
				else:
					try:
						P=self.chessBoard[z[yUp]][y][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							PossibleMoves[PossibleMovesCounter] = str(y) + ","+ str(yUp);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
					except:
						break;
				countUp = countUp+1;
			for xLeft in range(y-1,-1,-1):
				#print(chessBoard[z[x]][xLeft][0], end="-");
				if self.chessBoard[z[x]][xLeft][0] == "sp":
					PossibleMoves[PossibleMovesCounter] = str(xLeft)+ ","+str(x);
					PossibleMovesCounter=PossibleMovesCounter+1;
				else:
					try:
						P = self.chessBoard[z[x]][xLeft][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							PossibleMoves[PossibleMovesCounter] = str(xLeft)+ ","+str(x);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
					except:
						break;
				countMovesLeft = countMovesLeft+1;
			for xRight in range(y+1,8):
				#print(chessBoard[z[x]][xRight][0], end="-");
				if self.chessBoard[z[x]][xRight][0] == "sp":
					PossibleMoves[PossibleMovesCounter] = str(xRight) + "," + str(x);
					PossibleMovesCounter=PossibleMovesCounter+1;
				else:
					try:
						P = self.chessBoard[z[x]][xRight][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							PossibleMoves[PossibleMovesCounter] = str(xRight) + "," + str(x);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
					except:
						break;
				countMovesRight = countMovesRight+1;
			outPutMoves = list(filter(None, PossibleMoves));
			if len(outPutMoves) != 0:
				return outPutMoves;
		return "error";
		
	def findPossibleMovesBishop(self,pieceCoordinate):
		z = [7,6,5,4,3,2,1,0];
		x = int(pieceCoordinate[1]);
		y = int(pieceCoordinate[0]);
		chessPiece = self.chessBoard[z[x]][y][0];
		PossibleMoves = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		PossibleMovesCounter = 0;
		countMovesLeft = -1;	
		countMovesRight = -1;
		countUp = -1;
		countDown = -1;
		if chessPiece[0] == "b" or chessPiece[0] == "q":
			#print("you have selected the bishop your possable moves are");
			DownLeft = y;
			for yDownLeft in range(x-1,-1,-1):
				DownLeft=DownLeft-1;
				if DownLeft >= 0:
					#print(chessBoard[z[yDownLeft]][DownLeft][0]);
					if self.chessBoard[z[yDownLeft]][DownLeft][0] == "sp":
						#print(DownLeft,end="-");
						#print(yDownLeft);
						PossibleMoves[PossibleMovesCounter] = str(DownLeft) + "," + str(yDownLeft);
						PossibleMovesCounter=PossibleMovesCounter+1;
					else:
						P = self.chessBoard[z[yDownLeft]][DownLeft][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							#print(DownLeft,end="-");
							#print(yDownLeft);
							PossibleMoves[PossibleMovesCounter] = str(DownLeft) + "," + str(yDownLeft);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
				else:
					break;
			DownRight = y;
			for yDownRight in range(x-1,-1,-1):
				DownRight=DownRight+1;
				if DownRight <= 7:
					#print(chessBoard[z[yDownRight]][DownRight][0]);
					if self.chessBoard[z[yDownRight]][DownRight][0] == "sp":
						#print(DownLeft,end="-");
						#print(yDownLeft);
						PossibleMoves[PossibleMovesCounter] = str(DownRight) + "," + str(yDownRight);
						PossibleMovesCounter=PossibleMovesCounter+1;
					else:
						P = self.chessBoard[z[yDownRight]][DownRight][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							#print(DownLeft,end="-");
							#print(yDownLeft);
							PossibleMoves[PossibleMovesCounter] = str(DownRight) + "," + str(yDownRight);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
				else:
					break;
			
			leftUp = y;
			for yUpLeft in range(x+1,8):
				leftUp=leftUp-1;
				if leftUp >= 0:
					#print(chessBoard[z[yUpLeft]][leftUp][0]);
					if self.chessBoard[z[yUpLeft]][leftUp][0] == "sp":
						#print(DownLeft,end="-");
						#print(yDownLeft);
						PossibleMoves[PossibleMovesCounter] = str(leftUp) + "," + str(yUpLeft);
						PossibleMovesCounter=PossibleMovesCounter+1;
					else:
						P = self.chessBoard[z[yUpLeft]][leftUp][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							#print(DownLeft,end="-");
							#print(yDownLeft);
							PossibleMoves[PossibleMovesCounter] = str(leftUp) + "," + str(yUpLeft);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
				else:
					break;
			RightUp = y;
			for yUpRight in range(x+1,8):
				RightUp=RightUp+1;
				if RightUp <= 7:
					#print(chessBoard[z[yUpRight]][RightUp][0]);
					if self.chessBoard[z[yUpRight]][RightUp][0] == "sp":
						#print(DownLeft,end="-");
						#print(yDownLeft);
						PossibleMoves[PossibleMovesCounter] = str(RightUp) + "," + str(yUpRight);
						PossibleMovesCounter=PossibleMovesCounter+1;
					else:
						P = self.chessBoard[z[yUpRight]][RightUp][0];
						if P[1] == "1" and chessPiece[1] != "1" or P[1] == "2" and  chessPiece[1] != "2":	
							#print(DownLeft,end="-");
							#print(yDownLeft);
							PossibleMoves[PossibleMovesCounter] = str(RightUp) + "," + str(yUpRight);
							PossibleMovesCounter=PossibleMovesCounter+1;
						break;
				else:
					break;
			
			outPutMoves = list(filter(None, PossibleMoves));
			#print(outPutMoves);
			if len(outPutMoves) != 0:
				return outPutMoves;
		return "error";

	def findPossibleMovesKnight(self, pieceCoordinate):
		z = [7,6,5,4,3,2,1,0];
		x = int(pieceCoordinate[1]);
		y = int(pieceCoordinate[0]);
		chessPiece = self.chessBoard[z[x]][y][0];
		PossibleMoves = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		PossibleMovesCounter = 0;
		if chessPiece[0] == "n":
			#print("you have selected the Knight your possable moves are : ");
			try:
				p = self.chessBoard[z[x]-2][y+1][0];
				if x+2 <= 7 and y+1 <= 7:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[0]=  str(y+1) +","+ str(z[z[x]-2]);
						#print(chessBoard[z[x]-2][y+1][0]);	
			except:
				PossibleMoves[0]="";
			try:	
				p = self.chessBoard[z[x]-2][y-1][0];
				if x+2 <= 7 and y-1 >= 0:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[1]= str(y-1) +","+ str(z[z[x]-2]);
						#print(chessBoard[z[x]-2][y-1][0]);
			except:
				PossibleMoves[1]="";
			try:
				p = self.chessBoard[z[x]+2][y+1][0];
				if x-2 >= 0 and y+1 <= 7:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[2]= str(y+1) +","+ str(z[z[x]+2]);
						#print(chessBoard[z[x]+2][y+1][0]);
			except:
				PossibleMoves[2]="";
			try:	
				p = self.chessBoard[z[x]+2][y-1][0];
				if y-1 >= 0 and x-2 >= 0:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[3]=str(y-1) +","+ str(z[z[x]+2]);
						#print(chessBoard[z[x]+2][y-1][0]);
			except:
				PossibleMoves[3]="";
			try:
				p = self.chessBoard[z[x]-1][y+2][0];
				if y+2 >= 0 and x+1 <= 7:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[4]=str(y+2) +","+ str(z[z[x]-1]);
						#print(chessBoard[z[x]-1][y+2][0]);
			except:
				PossibleMoves[4]="";
			try:	
				p = self.chessBoard[z[x]+1][y+2][0];
				if x-1 >= 0 and y+2 <=7:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[5]=str(y+2) +","+ str(z[z[x]+1]);
						#print(chessBoard[z[x]+1][y+2][0]);
			except:
				PossibleMoves[5]="";
			try:
				p = self.chessBoard[z[x]-1][y-2][0];
				if y-2 >= 0 and x+1 <= 7:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[6]=str(y-2) +","+ str(z[z[x]-1]);
						#print(chessBoard[z[x]-1][y-2][0]);
			except:
				PossibleMoves[6]="";
			try:
				p = self.chessBoard[z[x]+1][y-2][0];	
				if y-2 >= 0 and x-1 >= 0:
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves[7]=str(y-2) +","+ str(z[z[x]+1]);
						#print(chessBoard[z[x]+1][y-2][0]);
			except:
				PossibleMoves[7]="";	
				
			outPutMoves = list(filter(None, PossibleMoves));
			#print(outPutMoves);
			if len(outPutMoves) != 0:
				return outPutMoves;
		return "error";

	def findPossibleMovesQueen(self,pieceCoordinate):
		MovesRook = self.findPossibleMovesRook(pieceCoordinate);
		MovesBishop = self.findPossibleMovesBishop(pieceCoordinate);
		if MovesRook[0] != "e" and MovesBishop[0] != "e":
			return MovesRook + MovesBishop;
		if MovesRook[0] != "e" and MovesBishop[0] == "e":
			return MovesRook;
		if MovesRook[0] == "e" and MovesBishop[0] != "e":
			return MovesBishop;
		return "error";

	def findPossibleMovesPawn(self,pieceCoordinate, analyzing):
		z = [7,6,5,4,3,2,1,0];
		x = int(pieceCoordinate[1]);
		y = int(pieceCoordinate[0]);
		chessPiece = self.chessBoard[z[x]][y][0];
		PossibleMoves = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		PossibleMovesCounter = 0;
		if chessPiece[0] == "p":
			p=self.chessBoard[z[x]][y][0];		

			###########################WHITE#############################
			
			if self.chessBoard[z[x]][y][1] == 1 and x+2 >= 0:
				if p[1] == "1" and self.chessBoard[z[x]-1][y][0] == "sp" and self.chessBoard[z[x]-2][y][0] == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]-2]));

			if x+1 <= 7:
				if p[1] == "1" and self.chessBoard[z[x]-1][y][0] == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]-1]));

			if x+1 <= 7 and y+1 <=7:
				if p[1] == "1" and self.chessBoard[z[x]-1][y+1][0] != "sp" and self.chessBoard[z[x]-1][y+1][0][1] != "1":
					PossibleMoves.append(str(y+1) +","+ str(z[z[x]-1]));

			if x+1 <= 7 and y-1 >=0:			
				if p[1] == "1" and self.chessBoard[z[x]-1][y-1][0] != "sp" and self.chessBoard[z[x]-1][y-1][0][1] != "1":
					PossibleMoves.append(str(y-1) +","+ str(z[z[x]-1]));

			###########################BLACK#############################

			if self.chessBoard[z[x]][y][1] == 1 and x-2 >= 0:
				if p[1] == "2" and self.chessBoard[z[x]+1][y][0] == "sp" and self.chessBoard[z[x]+2][y][0] == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]+2]));

			if x+1 <= 7:
				if p[1] == "2" and self.chessBoard[z[x]+1][y][0] == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]+1]));

			if x+1 <= 7 and y+1 <= 7:
				if p[1] == "2" and self.chessBoard[z[x]+1][y+1][0] != "sp" and self.chessBoard[z[x]+1][y+1][0][1] != "2":
					PossibleMoves.append(str(y+1) +","+ str(z[z[x]+1]));

			if x+1 <= 7 and y-1 >= 0:			
				if p[1] == "2" and self.chessBoard[z[x]+1][y-1][0] != "sp" and self.chessBoard[z[x]+1][y-1][0][1] != "2":
					PossibleMoves.append(str(y-1) +","+ str(z[z[x]+1]));

			outPutMoves = list(filter(None, PossibleMoves));
			if len(outPutMoves) != 0:
				return outPutMoves;
		return "error";

	def findPossibleMovesKing(self,pieceCoordinate):
		z = [7,6,5,4,3,2,1,0];
		x = int(pieceCoordinate[1]);
		y = int(pieceCoordinate[0]);
		chessPiece = self.chessBoard[z[x]][y][0];
		PossibleMoves = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		PossibleMovesCounter = 0;
		if chessPiece[0] == "k":
			#print("you have selected the King your possable moves are : ");
			if x+1 <= 7:
				p = self.chessBoard[z[x]-1][y][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]-1]));
			if x-1 >= 0:
				p = self.chessBoard[z[x]+1][y][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y) +","+ str(z[z[x]+1]));
			if y+1 <= 7:
				p = self.chessBoard[z[x]][y+1][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y+1) +","+ str(z[z[x]]));
			if y-1 >= 0:
				p = self.chessBoard[z[x]][y-1][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y-1) +","+ str(z[z[x]]));
			if x+1 <= 7 and y+1 <= 7:
				p = self.chessBoard[z[x]-1][y+1][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y+1) +","+ str(z[z[x]-1]));
			if x-1 >= 0 and y+1 <= 7:
				p = self.chessBoard[z[x]+1][y+1][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y+1) +","+ str(z[z[x]+1]));
			if y-1 >= 0 and x-1 >= 0:
					p = self.chessBoard[z[x]+1][y-1][0];
					if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
						PossibleMoves.append(str(y-1) +","+ str(z[z[x]+1]));
			if y-1 >= 0 and x+1 <= 7:
				p = self.chessBoard[z[x]-1][y-1][0];
				if p[1] == "1" and chessPiece[1] != "1" or p[1] == "2" and chessPiece[1] != "2" or p == "sp":
					PossibleMoves.append(str(y-1) +","+ str(z[z[x]-1]));
			outPutMoves = list(filter(None, PossibleMoves));
			if len(outPutMoves) != 0:
				#return self.removeMovesThatWillPutYouInCheck(outPutMoves, pieceCoordinate);
				return outPutMoves;
		return "error";

	def CheckIfPlayerIsInCheck(self):
		allPiecesMoves=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
		FindPossibleMovesRook=[];
		FindPossibleMovesBitshop=[];
		FindPossibleMovesKnight=[];
		FindPossibleMovesQueen=[];
		FindPossibleMovesKing=[];
		FindPossibleMovesPawn=[];
		z=[7,6,5,4,3,2,1,0];
		index = 0;
		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.chessBoard[x][y][0];
				tempMove = [y,z[int(x)]];
				if chessPiece[0] == "r":
					allPiecesMoves[index] = self.findPossibleMovesRook(tempMove);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
				if chessPiece[0] == "b":
					allPiecesMoves[index] = self.findPossibleMovesBishop(tempMove);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
				if chessPiece[0] == "n":
					allPiecesMoves[index] = self.findPossibleMovesKnight(tempMove);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
				if chessPiece[0] == "q":
					allPiecesMoves[index] = self.findPossibleMovesQueen(tempMove);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
				if chessPiece[0] == "k":
					allPiecesMoves[index] = self.findPossibleMovesKing(tempMove);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
				if chessPiece[0] == "p":
					allPiecesMoves[index] = self.findPossibleMovesPawn(tempMove,False);
					if allPiecesMoves[index] == "error":
						allPiecesMoves[index] = None;
					index=index+1;
		outPutMoves = list(filter(None, allPiecesMoves));
		#print(tempChessGame.chessBoard);
		kingCount = 0;
		for x in range(len(outPutMoves)):
			for y in range(len(outPutMoves[x])):
				tempCoordinate = outPutMoves[x][y];
				if self.chessBoard[z[int(tempCoordinate[2])]][int(tempCoordinate[0])][0] == "k2":
					self.playerInCheck = "black"; 
					kingCount = kingCount+1;
				if self.chessBoard[z[int(tempCoordinate[2])]][int(tempCoordinate[0])][0] == "k1":
					self.playerInCheck = "white"; 
					kingCount = kingCount+1;
		if kingCount>0:
			return True;
		else:
			self.playerInCheck = None; 
			return False;

	def removeMovesThatWillPutYouInCheck(self, outPutMoves, pieceCoordinate):
		if outPutMoves == "error" or not outPutMoves:
			return "error";
		filteredMoves = [];
		# simulate each move and reject those that leave the moving side in check
		chessPiece = self.returnChessPieces(int(pieceCoordinate[0]),int(pieceCoordinate[1]));
		if chessPiece == "sp":
			return "error";
		for Moves in outPutMoves:
			x = int(Moves[0]);
			y = int(Moves[2]);
			capturedPiece = self.returnChessPieces(x,y);
			self.setChessPieces(x,y,chessPiece);
			self.setChessPieces(int(pieceCoordinate[0]),int(pieceCoordinate[1]),"sp");
			self.CheckIfPlayerIsInCheck();
			if chessPiece[1] == "1" and self.playerInCheck != "white":
				filteredMoves.append(Moves);
			if chessPiece[1] == "2" and self.playerInCheck != "black":
				filteredMoves.append(Moves);
			self.setChessPieces(int(pieceCoordinate[0]),int(pieceCoordinate[1]),chessPiece);
			self.setChessPieces(x,y,capturedPiece);
		if not filteredMoves:
			return "error";
		return filteredMoves;
		



