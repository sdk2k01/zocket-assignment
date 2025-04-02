from dotenv import load_dotenv
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from gradio import mount_gradio_app
from mistralai.models.sdkerror import SDKError

from .ui import demo, retrieve_from_agent

load_dotenv(override=True)

# Instantiate FastAPI App
app = FastAPI()


# Endpoint for agentic query
@app.get("/agent-query")
async def agent_query(query: str):
    status_code = status.HTTP_200_OK
    result = {}
    try:
        result = retrieve_from_agent(query)
    except SDKError as e:
        status_code = status.HTTP_502_BAD_GATEWAY
        result = e.body
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        result = f"{str(e)}"

    return JSONResponse(status_code=status_code, content=result)


app = mount_gradio_app(app, demo, path="/")
