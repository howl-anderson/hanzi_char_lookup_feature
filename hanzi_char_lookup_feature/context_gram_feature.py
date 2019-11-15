from typing import List, Dict


class Feature(List[str]):
    pass


def create_feature(obj):
    if obj is None:
        return None
    if isinstance(obj, list):
        return Feature(obj)
    else:
        raise ValueError()


class GramFeature:
    def __init__(self, left_context: Feature, right_context: Feature):
        self.left_context = left_context
        self.right_context = right_context

    @property
    def contexts(self):
        return self.left_context, self.right_context

    def __str__(self):
        return "<L: {!s}, R: {!s}>".format(self.left_context, self.right_context)

    def __repr__(self):
        return "<L: {!s}, R: {!s}>".format(self.left_context, self.right_context)


class TokenGramFeature:
    def __init__(self, token, n_gram_feature=None):
        self.token = token
        self.n_gram_feature = (
            n_gram_feature if n_gram_feature is not None else {}
        )  # type: Dict[int, GramFeature]

    def __str__(self):
        return "[{!s} | {!s}]".format(self.token, self.n_gram_feature)


class ContextGramFeature(List[TokenGramFeature]):
    pass
