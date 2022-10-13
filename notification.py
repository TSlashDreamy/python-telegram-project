import schedule
#import requests
time="8:30"

def greeting():
    """Greeting function"""

    todos_dict = {
        '08:30': 'ООП',
        '10:20': 'It-проекти',
    }
    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')

def main():
    schedule.every().day.at('8:30').do(greeting)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()