import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import pytest
from app import app, db, Task


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client


def test_criar_tarefa(client):
    response = client.post(
        "/create",
        data={
            "title": "Tarefa Teste",
            "description": "Descrição",
            "status": "Pendente",
            "prazo_entrega": "2025-12-31",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Tarefa Teste" in response.data


def test_listar_tarefas(client):
    client.post(
        "/create",
        data={
            "title": "Tarefa A",
            "description": "Desc A",
            "status": "Pendente",
            "prazo_entrega": "2025-12-01",
        },
        follow_redirects=True,
    )

    client.post(
        "/create",
        data={
            "title": "Tarefa B",
            "description": "Desc B",
            "status": "Pendente",
            "prazo_entrega": "2025-12-02",
        },
        follow_redirects=True,
    )

    response = client.get("/")
    assert b"Tarefa A" in response.data
    assert b"Tarefa B" in response.data


def test_atualizar_tarefa(client):
    client.post(
        "/create",
        data={
            "title": "Antigo",
            "description": "Desc Antiga",
            "status": "Pendente",
            "prazo_entrega": "2025-12-03",
        },
        follow_redirects=True,
    )

    tarefa = Task.query.first()

    response = client.post(
        f"/update/{tarefa.id}",
        data={
            "title": "Atualizado",
            "description": "Nova descrição",
            "status": "Concluído",
            "prazo_entrega": "2025-12-10",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Atualizado" in response.data
    assert (
        b"Nova descri\xc3\xa7\xc3\xa3o" in response.data
    )  # <- versão com acento codificado


def test_deletar_tarefa(client):
    client.post(
        "/create",
        data={
            "title": "Para Deletar",
            "description": "Teste",
            "status": "Pendente",
            "prazo_entrega": "2025-12-04",
        },
        follow_redirects=True,
    )

    tarefa = Task.query.first()
    response = client.get(f"/delete/{tarefa.id}", follow_redirects=True)
    assert response.status_code == 200
    assert b"Para Deletar" not in response.data
