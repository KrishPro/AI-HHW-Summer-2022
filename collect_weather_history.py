"""
Written by KrishPro @ KP
"""

from typing import Dict, List
import requests
import argparse
import json
import os

API_PATH = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
API_KEY = "e40274f51fdf46b78d3185954222006"

def get_response(args: argparse.Namespace) -> Dict[str, Dict[str, List[dict]]]:
    """Create the the header for the request from the args and then hits the API and returns the response

    Args:
        args (argparse.Namespace): Parsed Arguments

    Returns:
        Dict[str, Dict[str, List[dict]]]: response from the API
    """

    # Preparing the header for the request
    header = {
        'q': args.location,
        'date': args.start_date,
        'enddate': args.end_date,
        'format': 'json',
        'tp': args.interval,
        'key': API_KEY
    }

    return requests.get(API_PATH, header).json()

def check_error(response: Dict[str, Dict[str, List[dict]]]):
    """This checks, if the response have any error message in it. Then, Displays the message and exits the program

    Args:
        response (Dict[str, Dict[str, List[dict]]]): The response from the API
    """
    # Checks if the response contains the error
    if 'error' in response['data'].keys():

        # Prints the error message
        print("ERROR:", ' and '.join([e['msg'] for e in response['data']['error']]))

        # Exits the program
        print("Exitting...")
        exit()

def dump_response(response: Dict[str, Dict[str, List[dict]]], file_path: str):
    """Simply, dumpes the response as json on the file_path

    Args:
        response (Dict[str, Dict[str, List[dict]]]): The response from the API
        file_path (str): File path, where the response will be dumped
    """
    # Opens the file
    with open(file_path, 'w') as f:

        # Dumps into the file
        json.dump(response, f)


def main(args: argparse.Namespace):
    """Hits the API and Saves the results

    Args:
        args (argparse.Namespace): Parsed Arguments
    """

    # Fetching the response
    response = get_response(args)

    # Checking for errors in the responce
    check_error(response)
  
    # Printing what we have fetched
    print(f"Location: {response['data']['request'][0]['query']}")
    print(f"Start Date: {args.start_date}")
    print(f"End Date: {args.end_date}")
    
    # Creating file_path
    file_dir = args.output_dir
    file_name = f'detailed.json'
    file_path = os.path.join(file_dir, file_name)

    # Making sure that the file_dir exists
    if not os.path.exists(file_dir): os.makedirs(file_dir)
    
    # Dumping the response
    dump_response(response, file_path)

    # Logging the output file path
    print()
    print(f"Output file: {file_path}")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--location', '-l', default="noida", type=str)
    parser.add_argument('--start-date', '-sd', default="2022-06-01", type=str)
    parser.add_argument('--end-date', '-ed', default="2022-06-15", type=str)
    parser.add_argument('--interval', '-i', default=3, type=int)
    parser.add_argument('--output-dir', '-o', default="Data", type=str)

    args = parser.parse_args()
    main(args)