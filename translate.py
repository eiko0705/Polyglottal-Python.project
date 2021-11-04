from googletrans import Translator
import summary

translator = Translator()

summary_contents = summary.lexrank_summary()


def summary_translate():

    # translate summary
    result = translator.translate(summary_contents[0], src="en", dest="ja")

    return result.text


if __name__ == '__main__':
    summary_translate()
