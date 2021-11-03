from googletrans import Translator
import summary

translator = Translator()

summary_contents = summary.lexrank_summary()


def summary_translate():

    tranlate_summary = []

    for summary in summary_contents:

        # translate summary
        result = translator.translate(summary, src="en", dest="ja")

        # push into the translate_summary list
        tranlate_summary.append(result.text)

    return tranlate_summary


print(summary_translate())

if __name__ == '__main__':
    summary_translate()
