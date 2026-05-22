# Estrutura do Projeto

## models/

Contém as classes ORM (SQLAlchemy) que representam as tabelas do banco de dados. Cada arquivo define uma entidade.

## schemas/

Define os modelos Pydantic de entrada (request) e saída (response) da API. Responsável pela validação e serialização dos dados.

## controllers/

Contém os routers do FastAPI com os endpoints. É onde fica a lógica de cada rota — recebe a requisição, interage com o banco e retorna a resposta.

---

## `__init__.py` e Namespace Packages

O `__init__.py` transforma uma pasta em um **pacote Python** e permite centralizar exports:

```python
# models/__init__.py
from .account import Account
from .transaction import Transaction
```

Isso permite importar diretamente do pacote:

```python
from ..models import Account, Transaction
```

Sem o `__init__.py`, desde o Python 3.3, a pasta ainda funciona como um **namespace package** — mas os imports ficam mais verbosos e não há um ponto central para controlar o que é público. Na prática, usar `__init__.py` mantém os imports limpos e explícitos.
