#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=10&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    for questiondict in data["results"]:
        print(questiondict["question"])
        print(questiondict["correct_answer"])
if __name__ == "__main__":
    main()

