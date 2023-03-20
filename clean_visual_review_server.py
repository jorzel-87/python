#!/usr/bin/env python

import requests
import logging

max_runs_in_suit = 20

abc_mailing_assets = requests.get(
    'http://<ip>:7000/api/projects/1/suites/1')
abc_app = requests.get(
    'http://<ip>:7000/api/projects/1/suites/2')
abc_manager_app = requests.get(
    'http://<ip>:7000/api/projects/2/suites/3')

suits = [abc_mailing_assets, abc_app, abc_manager_app]

server_url = 'http://<ip>:7000/api/runs/{}'

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s - %(asctime)s - %(message)s',
                    datefmt='%H:%M:%S')

def delete_runs_from_server(runs, server_url):
    for run in runs:
        run_url = server_url.format(run["id"])
        logging.info(f"removing {run_url} started")
        requests.delete(run_url)

def main():
    global suits, server_url
    for suit in suits:
        jsonResponse = suit.json()
        runs_to_delete = jsonResponse["runs"][max_runs_in_suit:]
        delete_runs_from_server(runs_to_delete, server_url)

if __name__ == "__main__":
    main()
