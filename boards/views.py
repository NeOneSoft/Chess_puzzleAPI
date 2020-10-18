# Djangorestframework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models and Serializers
from .models import Board
from .serializers import BoardSerializer, CreateBoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBoardSerializer
        return BoardSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.solutions = 0

    # Put queens over chess board using recursive function
    def put_queen(self, positions, target_row):
        """
        1.- Check if we can put a queen over N according to the possible cases
        2.- If we found a valid place try to the same for the next row using
        our recursive function
        3.- Repeat the action until complete our N*N chessboard
        """
        # In case we reach our chess board size, give the number solutions. If the number of target_row == N row size,
        # print our chess board
        board_size = self.get_object()
        size = board_size.board_size
        if target_row == size:
            self.solutions += 1
            self.show_full_positions(positions)  # This line print the positions for each solution on console
        else:
            # Traverse over N columns positions try to place a queen
            for column in range(size):
                # Define invalid positions
                if self.verify_position(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    # Check function to verify queen's position
    def verify_position(self, positions, ocuppied_rows, column):
        """
        This function check the position according to previous placed queens, using column and diagonal constraits
        """
        for i in range(ocuppied_rows):
            # Check column positions and diagonal positions
            if positions[i] == column or \
                    positions[i] - i == column - ocuppied_rows or \
                    positions[i] + i == column + ocuppied_rows:
                return False
        return True

    # Print our positions for each solution
    def show_full_positions(self, positions):
        print(positions)

    # Find the number of solutions for N*N size chess board
    @action(detail=True, methods=['GET'])
    def results(self, request, pk=None):
        board_size = self.get_object()
        size = board_size.board_size
        positions = [-1] * size
        self.put_queen(positions, 0)
        return Response({"Number of found solutions": self.solutions})
