from swimai import SwimClient

from ml.record import TrainingRecord, TestingRecord, handle_training_record, handle_testing_record


async def receive_training(new_value, old_value):
    if new_value:
        print(f'Received new training record {new_value}')
        handle_training_record(new_value)


async def receive_testing(new_value, old_value):
    if new_value:
        print(f'Received new testing record {new_value}')
        handle_testing_record(new_value)


if __name__ == '__main__':
    open('output/accuracies.txt', 'w').close()
    open('output/testing_results.txt', 'w').close()

    uri = "ws://localhost:9001"
    training_agents = list()
    training_agents.append('/training/1')
    training_agents.append('/training/2')
    training_agents.append('/training/3')
    training_agents.append('/training/4')
    testing_agents = list()
    testing_agents.append('/testing/1')
    testing_agents.append('/testing/2')

    swim_client = SwimClient()
    swim_client.start()

    for agent in training_agents:
        downlink = swim_client.downlink_value()
        downlink.set_host_uri(uri)
        downlink.set_node_uri(agent)
        downlink.set_lane_uri('data')
        downlink.did_set(receive_training)
        downlink.register_class(TrainingRecord)
        downlink.open()

    for agent in testing_agents:
        downlink = swim_client.downlink_value()
        downlink.set_host_uri(uri)
        downlink.set_node_uri(agent)
        downlink.set_lane_uri('data')
        downlink.did_set(receive_testing)
        downlink.register_class(TestingRecord)
        downlink.open()

    print('Client has been started and it\'s waiting for data...')
