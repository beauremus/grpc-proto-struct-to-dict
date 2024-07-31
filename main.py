#!/usr/bin/env python3

from bosdyn.api import data_acquisition_pb2
from google.protobuf.json_format import MessageToDict
from google.protobuf.struct_pb2 import Struct


def main():
    # Create action_id
    action_id = data_acquisition_pb2.CaptureActionId()
    action_id.action_name = "beaction"
    action_id.group_name = "greaup"

    # Create metadata
    struct = Struct()
    struct.update({"blah": "arb text", "second": [2, 12]})
    metadata = data_acquisition_pb2.Metadata(data=struct)

    # Create Plugin data request
    request = data_acquisition_pb2.AcquirePluginDataRequest(
        action_id=action_id, metadata=metadata
    )

    # Convert request metadata to a dictionary
    output = MessageToDict(request.metadata.data)

    # Access the "blah" field of the metadata and print it
    print(output["blah"])


if __name__ == "__main__":
    main()
