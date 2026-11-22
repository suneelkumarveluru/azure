# Azure Data Engineering Examples

Practical examples for working with Azure services using environment-based authentication.

## Azure Blob Storage inventory

```bash
python -m pip install azure-storage-blob
export AZURE_STORAGE_CONNECTION_STRING="your-connection-string"
python examples/blob_inventory.py my-container
```

In Windows PowerShell, use `$env:AZURE_STORAGE_CONNECTION_STRING = "your-connection-string"` instead of `export`.

Prints the names and sizes of blobs in a container. Use scoped credentials or managed identity for production; never commit connection strings. Requires a live Azure Storage account for execution.
