import requests
from http import HTTPStatus


class TestApiEndpoint:
    @classmethod
    def setup_class(cls):
        cls.web = lambda cls, endpoint, params=None: requests.get(
            f"http://localhost:8000{endpoint}", params
        )

    @classmethod
    def teardown_class(cls):
        del cls.web

    def test_home(self):
        assert self.web("/").status_code == HTTPStatus.OK

    def test_ecoles(self):
        assert self.web("/ecoles").status_code == HTTPStatus.OK

    def test_ecoles_par_groupe(self):
        params = {"groupe": "INP"}
        assert self.web("/ecoles",params).status_code == HTTPStatus.OK

    def test_ecole(self):
        _id = "8"
        assert self.web(f"/ecoles/{_id}").status_code == HTTPStatus.OK

    def test_ecole_inexistante(self):
        _id = "42"
        assert self.web(f"/ecoles/{_id}").status_code == HTTPStatus.NOT_FOUND