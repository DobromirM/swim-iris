import asyncio

from client import run

if __name__ == '__main__':
    uri = "ws://localhost:9001"

    agents = list()
    agents.append(['/training/1', 'data'])
    agents.append(['/training/2', 'data'])
    agents.append(['/training/3', 'data'])
    agents.append(['/training/4', 'data'])

    agents.append(['/testing/1', 'data'])
    agents.append(['/testing/2', 'data'])

    asyncio.get_event_loop().run_until_complete(run(uri, agents))
