
import azure.functions as func

# Create the Azure Functions application.
app = func.FunctionApp()


# HTTP trigger means this function runs when
# someone sends an HTTP request to its URL.
@app.route(
    route="hello",
    auth_level=func.AuthLevel.ANONYMOUS
)
def hello(req: func.HttpRequest) -> func.HttpResponse:

    # Read the name from the URL query string.
    # Example: ?name=Shailaja
    name = req.params.get("name")

    # If no name is provided, use "Developer".
    if not name:
        name = "Developer"

    # Prepare the response message.
    message = (
        f"Hello {name}!\n"
        "Dei Ramesh Avolothan unaku.\n"
        "I am learning Azure Functions and GitHub Actions."
    )

    # Return the response to the browser.
    return func.HttpResponse(
        message,
        status_code=200
    )
