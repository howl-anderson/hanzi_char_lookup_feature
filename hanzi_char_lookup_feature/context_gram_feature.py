from typing import List, Dict, Union


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
    def __init__(self, left_context: Union[None, Feature], right_context: Union[None, Feature]):
        self.left_context = left_context
        self.right_context = right_context

    @property
    def contexts(self):
        return self.left_context, self.right_context

    def __str__(self):
        return "<L: {!s}, R: {!s}>".format(self.left_context, self.right_context)

    def __repr__(self):
        return "<L: {!s}, R: {!s}>".format(self.left_context, self.right_context)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.left_context == other.left_context and self.right_context == other.right_context


class TokenGramFeature:
    def __init__(self, token, n_gram_feature=None):
        self.token = token
        self.n_gram_feature = (
            n_gram_feature if n_gram_feature is not None else {}
        )  # type: Dict[int, GramFeature]

    def __str__(self):
        return "[{!s} | {!s}]".format(self.token, self.n_gram_feature)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.token == other.token and self.n_gram_feature == other.n_gram_feature

    def __hash__(self):
        return hash((self.token, self.n_gram_feature.items()))


class ContextGramFeature(List[TokenGramFeature]):
    pass
