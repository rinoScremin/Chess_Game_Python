import arcade
import os
from ChessGameRules import chessGameRules
from ChessAI import chessGameAI
from random import randint

class ChessGame(arcade.Window):

	difficultyLevel = input("Enter The Difficulty Level: ");
	
	def __init__(self, width, height):
		super().__init__(width, height);

		self.ChessGameLogic = chessGameRules();

		self.chessAI = chessGameAI();

		self.Pawn_list = None;
		self.Rook_list = None;
		self.Knight_list = None;
		self.Bishop_list = None;
		self.king_list = None;
		self.Queen_list = None;

		self.B_Pawn_list = None;
		self.B_Rook_list = None;
		self.B_Knight_list = None;
		self.B_Bishop_list = None;
		self.B_king_list = None;
		self.B_Queen_list = None;

		self.B_QueenHit = False;
		self.B_KingHit = False;
		self.KingHit = False;
		self.QueenHit = False;

		self.mouse_current_state = False;

		self.CurrentPieceCoordinance = None;
		self.SelectedPieceCoordinance = None;
	
		self.BlackPieceCoordinance = None;
		self.WhitePieceCoordinance = None;

		self.PawnFirstMove = [True,True,True,True,True,True,True,True];
		self.b_PawnFirstMove = [True,True,True,True,True,True,True,True];
		#self.PawnCounter = 0;

		self.B_King = None;

		self.King_Select_list = [False];
		self.Queen_Select_list = [False];
		self.Rook_Select_list = [False,False];
		self.Knight_Select_list = [False,False];
		self.Bishop_Select_list = [False,False];
		self.Pawn_Select_list = [False,False,False,False,False,False,False,False];

		self.B_King_Select_list = [False];
		self.B_Queen_Select_list = [False];
		self.B_Rook_Select_list = [False,False];
		self.B_Knight_Select_list = [False,False];
		self.B_Bishop_Select_list = [False,False];
		self.B_Pawn_Select_list = [False,False,False,False,False,False,False,False];
		
		self.pawnAtEndOfBoard = False;
		
		self.count = 0;
		
		self.playersTurn = "white"; 
		
	def setup(self):
		
		file_path = os.path.dirname(os.path.abspath(__file__));
		os.chdir(file_path);

		self.chessPieces_scaling = 1;
	
		self.backGround = arcade.load_texture("chess_board_img.jpg");

		self.King_list = arcade.SpriteList();
		King = arcade.Sprite("King_img.jpg",self.chessPieces_scaling);
		King.center_x = 335;
		King.center_y = 35;
		King.boundary_left = King.center_x-(King.width/2); 
		King.boundary_right = King.center_x+(King.width/2);
		King.boundary_top = King.center_y+(King.height/2);
		King.boundary_bottom = King.center_y-(King.height/2);
		self.King_list.append(King);

		self.B_King_list = arcade.SpriteList();
		B_King = arcade.Sprite("B_King_img.jpg",self.chessPieces_scaling);
		B_King.center_x = 335;
		B_King.center_y = 560;
		B_King.boundary_left = B_King.center_x-(B_King.width/2); 
		B_King.boundary_right = B_King.center_x+(B_King.width/2);
		B_King.boundary_top = B_King.center_y+(B_King.height/2);
		B_King.boundary_bottom = B_King.center_y-(B_King.height/2);
		self.B_King_list.append(B_King);

		self.Queen_list = arcade.SpriteList();	
		Queen = arcade.Sprite("Queen_img.jpg",self.chessPieces_scaling);
		Queen.center_x = 260;
		Queen.center_y = 35;
		Queen.boundary_left = Queen.center_x-(Queen.width/2); 
		Queen.boundary_right = Queen.center_x+(Queen.width/2);
		Queen.boundary_top = Queen.center_y+(Queen.height/2);
		Queen.boundary_bottom = Queen.center_y-(Queen.height/2);
		self.Queen_list.append(Queen);

		self.B_Queen_list = arcade.SpriteList();	
		B_Queen = arcade.Sprite("B_Queen_img.jpg",self.chessPieces_scaling);
		B_Queen.center_x = 260;
		B_Queen.center_y = 560;
		B_Queen.boundary_left = B_Queen.center_x-(B_Queen.width/2); 
		B_Queen.boundary_right = B_Queen.center_x+(B_Queen.width/2);
		B_Queen.boundary_top = B_Queen.center_y+(B_Queen.height/2);
		B_Queen.boundary_bottom = B_Queen.center_y-(B_Queen.height/2);
		self.B_Queen_list.append(B_Queen);
		
		self.Pawn_list = arcade.SpriteList();
		pawnPosition = 35;
		PAWN_COUNT = 8;	
		for i in range(PAWN_COUNT):
			Pawn = arcade.Sprite("Pawn_img.jpg",self.chessPieces_scaling);
			Pawn.center_x = pawnPosition;
			Pawn.center_y = 110;
			Pawn.boundary_left = Pawn.center_x - (Pawn.width/2); 
			Pawn.boundary_right = Pawn.center_x + (Pawn.width/2);
			Pawn.boundary_top = Pawn.center_y + (Pawn.height/2);
			Pawn.boundary_bottom = Pawn.center_y - (Pawn.height/2);
			self.Pawn_list.append(Pawn);
			pawnPosition = pawnPosition + 75;

		self.B_Pawn_list = arcade.SpriteList();
		B_pawnPosition = 35;
		for i in range(PAWN_COUNT):
			Pawn = arcade.Sprite("B_Pawn_img.jpg",self.chessPieces_scaling);
			Pawn.center_x = B_pawnPosition;
			Pawn.center_y = 485;
			Pawn.boundary_left = Pawn.center_x - (Pawn.width/2); 
			Pawn.boundary_right = Pawn.center_x + (Pawn.width/2);
			Pawn.boundary_top = Pawn.center_y + (Pawn.height/2);
			Pawn.boundary_bottom = Pawn.center_y - (Pawn.height/2);
			self.B_Pawn_list.append(Pawn);
			B_pawnPosition = B_pawnPosition + 75;

		self.Rook_list = arcade.SpriteList();
		RookPosition = 35;
		ROOK_COUNT = 2;	
		for i in range(ROOK_COUNT):
			Rook = arcade.Sprite("Rook_img.jpg",self.chessPieces_scaling);
			Rook.center_x = RookPosition;
			Rook.center_y = 35;
			Rook.boundary_left = Rook.center_x - (Rook.width/2); 
			Rook.boundary_right = Rook.center_x + (Rook.width/2);
			Rook.boundary_top = Rook.center_y + (Rook.height/2);
			Rook.boundary_bottom = Rook.center_y - (Rook.height/2);
			self.Rook_list.append(Rook);
			RookPosition = RookPosition + 525;

		self.B_Rook_list = arcade.SpriteList();
		B_RookPosition = 35;
		ROOK_COUNT = 2;	
		for i in range(ROOK_COUNT):
			Rook = arcade.Sprite("B_Rook_img.jpg",self.chessPieces_scaling);
			Rook.center_x = B_RookPosition;
			Rook.center_y = 560;
			Rook.boundary_left = Rook.center_x - (Rook.width/2); 
			Rook.boundary_right = Rook.center_x + (Rook.width/2);
			Rook.boundary_top = Rook.center_y + (Rook.height/2);
			Rook.boundary_bottom = Rook.center_y - (Rook.height/2);
			self.B_Rook_list.append(Rook);
			B_RookPosition = B_RookPosition + 525;

		self.Knight_list = arcade.SpriteList();
		KnightPosition = 110;
		KNIGHT_COUNT = 2;	
		for i in range(KNIGHT_COUNT):
			Knight = arcade.Sprite("Knight_img.jpg",self.chessPieces_scaling);
			Knight.center_x = KnightPosition;
			Knight.center_y = 35;
			Knight.boundary_left = Knight.center_x - (Knight.width/2); 
			Knight.boundary_right = Knight.center_x + (Knight.width/2);
			Knight.boundary_top = Knight.center_y + (Knight.height/2);
			Knight.boundary_bottom = Knight.center_y - (Knight.height/2);
			self.Knight_list.append(Knight);
			KnightPosition = KnightPosition + 375;

		self.B_Knight_list = arcade.SpriteList();
		B_KnightPosition = 110;
		KNIGHT_COUNT = 2;	
		for i in range(KNIGHT_COUNT):
			Knight = arcade.Sprite("B_Knight_img.jpg",self.chessPieces_scaling);
			Knight.center_x = B_KnightPosition;
			Knight.center_y = 560;
			Knight.boundary_left = Knight.center_x - (Knight.width/2); 
			Knight.boundary_right = Knight.center_x + (Knight.width/2);
			Knight.boundary_top = Knight.center_y + (Knight.height/2);
			Knight.boundary_bottom = Knight.center_y - (Knight.height/2);
			self.B_Knight_list.append(Knight);
			B_KnightPosition = B_KnightPosition + 375;
		
		self.Bishop_list = arcade.SpriteList();
		BishopPosition = 185;
		BISHOP_COUNT = 2;	
		for i in range(BISHOP_COUNT):
			Bishop = arcade.Sprite("Bishop_img.jpg",self.chessPieces_scaling);
			Bishop.center_x = BishopPosition;
			Bishop.center_y = 35;
			Bishop.boundary_left = Bishop.center_x - (Bishop.width/2); 
			Bishop.boundary_right = Bishop.center_x + (Bishop.width/2);
			Bishop.boundary_top = Bishop.center_y + (Bishop.height/2);
			Bishop.boundary_bottom = Bishop.center_y - (Bishop.height/2);
			self.Bishop_list.append(Bishop);
			BishopPosition = BishopPosition + 225;

		self.B_Bishop_list = arcade.SpriteList();
		B_BishopPosition = 185;
		BISHOP_COUNT = 2;	
		for i in range(BISHOP_COUNT):
			Bishop = arcade.Sprite("B_Bishop_img.jpg",self.chessPieces_scaling);
			Bishop.center_x = B_BishopPosition;
			Bishop.center_y = 560;
			Bishop.boundary_left = Bishop.center_x - (Bishop.width/2); 
			Bishop.boundary_right = Bishop.center_x + (Bishop.width/2);
			Bishop.boundary_top = Bishop.center_y + (Bishop.height/2);
			Bishop.boundary_bottom = Bishop.center_y - (Bishop.height/2);
			self.B_Bishop_list.append(Bishop);
			B_BishopPosition = B_BishopPosition + 225;
		pass

	def on_draw(self):
		arcade.start_render();
		arcade.draw_texture_rectangle(300, 300, 600, 600, self.backGround);
		self.Rook_list.draw();
		self.Knight_list.draw();
		self.Bishop_list.draw();
		self.Pawn_list.draw();
		self.B_Pawn_list.draw()
		self.B_Rook_list.draw();
		self.B_Knight_list.draw();
		self.B_Bishop_list.draw();
		self.B_King_list.draw();
		self.B_Queen_list.draw();
		self.King_list.draw();	
		self.Queen_list.draw();

	def update(self, delta_time):
		for King in self.B_King_list:
			King.boundary_left = King.center_x-(King.width/2); 
			King.boundary_right = King.center_x+(King.width/2);
			King.boundary_top = King.center_y+(King.height/2);
			King.boundary_bottom = King.center_y-(King.height/2);
			King.update();
		
		for King in self.King_list:
			King.boundary_left = King.center_x-(King.width/2); 
			King.boundary_right = King.center_x+(King.width/2);
			King.boundary_top = King.center_y+(King.height/2);
			King.boundary_bottom = King.center_y-(King.height/2);
			King.update();

		for Queen in self.B_Queen_list: 
			Queen.boundary_left = Queen.center_x-(Queen.width/2); 
			Queen.boundary_right = Queen.center_x+(Queen.width/2);
			Queen.boundary_top = Queen.center_y+(Queen.height/2);
			Queen.boundary_bottom = Queen.center_y-(Queen.height/2);
			Queen.update();
		
		for Queen in self.Queen_list: 
			Queen.boundary_left = Queen.center_x-(Queen.width/2); 
			Queen.boundary_right = Queen.center_x+(Queen.width/2);
			Queen.boundary_top = Queen.center_y+(Queen.height/2);
			Queen.boundary_bottom = Queen.center_y-(Queen.height/2);
			Queen.update();

		for Rook in self.Rook_list: 
			Rook.boundary_left = Rook.center_x-(Rook.width/2); 
			Rook.boundary_right = Rook.center_x+(Rook.width/2);
			Rook.boundary_top = Rook.center_y+(Rook.height/2);
			Rook.boundary_bottom = Rook.center_y-(Rook.height/2);

		for Rook in self.B_Rook_list: 
			Rook.boundary_left = Rook.center_x-(Rook.width/2); 
			Rook.boundary_right = Rook.center_x+(Rook.width/2);
			Rook.boundary_top = Rook.center_y+(Rook.height/2);
			Rook.boundary_bottom = Rook.center_y-(Rook.height/2);

		for Knight in self.Knight_list: 
			Knight.boundary_left = Knight.center_x-(Knight.width/2); 
			Knight.boundary_right = Knight.center_x+(Knight.width/2);
			Knight.boundary_top = Knight.center_y+(Knight.height/2);
			Knight.boundary_bottom = Knight.center_y-(Knight.height/2);

		for Knight in self.B_Knight_list: 
			Knight.boundary_left = Knight.center_x-(Knight.width/2); 
			Knight.boundary_right = Knight.center_x+(Knight.width/2);
			Knight.boundary_top = Knight.center_y+(Knight.height/2);
			Knight.boundary_bottom = Knight.center_y-(Knight.height/2);

		for Bishop in self.Bishop_list: 
			Bishop.boundary_left = Bishop.center_x-(Bishop.width/2); 
			Bishop.boundary_right = Bishop.center_x+(Bishop.width/2);
			Bishop.boundary_top = Bishop.center_y+(Bishop.height/2);
			Bishop.boundary_bottom = Bishop.center_y-(Bishop.height/2);

		for Bishop in self.B_Bishop_list: 
			Bishop.boundary_left = Bishop.center_x-(Bishop.width/2); 
			Bishop.boundary_right = Bishop.center_x+(Bishop.width/2);
			Bishop.boundary_top = Bishop.center_y+(Bishop.height/2);
			Bishop.boundary_bottom = Bishop.center_y-(Bishop.height/2);

		for Pawn in self.Pawn_list:        
			Pawn.boundary_left = Pawn.center_x - (Pawn.width/2); 
			Pawn.boundary_right = Pawn.center_x + (Pawn.width/2);
			Pawn.boundary_top = Pawn.center_y + (Pawn.height/2);
			Pawn.boundary_bottom = Pawn.center_y - (Pawn.height/2);

		for Pawn in self.B_Pawn_list:        
			Pawn.boundary_left = Pawn.center_x - (Pawn.width/2); 
			Pawn.boundary_right = Pawn.center_x + (Pawn.width/2);
			Pawn.boundary_top = Pawn.center_y + (Pawn.height/2);
			Pawn.boundary_bottom = Pawn.center_y - (Pawn.height/2);
		self.AIMakeMove();
		pass
	
	def on_mouse_press(self, x, y, button, modifiers):
		self.mouse_current_state = True;

	def changeTurn(self):
		if self.playersTurn == "white":
			self.playersTurn = "black";
			return "black"
		if self.playersTurn == "black":
			self.playersTurn = "white";
			return "white"
		
	def on_mouse_release(self, x, y, button, modifiers):
		self.mouse_current_state = False;
		if self.HitTestWhiteOnWhite(self.Queen_list) or self.HitTestWhiteOnWhite(self.King_list) or self.HitTestWhiteOnWhite(self.Knight_list) or self.HitTestWhiteOnWhite(self.Pawn_list) or self.HitTestWhiteOnWhite(self.Bishop_list) or self.HitTestWhiteOnWhite(self.Rook_list):
			None;
		else:
			if self.playersTurn == "white":
				print();
				print("PLAYER 1 CHESS MOVE");
				self.MoveQueen(x,y, self.Queen_list, self.Queen_Select_list);
				self.MovePawn(x,y, self.Pawn_list, self.Pawn_Select_list);
				self.MoveKnight(x,y, self.Knight_list, self.Knight_Select_list);
				self.MoveBishop(x,y, self.Bishop_list,self.Bishop_Select_list);
				self.MoveRook(x,y, self.Rook_list,self.Rook_Select_list);
				self.MoveKing(x,y, self.King_list, self.King_Select_list);

	def HitTestWhiteOnWhite(self, Piece_list):
		for Piece in Piece_list:
			if arcade.check_for_collision_with_list(Piece, self.Pawn_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.Knight_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.Bishop_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.Rook_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.King_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.Queen_list) != []:
				return True;
		return False;
	def HitTestBlackOnBlack(self, Piece_list):
		for Piece in Piece_list:
			if arcade.check_for_collision_with_list(Piece, self.B_Pawn_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.B_Knight_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.B_Bishop_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.B_Rook_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.B_King_list) != []:
				return True;
			if arcade.check_for_collision_with_list(Piece, self.B_Queen_list) != []:
				return True;
		return False;

	def AIMakeMove(self):
			if self.playersTurn == "black":
				temp = self.chessAI.minimax(self.ChessGameLogic.chessBoard, int(self.difficultyLevel), -9999, 9999, False);
				chessPiecesCoordinance = [temp[0][0],temp[0][1]];
				chessPiecesBoardPostion = self.CoordinanceToBoardPostion(chessPiecesCoordinance[0],chessPiecesCoordinance[1]);
				chessPieces_x = chessPiecesBoardPostion[0];
				chessPieces_y = chessPiecesBoardPostion[1];
				newPostion = [temp[1][0],temp[1][1]];
				moveChessPieces = self.CoordinanceToBoardPostion(newPostion[0],newPostion[1]);
				x = moveChessPieces[0];
				y = moveChessPieces[1];
				Pieces=self.ChessGameLogic.returnChessPieces(chessPiecesCoordinance[0],chessPiecesCoordinance[1]);
				self.ChessGameLogic.setChessPieces(newPostion[0],newPostion[1],Pieces);
				self.ChessGameLogic.setChessPieces(chessPiecesCoordinance[0],chessPiecesCoordinance[1],"sp");
				for Pawn in self.B_Pawn_list:
					if Pawn.center_x == chessPieces_x and Pawn.center_y == chessPieces_y:
						Pawn.center_x = x;
						Pawn.center_y = y;
						self.HitTestBlackOnWhite(Pawn);
				for Knight in self.B_Knight_list:
					if Knight.center_x == chessPieces_x and Knight.center_y == chessPieces_y:
						Knight.center_x = x;
						Knight.center_y = y;
						self.HitTestBlackOnWhite(Knight);
				for Bishop in self.B_Bishop_list:
					if Bishop.center_x == chessPieces_x and Bishop.center_y == chessPieces_y:
						Bishop.center_x = x;
						Bishop.center_y = y;
						self.HitTestBlackOnWhite(Bishop);
				for Rook in self.B_Rook_list:
					if Rook.center_x == chessPieces_x and Rook.center_y == chessPieces_y:
						Rook.center_x = x;
						Rook.center_y = y;
						self.HitTestBlackOnWhite(Rook);
				for King in self.B_King_list:
					if King.center_x == chessPieces_x and King.center_y == chessPieces_y:
						King.center_x = x;
						King.center_y = y;
						self.HitTestBlackOnWhite(King);
				for Queen in self.B_Queen_list:
					if Queen.center_x == chessPieces_x and Queen.center_y == chessPieces_y:
						Queen.center_x = x;
						Queen.center_y = y;
						self.HitTestBlackOnWhite(Queen);
				self.PawnAtEndOfBoard();
				self.changeTurn();
				for queen in self.B_Queen_list:
					if arcade.check_for_collision_with_list(queen, self.B_Pawn_list):
						arcade.check_for_collision_with_list(queen, self.B_Pawn_list)[0].kill();
				print();
				print("AI CHESS MOVE");
				self.ChessGameLogic.printBoard();


	def HitTestBlackOnWhite(self, Piece):
		#self.B_Queen.kill();
		if self.playersTurn == "white":
			if arcade.check_for_collision_with_list(Piece, self.B_Pawn_list):
				arcade.check_for_collision_with_list(Piece, self.B_Pawn_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.B_Knight_list):
				arcade.check_for_collision_with_list(Piece, self.B_Knight_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.B_Bishop_list):
				arcade.check_for_collision_with_list(Piece, self.B_Bishop_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.B_Rook_list):
				arcade.check_for_collision_with_list(Piece, self.B_Rook_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.B_Queen_list):
				arcade.check_for_collision_with_list(Piece, self.B_Queen_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.B_King_list):
				arcade.check_for_collision_with_list(Piece, self.B_King_list)[0].kill();

			
		if self.playersTurn == "black":
			if arcade.check_for_collision_with_list(Piece, self.Pawn_list):
				arcade.check_for_collision_with_list(Piece, self.Pawn_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.Knight_list):
				arcade.check_for_collision_with_list(Piece, self.Knight_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.Bishop_list):
				arcade.check_for_collision_with_list(Piece, self.Bishop_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.Rook_list):
				arcade.check_for_collision_with_list(Piece, self.Rook_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.Queen_list):
				arcade.check_for_collision_with_list(Piece, self.Queen_list)[0].kill();
			if arcade.check_for_collision_with_list(Piece, self.King_list):
				arcade.check_for_collision_with_list(Piece, self.King_list)[0].kill();




	def MovePawn(self,x,y,Pawn_list,Pawn_Select_list):
		PawnCounter =0;		
		#perviousSetUp = self.ChessGameLogic.chessBoard;
		newSetUp = None;
		goodMove = False;
		for Pawn in Pawn_list: 
			if x >= Pawn.boundary_left and x <= Pawn.boundary_right and y <= Pawn.boundary_top and y >= Pawn.boundary_bottom:
				if Pawn_Select_list[self.count] == False: #  and self.isAnyPieceSelected() == False and goodMove == False:
					Pawn_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					PossibleMovesPawn = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesPawn(self.CurrentPieceCoordinance,False),self.CurrentPieceCoordinance);	
					for Move in PossibleMovesPawn:
						try:
							if int(self.findCoordinance(x,y)[0]) == int(Move[0]) and int(self.findCoordinance(x,y)[1]) == int(Move[2]):
								newPostion = self.CoordinanceToBoardPostion(int(Move[0]),int(Move[2]));
								Pawn.center_x = newPostion[0];
								Pawn.center_y = newPostion[1];
								goodMove = True;
								self.PawnFirstMove[PawnCounter] = False;
								self.ChessGameLogic.setChessPieces(int(Move[0]),int(Move[2]),self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.HitTestBlackOnWhite(Pawn);
								self.PawnAtEndOfBoard();
								self.changeTurn();
								self.ChessGameLogic.printBoard();
						except:
							None;
					Pawn_Select_list[self.count] = False;
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					Pawn.center_x = resetMove[0];
					Pawn.center_y = resetMove[1];
			PawnCounter = PawnCounter+1;
			self.count = self.count+1;
		self.count = 0;

	def MoveKnight(self,x,y,Knight_list,Knight_Select_list):
		for Knight in Knight_list:
			goodMove = False; 
			if x >= Knight.boundary_left and x <= Knight.boundary_right and y <= Knight.boundary_top and y >= Knight.boundary_bottom:
				if Knight_Select_list[self.count] == False:
					Knight_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					Knight_Select_list[self.count] = False;
					PossibleMovesKnight = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesKnight(self.CurrentPieceCoordinance),self.CurrentPieceCoordinance);
					for Move in PossibleMovesKnight:
						try:
							NextX = int(self.findCoordinance(x,y)[0]);
							NextY = int(self.findCoordinance(x,y)[1]);
							m0 = int(Move[0]);
							m1 = int(Move[2]);
							if NextX == m0 and NextY == m1:
								newPostion = self.CoordinanceToBoardPostion(m0,m1);
								Knight.center_x = newPostion[0];
								Knight.center_y = newPostion[1];
								goodMove = True;
								self.ChessGameLogic.setChessPieces(m0,m1,self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.ChessGameLogic.printBoard();
								self.HitTestBlackOnWhite(Knight);
								self.changeTurn();
						except:
							None;		
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					Knight.center_x = resetMove[0];
					Knight.center_y = resetMove[1];
			self.count = self.count+1;
		self.count = 0;

	def MoveBishop(self,x,y,Bishop_list,Bishop_Select_list):
		for Bishop in Bishop_list:
			goodMove = False; 
			if x >= Bishop.boundary_left and x <= Bishop.boundary_right and y <= Bishop.boundary_top and y >= Bishop.boundary_bottom:
				if Bishop_Select_list[self.count] == False:
					Bishop_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					Bishop_Select_list[self.count] = False;
					PossibleMovesBishop = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesBishop(self.CurrentPieceCoordinance),self.CurrentPieceCoordinance);
					for Move in PossibleMovesBishop:
						try:
							NextX = int(self.findCoordinance(x,y)[0]);
							NextY = int(self.findCoordinance(x,y)[1]);
							m0 = int(Move[0]);
							m1 = int(Move[2]);
							if NextX == m0 and NextY == m1:
								newPostion = self.CoordinanceToBoardPostion(m0,m1);
								Bishop.center_x = newPostion[0];
								Bishop.center_y = newPostion[1];
								goodMove = True;
								self.ChessGameLogic.setChessPieces(m0,m1,self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.ChessGameLogic.printBoard();
								self.HitTestBlackOnWhite(Bishop);
								self.changeTurn();
						except:
							None;		
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					Bishop.center_x = resetMove[0];
					Bishop.center_y = resetMove[1];
			self.count = self.count+1;
		self.count = 0;

	def MoveRook(self,x,y,Rook_list,Rook_Select_list):
		for Rook in Rook_list:
			goodMove = False; 
			if x >= Rook.boundary_left and x <= Rook.boundary_right and y <= Rook.boundary_top and y >= Rook.boundary_bottom:
				if Rook_Select_list[self.count] == False:
					Rook_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					Rook_Select_list[self.count] = False;
					PossibleMovesRook = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesRook(self.CurrentPieceCoordinance),self.CurrentPieceCoordinance);
					for Move in PossibleMovesRook:
						try:
							NextX = int(self.findCoordinance(x,y)[0]);
							NextY = int(self.findCoordinance(x,y)[1]);
							m0 = int(Move[0]);
							m1 = int(Move[2]);
							if NextX == m0 and NextY == m1:
								newPostion = self.CoordinanceToBoardPostion(m0,m1);
								Rook.center_x = newPostion[0];
								Rook.center_y = newPostion[1];
								goodMove = True;
								self.ChessGameLogic.setChessPieces(m0,m1,self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.ChessGameLogic.printBoard();
								self.HitTestBlackOnWhite(Rook);
								self.changeTurn();
						except:
							None;		
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					Rook.center_x = resetMove[0];
					Rook.center_y = resetMove[1];
			self.count = self.count+1;
		self.count = 0;

	def MoveKing(self,x,y,King_list,King_Select_list):
		goodMove = False; 
		for King in King_list:
			if x >= King.boundary_left and x <= King.boundary_right and y <= King.boundary_top and y >= King.boundary_bottom:
				if King_Select_list[self.count] == False:
					King_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					King_Select_list[self.count] = False;
					PossibleMovesKing = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesKing(self.CurrentPieceCoordinance),self.CurrentPieceCoordinance);
					for Move in PossibleMovesKing:
						try:
							NextX = int(self.findCoordinance(x,y)[0]);
							NextY = int(self.findCoordinance(x,y)[1]);
							m0 = int(Move[0]);
							m1 = int(Move[2]);
							if NextX == m0 and NextY == m1:
								newPostion = self.CoordinanceToBoardPostion(m0,m1);
								King.center_x = newPostion[0];
								King.center_y = newPostion[1];
								goodMove = True;
								self.ChessGameLogic.setChessPieces(m0,m1,self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.ChessGameLogic.printBoard();
								self.HitTestBlackOnWhite(King);
								self.changeTurn();
						except:
							None;		
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					King.center_x = resetMove[0];
					King.center_y = resetMove[1];
			self.count = self.count+1;
		self.count = 0;

	def MoveQueen(self,x,y,Queen_list,Queen_Select_list):
		goodMove = False; 
		for Queen in Queen_list:
			if x >= Queen.boundary_left and x <= Queen.boundary_right and y <= Queen.boundary_top and y >= Queen.boundary_bottom:
				if Queen_Select_list[self.count] == False:
					#print("assshit");
					Queen_Select_list[self.count] = True;
					self.CurrentPieceCoordinance = self.findCoordinance(x,y);
				else:
					Queen_Select_list[self.count] = False;
					PossibleMovesQueen = self.ChessGameLogic.removeMovesThatWillPutYouInCheck(self.ChessGameLogic.findPossibleMovesQueen(self.CurrentPieceCoordinance),self.CurrentPieceCoordinance);
					for Move in PossibleMovesQueen:
						try:
							NextX = int(self.findCoordinance(x,y)[0]);
							NextY = int(self.findCoordinance(x,y)[1]);
							m0 = int(Move[0]);
							m1 = int(Move[2]);
							if NextX == m0 and NextY == m1:
								newPostion = self.CoordinanceToBoardPostion(m0,m1);
								Queen.center_x = newPostion[0];
								Queen.center_y = newPostion[1];
								goodMove = True;
								self.ChessGameLogic.setChessPieces(m0,m1,self.ChessGameLogic.returnChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]));
								self.ChessGameLogic.setChessPieces(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1], "sp");
								self.ChessGameLogic.printBoard();
								self.HitTestBlackOnWhite(Queen);
								self.changeTurn();
						except:
							None;		
				if goodMove == False:
					resetMove = self.CoordinanceToBoardPostion(self.CurrentPieceCoordinance[0],self.CurrentPieceCoordinance[1]);
					Queen.center_x = resetMove[0];
					Queen.center_y = resetMove[1];
			self.count = self.count+1;
		self.count = 0;	
	
	def findCoordinance(self,center_x,center_y):
		x=0;	
		y=0;
		if center_x-75 >= 0:
			x=x+1;
		if center_x-150 >= 0:
			x=x+1;
		if center_x-225 >= 0:
			x=x+1;
		if center_x-300 >= 0:
			x=x+1;
		if center_x-375 >= 0:
			x=x+1;
		if center_x-450 >= 0:
			x=x+1;
		if center_x-525 >= 0:
			x=x+1;
		if center_y-75 >= 0:
			y=y+1;
		if center_y-150 >= 0:
			y=y+1;
		if center_y-225 >= 0:
			y=y+1;
		if center_y-300 >= 0:
			y=y+1;
		if center_y-375 >= 0:
			y=y+1;
		if center_y-450 >= 0:
			y=y+1;
		if center_y-525 >= 0:
			y=y+1;
		return [x,y];

	def CoordinanceToBoardPostion(self,x,y):
		center_x = (x*75)+35;
		center_y = (y*75)+35;
		return [center_x,center_y];


	def PawnAtEndOfBoard(self):
		for i in range(0,8):
			if self.ChessGameLogic.returnChessPieces(i,0) == "p2":
				self.B_Pawn_list[self.count].kill();
				self.B_Queen_Select_list.append(False);	
				self.ChessGameLogic.setChessPieces(i,0,"q2");
				B_Queen = arcade.Sprite("B_Queen_img.jpg",self.chessPieces_scaling);
				B_Queen.center_x = (i*75)+35;
				B_Queen.center_y = 35;
				B_Queen.boundary_left = B_Queen.center_x-(B_Queen.width/2); 
				B_Queen.boundary_right = B_Queen.center_x+(B_Queen.width/2);
				B_Queen.boundary_top = B_Queen.center_y+(B_Queen.height/2);
				B_Queen.boundary_bottom = B_Queen.center_y-(B_Queen.height/2);
				self.B_Queen_list.append(B_Queen);
				return True;
			if self.ChessGameLogic.returnChessPieces(i,7) == "p1":
				self.Pawn_list[self.count].kill();
				self.Queen_Select_list.append(False);	
				self.ChessGameLogic.setChessPieces(i,7,"q1");
				Queen = arcade.Sprite("Queen_img.jpg",self.chessPieces_scaling);
				Queen.center_x = (i*75)+35;
				Queen.center_y = 560;
				Queen.boundary_left = Queen.center_x-(Queen.width/2); 
				Queen.boundary_right = Queen.center_x+(Queen.width/2);
				Queen.boundary_top = Queen.center_y+(Queen.height/2);
				Queen.boundary_bottom = Queen.center_y-(Queen.height/2);
				self.Queen_list.append(Queen);
				return True;
		return False;


	def on_mouse_motion(self, x, y, dx, dy):
		sub_counter=0;
		for Selected_King in self.King_Select_list:
			if Selected_King:
				self.King_list[sub_counter].center_x = x;
				self.King_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;	
		for Selected_King in self.B_King_Select_list:
			if Selected_King:
				self.B_King_list[sub_counter].center_x = x;
				self.B_King_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Queen in self.Queen_Select_list:
			if Selected_Queen:
				self.Queen_list[sub_counter].center_x = x;
				self.Queen_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;	
		for Selected_Queen in self.B_Queen_Select_list:
			if Selected_Queen:
				self.B_Queen_list[sub_counter].center_x = x;
				self.B_Queen_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Pawn in self.Pawn_Select_list:
			if Selected_Pawn:
				self.Pawn_list[sub_counter].center_x = x;
				self.Pawn_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Pawn in self.B_Pawn_Select_list:
			if Selected_Pawn:
				self.B_Pawn_list[sub_counter].center_x = x;
				self.B_Pawn_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Bishop in self.Bishop_Select_list:
			if Selected_Bishop:
				self.Bishop_list[sub_counter].center_x = x;
				self.Bishop_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_B_Bishop in self.B_Bishop_Select_list:
			if Selected_B_Bishop:
				self.B_Bishop_list[sub_counter].center_x = x;
				self.B_Bishop_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Knight in self.Knight_Select_list:
			if Selected_Knight:
				self.Knight_list[sub_counter].center_x = x;
				self.Knight_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Knight in self.B_Knight_Select_list:
			if Selected_Knight:
				self.B_Knight_list[sub_counter].center_x = x;
				self.B_Knight_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Rook in self.Rook_Select_list:
			if Selected_Rook:
				self.Rook_list[sub_counter].center_x = x;
				self.Rook_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;
		sub_counter=0;
		for Selected_Rook in self.B_Rook_Select_list:
			if Selected_Rook:
				self.B_Rook_list[sub_counter].center_x = x;
				self.B_Rook_list[sub_counter].center_y = y;
			sub_counter=sub_counter+1;	
def main():
	game = ChessGame(600, 600);
	game.setup();
	arcade.run();


if __name__ == "__main__":
	main();