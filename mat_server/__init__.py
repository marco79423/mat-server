from mat_server.app import Container

container = Container()
cli = container.create_cli()

if __name__ == '__main__':
    cli()
