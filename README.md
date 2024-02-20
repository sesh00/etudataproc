# EtuDataProc

![PyPI](https://img.shields.io/pypi/v/etudataproc?color=orange) ![Python 3.6, 3.7, 3.8](https://img.shields.io/pypi/pyversions/etudataproc?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/sesh00/etudataproc?color=blueviolet) ![License](https://img.shields.io/pypi/l/d?color=blueviolet) 

EtuDataProc is a Python library designed to simplify interaction with a queue service API. It provides methods for authentication, sending codes to the queue, retrieving results, checking queue positions, and canceling tasks. This README serves as a guide to using the QueueClient library effectively.

## Installation

Install the current version with [PyPI](https://pypi.org/project/etudataproc):

```bash
pip install etudataproc
```

Or from Github:
```bash
pip install https://github.com/sesh00/etudataproc/archive/main.zip
```

## Usage
### Importing the QueueClient

To use QueueClient in your Python code, import it as follows:


```python
from etudataproc import QueueClient
```
### Initializing the QueueClient

You can initialize a QueueClient object by providing the base URL of the queue service and optionally the authentication token.

```python
queue_client = QueueClient(base_url="https://your-queue-service-url.com", token="your-auth-token")
```

### Authentication
You can authenticate with the queue service using your username and password.

```python
queue_client.authenticate(username="your-username", password="your-password")
```

### Sending Code to the Queue
To send a code to the queue, use the ```send_code()``` method.

```python
code = "your-code-to-be-sent"
queue_client.send_code(code)
```
### Retrieving Result
To retrieve the result of a task from the queue, use the ```get_result()``` method.

```python
result = queue_client.get_result()
```

### Checking Queue Position
You can check your position in the queue using the ```get_queue_position()``` method.
```python
position = queue_client.get_queue_position()
```

### Canceling Task
To cancel a task in the queue, use the ```cancel_task()``` method.
queue_client.cancel_task()
```python
queue_client.cancel_task()
```
## Error Handling
If authentication or token-related errors occur, QueueClient raises an Exception with an appropriate error message. Ensure to handle these exceptions appropriately in your code.

## Example
Here's a simple example demonstrating the usage of QueueClient:

```python
from etudataproc import QueueClient

queue_client = QueueClient(base_url="https://your-queue-service-url.com")
queue_client.authenticate(username="your-username", password="your-password")

code = "your-code-to-be-sent"
queue_client.send_code(code)

result = queue_client.get_result()
print("Task Result:", result)

position = queue_client.get_queue_position()
print("Queue Position:", position)

queue_client.cancel_task()

```


## Contributing

Contributions to EtuDataProc are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.


## License

The module is available as open source under the terms of the [MIT License](https://opensource.org/licenses/mit)

