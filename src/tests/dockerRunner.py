import docker

def is_running(container_name):
    """
    verify the status of a sniffer container by it's name
    :param container_name: the name of the container
    :return: Boolean if the status is ok
    """
    try:
        DOCKER_CLIENT = docker.from_env()
        RUNNING = 'running'

        container = DOCKER_CLIENT.containers.get(container_name)
        container_state = container.attrs['State']
        container_is_running = container_state['Status'] == RUNNING
        return container_is_running
    except Exception:
        print("Make sure the Splash Docker container is turned on!")
        return False

if __name__ == '__main__':
    my_container_name = "splash"
    print(is_running(my_container_name))