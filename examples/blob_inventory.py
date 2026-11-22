"""List blobs and sizes in an Azure container.

Usage: pip install azure-storage-blob
       export AZURE_STORAGE_CONNECTION_STRING='...'
       python examples/blob_inventory.py my-container
Credentials remain in environment variables; never commit them.
"""
import argparse
import os


def list_blobs(container_name: str) -> list[dict[str, object]]:
    from azure.storage.blob import BlobServiceClient
    connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    client = BlobServiceClient.from_connection_string(connection_string)
    container = client.get_container_client(container_name)
    return [{"name": item.name, "size_bytes": item.size}
            for item in container.list_blobs()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("container")
    args = parser.parse_args()
    for blob in list_blobs(args.container):
        print(f"{blob['size_bytes']:>12}  {blob['name']}")
