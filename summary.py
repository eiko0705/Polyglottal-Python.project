import scraping
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

mylist = scraping.scraping()
contents = []

for title, content in mylist:
    contents.append(content)


def lexrank_summary():

    summary_list = []

    for content in contents:

        # for strings
        parser = PlaintextParser.from_string(content, Tokenizer("english"))

        # using LexRank
        summarizer = LexRankSummarizer()

        # summarize the document with 3 sentences
        summary = summarizer(parser.document, 3)

        summary_list.append(summary)

    return summary_list


if __name__ == '__main__':
    lexrank_summary()
