# Understanding Boston Dynamics Metadata Payload

When providing unofficially supported data from a system on Spot, information is provided to users in a protobuf `Struct` which is generically formed JSON.

This is a strategy for parsing and accessing that data in a first-class manner in Python.

## Install

```sh
python -m pip install -r requirements.txt
```

## Run

This is a simple example that build a message and then prints the output from accessing the resulting Python dictionary.

```sh
python main.py
```

Out of the box, this results in `"arb text"` being output.

