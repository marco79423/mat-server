import click


@click.group()
def cli():
    """歡迎使用 mat-server"""
    pass


@cli.command('init', short_help='初始化 mat 設定')
def init():
    print('初始化 mat 設定')


@cli.command('serve', short_help='啟動 mat-server 伺服器')
@click.option('--host', default='0.0.0.0', help='啟動的 host')
@click.option('-p', '--port', default=9527, help='啟動的 port')
def serve(host, port):
    print(f'啟動 mat-server 伺服器 (http://{host}:{port})')

