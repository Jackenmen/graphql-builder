from typing import Any, Dict, Iterator, Protocol, TypeVar

from .template import GraphQLChainMap

__all__ = ("FieldBuilderT", "NestableFieldBuilderT")


class GraphQLFieldBuilderProtocol(Protocol):
    def __init__(self) -> None:
        ...

    def _append(self, substitutions: Dict[str, Any]) -> None:
        ...

    def iter_calls(self, parent_substitutions: GraphQLChainMap) -> Iterator[str]:
        ...


class GraphQLNestableFieldBuilderProtocol(Protocol):
    def __init__(self, substitutions: Dict[str, Any]) -> None:
        ...

    def iter_calls(self, parent_substitutions: GraphQLChainMap) -> Iterator[str]:
        ...


FieldBuilderT = TypeVar("FieldBuilderT", bound=GraphQLFieldBuilderProtocol)
NestableFieldBuilderT = TypeVar(
    "NestableFieldBuilderT", bound=GraphQLNestableFieldBuilderProtocol
)
