import subprocess
import os

def new_process(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,encoding="utf-8")
    return p

def test_word_count_l():
    print('Testing lword')
    print('=============\n')
    path = './gutenberg'
    for file_name in os.listdir(path):
        command_should = f'./words {path}/{file_name}'
        command_actual = f'./lwords {path}/{file_name}'
        print(f'Begin testing {command_should} and {command_actual}')
        process_should = new_process(command_should)
        process_actual = new_process(command_actual)
        result_should, _ = process_should.communicate()
        result_actual, _ = process_actual.communicate()
        if(result_should != '' and result_should == result_actual):
            print(f'Successful')
        else:
            print(f'Failed')
        print()

if __name__ == '__main__':
    test_word_count_l()
