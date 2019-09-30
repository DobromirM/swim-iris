import websocket


def generate_once(node, lane, value):
    message = f'@command(node:{node},lane:{lane}){value}'
    # equivalent old-school syntax:
    #   message = '@command(node:%s,lane:%s)%s' % (node, lane v)
    ws.send(message)


if __name__ == '__main__':
    ws = websocket.create_connection('ws://localhost:9001')
    generate_once('/training/1', 'publish', 'Hello, World!')
