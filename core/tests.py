# Django
from django.conf.urls import url, include
from django.urls import path
from django.test import TestCase

# Djangorestframework
from rest_framework import routers
from rest_framework.test import RequestsClient, APITestCase

# Model
from boards.models import Board

# Viewsets
from boards.views import BoardViewSet


# Model tests
class BoardModelTest(TestCase):
    """ Test module for Boards model """

    def setUp(self):
        Board.objects.create(board_size=8)

    def test_board_size(self):
        board_twelve = Board.objects.get(board_size=8)
        self.assertEqual(board_twelve.get_size(), 'The board size is 8')

    def create_board(self, board_size=9):
        return Board.objects.create(board_size=board_size)

    def test_course_creation(self):
        board_size = self.create_board()
        self.assertTrue(isinstance(board_size, Board))
        self.assertEqual(board_size.__str__(), board_size.board_size)

# API tests
class BoardsApiTest(APITestCase):
    """ Test API"""
    urlpatterns = [
        path('api/v1/', include('core.urls.v1')),
    ]

    def test_boards_url(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/boards/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual('{"id": 1, "board_size": 8}', '{"id": 1, "board_size": 8}')


# Extra action decorators
class TestExtraActions(TestCase):
    """ Test Extra Actions """
    router = routers.DefaultRouter()
    router.register(r'boards', BoardViewSet)

    urlpatterns = [
        url(r'', include(router.urls)),
    ]

    def test_action_routes(self):
        # Get action routes (first two are boards/detail)
        routes = self.router.get_routes(BoardViewSet)[2:]

        assert routes[0].url == '^{prefix}/{lookup}/results{trailing_slash}$'
        assert routes[0].mapping == {
            'get': 'results',
        }
