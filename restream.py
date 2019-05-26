"""
This module includes lex and yacc classes to tokenize and parse a string into a data-structure based on token and
grammar rules
"""


import re


version = '0.0.3'


class TokenStream:
    """
    Token stream class is a wrapper on a list which provides ge, peak and seek functions to get and set the head of a
    consumable list
    """
    def __init__(self, token_stream: list):
        """
        Init
        :param token_stream: list to be converted into a token-string
        """
        self.token_stream = token_stream
        self.head = 0

    def get(self) -> list:
        """
        Returns and consumes the head of the stream
        :return: the head element
        """
        if self.head == len(self.token_stream):
            return [None, None]

        self.head += 1
        return self.token_stream[self.head - 1]

    def peak(self) -> list:
        """
        Returns the head of the stream but does not consume it
        :return: the head element
        """
        if self.head == len(self.token_stream):
            return [None, None]

        return self.token_stream[self.head]

    def seek(self, head) -> None:
        """
        Sets the head to an index
        :param head: The index of the new head
        :return: None
        """
        if head < 0 or head > len(self.token_stream):
            return
        self.head = head

    def to_list(self):
        """
        Returns the original list
        :return: original list
        """
        return self.token_stream[self.head:]

    def __str__(self):
        """
        String representation of the token stream
        :return: string representation
        """
        return str(self.token_stream[self.head:])


class Lex:
    """
    This is the lex class, this provides lexical scanning functions
    """
    def __init__(self, token_list: list, ignore_list: list):
        """
        Init
        :param token_list: List of tokens {list of lists(name, regex)}
        :param ignore_list: List of tokens to ignore string(name)
        """
        self.token_list = [(token_name, re.compile(token_rule)) for token_name, token_rule in token_list]
        self.ignore_list = ignore_list

    def tokenize(self, text: str) -> TokenStream:
        """
        Tokenize the input string and returns a tokens-stream
        :param text:
        :return:
        """
        matched_tokens = []

        while text:
            for token_name, token_rule in self.token_list:
                match = token_rule.match(text)
                if match:
                    if token_name not in self.ignore_list:
                        matched_tokens.append((token_name, match.group()))
                    text = text[match.end():]
                    break
            else:
                err_str = text.split("\n", 2)[0]
                raise AssertionError('Error at: {} ...'.format(err_str))
        return TokenStream(matched_tokens)

    def tokenize_verbose(self, text: str) -> TokenStream:
        """
        Tokenize the input string and returns a tokens-stream with verbose outputs
        This is meant to be used for debugging
        :param text:
        :return:
        """
        matched_tokens = []

        while text:
            for token_name, token_rule in self.token_list:
                match = token_rule.match(text)
                if match:
                    print('Matched: {}'.format(match.group()))
                    if token_name not in self.ignore_list:
                        matched_tokens.append((token_name, match.group()))
                    text = text[match.end():]
                    break
            else:
                err_str = text.split("\n", 2)[0]
                raise AssertionError('Error at: {} ...'.format(err_str))
        return TokenStream(matched_tokens)


class Yacc:
    """
    This is the yacc class, this provides parsing of a token-string based on a grammar
    """
    def __init__(self, grammar: dict):
        """
        Init
        :param grammar: Grammar for the syntax
        """
        self.grammar = grammar

    def parse(self, tokens: TokenStream, lhs: str = 'start') -> object:
        """
        Parses a token-string into a data structure
        :param tokens: Token-stream
        :param lhs: Current state
        :return: parsed data structure else False of syntax error
        """
        productions = self.grammar[lhs]

        head = tokens.head
        for production in productions:
            args = []
            rhs = production[:-1]
            func = production[-1]

            for symbol in rhs:
                res = None
                if symbol not in self.grammar and symbol == tokens.peak()[0]:
                    res = tokens.get()[1]
                elif symbol in self.grammar:
                    res = self.parse(tokens, symbol)

                if res:
                    args.append(res)
                else:
                    tokens.seek(head)
                    break
            else:
                return func(*args)
        return False

    def parse_verbose(self, tokens: TokenStream, lhs: str = 'start') -> object:
        """
        Parses a token-string into a data structure with verbose outputs
        This is meant to be used for debugging
        :param tokens: Token-stream
        :param lhs: Current state
        :return: parsed data structure else False of syntax error
        """
        productions = self.grammar[lhs]

        head = tokens.head
        for production in productions:
            print('============================================================')
            print('production: {}'.format(production[:-1]))
            args = []
            rhs = production[:-1]
            func = production[-1]

            for symbol in rhs:
                print('------------------------------------------------------------')
                print('Symbol: {} - Token: {}'.format(symbol, tokens.peak()[0]))
                res = None
                if symbol not in self.grammar and symbol == tokens.peak()[0]:
                    print('Matched symbol: {}'.format(res))
                    res = tokens.get()[1]
                elif symbol in self.grammar:
                    print('Matched production: {}'.format(symbol))
                    res = self.parse_verbose(tokens, symbol)

                if res:
                    args.append(res)
                else:
                    tokens.seek(head)
                    break
            else:
                return func(*args)
        return False
