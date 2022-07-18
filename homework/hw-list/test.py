import subprocess
import os
import time

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

def test_word_count_p():
    print('Testing pword')
    print('=============\n')
    path = './gutenberg'

    command_should = './words'
    command_actual = './pwords'

    for file_name in os.listdir(path):
        command_should = f'{command_should} {path}/{file_name}'
        command_actual = f'{command_actual} {path}/{file_name}'

    print(f'Begin testing {command_should} and {command_actual}')

    start_time = time.time()
    process_should = new_process(command_should)
    result_should, _ = process_should.communicate()
    end_time = time.time()
    interval_should = end_time - start_time
    print(f'words execution time is {interval_should} s')

    start_time = time.time()
    process_actual = new_process(command_actual)
    result_actual, _ = process_actual.communicate()
    end_time = time.time()
    interval_actual = end_time - start_time
    print(f'pwords execution time is {interval_actual} s')
    if(result_should != '' and result_should == result_actual):
        print(f'Successful')
    else:
        print(f'Failed')
    print()

if __name__ == '__main__':
    test_word_count_l()
    test_word_count_p()
