import os
from datapreprocess import preprocess
import train_eval
from config import Config


class Robot():
    def __init__(self):
        pass

    def init_torch(self, **kwargs):
        self.opt = Config()
        for k, v in kwargs.items():  # 设置参数
            setattr(self.opt, k, v)

        self.searcher, self.sos, self.eos, self.unknown, self.word2ix, self.ix2word = train_eval.test(self.opt)

        if os.path.isfile(self.opt.corpus_data_path) == False:
            preprocess()

    def answer(self, input_sentence) -> str:
        output_words = train_eval.output_answer(input_sentence, self.searcher, self.sos, self.eos, self.unknown,
                                                self.opt, self.word2ix, self.ix2word)
        return output_words


robot = Robot()
