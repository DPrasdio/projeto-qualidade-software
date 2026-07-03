"""
Regra de negócio: Gerenciamento de restaurantes favoritos.

Contexto: no PBL5, foi identificado o BUG-02 — "favorito não persiste
entre sessões". Esta funcionalidade implementa o gerenciamento de
favoritos de forma persistente (em memória, simulando um repositório),
evitando duplicidade e permitindo listar os favoritos de um usuário.
"""

class GerenciadorFavoritos:
    """Gerencia os restaurantes favoritados por cada usuário."""

    def __init__(self):
        # Simula uma "persistência": usuario_id -> conjunto de restaurante_id
        self._favoritos = {}

    def adicionar(self, usuario_id: str, restaurante_id: str) -> None:
        """Adiciona um restaurante aos favoritos do usuário.

        Não gera duplicidade: favoritar duas vezes o mesmo restaurante
        não cria entradas repetidas.
        """
        if not usuario_id or not restaurante_id:
            raise ValueError("usuario_id e restaurante_id são obrigatórios")

        if usuario_id not in self._favoritos:
            self._favoritos[usuario_id] = set()

        self._favoritos[usuario_id].add(restaurante_id)

    def remover(self, usuario_id: str, restaurante_id: str) -> None:
        """Remove um restaurante dos favoritos do usuário, se existir."""
        if usuario_id in self._favoritos:
            self._favoritos[usuario_id].discard(restaurante_id)

    def listar(self, usuario_id: str) -> list:
        """Retorna a lista de restaurantes favoritos de um usuário."""
        return sorted(self._favoritos.get(usuario_id, set()))

    def eh_favorito(self, usuario_id: str, restaurante_id: str) -> bool:
        """Verifica se um restaurante está entre os favoritos do usuário."""
        return restaurante_id in self._favoritos.get(usuario_id, set())
