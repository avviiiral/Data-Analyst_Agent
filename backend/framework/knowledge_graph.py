from __future__ import annotations

from collections import defaultdict


class KnowledgeGraph:

    def __init__(self):

        self._graph = defaultdict(set)

    def add_relation(
        self,
        source: str,
        relation: str,
        target: str,
    ):

        self._graph[source].add((relation, target))

    def neighbors(
        self,
        source: str,
    ):

        return list(self._graph.get(source, []))

    def related(
        self,
        source: str,
        relation: str,
    ):

        return [
            target
            for rel, target in self._graph.get(source, [])
            if rel == relation
        ]

    def nodes(self):

        return sorted(self._graph.keys())

    def clear(self):

        self._graph.clear()

    def snapshot(self):

        return {
            node: list(edges)
            for node, edges in self._graph.items()
        }


knowledge_graph = KnowledgeGraph()