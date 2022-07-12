import json
import itertools
from typing import List


def get_input():
    with open('example_big.in.json', 'r') as file:
        inputs = json.load(file)
    return inputs


def get_desired_output():
    with open('example_big.out', 'r') as file:
        output = file.readlines()
    return [x.strip() for x in output]


def create_dictionary(pairs: List[list]) -> List[list]:
    k: list = pairs.copy()
    for a, j in enumerate(k):
        i = []
        for m, d in enumerate(di):
            if j[0] in d or j[1] in d:
                for ele in d:
                    if ele not in j:
                        i.append(ele)
        i = list(set(i))
        j.extend(i)
    # clean dictionary
    all_list = list([list(set(x)) for x in k])
    all_list.sort()
    main_dict = list(all_list for all_list,_ in itertools.groupby(all_list))
    return main_dict


def generate_results(main_dict: List[list]) -> list:
    results = []
    for y, i in q:
        do_continue = False
        f = y.lower()
        s = i.lower()
        if f == s:
            results.append('synonyms')
            continue
        for j in main_dict:
            if f in j and s in j:
                results.append('synonyms')
                do_continue = True
                break
        if not do_continue:
            results.append('different')
    return results   

    
def check_output(results: list, output: list) -> int:
    score: int = 0
    output = [x.strip() for x in output]
    for x, i in zip(results, output):
        if x == i:
            score += 1
    return score


if __name__ == "__main__":
    inputs = get_input()
    desired_output = get_desired_output()

    results = []
    for t in inputs['testCases']:
        # clean inputs
        di = t['dictionary']
        di = [[x[0].lower(), x[1].lower()] for x in di if x[0].lower() != x[1].lower()]
        q = t['queries']
        q = [[x[0].lower(), x[1].lower()] for x in q]
        # create dictionary
        main_dict = create_dictionary(di)
        # get results
        results.extend(generate_results(main_dict))
        
    score = check_output(results, output)
    print(f'Your score: {score}/{len(output)}')

