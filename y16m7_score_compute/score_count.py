import re
import threading
import sys


class score_count_thread(threading.Thread):
    def __init__(self, filepath):
        self.filepath = filepath
        self.sum_score = 0
        self.result = 0
        return super(score_count_thread, self).__init__()
    def run(self):
        f = open(self.filepath, 'r')
        num = 0
        iter_line = iter(f)
        for line in iter_line:
            data = re.search(r':(100|[1-9]?[0-9])', line).group()
            if data:
                score = int(data[1:])
                num += 1
                self.sum_score += score
            else:
                print '%s is invalid!' % line
        f.close()
        self.result = self.sum_score / num
        print '%d students\' sum score is %d, the avg score is %d.\n' % (num, self.sum_score, self.result)


def score_count(filepath_list):
    for filepath in filepath_list:
        t = score_count_thread(filepath)
        t.start()

if __name__ == '__main__':
    print sys.argv[1:]
    score_count(sys.argv[1:])