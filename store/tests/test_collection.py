from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from store.models import Collection
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_is_anonymous_return_401(self):
        client = APIClient()

        response = client.post("/store/collections/", {"title": "a"})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_401(self):
        client = APIClient()
        client.force_authenticate(user={})

        response = client.post("/store/collections/", {"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self):
        client = APIClient()
        User = get_user_model()
        client.force_authenticate(user=User(is_staff=True))

        response = client.post("/store/collections/", {"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_return_201(self):
        client = APIClient()
        User = get_user_model()
        client.force_authenticate(user=User(is_staff=True))

        response = client.post("/store/collections/", {"title": "a"})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self):
        collection = baker.make(Collection)
        client = APIClient()

        response = client.get(f"/store/collections/{collection.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"id": collection.id, "title": collection.title}
