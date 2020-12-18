import os
import uvicorn

import app


def get_app_port() -> int:
    app_port_env = os.environ.get('APP_PORT')
    return int(app_port_env) if app_port_env else 8000


if __name__ == '__main__':
    uvicorn.run(app.main.app, host="0.0.0.0", port=get_app_port())
