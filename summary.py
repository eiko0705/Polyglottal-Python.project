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
        summary_tuple = summarizer(parser.document, 3)

        # convert tuple to string
        summary_str = ' '.join(map(str, summary_tuple))

        summary_list.append(summary_str)

    return summary_list


if __name__ == '__main__':
    lexrank_summary()
